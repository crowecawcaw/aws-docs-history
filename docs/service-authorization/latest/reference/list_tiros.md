# Actions, resources, and condition keys for AWS Tiros

AWS Tiros (service prefix: `tiros`) provides the following
service-specific operations, resources, actions, and condition keys for use in IAM permission
policies.

References:

- Learn how to [configure this service](../../../vpc/latest/reachability/what-is-reachability-analyzer.md "../../../vpc/latest/reachability/what-is-reachability-analyzer.md").
- View a list of the [API operations available for
  this service](../../../AWSEC2/latest/APIReference/Welcome.md "../../../AWSEC2/latest/APIReference/Welcome.md").
- Learn how to secure this service and its resources by
  [using IAM](../../../vpc/latest/reachability/identity-access-management.md "../../../vpc/latest/reachability/identity-access-management.md") permission policies.
- View the [programmatic service authorization
  reference](https://servicereference.us-east-1.amazonaws.com/v1/tiros/tiros.json "https://servicereference.us-east-1.amazonaws.com/v1/tiros/tiros.json") for this service.

###### Topics

- [Actions defined by AWS Tiros](#list_tiros-actions-as-permissions "#list_tiros-actions-as-permissions")
- [Permission-only actions for AWS Tiros](#list_tiros-permission-only-actions "#list_tiros-permission-only-actions")
- [Resource types defined by AWS Tiros](#list_tiros-resources-for-iam-policies "#list_tiros-resources-for-iam-policies")
- [Condition keys for AWS Tiros](#list_tiros-policy-keys "#list_tiros-policy-keys")

## Actions defined by AWS Tiros

AWS Tiros has no API operations that can be used in the
`Actions` element of an IAM policy statement.

## Permission-only actions for AWS Tiros

The following actions are defined by AWS Tiros but are not directly
invocable through any API operation. They can only be used in IAM policy statements
to grant or deny permissions.

| Actions                                                                                                                                                                            | Description                                                                                    | Resource types (\*required) | Condition keys | Access level |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | --------------------------- | -------------- | ------------ |
| [CreateQuery](../../../vpc/latest/reachability/security_iam_required-API-permissions.md "../../../vpc/latest/reachability/security_iam_required-API-permissions.md")               | Grants permission to create a VPC reachability query                                           |                             |                | Write        |
| [ExtendQuery](../../../vpc/latest/reachability/security_iam_required-API-permissions.md "../../../vpc/latest/reachability/security_iam_required-API-permissions.md")               | Grants permission to extend a VPC reachability query to include the calling principals account |                             |                | Write        |
| [GetQueryAnswer](../../../vpc/latest/reachability/security_iam_required-API-permissions.md "../../../vpc/latest/reachability/security_iam_required-API-permissions.md")            | Grants permission to get VPC reachability query answers                                        |                             |                | Read         |
| [GetQueryExplanation](../../../vpc/latest/reachability/security_iam_required-API-permissions.md "../../../vpc/latest/reachability/security_iam_required-API-permissions.md")       | Grants permission to get VPC reachability query explanations                                   |                             |                | Read         |
| [GetQueryExtensionAccounts](../../../vpc/latest/reachability/security_iam_required-API-permissions.md "../../../vpc/latest/reachability/security_iam_required-API-permissions.md") | Grants permission to list accounts that might be useful in a new query                         |                             |                | Read         |

## Resource types defined by AWS Tiros

AWS Tiros does not support specifying a resource ARN in the
`Resource` element of an IAM policy statement.

## Condition keys for AWS Tiros

AWS Tiros has no service-specific condition keys that can be used in the
`Condition` element of policy statements.
