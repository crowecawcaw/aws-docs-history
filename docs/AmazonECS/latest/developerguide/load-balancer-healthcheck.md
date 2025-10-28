# Optimize load balancer health

check parameters for Amazon ECS

Load balancers route requests only to the healthy targets in the Availability Zones
for the load balancer. Each target is registered to a target group. The load balancer
checks the health of each target, using the target group health check settings. After
you register the target, it must pass one health check to be considered healthy. Amazon ECS
monitors the load balancer. The load balancer periodically sends health checks to the
Amazon ECS container. The Amazon ECS agent monitors, and waits for the load balancer to report on
the container health. It does this before it considers the container to be in a healthy
status.

Two Elastic Load Balancing health check parameters affect deployment speed:

- Health check interval: Determines the approximate amount of
  time, in seconds, between health checks of an individual container. By default,
  the load balancer checks every 30 seconds.

This parameter is named:

    + `HealthCheckIntervalSeconds` in the Elastic Load Balancing API
    + **Interval** on the Amazon EC2 console

- Healthy threshold count: Determines the number of consecutive
  health check successes required before considering an unhealthy container
  healthy. By default, the load balancer requires five passing health checks
  before it reports that the target container is healthy.

This parameter is named:

    + `HealthyThresholdCount` in the Elastic Load Balancing API
    + **Healthy threshold** on the Amazon EC2 console

**Important:** For newly registered targets, only a single successful health check is required to consider the target healthy, regardless of the healthy threshold count setting. The healthy threshold count only applies when a target is transitioning from an unhealthy state back to a healthy state.

With the default settings, if a target becomes unhealthy and then recovers, the total time to determine the health of a container is two minutes and 30 seconds (`30 seconds * 5 = 150 seconds`).

You can speed up the health-check process if your service starts up and stabilizes in under 10 seconds. To speed up the process, reduce the health check interval and the healthy threshold count.

- `HealthCheckIntervalSeconds` (Elastic Load Balancing API name) or **Interval** (Amazon EC2 console name): 5
- `HealthyThresholdCount` (Elastic Load Balancing API name) or **Healthy threshold** (Amazon EC2 console name): 2
  With this setting, the health-check process takes 10 seconds compared to the default
  of two minutes and 30 seconds.

For more information about the Elastic Load Balancing health check parameters, see [Health checks for your target groups](../../../elasticloadbalancing/latest/application/target-group-health-checks.md "../../../elasticloadbalancing/latest/application/target-group-health-checks.md") in the _Elastic Load Balancing User Guide_.
