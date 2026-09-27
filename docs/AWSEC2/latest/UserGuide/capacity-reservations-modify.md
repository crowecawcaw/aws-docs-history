

# Modify a Capacity Reservation
<a name="capacity-reservations-modify"></a>

If you have an active Capacity Reservation that isn't a good fit for the workload that needs the capacity, you can modify the instance quantity, instance eligibility (`open` or `targeted`), and end time (`At specific time` or `Manually`). If you specify a new instance quantity that exceeds your remaining On-Demand Instance limit for the selected instance type, the update fails.

If you have a future-dated Capacity Reservation in the `scheduled` state, you can postpone the start date, or move the end date. For more information, see [Change dates of a future-dated Capacity Reservation](#cr-delay-start-date).

The allowed modifications depend on the state of the Capacity Reservation:
+ `assessing` state — You can modify the tags only.
+ `scheduled` state — You can modify the tags, postpone the start date, and change the end date.
+ `pending` state — You can't modify the Capacity Reservation in any way.
+ `active` state but still within the commitment duration — You can't decrease the instance count below the committed instance count, or set an end date that is before the committed duration. All other modifications are allowed.
+ `active` state with no commitment duration or elapsed commitment duration — All modifications are allowed.
+ `delayed`, `expired`, `cancelled`, `unsupported`, or `failed` state — You can't modify the Capacity Reservation in any way.

**Considerations**
+ You can't change the instance type, platform, Availability Zone, or tenancy after creation. If you need to modify any of these attributes, we recommend that you cancel the reservation, and then create a new one with the required attributes.
+ If you modify an active Capacity Reservation by changing the instance eligibility from `targeted` to `open`, any running instances that match the attributes of the Capacity Reservation, have the `CapacityReservationPreference` parameter set to `open`, and are not yet running in a Capacity Reservation, will automatically use the modified Capacity Reservation.
+ To change the instance eligibility, the Capacity Reservation must be completely idle (zero usage) because Amazon EC2 can't modify instance eligibility when instances are running inside the reservation.

## Modify an active Capacity Reservation
<a name="cr-modify-active"></a>

Use the following procedures to change the capacity, instance eligibility, or end time of a Capacity Reservation that is in the `active` state.

------
#### [ Console ]

**To modify a Capacity Reservation**

1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/).

1. Choose **Capacity Reservations**, select the Capacity Reservation to modify, and then choose **Edit**.

1. Modify the **Total capacity**, **Capacity Reservation ends**, or **Instance eligibility** options as needed, and choose **Save**.

------
#### [ AWS CLI ]

