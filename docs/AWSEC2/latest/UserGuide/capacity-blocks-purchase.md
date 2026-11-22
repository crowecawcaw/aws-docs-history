

# Find and purchase Capacity Blocks

To reserve a Capacity Block, you first need to find a block of time when capacity is available that matches your needs. To find a Capacity Block that is available to reserve, you specify the following.
+ Up to 10 instance types
+ The number of instances that you need
+ The duration of time that you need the instances
+ The date range that you need your reservation
+ (Amazon EC2 console only, optional) Additional AWS Regions to search, beyond your current Region

To search for an available Capacity Block offering, you specify a reservation duration and instance count. You must specify reservation durations in ** 1-day increments up to 14 days, and in 7-day increments up to 182 days**. Each Capacity Block can have up to 64 instances, and you can have up to 256 instances across Capacity Blocks.

When you request a Capacity Block that matches your specifications, the details of up to 6 (API) or 10 (Amazon EC2 console) available blocks are returned. All Capacity Blocks end at 11:30AM UTC, so the blocks starting on the same day will have durations that are the closest match to your desired duration. One block will have a duration that is slightly less than your desired duration, while the other will have a duration slightly greater than your desired duration.

When you search, Amazon EC2 looks across every instance type that you specify, in every Availability Zone and Local Zone in the Regions that you search. Offerings are ranked by earliest start date, so the options that get you started soonest appear first.
+ **Instance types** – You can specify up to 10 instance types in a single search.
+ **Regions** – In the Amazon EC2 console, you can search your current Region and additional Regions in one view. With the AWS CLI, AWS SDKs, and API, a search covers only the Region of the endpoint that you call. To find capacity in other Regions, send a separate request to each Regional endpoint.
+ **Local Zones** – Search includes Local Zones in the Regions you search, whether or not you have opted in to them. You must opt in to a Local Zone before you can purchase a Capacity Block there.
+ **UltraServers** – Searching across multiple instance types and Regions isn't available for UltraServer Capacity Blocks.

The offering details include the instance type, the start time of the reservation, the Availability Zone or Local Zone for the reservation, and the price of the reservation. For more information, see [Capacity Blocks pricing and billing](capacity-blocks-pricing-billing.md).

If none of your instance type and Region combinations has matching capacity, the search returns no offerings.

You can purchase the Capacity Block offering you are shown, or you can modify your search criteria to see the other options that are available. There is no predefined expiration time for the offering, but offerings are only available on a first-come, first-served basis.

You purchase an offering in the Region where the Capacity Block is located. In the Amazon EC2 console, if you select an offering in a Region other than your current one, you are prompted to switch to that Region to complete the purchase.

When you purchase a Capacity Block offering, you get an immediate response confirming that your Capacity Block was reserved. After confirmation, you will see a new Capacity Reservation in your account with a reservation type of `capacity-block` and a `start-date` set to the start time of the offering that you purchased. Your Capacity Block reservation is created with a state of `payment-pending`. After the upfront payment is successfully processed, the reservation state changes to `scheduled`. For more information, see [Billing](capacity-blocks-pricing-billing.md#capacity-blocks-billing).

**Note**  
 To purchase and use Capacity Blocks in Local Zones, you must be opted in to the Local Zone. 

------
#### [ Console ]

**To find and purchase a Capacity Block**

1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/).

1. In the navigation bar at the top of the screen, select an AWS Region. This is the Region that appears first in your results. You can add other Regions to the search in a later step. Capacity Block sizes of 64 instances are not supported for all instance types in all Regions.

1. In the navigation pane, choose **Capacity Reservations**, **Create Capacity Block**.

1. Under **Capacity Block types**, choose either **Instances** or ** UltraServers**.

