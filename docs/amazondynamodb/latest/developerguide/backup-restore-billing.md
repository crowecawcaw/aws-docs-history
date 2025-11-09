# Understanding Amazon DynamoDB billing for backups

This guide provides details about how DynamoDB billing works for backups. We'll break down
the various components that contribute to the overall cost, providing clear explanations and
practical examples.

DynamoDB offers on-demand backups and point-in-time recovery (PITR) backups to help protect
your DynamoDB data from disaster events and offers data archiving for long-term
retention.

## How it works

DynamoDB on-demand backups are billed monthly. If you take a backup on any particular day
of the month, you’ll see a single charge for that backup calculated for the remaining
days of the month (example: creating a backup on the 27th, you will only be charged for
the few days remaining in that month, applied as a single charge on the 27th).

If you retain your previously taken backups for subsequent months, you'll always see a
full month’s charge for that backup applied on the 1st. If the backup is removed before
the month’s end, the charges will be adjusted based on actual usage.

As an example, if you created a backup on July 27th, and it is maintained through the
month of August, you will see the following charges for that backup:

- A charge on July 27th for the remaining days of July
- A charge on August 1st for the entire month of August
- A charge on the 1st of every subsequent month that backup exists

When backups are maintained for DynamoDB tables, you may observe that the expense for the
`DynamoDB (Region)-TimedBackupStorage-ByteHrs` usage metric seems abnormally
high on the 1st of the month. In addition, if you check this metric at the start of a
new month and compare it against previous billing cycles, you may observe what appears
to be a large spike in usage. This is by design. On the 1st of every month, any existing
DynamoDB backups will have usage charges for the entire month applied. Any DynamoDB backups
that are removed during the month will have their usage expense prorated to reflect
actual usage. As a result, you may see the charge (applied on the 1st) decrease
throughout the month. This is because retention policies apply expirations or manual
deletions to carried over backups occur. This will be explored in a scenario below.

Similarly, you'll notice smaller spikes throughout the month as new backups are created,
with their charges applied on the day of creation for the remainder of the month.

## DynamoDB backup billing example

Here is an example of what you may see in Cost Explorer at the start of the month:

![Image showing DynamoDB billing chart in Cost Explorer.](images/ddb-backups-billing-ce.png)

Notice how February 1st appears to have a much larger spike relative to previous
months. Let’s break down why this occurs.

