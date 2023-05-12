from google.cloud import asset_v1

# Replace [PROJECT_ID] with the ID of your GCP project
project_id =  '[online-legacy-web]'

# Create the asset client
client = asset_v1.AssetServiceClient()

# Create the parent resource
parent = f'projects/{project_id}'

# Create the request object
request = asset_v1.ListAssetsRequest(
    parent=parent,
    asset_types=['compute.googleapis.com/Instance']
)

# Call the API to list the assets
response = client.list_assets(request)

# Print the name of each asset
for asset in response:
    print(asset.asset.name)