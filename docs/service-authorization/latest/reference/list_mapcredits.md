# Actions, resources, and condition keys for AWS Migration Acceleration Program Credits

AWS Migration Acceleration Program Credits (service prefix: `mapcredits`) provides the following
service-specific operations, resources, actions, and condition keys for use in IAM permission
policies.

References:

- Learn how to [configure this service](../../../awsaccountbilling/latest/aboutv2/billing-what-is.md "../../../awsaccountbilling/latest/aboutv2/billing-what-is.md").
- View a list of the [API operations available for
  this service](../../../awsaccountbilling/latest/aboutv2/billing-permissions-ref.md "../../../awsaccountbilling/latest/aboutv2/billing-permissions-ref.md").
- Learn how to secure this service and its resources by
  [using IAM](../../../awsaccountbilling/latest/aboutv2/security-iam.md "../../../awsaccountbilling/latest/aboutv2/security-iam.md") permission policies.
- View the [programmatic service authorization
  reference](https://servicereference.us-east-1.amazonaws.com/v1/mapcredits/mapcredits.json "https://servicereference.us-east-1.amazonaws.com/v1/mapcredits/mapcredits.json") for this service.

###### Topics

- [Actions defined by AWS Migration Acceleration Program Credits](#list_mapcredits-actions-as-permissions "#list_mapcredits-actions-as-permissions")
- [Permission-only actions for AWS Migration Acceleration Program Credits](#list_mapcredits-permission-only-actions "#list_mapcredits-permission-only-actions")
- [Resource types defined by AWS Migration Acceleration Program Credits](#list_mapcredits-resources-for-iam-policies "#list_mapcredits-resources-for-iam-policies")
- [Condition keys for AWS Migration Acceleration Program Credits](#list_mapcredits-policy-keys "#list_mapcredits-policy-keys")

## Actions defined by AWS Migration Acceleration Program Credits

AWS Migration Acceleration Program Credits has no API operations that can be used in the
`Actions` element of an IAM policy statement.

## Permission-only actions for AWS Migration Acceleration Program Credits

The following actions are defined by AWS Migration Acceleration Program Credits but are not directly
invocable through any API operation. They can only be used in IAM policy statements
to grant or deny permissions.

| Actions                                                                                                                                                               | Description                                                                                                                 | Resource types (\*required)                                                              | Condition keys | Access level |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | -------------- | ------------ |
| [ListAssociatedPrograms](../../../awsaccountbilling/latest/aboutv2/billing-permissions-ref.md "../../../awsaccountbilling/latest/aboutv2/billing-permissions-ref.md") | Grants permission to view the user's associated Migration Acceleration Program agreements                                   | [agreement\*](#list_mapcredits-resource-agreement "#list_mapcredits-resource-agreement") |                | List         |
| [ListQuarterCredits](../../../awsaccountbilling/latest/aboutv2/billing-permissions-ref.md "../../../awsaccountbilling/latest/aboutv2/billing-permissions-ref.md")     | Grants permission to view Migration Acceleration Program agreements credits associated with the user's payer account        | [agreement\*](#list_mapcredits-resource-agreement "#list_mapcredits-resource-agreement") |                | List         |
| [ListQuarterSpend](../../../awsaccountbilling/latest/aboutv2/billing-permissions-ref.md "../../../awsaccountbilling/latest/aboutv2/billing-permissions-ref.md")       | Grants permission to view Migration Acceleration Program agreements eligible spend associated with the user's payer account | [agreement\*](#list_mapcredits-resource-agreement "#list_mapcredits-resource-agreement") |                | List         |

## Resource types defined by AWS Migration Acceleration Program Credits

The following resource types are defined by this service and can be used in the
`Resource` element of IAM permission policy statements.

| Resource types                                                                                                                                           | ARN                                                       | Condition keys |
| -------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------- | -------------- |
| [agreement](../../../awsaccountbilling/latest/aboutv2/billing-permissions-ref.md "../../../awsaccountbilling/latest/aboutv2/billing-permissions-ref.md") | arn:${Partition}:mapcredits:::${Agreement}/${AgreementId} |                |

## Condition keys for AWS Migration Acceleration Program Credits

AWS Migration Acceleration Program Credits has no service-specific condition keys that can be used in the
`Condition` element of policy statements.
