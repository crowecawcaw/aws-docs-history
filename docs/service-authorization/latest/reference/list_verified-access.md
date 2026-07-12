# Actions, resources, and condition keys for AWS Verified Access

AWS Verified Access (service prefix: `verified-access`) provides the following
service-specific operations, resources, actions, and condition keys for use in IAM permission
policies.

References:

- Learn how to [configure this service](../../../verified-access/latest/ug/what-is-verified-access.md "../../../verified-access/latest/ug/what-is-verified-access.md").
- View a list of the [API operations available for
  this service](../../../AWSEC2/latest/APIReference/operation-list-verified-access.md "../../../AWSEC2/latest/APIReference/operation-list-verified-access.md").
- Learn how to secure this service and its resources by
  [using IAM](../../../verified-access/latest/ug/security_iam_id-based-policy-examples.md#security_iam_id-based-policy-examples-create-instance "../../../verified-access/latest/ug/security_iam_id-based-policy-examples.md#security_iam_id-based-policy-examples-create-instance") permission policies.
- View the [programmatic service authorization
  reference](https://servicereference.us-east-1.amazonaws.com/v1/verified-access/verified-access.json "https://servicereference.us-east-1.amazonaws.com/v1/verified-access/verified-access.json") for this service.

###### Topics

- [Actions defined by AWS Verified Access](#list_verified-access-actions-as-permissions "#list_verified-access-actions-as-permissions")
- [Permission-only actions for AWS Verified Access](#list_verified-access-permission-only-actions "#list_verified-access-permission-only-actions")
- [Resource types defined by AWS Verified Access](#list_verified-access-resources-for-iam-policies "#list_verified-access-resources-for-iam-policies")
- [Condition keys for AWS Verified Access](#list_verified-access-policy-keys "#list_verified-access-policy-keys")

## Actions defined by AWS Verified Access

AWS Verified Access has no API operations that can be used in the
`Actions` element of an IAM policy statement.

## Permission-only actions for AWS Verified Access

The following actions are defined by AWS Verified Access but are not directly
invocable through any API operation. They can only be used in IAM policy statements
to grant or deny permissions.

| Actions                                                                                                                                                                                                                                                                                      | Description                                          | Resource types (\*required) | Condition keys | Access level |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------- | --------------------------- | -------------- | ------------ |
| [AllowVerifiedAccess](../../../verified-access/latest/ug/security_iam_id-based-policy-examples.md#security_iam_id-based-policy-examples-create-instance "../../../verified-access/latest/ug/security_iam_id-based-policy-examples.md#security_iam_id-based-policy-examples-create-instance") | Grants permission to create Verified Access Instance |                             |                | Write        |

## Resource types defined by AWS Verified Access

AWS Verified Access does not support specifying a resource ARN in the
`Resource` element of an IAM policy statement.

## Condition keys for AWS Verified Access

AWS Verified Access has no service-specific condition keys that can be used in the
`Condition` element of policy statements.
