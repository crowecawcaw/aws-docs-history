# Actions, resources, and condition keys for AWS IQ Permissions

AWS IQ Permissions (service prefix: `iq-permission`) provides the following
service-specific operations, resources, actions, and condition keys for use in IAM permission
policies.

References:

- Learn how to [configure this service](../../../aws-iq/latest/experts-user-guide.md "../../../aws-iq/latest/experts-user-guide.md").
- View a list of the [API operations available for
  this service](../../../aws-iq/latest/experts-user-guide.md "../../../aws-iq/latest/experts-user-guide.md").
- Learn how to secure this service and its resources by
  [using IAM](../../../aws-iq/latest/experts-user-guide/set-up-expert-account-permissions-to-use-aws-iq.md "../../../aws-iq/latest/experts-user-guide/set-up-expert-account-permissions-to-use-aws-iq.md") permission policies.
- View the [programmatic service authorization
  reference](https://servicereference.us-east-1.amazonaws.com/v1/iq-permission/iq-permission.json "https://servicereference.us-east-1.amazonaws.com/v1/iq-permission/iq-permission.json") for this service.

###### Topics

- [Actions defined by AWS IQ Permissions](#list_iq-permission-actions-as-permissions "#list_iq-permission-actions-as-permissions")
- [Resource types defined by AWS IQ Permissions](#list_iq-permission-resources-for-iam-policies "#list_iq-permission-resources-for-iam-policies")
- [Condition keys for AWS IQ Permissions](#list_iq-permission-policy-keys "#list_iq-permission-policy-keys")

## Actions defined by AWS IQ Permissions

You can specify the following actions in the `Action` element of an IAM
policy statement. Use policies to grant permissions to perform an operation in AWS. When
you use an action in a policy, you usually allow or deny access to the API operation or CLI
command with the same name. However, in some cases, a single action controls access to more
than one operation. Alternatively, some operations require several different actions.

| Actions                                                                              | Description                                                                                                                        | Resource types (\*required)                                                                       | Condition keys | Access level |
| ------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- | -------------- | ------------ |
| [ApproveAccessGrant](https://aws.amazon.com/iq/ "https://aws.amazon.com/iq/")        | Grants permission to approve a permission request                                                                                  | [permission\*](#list_iq-permission-resource-permission "#list_iq-permission-resource-permission") |                | Write        |
| [ApprovePermissionRequest](https://aws.amazon.com/iq/ "https://aws.amazon.com/iq/")  | Grants permission to approve a permission request                                                                                  | [permission\*](#list_iq-permission-resource-permission "#list_iq-permission-resource-permission") |                | Write        |
| [AssumePermissionRole](https://aws.amazon.com/iq/ "https://aws.amazon.com/iq/")      | Grants permission to obtain a set of temporary security credentials for experts which they can use to access buyers' AWS resources | [permission\*](#list_iq-permission-resource-permission "#list_iq-permission-resource-permission") |                | Write        |
| [CreatePermissionRequest](https://aws.amazon.com/iq/ "https://aws.amazon.com/iq/")   | Grants permission to create a permission request                                                                                   | [permission\*](#list_iq-permission-resource-permission "#list_iq-permission-resource-permission") |                | Write        |
| [GetPermissionRequest](https://aws.amazon.com/iq/ "https://aws.amazon.com/iq/")      | Grants permission to get a permission request                                                                                      | [permission\*](#list_iq-permission-resource-permission "#list_iq-permission-resource-permission") |                | Read         |
| [ListPermissionRequests](https://aws.amazon.com/iq/ "https://aws.amazon.com/iq/")    | Grants permission to list permission requests                                                                                      | [permission\*](#list_iq-permission-resource-permission "#list_iq-permission-resource-permission") |                | Read         |
| [RejectPermissionRequest](https://aws.amazon.com/iq/ "https://aws.amazon.com/iq/")   | Grants permission to reject a permission request                                                                                   | [permission\*](#list_iq-permission-resource-permission "#list_iq-permission-resource-permission") |                | Write        |
| [RevokePermissionRequest](https://aws.amazon.com/iq/ "https://aws.amazon.com/iq/")   | Grants permission to revoke a permission request which was previously approved                                                     | [permission\*](#list_iq-permission-resource-permission "#list_iq-permission-resource-permission") |                | Write        |
| [WithdrawPermissionRequest](https://aws.amazon.com/iq/ "https://aws.amazon.com/iq/") | Grants permission to withdraw a permission request that has not been approved or declined                                          | [permission\*](#list_iq-permission-resource-permission "#list_iq-permission-resource-permission") |                | Write        |

## Resource types defined by AWS IQ Permissions

The following resource types are defined by this service and can be used in the
`Resource` element of IAM permission policy statements.

| Resource types                                                        | ARN                                                                         | Condition keys |
| --------------------------------------------------------------------- | --------------------------------------------------------------------------- | -------------- |
| [permission](https://aws.amazon.com/iq/ "https://aws.amazon.com/iq/") | arn:${Partition}:iq-permission:${Region}::permission/${PermissionRequestId} |                |

## Condition keys for AWS IQ Permissions

AWS IQ Permissions has no service-specific condition keys that can be used in the
`Condition` element of policy statements.
