

# Actions, resources, and condition keys for AWS CodeDeploy secure host commands service
<a name="list_codedeploy-commands-secure"></a>

AWS CodeDeploy secure host commands service (service prefix: `codedeploy-commands-secure`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/codedeploy/latest/userguide/vpc-endpoints.html#vpc-codedeploy-agent-configuration).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/codedeploy/latest/userguide/vpc-endpoints.html#vpc-codedeploy-agent-configuration).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/codedeploy/latest/userguide/vpc-endpoints.html#vpc-codedeploy-agent-configuration) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/codedeploy-commands-secure/codedeploy-commands-secure.json) for this service.

**Topics**
+ [Actions defined by AWS CodeDeploy secure host commands service](#list_codedeploy-commands-secure-actions-as-permissions)
+ [Resource types defined by AWS CodeDeploy secure host commands service](#list_codedeploy-commands-secure-resources-for-iam-policies)
+ [Condition keys for AWS CodeDeploy secure host commands service](#list_codedeploy-commands-secure-policy-keys)

## Actions defined by AWS CodeDeploy secure host commands service
<a name="list_codedeploy-commands-secure-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.



| Actions | Description | Resource types (\*required) | Condition keys | Access level | 
| --- | --- | --- | --- | --- | 
|   [GetDeploymentSpecification](https://docs.aws.amazon.com/codedeploy/latest/userguide/vpc-endpoints.html#vpc-codedeploy-agent-configuration)  | Grants permission to get deployment specification |  |   | Read | 
|   [PollHostCommand](https://docs.aws.amazon.com/codedeploy/latest/userguide/vpc-endpoints.html#vpc-codedeploy-agent-configuration)  | Grants permission to request host agent commands |  |   | Read | 
|   [PutHostCommandAcknowledgement](https://docs.aws.amazon.com/codedeploy/latest/userguide/vpc-endpoints.html#vpc-codedeploy-agent-configuration)  | Grants permission to mark host agent commands acknowledged |  |   | Write | 
|   [PutHostCommandComplete](https://docs.aws.amazon.com/codedeploy/latest/userguide/vpc-endpoints.html#vpc-codedeploy-agent-configuration)  | Grants permission to mark host agent commands completed |  |   | Write | 

## Resource types defined by AWS CodeDeploy secure host commands service
<a name="list_codedeploy-commands-secure-resources-for-iam-policies"></a>

AWS CodeDeploy secure host commands service does not support specifying a resource ARN in the `Resource` element of an IAM policy statement.

## Condition keys for AWS CodeDeploy secure host commands service
<a name="list_codedeploy-commands-secure-policy-keys"></a>

AWS CodeDeploy secure host commands service has no service-specific condition keys that can be used in the `Condition` element of policy statements.