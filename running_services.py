from datetime import datetime, timedelta
from google.cloud import logging_v2

# Set the GCP project ID
project_id = "online-legacy-web"

# Set the name of the log to query
log_name = "cloudaudit.googleapis.com%2Factivity"

# Create a logging client
#logging_client = logging_v2.LoggingServiceV2Client()
client = logging_v2.Client(project=project_id)


# Set the filter for the log query to only include logs from the past hour
timestamp_format = "%Y-%m-%dT%H:%M:%S.%fZ"
start_time = (datetime.utcnow() - timedelta(hours=6)).strftime(timestamp_format)
filter_str = f'logName="projects/{project_id}/logs/{log_name}" AND timestamp>="{start_time}"'

try: 
    # Execute the log query
    response = client.list_entries(filter_=filter_str)

    # Extract the unique service names and their labels from the log entries
    services = {}
    for entry in response:
        if "service_name" in entry.resource.labels:
            service_name = entry.resource.labels["service_name"]
            if service_name not in services:
                services[service_name] = set()
            if entry.labels is not None:
                for key, value in entry.labels.items():
                    if key.startswith("labels.") and key != "labels.resource_type":
                        label_key = key[len("labels."):]
                        services[service_name].add((label_key, value))

    # Print the list of running services and their labels
    print("Running services:")
    if len(services) == 0:
        print("No running services found.")
    for service_name, labels in services.items():
        print(f"{service_name}:")
        for label_key, label_value in labels:
            print(f"\t{label_key}: {label_value}")

except GoogleAPIError as e:
    print(f"Error executing log query: {e}")