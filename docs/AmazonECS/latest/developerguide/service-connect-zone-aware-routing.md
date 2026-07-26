# Amazon ECS Service Connect zone-aware routing

With Amazon ECS Service Connect zone-aware routing, traffic stays within the same
Availability Zone (AZ) as the client. This reduces cross-AZ data transfer costs and
latency without requiring additional infrastructure or application code changes. When
endpoints are balanced across AZs, more than 80% of traffic stays local while traffic
weights dynamically adjust as endpoints scale to maintain balanced load across target
services. Zone-aware routing is on by default for all new and existing services that
use Service Connect.

## How zone-aware routing works

The algorithm uses the Envoy zone-aware routing feature in the Service Connect proxy
to route traffic based on endpoint locality:

1. **Endpoint discovery** ‐ The proxy
   discovers all available endpoints for the destination service and their AZ
   placement.
2. **Same-AZ prioritization** ‐ The proxy
   calculates what percentage of traffic stays in the same AZ based on the
   ratio of endpoint distribution between the source (client) and destination
   (server) AZs. When endpoints are evenly spread across zones, same-AZ
   traffic typically exceeds 80%.
3. **Residual capacity routing** ‐ Traffic
   that cannot stay in the same AZ is distributed to other AZs based on their
   residual capacity. The proxy calculates the residual capacity of each zone
   and splits cross-AZ traffic proportionally among zones with positive
   residual capacity. As endpoints scale up or down, the proxy recalculates
   routing weights in real time.
4. **Overload protection and fallback** ‐
   To prevent overloading a single AZ, the proxy requires at least
   2 × the number of AZs as available endpoints in the destination
   service. For a 3-AZ Region, this means at least 6 endpoints. Below this
   threshold, zone-aware routing deactivates and traffic is distributed evenly
   using round-robin load balancing. Routing reactivates automatically
   when the endpoint count exceeds the threshold. If endpoints in the same AZ
   become unavailable, traffic redistributes across other AZs to
   maintain availability.

## Verify zone-aware routing on Amazon EC2

On Amazon EC2 container instances that use the Docker runtime, you can inspect Envoy
proxy statistics inside the Service Connect agent container to confirm that
zone-aware routing is active. This procedure requires AWS Systems Manager Session Manager
host access and `docker exec`. For AWS Fargate or container instances
that use `containerd`, use Amazon Virtual Private Cloud Flow Logs to verify routing
behavior as described in [Monitoring zone-aware routing](#service-connect-zone-aware-routing-monitoring "#service-connect-zone-aware-routing-monitoring").

###### To verify zone-aware routing on Amazon EC2 with Docker

1. Connect to the container instance with AWS Systems Manager Session Manager.
   Replace `instance-id` with your container
   instance ID.

```
aws ssm start-session --target `instance-id`
```

2. Open a shell in the Service Connect agent container.

```
sudo docker exec -it $(sudo docker ps --filter "name=ecs-service-connect" -q | head -1) /bin/sh
```

3. Query zone routing statistics from the Envoy admin interface.

```
curl --unix-socket /tmp/envoy_admin.sock http://unix/stats | grep "lb_zone"
```

4. Verify the output. A healthy deployment with zone-aware routing active
   shows zero cross-zone requests:

```
cluster.`my-service`.lb_zone_routing_cross_zone: 0
cluster.`my-service`.lb_zone_cluster_too_small: 0
```

The following table describes the key zone routing metrics.

| Metric                       | Description                                                                                                                                                                                                                                       |
| ---------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `lb_zone_routing_cross_zone` | Number of requests routed to an endpoint in a different AZ. A<br>sustained value of 0 confirms all traffic stays within the same<br>AZ.                                                                                                           |
| `lb_zone_cluster_too_small`  | Number of times zone-aware routing was bypassed because the<br>endpoint count was below the minimum threshold. Non-zero values<br>during initial deployment are expected and resolve as endpoints<br>become healthy. A stable deployment shows 0. |

## Monitoring zone-aware routing

Use Amazon Virtual Private Cloud Flow Logs with the `az-id` field to observe traffic
patterns at the network level. This shows which AZ each flow record originates from
and terminates in, letting you measure same-AZ versus cross-AZ traffic ratios. You
can also use AWS Cost Explorer to track cross-AZ data transfer charges before and
after you redeploy your services to enable zone-aware routing.

For more information about configuring flow logs, see [VPC Flow Logs](../../../vpc/latest/userguide/flow-logs.md "../../../vpc/latest/userguide/flow-logs.md") in the
_Amazon Virtual Private Cloud User Guide_.

## Considerations

Keep the following in mind when you use zone-aware routing:

- Zone-aware routing works with all launch types.
- Zone-aware routing is compatible with cross-account Service Connect
  namespaces shared through AWS Resource Access Manager.
- Existing services (both client and server) require a one-time
  redeployment to activate zone-aware routing. After the initial
  redeployment, routing adjusts dynamically as endpoints change without
  further redeployments.
