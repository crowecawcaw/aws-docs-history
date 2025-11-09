# Understanding Savings Plans

You can use Cost and Usage Reports (AWS CUR) to track your Savings Plans utilization, charges, and
allocations.

## Savings Plans line items

Savings Plans provide a flexible pricing model that offers low prices on Amazon EC2,
AWS Fargate, AWS Lambda, and Amazon SageMaker AI in exchange for a commitment to a consistent
amount of usage (measured in $/hour) for a 1-year or 3-year term.

The following line items in AWS CUR help you track and manage your spend with Savings Plans.

###### Note

In the following tables, the columns and rows from AWS CUR are transposed for
clarity. The values in the first column represent the headers of a report. These
examples include only a few key AWS CUR columns. To learn more about other AWS CUR
columns, see the [Data dictionary](data-dictionary.md "data-dictionary.md").

**Upfront fee**

The **SavingsPlanUpfrontFee** line item is added to
your bill when you purchase an `All Upfront` or `Partial
 Upfront` Savings Plans. The following table shows how this
one-time fee appears in some AWS CUR columns.

|                                  |                                                                                      |                                                                                                                     |
| -------------------------------- | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------- |
| **lineItem/LineItemType**        | SavingsPlanUpfrontFee                                                                | SavingsPlanUpfrontFee                                                                                               |
| **lineItem/ProductCode**         | ComputeSavingsPlans                                                                  | ComputeSavingsPlans                                                                                                 |
| **lineItem/UsageStartDate**      | 2019-10-10T00:03:54Z                                                                 | 2019-10-10T00:12:15Z                                                                                                |
| **lineItem/LineItemDescription** | USD $43.80 one-time fee for 1 year All Upfront<br>Compute Savings Plans ID: 70352035 | USD $43.80 one-time fee for 3-year Partial Upfront<br>Any Region M5 Instance Type EC2 Savings Plans ID:<br>12355516 |
| **lineItem/UnblendedCost**       | 43.8                                                                                 | 43.8                                                                                                                |
| **savingsPlan/SavingsPlanARN**   | arn:aws:savingsplans:: 5555555555555:savingsplan/<br>bc1d08fd                        | arn:aws:savingsplans:: 5555555555555:savingsplan/<br>67b0ef20                                                       |

**Savings Plans recurring monthly fee**

The **SavingsPlanRecurringFee** line item describes
the recurring hourly charges that correspond to `No Upfront`
or `Partial Upfront` Savings Plans. Initially, the
**SavingsPlanRecurringFee** is added to your bill
on the day of purchase and hourly thereafter.

The **SavingsPlanRecurringFee** allocated to the hour
(applicable to Hourly cost and usage) or day (applicable to Daily cost
and usage) is added to your bill at the hour of purchase. It is added
every hour/day of the billing period subsequently.

For an `All Upfront` Savings Plans, the line item indicates
the portion of the Savings Plans unused during the billing
period.

The following table shows how the recurring hourly charges appear in
some AWS CUR columns.

|                                  |                                                               |                                                                     |
| -------------------------------- | ------------------------------------------------------------- | ------------------------------------------------------------------- |
| **lineItem/LineItemType**        | SavingsPlanRecurringFee                                       | SavingsPlanRecurringFee                                             |
| **lineItem/UsageStartDate**      | 2019-20-10T00:00:00Z                                          | 2019-20-10T00:00:00Z                                                |
| **lineItem/ProductCode**         | Compute Savings Plans                                         | Compute Savings Plans                                               |
| **lineItem/UsageType**           | ComputeSP:1yrPartialUpfront                                   | USE2-EC2SP:t3.1yrPartialUpfront                                     |
| **lineItem/UnblendedCost**       | 0.01                                                          | 0.01                                                                |
| **lineItem/LineItemDescription** | 1 year Partial Upfront Compute Savings Plan                   | 1 year Partial Upfront t3 EC2 Instance Savings Plan<br>in us-east-2 |
| **savingsPlan/SavingsPlanARN**   | arn:aws:savingsplans:: 5555555555555:savingsplan/<br>bc1d08fd | arn:aws:savingsplans:: 5555555555555:savingsplan/<br>bc1d08fd       |
| **savingsPlan/PaymentOption**    | Partial Upfront                                               | Partial Upfront                                                     |
| **savingsPlan/OfferingType**     | ComputeSavingsPlans                                           | EC2InstanceSavingsPlans                                             |
| **savingsPlan/PurchaseTerm**     | 1yr                                                           | 1yr                                                                 |

