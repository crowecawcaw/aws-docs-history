# Quotas and restrictions

The following table describes quotas and restrictions within AWS Billing Conductor.

## Quotas

**Using Billing Conductor as a standalone service**

|                                                                                             |        |
| ------------------------------------------------------------------------------------------- | ------ |
| Number of billing groups per payer account                                                  | 5,000  |
| Number of accounts per billing group                                                        | 1,000  |
| Number of pricing plans                                                                     | 5,000  |
| Number of pricing rules                                                                     | 50,000 |
| Number of pricing rules that can associate to a pricing plan                                | 500    |
| Number of pricing plans that can associate with a pricing rule                              | 1,000  |
| Number of custom line items                                                                 | 50,000 |
| Number of source values that can associate to a percentage custom line item                 | 100    |
| Number of percentage custom that can associate to a flat custom line item                   | 100    |
| Number of custom line item that configured line item filters per billing group              | 10     |
| Number of custom line item that configured "ITEMIZED" as computation rule per billing group | 5      |

**Using Billing Conductor with billing transfer**

|                                                                             |                                                                                               |
| --------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- |
| Number of one-to-one billing group mappings per bill transfer account       | Same as the number of billing transfers allowed for the billing transfer account to<br>manage |
| Number of billing groups per bill source account                            | 1                                                                                             |
| Number of accounts per billing group                                        | 1,000                                                                                         |
| Number of pricing plans                                                     | 5,000                                                                                         |
| Number of pricing rules                                                     | 50,000                                                                                        |
| Number of pricing rules that can associate to a pricing plan                | 500                                                                                           |
| Number of pricing plans that can associate with a pricing rule              | 1,000                                                                                         |
| Number of custom line items                                                 | 50,000                                                                                        |
| Number of source values that can associate to a percentage custom line item | 100                                                                                           |
| Number of percentage custom that can associate to a flat custom line item   | 100                                                                                           |

## Restrictions

Other restrictions in the following table cannot be increased.

**Using Billing Conductor as a standalone service**

|                                                                 |                                                                                                      |
| --------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| Number of Cost and Usage Reports per billing group billing view | 10                                                                                                   |
| Number of pro forma for bill transfer account                   | Same as the number of billing transfers allowed for the billing transfer account to<br>manage        |
| Billing group name                                              | • Must be within 128 characters<br>• Cannot contain a `space`<br>• Cannot contain special characters |
| Billing group description                                       | Must be within 1,024 characters                                                                      |
| Pricing plan name                                               | • Must be within 128 characters<br>• Cannot contain a `space`<br>• Cannot contain special characters |
| Pricing plan description                                        | Must be within 1,024 characters                                                                      |
| Custom line item name                                           | • Must be within 128 characters<br>• Cannot contain a `space`<br>• Cannot contain special characters |

**Using Billing Conductor with billing transfer**

|                                                     |                                                                                                      |
| --------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| Number of pro forma &CUR; for bill transfer account | 10                                                                                                   |
| Billing group name                                  | • Must be within 128 characters<br>• Cannot contain a `space`<br>• Cannot contain special characters |
| Billing group description                           | Must be within 1,024 characters                                                                      |
| Pricing plan name                                   | • Must be within 128 characters<br>• Cannot contain a `space`<br>• Cannot contain special characters |
| Pricing plan description                            | Must be within 1,024 characters                                                                      |
| Custom line item name                               | • Must be within 128 characters<br>• Cannot contain a `space`<br>• Cannot contain special characters |
