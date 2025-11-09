# Understanding unused reservation

costs

You can use AWS Cost and Usage Reports (AWS CUR) to understand unused RI costs. The following four
scenarios show how.

###### Note

In the following tables, the columns and rows from AWS CUR and DBR/DBR-RT are
transposed for clarity. The values in the first column represent the headers of a
report.

## Scenario 1: RI usage is 100%

RI Fee line item has $0 unused cost and 0 usage hours.

Using the DBR/DBR-RT, you can understand your unused RI usage and costs by
referring to the fields UsageQuantity and UnblendedCosts for RI Fee line items. RI
Fee line items can be identified by the existence of ‘purchased hours’ information
in the ItemDescription field. Table 1 illustrates the columns and information used
to manage unused RI costs in the DBR and DBR-RT report.

**Table 1 – Unused RI costs for a 100% RI usage in DBR and
DBR-RT before June 17, 2019**

|                       |                                                                                                        |                                                                  |
| --------------------- | ------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------- |
| **ProductName**       | Amazon Elastic Compute Cloud                                                                           | Amazon Elastic Compute Cloud                                     |
| **UsageType**         | `HeavyUsage:c3.8xlarge`                                                                                | `HeavyUsage:c3.8xlarge`                                          |
| **Operation**         | `RunInstances`                                                                                         | `RunInstances`                                                   |
| **Availability Zone** | `us-east-1a`                                                                                           | `us-east-1a`                                                     |
| **Reserved Instance** | Y                                                                                                      | Y                                                                |
| **ItemDescription**   | `USD 0.10 hourly fee per Linux/UNIX (Amazon VPC), c3:8xlarge<br>(744 hours purchased, 744 hours used)` | `USD 0.10 hourly fee per Linux/UNIX (Amazon VPC),<br>c3:8xlarge` |
| **Usage Quantity**    | `0`                                                                                                    | `744`                                                            |
| **Unblended Rate**    | `0.1`                                                                                                  | `0.1`                                                            |
| **Unblended Cost**    | `0`                                                                                                    | `74.4`                                                           |

Using AWS CUR, you can understand your unused RI usage and costs by referring to the
fields ‘reservation/ UnusedQuantity’ and ‘reservation/ UnusedRecurringFee’ for RI
Fee line items. Table 4 below illustrates the current columns and information
utilized to manage unused RI costs in AWS CUR.

**Table 2 – Unused RI costs for a 100% RI usage in
AWS CUR**

|                                                           |                                                                  |                                                                  |
| --------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- |
| **lineitem/Productcode**                                  | Amazon EC2                                                       | Amazon EC2                                                       |
| **UsageType**                                             | `HeavyUsage:c3.8xlarge`                                          | `USW2-BoxUsage:c3.8xlarge`                                       |
| **lineitem/LineItemType**                                 | `RI Fee`                                                         | `DiscountedUsage`                                                |
| **lineitem/LineItemDescription**                          | `USD 0.10 hourly fee per Linux/UNIX (Amazon VPC),<br>c3:8xlarge` | `USD 0.00 hourly fee per Linux/UNIX (Amazon VPC),<br>c3:8xlarge` |
| **lineitem/UsageAmount**                                  | `744`                                                            | `744`                                                            |
| **lineitem/NormalizedUsageAmount**                        | `47,616`                                                         | `47,616`                                                         |
| **lineitem/UnblendedRate**                                | `0.1`                                                            | `0`                                                              |
| **lineitem/UnblendedCost**                                | `74.4`                                                           | `0`                                                              |
| **reservation/UnusedQuantity**                            | `0`                                                              |                                                                  |
| **reservation/UnusedRecurringFee**                        | `0`                                                              |                                                                  |
| **reservation/UnusedAmortizedUpfrontFeeForBillingPeriod** | `0`                                                              |                                                                  |
| **reservation/RecurringFeeForUsage**                      |                                                                  | `74.4`                                                           |
| **reservation/AmortizedUpfrontCostForUsage**              |                                                                  | `5`                                                              |
| **reservation/EffectiveCost**                             |                                                                  | `79.4`                                                           |

In addition to matching the current functionality supported by DBR/DBR-RT, AWS CUR
has the following advantages:

