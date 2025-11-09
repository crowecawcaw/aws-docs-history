# Understanding your reservation line

items

RIs provide you a significant discount compared to On-Demand Instance pricing. RIs
aren't physical instances. They're a billing discount applied to the use of
On-Demand Instances in your account. These On-Demand Instances must match certain
attributes to benefit from the billing discount.

###### Topics

- [Upfront fee](#upfront-fee "#upfront-fee")
- [True-up fee](#true-up-fee "#true-up-fee")
- [Recurring monthly RI fee](#recurring-monthly "#recurring-monthly")
- [RI discount benefits](#discount-benefits "#discount-benefits")
- [Reserved Instance type](#ri-type "#ri-type")
- [Reserved Instance benefits applied to
  instance usage](#ri-instance-usage "#ri-instance-usage")

###### Note

In the following tables, the columns and rows from AWS CUR are transposed for
clarity. The values in the first column represent the headers of a report. These
examples include only a few key AWS CUR columns. To learn more about other AWS CUR
columns, see the [Data dictionary](data-dictionary.md "data-dictionary.md").

## Upfront fee

The **Fee** line item is added to your bill when you purchase
an `All Upfront` or `Partial Upfront` RI.

The following table shows how this one-time fee appears in some AWS CUR
columns.

|                                  |                                                                                            |
| -------------------------------- | ------------------------------------------------------------------------------------------ |
| **lineItem/LineItemType**        | Fee                                                                                        |
| **lineItem/ProductCode**         | AmazonEC2                                                                                  |
| **lineItem/UsageStartDate**      | 2016-01-01T00:00:00Z                                                                       |
| **lineItem/LineItemDescription** | Sign up charge for subscription: 363836886, planId:<br>1026576                             |
| **lineItem/UnblendedCost**       | 68                                                                                         |
| **Reservation/ReservationARN**   | arn:aws:ec2:us-east-1:123456789012:reserved-instances/f8c204c1-dd48-43f1-adb8-f88aa61e0dea |

## True-up fee

If you exchange a Convertible Reserved Instance, any cost associated with the
exchange of the original Reserved Instance and the new Reserved instance
(true-up fee) is also added to your bill as a **Fee** line
item. For a true-up fee, the
**reservation/ReservationARN** column
contains
**reserved-instance-exchange/riex**.

The following table shows a true-up fee from exchanging a Convertible Reserved
Instance.

| lineItem/LineItemType | lineItem/ProductCode | lineItem/UsageStartDate | lineItem/LineItemDescription | lineItem/UnblendedCost | Reservation/ReservationARN                                                                              |
| --------------------- | -------------------- | ----------------------- | ---------------------------- | ---------------------- | ------------------------------------------------------------------------------------------------------- |
| Fee                   | AmazonEC2            | 2016-01-01T00:00:00Z    |                              |                        | arn:aws:ec2:eu-west-1:012345678901:reserved-instance-exchange/riex-examplef-5d71-4215-886f-17a3f64ea972 |

## Recurring monthly RI fee

The **RI Fee** line item describes the recurring monthly
charges that are associated RIs applied that month. The **RI
Fee** initially is added to your bill on the day of purchase and on
the first day of each billing period thereafter.

The **RI Fee** is calculated by multiplying your discounted
hourly rate and the number of hours in the month.

The following table shows how the recurring monthly charges appear in the
report.

|                                              |                                                                                            |
| -------------------------------------------- | ------------------------------------------------------------------------------------------ |
| **lineItem/LineItemType**                    | RI fee                                                                                     |
| **lineItem/ProductCode**                     | AmazonEC2                                                                                  |
| **lineItem/UsageStartDate**                  | 2016-01-01T00:00:00Z                                                                       |
| **lineItem/UsageType**                       | HeavyUsage: m4.large                                                                       |
| **lineItem/LineItemDescription**             | USD 0.0309 hourly fee per Linux/UNIX (Amazon VPC), m4.large<br>instance                    |
| **lineItem/NormalizationFactor**             | 4                                                                                          |
| **lineItem/UnblendedCost**                   | 23                                                                                         |
| **Reservation/AvailabilityZone**             |                                                                                            |
| **Reservation/ReservationARN**               | arn:aws:ec2:us-east-1:123456789012:reserved-instances/f8c204c1-dd48-43f1-adb8-f88aa61e0dea |
| **Reservation/TotalReservedunits**           | 744                                                                                        |
| **Reservation/TotalReservedNormalizedUnits** | 2976                                                                                       |

Recurring monthly charges are recorded differently for RIs that have an
Availability Zone or AWS Region Region scope. For RIs that have an
Availability Zone scope, the corresponding Availability Zone is shown in the
**reservation/AvailabilityZone** column.
For RIs that have a Region scope, the
**reservation/AvailabilityZone** column
is empty. RIs with a Region scope have values for the
**lineitem/NormalizationFactor** and
**reservation/TotalReservedNormalizedUnits**
columns that show the instance size.

###### Note

The recurring RI fee is calculated differently than the
SavingsPlanRecurringFee. The recurring RI fee is a monthly charge while the
SavingsPlanRecurringFee is an hourly charge. For information on the
SavingsPlanRecurringFee, see [Understanding Savings Plans](cur-sp.md "cur-sp.md").

## RI discount benefits

The **Discounted Usage** line item describes the instance
usage that received a matching RI discount benefit, and is added to your bill
when you have usage that matches one of your RIs. AWS calculates RI discount
benefits based on matching usage: for example, the use of an instance that
matches the instance reservation. If you have matching usage, the cost
associated with the usage line item is always zero because the charges
associated with RIs are already accounted for in the two other line items (the
upfront fee and the recurring monthly charges).

The following table shows an example of usage that received an RI discount
benefit.

|                                    |                                                                                            |
| ---------------------------------- | ------------------------------------------------------------------------------------------ |
| **lineItem/LineItemType**          | DiscountedUsage                                                                            |
| **lineItem/ProductCode**           | AmazonEC2                                                                                  |
| **lineItem/UsageStartDate**        | 2016-01-01T00:00:00Z                                                                       |
| **lineItem/UsageType**             | BoxUsage:m4.large                                                                          |
| **lineItem/LineItemDescription**   | Linux/UNIX (Amazon VPC), m4.large Reserved Instance<br>applied                             |
| **lineItem/ResourceId**            | i-1bd250bc                                                                                 |
| **lineItem/AvailabilityZone**      | us-east-1b                                                                                 |
| **lineItem/NormalizationFactor**   | 4                                                                                          |
| **lineItem/NormalizedUsageAmount** | 4                                                                                          |
| **lineItem/UnblendedRate**         | 0                                                                                          |
| **lineItem/UnblendedCost**         | 0                                                                                          |
| **Reservation/ReservationARN**     | arn:aws:ec2:us-east-1:123456789012:reserved-instances/f8c204c1-dd48-43f1-adb8-f88aa61e0dea |

The value for **UsageAmount** in the Amazon EC2
**DiscountedUsage** line is the actual number of hours
used. The value for **NormalizedUsageAmount** is the value for
**UsageAmount** multiplied by the value for
**NormalizationFactor**. The value for
**NormalizationFactor** is determined by the instance size.
When an RI benefit discount is applied to a matching line item of usage, the
Amazon Resource Name (ARN) value in the
**reservation/ReservationARN** column
for the initial upfront fees and recurring monthly charges matches the ARN value
in the discounted usage line items.

For more information about mapping instance size to normalization factor, see
[Support for
modifying instance sizes](../../../AWSEC2/latest/UserGuide/ri-modification-instancemove.md "../../../AWSEC2/latest/UserGuide/ri-modification-instancemove.md") in the
_Amazon EC2 User Guide_.

## Reserved Instance type

To determine if your report line items are associated with a Standard Reserved
Instance or a Convertible Reserved Instance, filter the
**lineItem/LineItemType** column by
**Fee** or **RI fee**. Then, review the
**product/OfferingClass** column, which
indicates the Reserved Instance type.

To determine if your report line items are associated with a zonal or regional
Reserved Instance, review the
**reservation/AvailabilityZone** column.
For zonal Reserved Instances, this column shows the corresponding Availability
Zone. For regional Reserved Instances, this column is empty.

## Reserved Instance benefits applied to

instance usage

To understand which instance usage line items benefitted from which Reserved
Instances, you can filter your report by one or more of the following
columns:

- **reservation/reservationARN**: Filter
  this column by a reservation ARN to identify which Reserved Instance
  lease is associated with each line item.
- **lineitem/ResourceId**: Review this
  column for the ID of the resource that's covered by the Reserved
  Instance.
- **lineitem/LineItemType**: Filter this
  column by **Fee**, **RI fee**, or
  **DiscountedUsage** to determine the associated
  fees or benefits.
- **lineitem/UsageType**: Filter this
  column by **HeavyUsage** to identify **RI
  fee** line items. Or, filter this column by
  **BoxUsage** to identify
  **DiscountedUsage** line items.
- **lineitem/UsageAmount**: For
  **RI fee** line items, this column shows the total
  number of hours in the month that the Reserved Instance was applied. For
  **DiscountedUsage** line items, this column shows
  the total number of hours that the Reserved Instance was applied to a
  specific instance at the daily or monthly level, depending on how you
  configured your report.

To understand a size flexible Reserved Instance’s number of normalized units
applied to instance usage, review the
**lineitem/NormalizedUsageAmount**
column in your report. The value in this column equals the product of the
following columns:

- **lineitem/UsageAmount**: This column
  shows the metered instance usage measured in hours.
- **lineItem/NormalizationFactor**: For
  **DiscountedUsage** and **RI fee**
  line items, this column shows the associated normalization factor of the
  instance. For more information on the normalization factor, see [Instance size flexibility determined by normalization
  factor](../../../AWSEC2/latest/UserGuide/apply_ri.md#ri-normalization-factor "../../../AWSEC2/latest/UserGuide/apply_ri.md#ri-normalization-factor") in the _Amazon EC2 User Guide_.

For AWS Organizations with multiple accounts, to see which accounts purchased or
benefitted from a Reserved Instance, review the following columns:

- **reservation/reservationARN**: Review
  the reservation ARNs to see which accounts purchased the Reserved
  Instance. The ARN includes the account ID.
- **lineitem/UsageAccountId**: For
  **DiscountedUsage** line items, this column
  identifies the account IDs that received benefits from the purchased
  Reserved Instances.

###### Note

A Reserved Instance is a billing subscription and not a resource like an
Amazon EC2 instance. Because of this, Reserved Instances that are tagged don't
populate line items like a tagged resource. For line items with
**DiscountedUsage**, tags populate for the tagged
resources and not for the Reserved Instance.

To identify costs associated with a specific Reserved Instance lease, you
can filter **Fee** or **RI fee** line
items by the Reserved Instance ARN, which is the lease ID. To organize your
cost data for Reserved Instances, consider using AWS Cost Categories. For
more information, see [Managing your costs with AWS Cost Categories](../../../awsaccountbilling/latest/aboutv2/manage-cost-categories.md "../../../awsaccountbilling/latest/aboutv2/manage-cost-categories.md") in the
_AWS Billing User Guide_
