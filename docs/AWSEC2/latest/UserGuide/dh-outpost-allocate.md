# Allocate an Amazon EC2 Dedicated Host on AWS Outposts

You allocate and use Dedicated Hosts on Outposts in the same way that would with Dedicated Hosts in an
AWS Region.

###### Prerequisites

Create a subnet on the Outpost. For more information, see [Create a
subnet](../../../outposts/latest/userguide/launch-instance.md#create-subnet "../../../outposts/latest/userguide/launch-instance.md#create-subnet") in the _AWS Outposts User Guide_.

**To allocate a Dedicated Host on an Outpost, use one of the following
methods:**

Console

###### To allocate a Dedicated Host on an Outpost using the AWS Outposts console

1. Open the AWS Outposts console at [https://console.aws.amazon.com/outposts/](https://console.aws.amazon.com/outposts/home "https://console.aws.amazon.com/outposts/home").
2. In the navigation pane, choose **Outposts**.
   Select the Outpost and then choose **Actions**,
   **Allocate Dedicated Host**.
3. Configure the Dedicated Host as needed. For more information, see [Allocate an Amazon EC2 Dedicated Host for use in
   your account](dedicated-hosts-allocating.md "dedicated-hosts-allocating.md").

###### Note

**Availability Zone** and
**Outpost ARN** should be pre-populated
with the Availability Zone and ARN of the selected
Outpost. 4. Choose **Allocate**.

###### To allocate a Dedicated Host on an Outpost using the Amazon EC2 console

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation pane, choose **Dedicated Hosts**, and
   then choose **Allocate Dedicated Host**.
3. For **Availability Zone**, select the
   Availability Zone associated with the Outpost.
4. For **Outpost ARN**, enter the ARN of the
   Outpost.
5. To target specific hardware assets on the Outpost, for
   **Target specific hardware assets on
   Outpost**, select **Enable**. For
   each hardware asset to target, choose **Add asset
   ID**, and then enter the ID of the hardware
   asset.

###### Note

The value that you specify for
**Quantity** must be equal to the
number of asset IDs that you specify. For example, if you
specify 3 asset IDs, then Quantity must also be 3. 6. Configure the remaining Dedicated Host settings as needed. For more
information, see [Allocate an Amazon EC2 Dedicated Host for use in
your account](dedicated-hosts-allocating.md "dedicated-hosts-allocating.md"). 7. Choose **Allocate**.

AWS CLI

###### To allocate a Dedicated Host on an Outpost

Use the [allocate-hosts](../../../cli/latest/reference/ec2/allocate-hosts.md "../../../cli/latest/reference/ec2/allocate-hosts.md") command. For
`--availability-zone`, specify the Availability Zone
associated with the Outpost. For `--outpost-arn`, specify
the ARN of the Outpost. Optionally, for `--asset-ids`,
specify the IDs of the Outpost hardware assets to target.

```
aws ec2 allocate-hosts \
    --availability-zone "`us-east-1a`" \
    --outpost-arn "`arn:aws:outposts:us-east-1a:111122223333:outpost/op-4fe3dc21baEXAMPLE`" \
    --asset-ids `asset_id` \
    --instance-family "`m5`" \
    --auto-placement "`off`" \
    --quantity 1
```

PowerShell

###### To allocate a Dedicated Host on an Outpost

Use the [New-EC2Host](../../../powershell/latest/reference/items/New-EC2Host.md "../../../powershell/latest/reference/items/New-EC2Host.md") cmdlet. Specify the Availability Zone
associated with the Outpost. Optionally, for `-AssetId`,
specify the IDs of the Outpost hardware assets to target.

```
New-EC2Host `
    -AvailabilityZone "`us-east-1a`" `
    -OutpostArn "`arn:aws:outposts:us-east-1a:111122223333:outpost/op-4fe3dc21baEXAMPLE`" `
    -AssetId `asset_id` `
    -InstanceFamily "`m5`" `
    -AutoPlacement "`off`" `
    -Quantity 1
```

###### To launch an instance onto a Dedicated Host on an Outpost

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation pane, choose **Dedicated Hosts**. Select the Dedicated Host
   that you allocated in the previous step and choose
   **Actions**, **Launch instance onto
   host**.
3. Configure the instance as needed and then launch the instance. For more
   information, see [Launch Amazon EC2 instances on an Amazon EC2 Dedicated Host](launching-dedicated-hosts-instances.md "launching-dedicated-hosts-instances.md").
