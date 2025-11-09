# Health checks for Gateway Load Balancer target groups

You register your targets with one or more target groups. Your Gateway Load Balancer starts routing
requests to a newly registered target as soon as the registration process completes. It can
take a few minutes for the registration process to complete and for health checks to
start.

The Gateway Load Balancer periodically sends a request to each registered target to check its status.
After each health check is complete, the Gateway Load Balancer closes the connection that was established
for the health check.

## Health check settings

You configure active health checks for the targets in a target group by using the
following settings. If the health checks exceed the specified number of
**UnhealthyThresholdCount** consecutive failures, the Gateway Load Balancer takes
the target out of service. When the health checks exceed the specified number of
**HealthyThresholdCount** consecutive successes, the Gateway Load Balancer puts the
target back in service.

| Setting                        | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| ------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **HealthCheckProtocol**        | The protocol that the load balancer uses when performing health<br>checks on targets. The possible protocols are HTTP, HTTPS, and TCP.<br>The default is TCP.                                                                                                                                                                                                                                                                                                                                 |
| **HealthCheckPort**            | The port that Gateway Load Balancer uses when performing health checks on targets.<br>The range is 1 to 65535. The default is 80.                                                                                                                                                                                                                                                                                                                                                             |
| **HealthCheckPath**            | [HTTP/HTTPS health checks] The health check path that is the destination<br>on the targets for health checks. The default is /.                                                                                                                                                                                                                                                                                                                                                               |
| **HealthCheckTimeoutSeconds**  | The amount of time, in seconds, during which no response from a<br>target means a failed health check. The range is 2 to 120. The<br>default is 5.                                                                                                                                                                                                                                                                                                                                            |
| **HealthCheckIntervalSeconds** | The approximate amount of time, in seconds, between health checks<br>of an individual target. The range is 5 to 300. The default is 10<br>seconds. This value must be greater than or equal to<br>**HealthCheckTimeoutSeconds**.<br>ImportantHealth checks for Gateway Load Balancers are distributed and use a consensus<br>mechanism to determine target health. Therefore, you should<br>expect target appliances to receive several health checks within<br>the configured time interval. |
| **HealthyThresholdCount**      | The number of consecutive successful health checks required before<br>considering an unhealthy target healthy. The range is 2 to 10. The<br>default is 5.                                                                                                                                                                                                                                                                                                                                     |
| **UnhealthyThresholdCount**    | The number of consecutive failed health checks required before<br>considering a target unhealthy. The range is 2 to 10. The default is<br>2.                                                                                                                                                                                                                                                                                                                                                  |
| **Matcher**                    | [HTTP/HTTPS health checks] The HTTP codes to use when checking for<br>a successful response from a target. This value must be<br>200-399.                                                                                                                                                                                                                                                                                                                                                     |

## Target health status

Before the Gateway Load Balancer sends a health check request to a target, you must register it with a
target group, specify its target group in a listener rule, and ensure that the
Availability Zone of the target is enabled for the Gateway Load Balancer.

The following table describes the possible values for the health status of a
registered target.

| Value         | Description                                                                                                                                                                                                                                                                 |
| ------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------- | ------------------------- | ------------------- |
| `initial`     | The Gateway Load Balancer is in the process of registering the target or<br>performing the initial health checks on the target.<br>Related reason codes: `Elb.RegistrationInProgress`                                                                                       | <br>`Elb.InitialHealthChecking` |
| `healthy`     | The target is healthy.<br>Related reason codes: None                                                                                                                                                                                                                        |
| `unhealthy`   | The target did not respond to a health check or failed the health<br>check.<br>Related reason code: `Target.FailedHealthChecks`                                                                                                                                             |
| `unused`      | The target is not registered with a target group, the target group<br>is not used in a listener rule, the target is in an Availability<br>Zone that is not enabled, or the target is in the stopped or<br>terminated state.<br>Related reason codes: `Target.NotRegistered` | <br>`Target.NotInUse`           | `Target.InvalidState`<br> | `Target.IpUnusable` |
| `draining`    | The target is deregistering and connection draining is in<br>process.<br>Related reason code:<br>`Target.DeregistrationInProgress`                                                                                                                                          |
| `unavailable` | Target health is unavailable.<br>Related reason code: `Elb.InternalError`                                                                                                                                                                                                   |

## Health check reason codes

If the status of a target is any value other than `Healthy`, the API
returns a reason code and a description of the issue, and the console displays the same
description. Reason codes that begin with `Elb` originate on the Gateway Load Balancer side
and reason codes that begin with `Target` originate on the target
side.

