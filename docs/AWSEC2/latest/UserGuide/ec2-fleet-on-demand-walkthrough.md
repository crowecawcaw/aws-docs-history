# Tutorial: Configure EC2 Fleet to use On-Demand Instances

as the primary capacity

This tutorial uses a fictitious company called ABC Online to illustrate the process of
requesting an EC2 Fleet with On-Demand as the primary capacity, and Spot capacity if
available.

## Objective

ABC Online, a restaurant delivery company, aims to provision Amazon EC2 capacity across
EC2 instance types and purchasing options to achieve their desired scale,
performance, and cost.

## Plan

ABC Online requires a fixed capacity to handle peak periods, but would like to
benefit from additional capacity at a lower cost. The company determines the
following requirements for their EC2 Fleet:

- On-Demand Instance capacity – ABC Online requires 15 On-Demand Instances to ensure that they
  can accommodate traffic at peak periods.
- Spot Instance capacity – To enhance performance, but at a lower price, ABC
  Online plans to provision 5 Spot Instances.

## Verify

permissions

Before creating an EC2 Fleet, ABC Online verifies that it has an IAM role with the
required permissions. For more information, see [EC2 Fleet prerequisites](ec2-fleet-prerequisites.md "ec2-fleet-prerequisites.md").

## Create a

launch template

Next, ABC Online creates a launch template. The launch template ID is used in the
following step. For more information, see [Create an Amazon EC2 launch template](create-launch-template.md "create-launch-template.md").

## Create the EC2 Fleet

ABC Online creates a file, `config.json`, with the following
configuration for its EC2 Fleet. In the following example, replace the resource
identifiers with your own resource identifiers.

```
{
    "LaunchTemplateConfigs": [
        {
            "LaunchTemplateSpecification": {
                "LaunchTemplateId": "`lt-07b3bc7625cdab851`",
                "Version": "`2`"
            }

        }
    ],
    "TargetCapacitySpecification": {
        "TotalTargetCapacity": 20,
        "OnDemandTargetCapacity":15,
        "DefaultTargetCapacityType": "spot"
    }
}
```

ABC Online creates the EC2 Fleet using the following [create-fleet](../../../cli/latest/reference/ec2/create-fleet.md "../../../cli/latest/reference/ec2/create-fleet.md") command.

```
aws ec2 create-fleet --cli-input-json file://config.json
```

For more information, see [Create an EC2 Fleet](create-ec2-fleet.md "create-ec2-fleet.md").

## Fulfillment

The allocation strategy determines that the On-Demand capacity is always
fulfilled, while the balance of the target capacity is fulfilled as Spot if there is
available capacity.
