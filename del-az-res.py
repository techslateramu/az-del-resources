import os
from azure.identity import DefaultAzureCredential
from azure.mgmt.resource import ResourceManagementClient

# Replace these with your own values
# subscription_id = os.environ.get('AZURE_SUBSCRIPTION_ID')
subscription_id = "d9d24cf2-e4f1-4942-958f-a6bd839a3f1e"


# Create a ResourceManagementClient
resource_client = ResourceManagementClient(DefaultAzureCredential(), subscription_id)


# List all resource groups in the subscription
resource_groups = resource_client.resource_groups.list()

# Iterate through each resource group and delete resources
for resource_group in resource_groups:
    print(f"Deleting resources in resource group: {resource_group.name}")
    
    # List all resources in the resource group
    resources = resource_client.resources.list_by_resource_group(resource_group.name)

    # Delete each resource in the resource group
    for resource in resources:
        print(f"Deleting resource: {resource.name} - Type: {resource.type}")
        
        # Corrected code for deletion
        resource_client.resources.begin_delete_by_id(resource.id, api_version='2023-04-01').wait()

    print("Resource group cleared.")
    
    # Delete the resource group itself
    resource_client.resource_groups.begin_delete(resource_group.name).wait()
    print(f"Resource group {resource_group.name} deleted.")

print("All resources and resource groups in the subscription deleted successfully.")