| Reason code                       | Description                                                                                                                                                                   |
| --------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `Elb.InitialHealthChecking`       | Initial health checks in progress                                                                                                                                             |
| `Elb.InternalError`               | Health checks failed due to an internal error                                                                                                                                 |
| `Elb.RegistrationInProgress`      | Target registration is in progress                                                                                                                                            |
| `Target.DeregistrationInProgress` | Target deregistration is in progress                                                                                                                                          |
| `Target.FailedHealthChecks`       | Health checks failed                                                                                                                                                          |
| `Target.InvalidState`             | Target is in the stopped state<br>Target is in the terminated state<br>Target is in the terminated or stopped state<br>Target is in an invalid state                          |
| `Target.IpUnusable`               | The IP address cannot be used as a target, as it is in use by a<br>load balancer                                                                                              |
| `Target.NotInUse`                 | Target group is not configured to receive traffic from the<br>Gateway Load Balancer<br>Target is in an Availability Zone that is not enabled for the<br>Gateway Load Balancer |
| `Target.NotRegistered`            | Target is not registered to the target group                                                                                                                                  |

## Gateway Load Balancer target failure scenarios

**Existing flows**: By default, existing flows go to the
same target unless the flow times out or is reset, regardless of the health and
registration status of the target. This approach facilitates connection draining,
and accommodates 3rd party firewalls that are sometimes unable to respond to health
checks due to high CPU usage. For more information, see
[Target failover](edit-target-group-attributes.md#target-failover "edit-target-group-attributes.md#target-failover").

**New flows**: New flows are sent to a healthy target.
When a load balancing decision for a flow has been made, the Gateway Load Balancer will send the flow to
the same target even if that target becomes unhealthy, or other targets become
healthy.

When all targets are unhealthy, the Gateway Load Balancer picks a target at random and forwards
traffic to it for the life of the flow, until it is either reset or has timed out.
Because traffic is being forwarded to an unhealthy target, traffic is dropped until that
target becomes healthy again.

**TLS 1.3**: If a target group is configured with HTTPS
health checks, its registered targets fail health checks if they support only TLS 1.3.
These targets must support an earlier version of TLS, such as TLS 1.2.

**Cross-zone load balancing**: By default, load balancing
across Availability Zones is disabled. If load balancing across zones is enabled, each
Gateway Load Balancer is able to see all targets in all Availability Zones, and they are all treated the
same, regardless of their zone.

Load balancing and health check decisions are always independent among zones. Even
when load balancing across zones is enabled, the behavior for existing flows and new
flows is the same as described above. For more information, see [Cross-zone load balancing](../userguide/how-elastic-load-balancing-works.md#cross-zone-load-balancing "../userguide/how-elastic-load-balancing-works.md#cross-zone-load-balancing") in the
_Elastic Load Balancing User Guide_.

## Check the health of your targets

You can check the health status of the targets registered with your target
groups.

###### To check the health of your targets using the console

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation pane, under **Load Balancing**,
   choose **Target Groups**.
3. Choose the name of the target group to open its details
   page.
4. On the **Targets** tab, the
   **Status** column indicates the status of each
   target.
5. If the target status is any value other than `Healthy`,
   the **Status details** column contains more
   information.

###### To check the health of your targets using the AWS CLI

Use the [describe-target-health](../../../cli/latest/reference/elbv2/describe-target-health.md "../../../cli/latest/reference/elbv2/describe-target-health.md") command. The output of this command contains the
target health state. It includes a reason code if the status is any value other than
`Healthy`.

###### To receive email notifications about unhealthy targets

Use CloudWatch alarms to trigger a Lambda function to send details about unhealthy
targets. For step-by-step instructions, see the following blog post: [Identifying unhealthy targets of your load balancer](https://aws.amazon.com/blogs/networking-and-content-delivery/identifying-unhealthy-targets-of-elastic-load-balancer/ "https://aws.amazon.com/blogs/networking-and-content-delivery/identifying-unhealthy-targets-of-elastic-load-balancer/").

## Modify health check settings

You can modify some of the health check settings for your target group.

###### To modify health check settings for a target group using the console

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation pane, under **Load Balancing**,
   choose **Target Groups**.
3. Choose the name of the target group to open its details
   page.
4. On the **Group details** tab, in the
   **Health check settings** section, choose
   **Edit**.
5. On the **Edit health check settings** page,
   modify the settings as needed, and then choose **Save
   changes**.

###### To modify health check settings for a target group using the AWS CLI

Use the [modify-target-group](../../../cli/latest/reference/elbv2/modify-target-group.md "../../../cli/latest/reference/elbv2/modify-target-group.md") command.
