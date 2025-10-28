# Create a target group for your Network Load Balancer

You register targets for your Network Load Balancer with a target group. By default, the load balancer
sends requests to registered targets using the port and protocol that you specified for
the target group. You can override this port when you register each target with the
target group.

To route traffic to the targets in a target group, create a listener and specify the
target group in the default action for the listener. For more information, see [Listener rules](load-balancer-listeners.md#listener-rules "load-balancer-listeners.md#listener-rules"). You can specify the same
target group in multiple listeners, but these listeners must belong to the same Network Load Balancer.
To use a target group with a load balancer, you must verify that the target group is not
in use by a listener for any other load balancer.

You can add or remove targets from your target group at any time. For more
information, see [Register targets for your Network Load Balancer](target-group-register-targets.md "target-group-register-targets.md"). You can also modify the health
check settings for your target group. For more information, see [Update the health check settings of a Network Load Balancer
target group](modify-health-check-settings.md "modify-health-check-settings.md").

###### Requirements

- After you create a target group, you can't change its target type or its
  IP address type.
- All targets in a target group must have the same IP address type as the
  target group: IPv4 or IPv6.
- You must use an IPv6 target group with a dualstack load balancer.
- You can't use an IPv4 target group with a UDP listener for a
  `dualstack` load balancer.

Console

###### To create a target group

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation pane, choose **Target
   Groups**.
3. Choose **Create target group**.
4. For the **Basic configuration** pane, do the following:
   1. For **Choose a target type**, select
      **Instances** to register targets by instance
      ID, **IP addresses** to register targets by IP
      address, or **Application Load Balancer** to register an Application Load Balancer as a
      target.
   2. For **Target group name**, enter a name for the
      target group. This name must be unique per Region per account, can
      have a maximum of 32 characters, must contain only alphanumeric
      characters or hyphens, and must not begin or end with a
      hyphen.
   3. For **Protocol**, choose a protocol as
      follows:
      - If the listener protocol is TCP, choose
        **TCP** or
        **TCP_UDP**.
      - If the listener protocol is TLS, choose
        **TCP** or
        **TLS**.
      - If the listener protocol is UDP, choose
        **UDP** or
        **TCP_UDP**.
      - If the listener protocol is TCP_UDP, choose
        **TCP_UDP**.
      - If the target type is **Application Load Balancer**, the protocol
        must be TCP.

   4. For **Port**, modify the default value as needed.

   If the target type is **Application Load Balancer**, the port must match
   the listener port of the Application Load Balancer. 5. For **IP address type**, choose **IPv4**
   or **IPv6**. This option is available only if the target
   type is **Instances** or **IP addresses**. 6. For **VPC**, select the virtual private cloud
   (VPC) with the targets to register.

5. For the **Health checks** pane, modify the default
   settings as needed. For **Advanced health check settings**,
   choose the health check port, count, timeout, interval, and specify success
   codes. If health checks consecutively exceed the **Unhealthy
   threshold** count, the load balancer takes the target
   out of service. If health checks consecutively exceed the
   **Healthy threshold** count, the load balancer
   puts the target back in service. For more information, see .
6. (Optional) To add a tag, expand **Tags**, choose
   **Add tag**, and enter a tag key and a tag value.
7. Choose **Next**.
8. (Optional) Register targets. The target type of the target group determines
   the information that you provide. If you aren't ready to register targets now,
   you can register them later.
   - **Instances** – Select the EC2 instances, enter
     the ports, and choose **Include as pending
     below**.
   - **IP addresses** – Choose the VPC that contains
     the IP addresses or **Other private IP addresses**,
     enter the IP addresses and ports, and choose **Include as
     pending below**.
   - **Application Load Balancer** – Select the Application Load Balancer. For more
     information, see [Use Application Load Balancers as targets](application-load-balancer-target.md "application-load-balancer-target.md").

9. Choose **Create target group**.

AWS CLI

###### To create a target group

Use the [create-target-group](../../../cli/latest/reference/elbv2/create-target-group.md "../../../cli/latest/reference/elbv2/create-target-group.md") command. The following example
creates a target group with the TCP protocol, targets registered
by IP address, one tag, and default health check settings.

```
aws elbv2 create-target-group \
    --name `my-target-group` \
    --protocol TCP \
    --port 80 \
    --target-type `ip` \
    --vpc-id `vpc-1234567890abcdef0` \
    --tags Key=`department`,Value=`123`
```

###### To register targets

Use the [register-targets](../../../cli/latest/reference/elbv2/register-targets.md "../../../cli/latest/reference/elbv2/register-targets.md") command to register targets
with the target group. For examples, see
[Register targets](target-group-register-targets.md#register-targets "target-group-register-targets.md#register-targets").

CloudFormation

###### To create a target group

Define a resource of type [AWS::ElasticLoadBalancingV2::TargetGroup](../../../AWSCloudFormation/latest/TemplateReference/aws-resource-elasticloadbalancingv2-targetgroup.md "../../../AWSCloudFormation/latest/TemplateReference/aws-resource-elasticloadbalancingv2-targetgroup.md"). The
following example creates a target group with the TCP protocol,
targets registered by IP address, one tag, default health
check settings, and two registered targets.

```
Resources:
  myTargetGroup:
    Type: 'AWS::ElasticLoadBalancingV2::TargetGroup'
    Properties:
      Name: `my-target-group`
      Protocol: TCP
      Port: 80
      TargetType: `ip`
      VpcId: !Ref myVPC
      Tags:
        - Key: '`department`'
          Value: '`123`'
      Targets:
        - Id: 10.0.50.10
          Port: 80
        - Id: 10.0.50.20
          Port: 80
```
