

# Actions, resources, and condition keys for AWS App Studio
<a name="list_appstudio"></a>

AWS App Studio (service prefix: `appstudio`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/appstudio/latest/userguide/).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/appstudio/latest/userguide/).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/appstudio/latest/userguide/) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/appstudio/appstudio.json) for this service.

**Topics**
+ [Actions defined by AWS App Studio](#list_appstudio-actions-as-permissions)
+ [Permission-only actions for AWS App Studio](#list_appstudio-permission-only-actions)
+ [Resource types defined by AWS App Studio](#list_appstudio-resources-for-iam-policies)
+ [Condition keys for AWS App Studio](#list_appstudio-policy-keys)

## Actions defined by AWS App Studio
<a name="list_appstudio-actions-as-permissions"></a>

AWS App Studio has no API operations that can be used in the `Actions` element of an IAM policy statement.

## Permission-only actions for AWS App Studio
<a name="list_appstudio-permission-only-actions"></a>

The following actions are defined by AWS App Studio but are not directly invocable through any API operation. They can only be used in IAM policy statements to grant or deny permissions.



| Actions | Description | Resource types (\*required) | Condition keys | Access level | 
| --- | --- | --- | --- | --- | 
|   [GetAccountStatus](https://docs.aws.amazon.com/appstudio/latest/userguide/)  | Grants permission to describe the account's current status |  |   | Read | 
|   [GetEnablementJobStatus](https://docs.aws.amazon.com/appstudio/latest/userguide/)  | Grants permission to fetch status of a enablement job |  |   | Read | 
|   [StartEnablementJob](https://docs.aws.amazon.com/appstudio/latest/userguide/)  | Grants permission to submit a enablement job |  |   | Write | 
|   [StartRollbackEnablementJob](https://docs.aws.amazon.com/appstudio/latest/userguide/)  | Grants permission to rollback an enablement job |  |   | Write | 
|   [StartTeamDeployment](https://docs.aws.amazon.com/appstudio/latest/userguide/)  | Grants permission to start a team deployment |  |   | Write | 

## Resource types defined by AWS App Studio
<a name="list_appstudio-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [application](https://docs.aws.amazon.com/appstudio/latest/userguide/concepts.html#concepts-application)  | arn:${Partition}:appstudio:${Region}:${Account}:application/${ApplicationId} |   | 
|  [connector](https://docs.aws.amazon.com/appstudio/latest/userguide/concepts.html#concepts-connector)  | arn:${Partition}:appstudio:${Region}:${Account}:connector/${ConnectionId} |   | 
|  [instance](https://docs.aws.amazon.com/appstudio/latest/userguide/concepts.html#concepts-instance)  | arn:${Partition}:appstudio:${Region}:${Account}:instance/${InstanceId} |   | 

## Condition keys for AWS App Studio
<a name="list_appstudio-policy-keys"></a>

AWS App Studio has no service-specific condition keys that can be used in the `Condition` element of policy statements.