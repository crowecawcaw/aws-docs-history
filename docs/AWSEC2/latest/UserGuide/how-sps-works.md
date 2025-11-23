# How Spot placement score works

When you use the Spot placement score feature, you first specify your compute requirements for your
Spot Instances, and then Amazon EC2 returns the top 10
Regions or Availability
Zones where your Spot request is likely to succeed. Each Region or Availability Zone is
scored on a scale from 1 to 10, with 10 indicating that your Spot request is highly
likely to succeed, and 1 indicating that your Spot request is not likely to
succeed.

###### To use the Spot placement score feature, follow these steps:

- [Step 1: Specify your Spot
  requirements](#sps-specify-requirements "#sps-specify-requirements")
- [Step 2: Filter the Spot placement score response](#get-sps "#get-sps")
- [Step 3: Review the recommendations](#sps-recommendations "#sps-recommendations")
- [Step 4: Use the recommendations](#sps-use-recommendations "#sps-use-recommendations")

## Step 1: Specify your Spot

requirements

First, you specify your desired target Spot capacity and your compute
requirements, as follows:

1. Specify the target Spot capacity, and optionally the
   target capacity unit.

You can specify your desired target Spot capacity in terms of the number
of instances or vCPUs, or in terms of the amount of memory in MiB. To
specify the target capacity in number of vCPUs or amount of memory, you must
specify the target capacity unit as `vcpu` or
`memory-mib`. Otherwise, it defaults to number of
instances.

By specifying your target capacity in terms of the number of vCPUs or the
amount of memory, you can use these units when counting the total capacity.
For example, if you want to use a mix of instances of different sizes, you
can specify the target capacity as a total number of vCPUs. The Spot placement score
feature then considers each instance type in the request by its number of
vCPUs, and counts the total number of vCPUs rather than the total number of
instances when totaling up the target capacity.

For example, say you specify a total target capacity of 30 vCPUs, and your
instance type list consists of c5.xlarge (4 vCPUs), m5.2xlarge (8 vCPUs),
and r5.large (2 vCPUs). To achieve a total of 30 vCPUs, you could get a mix
of 2 c5.xlarge (2\*4 vCPUs), 2 m5.2xlarge (2\*8 vCPUs), and 3 r5.large (3\*2
vCPUs). 2. Specify instance types or instance
attributes.

You can either specify the instance types to use, or you can specify the
instance attributes that you need for your compute requirements, and then
let Amazon EC2 identify the instance types that have those attributes. This is
known as attribute-based instance type selection.

You can't specify both instance types and instance attributes in the same
Spot placement score request.

If you specify instance types, you must specify at least three different
instance types, otherwise Amazon EC2 will return a low Spot placement score. Similarly, if you
specify instance attributes, they must resolve to at least three different
instance types.

For examples of different ways to specify your Spot requirements, see [Example configurations](work-with-spot-placement-score.md#sps-example-configs "work-with-spot-placement-score.md#sps-example-configs").

## Step 2: Filter the Spot placement score response

Amazon EC2 calculates the Spot placement score for each Region or Availability Zone, and
returns either the top 10 Regions or the top 10 Availability Zones where your Spot
request is likely to succeed. The default is to return a list of scored Regions. If
you plan to launch all of your Spot capacity into a single Availability Zone, then
it's useful to request a list of scored Availability Zones.

You can specify a Region filter to narrow down the Regions that will
be returned in the response.

You can combine the Region filter and a request for scored
Availability Zones. In this way, the scored Availability Zones are confined to the
Regions for which you've filtered. To find the highest-scored Availability Zone in a
Region, specify only that Region, and the response will return a scored list of all
of the Availability Zones in that Region.

## Step 3: Review the recommendations

The Spot placement score for each Region or Availability Zone is calculated based on the target
capacity, the composition of the instance types, the historical and current Spot
usage trends, and the time of the request. Because Spot capacity is constantly
fluctuating, the same Spot placement score request can yield different scores when calculated at
different times.

Regions and Availability Zones are scored on a scale from 1 to 10. A score of 10
indicates that your Spot request is highly likely—but not
guaranteed—to succeed. A score of 1 indicates that your Spot request is not
likely to succeed at all. The same score might be returned for different Regions or
Availability Zones.

If low scores are returned, you can edit your compute requirements and recalculate
the score. You can also request Spot placement score recommendations for the same compute
requirements at different times of the day.

## Step 4: Use the recommendations

A Spot placement score is only relevant if your Spot request has exactly the same configuration
as the Spot placement score configuration (target capacity, target capacity unit, and instance
types or instance attributes), and is configured to use the
`capacity-optimized` allocation strategy. Otherwise, the likelihood
of getting available Spot capacity will not align with the score.

While a Spot placement score serves as a guideline, and no score guarantees that your Spot
request will be fully or partially fulfilled, you can use the following information
to get the best results:

- **Use the same configuration** – The
  Spot placement score is relevant only if the Spot request configuration (target capacity,
  target capacity unit, and instance types or instance attributes) in your
  Amazon EC2 Auto Scaling group, EC2 Fleet, or Spot Fleet is the same as what you entered to get the
  Spot placement score.

If you used attribute-based instance type selection in your Spot placement score request, you can use
attribute-based instance type selection to configure your Amazon EC2 Auto Scaling group, EC2 Fleet,
or Spot Fleet. For more information, see [Create mixed instances group using attribute-based instance type
selection](../../../autoscaling/ec2/userguide/create-mixed-instances-group-attribute-based-instance-type-selection.md "../../../autoscaling/ec2/userguide/create-mixed-instances-group-attribute-based-instance-type-selection.md") and [Specify attributes for
instance type selection for EC2 Fleet or Spot Fleet](ec2-fleet-attribute-based-instance-type-selection.md "ec2-fleet-attribute-based-instance-type-selection.md").

###### Note

If you specified your target capacity in terms of the number of vCPUs
or the amount of memory, and you specified instance types in your Spot
placement score configuration, note that you can’t currently create this
configuration in your Amazon EC2 Auto Scaling group, EC2 Fleet, or Spot Fleet. Instead, you must
manually set the instance weighting by using the
`WeightedCapacity` parameter.

- **Use the `capacity-optimized` allocation
  strategy** – Any score assumes that your fleet request
  will be configured to use all Availability Zones (for requesting capacity
  across Regions) or a single Availability Zone (if requesting capacity
  in one Availability Zone) and the `capacity-optimized` Spot
  allocation strategy for your request for Spot capacity to succeed. If you
  use other allocation strategies, such as `lowest-price`, the
  likelihood of getting available Spot capacity will not align with the
  score.
- **Act on a score immediately** – The
  Spot placement score recommendation reflects the available Spot capacity at the time of the
  request, and the same configuration can yield different scores when
  calculated at different times due to Spot capacity fluctuations. While a
  score of 10 means that your Spot capacity request is highly
  likely—but not guaranteed—to succeed, for best results we
  recommend that you act on a score immediately. We also recommend that you
  get a fresh score each time you attempt a capacity request.
