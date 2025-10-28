# Find and purchase Capacity Blocks

To reserve a Capacity Block, you first need to find a block of time when capacity is
available that matches your needs. To find a Capacity Block that is available to reserve,
you specify the following.

- The number of instances that you need
- The duration of time you that you need the instances
- The date range that you need your reservation
  To search for an available Capacity Block offering, you specify a reservation duration
  and instance count. You must specify reservation durations in **1-day increments up to 14 days, and in 7-day increments up to 182 days**.
  Each Capacity Block can have up to 64 instances, and you can have up to 256 instances
  across Capacity Blocks.

When you request a Capacity Block that matches your specifications, we provide the
details of up to 3 available blocks. All Capacity Blocks end at 11:30AM UTC, so the
blocks starting on the same day will have durations that are the closest match to
your desired duration. One block will have a duration that is slightly less than
your desired duration, while the other will have a duration slightly greater than
your desired duration.

The offering details include the start time of the reservation, the Availability
Zone for the reservation, and the price of the reservation. For more information,
see [Capacity Blocks pricing and billing](capacity-blocks-pricing-billing.md "capacity-blocks-pricing-billing.md").

You can purchase the Capacity Block offering you are shown, or you can modify your
search criteria to see the other options that are available. There is no predefined
expiration time for the offering, but offerings are only available on a first-come,
first-served basis.

When you purchase a Capacity Block offering, you get an immediate response confirming
that your Capacity Block was reserved. After confirmation, you will see a new Capacity Reservation in your
account with a reservation type of `capacity-block` and a
`start-date` set to the start time of the offering that you
purchased. Your Capacity Block reservation is created with a state of
`payment-pending`. After the upfront payment is successfully
processed, the reservation state changes to `scheduled`. For more
information, see [Billing](capacity-blocks-pricing-billing.md#capacity-blocks-billing "capacity-blocks-pricing-billing.md#capacity-blocks-billing").

###### Note

To use `P6e-GB200` UltraServer Capacity Blocks, you must be opted in to the
Dallas Local Zone (N. Virginia) Local Zone.

Console

###### To find and purchase a Capacity Block

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation bar at the top of the screen, select an
   AWS Region. This choice is important because Capacity Block sizes of
   64 instances are not supported for all instance types in all
   Regions.
3. In the navigation pane, choose **Capacity Reservations**,
   **Create Capacity Block**.
4. Under **Capacity Block types**, choose
   either **Instances** or **UltraServers**.
5. Under **Capacity attributes**, you can define
   your Capacity Block search parameters. By default, the platform is
   Linux. If you want to select a different operating system, use
   the AWS CLI. For more information, see [Supported platforms](ec2-capacity-blocks.md#capacity-blocks-platforms "ec2-capacity-blocks.md#capacity-blocks-platforms").
6. Under **Total capacity** (for Instances) or
   **UltraServer count** (for UltraServers),
   specify the number of instances or UltraServers you want to reserve.
7. Under **Duration**, enter the number of days
   or weeks you need the reservation for.
8. Under **Date range to search for Capacity Blocks**,
   enter the earliest date that you want your reservation to
   start.
9. Choose **Find Capacity Blocks**.
10. If a Capacity Block is available that meets your specifications, you
    see an offering under **Recommended
    Capacity Blocks**. If there are multiple offerings that meet
    your specifications, the earliest available Capacity Block offering is
    shown. To view other Capacity Block offerings, adjust your search
    inputs and choose **Find Capacity Blocks**
    again.
11. When you find a Capacity Block offering that you want to purchase,
    choose **Next**.
12. (Optional) On the **Add tags** page, choose
    **Add new tag**.
13. The **Review and purchase** page lists the
    start and end date, duration, total number of instances, and
    price.

###### Note

Capacity Blocks can't be canceled after you reserve them. 14. In the popup window **Purchase a Capacity Block**,
type confirm, then choose **Purchase**.

AWS CLI

###### To find an instance Capacity Block

Use the [describe-capacity-block-offerings](../../../cli/latest/reference/ec2/describe-capacity-block-offerings.md "../../../cli/latest/reference/ec2/describe-capacity-block-offerings.md") command.

The following example finds instance Capacity Blocks.

```
aws ec2 describe-capacity-block-offerings \
--instance-type `p5.48xlarge` \
--instance-count `16` \
--start-date-range `2023-08-14T00:00:00Z` \
--end-date-range `2023-10-22-T00:00:00Z` \
--capacity-duration-hours `48`
```

The following example finds UltraServer Capacity Blocks.

```
aws ec2 describe-capacity-block-offerings \
--ultraserver-type `u-p6e-gb200x72` \
--ultraserver-count `1` \
--start-date-range `2023-08-14T00:00:00Z` \
--end-date-range `2023-10-22-T00:00:00Z` \
--capacity-duration-hours `48`
```

###### To purchase a Capacity Block

Use the [purchase-capacity-block](../../../cli/latest/reference/ec2/purchase-capacity-block.md "../../../cli/latest/reference/ec2/purchase-capacity-block.md") command with the offering ID of the Capacity Block
from the output of the previous example.

```
aws ec2 purchase-capacity-block \
--capacity-block-offering-id `cb-0123456789abcdefg` \
--instance-platform `Linux/UNIX`
```

PowerShell

###### To find Capacity Blocks

Use the [Get-EC2CapacityBlockOffering](../../../powershell/latest/reference/items/Get-EC2CapacityBlockOffering.md "../../../powershell/latest/reference/items/Get-EC2CapacityBlockOffering.md") cmdlet.

The following example finds instance Capacity Blocks.

```
Get-EC2CapacityBlockOffering `
-InstanceType `p5.48xlarge` `
-InstanceCount `16` `
-CapacityDurationHour `48` `
-StartDateRange `2023-08-14T00:00:00Z` `
-EndDateRange `2023-10-22-T00:00:00Z`
```

The following example finds UltraServer Capacity Blocks.

```
Get-EC2CapacityBlockOffering `
-UltraserverType `u-p6e-gb200x72` `
-UltraserverCount  `1` `
-CapacityDurationHour `48` `
-StartDateRange `2023-08-14T00:00:00Z` `
-EndDateRange `2023-10-22-T00:00:00Z`
```

###### To purchase a Capacity Block

Use the [New-EC2EC2CapacityBlock](../../../powershell/latest/reference/items/New-EC2EC2CapacityBlock.md "../../../powershell/latest/reference/items/New-EC2EC2CapacityBlock.md") cmdlet with the offering ID
of the Capacity Block from the output of the previous example.

```
New-EC2EC2CapacityBlock `
-CapacityBlockOfferingId `cb-0123456789abcdefg` `
-InstancePlatform `Linux/UNIX`
```
