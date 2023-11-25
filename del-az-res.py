from azure.identity import ClientSecretCredential
from azure.mgmt.resource import ResourceManagementClient

def delete_all_resources(subscription_id, client_id, client_secret, tenant_id):
    # Create a ClientSecretCredential using explicit credentials
    credential = ClientSecretCredential(
        client_id=client_id,
        client_secret=client_secret,
        tenant_id=tenant_id
    )

    # Create a ResourceManagementClient using the credential
    resource_client = ResourceManagementClient(credential, subscription_id)

    # Get all resource groups in the subscription
    resource_groups = resource_client.resource_groups.list()

    for rg in resource_groups:
        print(f"Deleting resource group: {rg.name}")
        resource_client.resource_groups.begin_delete(rg.name).wait()

if __name__ == "__main__":
    # Replace these values with your actual Azure subscription and application (service principal) details
    subscription_id = "your-subscription-id"
    client_id = "your-client-id"
    client_secret = "your-client-secret"
    tenant_id = "your-tenant-id"

    delete_all_resources(subscription_id, client_id, client_secret, tenant_id)