- Using AWS CUR, you are able to access information regarding the
  EffectiveCost for the DiscountedUsage line item, which includes both the
  recurring and upfront fees. The DBR only accounts for recurring fees.
- In AWS CUR, the UsageType field is not transformed for the DiscountedUsage
  line items whereas DBR replaces the information with RI Fee line item
  information. This is because the user can group line items in AWS CUR by
  ReservationARN in order to understand what usage was discounted by which
  RI.
- In AWS CUR, the LineItemDescription field is not transformed for the RI Fee
  line item. DBR appends the hours purchased and hours used.

## Scenario 2: Partial RI usage

RI Fee line item has unused cost and usage.

Using the DBR/DBR-RT, you can understand your unused RI usage and costs by
referring to fields UsageQuantity and UnblendedCosts for RI Fee line items. Table 3
illustrates the columns and information used to manage unused RI costs in the DBR
and DBR-RT report.

**Table 3 – Unused RI costs for a partial RI usage in DBR and
DBR-RT before June 17, 2019**

|                       |                                                                                                        |                                                                  |
| --------------------- | ------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------- |
| **ProductName**       | Amazon Elastic Compute Cloud                                                                           | Amazon Elastic Compute Cloud                                     |
| **UsageType**         | `HeavyUsage:c3.8xlarge`                                                                                | `HeavyUsage:c3.8xlarge`                                          |
| **Operation**         | `RunInstances`                                                                                         | `RunInstances`                                                   |
| **Availability Zone** | `us-east-1a`                                                                                           | `us-east-1a`                                                     |
| **Reserved Instance** | Y                                                                                                      | Y                                                                |
| **ItemDescription**   | `USD 0.10 hourly fee per Linux/UNIX (Amazon VPC), c3:8xlarge<br>(744 hours purchased, 644 hours used)` | `USD 0.10 hourly fee per Linux/UNIX (Amazon VPC),<br>c3:8xlarge` |
| **Usage Quantity**    | `100`                                                                                                  | `644`                                                            |
| **Unblended Rate**    | `0.1`                                                                                                  | `0.1`                                                            |
| **Unblended Cost**    | `10`                                                                                                   | `64.4`                                                           |

Using AWS CUR, you can understand your unused RI usage and costs by referring to
fields ‘reservation/ UnusedQuantity’ and ‘reservation/ UnusedRecurringFee’ for RI
Fee line items. Table 4 illustrates the current columns and information utilized to
manage unused RI costs in AWS CUR.

**Table 4 – Unused RI costs for a partial RI usage in
AWS CUR**

|                                                           |                                                                  |                                                                  |
| --------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- |
| **lineitem/Productcode**                                  | Amazon EC2                                                       | Amazon EC2                                                       |
| **UsageType**                                             | `HeavyUsage:c3.8xlarge`                                          | `USW2-BoxUsage:c3.8xlarge`                                       |
| **lineitem/LineItemType**                                 | `RI Fee`                                                         | `DiscountedUsage`                                                |
| **lineitem/LineItemDescription**                          | `USD 0.10 hourly fee per Linux/UNIX (Amazon VPC),<br>c3:8xlarge` | `USD 0.00 hourly fee per Linux/UNIX (Amazon VPC),<br>c3:8xlarge` |
| **lineitem/UsageAmount**                                  | `744`                                                            | `644`                                                            |
| **lineitem/NormalizedUsageAmount**                        | `47,616`                                                         | `47,216`                                                         |
| **lineitem/UnblendedRate**                                | `0.1`                                                            | `0`                                                              |
| **lineitem/UnblendedCost**                                | `74.4`                                                           | `0`                                                              |
| **reservation/UnusedQuantity**                            | `100`                                                            |                                                                  |
| **reservation/UnusedRecurringFee**                        | `0`                                                              |                                                                  |
| **reservation/UnusedAmortizedUpfrontFeeForBillingPeriod** | `10`                                                             |                                                                  |
| **reservation/RecurringFeeForUsage**                      |                                                                  | `64.4`                                                           |
| **reservation/AmortizedUpfrontCostForUsage**              |                                                                  | `5`                                                              |
| **reservation/EffectiveCost**                             |                                                                  | `69.4`                                                           |

In addition to matching the current functionality supported by DBR/DBR-RT, AWS CUR
has the following advantages:

