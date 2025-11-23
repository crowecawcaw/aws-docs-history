# Create a target group for your Application Load Balancer

You register your targets with a target group. By default, the load balancer sends
requests to registered targets using the port and protocol that you specified for the
target group. You can override this port when you register each target with the target
group.

After you create a target group, you can add tags.

To route traffic to the targets in a target group, specify the target group in an
action when you create a listener or create a rule for your listener. For more
information, see [Listener rules for your Application Load Balancer](listener-rules.md "listener-rules.md"). You
can specify the same target group in multiple listeners, but these listeners must belong
to the same Application Load Balancer. To use a target group with a load balancer, you must verify that the
target group is not in use by a listener for any other load balancer.

You can add or remove targets from your target group at any time. For more
information, see [Register targets with your Application Load Balancer target group](target-group-register-targets.md "target-group-register-targets.md"). You can also modify the health
check settings for your target group. For more information, see [Update the health check settings of an Application Load Balancer
target group](modify-health-check-settings.md "modify-health-check-settings.md").

Console

###### To create a target group

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. On the navigation pane, under **Load Balancing**,
   choose **Target Groups**.
3. Choose **Create target group**.
4. For **Choose a target type**, select
   **Instances** to register targets by instance
   ID, **IP addresses** to register targets by IP
   address, or **Lambda function** to register a
   Lambda function as a target.
5. For **Target group name**, type a name for the
   target group. This name must be unique per region per account, can
   have a maximum of 32 characters, must contain only alphanumeric
   characters or hyphens, and must not begin or end with a
   hyphen.
6. (Optional) For **Protocol** and
   **Port**, modify the default values as
   needed.
7. If the target type is **Instances** or **IP addresses**, choose
   **IPv4** or **IPv6** as the
   **IP address type**, otherwise skip to the next
   step.

Note that only targets that have the selected IP address type can
be included in this target group. The IP address type can't be
changed after the target group is created. 8. For **VPC**, select a virtual private cloud
(VPC). Note that for **IP addresses** target types,
the VPCs available for selection are those that support the
**IP address type** that you chose in the
previous step. 9. (Optional) For **Protocol version**, modify the
default value as needed. For more information, see
[Protocol version](load-balancer-target-groups.md#target-group-protocol-version "load-balancer-target-groups.md#target-group-protocol-version"). 10. (Optional) In the **Health checks** section,
modify the default settings as needed. For more information, see
[Health check settings](target-group-health-checks.md#health-check-settings "target-group-health-checks.md#health-check-settings"). 11. If the target type is **Lambda function**, you
can enable health checks by selecting **Enable** in
the **Health checks** section. 12. (Optional) To enable **Target optimizer** on the
target group, specify a target control port. The port cannot be modified
after target group creation. Target optimizer works with the help of an agent
that you install on targets. For more information, see
[Target Optimizer](target-group-register-targets.md#register-targets-target-optimizer "target-group-register-targets.md#register-targets-target-optimizer"). 13. (Optional) Add one or more tags as follows:

    1. Expand the **Tags** section.
    2. Choose **Add tag**.
    3. Enter the tag key and the tag value.

14. Choose **Next**.
15. (Optional) Add one or more targets as follows:
    - If the target type is **Instances**,
      select one or more instances, enter one or more ports, and
      then choose **Include as pending
      below**.

    **Note:** The instances must have an assigned
    primary IPv6 address to be registered with a IPv6 target group.
    - If the target type is **IP addresses**,
      do the following:
      1. Select a network **VPC** from the
         list, or choose **Other private IP
         addresses**.
      2. Enter the IP address manually, or find the IP
         address using instance details. You can enter up to
         five IP addresses at a time.
      3. Enter the ports for routing traffic to the
         specified IP addresses.
      4. Choose **Include as pending
         below**.

    - If the target type is a **Lambda
      function**, specify a single Lambda function or
      omit this step and specify a Lambda function later.

16. Choose **Create target group**.

AWS CLI

###### To create a target group

Use the [create-target-group](../../../cli/latest/reference/elbv2/create-target-group.md "../../../cli/latest/reference/elbv2/create-target-group.md") command. The following example
creates a target group with the HTTP protocol, targets registered
by IP address, one tag, and default health check settings.

```
aws elbv2 create-target-group \
    --name `my-target-group` \
    --protocol HTTP \
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
following example creates a target group with the HTTP protocol,
targets registered by IP address, one tag, default health
check settings, and two registered targets.

```
Resources:
  myTargetGroup:
    Type: 'AWS::ElasticLoadBalancingV2::TargetGroup'
    Properties:
      Name: `my-target-group`
      Protocol: HTTP
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