1. Under **Capacity attributes**, you can define your Capacity Block search parameters. For **Instance types**, choose one or more instance types. (UltraServers: choose a single UltraServer type.) By default, the platform is Linux. If you want to select a different operating system, use the AWS CLI. For more information, see [Supported platforms](ec2-capacity-blocks.md#capacity-blocks-platforms).

1. (Optional, instances only) Under **Regions**, choose additional Regions to search. Your current Region is always searched.

1. Under **Total capacity** (for Instances) or **UltraServer count** (for UltraServers), specify the number of instances or UltraServers you want to reserve.

1. Under **Duration**, enter the number of days or weeks you need the reservation for.

1. Under **Date range to search for Capacity Blocks**, enter the earliest date that you want your reservation to start.

1. Choose **Find Capacity Blocks**.

1. If Capacity Blocks are available that meet your specifications, the results show up to 10 offerings ranked by earliest start date, in two sections:
   + **Your current Region** – Initially shows up to the three earliest offerings. Expand the section to see more.
   + **Other Regions** – Offerings in the additional Regions that you searched. Expand the section to see them.

   Each offering shows the instance type, Region, Availability Zone or Local Zone, start and end date, and price.

1. When you find a Capacity Block offering that you want to purchase, choose **Next**. If the offering is in a different Region than your current Region, you are prompted to switch to that Region before you continue.

1. (Optional) On the **Add tags** page, choose **Add new tag**.

1. The **Review and purchase** page lists the start and end date, duration, total number of instances, and price. 
**Note**  
Capacity Blocks can't be canceled after you reserve them.

1. In the popup window **Purchase a Capacity Block**, type confirm, then choose **Purchase**.

------
#### [ AWS CLI ]

**To find an instance Capacity Block**  
Use the [ describe-capacity-block-offerings](https://docs.aws.amazon.com/cli/latest/reference/ec2/describe-capacity-block-offerings.html) command.

The following example finds instance Capacity Blocks.

```bash
aws ec2 describe-capacity-block-offerings \
--instance-type {{p5.48xlarge}} \
--instance-count {{16}} \
--start-date-range {{2023-08-14T00:00:00Z}} \
--end-date-range {{2023-10-22-T00:00:00Z}} \
--capacity-duration-hours {{48}} \
--all-availability-zones
```

The following example searches across multiple instance types in the Region of your AWS CLI configuration. Offerings for any of the listed instance types are returned, ranked by earliest start date.

```bash
aws ec2 describe-capacity-block-offerings \
--instance-type-preferences InstanceType={{p5.48xlarge}} InstanceType={{p5e.48xlarge}} InstanceType={{p5en.48xlarge}} \
--instance-count {{32}} \
--capacity-duration-hours {{336}} \
--start-date-range {{2026-03-01T00:00:00Z}} \
--end-date-range {{2026-03-31T23:59:59Z}} \
--all-availability-zones
```

The following example finds UltraServer Capacity Blocks.

```bash
aws ec2 describe-capacity-block-offerings \
--ultraserver-type {{u-p6e-gb200x72}} \
--ultraserver-count {{1}} \
--start-date-range {{2023-08-14T00:00:00Z}} \
--end-date-range {{2023-10-22-T00:00:00Z}} \
--capacity-duration-hours {{48}}
```

**To purchase a Capacity Block**  
Use the [ purchase-capacity-block](https://docs.aws.amazon.com/cli/latest/reference/ec2/purchase-capacity-block.html) command with the offering ID of the Capacity Block from the output of the previous example.

```bash
aws ec2 purchase-capacity-block \
--capacity-block-offering-id {{cb-0123456789abcdefg}} \
--instance-platform {{Linux/UNIX}}
```

------
#### [ PowerShell ]

**To find Capacity Blocks**  
Use the [Get-EC2CapacityBlockOffering](https://docs.aws.amazon.com/powershell/latest/reference/items/Get-EC2CapacityBlockOffering.html) cmdlet.

The following example finds instance Capacity Blocks.

```powershell
Get-EC2CapacityBlockOffering `
-InstanceType {{p5.48xlarge}} `
-InstanceCount {{16}} `
-CapacityDurationHour {{48}} `
-StartDateRange {{2023-08-14T00:00:00Z}} `
-EndDateRange {{2023-10-22-T00:00:00Z}} `
-AllAvailabilityZones {{$true}}
```

The following example searches across multiple instance types in the current Region. Each instance type preference is a structure with an `InstanceType` property. Offerings for any of the listed instance types are returned, ranked by earliest start date.

```powershell
$preferences = @(
    New-Object Amazon.EC2.Model.CapacityBlockInstanceTypePreference -Property @{ InstanceType = "{{p5.48xlarge}}" }
    New-Object Amazon.EC2.Model.CapacityBlockInstanceTypePreference -Property @{ InstanceType = "{{p5e.48xlarge}}" }
    New-Object Amazon.EC2.Model.CapacityBlockInstanceTypePreference -Property @{ InstanceType = "{{p5en.48xlarge}}" }
)

Get-EC2CapacityBlockOffering `
-InstanceTypePreference $preferences `
-InstanceCount {{32}} `
-CapacityDurationHour {{336}} `
-StartDateRange {{2026-03-01T00:00:00Z}} `
-EndDateRange {{2026-03-31T23:59:59Z}}
```

The following example finds UltraServer Capacity Blocks.

```powershell
Get-EC2CapacityBlockOffering `
-UltraserverType {{u-p6e-gb200x72}} `
-UltraserverCount  {{1}} `
-CapacityDurationHour {{48}} `   
-StartDateRange {{2023-08-14T00:00:00Z}} `
-EndDateRange {{2023-10-22-T00:00:00Z}}
```

**To purchase a Capacity Block**  
Use the [New-EC2EC2CapacityBlock](https://docs.aws.amazon.com/powershell/latest/reference/items/New-EC2EC2CapacityBlock.html) cmdlet with the offering ID of the Capacity Block from the output of the previous example.

```powershell
New-EC2EC2CapacityBlock `
-CapacityBlockOfferingId {{cb-0123456789abcdefg}} `
-InstancePlatform {{Linux/UNIX}}
```

------