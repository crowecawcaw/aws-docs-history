# Tutorial:

Configure your EC2 Fleet to launch instances into Capacity Blocks

This tutorial walks you through the steps that you must perform so that your EC2 Fleet launches
instances into Capacity Blocks.

In most cases, the target capacity of the EC2 Fleet request should be less than or equal to
the available capacity of the Capacity Block reservation that you are targeting. Target
capacity requests that exceed the limits of the Capacity Block reservation will not be
fulfilled. If the target capacity request exceeds the limits of your Capacity Block
reservation, you will receive an `Insufficient Capacity Exception` for the
capacity that exceeds the limits of your Capacity Block reservation.

###### Note

For Capacity Blocks, EC2 Fleet will not fallback to launching On-Demand Instances for the remainder of the
desired target capacity.

If EC2 Fleet is unable to fulfill the requested target capacity in an available Capacity Block
reservation, EC2 Fleet will fulfill as much capacity as it can and return the instances that
it was able to launch. You can repeat the call to EC2 Fleet again until all the instances are
provisioned.

After configuring the EC2 Fleet request, you must wait until the start date of your
Capacity Block reservation. If you make requests to EC2 Fleet to launch into a Capacity Block that hasn't
started yet, you will receive an `Insufficient Capacity Error`.

After your Capacity Block reservation becomes active, you can make EC2 Fleet API calls and provision
the instances into your Capacity Block based on the parameters you selected. Instances running
in the Capacity Block continue to run until you manually stop or terminate them or until Amazon EC2
terminates the instances when the Capacity Block reservation ends.

For more information about Capacity Blocks, see [Capacity Blocks for ML](ec2-capacity-blocks.md "ec2-capacity-blocks.md").

###### Considerations

- Only EC2 Fleet requests of type `instant` are supported for launching
  instances into Capacity Blocks. For more information, see [Configure an EC2 Fleet of type instant](instant-fleet.md "instant-fleet.md").
- Multiple Capacity Blocks in the same EC2 Fleet request aren't supported.
- Using `OnDemandTargetCapacity` or `SpotTargetCapacity`
  while also setting `capacity-block` as the
  `DefaultTargetCapacity` isn't supported.
- If `DefaultTargetCapacityType` is set to
  `capacity-block`, you can't provide
  `OnDemandOptions::CapacityReservationOptions`. An exception will
  occur.

###### To configure an EC2 Fleet to launch instances into Capacity Blocks

1. **Create a launch template.**

In the launch template, do the following:

    * For `InstanceMarketOptionsRequest`, set
     `MarketType` to `capacity-block`.
    * To target the Capacity Block reservation, for
     `CapacityReservationID`, specify the Capacity Block reservation
     ID.

Make note of launch template name and version. You'll use this information in the next
step.

For more information about creating a launch template, see [Create an Amazon EC2 launch template](create-launch-template.md "create-launch-template.md"). 2. **Configure the EC2 Fleet.**

Create a file, `config.json`, with the following configuration for your
EC2 Fleet. In the following example, replace the resource identifiers with your own
resource identifiers.

For more information about configuring an EC2 Fleet, see [Create an EC2 Fleet](create-ec2-fleet.md "create-ec2-fleet.md").

```
{
    "LaunchTemplateConfigs": [
        {
            "LaunchTemplateSpecification": {
                "LaunchTemplateName": "`CBR-launch-template`",
                "Version": "`1`"
            },
            "Overrides": [
                {
                    "InstanceType": "`p5.48xlarge`",
                    "AvailabilityZone": "`us-east-1a`"
                },
            ]
        }
    ],
    "TargetCapacitySpecification": {
        "TotalTargetCapacity": `10`,
        "DefaultTargetCapacityType": "capacity-block"
    },
    "Type": "instant"
}
```

3. **Launch the fleet.**

Use the following [create-fleet](../../../cli/latest/reference/ec2/create-fleet.md "../../../cli/latest/reference/ec2/create-fleet.md") command.

```
aws ec2 create-fleet --cli-input-json file://config.json
```

For more information, see [Create an EC2 Fleet](create-ec2-fleet.md#create-ec2-fleet-procedure "create-ec2-fleet.md#create-ec2-fleet-procedure").
