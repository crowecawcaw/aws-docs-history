# Health checks for Network Load Balancer target groups

You register your targets with one or more target groups. The load balancer starts routing
requests to a newly registered target as soon as the registration process completes and the
targets pass the initial health checks. It can take a few minutes for the registration process
to complete and health checks to start.

Network Load Balancers use active and passive health checks to determine whether a target is available to
handle requests. By default, each load balancer node routes requests only to the healthy
targets in its Availability Zone. If you enable cross-zone load balancing, each load
balancer node routes requests to the healthy targets in all enabled Availability Zones. For
more information, see [Cross-zone load balancing](network-load-balancers.md#cross-zone-load-balancing "network-load-balancers.md#cross-zone-load-balancing").

With passive health checks, the load balancer observes how targets respond to connections.
Passive health checks enable the load balancer to detect an unhealthy target before it is
reported as unhealthy by the active health checks. You cannot disable, configure, or monitor
passive health checks. Passive health checks are not supported for UDP traffic, and target
groups with stickiness turned on. For more information, see [Sticky sessions](edit-target-group-attributes.md#sticky-sessions "edit-target-group-attributes.md#sticky-sessions").

If a target becomes unhealthy, the load balancer sends a TCP RST for packets received on
the client connections associated with the target, unless the unhealthy target triggers the
load balancer to fail open.

If target groups don't have a healthy target in an enabled Availability Zone, we remove
the IP address for the corresponding subnet from DNS so that requests cannot be routed to
targets in that Availability Zone. If all targets fail health checks at the same time in all
enabled Availability Zones, the load balancer fails open. Network Load Balancers will also fail open when you
have an empty target group. The effect of the fail open is to allow traffic to all targets in
all enabled Availability Zones, regardless of their health status.

If a target group is configured with HTTPS health checks, its registered targets fail
health checks if they support only TLS 1.3. These targets must support an earlier version
of TLS, such as TLS 1.2.

For HTTP or HTTPS health check requests, the host header contains the IP address of the
load balancer node and the listener port, not the IP address of the target and the health
check port.

If you add a TLS listener to your Network Load Balancer, we perform a listener connectivity test. As TLS
termination also terminates a TCP connection, a new TCP connection is established between
your load balancer and your targets. Therefore, you might see the TCP connections for this test
sent from your load balancer to the targets that are registered with your TLS listener. You
can identify these TCP connections because they have the source IP address of your Network Load Balancer and the
connections do not contain data packets.

For a UDP service, target availability can be tested using non-UDP health checks on your
target group. You can use any available health check (TCP, HTTP, or HTTPS), and any port on
your target to verify the availability of a UDP service. If the service receiving the health
check fails, your target is considered unavailable. To improve the accuracy of health checks
for a UDP service, configure the service listening to the health check port to track the
status of your UDP service and fail the health check if the service is unavailable.

For more information, see [Target group health](load-balancer-target-groups.md#target-group-health "load-balancer-target-groups.md#target-group-health").

###### Contents

- [Health check settings](#health-check-settings "#health-check-settings")
- [Target health status](#target-health-states "#target-health-states")
- [Health check reason codes](#target-health-reason-codes "#target-health-reason-codes")
- [Check target health](check-target-health.md "check-target-health.md")
- [Update health check settings](modify-health-check-settings.md "modify-health-check-settings.md")

## Health check settings

You configure active health checks for the targets in a target group using the
following settings. If the health checks exceed
**UnhealthyThresholdCount** consecutive failures, the load balancer
takes the target out of service. When the health checks exceed
**HealthyThresholdCount** consecutive successes, the load balancer
puts the target back in service.

| Setting                        | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | Default                                                                             |
| ------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| **HealthCheckProtocol**        | The protocol the load balancer uses when performing health checks<br>on targets. The possible protocols are HTTP, HTTPS, and TCP. The<br>default is the TCP protocol. If the target type is `alb`,<br>the supported health check protocols are HTTP and HTTPS.                                                                                                                                                                                                                                                                                             | TCP                                                                                 |
| **HealthCheckPort**            | The port the load balancer uses when performing health checks on<br>targets. The default is to use the port on which each target<br>receives traffic from the load balancer.                                                                                                                                                                                                                                                                                                                                                                               | Port on which each target receives traffic from the load<br>balancer.               |
| **HealthCheckPath**            | [HTTP/HTTPS health checks] The health check path that is the destination<br>on the targets for health checks. The default is /.                                                                                                                                                                                                                                                                                                                                                                                                                            | /                                                                                   |
| **HealthCheckTimeoutSeconds**  | The amount of time, in seconds, during which no response from a target<br>means a failed health check. The range is 2–120 seconds. The default<br>values are 6 seconds for HTTP and 10 seconds for TCP and HTTPS health<br>checks.                                                                                                                                                                                                                                                                                                                         | 6 seconds for HTTP health checks and 10 seconds for TCP and HTTPS<br>health checks. |
| **HealthCheckIntervalSeconds** | The approximate amount of time, in seconds, between health checks<br>of an individual target. The range is 5–300 seconds. The default<br>is 30 seconds.<br>Health checks for a Network Load Balancer are distributed and use a consensus<br>mechanism to determine target health. Therefore, targets receive<br>more than the configured number of health checks. To reduce the<br>impact to your targets if you are using HTTP health checks, use<br>a simpler destination on the targets, such as a static HTML<br>file, or switch to TCP health checks. | 30 seconds                                                                          |
| **HealthyThresholdCount**      | The number of consecutive successful health checks required before<br>considering an unhealthy target healthy. The range is 2–10. The default<br>is 5.                                                                                                                                                                                                                                                                                                                                                                                                     | 5                                                                                   |
| **UnhealthyThresholdCount**    | The number of consecutive failed health checks required before considering<br>a target unhealthy. The range is 2–10. The default is 2.                                                                                                                                                                                                                                                                                                                                                                                                                     | 2                                                                                   |
| **Matcher**                    | [HTTP/HTTPS health checks] The HTTP codes to use when checking for a<br>successful response from a target. The range is 200 to 599. The default<br>is 200-399.                                                                                                                                                                                                                                                                                                                                                                                             | 200-399                                                                             |

## Target health status

Before the load balancer sends a health check request to a target, you must register
it with a target group, specify its target group in a listener rule, and ensure that the
Availability Zone of the target is enabled for the load balancer.

The following table describes the possible values for the health status of a
registered target.

| Value                | Description                                                                                                                                                                                                                                                                   |
| -------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------- | ------------------------- | ------------------- |
| `initial`            | The load balancer is in the process of registering the target or<br>performing the initial health checks on the target.<br>Related reason codes: `Elb.RegistrationInProgress`                                                                                                 | <br>`Elb.InitialHealthChecking` |
| `healthy`            | The target is healthy.<br>Related reason codes: None                                                                                                                                                                                                                          |
| `unhealthy`          | The target did not respond to a health check, failed the health check,<br>or the target is in stopped state.<br>Related reason code: `Target.FailedHealthChecks`                                                                                                              |
| `draining`           | The target is deregistering and connection draining is in<br>process.<br>Related reason code:<br>`Target.DeregistrationInProgress`                                                                                                                                            |
| `unhealthy.draining` | The target did not respond to health checks or failed<br>the health checks and enters a grace period. The target<br>supports existing connections and will not accept any<br>new connections during this grace period.<br>Related reason code:<br>`Target.FailedHealthChecks` |
| `unavailable`        | Target health is unavailable.<br>Related reason code: `Elb.InternalError`                                                                                                                                                                                                     |
| `unused`             | The target is not registered with a target group, the<br>target group is not used in a listener rule, or the target<br>is in an Availability Zone that is not enabled.<br>Related reason codes: `Target.NotRegistered`                                                        | <br>`Target.NotInUse`           | `Target.InvalidState`<br> | `Target.IpUnusable` |

## Health check reason codes

If the status of a target is any value other than `Healthy`, the API
returns a reason code and a description of the issue, and the console displays the same
description in a tooltip. Note that reason codes that begin with `Elb`
originate on the load balancer side and reason codes that begin with `Target`
originate on the target side.

| Reason code                       | Description                                                                                                                                                   |
| --------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `Elb.InitialHealthChecking`       | Initial health checks in progress                                                                                                                             |
| `Elb.InternalError`               | Health checks failed due to an internal error                                                                                                                 |
| `Elb.RegistrationInProgress`      | Target registration is in progress                                                                                                                            |
| `Target.DeregistrationInProgress` | Target deregistration is in progress                                                                                                                          |
| `Target.FailedHealthChecks`       | Health checks failed                                                                                                                                          |
| `Target.InvalidState`             | Target is in the stopped state<br>Target is in the terminated state<br>Target is in the terminated or stopped state<br>Target is in an invalid state          |
| `Target.IpUnusable`               | The IP address cannot be used as a target, as it is in use by a<br>load balancer                                                                              |
| `Target.NotInUse`                 | Target group is not configured to receive traffic from the load<br>balancer<br>Target is in an Availability Zone that is not enabled for the load<br>balancer |
| `Target.NotRegistered`            | Target is not registered to the target group                                                                                                                  |
