# Health checks for your VPC Lattice target groups

Your service periodically sends requests to its registered targets to test their
status. These tests are called _health checks_.

Each VPC Lattice service routes requests only to the healthy targets. Each service
checks the health of each target, using the health check settings for the target groups
with which the target is registered. After your target is registered, it must pass one
health check to be considered healthy. After each health check is completed, the service
closes the connection that was established for the health check.

**Limitations and considerations**

- When the target group protocol version is HTTP1, health checks are enabled by
  default.
- When the target group protocol version is HTTP2, health checks are not enabled
  by default. However, you can enable health checks, and manually set the protocol
  version to HTTP1 or HTTP2.
- Health checks do not support gRPC target group protocol versions. However, if
  you enable health checks, you must specify the health check protocol version as
  HTTP1 or HTTP2.
- Health checks do not support Lambda target groups.
- Health checks do not support Application Load Balancer target groups. However, you can enable
  health checks for the targets of your Application Load Balancer using ELB. For more information, see
  [Target group health checks](../../../elasticloadbalancing/latest/application/target-group-health-checks.md "../../../elasticloadbalancing/latest/application/target-group-health-checks.md") in the _User Guide for Application Load Balancers_.

## Health check settings

You configure health checks for the targets in a target group as described in the
following table. The setting names used in the table are the names used in the API.
The service sends a health check request to each registered target every
**HealthCheckIntervalSeconds** seconds, using the specified
port, protocol, and ping path. Each health check request is independent and the
result lasts for the entire interval. The time that it takes for the target to
respond does not affect the interval for the next health check request. If the
health checks exceed **UnhealthyThresholdCount** consecutive
failures, the service takes the target out of service. When the health checks exceed
**HealthyThresholdCount** consecutive successes, the service
puts the target back in service.

| Setting                        | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| ------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **HealthCheckProtocol**        | The protocol the service uses when performing health checks on<br>targets. The possible protocols are HTTP and HTTPS. The default<br>is the HTTP protocol.                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| **HealthCheckPort**            | The port the service uses when performing health checks on<br>targets. The default is to use the port on which each target<br>receives traffic from the service.                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| **HealthCheckPath**            | The destination for health checks on the targets.<br>If the protocol version is HTTP1 or HTTP2, specify a valid URI<br>(/_path_?_query_). The<br>default is /.                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| **HealthCheckTimeoutSeconds**  | The amount of time, in seconds, during which no response from<br>a target means a failed health check. The range is 1–120<br>seconds. The default is 5 seconds if the target type is<br>`INSTANCE` or `IP`. Specify 0 to reset<br>this setting to its default value.                                                                                                                                                                                                                                                                                                                                |
| **HealthCheckIntervalSeconds** | The approximate amount of time, in seconds, between health<br>checks of an individual target. The range is 5–300<br>seconds. The default is 30 seconds if the target type is<br>`INSTANCE` or `IP`. Specify 0 to reset<br>this setting to its default value.                                                                                                                                                                                                                                                                                                                                        |
| **HealthyThresholdCount**      | The number of consecutive successful health checks required<br>before an unhealthy target is considered healthy. The range is<br>2–10. The default is 5. Specify 0 to reset this setting<br>to its default value.                                                                                                                                                                                                                                                                                                                                                                                   |
| **UnhealthyThresholdCount**    | The number of consecutive health check failures required<br>before considering a target unhealthy. The range is 2–10.<br>The default is 2. Specify 0 to reset this setting to its<br>default value.                                                                                                                                                                                                                                                                                                                                                                                                 |
| **Matcher**                    | The codes to use when checking for a successful response from<br>a target. These are called \*_Success codes_<br>• in<br>the console.<br>If the protocol version is HTTP1 or HTTP2, the possible values<br>are from 200 to 499. You can specify multiple values (for<br>example, "200,202") or a range of values (for example,<br>"200-299"). The default value is 200.<br>Health check protocol version for gRPC is not currently<br>supported. However, if your target group protocol version is<br>gRPC, you can specify HTTP1 or HTTP2 protocol versions in your<br>health check configuration. |

## Check the health of your targets

You can check the health status of the targets registered with your target
groups.

###### To check the health of your targets using the console

1. Open the Amazon VPC console at
   [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
2. On the navigation pane, under **VPC Lattice**, choose
   **Target groups**.
3. Choose the name of the target group to open its details page.
4. On the **Targets** tab, the **Health status**
   column indicates the status of each target. If the status is any value other than
   `Healthy`, the **Health status details** column contains
   more information.

###### To check the health of your targets using the AWS CLI

Use the [list-targets](../../../cli/latest/reference/vpc-lattice/list-targets.md "../../../cli/latest/reference/vpc-lattice/list-targets.md")
command. The output of this command contains the target health state. If the status
is any value other than `Healthy`, the output also includes a reason code.

###### To receive email notifications about unhealthy targets

Use CloudWatch alarms to initiate a Lambda function to send details about unhealthy
targets.

## Modify the health check settings

You can modify the health check settings for your target group at any time.

###### To modify the health check settings using the console

1. Open the Amazon VPC console at
   [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
2. On the navigation pane, under **VPC Lattice**, choose
   **Target groups**.
3. Choose the name of the target group to open its details page.
4. On the **Health checks** tab, in the
   **Health check settings** section, choose
   **Edit**.
5. Modify the health check settings as needed.
6. Choose **Save changes**.

###### To modify the health check settings using the AWS CLI

Use the [update-target-group](../../../cli/latest/reference/vpc-lattice/update-target-group.md "../../../cli/latest/reference/vpc-lattice/update-target-group.md") command.
