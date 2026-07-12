# Actions, resources, and condition keys for Amazon Message Gateway Service

Amazon Message Gateway Service (service prefix: `ssmmessages`) provides the following
service-specific operations, resources, actions, and condition keys for use in IAM permission
policies.

References:

- Learn how to [configure this service](../../../systems-manager/latest/userguide/session-manager.md "../../../systems-manager/latest/userguide/session-manager.md").
- View a list of the [API operations available for
  this service](../../../systems-manager/latest/userguide/systems-manager-setting-up-messageAPIs.md "../../../systems-manager/latest/userguide/systems-manager-setting-up-messageAPIs.md").
- Learn how to secure this service and its resources by
  [using IAM](../../../systems-manager/latest/userguide/setup-instance-permissions.md "../../../systems-manager/latest/userguide/setup-instance-permissions.md") permission policies.
- View the [programmatic service authorization
  reference](https://servicereference.us-east-1.amazonaws.com/v1/ssmmessages/ssmmessages.json "https://servicereference.us-east-1.amazonaws.com/v1/ssmmessages/ssmmessages.json") for this service.

###### Topics

- [Actions defined by Amazon Message Gateway Service](#list_ssmmessages-actions-as-permissions "#list_ssmmessages-actions-as-permissions")
- [Resource types defined by Amazon Message Gateway Service](#list_ssmmessages-resources-for-iam-policies "#list_ssmmessages-resources-for-iam-policies")
- [Condition keys for Amazon Message Gateway Service](#list_ssmmessages-policy-keys "#list_ssmmessages-policy-keys")

## Actions defined by Amazon Message Gateway Service

You can specify the following actions in the `Action` element of an IAM
policy statement. Use policies to grant permissions to perform an operation in AWS. When
you use an action in a policy, you usually allow or deny access to the API operation or CLI
command with the same name. However, in some cases, a single action controls access to more
than one operation. Alternatively, some operations require several different actions.

| Actions                                                                                                                                                                                                     | Description                                                                                                                          | Resource types (\*required) | Condition keys                                                                                                                                                                                                           | Access level |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------ | --------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------ |
| [CreateControlChannel](../../../systems-manager/latest/userguide/getting-started-create-iam-instance-profile.md "../../../systems-manager/latest/userguide/getting-started-create-iam-instance-profile.md") | Grants permission to register a control channel for an instance to send control messages to Systems Manager service                  |                             | [ec2:SourceInstanceARN](#list_ssmmessages-ec2_SourceInstanceARN "#list_ssmmessages-ec2_SourceInstanceARN")<br>[ssm:SourceInstanceARN](#list_ssmmessages-ssm_SourceInstanceARN "#list_ssmmessages-ssm_SourceInstanceARN") | Write        |
| [CreateDataChannel](../../../systems-manager/latest/userguide/getting-started-create-iam-instance-profile.md "../../../systems-manager/latest/userguide/getting-started-create-iam-instance-profile.md")    | Grants permission to register a data channel for an instance to send data messages to Systems Manager service                        |                             |                                                                                                                                                                                                                          | Write        |
| [OpenControlChannel](../../../systems-manager/latest/userguide/getting-started-create-iam-instance-profile.md "../../../systems-manager/latest/userguide/getting-started-create-iam-instance-profile.md")   | Grants permission to open a websocket connection for a registered control channel stream from an instance to Systems Manager service |                             |                                                                                                                                                                                                                          | Write        |
| [OpenDataChannel](../../../systems-manager/latest/userguide/getting-started-create-iam-instance-profile.md "../../../systems-manager/latest/userguide/getting-started-create-iam-instance-profile.md")      | Grants permission to open a websocket connection for a registered data channel stream from an instance to Systems Manager service    |                             |                                                                                                                                                                                                                          | Write        |

## Resource types defined by Amazon Message Gateway Service

Amazon Message Gateway Service does not support specifying a resource ARN in the
`Resource` element of an IAM policy statement.

## Condition keys for Amazon Message Gateway Service

Amazon Message Gateway Service defines the following condition keys that can be used in the
`Condition` element of an IAM policy.

| Condition keys                                                                                                                                                                                                       | Description                                                                                                                                                                                                                                                                           | Type |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---- |
| [ec2:SourceInstanceARN](../../../AWSEC2/latest/UserGuide/iam-policy-structure.md#amazon-ec2-keys "../../../AWSEC2/latest/UserGuide/iam-policy-structure.md#amazon-ec2-keys")                                         | Filters access by the ARN of the instance from which the request originated                                                                                                                                                                                                           | ARN  |
| [ssm:SourceInstanceARN](../../../systems-manager/latest/userguide/security_iam_service-with-iam.md#policy-conditions "../../../systems-manager/latest/userguide/security_iam_service-with-iam.md#policy-conditions") | Filters access by verifying the Amazon Resource Name (ARN) of the AWS Systems Manager's managed instance from which the request is made. This key is not present when the request comes from the managed instance authenticated with an IAM role associated with EC2 instance profile | ARN  |
