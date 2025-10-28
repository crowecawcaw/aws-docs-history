# Update the target group health settings for your Network Load Balancer

By default, Network Load Balancers monitor the health of targets and route requests to healthy targets.
However, if the load balancer doesn't have enough healthy targets, it automatically sends
traffic to all registered targets (fail open). You can modify the target group health
settings for your target group to define the thresholds for DNS failover and routing
failover. For more information, see [Target group health](load-balancer-target-groups.md#target-group-health "load-balancer-target-groups.md#target-group-health").

Console

###### To update the target group health settings

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation pane, under **Load Balancing**,
   choose **Target Groups**.
3. Choose the name of the target group to open its details
   page.
4. On the **Attributes** tab, choose
   **Edit**.
5. Expand **Target group health requirements**.
6. For **Configuration type**, we recommend that
   you choose **Unified configuration**, which sets
   the same threshold for both DNS failover and routing failover.
7. For **Healthy state requirements**, do one of
   the following:
   - Choose **Minimum healthy target count**, and then
     enter a number from 1 to the maximum number of targets for your
     target group.
   - Choose **Minimum healthy target percentage**,
     and then enter a number from 1 to 100.

8. The informational text indicates whether cross-zone load balancing
   is enabled for the target group. If cross-zone load balancing is disabled,
   you can enable it to ensure that you have enough capacity. Under
   **Target selection configuration**, update
   **Cross-zone load balancing**.

The following text indicates that cross-zone load balancing is disabled:

```
Healthy state requirements apply to each zone independently.
```

The following text indicates that cross-zone load balancing is enabled:

```
Healthy state requirements apply to the total targets across all applicable zones.
```

9. Choose **Save changes**.

AWS CLI

###### To update the target group health settings

Use the [modify-target-group-attributes](../../../cli/latest/reference/elbv2/modify-target-group-attributes.md "../../../cli/latest/reference/elbv2/modify-target-group-attributes.md") command. The following example
sets the healthy threshold for both unhealthy state actions to 50%.

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
      Protocol: TCP
      Port: 80
      TargetType: ip
      VpcId: !Ref myVPC
      TargetGroupAttributes:
        - Key: "target_group_health.dns_failover.minimum_healthy_targets.percentage"
          Value: "`50`"
        - Key: "target_group_health.unhealthy_state_routing.minimum_healthy_targets.percentage"
          Value: "`50`"
```
