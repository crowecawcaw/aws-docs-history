# Monitoring your size flexible

reservations for Amazon EC2

Amazon EC2 Reserved Instances that apply to a Region provide Availability Zone
flexibility and instance size flexibility. Reserved Instances that provide
Availability Zone flexibility provide a discount on usage in any Availability Zone
in the Region. Reserved Instances that provide instance size flexibility provide a
discount on usage, regardless of instance size in that family. Size flexible
Reserved Instances apply to the smallest instance sizes first. For more information,
see [How
Reserved Instances are applied](../../../AWSEC2/latest/UserGuide/apply_ri.md "../../../AWSEC2/latest/UserGuide/apply_ri.md") in the
_Amazon EC2 User Guide_.

To understand how instance size flexibility provided by your Reserved Instance is
applied to your usage, refer to the
**lineItem/NormalizationFactor** and
**lineItem/NormalizedUsageAmount**
columns.

###### Note

Instance size flexibility is supported only by Linux or Unix Reserved
Instances with default tenancy that are assigned to a Region. For more
information on the limitations of instance size flexibility for Regional
Reserved Instances, see [How regional
Reserved Instances are applied](../../../AWSEC2/latest/UserGuide/apply_ri.md#apply-regional-ri "../../../AWSEC2/latest/UserGuide/apply_ri.md#apply-regional-ri") in the
_Amazon EC2 User Guide_.

In a Cost and Usage Report, the Reserved Instance usage is applied by default to the
account that purchased the Reserved Instance. Any available Reserved Instance
benefit that the purchasing account can’t use within the hour is then applied to
other linked accounts based on the available matching On-Demand Instance
usage.

## Example

You purchase one `m4.xlarge` RI in a given Region. This
`m4.xlarge` RI can be applied automatically to all
`m4` instance usage in the same Region. In the following table,
AWS applied the `m4.xlarge` to two separate `m4.large`
instances.

|                                                  |                                                                          |                                                                     |                                                                     |
| ------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| **lineItem/LineItemType**                        | RIFee                                                                    | Discounted Usage                                                    | Discounted Usage                                                    |
| **lineItem/ProductCode**                         | AmazonEC2                                                                | AmazonEC2                                                           | AmazonEC2                                                           |
| **lineItem/UsageStartDate**                      | 2016-01-01T00:00:00Z                                                     | 2016-01-01T00:00:00Z                                                | 2016-01-01T00:00:00Z                                                |
| **lineItem/UsageType**                           | HeavyUsage:m4.xlarge                                                     | BoxUsage:m4.large                                                   | BoxUsage:m4.large                                                   |
| **lineItem/LineItemDescription**                 | USD 0.0618 hourly fee per Linux/UNIX (Amazon VPC), m4.xlarge<br>instance | Linux/UNIX (Amazon VPC), m4.large Reserved Instance<br>applied      | Linux/UNIX (Amazon VPC), m4.large Reserved Instance<br>applied      |
| **lineItem/ResourceId**                          |                                                                          | i-1bd250bc                                                          | i-1df340ed                                                          |
| **lineItem/UsageAmount**                         |                                                                          | 1                                                                   | 1                                                                   |
| **lineItem/NormalizationFactor**                 | 4                                                                        | 4                                                                   | 4                                                                   |
| **lineItem/NormalizedUsageAmount**               |                                                                          | 4                                                                   | 4                                                                   |
| **lineItem/UnblendedRate**                       |                                                                          | 0                                                                   | 0                                                                   |
| **lineItem/UnblendedCost**                       | 46                                                                       | 0                                                                   | 0                                                                   |
| **Reservation/<br>ReservationARN**               | arn:aws:ec2:us-east-1: 123456789012:reserved-instances<br>/f8c204c1      | arn:aws:ec2:us-east-1: 123456789012:reserved-instances<br>/f8c204c1 | arn:aws:ec2:us-east-1: 123456789012:reserved-instances<br>/f8c204c1 |
| **Reservation/TotalReservedUnits**               | 744                                                                      |                                                                     |                                                                     |
| **Reservation/TotalReserved<br>NormalizedUnits** | 5952                                                                     |                                                                     |                                                                     |

The two `m4.large` usage line items have different
**ResourceId**s, and both received a discount benefit from
the single `m4.xlarge` RI. This is shown by matching the
**reservationARN** value across the usage and recurring
monthly charge line items.

For more information about RI purchase options, see [How you are billed](../../../AWSEC2/latest/UserGuide/concepts-reserved-instances-application.md#reserved-instances-payment-options "../../../AWSEC2/latest/UserGuide/concepts-reserved-instances-application.md#reserved-instances-payment-options") in the
_Amazon EC2 User Guide_.