From the [DynamoDB Pricing
Page](https://aws.amazon.com/dynamodb/pricing/on-demand/ "https://aws.amazon.com/dynamodb/pricing/on-demand/"):

_“The total backup storage size billed each month is the sum of
all backups of DynamoDB tables. DynamoDB monitors the size of on-demand backups
continuously throughout the month to determine your backup
charges.”_

This explains why the bill consistently shows a large spike in usage on the 1st of
every month. Any existing backups coming into a new month have a full month’s charges
applied to the 1st. Put another way, if you enter the month with 300 DynamoDB backups, you
will see a full month’s usage charges applied on the 1st day of the month for all 300
backups.

New backups taken throughout the month will incur usage charges from the day of creation
until the end of the month.

**What if the backup is deleted mid-month?**

Here are a few scenarios to consider:

1. If a backup from the previous month is deleted on the 15th of the current
   month, the usage charges for that backup,still applied on the 1st, will be
   adjusted to the actual usage instead of the assumed full month of usage
   previously applied. The example below explains this more in detail.
2. When you create a backup during the month, usage charges for the remainder of
   the month are applied to the day it was created. However, if you delete this
   backup before the month ends, your usage charges will be adjusted to include
   only the days the backup was active, still applied on its creation date.

**Why does the current month’s usage appear to be so much higher
on the 1st than previous months, and what happens if I remove the
backups?**

To answer this important 2-part question, let’s set up an example scenario using the
following information:

- **Length of Month**: 30 Days
- **DynamoDB Backup Frequency**: 10/day, 300/mo
- **DynamoDB Backup Retention Policy**: 30 Days
- **DynamoDB Per-Backup Cost**: $2/day, $60/mo
- **Previous 1st of Month Total**
  (`TimedBackupStorage-ByteHrs`, checked on the 1st of the Current
  Month): $9,300
- **Previous Month Total**
  (`TimedBackupStorage-ByteHrs`): $18,600
- **Current 1st of Month Total**
  (`TimedBackupStorage-ByteHrs`, Checked on the 1st): $18,000
- **Changes in DynamoDB Usage Month-to-Month**: None

Using the information above, we can see that 300 backups were created in the previous
month with a policy to maintain them for 30 days. On the 1st of a new month, all of
these backups still remain as they've not yet hit the end of their recovery period.
However, with each passing day, the oldest sets of backups will begin to drop off, as
shown here:

| DynamoDB backup dropoff table             | New month | Day 1 | Day 2 | Day 3 | Day 4 | Day 5 |
| ----------------------------------------- | --------- | ----- | ----- | ----- | ----- | ----- |
| Total previous month backups carried over | 300       | 290   | 280   | 270   | 260   |

- On the 1st, we can see 300 backups @ $60/mo per backup, totaling $18,000 of
  `TimedBackupStorage-ByteHrs` applied. This is in contrast to the
  previous month, where the entire month’s total was $18,600.
- On the 2nd, 10 of those backups will have expired and drop off. When this occurs,
  the applied charge for those backups will be adjusted to **Actual Usage** instead of **Assumed
  Usage**. This results in those 10 backups, previously with an applied
  charge on the 1st of $600 (10 Backups x 30 Days) being adjusted down to $20 (10
  Backups x 1 Day).
- The following day, the next block of 10 will expire and drop, shifting their usage
  from 30 days down to 2 days, reducing their charge to $40 (10 Backups x 2
  Days).
  With every passing day, we’ll see that larger-than-previous-month spike begin to shrink.
  If we expand this to cover the entire month, we’ll observe the following:

| DynamoDB Backup Charges (1st of Month) Progression | 300 backups in blocks of 10 | 1st     | 10th    | 20th   | 30th |
| -------------------------------------------------- | --------------------------- | ------- | ------- | ------ | ---- |
| Block 1                                            | $600                        | $20     | $20     | $20    |
| Block 2                                            | $600                        | $40     | $40     | $40    |
| Block 3                                            | $600                        | $60     | $60     | $60    |
| Block 4                                            | $600                        | $80     | $80     | $80    |
| Block 5                                            | $600                        | $100    | $100    | $100   |
| Block 6                                            | $600                        | $120    | $120    | $120   |
| Block 7                                            | $600                        | $140    | $140    | $140   |
| Block 8                                            | $600                        | $160    | $160    | $160   |
| Block 9                                            | $600                        | $180    | $180    | $180   |
| Block 10                                           | $600                        | $600    | $200    | $200   |
| Block 11                                           | $600                        | $600    | $220    | $220   |
| Block 12                                           | $600                        | $600    | $240    | $240   |
| Block 13                                           | $600                        | $600    | $260    | $260   |
| Block 14                                           | $600                        | $600    | $280    | $280   |
| Block 15                                           | $600                        | $600    | $300    | $300   |
| Block 16                                           | $600                        | $600    | $320    | $320   |
| Block 17                                           | $600                        | $600    | $340    | $340   |
| Block 18                                           | $600                        | $600    | $360    | $360   |
| Block 19                                           | $600                        | $600    | $380    | $380   |
| Block 20                                           | $600                        | $600    | $600    | $400   |
| Block 21                                           | $600                        | $600    | $600    | $420   |
| Block 22                                           | $600                        | $600    | $600    | $440   |
| Block 23                                           | $600                        | $600    | $600    | $460   |
| Block 24                                           | $600                        | $600    | $600    | $480   |
| Block 25                                           | $600                        | $600    | $600    | $500   |
| Block 26                                           | $600                        | $600    | $600    | $520   |
| Block 27                                           | $600                        | $600    | $600    | $540   |
| Block 28                                           | $600                        | $600    | $600    | $560   |
| Block 29                                           | $600                        | $600    | $600    | $580   |
| Block 30                                           | $600                        | $600    | $600    | $600   |
| 1st of month total ($)                             | $18,000                     | $13,500 | $10,400 | $9,300 |

As a new block drops off each day, it has its usage adjusted to how many days it existed,
versus the full month amount. As a result, by month’s end the charges observed on the 1st
will have dropped from the initial $18,000 down to the expected $9,300. This number,
combined with the newly created backups through the month (which will have a billing table
similar to the above, but reversed), will result in a monthly expense in line with last
month’s $18,600.
