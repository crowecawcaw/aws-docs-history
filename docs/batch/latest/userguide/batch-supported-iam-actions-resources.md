

# Supported resource-level permissions for AWS Batch API actions
<a name="batch-supported-iam-actions-resources"></a>

The term *resource-level permissions* refers to the ability to specify the resources that users are allowed to perform actions on. AWS Batch has partial support for resource-level permissions. For some AWS Batch actions, you can control when users are allowed to use those actions based on conditions that must be met. You can also control based on the specific resources that users are allowed to use. For example, you can grant users permissions to submit jobs, but only to a specific job queue and only with a specific job definition. 

For details about actions and resource types defined by AWS Batch, including the format of the ARNs for each of the resource types, see Actions, Resources, and Condition Keys for [AWS Batch](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsbatch.html) in the *Service Authorization Reference*.