**To modify a Capacity Reservation**  
Use the [modify-capacity-reservation](https://docs.aws.amazon.com/cli/latest/reference/ec2/modify-capacity-reservation.html) command. The following example modifies the specified Capacity Reservation to reserve capacity for eight instances.

```
aws ec2 modify-capacity-reservation \
    --capacity-reservation-id {{cr-1234567890abcdef0}} \
    --instance-count {{8}}
```

------
#### [ PowerShell ]

**To modify a Capacity Reservation**  
Use the [Edit-EC2CapacityReservation](https://docs.aws.amazon.com/powershell/latest/reference/items/Edit-EC2CapacityReservation.html) cmdlet. The following example modifies the specified Capacity Reservation to reserve capacity for eight instances.

```
Edit-EC2CapacityReservation `
    -CapacityReservationId {{cr-1234567890abcdef0}} `
    -InstanceCount {{8}}
```

------

## Change dates of a future-dated Capacity Reservation
<a name="cr-delay-start-date"></a>

While a future-dated Capacity Reservation is in the `scheduled` state, you can postpone the start date or change the end date.

### Date-change quote
<a name="cr-delay-start-date-quote"></a>

To postpone a start date, you need a date-change quote. The quote shows the exact terms for you to review and accept:
+ The new start date
+ Any additional commitment
+ The resulting commitment duration and commitment end date

Additional commitment might be required when you postpone a start date. The amount depends on when you make the request relative to the current start date. The following table shows the typical commitment change required.


**Commitment change by request timing**  

| When you make the request | Typical commitment change | 
| --- | --- | 
| More than two weeks before the current start date | No additional commitment | 
| Within two weeks of the current start date | One additional day of commitment for each day you postpone | 

The table provides general guidance. Your quote shows the exact commitment terms.

For example, suppose you have a `scheduled` future-dated Capacity Reservation with a 14-day commitment duration and a start date of 2026-05-15. On 2026-05-08, you postpone the start date by 7 days. Because that date is within two weeks of the start date, Amazon EC2 adds one day of commitment for each day you postpone, for a total commitment duration of 21 days. If you make the same request more than two weeks before the start date, Amazon EC2 adds no commitment.

To generate a quote, use `CreateCapacityReservationDateChangeQuote` with the new start date. To accept the terms, pass the quote ID to `ModifyCapacityReservation` with `--accept-terms true`. The quote carries the requested start date, so you don't pass it again. Amazon EC2 then processes the request. To track its progress, check the `AdjustmentStatus` field: `requested` while Amazon EC2 evaluates the change, `applied` when the new start date replaces the original one, or `rejected` when Amazon EC2 can't support it.

A date-change quote is valid for 24 hours. After 24 hours, you must generate a new quote.

### Considerations
<a name="cr-delay-start-date-limits"></a>
+ To change the start date while the reservation is still in the `assessing` state, cancel it for free and submit a new request with the start date that you want. For more information, see [Cancel a Capacity Reservation](capacity-reservations-release.md).
+ You can postpone the start date up to 30 cumulative days from `OriginalStartDate`. For example, if you postpone the start date by 10 days, you can later postpone it by up to 20 more days. Each request needs a new quote.
+ You can't postpone a start date that is less than one hour away.
+ A future-dated Capacity Reservation can have only one modification request in progress. You can't replace or cancel a request while Amazon EC2 processes it. Wait for the request to reach `applied` or `rejected`.

### Change dates of a scheduled Capacity Reservation
<a name="cr-change-dates-procedure"></a>

------
#### [ Console ]

**To change the dates**

1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/).

1. Choose **Capacity Reservations**, select the Capacity Reservation to modify, and then choose **Edit**.

1. Modify the end date or postpone the start date, and then choose **Save**.

1. If you're postponing the start date, review the terms of the date-change quote, including any additional commitment and the new commitment end date. Enter `confirm` to accept the terms.

1. To track the request, choose the Capacity Reservation and view the **Adjustment status** field.

------
#### [ AWS CLI ]

**To change the dates**  
Use the [modify-capacity-reservation](https://docs.aws.amazon.com/cli/latest/reference/ec2/modify-capacity-reservation.html) command, specifying the new end date.

```
aws ec2 modify-capacity-reservation \
    --capacity-reservation-id {{cr-1234567890abcdef0}} \
    --end-date {{2026-06-30T00:00:00.000Z}}
```

To postpone the start date, first generate a date-change quote using [create-capacity-reservation-date-change-quote](https://docs.aws.amazon.com/cli/latest/reference/ec2/create-capacity-reservation-date-change-quote.html), then pass the quote ID to the modify command.

```
aws ec2 create-capacity-reservation-date-change-quote \
    --capacity-reservation-id {{cr-1234567890abcdef0}} \
    --new-start-date {{2026-05-22T00:00:00.000Z}}
```

Review the `CapacityReservationModificationQuote` in the response, including any additional commitment and the resulting `CommitmentEndDate`. Then submit with the quote ID:

```
aws ec2 modify-capacity-reservation \
    --capacity-reservation-id {{cr-1234567890abcdef0}} \
    --quote-id {{crmq-1a2b3c4d5e6f7g8h9i0j}} \
    --accept-terms true
```

To track the request, use [describe-capacity-reservations](https://docs.aws.amazon.com/cli/latest/reference/ec2/describe-capacity-reservations.html) and check the `AdjustmentStatus` field: `requested` while Amazon EC2 evaluates the change, `applied` when it updates the reservation, or `rejected` when it doesn't.

------
#### [ PowerShell ]

**To change the dates**  
Use the [Edit-EC2CapacityReservation](https://docs.aws.amazon.com/powershell/latest/reference/items/Edit-EC2CapacityReservation.html) cmdlet, specifying the new end date.

```
Edit-EC2CapacityReservation `
    -CapacityReservationId {{cr-1234567890abcdef0}} `
    -EndDate {{2026-06-30T00:00:00.000Z}}
```

To postpone the start date, first generate a date-change quote using [New-EC2CapacityReservationDateChangeQuote](https://docs.aws.amazon.com/powershell/latest/reference/items/New-EC2CapacityReservationDateChangeQuote.html), then pass the quote ID to the `Edit-EC2CapacityReservation` cmdlet.

```
New-EC2CapacityReservationDateChangeQuote `
    -CapacityReservationId {{cr-1234567890abcdef0}} `
    -NewStartDate {{2026-05-22T00:00:00.000Z}}
```

Review the `CapacityReservationModificationQuote` in the response, including any additional commitment and the resulting commitment end date. Then submit with the quote ID:

```
Edit-EC2CapacityReservation `
    -CapacityReservationId {{cr-1234567890abcdef0}} `
    -QuoteId {{crmq-1a2b3c4d5e6f7g8h9i0j}} `
    -AcceptTerms $true
```

To track the request, use [Get-EC2CapacityReservation](https://docs.aws.amazon.com/powershell/latest/reference/items/Get-EC2CapacityReservation.html) and check the `AdjustmentStatus` field: `requested` while Amazon EC2 evaluates the change, `applied` when it updates the reservation, or `rejected` when it doesn't.

------