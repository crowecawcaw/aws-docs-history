# Actions, resources, and condition keys for AWS Import Export Disk Service

AWS Import Export Disk Service (service prefix: `importexport`) provides the following
service-specific operations, resources, actions, and condition keys for use in IAM permission
policies.

References:

- Learn how to [configure this service](../../../AWSImportExport/latest/DG.md "../../../AWSImportExport/latest/DG.md").
- View a list of the [API operations available for
  this service](../../../AWSImportExport/latest/DG/api-reference.md "../../../AWSImportExport/latest/DG/api-reference.md").
- Learn how to secure this service and its resources by
  [using IAM](../../../AWSImportExport/latest/DG/using-iam.md "../../../AWSImportExport/latest/DG/using-iam.md") permission policies.
- View the [programmatic service authorization
  reference](https://servicereference.us-east-1.amazonaws.com/v1/importexport/importexport.json "https://servicereference.us-east-1.amazonaws.com/v1/importexport/importexport.json") for this service.

###### Topics

- [Actions defined by AWS Import Export Disk Service](#list_importexport-actions-as-permissions "#list_importexport-actions-as-permissions")
- [Resource types defined by AWS Import Export Disk Service](#list_importexport-resources-for-iam-policies "#list_importexport-resources-for-iam-policies")
- [Condition keys for AWS Import Export Disk Service](#list_importexport-policy-keys "#list_importexport-policy-keys")

## Actions defined by AWS Import Export Disk Service

You can specify the following actions in the `Action` element of an IAM
policy statement. Use policies to grant permissions to perform an operation in AWS. When
you use an action in a policy, you usually allow or deny access to the API operation or CLI
command with the same name. However, in some cases, a single action controls access to more
than one operation. Alternatively, some operations require several different actions.

| Actions                                                                                                                                   | Description                                                                                                                                                                     | Resource types (\*required) | Condition keys | Access level |
| ----------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------- | -------------- | ------------ |
| [CancelJob](../../../AWSImportExport/latest/DG/WebCancelJob.md "../../../AWSImportExport/latest/DG/WebCancelJob.md")                      | This action cancels a specified job. Only the job owner can cancel it. The action fails if the job has already started or is complete.                                          |                             |                | Write        |
| [CreateJob](../../../AWSImportExport/latest/DG/WebCreateJob.md "../../../AWSImportExport/latest/DG/WebCreateJob.md")                      | This action initiates the process of scheduling an upload or download of your data.                                                                                             |                             |                | Write        |
| [GetShippingLabel](../../../AWSImportExport/latest/DG/WebGetShippingLabel.md "../../../AWSImportExport/latest/DG/WebGetShippingLabel.md") | This action generates a pre-paid shipping label that you will use to ship your device to AWS for processing.                                                                    |                             |                | Read         |
| [GetStatus](../../../AWSImportExport/latest/DG/WebGetStatus.md "../../../AWSImportExport/latest/DG/WebGetStatus.md")                      | This action returns information about a job, including where the job is in the processing pipeline, the status of the results, and the signature value associated with the job. |                             |                | Read         |
| [ListJobs](../../../AWSImportExport/latest/DG/WebListJobs.md "../../../AWSImportExport/latest/DG/WebListJobs.md")                         | This action returns the jobs associated with the requester.                                                                                                                     |                             |                | List         |
| [UpdateJob](../../../AWSImportExport/latest/DG/WebUpdateJob.md "../../../AWSImportExport/latest/DG/WebUpdateJob.md")                      | You use this action to change the parameters specified in the original manifest file by supplying a new manifest file.                                                          |                             |                | Write        |

## Resource types defined by AWS Import Export Disk Service

AWS Import Export Disk Service does not support specifying a resource ARN in the
`Resource` element of an IAM policy statement.

## Condition keys for AWS Import Export Disk Service

AWS Import Export Disk Service has no service-specific condition keys that can be used in the
`Condition` element of policy statements.
