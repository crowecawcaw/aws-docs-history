# Managing On-Demand instances

and Spot instances

You can launch and automatically scale a fleet of On-Demand Instances and Spot Instances
within a single Auto Scaling group. The following options can be used in tandem to configure how the
Auto Scaling service manages Spot Instances and On-Demand Instances in your environment.

You can configure these options for your environment using the [Elastic Beanstalk console](environments-cfg-autoscaling-configuration-approaches.md#environments-cfg-autoscaling-console "environments-cfg-autoscaling-configuration-approaches.md#environments-cfg-autoscaling-console"), [namespace configuration options](environments-cfg-autoscaling-configuration-approaches.md#environments-cfg-autoscaling-namespace "environments-cfg-autoscaling-configuration-approaches.md#environments-cfg-autoscaling-namespace"),
the [AWS CLI](environments-cfg-autoscaling-configuration-approaches.md#environments-cfg-autoscaling-aws-cli "environments-cfg-autoscaling-configuration-approaches.md#environments-cfg-autoscaling-aws-cli"), or the [EB CLI](environments-cfg-autoscaling-configuration-approaches.md#environments-cfg-autoscaling-ebcli "environments-cfg-autoscaling-configuration-approaches.md#environments-cfg-autoscaling-ebcli").

These options are part of the [aws:ec2:instances](command-options-general.md#command-options-general-ec2instances "command-options-general.md#command-options-general-ec2instances") namespace:

- `EnableSpot` ‐ When set to `true` this setting enables
  Spot Instance requests for your environment.
- `SpotFleetOnDemandBase` ‐ Sets the minimum number of On-Demand
  Instances that your Auto Scaling group provisions before considering Spot Instances as your
  environment scales up.
- `SpotFleetOnDemandAboveBasePercentage` ‐ The percentage of On-Demand
  Instances as part of additional capacity that your Auto Scaling group provisions beyond the
  `SpotOnDemandBase` instances.
  The previously listed options correlate with the following options in the [aws:autoscaling:asg](command-options-general.md#command-options-general-autoscalingasg "command-options-general.md#command-options-general-autoscalingasg")
  namespace:

- `MinSize` ‐ The minimum number of instances that you want in your
  Auto Scaling group.
- `MaxSize` ‐ The maximum number of instances that you want in your
  Auto Scaling group.

###### Important

The `EnableSpot`
option setting can cause Elastic Beanstalk to migrate an existing environment with launch configurations to launch
templates. Doing so requires the necessary permissions to manage launch templates. These permissions are included in our managed policy. If you use custom
policies instead of our managed policies, environment creation or updates might fail when you update your environment
configuration. For more information
and other considerations, see [Migrating your Elastic Beanstalk
environment to launch templates](environments-cfg-autoscaling-launch-templates.md "environments-cfg-autoscaling-launch-templates.md") .

## Applying both sets

of namespace options

The following points describe how the combination of these option settings affects the
scaling for your environment.

- Only `MinSize` determines your environment’s initial capacity—the
  number of instances you want running at a minimum.
- `SpotFleetOnDemandBase` doesn't affect initial capacity. When Spot is
  enabled, this option determines how many On-Demand Instances are provisioned before
  any Spot Instances are considered.
- Consider when `SpotFleetOnDemandBase` is less than
  `MinSize`. You'll still get exactly `MinSize` instances as
  initial capacity. At least `SpotFleetOnDemandBase` of them must be
  On-Demand Instances.
- Consider when `SpotFleetOnDemandBase` is greater than
  `MinSize`. As your environment scales out, you're guaranteed to get at
  least an additional amount of instances equal to the difference between the two
  values. In other words, you're guaranteed to get at least an additional
  `(SpotFleetOnDemandBase - MinSize)` instances that are On-Demand before
  satisfying the `SpotFleetOnDemandBase` requirement.

###### Single-instance environments

In production environments, Spot Instances are particularly useful as part of a
scalable, load-balanced environment. We don't recommend using Spot in a single-instance
environment. If Spot Instances aren't available, you might lose the entire capacity (a
single instance) of your environment. You may still wish to use a Spot Instance in a
single instance environment for development or testing. When you do, be sure to set both
`SpotFleetOnDemandBase` and
`SpotFleetOnDemandAboveBasePercentage` to zero. Any other settings result
in an On-Demand Instance.

## Examples of

scaling options settings

The following examples demonstrate different scenarios of setting the various scaling
options. All examples assume a load-balanced environment with Spot Instance requests
enabled.

###### Example 1: On-Demand and Spot as part

of initial capacity

| Option settings                        | **Option**            | **Namespace** | **Value** |
| -------------------------------------- | --------------------- | ------------- | --------- |
| `MinSize`                              | `aws:autoscaling:asg` | `10`          |
| `MaxSize`                              | `aws:autoscaling:asg` | `24`          |
| `SpotFleetOnDemandBase`                | `aws:ec2:instances`   | `4`           |
| `SpotFleetOnDemandAboveBasePercentage` | `aws:ec2:instances`   | `50`          |

In this example, the environment starts with ten instances, of which seven are
On-Demand (four base, and 50% of the six above base) and three are Spot. The environment
can scale out up to 24 instances. As it scales out, the portion of On-Demand in the part
of the fleet above the four base On-Demand instances is kept at 50%, up to a maximum of 24
instances overall, of which 14 are On-Demand (four base, and 50% of the 20 above base) and
ten are Spot.

###### Example 2: All On-Demand initial

capacity

| Option settings                        | **Option**            | **Namespace** | **Value** |
| -------------------------------------- | --------------------- | ------------- | --------- |
| `MinSize`                              | `aws:autoscaling:asg` | `4`           |
| `MaxSize`                              | `aws:autoscaling:asg` | `24`          |
| `SpotFleetOnDemandBase`                | `aws:ec2:instances`   | `4`           |
| `SpotFleetOnDemandAboveBasePercentage` | `aws:ec2:instances`   | `50`          |

In this example, the environment starts with four instances, all of which are
On-Demand. The environment can scale out up to 24 instances. As it scales out, the portion
of On-Demand in the part of the fleet above the four base On-Demand instances is kept at
50%, up to a maximum of 24 instances overall, of which 14 are On-Demand (four base, and
50% of the 20 above base) and ten are Spot.

###### Example 3: Additional On-Demand base

beyond initial capacity

| Option settings                        | **Option**            | **Namespace** | **Value** |
| -------------------------------------- | --------------------- | ------------- | --------- |
| `MinSize`                              | `aws:autoscaling:asg` | `3`           |
| `MaxSize`                              | `aws:autoscaling:asg` | `24`          |
| `SpotFleetOnDemandBase`                | `aws:ec2:instances`   | `4`           |
| `SpotFleetOnDemandAboveBasePercentage` | `aws:ec2:instances`   | `50`          |

In this example, the environment starts with three instances, all of which are
On-Demand. The environment can scale out up to 24 instances. The first additional instance
above the initial three is On-Demand, to complete the four base On-Demand instances. As it
scales out further, the portion of On-Demand in the part of the fleet above the four base
On-Demand instances is kept at 50%, up to a maximum of 24 instances overall, of which 14
are On-Demand (four base, and 50% of the 20 above base) and ten are Spot.
