from google.cloud import compute_v1

def get_load_balancer_creation_dates(project_id):
    # Authenticate using the default credentials

    # Create a compute client
    client = compute_v1.ForwardingRulesClient()

    # Retrieve the list of load balancers
    load_balancers = client.list(project=project_id, region='global')

    # Iterate over the load balancers and extract their creation dates
    creation_dates = []
    for load_balancer in load_balancers:
        creation_dates.append((load_balancer.name, load_balancer.creation_timestamp))

    return creation_dates

# Replace 'your-project-id' with your actual GCP project ID
project_id = 'corp'
creation_dates = get_load_balancer_creation_dates(project_id)

# Print the load balancer names and their creation dates
for load_balancer, creation_date in creation_dates:
    print(f"Load Balancer: {load_balancer}")
    print(f"Creation Date: {creation_date}")
    print()
