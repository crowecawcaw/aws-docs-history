

# Parameter types for Azure and Google Cloud resources

Automation runbooks can declare parameters that use the following types to identify a Cloud Connector, a Microsoft Azure resource, or a Google Cloud resource. When an execution starts, Automation validates each input value against the type's pattern.
+ Systems Manager matches type strings exactly, including their mixed casing. For example, `microsoft.Compute/VirtualMachines` starts with a lowercase `m`, but `Microsoft.Storage/storageAccounts/blobServices/containers` starts with an uppercase `M`. A type string with the wrong casing isn't recognized.
+ Azure resource ID values are matched case-insensitively.
+ In the Automation console, a parameter of type `AWS::SSM::CloudConnector::Id` is a connector list (**Choose or enter a Cloud Connector ID**). An Azure virtual machine (VM) input shows a typed field with a format hint. For Azure types other than blob containers and managed identities, the Azure picker is available after you sign in with Azure sign-in. Google Cloud inputs are typed fields. For Azure sign-in, see [Choosing Azure resources with Azure sign-in](automation-azure-sign-in.md).

## Cloud Connector type
<a name="automation-multicloud-parameter-types-connector"></a>


| Type | Base type | Value format | Description | 
| --- | --- | --- | --- | 
| AWS::SSM::CloudConnector::Id | String | a1b2c3d4-5678-90ab-cdef-EXAMPLE11111 | The ID of a Cloud Connector, as a GUID. | 

## Azure types
<a name="automation-multicloud-parameter-types-azure"></a>

Azure values are full Azure Resource Manager (ARM) resource IDs. In the examples, replace the placeholders with your subscription ID, resource group, and resource names.


| Type | Base type | Value format | Description | 
| --- | --- | --- | --- | 
| microsoft.Compute/VirtualMachines | String | /subscriptions/<subscription-id>/resourceGroups/<resource-group>/providers/Microsoft.Compute/virtualMachines/<vm-name> | An Azure virtual machine. | 
| List<microsoft.Compute/VirtualMachines> | StringList | /subscriptions/<subscription-id>/resourceGroups/<resource-group>/providers/Microsoft.Compute/virtualMachines/<vm-name> | A list of Azure virtual machines. | 
| microsoft.Compute/disks | String | /subscriptions/<subscription-id>/resourceGroups/<resource-group>/providers/Microsoft.Compute/disks/<disk-name> | An Azure managed disk. | 
| microsoft.Compute/virtualMachineScaleSets | String | /subscriptions/<subscription-id>/resourceGroups/<resource-group>/providers/Microsoft.Compute/virtualMachineScaleSets/<scale-set-name> | An Azure virtual machine scale set. | 
| microsoft.Sql/servers | String | /subscriptions/<subscription-id>/resourceGroups/<resource-group>/providers/Microsoft.Sql/servers/<server-name> | An Azure SQL server. | 
| microsoft.Sql/servers/databases | String | /subscriptions/<subscription-id>/resourceGroups/<resource-group>/providers/Microsoft.Sql/servers/<server-name>/databases/<database-name> | An Azure SQL database. | 
| microsoft.Storage/StorageAccounts | String | /subscriptions/<subscription-id>/resourceGroups/<resource-group>/providers/Microsoft.Storage/storageAccounts/<account-name> | An Azure storage account. | 
| Microsoft.Storage/storageAccounts/blobServices/containers | String | /subscriptions/<subscription-id>/resourceGroups/<resource-group>/providers/Microsoft.Storage/storageAccounts/<account-name>/blobServices/default/containers/<container-name> | An Azure blob container. | 
| List<Microsoft.Storage/storageAccounts/blobServices/containers> | StringList | /subscriptions/<subscription-id>/resourceGroups/<resource-group>/providers/Microsoft.Storage/storageAccounts/<account-name>/blobServices/default/containers/<container-name> | A list of Azure blob containers. | 
| microsoft.KeyVault/vaults | String | /subscriptions/<subscription-id>/resourceGroups/<resource-group>/providers/Microsoft.KeyVault/vaults/<vault-name> | An Azure key vault. | 
| microsoft.Web/sites | String | /subscriptions/<subscription-id>/resourceGroups/<resource-group>/providers/Microsoft.Web/sites/<site-name> | An Azure app service. | 
| microsoft.ContainerService/managedClusters | String | /subscriptions/<subscription-id>/resourceGroups/<resource-group>/providers/Microsoft.ContainerService/managedClusters/<cluster-name> | An Azure Kubernetes Service (AKS) cluster. | 
| microsoft.ContainerInstance/containerGroups | String | /subscriptions/<subscription-id>/resourceGroups/<resource-group>/providers/Microsoft.ContainerInstance/containerGroups/<group-name> | An Azure container instance group. | 
| microsoft.ManagedIdentity/userAssignedIdentities | String | /subscriptions/<subscription-id>/resourceGroups/<resource-group>/providers/Microsoft.ManagedIdentity/userAssignedIdentities/<identity-name> | An Azure user-assigned managed identity. | 
| List<microsoft.ManagedIdentity/userAssignedIdentities> | StringList | /subscriptions/<subscription-id>/resourceGroups/<resource-group>/providers/Microsoft.ManagedIdentity/userAssignedIdentities/<identity-name> | A list of Azure user-assigned managed identities. | 

## Google Cloud types
<a name="automation-multicloud-parameter-types-gcp"></a>

Google Cloud values are Cloud Asset Inventory resource names. In the examples, replace the placeholders with your project, zone or location, and resource names.


| Type | Base type | Value format | Description | 
| --- | --- | --- | --- | 
| compute.googleapis.com/Instance | String | projects/<project-id>/zones/<zone>/instances/<instance-name> | A Google Cloud VM instance. | 
| List<compute.googleapis.com/Instance> | StringList | projects/<project-id>/zones/<zone>/instances/<instance-name> | A list of Google Cloud VM instances. | 
| compute.googleapis.com/Disk | String | projects/<project-id>/zones/<zone>/disks/<disk-name> | A Google Cloud disk (zonal or regional). | 
| compute.googleapis.com/InstanceGroup | String | projects/<project-id>/zones/<zone>/instanceGroups/<group-name> | A Google Cloud instance group. | 
| container.googleapis.com/Cluster | String | projects/<project-id>/locations/<location>/clusters/<cluster-name> | A Google Kubernetes Engine (GKE) cluster. | 
| sqladmin.googleapis.com/Instance | String | projects/<project-id>/instances/<instance-name> | A Cloud SQL instance. | 
| run.googleapis.com/Service | String | projects/<project-id>/locations/<location>/services/<service-name> | A Cloud Run service. | 
| cloudfunctions.googleapis.com/CloudFunction | String | projects/<project-id>/locations/<location>/functions/<function-name> | A Cloud Functions function. | 
| bigquery.googleapis.com/Dataset | String | projects/<project-id>/datasets/<dataset-name> | A BigQuery dataset. | 
| pubsub.googleapis.com/Topic | String | projects/<project-id>/topics/<topic-name> | A Pub/Sub topic. | 
| storage.googleapis.com/Bucket | String | <bucket-name> | A Cloud Storage bucket. | 
| List<storage.googleapis.com/Bucket> | StringList | <bucket-name> | A list of Cloud Storage buckets. | 
| iam.googleapis.com/ServiceAccount | String | projects/<project-id>/serviceAccounts/<service-account-email> | A Google Cloud service account. | 
| List<iam.googleapis.com/ServiceAccount> | StringList | projects/<project-id>/serviceAccounts/<service-account-email> | A list of Google Cloud service accounts. | 