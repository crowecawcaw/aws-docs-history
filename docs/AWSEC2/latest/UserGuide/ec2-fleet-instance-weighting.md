# Use instance weighting to manage cost and

performance of your EC2 Fleet or Spot Fleet

With instance weighting, you assign a weight to each instance type in your EC2 Fleet or
Spot Fleet to represent their compute capacity and performance relative to each other. Based
on the weights, the fleet can use any combination of the specified instance types, as
long as it can fulfil the desired target capacity. This can help you manage the cost and
performance of your fleet.

The weight represents the capacity units that an instance type contributes to the
total target capacity.

**Example: Use instance weighting for performance
management**

Suppose your fleet has two instance types, and you assign a different weight to each
instance type to reflect how many you need of each to achieve the same performance, as
follows:

- `m5.large` – weight: 1
- `m5.2xlarge` – weight: 4
  By assigning these weights, you're saying that you'd need 4 `m5.large`
  instances to achieve the same performance as 1 `m5.2xlarge`.

To calculate how many instances of each instance type are needed for a given target
capacity, use the following formula:

`target capacity / weight = number of instances`

If your target capacity is 8 units, the fleet could fulfill the target capacity with
either `m5.large` or `m5.2xlarge`, or a mix of both, as
follows:

- 8 `m5.large` instances (capacity of 8 / weight of 1 = 8
  instances)
- 2 `m5.2xlarge` instances (capacity of 8 / weight of 4 = 2
  instances)
- 4 `m5.large` and 1 `m5.2xlarge`
  **Example: Use instance weighting for cost
  management**

By default, the price that you specify is per _instance_ hour. When you use the instance weighting feature, the price
that you specify is per _unit_ hour. You can calculate
your price per unit hour by dividing your price for an instance type by the number of
units that it represents. The fleet calculates the number of instances to launch by
dividing the target capacity by the instance weight. If the result isn't an integer, the
fleet rounds it up to the next integer, so that the size of your fleet is not below its
target capacity. The fleet can select any pool that you specify in your launch
specification, even if the capacity of the instances launched exceeds the requested
target capacity.

The following table includes examples of calculations to determine the price per unit
for a fleet with a target capacity of 10.

| Instance type | Instance weight | Target capacity | Number of instances launched           | Price per instance hour | Price per unit hour        |
| ------------- | --------------- | --------------- | -------------------------------------- | ----------------------- | -------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `r3.xlarge`   | 2               | 10              | 5 (10 divided by 2)                    | $0.05                   | $0.025 (.05 divided by 2)  |
| `r3.8xlarge`  | 8               | 10              | 2 (10 divided by 8, result rounded up) | $0.10                   | $0.0125 (.10 divided by 8) | Use the fleet instance weighting as follows to provision the target capacity that you want in the pools with the lowest price per unit at the time of fulfillment: 1. Set the target capacity for your fleet either in instances (the default) or in the units of your choice, such as vCPU, memory, storage, or throughput. 2. Set the price per unit. 3. For each launch specification, specify the weight, which is the number of units that the instance type represents toward the target capacity. ###### Instance weighting example Consider a fleet request with the following configuration: <br>• A target capacity of 24 <br>• A launch specification with an instance type `r3.2xlarge` and a weight of 6 <br>• A launch specification with an instance type `c3.xlarge` and a weight of 5 The weights represent the number of units that instance type represents toward the target capacity. If the first launch specification provides the lowest price per unit (price for `r3.2xlarge` per instance hour divided by 6), the fleet would launch four of these instances (24 divided by 6). If the second launch specification provides the lowest price per unit (price for `c3.xlarge` per instance hour divided by 5), the fleet would launch five of these instances (24 divided by 5, result rounded up). ###### Instance weighting and allocation strategy Consider a fleet request with the following configuration: <br>• A target capacity of 30 Spot Instances <br>• A launch specification with an instance type `c3.2xlarge` and a weight of 8 <br>• A launch specification with an instance type `m3.xlarge` and a weight of 8 <br>• A launch specification with an instance type `r3.xlarge` and a weight of 8 The fleet would launch four instances (30 divided by 8, result rounded up). With the `diversified` strategy, the fleet launches one instance in each of the three pools, and the fourth instance in whichever of the three pools provides the lowest price per unit. |
