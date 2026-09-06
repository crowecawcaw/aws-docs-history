

# Actions, resources, and condition keys for AWS Import Export Disk Service
<a name="list_importexport"></a>

AWS Import Export Disk Service (service prefix: `importexport`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/AWSImportExport/latest/DG/).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/AWSImportExport/latest/DG/api-reference.html).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/AWSImportExport/latest/DG/using-iam.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/importexport/importexport.json) for this service.

**Topics**
+ [Actions defined by AWS Import Export Disk Service](#list_importexport-actions-as-permissions)
+ [Resource types defined by AWS Import Export Disk Service](#list_importexport-resources-for-iam-policies)
+ [Condition keys for AWS Import Export Disk Service](#list_importexport-policy-keys)

## Actions defined by AWS Import Export Disk Service
<a name="list_importexport-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.



| Actions | Description | Resource types (\*required) | Condition keys | Access level | 
| --- | --- | --- | --- | --- | 
|   [CancelJob](https://docs.aws.amazon.com/AWSImportExport/latest/DG/WebCancelJob.html)  | This action cancels a specified job. Only the job owner can cancel it. The action fails if the job has already started or is complete. |  |   | Write | 
|   [CreateJob](https://docs.aws.amazon.com/AWSImportExport/latest/DG/WebCreateJob.html)  | This action initiates the process of scheduling an upload or download of your data. |  |   | Write | 
|   [GetShippingLabel](https://docs.aws.amazon.com/AWSImportExport/latest/DG/WebGetShippingLabel.html)  | This action generates a pre-paid shipping label that you will use to ship your device to AWS for processing. |  |   | Read | 
|   [GetStatus](https://docs.aws.amazon.com/AWSImportExport/latest/DG/WebGetStatus.html)  | This action returns information about a job, including where the job is in the processing pipeline, the status of the results, and the signature value associated with the job. |  |   | Read | 
|   [ListJobs](https://docs.aws.amazon.com/AWSImportExport/latest/DG/WebListJobs.html)  | This action returns the jobs associated with the requester. |  |   | List | 
|   [UpdateJob](https://docs.aws.amazon.com/AWSImportExport/latest/DG/WebUpdateJob.html)  | You use this action to change the parameters specified in the original manifest file by supplying a new manifest file. |  |   | Write | 

## Resource types defined by AWS Import Export Disk Service
<a name="list_importexport-resources-for-iam-policies"></a>

AWS Import Export Disk Service does not support specifying a resource ARN in the `Resource` element of an IAM policy statement.

## Condition keys for AWS Import Export Disk Service
<a name="list_importexport-policy-keys"></a>

AWS Import Export Disk Service has no service-specific condition keys that can be used in the `Condition` element of policy statements.