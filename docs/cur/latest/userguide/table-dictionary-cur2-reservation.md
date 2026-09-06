

# Reservation columns
<a name="table-dictionary-cur2-reservation"></a>

Reservation columns contain data about a reservation that applies to the line item.



| Column name | Description | Data type | 
| --- | --- | --- | 
| reservation\_amortized\_upfront\_cost\_for\_usage | The initial upfront payment for all upfront RIs and partial upfront RIs amortized for usage time. The value is equal to: RIAmortizedUpfrontFeeForBillingPeriod \* The normalized usage amount for DiscountedUsage line items / The normalized usage amount for the RIFee. Because there are no upfront payments for no upfront RIs, the value for a no upfront RI is 0. We don't provide this value for Dedicated Host reservations at this time. The change will be made in a future update. | double | 
| reservation\_amortized\_upfront\_fee\_for\_billing\_period | Describes how much of the upfront fee for this reservation is costing you for the billing period. The initial upfront payment for all upfront RIs and partial upfront RIs, amortized over this month. Because there are no upfront fees for no upfront RIs, the value for no upfront RIs is `0`. We don't provide this value for Dedicated Host reservations at this time. The change will be made in a future update. | double | 
| reservation\_availability\_zone | The Availability Zone of the resource that is associated with this line item. | string | 
| reservation\_effective\_cost | The sum of both the upfront and hourly rate of your RI, averaged into an effective hourly rate. EffectiveCost is calculated by taking the amortizedUpfrontCostForUsage and adding it to the recurringFeeForUsage. | double | 
| reservation\_end\_time | The end date of the associated RI lease term. | string | 
| reservation\_modification\_status | Shows whether the RI lease was modified or if it is unaltered.<br />**Original:** The purchased RI was never modified.<br />**System:** The purchased RI was modified using the console or API.<br />**Manual:** The purchased RI was modified using AWS Support assistance.<br />**ManualWithData:** The purchased RI was modified using AWS Support assistance, and AWS calculated estimates for the RI. | string | 
| reservation\_net\_amortized\_upfront\_cost\_for\_usage | The initial upfront payment for All Upfront RIs and Partial Upfront RIs amortized for usage time, if applicable. This column is included in your report only when your account has a discount in the applicable billing period. | double | 
| reservation\_net\_amortized\_upfront\_fee\_for\_billing\_period | The cost of the reservation's upfront fee for the billing period. This column is included in your report only when your account has a discount in the applicable billing period. | double | 
| reservation\_net\_effective\_cost | The sum of both the upfront fee and the hourly rate of your RI, averaged into an effective hourly rate. This column is included in your report only when your account has a discount in the applicable billing period. | double | 
| reservation\_net\_recurring\_fee\_for\_usage | The after-discount cost of the recurring usage fee. This column is included in your report only when your account has a discount in the applicable billing period. | double | 
| reservation\_net\_unused\_amortized\_upfront\_fee\_for\_billing\_period | The net unused amortized upfront fee for the billing period. This column is included in your report only when your account has a discount in the applicable billing period. | double | 
| reservation\_net\_unused\_recurring\_fee | The recurring fees associated with unused reservation hours for Partial Upfront and No Upfront RIs after discounts. This column is included in your report only when your account has a discount in the applicable billing period. | double | 
| reservation\_net\_upfront\_value | The upfront value of the RI with discounts applied. This column is included in your report only when your account has a discount in the applicable billing period. | double | 
| reservation\_normalized\_units\_per\_reservation | The number of normalized units for each instance of a reservation subscription. | string | 
| reservation\_number\_of\_reservations | The number of reservations that are covered by this subscription. For example, one RI subscription might have four associated RI reservations. | string | 
| reservation\_recurring\_fee\_for\_usage | The recurring fee amortized for usage time, for partial upfront RIs and no upfront RIs. The value is equal to: The unblended cost of the RIFee \* The sum of the normalized usage amount of Usage line items / The normalized usage amount of the RIFee for size flexible Reserved Instances. Because all upfront RIs don't have recurring fee payments greater than 0, the value for all upfront RIs is 0. | double | 
| reservation\_reservation\_a\_r\_n | The Amazon Resource Name (ARN) of the RI that this line item benefited from. This is also called the "RI Lease ID". This is a unique identifier of this particular AWS Reserved Instance. The value string also contains the AWS service name and the Region where the RI was purchased. | string | 
| reservation\_start\_time | The start date of the term of the associated Reserved Instance. | string | 
| reservation\_subscription\_id | A unique identifier that maps a line item with the associated offer. We recommend you use the RI ARN as your identifier of an AWS Reserved Instance, but both can be used. | string | 
| reservation\_total\_reserved\_normalized\_units | The total number of reserved normalized units for all instances for a reservation subscription. AWS computes total normalized units by multiplying the reservation/NormalizedUnitsPerReservation with reservation/NumberOfReservations. | string | 
| reservation\_total\_reserved\_units | TotalReservedUnits populates for both Fee and RIFee line items with distinct values. | string | 
| reservation\_units\_per\_reservation | UnitsPerReservation populates for both Fee and RIFee line items with distinct values. | string | 
| reservation\_unused\_amortized\_upfront\_fee\_for\_billing\_period | The amortized-upfront-fee-for-billing-period-column amortized portion of the initial upfront fee for all upfront RIs and partial upfront RIs. Because there are no upfront payments for no upfront RIs, the value for no upfront RIs is `0`. We don't provide this value for Dedicated Host reservations at this time. The change will be made in a future update. | double | 
| reservation\_unused\_normalized\_unit\_quantity | The number of unused normalized units for a size-flexible Regional RI that you didn't use during this billing period. | double | 
| reservation\_unused\_quantity | The number of RI hours that you didn't use during this billing period. | double | 
| reservation\_unused\_recurring\_fee | The recurring fees associated with your unused reservation hours for partial upfront and no upfront RIs. Because all upfront RIs don't have recurring fees greater than `0`, the value for All Upfront RIs is `0`. | double | 
| reservation\_upfront\_value | The upfront price paid for your AWS Reserved Instance. For no upfront RIs, this value is `0`. | double | 