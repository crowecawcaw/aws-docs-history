

# Manage tags using the CLI or API
<a name="tag-resources-api-sdk"></a>

Use the following AWS CLI commands or AWS Batch API operations to add, update, list, and delete the tags for your resources.


**Tag support for AWS Batch resources**  

| Task | API action | AWS CLI | AWS Tools for Windows PowerShell | 
| --- | --- | --- | --- | 
| Add or overwrite one or more tags. | [TagResource](https://docs.aws.amazon.com/batch/latest/APIReference/API_TagResource.html) | [tag-resource](https://docs.aws.amazon.com/cli/latest/reference/batch/tag-resource.html) | [Add-BATResourceTag](https://docs.aws.amazon.com/powershell/latest/reference/items/Add-BATResourceTag.html) | 
| Delete one or more tags. | [UntagResource](https://docs.aws.amazon.com/batch/latest/APIReference/API_UntagResource.html) | [untag-resource](https://docs.aws.amazon.com/cli/latest/reference/batch/untag-resource.html) | [Remove-BATResourceTag](https://docs.aws.amazon.com/powershell/latest/reference/items/Remove-BATResourceTag.html) | 
| List tags for a resource | [ListTagsForResource](https://docs.aws.amazon.com/batch/latest/APIReference/API_ListTagsForResource.html) | [list-tags-for-resource](https://docs.aws.amazon.com/cli/latest/reference/batch/list-tags-for-resource.html) | [Get-BATResourceTag](https://docs.aws.amazon.com/powershell/latest/reference/items/Get-BATResourceTag.html) | 

The following examples show how to tag or untag resources using the AWS CLI.

**Example 1: Tag an existing resource**  
The following command tags an existing resource.

```
aws batch tag-resource --resource-arn {{resource_ARN}} --tags {{team}}={{devs}}
```

**Example 2: Untag an existing resource**  
The following command deletes a tag from an existing resource.

```
aws batch untag-resource --resource-arn {{resource_ARN}} --tag-keys {{tag_key}}
```

**Example 3: List tags for a resource**  
The following command lists the tags associated with an existing resource.

```
aws batch list-tags-for-resource --resource-arn {{resource_ARN}}
```

Some resource-creating actions enable you to specify tags when you create the resource. The following actions support tagging on creation.


| Task | API action | AWS CLI | AWS Tools for Windows PowerShell | 
| --- | --- | --- | --- | 
| Create a compute environment | [CreateComputeEnvironment](https://docs.aws.amazon.com/batch/latest/APIReference/API_CreateComputeEnvironment.html) | [create-compute-environment](https://docs.aws.amazon.com/cli/latest/reference/batch/create-compute-environment.html) | [New-BATComputeEnvironment](https://docs.aws.amazon.com/powershell/latest/reference/items/New-BATComputeEnvironment.html) | 
| Create a job queue | [CreateJobQueue](https://docs.aws.amazon.com/batch/latest/APIReference/API_CreateJobQueue.html) | [create-job-queue](https://docs.aws.amazon.com/cli/latest/reference/batch/create-job-queue.html) | [New-BATJobQueue](https://docs.aws.amazon.com/powershell/latest/reference/items/New-BATJobQueue.html) | 
| Create a scheduling policy | [CreateSchedulingPolicy](https://docs.aws.amazon.com/batch/latest/APIReference/API_CreateSchedulingPolicy.html) | [create-scheduling-policy](https://docs.aws.amazon.com/cli/latest/reference/batch/create-scheduling-policy.html) | [New-BATSchedulingPolicy](https://docs.aws.amazon.com/powershell/latest/reference/items/New-BATSchedulingPolicy.html) | 
| Register a job definition | [RegisterJobDefinition](https://docs.aws.amazon.com/batch/latest/APIReference/API_RegisterJobDefinition.html) | [register-job-definition](https://docs.aws.amazon.com/cli/latest/reference/batch/register-job-definition.html) | [Register-BATJobDefinition](https://docs.aws.amazon.com/powershell/latest/reference/items/Register-BATJobDefinition.html) | 
| Submit a job | [SubmitJob](https://docs.aws.amazon.com/batch/latest/APIReference/API_SubmitJob.html) | [submit-job](https://docs.aws.amazon.com/cli/latest/reference/batch/submit-job.html) | [Submit-BATJob](https://docs.aws.amazon.com/powershell/latest/reference/items/Submit-BATJob.html) | 
| Create a consumable resource | [CreateConsumableResource](https://docs.aws.amazon.com/batch/latest/APIReference/API_CreateConsumableResource.html) | [create-consumable-resource](https://docs.aws.amazon.com/cli/latest/reference/batch/create-consumable-resource.html) | [New-BATConsumableResource](https://docs.aws.amazon.com/powershell/latest/reference/items/New-BATConsumableResource.html) | 
| Create a service environment | [CreateServiceEnvironment](https://docs.aws.amazon.com/batch/latest/APIReference/API_CreateServiceEnvironment.html) | [create-service-environment](https://docs.aws.amazon.com/cli/latest/reference/batch/create-service-environment.html) | [New-BATServiceEnvironment](https://docs.aws.amazon.com/powershell/latest/reference/items/New-BATServiceEnvironment.html) | 
| Create a quota share | [CreateQuotaShare](https://docs.aws.amazon.com/batch/latest/APIReference/API_CreateQuotaShare.html) | [create-quota-share](https://docs.aws.amazon.com/cli/latest/reference/batch/create-quota-share.html) | [New-BATQuotaShare](https://docs.aws.amazon.com/powershell/latest/reference/items/New-BATQuotaShare.html) | 