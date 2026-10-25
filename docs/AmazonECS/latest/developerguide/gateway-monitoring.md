

# Monitor a gateway
<a name="gateway-monitoring"></a>

You can monitor Amazon ECS Gateway to view the status of a gateway, identify the infrastructure that it manages, and inspect the connections between gateways and Amazon ECS services. You can also use Amazon CloudWatch and Elastic Load Balancing to monitor request traffic and the health of the targets receiving that traffic.

Gateway monitoring includes three types of information:
+ **Gateway and association status**: Whether the gateway is available, whether a configuration update succeeded, and which clusters are associated with it.
+ **Gateway route status**: Whether Amazon ECS provisioned or updated the ingress infrastructure for a particular service connection.
+ **Traffic and target health**: Whether the load balancer receives requests and whether the targets serving a service are healthy.

These statuses are independent. A gateway can be `ACTIVE` even if an individual gateway route failed to provision. A gateway route can be `ACTIVE` even if its application targets are unhealthy.

## View gateway status
<a name="gateway-view-status"></a>

Use `describe-gateway` to view the configuration and current status of a gateway.

```
aws ecs describe-gateway \
    --gateway my-gateway
```

The response includes the gateway's status, infrastructure IAM role, and configuration. Use it to confirm whether a change to the gateway's managed infrastructure has completed. Once an update begins, `statusReason` reports how many load balancers were updated out of the total. For example, 12/12 load balancers updated when every load balancer succeeded, or 10/12 load balancers updated, 2 load balancers failed update when some did not. A gateway that has never been updated has no `statusReason`. `failures` appears only when the gateway is in a failure state, so inspect it to identify the affected resources. A failure entry identifies the resource ARN and the failed operation, along with an error code and message. To resolve an update failure, see [Gateway update failures](gateway-troubleshooting.md#gateway-ts-update-failed). A gateway's cluster associations and routes are not part of this response.

To list the gateways in your account and Region, use `list-gateways`:

```
aws ecs list-gateways
```

To view the Amazon ECS clusters associated with a gateway, use `list-gateway-cluster-associations`:

```
aws ecs list-gateway-cluster-associations \
    --gateway my-gateway
```

An `ACTIVE` association makes a gateway available to compatible services in the cluster. An association in `DISASSOCIATING` remains until the gateway routes for that cluster are removed.

### Gateway, association, and route status
<a name="gateway-status-values"></a>

The following table shows which Amazon ECS operation to use for each resource and the status values it reports.


| Resource | API operations | Status values | What the status indicates | 
| --- | --- | --- | --- | 
| Gateway | DescribeGateway<br />ListGateways | ACTIVE<br />UPDATE\_IN\_PROGRESS<br />UPDATE\_COMPLETE<br />UPDATE\_FAILED<br />DELETED | The gateway's configuration state and the outcome of updates to its managed infrastructure. | 
| Gateway cluster association | ListGatewayClusterAssociations | ACTIVE<br />DISASSOCIATING | Whether the association can be used for new service connections or is waiting for existing routes to be removed. | 
| Gateway route | DescribeGatewayRoute<br />ListGatewayRoutes | ACTIVE<br />CREATE\_IN\_PROGRESS<br />CREATE\_FAILED<br />UPDATE\_IN\_PROGRESS<br />UPDATE\_FAILED<br />DELETE\_IN\_PROGRESS<br />DELETE\_FAILED | The provisioning or removal state of a service-to-gateway connection and its ingress resources. | 

A **gateway** is `ACTIVE` from creation until its first update. An update moves it to `UPDATE_IN_PROGRESS` and then to `UPDATE_COMPLETE` or `UPDATE_FAILED`. Of these, `UPDATE_FAILED` is the only state that needs you to act: read `statusReason` and the `failures` list to see which load balancers were not updated and why. `DELETED` is terminal, and a later request for the gateway returns `GatewayNotFoundException`.

A **gateway cluster association** is `ACTIVE` once you create it and `DISASSOCIATING` after you remove it. It stays `DISASSOCIATING` until every gateway route for that cluster is gone, so a long-lived `DISASSOCIATING` is a sign that services are still connected, not that anything failed.

A **gateway route** moves through its own create, update, and delete lifecycle and is `ACTIVE` while it carries traffic. The three `*_FAILED` states are where a per-service provisioning problem surfaces. `list-gateway-routes --status CREATE_FAILED UPDATE_FAILED` is how you find them. A connection in the application view does not have a separate status: its `status` is the status of its gateway route, so it uses these same values.

**Note**  
A gateway reporting `ACTIVE` does not mean every service behind it is healthy. Gateway status describes the gateway's own configuration. A service deployment that fails to provision ingress shows up on the gateway route, and an unhealthy application shows up in target group health, neither of which changes gateway status.

## Inspect managed infrastructure (platform view)
<a name="gateway-inspect-infrastructure"></a>

Use `describe-gateway-resources` to identify the ingress resources that a gateway manages for you.

```
aws ecs describe-gateway-resources \
    --gateway my-gateway
```

For a `hostSharedAlb` gateway, the response groups resources by Application Load Balancer. Each group identifies the load balancer, its listener, its security group, and the associated gateway routes. Use this view to find which load balancers belong to a gateway and which service connections share each load balancer.

The response returns ARNs of resources that Amazon ECS manages, not live status of the resources. If the response returned state, that state could be stale or contradict what the owning service reports. For the real state of a resource, use the ARN with the owning AWS service to inspect current resource state. For example, to describe a managed Application Load Balancer, run:

```
aws elbv2 describe-load-balancers \
    --load-balancer-arns arn:aws:elasticloadbalancing:us-west-2:123456789012:loadbalancer/app/example/0123456789abcdef
```

You can inspect listeners, listener rules, and target groups the same way with the relevant Elastic Load Balancing operations, and security groups with Amazon EC2. Because a gateway reports only its own record and not a live reading, it does not detect when something it manages is changed outside Amazon ECS. For more information, see [Changes made outside Amazon ECS](gateway-troubleshooting.md#gateway-changes-outside-ecs).

## Monitor gateway routes
<a name="gateway-inspect-routes"></a>

Use gateway routes to monitor individual service connections. Each route has its own provisioning status and generated service URL, even when several routes share an Application Load Balancer.

### List gateway routes
<a name="gateway-list-routes"></a>

To see all service connections through a gateway, run:

```
aws ecs list-gateway-routes \
    --gateway my-gateway
```

To find the routes for a particular service, specify the cluster and service:

```
aws ecs list-gateway-routes \
    --cluster my-cluster \
    --service my-service
```

The response identifies the route ARN, the associated service and gateway, and the route status. You can filter routes by gateway, cluster, service, container port name, or status. To filter by service, pass either a full service ARN or a service name together with its cluster. A service name on its own is ambiguous, because service names are unique only within a cluster, so Amazon ECS returns an error. Use the status filter to find routes whose provisioning or update failed:

```
aws ecs list-gateway-routes \
    --gateway my-gateway \
    --status CREATE_FAILED UPDATE_FAILED
```

A route in `CREATE_IN_PROGRESS` is still provisioning ingress resources, and a route in `ACTIVE` has finished. If a route is in a failed state, inspect it with `describe-gateway-route`, and see [Troubleshoot a gateway](gateway-troubleshooting.md) for recovery guidance.

### Inspect a gateway route
<a name="gateway-inspect-a-route"></a>

To inspect a particular connection, run `describe-gateway-route` with the route ARN:

```
aws ecs describe-gateway-route \
    --gateway-route-arn arn:aws:ecs:us-west-2:123456789012:gateway-route/my-gateway/a1b2c3d4/9f8e7d6c
```

The response includes the route's status and service URL, along with the identifiers of the ingress resources for that connection: the certificate, the load balancer and its listener, the listener rule for production traffic, the listener rule for test traffic, the load balancer's security groups, and the service security group where the gateway manages the ingress rule. Use these identifiers to follow a request from the shared load balancer to the service. A route normally lists one test listener rule, and lists more only while it is moving from one test header configuration to another. To find the target group that receives production traffic, or the alternate target group that a progressive deployment uses, inspect the service revision instead.

### View gateway connections for a service revision (application view)
<a name="gateway-service-resources-view"></a>

Application teams can inspect the gateway connections recorded for a deployed Amazon ECS service revision. Use `describe-service-revisions`:

```
aws ecs describe-service-revisions \
    --service-revision-arns arn:aws:ecs:us-west-2:123456789012:service-revision/my-cluster/my-service/1234567890123456789 \
    --query 'serviceRevisions[0].ecsManagedResources.gatewayConnections'
```

Each connection identifies the gateway and route, the container port name, the access type, the connection status, and the generated HTTPS service URL. A connection's `status` is the status of its gateway route, so it reports the gateway route status values. A connection also names the ingress resources for that service: the certificate, the load balancer and its listener, the listener rules for production and test traffic, the load balancer's security groups, and the production and alternate target groups. A progressive deployment registers the new revision in the alternate target group while the current revision keeps serving from the production one. Inspect a service revision when you want to verify which connections a particular deployment was configured with. Comparing two revisions shows what changed about a service's ingress between deployments. For instructions to create, change, or remove service connections, see [Connect Amazon ECS services to a gateway](gateway-connect-service.md).

## Monitor traffic and target health
<a name="gateway-monitor-traffic"></a>

After you connect a service, you watch two things: the traffic reaching it and the health of the targets serving it. Amazon ECS Gateway does not publish metrics of its own for this. Instead, you use the Application Load Balancer metrics that Elastic Load Balancing publishes to Amazon CloudWatch, and you read target health directly from Elastic Load Balancing.

### Choose the right metric dimensions
<a name="gateway-metric-dimensions"></a>

A gateway can place up to 25 services on one Application Load Balancer, so a metric reported for the whole load balancer combines every service on it. To see one service on its own, query the metric with the target group dimension instead of the load balancer dimension. Choose the dimensions that match what you want to see.


| Monitoring scope | Recommended dimensions | Useful metrics | 
| --- | --- | --- | 
| Individual service connection | TargetGroup with LoadBalancer | RequestCount, TargetResponseTime, HTTPCode\_Target\_5XX\_Count, HealthyHostCount, UnHealthyHostCount | 
| Shared load balancer | LoadBalancer | HTTPCode\_ELB\_5XX\_Count, ActiveConnectionCount, RejectedConnectionCount, ConsumedLCUs | 
| Availability Zone | AvailabilityZone with the applicable load balancer or target group dimensions | Target health and request metrics, to tell whether an issue is limited to one Availability Zone | 

Application teams should use the target group dimension. A request spike or a rise in 5XX responses on the load balancer dimension might come from another service that shares the load balancer, and you cannot attribute it to yours. Find your service's target group in its gateway connection, which `describe-service-revisions` returns. For the full list of metrics and the statistics each supports, see [CloudWatch metrics for your Application Load Balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/load-balancer-cloudwatch-metrics.html) in the *Application Load Balancers User Guide*.

**Note**  
Elastic Load Balancing publishes a metric only while traffic is flowing, and it does not count health check requests. A newly connected service that has not received traffic yet shows no request metrics. This is expected and does not indicate a problem.

### Check target health
<a name="gateway-check-target-health"></a>

Metrics show trends over time. To see the health of your targets right now, read the target group directly:

```
aws elbv2 describe-target-health \
    --target-group-arn arn:aws:elasticloadbalancing:us-west-2:123456789012:targetgroup/example/0123456789abcdef
```

The response gives the current state of each registered target, and a reason when a target is unhealthy, such as a failed health check and the response code it received. A gateway route in `ACTIVE` status means Amazon ECS finished provisioning the ingress. It does not mean the targets behind it are healthy, so check target health separately. If targets stay unhealthy, see [Service connectivity and target health](gateway-troubleshooting.md#gateway-connectivity-issues).

### Configure CloudWatch alarms
<a name="gateway-cloudwatch-alarms"></a>

Create alarms on the metrics that matter to your application, such as unhealthy targets, rising target response time, and target 5XX errors. Platform teams can also alarm on load balancer 5XX errors and rejected connections for the shared infrastructure.

A gateway adds load balancers as services connect and removes them as services disconnect, so an alarm tied to a single load balancer or target group ARN can quietly stop measuring anything when that resource goes away. Amazon ECS tags every load balancer it creates with the gateway's ARN. Select resources by that tag so your alarms and dashboards keep following the gateway as its infrastructure changes. For more information, see [Using resource tags for telemetry](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/UsingResourceTagsForTelemetry.html) in the *Amazon CloudWatch User Guide*. Account for metrics that are not emitted in every period by choosing how an alarm treats missing data.

## View traffic and operation logs
<a name="gateway-view-logs"></a>

### Application Load Balancer access logs
<a name="gateway-alb-access-logs"></a>

When access logging is enabled for a gateway's managed load balancers, Elastic Load Balancing delivers request records to the configured Amazon S3 bucket. Access logs capture request and response information that helps you examine traffic patterns and investigate individual requests.

Because the load balancers are shared, one load balancer's access logs can include requests for several services. Use the hostname in each log record to tell one service's requests from another's. Access logs are disabled by default. For how to turn them on, see [Enable access logs](gateway-managing.md#gateway-access-logs). For the log format and delivery behavior, see [Access logs for your Application Load Balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/load-balancer-access-logs.html) in the *Application Load Balancers User Guide*.

### Locate failure details
<a name="gateway-where-failures-recorded"></a>

When a monitoring operation reports a failure, use the following table to find where the failure is recorded.


| Failure observed | Where to look | Information available | 
| --- | --- | --- | 
| A gateway configuration update reports UPDATE\_FAILED | describe-gateway | statusReason and failures identify the affected managed resources and the operations that did not succeed. | 
| A service connection reports CREATE\_FAILED or UPDATE\_FAILED | describe-gateway-route | The route's status and the ingress resources for that connection. | 
| A service deployment does not reach the expected state | describe-service-revisions | The service revision's gateway connections and context about the deployment operations. | 
| Requests fail or application targets are unhealthy | Elastic Load Balancing target health, CloudWatch metrics, and access logs (if enabled) | Target health states, request metrics, and information about individual requests. | 

Use these sources to determine which resource or connection is affected. For symptoms, likely causes, and recovery procedures, see [Troubleshoot a gateway](gateway-troubleshooting.md).