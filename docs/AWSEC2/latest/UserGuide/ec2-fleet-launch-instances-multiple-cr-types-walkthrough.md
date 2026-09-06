

# Tutorial: Configure your EC2 Fleet to launch instances into multiple Capacity Reservation types using a Capacity Reservation Resource Group
<a name="ec2-fleet-launch-instances-multiple-cr-types-walkthrough"></a>

This tutorial walks you through the steps to configure an EC2 Fleet that launches instances across multiple Capacity Reservation types – On-Demand Capacity Reservations (ODCRs), Capacity Blocks for ML, and interruptible Capacity Reservations – using a single Capacity Reservation Resource Group.

You will learn how to create a Capacity Reservation Resource Group that contains different Capacity Reservation types, configure your EC2 Fleet to prioritize the Capacity Reservation types in a specific order, and optionally fall back to On-Demand capacity when reserved capacity is insufficient to meet your target.

## Considerations
<a name="ec2-fleet-multiple-cr-types-considerations"></a>
+ Only EC2 Fleet requests of type `instant` are supported when using `ReservedCapacityOptions`.
+ You must explicitly specify which Capacity Reservation types to target in the `ReservationTypes` list. EC2 Fleet launches instances only into the Capacity Reservation types that you specify.
+ `ReservedCapacityOptions` is mutually exclusive with `OnDemandOptions.CapacityReservationOptions`. You can't use both in the same EC2 Fleet request.

This tutorial assumes that you already have the following Capacity Reservations in your account:
+ An ODCR (`cr-1234567890abcdef1`) for `p5.48xlarge` in `us-east-1a`
+ An ODCR (`cr-abcdef1234567890a`) for `p4d.48xlarge` in `us-east-1b`
+ A Capacity Block (`cr-0123456789abcdef0`) for `p5.48xlarge` in `us-east-1a`
+ An interruptible Capacity Reservation (`cr-9876543210fedcba9`) for `p5.48xlarge` in `us-east-1a`, shared with you by another account in your organization

## Verify permissions
<a name="ec2-fleet-multiple-cr-types-verify-permissions"></a>

Before creating an EC2 Fleet, verify that you have an IAM role with the required permissions. For more information, see [EC2 Fleet prerequisites](ec2-fleet-prerequisites.md).

## Step 1: Create a Capacity Reservation Resource Group
<a name="ec2-fleet-multiple-cr-types-step1"></a>

Create a Capacity Reservation Resource Group to hold the Capacity Reservations that your EC2 Fleet targets. Configure the group so that it accepts Capacity Reservations of any instance type and Capacity Reservation type, which allows the group to hold a mix of Capacity Reservation types. For step-by-step instructions, see [Capacity Reservation groups](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/cr-groups.html).

**Note**  
When you create the group, do not specify the `instance-type` or `reservation-type` parameters in the `AWS::EC2::CapacityReservationPool` configuration. Omitting these parameters allows the group to accept Capacity Reservations of any instance type and Capacity Reservation type.

## Step 2: Add Capacity Reservations to the group
<a name="ec2-fleet-multiple-cr-types-step2"></a>

Add your Capacity Reservations to the Capacity Reservation Resource Group. You can add any combination of ODCRs, Capacity Blocks for ML, interruptible Capacity Reservations, and UltraServer Capacity Blocks. For this tutorial, add the four Capacity Reservations listed at the beginning of this tutorial. For step-by-step instructions, see [Capacity Reservation groups](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/cr-groups.html).

## Step 3: Create a launch template
<a name="ec2-fleet-multiple-cr-types-step3"></a>

