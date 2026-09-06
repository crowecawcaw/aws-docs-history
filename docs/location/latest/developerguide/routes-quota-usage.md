

# Routes Quota and Usage
<a name="routes-quota-usage"></a>

## Service Quota
<a name="service-quota"></a>

Amazon Location Service APIs have default quotas. You can increase quotas using the [service quota console](https://console.aws.amazon.com/servicequotas/home#!/services/geo/quotas). For limits exceeding 2x the default, request via the self-service console or contact support.


**Service Quota Limits**  

| API Name | Default | Max Adjustable Limit | More than Adjustable Max Limit | 
| --- | --- | --- | --- | 
| [Calculate routes](calculate-routes.md) | 20 | 40 | Request on [service quota console](https://console.aws.amazon.com/servicequotas/home#!/services/geo/quotas) or contact support team | 
| [Calculate isolines](calculate-isolines.md) | 20 | 40 | Request on [service quota console](https://console.aws.amazon.com/servicequotas/home#!/services/geo/quotas) or contact support team | 
| [Snap to Roads](snap-to-roads.md) | 20 | 40 | Request on [service quota console](https://console.aws.amazon.com/servicequotas/home#!/services/geo/quotas) or contact support team | 
| [Calculate route matrix](calculate-route-matrix.md) | 5 | 10 | Request on [service quota console](https://console.aws.amazon.com/servicequotas/home#!/services/geo/quotas) or contact support team | 
| [Optimize waypoints](actions-optimize-waypoints.md) | 5 | 10 | Request on [service quota console](https://console.aws.amazon.com/servicequotas/home#!/services/geo/quotas) or contact support team | 

## Other Usage Limits
<a name="other-usage-limits"></a>

In addition to service quotas, the following API usage limits apply:


**Other Usage Limits**  

| API Name | Limit | Value | 
| --- | --- | --- | 
| [Snap to Roads](snap-to-roads.md) | Sum of Geodesic distance between all TracePoints | 500KM | 
| [Snap to Roads](snap-to-roads.md) | Max `TracePoints` per request | 5,000 | 
| [Optimize waypoints](actions-optimize-waypoints.md) | Max `Waypoints` per request | 50 | 
| [Optimize waypoints](actions-optimize-waypoints.md) | Max `Waypoints` when using constraints (`AccessHours`, `AppointmentTime`, `ServiceDuration`, `Heading`, `SideOfStreet`, `Before`) | 20 | 
| [Optimize waypoints](actions-optimize-waypoints.md) | Sum of Geodesic distance between the Origin, Waypoints in the provided ordering, and Destination | 100KM | 
| [Optimize waypoints](actions-optimize-waypoints.md) | Perimeter of the bounding box surrounding the Origin, Waypoints, and Destination | 500KM | 
| [Calculate route matrix](calculate-route-matrix.md) | Max Distance between Origins and Destinations for Unbounded routing (If `Avoid` or `TravelModeOptions.Truck` is used) | 60KM | 
| [Calculate route matrix](calculate-route-matrix.md) | Max Distance between Origins and Destinations for Unbounded routing | 10000KM | 
| [Calculate route matrix](calculate-route-matrix.md) | Max Origins with `RoutingBoundary.Geometry` | 500 | 
| [Calculate route matrix](calculate-route-matrix.md) | Max Origins with `RoutingBoundary.Unbounded` | 15 | 
| [Calculate route matrix](calculate-route-matrix.md) | Max Origins for GrabMaps customers in `ap-southeast-1` and `ap-southeast-5` | 350 | 
| [Calculate route matrix](calculate-route-matrix.md) | Max Destinations with `RoutingBoundary.Geometry` | 500 | 
| [Calculate route matrix](calculate-route-matrix.md) | Max Destinations with `RoutingBoundary.Unbounded` | 100 | 
| [Calculate route matrix](calculate-route-matrix.md) | Max Destinations for GrabMaps customers in `ap-southeast-1` and `ap-southeast-5` | 350 | 
| [Calculate route matrix](calculate-route-matrix.md) | Max matrix size (Origins × Destinations) with `RoutingBoundary.Geometry` | 160,000 | 
| [Calculate route matrix](calculate-route-matrix.md) | Max matrix size (Origins × Destinations) with `RoutingBoundary.Unbounded` | 100 | 
| [Calculate route matrix](calculate-route-matrix.md) | Max matrix size (Origins × Destinations) for GrabMaps customers in `ap-southeast-1` and `ap-southeast-5` | 122,500 | 
| [Calculate routes](calculate-routes.md) | Response payload size after compression | 6MB | 
| [Calculate route matrix](calculate-route-matrix.md) | Response payload size after compression | 6MB | 
| [Calculate isolines](calculate-isolines.md) | Response payload size after compression | 6MB | 
| [Optimize waypoints](actions-optimize-waypoints.md) | Response payload size after compression | 6MB | 
| [Snap to Roads](snap-to-roads.md) | Response payload size after compression | 6MB | 

## Next Steps
<a name="next-steps"></a>

Please check the following for further details:
+ [Attribution](https://docs.aws.amazon.com/location/latest/developerguide/data-attribution.html): Information on data attribution requirements for Amazon Location Service.
+ [SLA](https://aws.amazon.com/location/sla/): The service level agreement for Amazon Location Service, including uptime commitments and response times.
+ [Service Terms](https://aws.amazon.com/service-terms/): Terms governing the use of Amazon Location Service, including restrictions and limitations.