###### Note

The SavingsPlanRecurringFee is calculated differently than the
recurring RI fee. The recurring RI fee is a monthly charge while the
SavingsPlanRecurringFee is an hourly charge. For information on the
recurring RI fee, see [Recurring monthly RI fee](regular-reserved-instances.md#recurring-monthly "regular-reserved-instances.md#recurring-monthly").

**Savings Plans discount benefits**

The **SavingsPlanCoveredUsage** line item describes
the instance usage that received Savings Plans benefits. A
**SavingsPlanCoveredUsage** line item shows an
unblended cost of what the On-Demand charge would have been without the
Savings Plans benefit. This unblended cost is offset by the
corresponding **SavingsPlanNegation** line item.

In each **SavingsPlanCoveredUsage** line item, you
can see how that usage was billed against your Savings Plans hourly commitment
by using the
**savingsPlan/SavingsPlanRate** and
**savingsPlan/SavingsPlanEffectiveCost**
fields.

You'll see a corresponding **SavingsPlanNegation**
for each **SavingsPlanCoveredUsage** line item.
**SavingsPlanNegation** line items offset the
unblended cost of **SavingsPlanCoveredUsage**, and
grouped at the hourly level by SavingsPlanARN, Operation, Usage Type,
and Availability Zone. Therefore, one
**SavingsPlanNegation** line item might correspond
to multiple **SavingsPlanCoveredUsage** line
items.

The following table shows how the covered usage and the negation line
items appear in some AWS CUR columns.

|                                          |                                                               |                                                               |                                                                                          |
| ---------------------------------------- | ------------------------------------------------------------- | ------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| **lineItem/LineItemType**                | SavingsPlanCoveredUsage                                       | SavingsPlanCoveredUsage                                       | SavingsPlanNegation                                                                      |
| **lineItem/UsageStartDate**              | 2019-10-10T00:00:00Z                                          | 2019-10-10T00:00:00Z                                          | 2019-10-10T00:00:00Z                                                                     |
| **lineItem/UsageEndDate**                | 2019-10-10T01:00:00Z                                          | 2019-10-10T01:00:00Z                                          | 2019-10-10T01:00:00Z                                                                     |
| **lineItem/ProductCode**                 | AmazonEC2                                                     | AmazonEC2                                                     | AmazonEC2                                                                                |
| **lineItem/UsageType**                   | BoxUsage:t3.nano                                              | BoxUsage:t3.nano                                              | BoxUsage:t3.nano                                                                         |
| **lineItem/UsageAmount**                 | 1                                                             | 0.5                                                           | -1.5                                                                                     |
| **lineItem/UnblendedCost**               | 0.0052                                                        | 0.0026                                                        | -0.0078                                                                                  |
| **lineItem/LineItemDescription**         | $0.0052 per On Demand Linux t3.nano Instance<br>Hour          | $0.0052 per On Demand Linux t3.nano Instance<br>Hour          | SavingsPlanNegation used by AccountId : 5555555555555<br>and UsageSku : K7ERD2Q28HHU97DT |
| **SavingsPlan/SavingPlanARN**            | arn:aws:savingsplans:: 5555555555555:<br>savingsplan/bc1d08fd | arn:aws:savingsplans:: 5555555555555:<br>savingsplan/bc1d08fd | arn:aws:savingsplans:: 5555555555555:<br>savingsplan/bc1d08fd                            |
| **savingsPlan/SavingsPlanRate**          | 0.0026                                                        | 0.0026                                                        |                                                                                          |
| **savingsPlan/SavingsPlanEffectiveCost** | 0.0026                                                        | 0.0013                                                        |                                                                                          |

When you have more usage than your Savings Plans commitment can cover, your
uncovered usage still appears as a Usage Line Item and the covered usage
appears as **SavingsPlanCoveredUsage** with the
corresponding **SavingsPlanNegation** line
items.
