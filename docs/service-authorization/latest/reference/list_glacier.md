

# Actions, resources, and condition keys for Amazon S3 Glacier
<a name="list_glacier"></a>

Amazon S3 Glacier (service prefix: `glacier`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/amazonglacier/latest/dev/).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/amazonglacier/latest/dev/amazon-glacier-api.html).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/amazonglacier/latest/dev/security-iam.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/glacier/glacier.json) for this service.

**Topics**
+ [API operations defined by Amazon S3 Glacier](#list_glacier-operations)
+ [Actions defined by Amazon S3 Glacier](#list_glacier-actions-as-permissions)
+ [Resource types defined by Amazon S3 Glacier](#list_glacier-resources-for-iam-policies)
+ [Condition keys for Amazon S3 Glacier](#list_glacier-policy-keys)

## API operations defined by Amazon S3 Glacier
<a name="list_glacier-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_glacier-actions-as-permissions).




- **   AbortMultipartUpload  **
  - **IAM action:**  [glacier:AbortMultipartUpload](#list_glacier-action-AbortMultipartUpload) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   AbortVaultLock  **
  - **IAM action:**  [glacier:AbortVaultLock](#list_glacier-action-AbortVaultLock) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Permissions management, Write

- **   AddTagsToVault  **
  - **IAM action:**  [glacier:AddTagsToVault](#list_glacier-action-AddTagsToVault) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   CompleteMultipartUpload  **
  - **IAM action:**  [glacier:CompleteMultipartUpload](#list_glacier-action-CompleteMultipartUpload) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CompleteVaultLock  **
  - **IAM action:**  [glacier:CompleteVaultLock](#list_glacier-action-CompleteVaultLock) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Permissions management, Write

- **   CreateVault  **
  - **IAM action:**  [glacier:CreateVault](#list_glacier-action-CreateVault) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteArchive  **
  - **IAM action:**  [glacier:DeleteArchive](#list_glacier-action-DeleteArchive) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteVault  **
  - **IAM action:**  [glacier:DeleteVault](#list_glacier-action-DeleteVault) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteVaultAccessPolicy  **
  - **IAM action:**  [glacier:DeleteVaultAccessPolicy](#list_glacier-action-DeleteVaultAccessPolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Permissions management, Write

- **   DeleteVaultNotifications  **
  - **IAM action:**  [glacier:DeleteVaultNotifications](#list_glacier-action-DeleteVaultNotifications) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DescribeJob  **
  - **IAM action:**  [glacier:DescribeJob](#list_glacier-action-DescribeJob) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeVault  **
  - **IAM action:**  [glacier:DescribeVault](#list_glacier-action-DescribeVault) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetDataRetrievalPolicy  **
  - **IAM action:**  [glacier:GetDataRetrievalPolicy](#list_glacier-action-GetDataRetrievalPolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetJobOutput  **
  - **IAM action:**  [glacier:GetJobOutput](#list_glacier-action-GetJobOutput) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetVaultAccessPolicy  **
  - **IAM action:**  [glacier:GetVaultAccessPolicy](#list_glacier-action-GetVaultAccessPolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetVaultLock  **
  - **IAM action:**  [glacier:GetVaultLock](#list_glacier-action-GetVaultLock) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetVaultNotifications  **
  - **IAM action:**  [glacier:GetVaultNotifications](#list_glacier-action-GetVaultNotifications) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   InitiateJob  **
  - **IAM action:**  [glacier:GetJobOutput](#list_glacier-action-GetJobOutput)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [glacier:InitiateJob](#list_glacier-action-InitiateJob)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   InitiateMultipartUpload  **
  - **IAM action:**  [glacier:InitiateMultipartUpload](#list_glacier-action-InitiateMultipartUpload) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   InitiateVaultLock  **
  - **IAM action:**  [glacier:InitiateVaultLock](#list_glacier-action-InitiateVaultLock) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Permissions management, Write

- **   ListJobs  **
  - **IAM action:**  [glacier:ListJobs](#list_glacier-action-ListJobs) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListMultipartUploads  **
  - **IAM action:**  [glacier:ListMultipartUploads](#list_glacier-action-ListMultipartUploads) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListParts  **
  - **IAM action:**  [glacier:ListParts](#list_glacier-action-ListParts) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListProvisionedCapacity  **
  - **IAM action:**  [glacier:ListProvisionedCapacity](#list_glacier-action-ListProvisionedCapacity) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListTagsForVault  **
  - **IAM action:**  [glacier:ListTagsForVault](#list_glacier-action-ListTagsForVault) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListVaults  **
  - **IAM action:**  [glacier:ListVaults](#list_glacier-action-ListVaults) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   PurchaseProvisionedCapacity  **
  - **IAM action:**  [glacier:PurchaseProvisionedCapacity](#list_glacier-action-PurchaseProvisionedCapacity) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   RemoveTagsFromVault  **
  - **IAM action:**  [glacier:RemoveTagsFromVault](#list_glacier-action-RemoveTagsFromVault) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   SetDataRetrievalPolicy  **
  - **IAM action:**  [glacier:SetDataRetrievalPolicy](#list_glacier-action-SetDataRetrievalPolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Permissions management, Write

- **   SetVaultAccessPolicy  **
  - **IAM action:**  [glacier:SetVaultAccessPolicy](#list_glacier-action-SetVaultAccessPolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Permissions management, Write

- **   SetVaultNotifications  **
  - **IAM action:**  [glacier:SetVaultNotifications](#list_glacier-action-SetVaultNotifications) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UploadArchive  **
  - **IAM action:**  [glacier:UploadArchive](#list_glacier-action-UploadArchive) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UploadMultipartPart  **
  - **IAM action:**  [glacier:UploadMultipartPart](#list_glacier-action-UploadMultipartPart) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write



## Actions defined by Amazon S3 Glacier
<a name="list_glacier-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [AbortMultipartUpload](https://docs.aws.amazon.com/amazonglacier/latest/dev/api-multipart-abort-upload.html)  **
  - **Description:** Grants permission to abort a multipart upload identified by the upload ID
  - **Resource types (\*required):** [vault\*](#list_glacier-resource-vault)
  - **Condition keys:**  
  - **Access level:** Write

- **   [AbortVaultLock](https://docs.aws.amazon.com/amazonglacier/latest/dev/api-AbortVaultLock.html)  **
  - **Description:** Grants permission to abort the vault locking process if the vault lock is not in the Locked state
  - **Resource types (\*required):** [vault\*](#list_glacier-resource-vault)
  - **Condition keys:**  
  - **Access level:** Permissions management, Write

- **   [AddTagsToVault](https://docs.aws.amazon.com/amazonglacier/latest/dev/api-AddTagsToVault.html)  **
  - **Description:** Grants permission to add the specified tags to a vault
  - **Resource types (\*required):** [vault\*](#list_glacier-resource-vault)
  - **Condition keys:**  
  - **Access level:** Tagging, Write

- **   [CompleteMultipartUpload](https://docs.aws.amazon.com/amazonglacier/latest/dev/api-multipart-complete-upload.html)  **
  - **Description:** Grants permission to complete a multipart upload process
  - **Resource types (\*required):** [vault\*](#list_glacier-resource-vault)
  - **Condition keys:**  
  - **Access level:** Write

- **   [CompleteVaultLock](https://docs.aws.amazon.com/amazonglacier/latest/dev/api-CompleteVaultLock.html)  **
  - **Description:** Grants permission to complete the vault locking process
  - **Resource types (\*required):** [vault\*](#list_glacier-resource-vault)
  - **Condition keys:**  
  - **Access level:** Permissions management, Write

- **   [CreateVault](https://docs.aws.amazon.com/amazonglacier/latest/dev/api-vault-put.html)  **
  - **Description:** Grants permission to create a new vault with the specified name
  - **Resource types (\*required):** [vault\*](#list_glacier-resource-vault)
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteArchive](https://docs.aws.amazon.com/amazonglacier/latest/dev/api-archive-delete.html)  **
  - **Description:** Grants permission to delete an archive from a vault
  - **Resource types (\*required):** [vault\*](#list_glacier-resource-vault)
  - **Condition keys:** [glacier:ArchiveAgeInDays](#list_glacier-glacier_ArchiveAgeInDays)
  - **Access level:** Write

- **   [DeleteVault](https://docs.aws.amazon.com/amazonglacier/latest/dev/api-vault-delete.html)  **
  - **Description:** Grants permission to delete a vault
  - **Resource types (\*required):** [vault\*](#list_glacier-resource-vault)
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteVaultAccessPolicy](https://docs.aws.amazon.com/amazonglacier/latest/dev/api-DeleteVaultAccessPolicy.html)  **
  - **Description:** Grants permission to delete the access policy associated with the specified vault
  - **Resource types (\*required):** [vault\*](#list_glacier-resource-vault)
  - **Condition keys:**  
  - **Access level:** Permissions management, Write

- **   [DeleteVaultNotifications](https://docs.aws.amazon.com/amazonglacier/latest/dev/api-vault-notifications-delete.html)  **
  - **Description:** Grants permission to delete the notification configuration set for a vault
  - **Resource types (\*required):** [vault\*](#list_glacier-resource-vault)
  - **Condition keys:**  
  - **Access level:** Write

- **   [DescribeJob](https://docs.aws.amazon.com/amazonglacier/latest/dev/api-describe-job-get.html)  **
  - **Description:** Grants permission to get information about a job previously initiated
  - **Resource types (\*required):** [vault\*](#list_glacier-resource-vault)
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeVault](https://docs.aws.amazon.com/amazonglacier/latest/dev/api-vault-get.html)  **
  - **Description:** Grants permission to get information about a vault
  - **Resource types (\*required):** [vault\*](#list_glacier-resource-vault)
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetDataRetrievalPolicy](https://docs.aws.amazon.com/amazonglacier/latest/dev/api-GetDataRetrievalPolicy.html)  **
  - **Description:** Grants permission to get the data retrieval policy
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetJobOutput](https://docs.aws.amazon.com/amazonglacier/latest/dev/api-job-output-get.html)  **
  - **Description:** Grants permission to download the output of the job specified
  - **Resource types (\*required):** [vault\*](#list_glacier-resource-vault)
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetVaultAccessPolicy](https://docs.aws.amazon.com/amazonglacier/latest/dev/api-GetVaultAccessPolicy.html)  **
  - **Description:** Grants permission to retrieve the access-policy subresource set on the vault
  - **Resource types (\*required):** [vault\*](#list_glacier-resource-vault)
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetVaultLock](https://docs.aws.amazon.com/amazonglacier/latest/dev/api-GetVaultLock.html)  **
  - **Description:** Grants permission to retrieve attributes from the lock-policy subresource set on the specified vault
  - **Resource types (\*required):** [vault\*](#list_glacier-resource-vault)
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetVaultNotifications](https://docs.aws.amazon.com/amazonglacier/latest/dev/api-vault-notifications-get.html)  **
  - **Description:** Grants permission to retrieve the notification-configuration subresource set on the vault
  - **Resource types (\*required):** [vault\*](#list_glacier-resource-vault)
  - **Condition keys:**  
  - **Access level:** Read

- **   [InitiateJob](https://docs.aws.amazon.com/amazonglacier/latest/dev/api-initiate-job-post.html)  **
  - **Description:** Grants permission to initiate a job of the specified type
  - **Resource types (\*required):** [vault\*](#list_glacier-resource-vault)
  - **Condition keys:** [glacier:ArchiveAgeInDays](#list_glacier-glacier_ArchiveAgeInDays)
  - **Access level:** Write

- **   [InitiateMultipartUpload](https://docs.aws.amazon.com/amazonglacier/latest/dev/api-multipart-initiate-upload.html)  **
  - **Description:** Grants permission to initiate a multipart upload
  - **Resource types (\*required):** [vault\*](#list_glacier-resource-vault)
  - **Condition keys:**  
  - **Access level:** Write

- **   [InitiateVaultLock](https://docs.aws.amazon.com/amazonglacier/latest/dev/api-InitiateVaultLock.html)  **
  - **Description:** Grants permission to initiate the vault locking process
  - **Resource types (\*required):** [vault\*](#list_glacier-resource-vault)
  - **Condition keys:**  
  - **Access level:** Permissions management, Write

- **   [ListJobs](https://docs.aws.amazon.com/amazonglacier/latest/dev/api-jobs-get.html)  **
  - **Description:** Grants permission to list jobs for a vault that are in-progress and jobs that have recently finished
  - **Resource types (\*required):** [vault\*](#list_glacier-resource-vault)
  - **Condition keys:**  
  - **Access level:** List

- **   [ListMultipartUploads](https://docs.aws.amazon.com/amazonglacier/latest/dev/api-multipart-list-uploads.html)  **
  - **Description:** Grants permission to list in-progress multipart uploads for the specified vault
  - **Resource types (\*required):** [vault\*](#list_glacier-resource-vault)
  - **Condition keys:**  
  - **Access level:** List

- **   [ListParts](https://docs.aws.amazon.com/amazonglacier/latest/dev/api-multipart-list-parts.html)  **
  - **Description:** Grants permission to list the parts of an archive that have been uploaded in a specific multipart upload
  - **Resource types (\*required):** [vault\*](#list_glacier-resource-vault)
  - **Condition keys:**  
  - **Access level:** List

- **   [ListProvisionedCapacity](https://docs.aws.amazon.com/amazonglacier/latest/dev/api-ListProvisionedCapacity.html)  **
  - **Description:** Grants permission to list the provisioned capacity for the specified AWS account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListTagsForVault](https://docs.aws.amazon.com/amazonglacier/latest/dev/api-ListTagsForVault.html)  **
  - **Description:** Grants permission to list all the tags attached to a vault
  - **Resource types (\*required):** [vault\*](#list_glacier-resource-vault)
  - **Condition keys:**  
  - **Access level:** List

- **   [ListVaults](https://docs.aws.amazon.com/amazonglacier/latest/dev/api-vaults-get.html)  **
  - **Description:** Grants permission to list all vaults
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [PurchaseProvisionedCapacity](https://docs.aws.amazon.com/amazonglacier/latest/dev/api-PurchaseProvisionedCapacity.html)  **
  - **Description:** Grants permission to purchases a provisioned capacity unit for an AWS account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [RemoveTagsFromVault](https://docs.aws.amazon.com/amazonglacier/latest/dev/api-RemoveTagsFromVault.html)  **
  - **Description:** Grants permission to remove one or more tags from the set of tags attached to a vault
  - **Resource types (\*required):** [vault\*](#list_glacier-resource-vault)
  - **Condition keys:**  
  - **Access level:** Tagging, Write

- **   [SetDataRetrievalPolicy](https://docs.aws.amazon.com/amazonglacier/latest/dev/api-SetDataRetrievalPolicy.html)  **
  - **Description:** Grants permission to set and then enacts a data retrieval policy in the region specified in the PUT request
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Permissions management, Write

- **   [SetVaultAccessPolicy](https://docs.aws.amazon.com/amazonglacier/latest/dev/api-SetVaultAccessPolicy.html)  **
  - **Description:** Grants permission to configure an access policy for a vault; will overwrite an existing policy
  - **Resource types (\*required):** [vault\*](#list_glacier-resource-vault)
  - **Condition keys:**  
  - **Access level:** Permissions management, Write

- **   [SetVaultNotifications](https://docs.aws.amazon.com/amazonglacier/latest/dev/api-vault-notifications-put.html)  **
  - **Description:** Grants permission to configure vault notifications
  - **Resource types (\*required):** [vault\*](#list_glacier-resource-vault)
  - **Condition keys:**  
  - **Access level:** Write

- **   [UploadArchive](https://docs.aws.amazon.com/amazonglacier/latest/dev/api-archive-post.html)  **
  - **Description:** Grants permission to upload an archive to a vault
  - **Resource types (\*required):** [vault\*](#list_glacier-resource-vault)
  - **Condition keys:**  
  - **Access level:** Write

- **   [UploadMultipartPart](https://docs.aws.amazon.com/amazonglacier/latest/dev/api-upload-part.html)  **
  - **Description:** Grants permission to upload a part of an archive
  - **Resource types (\*required):** [vault\*](#list_glacier-resource-vault)
  - **Condition keys:**  
  - **Access level:** Write



## Resource types defined by Amazon S3 Glacier
<a name="list_glacier-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [vault](https://docs.aws.amazon.com/amazonglacier/latest/dev/working-with-vaults.html)  | arn:${Partition}:glacier:${Region}:${Account}:vaults/${VaultName} |   | 

## Condition keys for Amazon S3 Glacier
<a name="list_glacier-policy-keys"></a>

Amazon S3 Glacier defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [glacier:ArchiveAgeInDays](https://docs.aws.amazon.com/amazonglacier/latest/dev/security_iam_service-with-iam.html#security_iam_service-with-iam-id-based-policies-conditionkeys)  | Filters access by how long an archive has been stored in the vault, in days | String | 
|   [glacier:ResourceTag/](https://docs.aws.amazon.com/amazonglacier/latest/dev/security_iam_service-with-iam.html#security_iam_service-with-iam-tags)  | Filters access by a customer-defined tag | String | 