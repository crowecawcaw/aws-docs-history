

# Data retrieval APIs for Amazon S3 Glacier
<a name="amazons3glacier"></a>

Amazon S3 Glacier provides the following APIs for data retrieval.



| Actions | Description | Access level | 
| --- | --- | --- | 
| <a name="glacier-DescribeJob"></a>[DescribeJob](https://docs.aws.amazon.com/amazonglacier/latest/dev/api-describe-job-get.html) | Get information about a job previously initiated | Read | 
| <a name="glacier-DescribeVault"></a>[DescribeVault](https://docs.aws.amazon.com/amazonglacier/latest/dev/api-vault-get.html) | Get information about a vault | Read | 
| <a name="glacier-GetDataRetrievalPolicy"></a>[GetDataRetrievalPolicy](https://docs.aws.amazon.com/amazonglacier/latest/dev/api-GetDataRetrievalPolicy.html) | Get the data retrieval policy | Read | 
| <a name="glacier-GetJobOutput"></a>[GetJobOutput](https://docs.aws.amazon.com/amazonglacier/latest/dev/api-job-output-get.html) | Download the output of the job specified | Read | 
| <a name="glacier-GetVaultAccessPolicy"></a>[GetVaultAccessPolicy](https://docs.aws.amazon.com/amazonglacier/latest/dev/api-GetVaultAccessPolicy.html) | Retrieve the access-policy subresource set on the vault | Read | 
| <a name="glacier-GetVaultLock"></a>[GetVaultLock](https://docs.aws.amazon.com/amazonglacier/latest/dev/api-GetVaultLock.html) | Retrieve attributes from the lock-policy subresource set on the specified vault | Read | 
| <a name="glacier-GetVaultNotifications"></a>[GetVaultNotifications](https://docs.aws.amazon.com/amazonglacier/latest/dev/api-vault-notifications-get.html) | Retrieve the notification-configuration subresource set on the vault | Read | 
| <a name="glacier-ListJobs"></a>[ListJobs](https://docs.aws.amazon.com/amazonglacier/latest/dev/api-jobs-get.html) | List jobs for a vault that are in-progress and jobs that have recently finished | List | 
| <a name="glacier-ListMultipartUploads"></a>[ListMultipartUploads](https://docs.aws.amazon.com/amazonglacier/latest/dev/api-multipart-list-uploads.html) | List in-progress multipart uploads for the specified vault | List | 
| <a name="glacier-ListParts"></a>[ListParts](https://docs.aws.amazon.com/amazonglacier/latest/dev/api-multipart-list-parts.html) | List the parts of an archive that have been uploaded in a specific multipart upload | List | 
| <a name="glacier-ListProvisionedCapacity"></a>[ListProvisionedCapacity](https://docs.aws.amazon.com/amazonglacier/latest/dev/api-ListProvisionedCapacity.html) | List the provisioned capacity for the specified AWS account | List | 
| <a name="glacier-ListTagsForVault"></a>[ListTagsForVault](https://docs.aws.amazon.com/amazonglacier/latest/dev/api-ListTagsForVault.html) | List all the tags attached to a vault | List | 
| <a name="glacier-ListVaults"></a>[ListVaults](https://docs.aws.amazon.com/amazonglacier/latest/dev/api-vaults-get.html) | List all vaults | List | 