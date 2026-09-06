

# Actions, resources, and condition keys for Tag Editor
<a name="list_resource-explorer"></a>

Tag Editor (service prefix: `resource-explorer`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/ARG/latest/userguide/).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/ARG/latest/userguide/).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/ARG/latest/userguide/) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/resource-explorer/resource-explorer.json) for this service.

**Topics**
+ [Actions defined by Tag Editor](#list_resource-explorer-actions-as-permissions)
+ [Permission-only actions for Tag Editor](#list_resource-explorer-permission-only-actions)
+ [Resource types defined by Tag Editor](#list_resource-explorer-resources-for-iam-policies)
+ [Condition keys for Tag Editor](#list_resource-explorer-policy-keys)

## Actions defined by Tag Editor
<a name="list_resource-explorer-actions-as-permissions"></a>

Tag Editor has no API operations that can be used in the `Actions` element of an IAM policy statement.

## Permission-only actions for Tag Editor
<a name="list_resource-explorer-permission-only-actions"></a>

The following actions are defined by Tag Editor but are not directly invocable through any API operation. They can only be used in IAM policy statements to grant or deny permissions.



| Actions | Description | Resource types (\*required) | Condition keys | Access level | 
| --- | --- | --- | --- | --- | 
|   [ListResourceTypes](https://docs.aws.amazon.com/ARG/latest/userguide/gettingstarted-prereqs.html#rg-permissions-te)  | Grants permission to retrieve the resource types currently supported by Tag Editor |  |   | List | 
|   [ListResources](https://docs.aws.amazon.com/ARG/latest/userguide/gettingstarted-prereqs.html#rg-permissions-te)  | Grants permission to retrieve the identifiers of the resources in the AWS account |  |   | List | 
|   [ListTags](https://docs.aws.amazon.com/ARG/latest/userguide/gettingstarted-prereqs.html#rg-permissions-te)  | Grants permission to retrieve the tags attached to the specified resource identifiers |  |   | Read | 

## Resource types defined by Tag Editor
<a name="list_resource-explorer-resources-for-iam-policies"></a>

Tag Editor does not support specifying a resource ARN in the `Resource` element of an IAM policy statement.

## Condition keys for Tag Editor
<a name="list_resource-explorer-policy-keys"></a>

Tag Editor has no service-specific condition keys that can be used in the `Condition` element of policy statements.