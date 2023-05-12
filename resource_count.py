from google.auth import compute_engine
from google.cloud import compute_v1

# Authenticate using the default credentials on the Compute Engine instance
credentials = compute_engine.Credentials()

# Create a Compute Engine client
compute_client = compute_v1.InstancesClient(credentials=credentials)

# Define the project and zone for your Compute Engine instance
project = 'my-project-id'
zone = 'us-central1-a'

# Get a list of all instances in the specified project and zone
instances = compute_client.list(project=project, zone=zone)

# Count the total number of CPUs used by all instances
total_cpus = 0
for instance in instances:
    total_cpus += instance.machine_type.virtual_cpus

# Print the total number of CPUs used by all instances
print(f"Total CPUs used in project {project} and zone {zone}: {total_cpus}")



# from google.cloud import compute
# from google.cloud import compute_v1

# # Create a Compute Engine client object
# compute_client = compute_v1.InstancesClient()

# # Get the list of instances in the project
# project_id = 'online-legacy-web'
# zone = 'europe-west1-b'
# instances = compute_client.list(project=project_id, zone=zone)

# # Count the number of CPU cores, memory RAM, and disks provisioned
# cpu_cores = 0
# memory_ram = 0
# disk_count = 0
# for instance in instances:
#     for cpu in instance.machine_type.virtual_cpus:
#         cpu_cores += cpu
#     memory_ram += instance.machine_type.memory_mb
#     for disk in instance.disks:
#         disk_count += 1

# print(f'CPU cores: {cpu_cores}')
# print(f'Memory RAM: {memory_ram} MB')
# print(f'Disk count: {disk_count}')