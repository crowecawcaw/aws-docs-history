# Edit target group attributes for your Application Load Balancer

After you create a target group for you Application Load Balancer, you can edit its target group attributes.

###### Target group attributes

- [Deregistration delay](#deregistration-delay "#deregistration-delay")
- [Routing algorithm](#modify-routing-algorithm "#modify-routing-algorithm")
- [Slow start mode](#slow-start-mode "#slow-start-mode")
- [Health settings](#modify-target-group-health-settings "#modify-target-group-health-settings")
- [Cross-zone load balancing](#modify-cross-zone "#modify-cross-zone")
- [Automatic Target Weights (ATW)](#automatic-target-weights "#automatic-target-weights")
- [Sticky sessions](#sticky-sessions "#sticky-sessions")

## Deregistration delay

ELB stops sending requests to targets that are deregistering. By default, ELB
waits 300 seconds before completing the deregistration process, which can help in-flight
requests to the target to complete. To change the amount of time that ELB waits,
update the deregistration delay value.

The initial state of a deregistering target is `draining`. After the
deregistration delay elapses, the deregistration process completes and the state of the
target is `unused`. If the target is part of an Auto Scaling group, it can be
terminated and replaced.

If a deregistering target has no in-flight requests and no active connections, ELB
immediately completes the deregistration process, without waiting for the deregistration
delay to elapse. However, even though target deregistration is complete, the status of
the target is displayed as `draining` until the deregistration delay timeout
expires. After the timeout expires, the target transitions to an `unused`
state.

If a deregistering target terminates the connection before the deregistration delay
elapses, the client receives a 500-level error response.

Console

###### To update the deregistration delay value

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. On the navigation pane, under **Load Balancing**,
   choose **Target Groups**.
3. Choose the name of the target group to open its details
   page.
4. On the **Attributes** tab, choose
   **Edit**.
5. In the **Target deregistration management** pane,
   enter a new value for **Deregistration delay**.
6. Choose **Save changes**.

AWS CLI

###### To update the deregistration delay value

Use the [modify-target-group-attributes](../../../cli/latest/reference/elbv2/modify-target-group-attributes.md "../../../cli/latest/reference/elbv2/modify-target-group-attributes.md") command with the
`deregistration_delay.timeout_seconds` attribute.

```
aws elbv2 modify-target-group-attributes \
    --target-group-arn `target-group-arn` \
    --attributes "Key=deregistration_delay.timeout_seconds,Value=`60`"
```

CloudFormation

###### To update the deregistration delay value

Update the [AWS::ElasticLoadBalancingV2::TargetGroup](../../../AWSCloudFormation/latest/TemplateReference/aws-resource-elasticloadbalancingv2-targetgroup.md "../../../AWSCloudFormation/latest/TemplateReference/aws-resource-elasticloadbalancingv2-targetgroup.md") resource
to include the `deregistration_delay.timeout_seconds`
attribute.

```
Resources:
  myTargetGroup:
    Type: 'AWS::ElasticLoadBalancingV2::TargetGroup'
    Properties:
      Name: my-target-group
      Protocol: HTTP
      Port: 80
      TargetType: ip
      VpcId: !Ref myVPC
      TargetGroupAttributes:
        - Key: "deregistration_delay.timeout_seconds"
          Value: "`60`"
```

## Routing algorithm

A routing algorithm is a method used by the load balancer when determining which targets
will receive requests. The **round robin** routing algorithm is used by default
to route requests at the target group level. The **least outstanding requests**
and **weighted random** routing algorithms are also available based on the needs of
your application. A target group can only have one active routing algorithm at a time, however the
routing algorithm can be updated whenever needed.

If you enable sticky sessions, the selected routing algorithm is used for the initial
target selection. Future requests from the same client will be forwarded to the
same target, bypassing the selected routing algorithm. If you have enabled target optimizer, the routing
algorithm can only be round robin.

###### Round robin

- The round robin routing algorithm routes requests evenly across
  healthy targets in the target group, in a sequential order.
- This algorithm is commonly used when the requests being received are similar in complexity
  , the registered targets are similar in processing capability, or if you need to distribute requests equally among targets.

###### Least outstanding requests

- The least outstanding requests routing algorithm routes requests to the targets with the
  lowest number of in progress requests.
- This algorithm is commonly used when the requests being received vary in complexity,
  the registered targets vary in processing capability.
- When a load balancer that supports HTTP/2 is using targets that only support HTTP/1.1,
  it converts the request to multiple HTTP/1.1 requests. In this configuration the least
  outstanding requests algorithm will treat each HTTP/2 request as multiple requests.
- When using WebSockets, the target is selected using the least outstanding requests algorithm.
  After the target is selected, the load balancer creates a connection to the target and sends
  all messages over this connection.
- The least outstanding requests routing algorithm can not be used with slow start mode.

###### Weighted random

- The weighted random routing algorithm routes requests evenly across healthy targets
  in the target group, in a random order.
- This algorithm supports Automatic Target Weights (ATW) anomaly mitigation.
- The weighted random routing algorithm can not be used with slow start mode.
- The weighted random routing algorithm can not be used with sticky sessions.

Console

###### To update the routing algorithm

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. On the navigation pane, under **Load Balancing**,
   choose **Target Groups**.
3. Choose the name of the target group to open its details
   page.
4. On the **Attributes** tab, choose
   **Edit**.
5. In the **Traffic configuration** pane, for
   **Load balancing algorithm**, choose
   **Round robin**,
   **Least outstanding requests**, or
   **Weighted random**.
6. Choose **Save changes**.

AWS CLI

###### To update the routing algorithm

Use the [modify-target-group-attributes](../../../cli/latest/reference/elbv2/modify-target-group-attributes.md "../../../cli/latest/reference/elbv2/modify-target-group-attributes.md") command with the
`load_balancing.algorithm.type` attribute.

```
aws elbv2 modify-target-group-attributes \
    --target-group-arn `target-group-arn` \
    --attributes "Key=load_balancing.algorithm.type,Value=`least_outstanding_requests`"
```

CloudFormation

###### To update the routing algorithm

Update the [AWS::ElasticLoadBalancingV2::TargetGroup](../../../AWSCloudFormation/latest/TemplateReference/aws-resource-elasticloadbalancingv2-targetgroup.md "../../../AWSCloudFormation/latest/TemplateReference/aws-resource-elasticloadbalancingv2-targetgroup.md") resource
to include the `load_balancing.algorithm.type` attribute.

```
Resources:
  myTargetGroup:
    Type: 'AWS::ElasticLoadBalancingV2::TargetGroup'
    Properties:
      Name: my-target-group
      Protocol: HTTP
      Port: 80
      TargetType: ip
      VpcId: !Ref myVPC
      TargetGroupAttributes:
        - Key: "load_balancing.algorithm.type"
          Value: "`least_outstanding_requests`"

```

## Slow start mode

By default, a target starts to receive its full share of requests as soon as it is
registered with a target group and passes an initial health check. Using slow start mode
gives targets time to warm up before the load balancer sends them a full share of
requests.

After you enable slow start for a target group, its targets enter slow start mode when
they are considered healthy by the target group. A target in slow start mode exits slow
start mode when the configured slow start duration period elapses or the target becomes
unhealthy. The load balancer linearly increases the number of requests that it can send
to a target in slow start mode. After a healthy target exits slow start mode, the load
balancer can send it a full share of requests.

###### Considerations

- When you enable slow start for a target group, the healthy targets registered
  with the target group do not enter slow start mode.
- When you enable slow start for an empty target group and then register targets
  using a single registration operation, these targets do not enter slow start
  mode. Newly registered targets enter slow start mode only when there is at least
  one healthy target that is not in slow start mode.
- If you deregister a target in slow start mode, the target exits slow start
  mode. If you register the same target again, it enters slow start mode when it
  is considered healthy by the target group.
- If a target in slow start mode becomes unhealthy, the target exits slow start
  mode. When the target becomes healthy, it enters slow start mode again.
- You can't enable slow start mode when using the **least outstanding requests**
  or **weighted random** routing algorithms.

Console

###### To update the slow start duration value

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. On the navigation pane, under **Load Balancing**,
   choose **Target Groups**.
3. Choose the name of the target group to open its details
   page.
4. On the **Attributes** tab, choose
   **Edit**.
5. In the **Traffic configuration** pane,
   enter a new value for **Slow start duration**.
   To disable slow start mode, enter 0.
6. Choose **Save changes**.

AWS CLI

###### To update the slow start duration value

Use the [modify-target-group-attributes](../../../cli/latest/reference/elbv2/modify-target-group-attributes.md "../../../cli/latest/reference/elbv2/modify-target-group-attributes.md") command with the
`slow_start.duration_seconds` attribute.

```
aws elbv2 modify-target-group-attributes \
    --target-group-arn `target-group-arn` \
    --attributes "Key=slow_start.duration_seconds,Value=`30`"
```

CloudFormation

###### To update the slow start duration value

Update the [AWS::ElasticLoadBalancingV2::TargetGroup](../../../AWSCloudFormation/latest/TemplateReference/aws-resource-elasticloadbalancingv2-targetgroup.md "../../../AWSCloudFormation/latest/TemplateReference/aws-resource-elasticloadbalancingv2-targetgroup.md") resource
to include the `slow_start.duration_seconds`
attribute.

```
Resources:
  myTargetGroup:
    Type: 'AWS::ElasticLoadBalancingV2::TargetGroup'
    Properties:
      Name: my-target-group
      Protocol: HTTP
      Port: 80
      TargetType: ip
      VpcId: !Ref myVPC
      TargetGroupAttributes:
        - Key: "slow_start.duration_seconds"
          Value: "`30`"
```

## Health settings

By default, Application Load Balancers monitor the health of targets and route requests to healthy targets.
However, if the load balancer doesn't have enough healthy targets, it automatically sends
traffic to all registered targets (fail open). You can modify the target group health
settings for your target group to define the thresholds for DNS failover and routing
failover. For more information, see [Target group health](load-balancer-target-groups.md#target-group-health "load-balancer-target-groups.md#target-group-health").

Console

###### To modify target group health settings

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation pane, under **Load Balancing**,
   choose **Target Groups**.
3. Choose the name of the target group to open its details
   page.
4. On the **Attributes** tab, choose
   **Edit**.
5. Check whether cross-zone load balancing is turned on or turned off. Update
   this setting as needed to ensure that you have enough capacity to handle the
   additional traffic if a zone fails.
6. Expand **Target group health requirements**.
7. For **Configuration type**, we recommend that
   you choose **Unified configuration**, which sets
   the same threshold for both actions.
8. For **Healthy state requirements**, do one of
   the following:
   - Choose **Minimum healthy target count**, and then
     enter a number from 1 to the maximum number of targets for your
     target group.
   - Choose **Minimum healthy target percentage**,
     and then enter a number from 1 to 100.

9. Choose **Save changes**.

AWS CLI

###### To modify target group health settings

Use the [modify-target-group-attributes](../../../cli/latest/reference/elbv2/modify-target-group-attributes.md "../../../cli/latest/reference/elbv2/modify-target-group-attributes.md") command. The following example sets
the healthy threshold for both unhealthy state actions to 50%.

```
aws elbv2 modify-target-group-attributes \
    --target-group-arn `target-group-arn` \
    --attributes \
        "Key=target_group_health.dns_failover.minimum_healthy_targets.percentage,Value=`50`" \
        "Key=target_group_health.unhealthy_state_routing.minimum_healthy_targets.percentage,Value=`50`"
```

CloudFormation

###### To modify target group health settings

Update the [AWS::ElasticLoadBalancingV2::TargetGroup](../../../AWSCloudFormation/latest/TemplateReference/aws-resource-elasticloadbalancingv2-targetgroup.md "../../../AWSCloudFormation/latest/TemplateReference/aws-resource-elasticloadbalancingv2-targetgroup.md") resource.
The following example sets the healthy threshold for both
unhealthy state actions to 50%.

```
Resources:
  myTargetGroup:
    Type: 'AWS::ElasticLoadBalancingV2::TargetGroup'
    Properties:
      Name: my-target-group
      Protocol: HTTP
      Port: 80
      TargetType: ip
      VpcId: !Ref myVPC
      TargetGroupAttributes:
        - Key: "target_group_health.dns_failover.minimum_healthy_targets.percentage"
          Value: "`50`"
        - Key: "target_group_health.unhealthy_state_routing.minimum_healthy_targets.percentage"
          Value: "`50`"
```

## Cross-zone load balancing

The nodes for your load balancer distribute requests from clients to registered targets.
When cross-zone load balancing is on, each load balancer node distributes traffic across the
registered targets in all registered Availability Zones. When cross-zone load balancing is
off, each load balancer node distributes traffic only across the registered targets in its
Availability Zone. This could be if zonal failure domains are preferred over regional,
ensuring that a healthy zone isn't impacted by an unhealthy zone, or for overall latency
improvements.

With Application Load Balancers, cross-zone load balancing is always turned on at the load balancer level, and
cannot be turned off. For target groups, the default is to use the load balancer setting,
but you can override the default by explicitly turning cross-zone load balancing off
at the target group level.

###### Considerations

- Target stickiness is not supported when cross-zone load balancing is off.
- Lambda functions as targets are not supported when cross-zone load balancing is off.
- Attempting to turn off cross-zone load balancing through the
  `ModifyTargetGroupAttributes` API if any targets have parameter
  `AvailabilityZone` set to `all` results in an
  error.
- When registering targets, the `AvailabilityZone` parameter is required.
  Specific Availability Zone values are only allowed when cross-zone load balancing is
  off. Otherwise, the parameter is ignored and treated as `all`.

###### Best practices

- Plan for enough target capacity across all Availability Zones that you expect to
  utilize, per target group. If you can't plan for enough capacity across all
  participating Availability Zones, we recommend that you keep cross-zone load
  balancing on.
- When configuring your Application Load Balancer with multiple target groups, ensure all target groups
  are participating in the same Availability Zones, within the configured Region. This
  is to avoid an Availability Zone being empty while cross-zone load balancing is off,
  as this triggers a 503 error for all HTTP requests that enter the empty Availability
  Zone.
- Avoid creating empty subnets. Application Load Balancers expose zonal IP addresses through DNS for the
  empty subnets, which triggers 503 errors for HTTP requests.
- There can be occurrences where a target group with cross-zone load balancing
  turned off has enough planned target capacity per Availability Zone, but all targets
  in an Availability Zone become unhealthy. When there is at least one target group
  with all unhealthy targets, the IP addresses of the load balancer nodes are removed
  from DNS. After the target group has at least one healthy target, the IP addresses
  are restored to DNS.

### Turn off cross-zone load balancing

You can turn off cross-zone load balancing for your Application Load Balancer target groups at any time.

Console

###### To turn off cross-zone load balancing

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. On the navigation pane, under **Load Balancing**,
   choose **Target Groups**.
3. Choose the name of the target group to open its details page.
4. On the **Attributes** tab, select
   **Edit**.
5. In the **Target selection configuration** pane,
   choose **Off** for **Cross-zone load
   balancing**.
6. Choose **Save changes**.

AWS CLI

###### To turn off cross-zone load balancing

Use the [modify-target-group-attributes](../../../cli/latest/reference/elbv2/modify-target-group-attributes.md "../../../cli/latest/reference/elbv2/modify-target-group-attributes.md") command and set the
`load_balancing.cross_zone.enabled` attribute to
`false`.

```
aws elbv2 modify-target-group-attributes \
    --target-group-arn `target-group-arn` \
    --attributes "Key=load_balancing.cross_zone.enabled,Value=false"
```

CloudFormation

###### To turn off cross-zone load balancing

Update the [AWS::ElasticLoadBalancingV2::TargetGroup](../../../AWSCloudFormation/latest/TemplateReference/aws-resource-elasticloadbalancingv2-targetgroup.md "../../../AWSCloudFormation/latest/TemplateReference/aws-resource-elasticloadbalancingv2-targetgroup.md") resource
to include the `load_balancing.cross_zone.enabled`
attribute.

```
Resources:
  myTargetGroup:
    Type: 'AWS::ElasticLoadBalancingV2::TargetGroup'
    Properties:
      Name: my-target-group
      Protocol: HTTP
      Port: 80
      TargetType: ip
      VpcId: !Ref myVPC
      TargetGroupAttributes:
        - Key: "load_balancing.cross_zone.enabled"
          Value: "`false`"
```

### Turn on cross-zone load balancing

You can turn on cross-zone load balancing for your Application Load Balancer target groups at any time.
The cross-zone load balancing setting at the target group level overrides the setting at
the load balancer level.

Console

###### To turn off cross-zone load balancing

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. On the navigation pane, under **Load Balancing**,
   choose **Target Groups**.
3. Choose the name of the target group to open its details page.
4. On the **Attributes** tab, select
   **Edit**.
5. In the **Target selection configuration** pane,
   choose **On** for **Cross-zone load
   balancing**.
6. Choose **Save changes**.

AWS CLI

###### To turn on cross-zone load balancing

Use the [modify-target-group-attributes](../../../cli/latest/reference/elbv2/modify-target-group-attributes.md "../../../cli/latest/reference/elbv2/modify-target-group-attributes.md") command and set the
`load_balancing.cross_zone.enabled` attribute to
`true`.

```
aws elbv2 modify-target-group-attributes \
    --target-group-arn `target-group-arn` \
    --attributes "Key=load_balancing.cross_zone.enabled,Value=true"
```

CloudFormation

###### To turn on cross-zone load balancing

Update the [AWS::ElasticLoadBalancingV2::TargetGroup](../../../AWSCloudFormation/latest/TemplateReference/aws-resource-elasticloadbalancingv2-targetgroup.md "../../../AWSCloudFormation/latest/TemplateReference/aws-resource-elasticloadbalancingv2-targetgroup.md") resource
to include the `load_balancing.cross_zone.enabled`
attribute.

```
Resources:
  myTargetGroup:
    Type: 'AWS::ElasticLoadBalancingV2::TargetGroup'
    Properties:
      Name: my-target-group
      Protocol: HTTP
      Port: 80
      TargetType: ip
      VpcId: !Ref myVPC
      TargetGroupAttributes:
        - Key: "load_balancing.cross_zone.enabled"
          Value: "`true`"
```

## Automatic Target Weights (ATW)

Automatic Target Weights (ATW) constantly monitors the targets running your applications,
detecting significant performance deviations, known as anomalies. ATW provides the ability to dynamically adjust the
amount of traffic routed to targets, through real time data anomaly detection.

Automatic Target Weights (ATW) performs anomaly detection on every Application Load Balancer in your
account automatically. When anomalous targets are identified, ATW can automatically
attempt to stabilize them by reducing the amount of traffic they're routed, known as
anomaly mitigation. ATW continuously optimizes traffic distribution to maximize
per-target success rates while minimizing target group failure rates.

###### Considerations:

- Anomaly detection currently monitors HTTP 5xx response codes coming from, and
  connection failures to, your targets. Anomaly detection is always on and can't
  be turned off.
- ATW is not supported when using Lambda as a target.

###### Contents

- [Anomaly detection](edit-target-group-attributes.md#anomaly-detection "edit-target-group-attributes.md#anomaly-detection")
- [Anomaly mitigation](edit-target-group-attributes.md#anomaly-mitigation "edit-target-group-attributes.md#anomaly-mitigation")

### Anomaly detection

ATW anomaly detection monitors for any targets that are displaying a significant deviation
in behavior from other targets in their target group. These deviations, called anomalies, are
determined by comparing the percent errors of one target with the percent errors of other
targets in the target group. These errors can be both connection errors and HTTP error codes. Targets
reporting significantly higher than their peers are then considered anomalous.

Anomaly detection requires a minimum of three healthy targets in the target group. When a
target is registered to a target group it must pass the health checks before receiving
traffic. After the target starts receiving traffic, ATW begins monitoring the target and continuously
publishes the anomaly result. For targets without anomalies, the anomaly result is `normal`.
For targets with anomalies, the anomaly result is `anomalous`.

ATW anomaly detection works independently from target group health checks. A target can be passing
all target group health checks, but still be marked anomalous due to an elevated error rate. Targets becoming
anomalous does not affect their target group health check status.

###### Anomaly detection status

You can view the current anomaly detection status. The following are the possible values:

- `normal` – No anomalies were detected.
- `anomalous` – Anomalies were detected.

Console

###### To view the anomaly detection status

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. On the navigation pane, under **Load Balancing**,
   choose **Target Groups**.
3. Choose the name of the target group to open its details
   page.
4. Choose the **Targets** tab.
5. Within the **Registered targets** table, the
   **Anomaly detection result** column displays
   the anomaly status of each target.

AWS CLI

###### To view the anomaly detection status

Use the [describe-target-health](../../../cli/latest/reference/elbv2/describe-target-health.md "../../../cli/latest/reference/elbv2/describe-target-health.md") command. The following example
displays the status for every target in the specified target group.

```
aws elbv2 describe-target-health \
    --target-group-arn `target-group-arn` \
    --include AnomalyDetection
```

### Anomaly mitigation

ATW anomaly mitigation routes traffic away from anomalous targets automatically, giving them an
opportunity to recover.

###### Requirement

The anomaly mitigation function of ATW is only available when using the **Weighted random**
routing algorithm.

###### During mitigation:

- ATW periodically adjusts the amount of traffic routed to anomalous targets.
  Currently, the period is every five seconds.
- ATW reduces the amount of traffic routed to anomalous targets to the minimum amount
  required to perform anomaly mitigation.
- Targets which are no longer detected as anomalous will gradually have more traffic routed to
  them until they reach parity with other normal targets in the target group.

Console

###### To turn on anomaly mitigation

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. On the navigation pane, under **Load Balancing**,
   choose **Target Groups**.
3. Choose the name of the target group to open its details
   page.
4. On the **Attributes** tab, choose
   **Edit**.
5. In the **Traffic configuration** pane, verify that
   the selected value for **Load balancing algorithm**
   is **Weighted random**.

When the weighted random algorithm is initially selected,
anomaly detection is on by default. 6. Under **Anomaly mitigation**, ensure that
**Turn on anomaly mitigation** is selected. 7. Choose **Save changes**.

AWS CLI

###### To turn on anomaly mitigation

Use the [modify-target-group-attributes](../../../cli/latest/reference/elbv2/modify-target-group-attributes.md "../../../cli/latest/reference/elbv2/modify-target-group-attributes.md") command with the
`load_balancing.algorithm.anomaly_mitigation` attribute.

```
aws elbv2
```

###### Mitigation status

You can check whether ATW is performing mitigation on a target. The following are the possible
values:

- `yes` – Mitigation is in progress.
- `no` – Mitigation is not in progress.

Console

###### To view the anomaly mitigation status

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. On the navigation pane, under **Load Balancing**,
   choose **Target Groups**.
3. Choose the name of the target group to open its details
   page.
4. Choose the **Targets** tab.
5. Within the **Registered targets** table, you can
   view the anomaly mitigation status of each target in the
   **Mitigation in effect** column.

AWS CLI

###### To view the anomaly mitigation status

Use the [describe-target-health](../../../cli/latest/reference/elbv2/describe-target-health.md "../../../cli/latest/reference/elbv2/describe-target-health.md") command. The following example
displays the status for every target in the specified target group.

```
aws elbv2 describe-target-health \
    --target-group-arn `target-group-arn` \
    --include AnomalyDetection
```

## Sticky sessions

By default, an Application Load Balancer routes each request independently to a registered target based on
the chosen load-balancing algorithm. However, you can use the sticky session feature
(also known as session affinity) to enable the load balancer to bind a user's session to
a specific target. This ensures that all requests from the user during the session are
sent to the same target. This feature is useful for servers that maintain state
information in order to provide a continuous experience to clients. To use sticky
sessions, the client must support cookies.

Application Load Balancers support both duration-based cookies and application-based cookies. Sticky
sessions are enabled at the target group level. You can use a combination of
duration-based stickiness, application-based stickiness, and no stickiness across
your target groups.

The key to managing sticky sessions is determining how long your load balancer should
consistently route the user's request to the same target. If your application has its
own session cookie, then you can use application-based stickiness and the load balancer
session cookie follows the duration specified by the application's session cookie. If
your application does not have its own session cookie, then you can use duration-based
stickiness to generate a load balancer session cookie with a duration that you specify.

The content of load balancer generated cookies are encrypted using a rotating key. You
can't decrypt or modify load balancer generated cookies.

For both stickiness types, the Application Load Balancer resets the expiry of the cookies it generates
after every request. If a cookie expires, the session is no longer sticky and the client
should remove the cookie from its cookie store.

###### Requirements

- An HTTP/HTTPS load balancer.
- At least one healthy instance in each Availability Zone.

###### Considerations

- Sticky sessions are not supported if [cross-zone load balancing](#modify-cross-zone "#modify-cross-zone")
  is disabled. Attempts to enable sticky sessions while cross-zone load balancing is disabled fail.
- For application-based cookies, cookie names have to be specified individually
  for each target group. However, for duration-based cookies, `AWSALB`
  is the only name used across all target groups.
- If you are using multiple layers of Application Load Balancers, you can enable
  sticky sessions across all layers with application-based cookies. However, with
  duration-based cookies, you can enable sticky sessions only on one layer,
  because `AWSALB` is the only name available.
- If the Application Load Balancer receives both an `AWSALBCORS` and an
  `AWSALB` duration-based stickiness cookie, the value in
  `AWSALBCORS` will take precedence.
- Application-based stickiness does not work with weighted target groups.
- If you have a [forward action](rule-action-types.md#forward-actions "rule-action-types.md#forward-actions") with
  multiple target groups, and sticky sessions are enabled for one or more of the
  target groups, you must enable stickiness at the target group level.
- WebSocket connections are inherently sticky. If the client requests a
  connection upgrade to WebSockets, the target that returns an HTTP 101 status
  code to accept the connection upgrade is the target used in the WebSockets
  connection. After the WebSockets upgrade is complete, cookie-based stickiness is
  not used.
- Application Load Balancers use the `Expires` attribute in the cookie header instead of
  the `Max-Age` attribute.
- Application Load Balancers do not support cookie values that are URL encoded.
- If the Application Load Balancer receives a new request while the target is draining
  due to deregistration, the request is routed to a healthy target.
- Sticky sessions are not supported if target optimizer is enabled.

###### Stickiness types

- [Duration-based stickiness](#duration-based-stickiness "#duration-based-stickiness")
- [Application-based stickiness](#application-based-stickiness "#application-based-stickiness")

### Duration-based stickiness

Duration-based stickiness routes requests to the same target in a target group
using a load balancer generated cookie (`AWSALB`). The cookie is used to
map the session to the target. If your application does not have its own session
cookie, you can specify your own stickiness duration and manage how long your load
balancer should consistently route the user's request to the same target.

When a load balancer first receives a request from a client, it routes the request
to a target (based on the chosen algorithm), and generates a cookie named
`AWSALB`. It encodes information about the selected target, encrypts
the cookie, and includes the cookie in the response to the client. The load balancer
generated cookie has its own expiry of 7 days which is non-configurable.

In subsequent requests, the client should include the `AWSALB` cookie.
When the load balancer receives a request from a client that contains the cookie, it
detects it and routes the request to the same target. If the cookie is present but
can't be decoded, or if it refers to a target that was deregistered or is
unhealthy, the load balancer selects a new target and updates the cookie with
information about the new target.

For cross-origin resource sharing (CORS) requests, some browsers require
`SameSite=None; Secure` to enable stickiness. To support these browsers
the load balancer always generates a second stickiness cookie,
`AWSALBCORS`, which includes the same information as the original
stickiness cookie, as well as the `SameSite` attribute. Clients
receive both cookies, including non CORS requests.

Console

###### To enable duration-based stickiness

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. On the navigation pane, under **Load Balancing**, choose
   **Target Groups**.
3. Choose the name of the target group to open its details page.
4. On the **Attributes** tab, choose
   **Edit**.
5. Under **Target selection configuration**, do the
   following:
   1. Select **Turn on stickiness**.
   2. For **Stickiness type**, select **Load
      balancer generated cookie**.
   3. For **Stickiness duration**, specify a value
      between 1 second and 7 days.

6. Choose **Save changes**.

AWS CLI

###### To enable duration-based stickiness

Use the [modify-target-group-attributes](../../../cli/latest/reference/elbv2/modify-target-group-attributes.md "../../../cli/latest/reference/elbv2/modify-target-group-attributes.md") command with the
`stickiness.enabled` and
`stickiness.lb_cookie.duration_seconds` attributes.

```
aws elbv2 modify-target-group-attributes \
    --target-group-arn `target-group-arn` \
    --attributes \
        "Key=stickiness.enabled,Value=true" \
        "Key=stickiness.lb_cookie.duration_seconds,Value=`300`"
```

CloudFormation

###### To enable duration-based stickiness

Update the [AWS::ElasticLoadBalancingV2::TargetGroup](../../../AWSCloudFormation/latest/TemplateReference/aws-resource-elasticloadbalancingv2-targetgroup.md "../../../AWSCloudFormation/latest/TemplateReference/aws-resource-elasticloadbalancingv2-targetgroup.md") resource
to include the `stickiness.enabled` and
`stickiness.lb_cookie.duration_seconds`
attributes.

```
Resources:
  myTargetGroup:
    Type: 'AWS::ElasticLoadBalancingV2::TargetGroup'
    Properties:
      Name: my-target-group
      Protocol: HTTP
      Port: 80
      TargetType: ip
      VpcId: !Ref myVPC
      TargetGroupAttributes:
        - Key: "stickiness.enabled"
          Value: "true"
        - Key: "stickiness.lb_cookie.duration_seconds"
          Value: "`300`"
```

### Application-based stickiness

Application-based stickiness gives you the flexibility to set your own criteria
for client-target stickiness. When you enable application-based stickiness, the load
balancer routes the first request to a target within the target group based on the
chosen algorithm. The target is expected to set a custom application cookie that
matches the cookie configured on the load balancer to enable stickiness. This custom
cookie can include any of the cookie attributes required by the application.

When the Application Load Balancer receives the custom application cookie from the target, it
automatically generates a new encrypted application cookie to capture stickiness
information. This load balancer generated application cookie captures stickiness
information for each target group that has application-based stickiness enabled.

The load balancer generated application cookie does not copy the attributes of the
custom cookie set by the target. It has its own expiry of 7 days which is
non-configurable. In the response to the client, the Application Load Balancer only validates the name
with which the custom cookie was configured at the target group level and not the
value or the expiry attribute of the custom cookie. As long as the name matches, the
load balancer sends both cookies, the custom cookie set by the target, and the
application cookie generated by the load balancer, in the response to the client.

In subsequent requests, clients have to send back both cookies to maintain
stickiness. The load balancer decrypts the application cookie, and checks whether
the configured duration of stickiness is still valid. It then uses the information
in the cookie to send the request to the same target within the target group to
maintain stickiness. The load balancer also proxies the custom application cookie to
the target without inspecting or modifying it. In subsequent responses, the expiry
of the load balancer generated application cookie and the duration of stickiness
configured on the load balancer are reset.
To
maintain stickiness between client and target, the expiry of the cookie, and the
duration of stickiness should not elapse.

If a target fails or becomes unhealthy, the load balancer stops routing requests
to that target, and chooses a new healthy target based on the chosen load balancing
algorithm. The load balancer treats the session as now being "stuck" to the new
healthy target, and continues routing requests to the new healthy target even if the
failed target comes back.

With cross-origin resource sharing (CORS) requests, to enable stickiness, the load
balancer adds the `SameSite=None; Secure` attributes to the load balancer
generated application cookie only if the user-agent version is Chromium80 or
above.

Because most browsers limit cookies to 4K in size, the load balancer shards
application cookies greater than 4K into multiple cookies. Application Load Balancers support cookies up
to 16K in size and can therefore create up to 4 shards that it sends to the client.
The application cookie name that the client sees begins with “AWSALBAPP-" and
includes a fragment number. For example, if the cookie size is 0-4K, the client sees
AWSALBAPP-0. If the cookie size is 4-8k, the client sees AWSALBAPP-0 and
AWSALBAPP-1, and so on.

Console

###### To enable application-based stickiness

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. On the navigation pane, under **Load Balancing**, choose
   **Target Groups**.
3. Choose the name of the target group to open its details page.
4. On the **Attributes** tab, choose
   **Edit**.
5. Under **Target selection configuration**, do the
   following:
   1. Select **Turn on stickiness**.
   2. For **Stickiness type**, select
      **Application-based cookie**.
   3. For **Stickiness duration**, specify a value
      between 1 second and 7 days.
   4. For **App cookie name**, enter a name for your
      application-based cookie.

   Do not use `AWSALB`, `AWSALBAPP`, or
   `AWSALBTG` for the cookie name; they're reserved for
   use by the load balancer.

6. Choose **Save changes**.

AWS CLI

###### To enable application-based stickiness

Use the [modify-target-group-attributes](../../../cli/latest/reference/elbv2/modify-target-group-attributes.md "../../../cli/latest/reference/elbv2/modify-target-group-attributes.md") command with the following
attributes:

- `stickiness.enabled`
- `stickiness.type`
- `stickiness.app_cookie.cookie_name`
- `stickiness.app_cookie.duration_seconds`

```
aws elbv2 modify-target-group-attributes \
    --target-group-arn `target-group-arn` \
    --attributes \
        "Key=stickiness.enabled,Value=true" \
        "Key=stickiness.type,Value=app_cookie" \
        "Key=stickiness.app_cookie.cookie_name,Value=`my-cookie-name`" \
        "Key=stickiness.app_cookie.duration_seconds,Value=`300`"
```

CloudFormation

###### To enable application-based stickiness

Update the [AWS::ElasticLoadBalancingV2::TargetGroup](../../../AWSCloudFormation/latest/TemplateReference/aws-resource-elasticloadbalancingv2-targetgroup.md "../../../AWSCloudFormation/latest/TemplateReference/aws-resource-elasticloadbalancingv2-targetgroup.md") resource
to include the following attributes:

- `stickiness.enabled`
- `stickiness.type`
- `stickiness.app_cookie.cookie_name`
- `stickiness.app_cookie.duration_seconds`

```
Resources:
  myTargetGroup:
    Type: 'AWS::ElasticLoadBalancingV2::TargetGroup'
    Properties:
      Name: my-target-group
      Protocol: HTTP
      Port: 80
      TargetType: ip
      VpcId: !Ref myVPC
      TargetGroupAttributes:
        - Key: "stickiness.enabled"
          Value: "true"
        - Key: "stickiness.type"
          Value: "app_cookie"
        - Key: "stickiness.app_cookie.cookie_name"
          Value: "`my-cookie-name`"
        - Key: "stickiness.app_cookie.duration_seconds"
          Value: "`300`"
```

###### Manual rebalancing

When scaling up, if the number of targets increase considerably, there is
potential for unequal distribution of load due to stickiness. In this scenario,
you can rebalance the load on your targets using the following two
options:

- Set an expiry on the cookie generated by the application that is prior to
  the current date and time. This prevents clients from sending the cookie
  to the Application Load Balancer, which will restart the process of establishing stickiness.
- Set a short duration on the load balancer's application-based
  stickiness configuration; for example, 1 second. This forces the Application Load Balancer
  to reestablish stickiness even if the cookie set by the target is not
  expired.
