

# Cancel a Capacity Reservation
<a name="capacity-reservations-release"></a>

You can cancel a Capacity Reservation that is in one of the following states:
+ `assessing`
+ `scheduled`
+ `active`
+ `delayed`

**Note**  
You can't modify or cancel a Capacity Block. For more information, see [Capacity Blocks for ML](ec2-capacity-blocks.md).

If the Capacity Reservation is `active` with no commitment duration or an elapsed commitment duration, cancellation is free.

If the Capacity Reservation is `assessing` or `delayed`, cancellation is free.

If the Capacity Reservation is `scheduled` or `active` with remaining commitment duration, a cancellation charge might apply. For more information, see [Cancellation charges](#cr-cancellation-charges).

If you cancel a Capacity Reservation that has running instances, the instances continue to run normally outside of the Capacity Reservation at standard On-Demand Instance rates or at a discounted rate if you have a matching Savings Plans or Regional Reserved Instance.

After you cancel a Capacity Reservation, instances that target it can no longer launch. Modify these instances so that they either target a different Capacity Reservation, launch into any open Capacity Reservation with matching attributes and sufficient capacity, or avoid launching into a Capacity Reservation. For more information, see [Modify the Capacity Reservation settings of your instance](capacity-reservations-modify-instance.md).

**Topics**
+ [Cancellation charges](#cr-cancellation-charges)
+ [Cancellation quote](#cr-cancellation-quote)
+ [Cancel a Capacity Reservation](#capacity-reservations-cancel-procedures)

## Cancellation charges
<a name="cr-cancellation-charges"></a>

If you cancel a future-dated Capacity Reservation within 8 weeks of the start date, or during the commitment duration after delivery, you're charged for a percentage of your commitment duration. Capacity is released as soon as you cancel, but the reservation continues to be billed at the On-Demand rate through the end of the reduced commitment period. If you have a matching Savings Plans or Regional Reserved Instance, the discounted rate applies automatically.

To calculate the charge, Amazon EC2 multiplies your commitment duration by a cancellation rate. The earlier you cancel relative to the start date, the lower the rate. The following table shows the cancellation rates.


**Cancellation rates**  

| When you cancel | Minimum cancellation rate | 
| --- | --- | 
| 8 or more weeks before the original start date | No charge | 
| 2 to 8 weeks before the original start date | 25% of total commitment | 
| Within 2 weeks of the original start date | 50% of total commitment | 
| After delivery, during the commitment duration | 50% of remaining commitment | 

This table provides general guidance on cancellation charges. The cancellation quote determines the exact cancellation charge duration.

For example, if you have a 70-instance `c8g.xlarge` Capacity Reservation with a 14-day commitment duration and you cancel within 2 weeks of the original start date (50% cancellation rate), you're charged for 7 days of commitment. During those 7 days, you pay for 70 instances at the On-Demand rate.

When you are charged for cancellation:
+ The Capacity Reservation enters the `cancelling` state.
+ The Capacity Reservation can't be modified, moved, shared, or split.
+ The Capacity Reservation remains visible in the console and in `DescribeCapacityReservations` responses.
+ The Capacity Reservation transitions to `cancelled` when the commitment ends.

To find when cancellation charges end, use the [describe-capacity-reservations](https://docs.aws.amazon.com/cli/latest/reference/ec2/describe-capacity-reservations.html) command and check the `CommitmentInfo.CommitmentEndDate` field in the response. Charges stop when the commitment ends and the Capacity Reservation transitions to `cancelled`. For information about how cancellation charges appear in the AWS Cost and Usage Report 2.0, see [Cancellation charges in Cost and Usage Report 2.0](capacity-reservations-pricing-billing.md#capacity-reservations-cancellation-billing-cur).

If the Capacity Reservation has remaining commitment duration, you can't cancel it while instances are still running. You must first stop or terminate the running instances, which prevents you from incurring both cancellation charges and On-Demand Instance charges at the same time.

To cancel a Capacity Reservation with a cancellation charge, you must first generate a cancellation quote and accept the terms. For more information, see [Cancellation quote](#cr-cancellation-quote).

## Cancellation quote
<a name="cr-cancellation-quote"></a>

When a cancellation requires a charge, you must review and accept a cancellation quote before proceeding. The quote provides the exact cancellation terms, including the following details:
+ The current configuration of the Capacity Reservation
+ The state that the Capacity Reservation transitions to after cancellation (`cancelling`)
+ The committed instance count that the charge applies to
+ The charge duration
+ The charge end date (when the commitment ends and the Capacity Reservation transitions to `cancelled`)

After you review the terms, you confirm the cancellation by accepting the quote.

In the Amazon EC2 console, the quote is generated automatically when you initiate a cancellation. You can review the terms and confirm your acceptance directly. With the AWS CLI or API, use `CreateCapacityReservationCancellationQuote` to generate the quote, then pass the quote ID to `CancelCapacityReservation`.

The cancellation quote is valid for 24 hours. After 24 hours, you must generate a new quote. To view your existing cancellation quotes, use `DescribeCapacityReservationCancellationQuotes`.

**Important**  
Cancellation is irreversible. After you accept a cancellation quote and cancel a Capacity Reservation, you can't undo the cancellation.

## Cancel a Capacity Reservation
<a name="capacity-reservations-cancel-procedures"></a>

Use the following procedures to cancel a Capacity Reservation.

------
#### [ Console ]

**To cancel a Capacity Reservation**

1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/).

1. Choose **Capacity Reservations** and select the Capacity Reservation to cancel.

1. Choose **Cancel reservation**.

1. If a cancellation quote is required, review the cancellation terms, including the charge duration and charge end date. Enter **confirm** to accept the terms.

1. Choose **Cancel reservation**.

------
#### [ AWS CLI ]

**To cancel a Capacity Reservation**  
Use the [cancel-capacity-reservation](https://docs.aws.amazon.com/cli/latest/reference/ec2/cancel-capacity-reservation.html) command.

```
aws ec2 cancel-capacity-reservation \
    --capacity-reservation-id {{cr-1234567890abcdef0}}
```

If a cancellation quote is required, first generate the quote using [create-capacity-reservation-cancellation-quote](https://docs.aws.amazon.com/cli/latest/reference/ec2/create-capacity-reservation-cancellation-quote.html), then pass the quote ID to the cancel command.

```
aws ec2 create-capacity-reservation-cancellation-quote \
    --capacity-reservation-id {{cr-1234567890abcdef0}}
```

Review the `CancellationTerms` in the response, including `ChargeCommitmentDurationHours` and `ChargeEndDate`. Then cancel with the quote ID:

```
aws ec2 cancel-capacity-reservation \
    --capacity-reservation-id {{cr-1234567890abcdef0}} \
    --quote-id {{crcq-1a2b3c4d5e6f7g8h9}} \
    --apply-cancellation-charges commitment-wind-down
```

------
#### [ PowerShell ]

**To cancel a Capacity Reservation**  
Use the [Remove-EC2CapacityReservation](https://docs.aws.amazon.com/powershell/latest/reference/items/Remove-EC2CapacityReservation.html) cmdlet.

```
Remove-EC2CapacityReservation `
    -CapacityReservationId {{cr-1234567890abcdef0}}
```

If a cancellation quote is required, first generate the quote using [New-EC2CapacityReservationCancellationQuote](https://docs.aws.amazon.com/powershell/latest/reference/items/New-EC2CapacityReservationCancellationQuote.html), then pass the quote ID to the cancel cmdlet.

```
New-EC2CapacityReservationCancellationQuote `
    -CapacityReservationId {{cr-1234567890abcdef0}}
```

Review the cancellation terms in the response. Then cancel with the quote ID:

```
Remove-EC2CapacityReservation `
    -CapacityReservationId {{cr-1234567890abcdef0}} `
    -QuoteId {{crcq-1a2b3c4d5e6f7g8h9}} `
    -ApplyCancellationCharge "commitment-wind-down"
```

------