

# Fulfillment metrics
<a name="capacity-manager-fulfillment-metrics"></a>

Fulfillment metrics answer the first and most important question: when you ask Amazon EC2 for capacity, are you receiving it? These are request-level metrics — a request that is flexible across multiple instance type and Availability Zone combinations is fulfilled if any combination delivers. A high fulfillment rate means your workloads are getting the capacity they need. A lower fulfillment rate means some requests are going unfulfilled, and you can act by reserving capacity or adding flexibility to your configuration.


| Metric | Description | Unit | 
| --- | --- | --- | 
| CapacityTotalRequestedVcpu | vCPUs you asked for. Retries within a five-minute window count once. | vCPUs | 
| SpotCapacityTotalRequestedVcpu | Spot vCPUs you asked for. Retries within a five-minute window count once. | vCPUs | 
| CapacityTotalFulfilledVcpu | vCPUs Amazon EC2 delivered. | vCPUs | 
| SpotCapacityTotalFulfilledVcpu | Spot vCPUs Amazon EC2 delivered. | vCPUs | 
| CapacityRequestFulfillmentRate | Fulfilled divided by requested for each request. Capacity from a fallback counts as fulfilled. This metric is vCPU-weighted. | Percentage | 
| SpotCapacityRequestFulfillmentRate | Fulfilled divided by requested for each Spot request. Capacity from a fallback counts as fulfilled. This metric is vCPU-weighted. | Percentage | 
| AvgInstAzCountPerRequestedVcpu | Average number of instance type and Availability Zone combinations included in each request, whether or not Amazon EC2 needed them, weighted by vCPUs. A higher value means the request gives Amazon EC2 more options. This metric is vCPU-weighted. | Count | 
| SpotAvgInstAzCountPerRequestedVcpu | Average number of instance type and Availability Zone combinations included in each Spot request, whether or not Amazon EC2 needed them, weighted by vCPUs. A higher value means the request gives Amazon EC2 more options. This metric is vCPU-weighted. | Count | 

**Note**  
The average and rate metrics are vCPU-weighted: larger requests carry more weight, so these values reflect the capacity that matters most rather than being diluted by small requests.

Dimensions available: tag, account ID, account name, Region.

**How fulfillment is calculated**

Capacity Manager calculates fulfillment using the following factors.
+ **Requested** — For a request targeting a single instance type, this is the number of instances requested multiplied by the vCPUs for that type. For a request targeting multiple instance types, the target capacity is normalized to vCPUs using your configured weights. Capacity Manager deduplicates retries within a five-minute window for the same configuration so they don't inflate the total. The largest single request in the window is kept.
+ **Fulfilled** — The real instances Amazon EC2 delivered. Capacity Manager doesn't deduplicate this value, because each delivery is a real outcome. Spot Instances that are later interrupted still count as fulfilled at the time of the original launch request.
+ **Fulfillment rate** — Calculated from the aggregated totals (sum of fulfilled divided by sum of requested), so larger requests carry more weight.
+ **Instance type and Availability Zone count** — The vCPU-weighted average number of instance type and Availability Zone combinations across your launches. For a workload that uses a consistent Amazon EC2 Fleet configuration, this equals the number of instance type and Availability Zone combinations in that configuration. If your workload doesn't use Amazon EC2 Fleet, this value is 1.

**To improve your request-level fulfillment rate**

If your request-level fulfillment rate isn't where you want it, some requests are going unfulfilled. Two actions raise your fulfillment rate:
+ **Add flexibility** — Launch across more instance types and Availability Zones so Amazon EC2 has more instance type and Availability Zone combinations that can satisfy a request — the more combinations a flexible request can draw from, the more likely one of them delivers. Check your instance type and Availability Zone count per request to see how broadly you are configured today.
+ **Secure Capacity Reservations** — If a workload requires a specific instance type in a specific Availability Zone, On-Demand Capacity Reservations reserve that capacity for your use.

The following AWS CLI command returns the daily On-Demand fulfillment rate for the workload tagged `ad-serving`:

```
aws ec2 get-capacity-manager-metric-data \
    --metric-names capacity-request-fulfillment-rate \
    --start-time 2026-04-09T00:00:00Z \
    --end-time 2026-04-16T00:00:00Z \
    --period 86400 \
    --filter-by DimensionCondition='{Dimension=tag,Comparison=equals,Values=[ad-serving]}'
```

In the `--filter-by` condition, replace the following values as needed:
+ `Dimension` — The dimension to filter by, such as `tag`.
+ `Comparison` — The comparison operator, such as `equals`.
+ `Values` — The value or values to match, such as `ad-serving`.

The following JSON structure shows the fulfillment rate response.

```
{
    "MetricDataResults": [
        {
            "Dimension": { "Tag": "ad-serving" },
            "Timestamp": "2026-04-09T00:00:00Z",
            "MetricValues": [
                { "Metric": "capacity-request-fulfillment-rate", "Value": 0.974 }
            ]
        }
    ]
}
```