

# Instance type and Availability Zone breakdown
<a name="capacity-manager-pool-breakdown"></a>

After you confirm at the request level that Amazon EC2 is fulfilling your requested capacity, per-combination metrics help you optimize where that capacity lands. Per-combination metrics take each option within a flexible request into account and show how each individual instance type and Availability Zone combination performed, which affects your cost, performance, and reservation utilization. They're most useful at the account level. In the console, drill into an account on the Capacity fulfillment tab, then choose View instance type and Availability Zone breakdown on any fulfillment row. Capacity Manager sorts combinations by fulfillment rate, lowest first, so the combinations with the most room to improve appear at the top.


| Metric | Description | Unit | 
| --- | --- | --- | 
| InstAzFulfillmentRate | Fulfilled divided by requested for each instance type and Availability Zone combination. A fallback earns no credit. This metric is vCPU-weighted. | Percentage | 
| SpotInstAzFulfillmentRate | Fulfilled divided by requested for each Spot instance type and Availability Zone combination. A fallback earns no credit. This metric is vCPU-weighted. | Percentage | 
| CapacityTotalFulfilledVcpu (with instance type and Availability Zone dimensions) | vCPUs delivered to each instance type and Availability Zone combination. These add up to the Level 1 Fulfilled total. | vCPUs | 
| SpotCapacityTotalFulfilledVcpu (with instance type and Availability Zone dimensions) | Spot vCPUs delivered to each instance type and Availability Zone combination. These add up to the Level 1 Fulfilled total. | vCPUs | 
| UnreservedTotalUsageHrsVcpu \+ ReservedTotalUsageHrsVcpu (added together in the console, with SpotTotalUsageHrsVcpu for Spot) | Compute time on each instance type and Availability Zone combination. These add up to the Level 1 total. | vCPU-hours | 

Dimensions available: instance type, instance family, Availability Zone ID, tag, account ID, account name, Region.

**Note**  
When you query `InstAzFulfillmentRate`, the request must include the Availability Zone ID dimension and at least one of instance type or instance family. The per-combination fulfillment rate is only meaningful at instance type and Availability Zone granularity, and it does not reconcile with the request-level fulfillment rate at higher aggregation levels.

**How the instance type and Availability Zone breakdown is calculated**
+ **Per-combination fulfillment rate** — It is volume-based. If an instance type and Availability Zone combination was asked for 1,000 vCPUs and delivered 620, its rate is 62%. Partial delivery counts proportionally. Per-combination rates do not average up to the request-level rate, because a single request can ask from multiple combinations.
+ **Fulfilled (per combination)** — The `CapacityTotalFulfilledVcpu` metric broken down by instance type and Availability Zone. Per-combination values sum to the request-level total.
+ **Usage (per combination)** — Existing usage metrics extended with instance type and Availability Zone dimensions, showing how long instances ran on each combination. Per-combination values sum to the request-level total.

The per-combination fulfillment rate appears only for instance type and Availability Zone combinations that had a capacity request evaluated during the period. A combination that was never reached (because a higher-priority combination succeeded first) doesn't appear.

**When request-level fulfillment is high but per-combination fulfillment is low**

This is the most common scenario, and it means your requested capacity is being fulfilled but not always landing where you prefer. For example, a 98% request-level fulfillment rate with a 58% instance type-AZ fulfillment rate on `c7i.8xlarge` means Amazon EC2 delivered from that instance type and Availability Zone combination 58% of the time you asked — and a fallback combination covered the rest, so you still got capacity. This is an optimization signal, not an alarm.
+ **When to act** — The cost difference matters (larger fallback instances cost more), you hold reservations on the preferred type that are going unused, or performance differs between types in a way that affects your application.
+ **When not to act** — Your request-level fulfillment rate is near 100% and the fallback types meet your performance and cost requirements. A lower per-combination rate on one or two instance type and Availability Zone combinations then shows why your configuration is resilient — it's working as designed.

**To improve per-combination fulfillment**
+ **Reserve capacity for combinations you prefer** — An On-Demand Capacity Reservation ensures capacity for a preferred instance type and Availability Zone combination regardless of overall demand.
+ **Add high-performing alternatives** — If c7i has a 60% instance type-AZ fulfillment rate and m7i is at 97%, adding m7i gives Amazon EC2 a highly available alternative to draw from.

The following JSON structure shows a constrained instance type and Availability Zone combination alongside a healthy fallback combination.

```
{
    "MetricDataResults": [
        {
            "Dimension": { "InstanceType": "c7i.8xlarge", "AvailabilityZoneId": "use1-az1", "Tag": "web-servers" },
            "MetricValues": [
                { "Metric": "inst-az-fulfillment-rate", "Value": 0.62 }
            ]
        },
        {
            "Dimension": { "InstanceType": "m7i.8xlarge", "AvailabilityZoneId": "use1-az1", "Tag": "web-servers" },
            "MetricValues": [
                { "Metric": "inst-az-fulfillment-rate", "Value": 0.97 }
            ]
        }
    ]
}
```