Use the [create-launch-template](https://docs.aws.amazon.com/cli/latest/reference/ec2/create-launch-template.html) command to create a launch template that targets the Capacity Reservation Resource Group. When you use `ReservedCapacityOptions` in your EC2 Fleet configuration, you do not need to set a `MarketType` in the launch template – EC2 Fleet sets this automatically for each Capacity Reservation type.

```
aws ec2 create-launch-template \
    --launch-template-name {{my-cr-resource-group-template}} \
    --launch-template-data \
        '{"ImageId": "ami-{{0123456789example}}",
          "CapacityReservationSpecification":
            {"CapacityReservationTarget":
                {"CapacityReservationResourceGroupArn": "arn:aws:resource-groups:{{us-east-1}}:{{123456789012}}:group/{{my-cr-resource-group}}"}
            }
        }'
```

## Step 4: Create an EC2 Fleet
<a name="ec2-fleet-multiple-cr-types-step4"></a>

Create an EC2 Fleet that targets multiple Capacity Reservation types in your Capacity Reservation Resource Group. The key configuration is `ReservedCapacityOptions`, which specifies the following:
+ `ReservationTypes` – An ordered list of Capacity Reservation types to target. EC2 Fleet works through the types in this order. Valid values are `on-demand-capacity-reservation`, `capacity-block`, and `interruptible-capacity-reservation`.
+ `AllocationStrategy` – How instance types are prioritized within each Capacity Reservation type. Set to `prioritized` to follow your instance type override order.
+ `ReservedCapacityFallbackOptions` – Set `MarketTypes` to `["on-demand"]` to launch On-Demand Instances when reserved capacity is insufficient. If you don't specify fallback options, EC2 Fleet does not fall back to any other market type after the specified Capacity Reservation types are exhausted.

Create a file named `config.json` with the following content. In the following example, replace the resource identifiers with your own resource identifiers.

```
{
    "LaunchTemplateConfigs": [
        {
            "LaunchTemplateSpecification": {
                "LaunchTemplateName": "{{my-cr-resource-group-template}}",
                "Version": "1"
            },
            "Overrides": [
                {
                    "InstanceType": "{{p5.48xlarge}}",
                    "AvailabilityZone": "{{us-east-1a}}",
                    "Priority": 1
                },
                {
                    "InstanceType": "{{p4d.48xlarge}}",
                    "AvailabilityZone": "{{us-east-1b}}",
                    "Priority": 2
                }
            ]
        }
    ],
    "TargetCapacitySpecification": {
        "TotalTargetCapacity": {{100}},
        "DefaultTargetCapacityType": "reserved-capacity"
    },
    "ReservedCapacityOptions": {
        "ReservationTypes": ["on-demand-capacity-reservation", "capacity-block", "interruptible-capacity-reservation"],
        "ReservedCapacityFallbackOptions": {
            "MarketTypes": ["on-demand"]
        },
        "AllocationStrategy": "prioritized"
    },
    "Type": "instant"
}
```

Use the [create-fleet](https://docs.aws.amazon.com/cli/latest/reference/ec2/create-fleet.html) command to launch the fleet:

```
aws ec2 create-fleet --cli-input-json file://config.json
```

For more information, see [Create an EC2 Fleet](create-ec2-fleet.md).

**How EC2 Fleet resolves Capacity Reservations**  
Based on the preceding configuration, EC2 Fleet attempts to launch instances in the following order:

1. **ODCRs** – `p5.48xlarge` reservations first (the highest priority instance type), and then `p4d.48xlarge` reservations. Within each instance type, if multiple ODCRs exist, one is selected at random.

1. **Capacity Blocks** – If no available capacity remains across all ODCRs, EC2 Fleet targets Capacity Blocks. `p5.48xlarge` reservations first, and then `p4d.48xlarge`, selected at random within each instance type.

1. **Interruptible Capacity Reservations** – If no available capacity remains across all Capacity Blocks, EC2 Fleet targets interruptible Capacity Reservations. `p5.48xlarge` reservations first, and then `p4d.48xlarge`, selected at random within each instance type.

1. **On-Demand fallback** – If reserved capacity is insufficient to meet the target of 100 instances, the remaining capacity is launched as On-Demand Instances. EC2 Fleet launches these On-Demand Instances according to the allocation strategy that you specify in `OnDemandOptions`.

**Note**  
EC2 Fleet resolves the Capacity Reservation type first, and then the instance type within each Capacity Reservation type. Each Capacity Reservation type is fully exhausted before EC2 Fleet moves to the next type in the ordered list.

## (Optional) Step 5: Verify instance properties
<a name="ec2-fleet-multiple-cr-types-step5"></a>

Use the [describe-instances](https://docs.aws.amazon.com/cli/latest/reference/ec2/describe-instances.html) command to verify which Capacity Reservation type each instance consumed. Instances launched by the fleet display the following properties.


| Property | On-Demand Capacity Reservation value | Capacity Block value | Interruptible Capacity Reservation value | On-Demand value | 
| --- | --- | --- | --- | --- | 
| instance-lifecycle | null | capacity-block | interruptible-capacity-reservation | null | 
| capacity-reservation-id | Capacity Reservation ID consumed | Capacity Reservation ID consumed | Capacity Reservation ID consumed | Not present | 
| capacity-reservation-specification | Group ARN | Group ARN | Group ARN | Not present | 

You can filter instances by Capacity Reservation Resource Group using the following command:

```
aws ec2 describe-instances \
    --filters "Name=capacity-reservation-specification.capacity-reservation-target.capacity-reservation-resource-group-arn,Values=arn:aws:resource-groups:{{us-east-1}}:{{123456789012}}:group/{{my-cr-resource-group}}"
```

## Clean up
<a name="ec2-fleet-multiple-cr-types-cleanup"></a>

To stop incurring charges, terminate the instances when they are no longer needed. Note that instances launched into Capacity Blocks are automatically terminated when the Capacity Block reservation ends. Instances launched into interruptible Capacity Reservations are automatically terminated if the capacity owner reclaims the capacity.

## Related resources
<a name="ec2-fleet-multiple-cr-types-related-resources"></a>
+ [Capacity Reservation groups](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/cr-groups.html)
+ [Capacity Blocks for ML](ec2-capacity-blocks.md)
+ [Interruptible Capacity Reservations](interruptible-capacity-reservations.md)
+ [Reserve compute capacity with EC2 On-Demand Capacity Reservations](ec2-capacity-reservations.md)
+ [Work with EC2 Fleet](manage-ec2-fleet.md)
+ [Create an EC2 Fleet](create-ec2-fleet.md)
+ [Store instance launch parameters in Amazon EC2 launch templates](ec2-launch-templates.md)