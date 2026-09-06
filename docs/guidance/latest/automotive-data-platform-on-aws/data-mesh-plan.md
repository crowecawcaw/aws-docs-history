

# Plan your deployment
<a name="data-mesh-plan"></a>

## Platform Foundation Cost Breakdown
<a name="platform-foundation-cost-breakdown"></a>

 **Additional monthly costs** for the DataZone V2 domain and governance layer:


| Service | Usage | Monthly Cost | Notes | 
| --- | --- | --- | --- | 
| Amazon DataZone V2 | 1 domain, 10 projects | $50–100 | Data catalog, governance, and subscription workflows | 
| AWS Lake Formation | Tag-based access control | $0 | No additional charge | 
| Amazon Macie | S3 classification (bootstrap) | $5–20 | Scales with data volume | 
| Additional S3 | Metadata storage | $5 | DataZone metadata | 
|  **Total**  |  |  **\~$60–125**  | Add to solution data-storage costs | 

## Cost Scaling Factors
<a name="cost-scaling-factors"></a>

 **Vehicle telemetry and EV operations** (`vehicle_telemetry_aggregated`, `charging_sessions`, `energy_usage`, `ota_campaigns`):
+ Data volume: Costs scale with connected-vehicle fleet size
+ Query frequency: More Athena queries = higher costs

 **Customer data** (`customer_360`, `customer_interactions`):
+ Data volume: Costs scale linearly with customer count
+ Query frequency: More Athena queries = higher costs
+ Downstream consumers can subscribe via DataZone V2 for BI or analytics workloads

 **Predictive Maintenance**:
+ Fleet size: Larger fleets require more Glue and SageMaker Studio notebook capacity