# Set a spending limit for your EC2 Fleet or

Spot Fleet

You can set a limit on how much you're willing to spend per hour on your EC2 Fleet or Spot Fleet.
When your spending limit is reached, the fleet stops launching instances, even if the
target capacity hasn't been reached.

There are separate spending limits for On-Demand Instances and Spot Instances.

###### To configure a spending limit for On-Demand Instances and Spot Instances in your EC2 Fleet

Use the [create-fleet](../../../cli/latest/reference/ec2/create-fleet.md "../../../cli/latest/reference/ec2/create-fleet.md")
command and the following parameters:

- For On-Demand Instances: In the `OnDemandOptions` structure, specify your
  spending limit in the `MaxTotalPrice` field.
- For Spot Instances: In the `SpotOptions` structure, specify your spending
  limit in the `MaxTotalPrice` field.

###### To configure a spending limit for On-Demand Instances and Spot Instances in your Spot Fleet

You can use the Amazon EC2 console or the AWS CLI to configure your spending
limit.

(Console) When creating the Spot Fleet, select the **Set maximum cost for Spot Instances**
checkbox, and then enter a value for **Set your max cost (per hour)**.
For more information, see step 6.e. in [Create a Spot Fleet request using defined
parameters](create-spot-fleet.md#create-spot-fleet-advanced "create-spot-fleet.md#create-spot-fleet-advanced").

(AWS CLI) Use the [request-spot-fleet](../../../cli/latest/reference/ec2/request-spot-fleet.md "../../../cli/latest/reference/ec2/request-spot-fleet.md")
command and the following parameters:

- For On-Demand Instances: Specify your spending limit in the
  `OnDemandMaxTotalPrice` field.
- For Spot Instances: Specify your spending limit in the `SpotMaxTotalPrice`
  field.

## Examples

The following examples show two different scenarios. In the first example, the
fleet stops launching On-Demand Instances when it has met the target capacity set for On-Demand Instances
(`OnDemandTargetCapacity`). In the second example, the fleet stops
launching On-Demand Instances when it has reached the maximum amount you’re willing to pay per
hour for On-Demand Instances (`MaxTotalPrice`).

**Example: Stop launching On-Demand Instances when target capacity is
reached**

Given a request for `m4.large` On-Demand Instances, where:

- On-Demand Price: $0.10 per hour
- `OnDemandTargetCapacity`: 10
- `MaxTotalPrice`: $1.50

The fleet launches 10 On-Demand Instances because the total of $1.00 (10 instances x $0.10)
does not exceed the `MaxTotalPrice` of $1.50 for On-Demand Instances.

**Example: Stop launching On-Demand Instances when maximum total price is
reached**

Given a request for `m4.large` On-Demand Instances, where:

- On-Demand Price: $0.10 per hour
- `OnDemandTargetCapacity`: 10
- `MaxTotalPrice`: $0.80

If the fleet launches the On-Demand target capacity (10 On-Demand Instances), the total cost
per hour would be $1.00. This is more than the amount ($0.80) specified for
`MaxTotalPrice` for On-Demand Instances. To prevent spending more than you're
willing to pay, the fleet launches only 8 On-Demand Instances (below the On-Demand target
capacity) because launching more would exceed the `MaxTotalPrice` for
On-Demand Instances.

## Burstable performance

instances

If you launch your Spot Instances using a [burstable performance instance type](burstable-performance-instances.md "burstable-performance-instances.md"), and if you plan to use your
burstable performance Spot Instances immediately and for a short duration, with no idle time
for accruing CPU credits, we recommend that you launch them in [Standard mode](burstable-performance-instances-standard-mode.md "burstable-performance-instances-standard-mode.md") to
avoid paying higher costs. If you launch burstable performance Spot Instances in [Unlimited mode](burstable-performance-instances-unlimited-mode.md "burstable-performance-instances-unlimited-mode.md")
and burst CPU immediately, you'll spend surplus credits for bursting. If you use the
instance for a short duration, the instance doesn't have time to accrue CPU credits
to pay down the surplus credits, and you are charged for the surplus credits when
you terminate the instance.

Unlimited mode is suitable for burstable performance Spot Instances only if the instance
runs long enough to accrue CPU credits for bursting. Otherwise, paying for surplus
credits makes burstable performance Spot Instances more expensive than using other instances.
For more information, see [When to use unlimited mode versus fixed
CPU](burstable-performance-instances-unlimited-mode-concepts.md#when-to-use-unlimited-mode "burstable-performance-instances-unlimited-mode-concepts.md#when-to-use-unlimited-mode").

Launch credits are meant to provide a productive initial launch experience for T2
instances by providing sufficient compute resources to configure the instance.
Repeated launches of T2 instances to access new launch credits is not permitted. If
you require sustained CPU, you can earn credits (by idling over some period), use
[Unlimited
mode](burstable-performance-instances-unlimited-mode.md "burstable-performance-instances-unlimited-mode.md") for T2 Spot Instances, or use an instance type with dedicated CPU.
