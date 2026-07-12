# Actions, resources, and condition keys for AWS Activate

AWS Activate (service prefix: `activate`) provides the following
service-specific operations, resources, actions, and condition keys for use in IAM permission
policies.

References:

- Learn how to [configure this service](https://aws.amazon.com/activate/faq/#AWS_Activate_Console "https://aws.amazon.com/activate/faq/#AWS_Activate_Console").
- View a list of the [API operations available for
  this service](https://aws.amazon.com/activate/faq/#AWS_Activate_Console "https://aws.amazon.com/activate/faq/#AWS_Activate_Console").
- Learn how to secure this service and its resources by
  [using IAM](https://aws.amazon.com/activate/faq/#AWS_Activate_Console "https://aws.amazon.com/activate/faq/#AWS_Activate_Console") permission policies.
- View the [programmatic service authorization
  reference](https://servicereference.us-east-1.amazonaws.com/v1/activate/activate.json "https://servicereference.us-east-1.amazonaws.com/v1/activate/activate.json") for this service.

###### Topics

- [Actions defined by AWS Activate](#list_activate-actions-as-permissions "#list_activate-actions-as-permissions")
- [Resource types defined by AWS Activate](#list_activate-resources-for-iam-policies "#list_activate-resources-for-iam-policies")
- [Condition keys for AWS Activate](#list_activate-policy-keys "#list_activate-policy-keys")

## Actions defined by AWS Activate

You can specify the following actions in the `Action` element of an IAM
policy statement. Use policies to grant permissions to perform an operation in AWS. When
you use an action in a policy, you usually allow or deny access to the API operation or CLI
command with the same name. However, in some cases, a single action controls access to more
than one operation. Alternatively, some operations require several different actions.

| Actions                                                    | Description                                                           | Resource types (\*required) | Condition keys | Access level |
| ---------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------- | -------------- | ------------ |
| [CreateForm](../../../index.md "../../../index.md")        | Grants permission to submit an Activate application form              |                             |                | Write        |
| [GetAccountContact](../../../index.md "../../../index.md") | Grants permission to get the AWS account contact information          |                             |                | Read         |
| [GetContentInfo](../../../index.md "../../../index.md")    | Grants permission to get Activate tech posts and offer information    |                             |                | Read         |
| [GetCosts](../../../index.md "../../../index.md")          | Grants permission to get the AWS cost information                     |                             |                | Read         |
| [GetCredits](../../../index.md "../../../index.md")        | Grants permission to get the AWS credit information                   |                             |                | Read         |
| [GetMemberInfo](../../../index.md "../../../index.md")     | Grants permission to get the Activate member information              |                             |                | Read         |
| [GetProgram](../../../index.md "../../../index.md")        | Grants permission to get an Activate program                          |                             |                | Read         |
| [PutMemberInfo](../../../index.md "../../../index.md")     | Grants permission to create or update the Activate member information |                             |                | Write        |

## Resource types defined by AWS Activate

AWS Activate does not support specifying a resource ARN in the
`Resource` element of an IAM policy statement.

## Condition keys for AWS Activate

AWS Activate has no service-specific condition keys that can be used in the
`Condition` element of policy statements.
