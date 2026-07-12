# Actions, resources, and condition keys for Amazon WorkSpaces Application Manager

Amazon WorkSpaces Application Manager (service prefix: `wam`) provides the following
service-specific operations, resources, actions, and condition keys for use in IAM permission
policies.

References:

- Learn how to [configure this service](../../../wam/latest/adminguide/iam.md "../../../wam/latest/adminguide/iam.md").
- View a list of the [API operations available for this
  service](../../../wam/latest/adminguide.md "../../../wam/latest/adminguide.md").
- Learn how to secure this service and its resources by
  [using IAM](../../../wam/latest/adminguide/iam.md "../../../wam/latest/adminguide/iam.md") permission policies.
- View the [programmatic service authorization
  reference](https://servicereference.us-east-1.amazonaws.com/v1/wam/wam.json "https://servicereference.us-east-1.amazonaws.com/v1/wam/wam.json") for this service.

###### Topics

- [Actions defined by Amazon WorkSpaces Application Manager](#list_wam-actions-as-permissions "#list_wam-actions-as-permissions")
- [Permission-only actions for Amazon WorkSpaces Application Manager](#list_wam-permission-only-actions "#list_wam-permission-only-actions")
- [Resource types defined by Amazon WorkSpaces Application Manager](#list_wam-resources-for-iam-policies "#list_wam-resources-for-iam-policies")
- [Condition keys for Amazon WorkSpaces Application Manager](#list_wam-policy-keys "#list_wam-policy-keys")

## Actions defined by Amazon WorkSpaces Application Manager

Amazon WorkSpaces Application Manager has no API operations that can be used in the
`Actions` element of an IAM policy statement.

## Permission-only actions for Amazon WorkSpaces Application Manager

The following actions are defined by Amazon WorkSpaces Application Manager but are not directly
invocable through any API operation. They can only be used in IAM policy statements
to grant or deny permissions.

| Actions                                                                                               | Description                                                                          | Resource types (\*required) | Condition keys | Access level |
| ----------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------ | --------------------------- | -------------- | ------------ |
| [AuthenticatePackager](../../../wam/latest/adminguide/iam.md "../../../wam/latest/adminguide/iam.md") | Allows the Amazon WAM packaging instance to access your application package catalog. |                             |                | Write        |

## Resource types defined by Amazon WorkSpaces Application Manager

Amazon WorkSpaces Application Manager does not support specifying a resource ARN in the
`Resource` element of an IAM policy statement.

## Condition keys for Amazon WorkSpaces Application Manager

Amazon WorkSpaces Application Manager has no service-specific condition keys that can be used in the
`Condition` element of policy statements.
