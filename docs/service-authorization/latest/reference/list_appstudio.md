# Actions, resources, and condition keys for AWS App Studio

AWS App Studio (service prefix: `appstudio`) provides the following
service-specific operations, resources, actions, and condition keys for use in IAM permission
policies.

References:

- Learn how to [configure this service](../../../appstudio/latest/userguide.md "../../../appstudio/latest/userguide.md").
- View a list of the [API operations available for
  this service](../../../appstudio/latest/userguide.md "../../../appstudio/latest/userguide.md").
- Learn how to secure this service and its resources by
  [using IAM](../../../appstudio/latest/userguide.md "../../../appstudio/latest/userguide.md") permission policies.
- View the [programmatic service authorization
  reference](https://servicereference.us-east-1.amazonaws.com/v1/appstudio/appstudio.json "https://servicereference.us-east-1.amazonaws.com/v1/appstudio/appstudio.json") for this service.

###### Topics

- [Actions defined by AWS App Studio](#list_appstudio-actions-as-permissions "#list_appstudio-actions-as-permissions")
- [Permission-only actions for AWS App Studio](#list_appstudio-permission-only-actions "#list_appstudio-permission-only-actions")
- [Resource types defined by AWS App Studio](#list_appstudio-resources-for-iam-policies "#list_appstudio-resources-for-iam-policies")
- [Condition keys for AWS App Studio](#list_appstudio-policy-keys "#list_appstudio-policy-keys")

## Actions defined by AWS App Studio

AWS App Studio has no API operations that can be used in the
`Actions` element of an IAM policy statement.

## Permission-only actions for AWS App Studio

The following actions are defined by AWS App Studio but are not directly
invocable through any API operation. They can only be used in IAM policy statements
to grant or deny permissions.

| Actions                                                                                                       | Description                                                | Resource types (\*required) | Condition keys | Access level |
| ------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------- | --------------------------- | -------------- | ------------ |
| [GetAccountStatus](../../../appstudio/latest/userguide.md "../../../appstudio/latest/userguide.md")           | Grants permission to describe the account's current status |                             |                | Read         |
| [GetEnablementJobStatus](../../../appstudio/latest/userguide.md "../../../appstudio/latest/userguide.md")     | Grants permission to fetch status of a enablement job      |                             |                | Read         |
| [StartEnablementJob](../../../appstudio/latest/userguide.md "../../../appstudio/latest/userguide.md")         | Grants permission to submit a enablement job               |                             |                | Write        |
| [StartRollbackEnablementJob](../../../appstudio/latest/userguide.md "../../../appstudio/latest/userguide.md") | Grants permission to rollback an enablement job            |                             |                | Write        |
| [StartTeamDeployment](../../../appstudio/latest/userguide.md "../../../appstudio/latest/userguide.md")        | Grants permission to start a team deployment               |                             |                | Write        |

## Resource types defined by AWS App Studio

The following resource types are defined by this service and can be used in the
`Resource` element of IAM permission policy statements.

| Resource types                                                                                                                                             | ARN                                                                          | Condition keys |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | -------------- |
| [application](../../../appstudio/latest/userguide/concepts.md#concepts-application "../../../appstudio/latest/userguide/concepts.md#concepts-application") | arn:${Partition}:appstudio:${Region}:${Account}:application/${ApplicationId} |                |
| [connector](../../../appstudio/latest/userguide/concepts.md#concepts-connector "../../../appstudio/latest/userguide/concepts.md#concepts-connector")       | arn:${Partition}:appstudio:${Region}:${Account}:connector/${ConnectionId}    |                |
| [instance](../../../appstudio/latest/userguide/concepts.md#concepts-instance "../../../appstudio/latest/userguide/concepts.md#concepts-instance")          | arn:${Partition}:appstudio:${Region}:${Account}:instance/${InstanceId}       |                |

## Condition keys for AWS App Studio

AWS App Studio has no service-specific condition keys that can be used in the
`Condition` element of policy statements.
