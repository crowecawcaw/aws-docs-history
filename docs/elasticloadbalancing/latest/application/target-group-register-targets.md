# Register targets with your Application Load Balancer target group

You register your targets with a target group. When you create a target group, you
specify its target type, which determines how you register its targets. For example, you
can register instance IDs, IP addresses, or Lambda functions. For more information, see
[Target groups for your Application Load Balancers](load-balancer-target-groups.md "load-balancer-target-groups.md").

If demand on your currently registered targets increases, you can register additional
targets in order to handle the demand. When your target is ready to handle requests,
register it with your target group. The load balancer starts routing requests to the
target as soon as the registration process completes and the target passes the initial
health checks.

If demand on your registered targets decreases, or you need to service a target, you
can deregister it from your target group. The load balancer stops routing requests to a
target as soon as you deregister it. When the target is ready to receive requests, you
can register it with the target group again.

When you deregister a target, the load balancer waits until in-flight requests have
completed. This is known as _connection draining_. The status of a
target is `draining` while connection draining is in progress.

When you deregister a target that was registered by IP address, you must wait for the
deregistration delay to complete before you can register the same IP address
again.

If you are registering targets by instance ID, you can use your load balancer with an
Auto Scaling group. After you attach a target group to an Auto Scaling group and the group scales out,
the instances launched by the Auto Scaling group are automatically registered with the target
group. If you detach the target group from the Auto Scaling group, the instances are
automatically deregistered from the target group. For more information, see [Attaching a load balancer to your
Auto Scaling group](../../../autoscaling/ec2/userguide/attach-load-balancer-asg.md "../../../autoscaling/ec2/userguide/attach-load-balancer-asg.md") in the _Amazon EC2 Auto Scaling User Guide_.

When shutting down an application on a target you must first deregister the target
from its target group and allow time for existing connections to drain. You can monitor
deregistration status using the describe-target-health CLI command, or by refreshing
the target group view in the AWS Management Console. After confirming the target is deregistered
you can proceed with stopping or terminating the application. This sequence prevents
users from experiencing 5XX errors when applications are terminated while still
processing traffic.

## Target security groups

When you register EC2 instances as targets, you must ensure that the security
groups for your instances allow the load balancer to communicate with your instances
on both the listener port and the health check port.

Recommended rules| **Inbound** |
| **Source** | **Port Range** | **Comment** |
| `load balancer security group` | `instance listener` | Allow traffic from the load balancer on the instance listener<br>port |
| `load balancer security group` | `health check` | Allow traffic from the load balancer on the health check<br>port |

