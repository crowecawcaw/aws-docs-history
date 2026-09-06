

# Tutorial: Configure your EC2 Fleet to launch instances into Interruptible Capacity Reservations
<a name="ec2-fleet-launch-instances-interruptible-cr-walkthrough"></a>

This tutorial walks you through the steps that you must perform so that your EC2 Fleet launches instances into Interruptible Capacity Reservations.

Interruptible Capacity Reservations represent spare capacity lent to you by On-Demand Capacity Reservation owners within your AWS organization. These reservations are suitable for interruptible workloads because the capacity owner can reclaim the capacity at any time with a 2-minute interruption notice, after which EC2 terminates the instances. For more information about Interruptible Capacity Reservations, see [Interruptible Capacity Reservations](interruptible-capacity-reservations.md).

The target capacity of the EC2 Fleet request should be less than or equal to the available capacity of the Interruptible Capacity Reservation that you are targeting. If the target capacity request exceeds the available capacity of your Interruptible Capacity Reservation, EC2 Fleet launches as many instances as it can and reports the launched instances in the API response.

Instances running in an Interruptible Capacity Reservation continue to run until you manually stop or terminate them, or until the capacity owner reclaims the capacity. When the capacity owner reclaims the capacity, Amazon EC2 sends an Amazon EventBridge notification 2 minutes before terminating the instances.

## Considerations
<a name="ec2-fleet-interruptible-cr-considerations"></a>
+ Only EC2 Fleet requests of type `instant` are supported for launching instances into Interruptible Capacity Reservations.
+ Using `OnDemandTargetCapacity` or `SpotTargetCapacity` while also setting `reserved-capacity` as the `DefaultTargetCapacityType` is not supported.
+ When you specify multiple launch templates, each targeting a different Interruptible Capacity Reservation, EC2 Fleet provisions instances across all matching reservations.
+ For Interruptible Capacity Reservations, EC2 Fleet does not fall back to launching On-Demand Instances or Spot Instances for the remainder of the desired target capacity.

## Verify permissions
<a name="ec2-fleet-interruptible-cr-verify-permissions"></a>

Before creating an EC2 Fleet, verify that you have an IAM role with the required permissions. For more information, see [EC2 Fleet prerequisites](ec2-fleet-prerequisites.md).

To launch instances into an Interruptible Capacity Reservation, you must perform the following steps:

## Step 1: Create a launch template
<a name="ec2-fleet-interruptible-cr-step1"></a>

