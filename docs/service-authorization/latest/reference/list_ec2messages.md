

# Actions, resources, and condition keys for Amazon Message Delivery Service
<a name="list_ec2messages"></a>

Amazon Message Delivery Service (service prefix: `ec2messages`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/systems-manager/latest/userguide/run-command.html).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/systems-manager/latest/APIReference/).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awssystemsmanager.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/ec2messages/ec2messages.json) for this service.

**Topics**
+ [Actions defined by Amazon Message Delivery Service](#list_ec2messages-actions-as-permissions)
+ [Resource types defined by Amazon Message Delivery Service](#list_ec2messages-resources-for-iam-policies)
+ [Condition keys for Amazon Message Delivery Service](#list_ec2messages-policy-keys)

## Actions defined by Amazon Message Delivery Service
<a name="list_ec2messages-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.



| Actions | Description | Resource types (\*required) | Condition keys | Access level | 
| --- | --- | --- | --- | --- | 
|   [AcknowledgeMessage](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-setting-up-messageAPIs.html)  | Grants permission to acknowledge a message, ensuring it will not be delivered again |  |   | Write | 
|   [DeleteMessage](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-setting-up-messageAPIs.html)  | Grants permission to delete a message |  |   | Write | 
|   [FailMessage](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-setting-up-messageAPIs.html)  | Grants permission to fail a message, signifying the message could not be processed successfully, ensuring it cannot be replied to or delivered again |  |   | Write | 
|   [GetEndpoint](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-setting-up-messageAPIs.html)  | Grants permission to route traffic to the correct endpoint based on the given destination for the messages |  |   | Read | 
|   [GetMessages](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-setting-up-messageAPIs.html)  | Grants permission to deliver messages to clients/instances using long polling |  | [ec2:SourceInstanceARN](#list_ec2messages-ec2_SourceInstanceARN)<br />[ssm:SourceInstanceARN](#list_ec2messages-ssm_SourceInstanceARN) | Read | 
|   [SendReply](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-setting-up-messageAPIs.html)  | Grants permission to send replies from clients/instances to upstream service |  | [ec2:SourceInstanceARN](#list_ec2messages-ec2_SourceInstanceARN)<br />[ssm:SourceInstanceARN](#list_ec2messages-ssm_SourceInstanceARN) | Write | 

## Resource types defined by Amazon Message Delivery Service
<a name="list_ec2messages-resources-for-iam-policies"></a>

Amazon Message Delivery Service does not support specifying a resource ARN in the `Resource` element of an IAM policy statement.

## Condition keys for Amazon Message Delivery Service
<a name="list_ec2messages-policy-keys"></a>

Amazon Message Delivery Service defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [ec2:SourceInstanceARN](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/iam-policy-structure.html#amazon-ec2-keys)  | Filters access by the ARN of the instance from which the request originated | ARN | 
|   [ssm:SourceInstanceARN](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awssystemsmanager.html#awssystemsmanager-policy-keys)  | Filters access by verifying the Amazon Resource Name (ARN) of the AWS Systems Manager's managed instance from which the request is made. This key is not present when the request comes from the managed instance authenticated with an IAM role associated with EC2 instance profile | ARN | 