We also recommend that you allow inbound ICMP traffic to support Path MTU
Discovery. For more information, see [Path MTU
Discovery](../../../AWSEC2/latest/UserGuide/network_mtu.md#path_mtu_discovery "../../../AWSEC2/latest/UserGuide/network_mtu.md#path_mtu_discovery") in the _Amazon EC2 User Guide_.

## Target Optimizer

Target optimizer lets you enforce strict concurrency on targets in a target group.
It works with the help of an agent that you install and configure on targets. The agent
serves as an inline proxy between the load balancer and your application. You configure
the agent to enforce a maximum number of concurrent requests that the load balancer
can send to the target. The agent tracks the number of requests the target is processing.
When the number falls below the configured maximum value, the agent sends a signal to
the load balancer letting it know that the target is ready to process another request.

To enable target optimizer, you specify a target control port when creating the target group.
The load balancer establishes control channels with agents on this port for management traffic.
This port is different from the port on which the load balancer sends application traffic.
Targets registered with the target group must have the agent running on them.

**Note: Target optimizer can only be enabled during target group creation. Target control
port cannot be modified after creation.**

The agent is available as a Docker image at:
`public.ecr.aws/aws-elb/target-optimizer/target-control-agent:latest`.
You configure the following environment variables when running the agent container:

`TARGET_CONTROL_DATA_ADDRESS`

The agent receives application traffic from the load balancer on this socket (IP:port).
The port in this socket is the application traffic port you configure for the target group.
By default, the agent can accept both plaintext and TLS connections.

`TARGET_CONTROL_CONTROL_ADDRESS`

The agent receives management traffic from the load balancer on this socket (IP:port). The port
in the socket is the target control port you configure for the target group.

`TARGET_CONTROL_DESTINATION_ADDRESS`

The agent proxies application traffic to this socket (IP:port). Your application should
be listening on this socket.

(Optional) `TARGET_CONTROL_MAX_CONCURRENCY`

The maximum number of concurrent requests that the target will receive from the load balancer. It can
be between 0-1000. The default is 1.

(Optional) `TARGET_CONTROL_TLS_CERT_PATH`

The location of the TLS certificate that the agent provides to the load balancer during TLS handshake.
By default, the agent generates a self-signed certificate in-memory.

(Optional) `TARGET_CONTROL_TLS_KEY_PATH`

The location of the private key corresponding to the TLS certificate that the agent provides to the
load balancer during TLS handshake. By default, the agent generates a private key in-memory.

(Optional) `TARGET_CONTROL_TLS_SECURITY_POLICY`

The ELB security policy that you configure for the target group. The default is `ELBSecurityPolicy-2016-08`.

(Optional) `TARGET_CONTROL_PROTOCOL_VERSION`

The protocol through which the load balancer communicates with the agent. Possible values are `HTTP1`,
`HTTP2`, `GRPC`. The default is `HTTP1`.

(Optional) `RUST_LOG`

The log level of the agent process. The agent software is written in Rust. Possible values are `debug`,
`info`,and `error` . The default is `info`.

To modify the value for any environment variable, you have to restart the agent with the new value. You can monitor
target optimizer with the following metrics:
`TargetControlRequestCount`, `TargetControlRequestRejectCount`,
`TargetControlActiveChannelCount`, `TargetControlNewChannelCount`,
`TargetControlChannelErrorCount`, `TargetControlWorkQueueLength`,
`TargetControlProcessedBytes`. For more information, see
[Target optimizer metrics](load-balancer-cloudwatch-metrics.md#target-optimizer-metric-table "load-balancer-cloudwatch-metrics.md#target-optimizer-metric-table")
For troubleshooting information, see
[Troubleshooting target optimizer](load-balancer-troubleshooting.md#troubleshoot-target-optimizer "load-balancer-troubleshooting.md#troubleshoot-target-optimizer")

## Shared subnets

Participants can create an Application Load Balancer in a shared VPC. Participants can't register
a target that runs in a subnet that is not shared with them.

## Register targets

Each target group must have at least one registered target in each Availability Zone
that is enabled for the load balancer.

The target type of your target group determines how you register targets with that
target group. For more information, see [Target type](load-balancer-target-groups.md#target-type "load-balancer-target-groups.md#target-type").

###### Requirements and considerations

- An instance must be in the `running` state when you register
  it.
- A target instance must be in the virtual private cloud (VPC) that you specified
  for the target group.
- When registering targets by instance ID for a IPv6 target group, the targets
  must have an assigned primary IPv6 address. To learn more, see [IPv6 addresses](../../../AWSEC2/latest/UserGuide/using-instance-addressing.md#ipv6-addressing "../../../AWSEC2/latest/UserGuide/using-instance-addressing.md#ipv6-addressing") in the _Amazon EC2 User Guide_
- When registering targets by IP address for an IPv4 target group, the IP
  addresses that you register must be from one of the following CIDR blocks:
  - The subnets of the target group VPC
  - 10.0.0.0/8 (RFC 1918)
  - 100.64.0.0/10 (RFC 6598)
  - 172.16.0.0/12 (RFC 1918)
  - 192.168.0.0/16 (RFC 1918)

- When registering targets by IP address for an IPv6 target group, the IP
  addresses that you register must be within the VPC IPv6 CIDR block or
  within the IPv6 CIDR block of a peered VPC.
- You can't register the IP addresses of another Application Load Balancer in the same VPC.
  If the other Application Load Balancer is in a VPC that is peered to the load balancer VPC,
  you can register its IP addresses.

Console

###### To register targets

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. On the navigation pane, under **Load Balancing**,
   choose **Target Groups**.
3. Choose the name of the target group to open its details
   page.
4. Choose the **Targets** tab.
5. Choose **Register targets**.
6. If the target type of the target group is `instance`,
   select available instances, override the default port if needed,
   and then choose **Include as pending below**.
7. If the target type of the target group is `ip`, for
   each IP address, select the network, enter the IP addresses and
   ports, and choose **Include as pending below**.
8. If the target type of the target group is `lambda`,
   select the Lambda function or enter its ARN. For more information,
   see [Use Lambda functions as targets](lambda-functions.md "lambda-functions.md").
9. Choose **Register pending targets**.

AWS CLI

###### To register targets

Use the [register-targets](../../../cli/latest/reference/elbv2/register-targets.md "../../../cli/latest/reference/elbv2/register-targets.md") command. The following example
registers targets by instance ID. Because the port is not
specified, the load balancer uses the target group port.

```
aws elbv2 register-targets \
    --target-group-arn `target-group-arn` \
    --targets Id=`i-1234567890abcdef0` Id=`i-0abcdef1234567890`
```

The following example registers targets by IP address. Because
the port is not specified, the load balancer uses the target
group port.

```
aws elbv2 register-targets \
    --target-group-arn `target-group-arn` \
    --targets Id=`10.0.50.10` Id=`10.0.50.20`
```

The following example registers a Lambda function as a target.

```
aws elbv2 register-targets \
    --target-group-arn `target-group-arn` \
    --targets Id=`lambda-function-arn`
```

CloudFormation

###### To register targets

Update the [AWS::ElasticLoadBalancingV2::TargetGroup](../../../AWSCloudFormation/latest/TemplateReference/aws-resource-elasticloadbalancingv2-targetgroup.md "../../../AWSCloudFormation/latest/TemplateReference/aws-resource-elasticloadbalancingv2-targetgroup.md") resource
to include the new targets. The following example registers
two targets by instance ID.

```
Resources:
  myTargetGroup:
    Type: 'AWS::ElasticLoadBalancingV2::TargetGroup'
    Properties:
      Name: my-target-group
      Protocol: HTTP
      Port: 80
      TargetType: instance
      VpcId: !Ref myVPC
      Targets:
        - Id: !GetAtt Instance1.InstanceId
          Port: 80
        - Id: !GetAtt Instance2.InstanceId
          Port: 80
```

## Deregister targets

If demand on your application decreases, or if you need to service your targets, you
can deregister targets from your target groups. Deregistering a target removes it from
your target group, but does not affect the target otherwise.

Console

###### To deregister targets

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. On the navigation pane, under **Load Balancing**,
   choose **Target Groups**.
3. Choose the name of the target group to open its details
   page.
4. On the **Targets** tab, select
   the targets to remove.
5. Choose **Deregister**.
6. When prompted for confirmation, choose
   **Deregister**.

AWS CLI

###### To deregister targets

Use the [deregister-targets](../../../cli/latest/reference/elbv2/deregister-targets.md "../../../cli/latest/reference/elbv2/deregister-targets.md") command. The following example
deregisters two targets that were registered by instance ID.

```
aws elbv2 deregister-targets \
    --target-group-arn `target-group-arn` \
    --targets Id=`i-1234567890abcdef0` Id=`i-0abcdef1234567890`
```
