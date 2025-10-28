# Launch instances using Capacity Blocks

To use your Capacity Block, you must specify the Capacity Block reservation ID when launching
instances. Launching an instance into a Capacity Block reduces the available capacity by
the number of instances launched. For example, if your purchased instance capacity
is eight instances and you launch four instances, the available capacity is reduced
by four.

If you terminate an instance running in the Capacity Block before the reservation ends,
you can launch a new instance in its place. When you stop or terminate an instance
in a Capacity Block, it takes several minutes to clean up your instance before you can
launch another instance to replace it. During this time, your instance will be in a
stopping or `shutting-down` state. After this process is complete, your
instance state will change to `stopped` or `terminated`. Then,
the available capacity in your Capacity Block will update to show another instance
available to use.

###### Requirements

- Your instance can't launch in a subnet in a different
  Availability Zone from the Availability Zone where your
  Capacity Block is located.
- Your instance can't launch using an AMI with a different platform than
  the platform for your Capacity Block.
- To use `P6e-GB200` UltraServer Capacity Blocks, you must be opted in to the
  Dallas Local Zone (N. Virginia) Local Zone.

Console

###### To launch instances into a Capacity Block

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation bar at the top of the screen, select the Region for your
   Capacity Block reservation.
3. From the Amazon EC2 console dashboard, choose **Launch instance**.
4. Follow the procedure to [launch an
   instance](ec2-launch-instance-wizard.md "ec2-launch-instance-wizard.md").
5. Expand **Advanced details**, and for **Purchasing option**,
   choose **Capacity Blocks**. Then do one of the following:
   - To launch the instances into a specific Capacity Block, for **Capacity Reservation**
     choose **Specify Capacity Reservation**, and then select the Capacity Block.
   - (_UltraServers only_) To launch the instances into an UltraServer Capacity Block
     resource group, for **Capacity Reservation** choose **Specify Capacity Reservation resource
     group**, and then select the resource group.

6. Choose **Launch instance**.

AWS CLI

###### To launch instances using into a Capacity Block

Use the [run-instances](../../../cli/latest/reference/ec2/run-instances.md "../../../cli/latest/reference/ec2/run-instances.md") command with the `instance-market-options MarketType` option.

The following example launches an instance into a specific Capacity Block.

```
aws ec2 run-instances \
--image-id `ami-0abcdef1234567890` \
--count `1` \
--instance-type `p5.48xlarge` \
--key-name `my-key-pair` \
--subnet-id `subnet-0abcdef1234567890` \
**--instance-market-options MarketType='capacity-block' \
--capacity-reservation-specification CapacityReservationTarget={CapacityReservationId=`capacity_block_id`}**
```

The following example launches an instance into an UltraServer Capacity Block resource group.

```
aws ec2 run-instances \
--image-id `ami-0abcdef1234567890` \
--count `1` \
--instance-type `p6e-gb200.36xlarge` \
--key-name `my-key-pair` \
--subnet-id `subnet-0abcdef1234567890` \
**--instance-market-options MarketType='capacity-block' \
--capacity-reservation-specification CapacityReservationTarget={CapacityReservationResourceGroupArn=`resource_group_arn`}**
```

PowerShell

###### To launch instances into a Capacity Block

Use the [New-EC2Instance](../../../powershell/latest/reference/items/New-EC2Instance.md "../../../powershell/latest/reference/items/New-EC2Instance.md")
cmdlet with the `-InstanceMarketOption` option defined as follows.

```
$marketoption = New-Object Amazon.EC2.Model.InstanceMarketOptionsRequest
$marketoption.MarketType = "capacity-block"
```

The following example launches an instance into a specific Capacity Block.

```
New-EC2Instance `
-ImageId `ami-0abcdef1234567890` `
-InstanceType `p5.48xlarge` `
-KeyName "`my-key-pair`" `
-SubnetId `subnet-0abcdef1234567890` `
**-InstanceMarketOptions $marketoption `
-CapacityReservationTarget\_CapacityReservationId `capacity_block_id`**
```

The following example launches an instance into an UltraServer Capacity Block resource group.

```
New-EC2Instance `
-ImageId `ami-0abcdef1234567890` `
-InstanceType `p6e-gb200.36xlarge` `
-KeyName "`my-key-pair`" `
-SubnetId `subnet-0abcdef1234567890` `
**-InstanceMarketOptions $marketoption `
-CapacityReservationTarget\_CapacityReservationResourceGroupArn "`resource_group_arn`"**
```

###### Related resources

- To create a launch template targeting a Capacity Block, see
  [Store instance launch parameters in Amazon EC2 launch templates](ec2-launch-templates.md "ec2-launch-templates.md").
- To launch instances into a Capacity Block using EC2 Fleet, see
  [Tutorial:
  Configure your EC2 Fleet to launch instances into Capacity Blocks](ec2-fleet-launch-instances-capacity-blocks-walkthrough.md "ec2-fleet-launch-instances-capacity-blocks-walkthrough.md").
- To set up an EKS managed node group with a Capacity Block, see
  [Create a managed node group with Capacity Blocks for ML](../../../eks/latest/userguide/capacity-blocks-mng.md "../../../eks/latest/userguide/capacity-blocks-mng.md") in the
  **Amazon EKS User Guide**.
- To set up AWS ParallelCluster using a Capacity Block, see [ML on
  AWS ParallelCluster](https://catalog.workshops.aws/ml-on-aws-parallelcluster/en-US "https://catalog.workshops.aws/ml-on-aws-parallelcluster/en-US").