- AWS CUR has a separate column representing UnusedQuantity for the RI Fee
  line item vs. DBR / DBR-RT which overloads the UsageQuantity column with the
  unused hours

## Scenario 3: Capacity reservation

DBR/DBR-RT filters out Capacity Reservations related UnusedBox and UnusedDed usage
type line items when covered by an RI because the RI Fee line item already covers
the unused amount in the UsageQuantity and UnblendedCost fields. Table 5 illustrates
the columns and information utilized to manage unused RI costs in the DBR and DBR-RT
report.

**Table 5 – Unused RI costs for Capacity Reservation scenario
in DBR and DBR-RT prior to June 17 2019**

|                       |                                                                                                        |                                                                  |
| --------------------- | ------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------- |
| **ProductName**       | Amazon Elastic Compute Cloud                                                                           | Amazon Elastic Compute Cloud                                     |
| **UsageType**         | `HeavyUsage:c3.8xlarge`                                                                                | `HeavyUsage:c3.8xlarge`                                          |
| **Operation**         | `RunInstances`                                                                                         | `RunInstances`                                                   |
| **Availability Zone** | `us-east-1a`                                                                                           | `us-east-1a`                                                     |
| **Reserved Instance** | Y                                                                                                      | Y                                                                |
| **ItemDescription**   | `USD 0.10 hourly fee per Linux/UNIX (Amazon VPC), c3:8xlarge<br>(744 hours purchased, 734 hours used)` | `USD 0.10 hourly fee per Linux/UNIX (Amazon VPC),<br>c3:8xlarge` |
| **Usage Quantity**    | `10`                                                                                                   | `734`                                                            |
| **Unblended Rate**    | `0.1`                                                                                                  | `0.1`                                                            |
| **Unblended Cost**    | `1`                                                                                                    | `73.4`                                                           |

AWS CUR shows these line items as DiscountedUsage. Table 6 illustrates the current
columns and information utilized to manage unused RI costs in AWS CUR.

**Table 6 – Unused RI costs for the Capacity Reservation
scenario in AWS CUR**

|                                              |                                                                  |                                                                                 |                                                                  |
| -------------------------------------------- | ---------------------------------------------------------------- | ------------------------------------------------------------------------------- | ---------------------------------------------------------------- |
| **lineitem/Productcode**                     | Amazon EC2                                                       | Amazon EC2                                                                      | Amazon EC2                                                       |
| **UsageType**                                | `HeavyUsage: c3.8xlarge`                                         | `USW2-Reservation: c3.8xlarge`                                                  | `USW2-BoxUsage: c3.8xlarge`                                      |
| **lineitem/LineItemType**                    | `RI Fee`                                                         | `Usage`                                                                         | `DiscountedUsage`                                                |
| **lineitem/LineItemDescription**             | `USD 0.10 hourly fee per Linux/UNIX (Amazon VPC),<br>c3:8xlarge` | `USD 0.00 per Reservation Linux/UNIX (Amazon VPC),<br>c3:8xlarge Instance Hour` | `USD 0.00 hourly fee per Linux/UNIX (Amazon VPC),<br>c3:8xlarge` |
| **lineitem/UsageAmount**                     | `744`                                                            | `744`                                                                           | `744`                                                            |
| **lineitem/NormalizedUsageAmount**           | `47,616`                                                         |                                                                                 | `47,216`                                                         |
| **lineitem/UnblendedRate**                   | `0.1`                                                            | `0`                                                                             | `0`                                                              |
| **lineitem/UnblendedCost**                   | `74.4`                                                           | `0`                                                                             | `0`                                                              |
| **reservation/RecurringFeeForUsage**         |                                                                  |                                                                                 | `64.4`                                                           |
| **reservation/AmortizedUpfrontCostForUsage** |                                                                  |                                                                                 | `5`                                                              |
| **reservation/EffectiveCost**                |                                                                  |                                                                                 | `69.4`                                                           |

## Scenario 4: Size flexible reservations

Utilizing the DBR/DBR-RT, you can understand your unused RI usage and costs by
referring to fields UsageQuantity and UnblendedCosts for RI Fee line items. RI Fee
line items can be identified by the existence of ‘purchased hours’ information in
the ItemDescription field. Table 9 illustrates the columns and information utilized
to manage unused RI costs in the DBR and DBR-RT report.

