

# Health checks for Managed Endpoints
<a name="health-checks-for-managed-endpoints"></a>

RTB Fabric health checks let you configure application-level health checking for Auto Scaling group (ASG)-backed responder endpoints. When enabled, RTB Fabric continuously probes each Amazon EC2 instance in your ASGs using HTTP or HTTPS health checks and routes traffic only to instances that are confirmed healthy. This reduces error rates during different instance lifecycle stages such as deployments, scaling events, instance failures, and decommissioning.

Without health checks, RTB Fabric routes traffic to all running instances in your ASGs regardless of application readiness. Instances that are booting, deploying, decommissioning, or experiencing application failures still receive traffic, which can cause elevated error rates for your bidding traffic.

**Note**  
Health checks are available only for Auto Scaling group Managed Endpoints on responder gateways. EKS endpoints and domain name endpoints do not support this feature.

## How health checks work
<a name="health-checks-how-it-works"></a>

When you enable health checks, RTB Fabric performs the following operations:

1. **Instance discovery** – RTB Fabric periodically queries your Auto Scaling groups to discover the current set of Amazon EC2 instance IP addresses, grouped by Availability Zone.

1. **Health probing** – RTB Fabric sends HTTP or HTTPS requests to each instance using your configured port, path, protocol, and timeout. An instance is considered healthy if the response status code matches your configured `statusCodeMatcher`.

1. **Health status determination** – RTB Fabric maintains a per-instance health status with threshold-based transitions. An instance must pass a consecutive number of probes (defined by `healthyThresholdCount`) to be marked healthy, and fail a consecutive number of probes (defined by `unhealthyThresholdCount`) to be marked unhealthy. This prevents single transient failures from removing instances from rotation.

1. **Traffic routing** – RTB Fabric routes bid request traffic only to instances that are confirmed healthy. Healthy instances are tracked per Availability Zone, enabling AZ-aware routing decisions.

Health checks are distributed across multiple hosts and use a consensus mechanism to determine target health. Therefore, your instances may receive more than the configured number of health check probes.

### Key behaviors
<a name="health-checks-key-behaviors"></a>
+ **Threshold-based transitions** – Once healthy, an instance must fail for `unhealthyThresholdCount` consecutive probes before being marked unhealthy. A single failed probe does not remove an instance from rotation. Similarly, an unhealthy instance must pass `healthyThresholdCount` consecutive probes before being marked healthy again.
+ **Fail-open** – If health checking is temporarily unavailable, or if all your instances are deemed unhealthy, RTB Fabric falls back to routing traffic to all discovered instances rather than routing to no instances. This ensures your bidding traffic continues to flow.
+ **Configuration updates** – Changes to health check parameters (such as interval, thresholds, port, or path) take effect automatically after you update the responder gateway.

## Enabling health checks
<a name="health-checks-enabling"></a>

To enable health checks, add a `healthCheckConfig` object to the `autoScalingGroups` configuration when creating or updating a responder gateway. The presence of `healthCheckConfig` is the enablement signal – when omitted, no active health checking is performed.

**Important**  
You must explicitly specify `port` and `path` so that RTB Fabric sends health check probes to the correct endpoint on your instances.

### Enabling health checks (console)
<a name="health-checks-enabling-console"></a>

**To enable health checks when creating a responder gateway**

