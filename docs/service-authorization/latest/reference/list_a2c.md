# Actions, resources, and condition keys for AWS App2Container

AWS App2Container (service prefix: `a2c`) provides the following
service-specific operations, resources, actions, and condition keys for use in IAM permission
policies.

References:

- Learn how to [configure this service](../../../tk-dotnet-refactoring/latest/userguide/what-is-tk-dotnet-refactoring.md "../../../tk-dotnet-refactoring/latest/userguide/what-is-tk-dotnet-refactoring.md").
- View a list of the [API operations available for
  this service](../../../tk-dotnet-refactoring/latest/userguide/what-is-tk-dotnet-refactoring.md "../../../tk-dotnet-refactoring/latest/userguide/what-is-tk-dotnet-refactoring.md").
- Learn how to secure this service and its resources by
  [using IAM](../../../tk-dotnet-refactoring/latest/userguide/dotnet-refactoring-security.md "../../../tk-dotnet-refactoring/latest/userguide/dotnet-refactoring-security.md") permission policies.
- View the [programmatic service authorization
  reference](https://servicereference.us-east-1.amazonaws.com/v1/a2c/a2c.json "https://servicereference.us-east-1.amazonaws.com/v1/a2c/a2c.json") for this service.

###### Topics

- [Actions defined by AWS App2Container](#list_a2c-actions-as-permissions "#list_a2c-actions-as-permissions")
- [Resource types defined by AWS App2Container](#list_a2c-resources-for-iam-policies "#list_a2c-resources-for-iam-policies")
- [Condition keys for AWS App2Container](#list_a2c-policy-keys "#list_a2c-policy-keys")

## Actions defined by AWS App2Container

You can specify the following actions in the `Action` element of an IAM
policy statement. Use policies to grant permissions to perform an operation in AWS. When
you use an action in a policy, you usually allow or deny access to the API operation or CLI
command with the same name. However, in some cases, a single action controls access to more
than one operation. Alternatively, some operations require several different actions.

| Actions                                                                                                                                                                                              | Description                                                       | Resource types (\*required) | Condition keys | Access level |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------- | --------------------------- | -------------- | ------------ |
| [GetContainerizationJobDetails](../../../tk-dotnet-refactoring/latest/userguide/what-is-tk-dotnet-refactoring.md "../../../tk-dotnet-refactoring/latest/userguide/what-is-tk-dotnet-refactoring.md") | Grants permission to get the details of all Containerization jobs |                             |                | Read         |
| [GetDeploymentJobDetails](../../../tk-dotnet-refactoring/latest/userguide/what-is-tk-dotnet-refactoring.md "../../../tk-dotnet-refactoring/latest/userguide/what-is-tk-dotnet-refactoring.md")       | Grants permission to get the details of all Deployment jobs       |                             |                | Read         |
| [StartContainerizationJob](../../../tk-dotnet-refactoring/latest/userguide/what-is-tk-dotnet-refactoring.md "../../../tk-dotnet-refactoring/latest/userguide/what-is-tk-dotnet-refactoring.md")      | Grants permission to start a Containerization job                 |                             |                | Write        |
| [StartDeploymentJob](../../../tk-dotnet-refactoring/latest/userguide/what-is-tk-dotnet-refactoring.md "../../../tk-dotnet-refactoring/latest/userguide/what-is-tk-dotnet-refactoring.md")            | Grants permission to start a Deploymnet job                       |                             |                | Write        |

## Resource types defined by AWS App2Container

AWS App2Container does not support specifying a resource ARN in the
`Resource` element of an IAM policy statement.

## Condition keys for AWS App2Container

AWS App2Container has no service-specific condition keys that can be used in the
`Condition` element of policy statements.
