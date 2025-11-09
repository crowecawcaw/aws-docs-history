# Quotas and restrictions

The following table describes quotas and restrictions within AWS Billing Conductor.

## Quotas

|                                                                             |        |
| --------------------------------------------------------------------------- | ------ |
| Number of billing groups per payer account                                  | 5,000  |
| Number of accounts per billing group                                        | 1,000  |
| Number of pricing plans                                                     | 5,000  |
| Number of pricing rules                                                     | 50,000 |
| Number of pricing rules that can associate to a pricing plan                | 500    |
| Number of pricing plans that can associate with a pricing rule              | 1,000  |
| Number of custom line items                                                 | 50,000 |
| Number of source values that can associate to a percentage custom line item | 100    |
| Number of percentage custom that can associate to a flat custom line item   | 100    |

## Restrictions

Other restrictions in the following table cannot be increased.

|                                                                  |                                                                                                      |
| ---------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| Number of billing group Cost and Usage Reports per billing group | 10                                                                                                   |
| Billing group name                                               | • Must be within 128 characters<br>• Cannot contain a `space`<br>• Cannot contain special characters |
| Billing group description                                        | Must be within 1,024 characters                                                                      |
| Pricing plan name                                                | • Must be within 128 characters<br>• Cannot contain a `space`<br>• Cannot contain special characters |
| Pricing plan description                                         | Must be within 1,024 characters                                                                      |
| Custom line item name                                            | • Must be within 128 characters<br>• Cannot contain a `space`<br>• Cannot contain special characters |
