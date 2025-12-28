# Routes Quota and Usage

## Service Quota

Amazon Location Service APIs have default quotas. You can increase quotas using
the [service quota console](https://console.aws.amazon.com/servicequotas/home#!/services/geo/quotas "https://console.aws.amazon.com/servicequotas/home#!/services/geo/quotas"). For limits exceeding 2x the default, request via
the self-service console or contact support.

| Service Quota Limits                                                                | API Name | Default | Max Adjustable Limit                                                                                                                                                                                          | More than Adjustable Max Limit |
| ----------------------------------------------------------------------------------- | -------- | ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------ |
| [Calculate routes](calculate-routes.md "calculate-routes.md")                       | 20       | 40      | Request on [service quota console](https://console.aws.amazon.com/servicequotas/home#!/services/geo/quotas "https://console.aws.amazon.com/servicequotas/home#!/services/geo/quotas") or contact support team |
| [CalculateIsolines](calculate-isolines.md "calculate-isolines.md")                  | 20       | 40      | Request on [service quota console](https://console.aws.amazon.com/servicequotas/home#!/services/geo/quotas "https://console.aws.amazon.com/servicequotas/home#!/services/geo/quotas") or contact support team |
| [Snap to Roads](snap-to-roads.md "snap-to-roads.md")                                | 20       | 40      | Request on [service quota console](https://console.aws.amazon.com/servicequotas/home#!/services/geo/quotas "https://console.aws.amazon.com/servicequotas/home#!/services/geo/quotas") or contact support team |
| [Calculate route matrix](calculate-route-matrix.md "calculate-route-matrix.md")     | 5        | 10      | Request on [service quota console](https://console.aws.amazon.com/servicequotas/home#!/services/geo/quotas "https://console.aws.amazon.com/servicequotas/home#!/services/geo/quotas") or contact support team |
| [Optimize waypoints](actions-optimize-waypoints.md "actions-optimize-waypoints.md") | 5        | 10      | Request on [service quota console](https://console.aws.amazon.com/servicequotas/home#!/services/geo/quotas "https://console.aws.amazon.com/servicequotas/home#!/services/geo/quotas") or contact support team |

## Other Usage Limits

In addition to service quotas, the following API usage limits apply:

| Other Usage Limits                                                                  | API Name                                                                                                                | Limit   | Value |
| ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------- | ------- | ----- |
| [Snap to Roads](snap-to-roads.md "snap-to-roads.md")                                | Sum of Geodesic distance between all<br>TracePoints                                                                     | 500KM   |
| [Optimize waypoints](actions-optimize-waypoints.md "actions-optimize-waypoints.md") | Sum of Geodesic distance between the Origin, Waypoints in<br>the provided ordering, and Destination                     | 100KM   |
| [Optimize waypoints](actions-optimize-waypoints.md "actions-optimize-waypoints.md") | Perimeter of the bounding box surrounding the Origin,<br>Waypoints, and Destination                                     | 500KM   |
| [Calculate route matrix](calculate-route-matrix.md "calculate-route-matrix.md")     | Max Distance between Origins and Destinations for Unbounded<br>routing (If Avoid or TravelModeOptions.Truck is<br>used) | 60KM    |
| [Calculate route matrix](calculate-route-matrix.md "calculate-route-matrix.md")     | Max Distance between Origins and Destinations for Unbounded<br>routing                                                  | 10000KM |
| [Calculate routes](calculate-routes.md "calculate-routes.md")                       | Response payload size after compression                                                                                 | 6MB     |
| [Calculate route matrix](calculate-route-matrix.md "calculate-route-matrix.md")     | Response payload size after compression                                                                                 | 6MB     |
| [Calculate isolines](calculate-isolines.md "calculate-isolines.md")                 | Response payload size after compression                                                                                 | 6MB     |
| [Optimize waypoints](actions-optimize-waypoints.md "actions-optimize-waypoints.md") | Response payload size after compression                                                                                 | 6MB     |
| [Snap to Roads](snap-to-roads.md "snap-to-roads.md")                                | Response payload size after compression                                                                                 | 6MB     |

## Next Steps

Please check the following for further details:

- [Attribution](location/latest/developerguide/data-attribution.md "location/latest/developerguide/data-attribution.md"): Information on data attribution requirements for
  Amazon Location Service.
- [SLA](https://aws.amazon.com/location/sla/ "https://aws.amazon.com/location/sla/"): The service
  level agreement for Amazon Location Service, including uptime commitments
  and response times.
- [Service Terms](https://aws.amazon.com/service-terms/ "https://aws.amazon.com/service-terms/"):
  Terms governing the use of Amazon Location Service, including restrictions
  and limitations.