Use the [create-launch-template](https://docs.aws.amazon.com/cli/latest/reference/ec2/create-launch-template.html) command to create a launch template that specifies the Interruptible Capacity Reservation to target. In the launch template, set `MarketType` to `interruptible-capacity-reservation` and specify the `CapacityReservationId` of your Interruptible Capacity Reservation.

Example launch template configuration:

```
{
    "LaunchTemplateName": "{{interruptible-cr-launch-template}}",
    "LaunchTemplateData": {
        "InstanceType": "{{m5.large}}",
        "ImageId": "ami-{{0abcdef1234567890}}",
        "CapacityReservationSpecification": {
            "CapacityReservationTarget": {
                "CapacityReservationId": "{{cr-0123456789abcdef0}}"
            }
        },
        "InstanceMarketOptions": {
            "MarketType": "interruptible-capacity-reservation"
        }
    }
}
```

Example output

```
{
    "LaunchTemplate": {
        "LaunchTemplateId": "lt-0123456789example",
        "LaunchTemplateName": "interruptible-cr-launch-template",
        "CreateTime": "2026-03-12T10:00:00.000Z",
        "CreatedBy": "arn:aws:iam::123456789012:user/Admin",
        "DefaultVersionNumber": 1,
        "LatestVersionNumber": 1
    }
}
```

For more information, see [Create an Amazon EC2 launch template](create-launch-template.md).

## Step 2: Configure the EC2 Fleet
<a name="ec2-fleet-interruptible-cr-step2"></a>

Create a configuration file for the EC2 Fleet that specifies the launch template and target capacity. The following configuration uses the launch template `interruptible-cr-launch-template` that you created in Step 1.

You must specify `ReservedCapacityOptions` with `ReservationType` set to `interruptible-capacity-reservation` when using `reserved-capacity` as the `DefaultTargetCapacityType`.

Create a file named `config.json` with the following content:

```
{
    "LaunchTemplateConfigs": [
        {
            "LaunchTemplateSpecification": {
                "LaunchTemplateName": "{{interruptible-cr-launch-template}}",
                "Version": "1"
            },
            "Overrides": [
                {
                    "InstanceType": "{{m5.large}}",
                    "AvailabilityZone": "{{us-east-1a}}"
                }
            ]
        }
    ],
    "TargetCapacitySpecification": {
        "TotalTargetCapacity": {{10}},
        "DefaultTargetCapacityType": "reserved-capacity"
    },
    "ReservedCapacityOptions": {
        "ReservationType": ["interruptible-capacity-reservation"]
    },
    "Type": "instant"
}
```

Key configuration parameters:


| Parameter | Description | 
| --- | --- | 
| DefaultTargetCapacityType | Set to reserved-capacity to indicate that instances should be launched into reserved capacity. | 
| ReservedCapacityOptions | Specifies the type of reserved capacity. For Interruptible Capacity Reservations, set ReservationType to ["interruptible-capacity-reservation"]. | 
| Type | Must be set to instant. Only instant fleets are supported for Interruptible Capacity Reservations. | 

## Step 3: Launch the fleet and view results
<a name="ec2-fleet-interruptible-cr-step3"></a>

Use the [create-fleet](https://docs.aws.amazon.com/cli/latest/reference/ec2/create-fleet.html) command to create the fleet:

```
aws ec2 create-fleet \
    --cli-input-json file://config.json
```

After you create the `instant` fleet using the preceding configuration, EC2 Fleet launches 10 instances into the Interruptible Capacity Reservation to meet the target capacity.

**Note**  
If the fleet cannot fulfill the full target capacity, the response includes the instances that were launched and any errors for unfulfilled capacity.

Example output

```
{
    "FleetId": "fleet-12345678-1234-1234-1234-123456789012",
    "Instances": [
        {
            "LaunchTemplateAndOverrides": {
                "LaunchTemplateSpecification": {
                    "LaunchTemplateId": "lt-0123456789example",
                    "Version": "1"
                },
                "Overrides": {
                    "InstanceType": "m5.large",
                    "AvailabilityZone": "us-east-1a"
                }
            },
            "Lifecycle": "interruptible-capacity-reservation",
            "InstanceIds": [
                "i-0123456789example1",
                "i-0123456789example2",
                "i-0123456789example3",
                "i-0123456789example4",
                "i-0123456789example5",
                "i-0123456789example6",
                "i-0123456789example7",
                "i-0123456789example8",
                "i-0123456789example9",
                "i-0123456789example0"
            ],
            "InstanceType": "m5.large",
            "Platform": "Linux/UNIX"
        }
    ],
    "Errors": []
}
```

For more information, see [Create an EC2 Fleet](create-ec2-fleet.md).

## Clean up
<a name="ec2-fleet-interruptible-cr-cleanup"></a>

To stop incurring charges, terminate the instances when they are no longer needed. Note that EC2 also terminates instances launched into an Interruptible Capacity Reservation automatically when the capacity owner reclaims the capacity.

## Related resources
<a name="ec2-fleet-interruptible-cr-related-resources"></a>
+ [Interruptible Capacity Reservations](interruptible-capacity-reservations.md)
+ [Reserve compute capacity with EC2 On-Demand Capacity Reservations](ec2-capacity-reservations.md)
+ [Work with EC2 Fleet](manage-ec2-fleet.md)
+ [Create an EC2 Fleet](create-ec2-fleet.md)
+ [Store instance launch parameters in Amazon EC2 launch templates](ec2-launch-templates.md)