**Table 7 – Unused RI costs for a size flex RI scenario in DBR
and DBR-RT before June 17, 2019**

|                       |                                                                                                        |                                                                                                |
| --------------------- | ------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------- |
| **ProductName**       | Amazon Elastic Compute Cloud                                                                           | Amazon Elastic Compute Cloud                                                                   |
| **UsageType**         | `HeavyUsage:c3.8xlarge`                                                                                | `HeavyUsage:c3.8xlarge`                                                                        |
| **Operation**         | `RunInstances`                                                                                         | `RunInstances`                                                                                 |
| **Availability Zone** | `us-east-1a`                                                                                           | `us-east-1a`                                                                                   |
| **Reserved Instance** | Y                                                                                                      | Y                                                                                              |
| **ItemDescription**   | `USD 0.10 hourly fee per Linux/UNIX (Amazon VPC), c3:8xlarge<br>(744 hours purchased, 644 hours used)` | `USD 0.10 hourly fee per Linux/UNIX (Amazon VPC),<br>c3:8xlarge; UsageType: BoxUsage:c3.large` |
| **Usage Quantity**    | `100`                                                                                                  | `644`                                                                                          |
| **Unblended Rate**    | `0.1`                                                                                                  | `0.1`                                                                                          |
| **Unblended Cost**    | `10`                                                                                                   | `64.4`                                                                                         |

Using AWS CUR, you can understand your unused RI usage and costs by referring to
fields ‘reservation/ UnusedQuantity’ and ‘reservation/ UnusedRecurringFee’ for RI
Fee line items. Table 8 illustrates the current columns and information utilized to
manage unused RI costs in the AWS CUR.

**Table 8 – Unused RI costs for a size flex RI scenario in
AWS CUR**

|                                                           |                                                                  |                                                                 |
| --------------------------------------------------------- | ---------------------------------------------------------------- | --------------------------------------------------------------- |
| **lineitem/Productcode**                                  | Amazon EC2                                                       | Amazon EC2                                                      |
| **UsageType**                                             | `HeavyUsage:c3.8xlarge`                                          | `USW2-BoxUsage:c3.8xlarge`                                      |
| **lineitem/LineItemType**                                 | `RI Fee`                                                         | `DiscountedUsage`                                               |
| **lineitem/LineItemDescription**                          | `USD 0.10 hourly fee per Linux/UNIX (Amazon VPC),<br>c3:8xlarge` | `USD 0.00 hourly fee per Linux/UNIX (Amazon VPC),<br>c3:8large` |
| **lineitem/UsageAmount**                                  | `744`                                                            | `644`                                                           |
| **lineitem/NormalizedUsageAmount**                        | `47,616`                                                         | `2,576`                                                         |
| **lineitem/UnblendedRate**                                | `0.1`                                                            | `0`                                                             |
| **lineitem/UnblendedCost**                                | `74.4`                                                           | `0`                                                             |
| **reservation/UnusedQuantity**                            | `100`                                                            |                                                                 |
| **reservation/UnusedRecurringFee**                        | `70.37`                                                          |                                                                 |
| **reservation/UnusedAmortizedUpfrontFeeForBillingPeriod** | `5.5`                                                            |                                                                 |
| **reservation/RecurringFeeForUsage**                      |                                                                  | `4.03`                                                          |
| **reservation/AmortizedUpfrontCostForUsage**              |                                                                  | `0.5`                                                           |
| **reservation/EffectiveCost**                             |                                                                  | `4.53`                                                          |

In addition to matching the current functionality supported by DBR/DBR-RT, AWS CUR
has the following advantages:

- AWS CUR has the NormalizedUsageAmount and quantity. The DBR / DBR-RT do not
  have columns representing this.
- AWS CUR UsageType and Operation are not transformed for the DiscountedUsage
  lineitem. The DBR / DBR-RT replaces these values with the RI Fee line
  item.
- AWS CUR LineItemDescription is not transformed for the DiscountedUsage line
  item. In DBR / DBR-RT, which replaces with the RI Fee line item description
  and appends the DiscountedUsage line item Usage Type to the end of the
  string i.e. “USD 0.10 hourly fee per Linux/UNIX (Amazon VPC), c3:8xlarge;
  UsageType: BoxUsage:c3.large”