1. Sign in to the AWS Management Console and open the RTB Fabric console at [https://console.aws.amazon.com/rtbfabric](https://console.aws.amazon.com/rtbfabric).

1. In the navigation pane, choose **Responder gateways**.

1. Choose **Create responder gateway**.

1. In the **Responder endpoint configuration** section, choose **Auto Scaling group** as the endpoint type.

1. Configure the Auto Scaling group settings (group names, IAM role, port, and protocol).

1. In the **Health check configuration** section, configure the health check settings:

   1. For **Health check port**, enter the port on each instance where your health check endpoint is available.

   1. For **Health check path**, enter the HTTP path to probe (for example, `/health`). Must start with `/`.

   1. (Optional) For **Protocol**, select **HTTP** or **HTTPS**. Default: HTTP.

   1. (Optional) Configure advanced settings such as timeout, interval, status code matcher, and threshold counts.

1. Choose **Create Gateway**.

### AWS CLI
<a name="health-checks-enabling-cli"></a>

**Create a responder gateway with health checks**

```
$ aws rtbfabric create-responder-gateway \
--description {{"Responder gateway with health checks"}} \
--vpc-id {{vpc-01f345ad6524a6d7}} \
--subnet-ids {{subnet-abc12345 subnet-def67890}} \
--security-group-ids {{sg-12345678}} \
--port {{8080}} \
--protocol {{HTTP}} \
--managed-endpoint-configuration {{'{"autoScalingGroups":{"autoScalingGroupNames":["my-bidder-asg"],"roleArn":"arn:aws:iam::123456789012:role/MyASGRole","healthCheckConfig":{"port":8081,"path":"/health"}}}'}} \
--client-token {{"unique-client-token-456"}} \
--endpoint-url https://rtbfabric.{{us-east-1}}.amazonaws.com \
--region {{us-east-1}}
```

When only `port` and `path` are specified, all other fields use their default values.

**Update health check configuration**

Use `UpdateResponderGateway` to add health checks to an existing gateway or modify the health check settings.

```
$ aws rtbfabric update-responder-gateway \
--gateway-id {{"rtb-gw-abc123def456"}} \
--managed-endpoint-configuration {{'{"autoScalingGroups":{"autoScalingGroupNames":["my-bidder-asg"],"roleArn":"arn:aws:iam::123456789012:role/MyASGRole","healthCheckConfig":{"port":8081,"path":"/health","protocol":"HTTPS","timeoutMs":1000,"intervalSeconds":10,"statusCodeMatcher":"200-299","healthyThresholdCount":3,"unhealthyThresholdCount":3}}}'}} \
--endpoint-url https://rtbfabric.{{us-east-1}}.amazonaws.com \
--region {{us-east-1}}
```

## Health check configuration reference
<a name="health-checks-configuration-reference"></a>

The following table describes the settings for health checks. The setting names used in the table are the API field names within the `healthCheckConfig` object.


| Setting | Description | Default | Range | Required | 
| --- | --- | --- | --- | --- | 
| `port` | The port on each instance to probe. This should be the port where your application's health check endpoint is available, which is typically different from the RTB traffic port. | – | 80–65535 | Yes | 
| `path` | The HTTP path to probe on each instance (for example, `/health`). Must start with `/`. | – | 1–128 characters | Yes | 
| `protocol` | The protocol for the health check probe. | `HTTP` | `HTTP`, `HTTPS` | No | 
| `timeoutMs` | The time, in milliseconds, during which no response from a target means a failed health check. | 500 | 100–5000 | No | 
| `intervalSeconds` | The approximate amount of time, in seconds, between health checks of an individual target. | 5 | 5–60 | No | 
| `statusCodeMatcher` | The HTTP status codes to use when checking for a successful response from a target. You can specify a single code (`"200"`), a comma-separated list (`"200,204"`), or a range (`"200-299"`). | `"200"` | 1–50 characters | No | 
| `healthyThresholdCount` | The number of consecutive successful health checks required before an unhealthy target is considered healthy. | 5 | 2–10 | No | 
| `unhealthyThresholdCount` | The number of consecutive failed health checks required before a healthy target is considered unhealthy. | 2 | 2–10 | No | 

## Security group requirements
<a name="health-checks-security-groups"></a>

For health checks to work, RTB Fabric must be able to reach the health check port on your instances. RTB Fabric sends health check probes through a network interface in your VPC. You must configure your instance security groups to allow inbound traffic on the health check port from your VPC CIDR.

**Important**  
If your health check port is different from the RTB traffic port, you must add an additional inbound rule to your instance security groups for the health check port. Without this rule, all health check probes will fail and no instances will be marked healthy.

Add the following inbound rule to the security groups attached to your Amazon EC2 instances:


| Type | Protocol | Port range | Source | 
| --- | --- | --- | --- | 
| Custom TCP | TCP (HTTP or HTTPS based on your health check protocol configuration) | Your health check port (for example, 8081) | Your VPC CIDR (for example, `10.0.0.0/16`). If your VPC has secondary CIDR blocks, include those as well. | 

This is similar to how Elastic Load Balancing health checks require inbound rules on target security groups for the health check port. For more information about load balancer security group requirements, see [Update the security groups for your Application Load Balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/load-balancer-update-security-groups.html) in the *Elastic Load Balancing User Guide*.

**Tip**  
Verify that your security groups allow traffic on the health check port *before* enabling health checks. If health check probes cannot reach your instances, all instances will be marked unhealthy. Because RTB Fabric uses fail-open behavior, traffic will fall back to all instances, but the health check feature will not provide any benefit until the security group is corrected.

## Viewing health check configuration
<a name="health-checks-viewing"></a>

You can view the current health check configuration for a responder gateway using the console or the AWS CLI.

**To view health check configuration (console)**

1. Sign in to the AWS Management Console and open the RTB Fabric console at [https://console.aws.amazon.com/rtbfabric](https://console.aws.amazon.com/rtbfabric).

1. In the navigation pane, choose **Responder gateways**.

1. Select the gateway and choose **View details**.

1. The **Health check configuration** section displays the current settings, or indicates that health checks are not configured.

### AWS CLI
<a name="health-checks-viewing-cli"></a>

Use the following command to view the current health check configuration for a responder gateway.

```
$ aws rtbfabric get-responder-gateway \
--gateway-id {{"rtb-gw-abc123def456"}} \
--endpoint-url https://rtbfabric.{{us-east-1}}.amazonaws.com \
--region {{us-east-1}}
```

If health checks are configured, the response includes a `healthCheckConfig` object within the `managedEndpointConfiguration`:

```
{
    "gatewayId": "rtb-gw-abc123def456",
    "managedEndpointConfiguration": {
        "autoScalingGroups": {
            "autoScalingGroupNames": ["my-bidder-asg"],
            "roleArn": "arn:aws:iam::123456789012:role/MyASGRole",
            "healthCheckConfig": {
                "port": 8081,
                "path": "/health",
                "protocol": "HTTP",
                "timeoutMs": 500,
                "intervalSeconds": 5,
                "statusCodeMatcher": "200",
                "healthyThresholdCount": 5,
                "unhealthyThresholdCount": 2
            }
        }
    }
}
```

If health checks are not configured, the `healthCheckConfig` field is absent from the response.

## Best practices
<a name="health-checks-best-practices"></a>
+ **Update security groups before enabling health checks** – Ensure that your instance security groups allow inbound traffic on the health check port from your VPC CIDR before you enable health checks. See [Security group requirements](#health-checks-security-groups).
+ **Choose appropriate thresholds** – Set `unhealthyThresholdCount` low to quickly remove failing instances from rotation. Set `healthyThresholdCount` higher to ensure instances are fully stable before receiving traffic again.
+ **Match the timeout to your health endpoint** – Set `timeoutMs` to a value that accommodates your health endpoint's typical response time with some margin.
+ **Monitor healthy target IP counts** – After enabling health checks, monitor the `healthy-target-ip-count` CloudWatch metric. A sudden drop compared to `target-ip-count` may indicate that health check probes are failing for your instances. For more information, see [RTB Fabric metrics](monitoring-cloudwatch-metrics.md).

## Troubleshooting health checks
<a name="health-checks-troubleshooting"></a>

The following are common issues with health checks and steps to resolve them.

### All instances are unhealthy
<a name="health-checks-troubleshooting-all-unhealthy"></a>

**Symptom:** After enabling health checks, the `healthy-target-ip-count` metric is zero while `target-ip-count` shows the expected number of instances.

**Possible causes:**
+ **Security group misconfigured** – Your instance security groups do not allow inbound traffic on the health check port from your VPC CIDR. Verify the inbound rules on your instance security groups. See [Security group requirements](#health-checks-security-groups).
+ **Wrong port or path** – The configured `port` or `path` does not match where your health endpoint is actually listening. Verify your health check configuration using `GetResponderGateway`, and test the endpoint locally on an instance by running `curl http://localhost:{{port}}{{/path}}`.
+ **Health endpoint returning unexpected status code** – Your health endpoint returns a status code that does not match the configured `statusCodeMatcher`. Verify the response code by testing the endpoint locally and adjust the `statusCodeMatcher` if needed.
+ **Timeout too short** – The configured `timeoutMs` is shorter than your health endpoint's response time. Increase the timeout value or optimize your health endpoint's response time.

### Some instances are unhealthy
<a name="health-checks-troubleshooting-some-unhealthy"></a>

**Symptom:** The `healthy-target-ip-count` metric is lower than `target-ip-count`, indicating that some instances are failing health checks.

**Possible causes:**
+ **Instances are deploying** – During rolling deployments, instances that are restarting or not yet ready may fail health checks. This is expected behavior. The `healthy-target-ip-count` should recover after deployment completes.
+ **Application issues on specific instances** – Some instances may have application-level issues. Check your application logs on the affected instances.
+ **Availability Zone issues** – If all unhealthy instances are in the same Availability Zone, there may be a network or infrastructure issue affecting that zone.

### No healthy-target-ip-count metric
<a name="health-checks-troubleshooting-no-metric"></a>

**Symptom:** The `healthy-target-ip-count` metric does not appear in CloudWatch after enabling health checks.

**Possible causes:**
+ **Health check configuration not saved** – Verify that the `healthCheckConfig` is present in the gateway configuration by calling `GetResponderGateway`. See [Viewing health check configuration](#health-checks-viewing).
+ **Gateway still activating or updating** – After enabling or updating health checks, the health checking infrastructure requires a few minutes to deploy. Wait for the gateway status to return to **Active** and check the metric again.