# Actions, resources, and condition keys for AWS Elemental Appliances and Software

AWS Elemental Appliances and Software (service prefix: `elemental-appliances-software`) provides the following
service-specific operations, resources, actions, and condition keys for use in IAM permission
policies.

References:

- Learn how to [configure this service](../../../elemental-appliances-software/latest/ug.md "../../../elemental-appliances-software/latest/ug.md").
- View a list of the [API operations available for
  this service](../../../elemental-appliances-software/latest/ug.md "../../../elemental-appliances-software/latest/ug.md").
- Learn how to secure this service and its resources by
  [using IAM](../../../elemental-appliances-software/latest/ug.md "../../../elemental-appliances-software/latest/ug.md") permission policies.
- View the [programmatic service authorization
  reference](https://servicereference.us-east-1.amazonaws.com/v1/elemental-appliances-software/elemental-appliances-software.json "https://servicereference.us-east-1.amazonaws.com/v1/elemental-appliances-software/elemental-appliances-software.json") for this service.

###### Topics

- [Actions defined by AWS Elemental Appliances and Software](#list_elemental-appliances-software-actions-as-permissions "#list_elemental-appliances-software-actions-as-permissions")
- [Permission-only actions for AWS Elemental Appliances and Software](#list_elemental-appliances-software-permission-only-actions "#list_elemental-appliances-software-permission-only-actions")
- [Resource types defined by AWS Elemental Appliances and Software](#list_elemental-appliances-software-resources-for-iam-policies "#list_elemental-appliances-software-resources-for-iam-policies")
- [Condition keys for AWS Elemental Appliances and Software](#list_elemental-appliances-software-policy-keys "#list_elemental-appliances-software-policy-keys")

## Actions defined by AWS Elemental Appliances and Software

AWS Elemental Appliances and Software has no API operations that can be used in the
`Actions` element of an IAM policy statement.

## Permission-only actions for AWS Elemental Appliances and Software

The following actions are defined by AWS Elemental Appliances and Software but are not directly
invocable through any API operation. They can only be used in IAM policy statements
to grant or deny permissions.

| Actions                                                                                                         | Description                                                                   | Resource types (\*required)                                                                                        | Condition keys | Access level |
| --------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------ | -------------- | ------------ |
| [CompleteUpload](../../../elemental-appliances-software.md "../../../elemental-appliances-software.md")         | Grants permission to complete an upload of an attachment for a quote or order |                                                                                                                    |                | Write        |
| [CreateOrderV1](../../../elemental-appliances-software.md "../../../elemental-appliances-software.md")          | Grants permission to create an order                                          |                                                                                                                    |                | Write        |
| [CreateQuote](../../../elemental-appliances-software.md "../../../elemental-appliances-software.md")            | Grants permission to create a quote                                           | [quote\*](#list_elemental-appliances-software-resource-quote "#list_elemental-appliances-software-resource-quote") |                | Write        |
| [GetAvsCorrectAddress](../../../elemental-appliances-software.md "../../../elemental-appliances-software.md")   | Grants permission to validate an address                                      |                                                                                                                    |                | Read         |
| [GetBillingAddresses](../../../elemental-appliances-software.md "../../../elemental-appliances-software.md")    | Grants permission to list the billing addresses in the AWS Account            |                                                                                                                    |                | Read         |
| [GetDeliveryAddressesV2](../../../elemental-appliances-software.md "../../../elemental-appliances-software.md") | Grants permission to list the delivery addresses in the AWS Account           |                                                                                                                    |                | Read         |
| [GetOrder](../../../elemental-appliances-software.md "../../../elemental-appliances-software.md")               | Grants permission to describe an order                                        |                                                                                                                    |                | Read         |
| [GetOrdersV2](../../../elemental-appliances-software.md "../../../elemental-appliances-software.md")            | Grants permission to list the orders in the AWS Account                       |                                                                                                                    |                | Read         |
| [GetQuote](../../../elemental-appliances-software.md "../../../elemental-appliances-software.md")               | Grants permission to describe a quote                                         | [quote\*](#list_elemental-appliances-software-resource-quote "#list_elemental-appliances-software-resource-quote") |                | Read         |
| [GetTaxes](../../../elemental-appliances-software.md "../../../elemental-appliances-software.md")               | Grants permission to calculate taxes for an order                             |                                                                                                                    |                | Read         |
| [ListQuotes](../../../elemental-appliances-software.md "../../../elemental-appliances-software.md")             | Grants permission to list the quotes in the AWS Account                       |                                                                                                                    |                | List         |
| [StartUpload](../../../elemental-appliances-software.md "../../../elemental-appliances-software.md")            | Grants permission to start an upload of an attachment for a quote or order    |                                                                                                                    |                | Write        |
| [SubmitOrderV1](../../../elemental-appliances-software.md "../../../elemental-appliances-software.md")          | Grants permission to submit an order                                          |                                                                                                                    |                | Write        |
| [UpdateQuote](../../../elemental-appliances-software.md "../../../elemental-appliances-software.md")            | Grants permission to modify a quote                                           | [quote\*](#list_elemental-appliances-software-resource-quote "#list_elemental-appliances-software-resource-quote") |                | Write        |

## Resource types defined by AWS Elemental Appliances and Software

The following resource types are defined by this service and can be used in the
`Resource` element of IAM permission policy statements.

| Resource types                                                                                 | ARN                                                                                     | Condition keys |
| ---------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | -------------- |
| [quote](../../../elemental-appliances-software.md "../../../elemental-appliances-software.md") | arn:${Partition}:elemental-appliances-software:${Region}:${Account}:quote/${ResourceId} |                |

## Condition keys for AWS Elemental Appliances and Software

AWS Elemental Appliances and Software has no service-specific condition keys that can be used in the
`Condition` element of policy statements.
