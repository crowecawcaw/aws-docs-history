# Update the security groups for your Network Load Balancer

You can associate a security group with your Network Load Balancer to control the traffic that is
allowed to reach and leave the Network Load Balancer. You specify the ports, protocols, and
sources to allow for inbound traffic and the ports, protocols, and destinations to allow
for outbound traffic. If you don't assign a security group to your Network Load Balancer, all
client traffic can reach the Network Load Balancer listeners and all traffic can leave the Network Load Balancer.

You can add a rule to the security groups associated with your targets that references the
security group associated with your Network Load Balancer. This allows clients to send traffic to your targets
through your Network Load Balancer, but prevents them from sending traffic directly to your targets.
Referencing the security group associated with your Network Load Balancer in the security groups associated
with your targets ensures that your targets accept traffic from your Network Load Balancer even if you
enable [client IP preservation](edit-target-group-attributes.md#client-ip-preservation "edit-target-group-attributes.md#client-ip-preservation") for your Network Load Balancer.

You are not charged for traffic that is blocked by inbound security group rules.

###### Contents

- [Considerations](#security-group-considerations "#security-group-considerations")
- [Example: Filter client traffic](#filter-client-traffic-recommended-rules "#filter-client-traffic-recommended-rules")
- [Example: Accept traffic only from the Network Load Balancer](#load-balancer-traffic-only-recommended-rules "#load-balancer-traffic-only-recommended-rules")
- [Update the associated security groups](#update-security-group "#update-security-group")
- [Update the security settings](#update-security-settings "#update-security-settings")
- [Monitor Network Load Balancer security groups](#monitor-load-balancer-security-groups "#monitor-load-balancer-security-groups")

## Considerations

- You can associate security groups with a Network Load Balancer when you create it. If you
  create a Network Load Balancer without associating any security groups, you can't associate
  them with the Network Load Balancer later on. We recommend that you associate a
  security group with your Network Load Balancer when you create it.
- After you create a Network Load Balancer with associated security groups, you can change
  the security groups associated with the Network Load Balancer at any time.
- Health checks are subject to outbound rules, but not inbound rules. You must
  ensure that outbound rules don't block health check traffic. Otherwise, the Network Load Balancer
  considers the targets unhealthy.
- You can control whether PrivateLink traffic is subject to inbound rules. If
  you enable inbound rules on PrivateLink traffic, the source of the traffic is
  the private IP address of the client, not the endpoint interface.

## Example: Filter client traffic

The following inbound rules in the security group associated with your Network Load Balancer allow
only traffic that comes from the specified address range. If this is an internal
Network Load Balancer, you can specify a VPC CIDR range as the source to allow only traffic
from a specific VPC. If this is an internet-facing Network Load Balancer that must accept
traffic from anywhere on the internet, you can specify 0.0.0.0/0 as the
source.

| Inbound    | Protocol                  | Source          | Port range                                                         | Comment |
| ---------- | ------------------------- | --------------- | ------------------------------------------------------------------ | ------- |
| `protocol` | `client IP address range` | `listener port` | Allows inbound traffic from the source CIDR on the listener port   |
| ICMP       | 0.0.0.0/0                 | All             | Allows inbound ICMP traffic to support MTU or Path MTU Discovery † |

† For more information, see [Path MTU Discovery](../../../AWSEC2/latest/UserGuide/network_mtu.md#path_mtu_discovery "../../../AWSEC2/latest/UserGuide/network_mtu.md#path_mtu_discovery") in the _Amazon EC2 User Guide_.

| Outbound | Protocol | Destination | Port range                  | Comment |
| -------- | -------- | ----------- | --------------------------- | ------- |
| All      | Anywhere | All         | Allows all outbound traffic |

## Example: Accept traffic only from the Network Load Balancer

Suppose that your Network Load Balancer has a security group sg-111112222233333. Use the following
rules in the security groups associated with your target instances to ensure that
they accept traffic only from the Network Load Balancer. You must ensure that the targets accept
traffic from the Network Load Balancer on both the target port and the health check port.
For more information, see [Target security groups](target-group-register-targets.md#target-security-groups "target-group-register-targets.md#target-security-groups").

| Inbound    | Protocol           | Source         | Port range                                                                     | Comment |
| ---------- | ------------------ | -------------- | ------------------------------------------------------------------------------ | ------- |
| `protocol` | sg-111112222233333 | `target port`  | Allows inbound traffic from the Network Load Balancer on the target port       |
| `protocol` | sg-111112222233333 | `health check` | Allows inbound traffic from the Network Load Balancer on the health check port |

| Outbound | Protocol | Destination | Port range                  | Comment |
| -------- | -------- | ----------- | --------------------------- | ------- |
| All      | Anywhere | Any         | Allows all outbound traffic |

## Update the associated security groups

If you associated at least one security group with a Network Load Balancer when you created
it, you can update the security groups for that Network Load Balancer at any time.

Console

###### To update the security groups

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. On the navigation pane, under **Load Balancing**, choose
   **Load Balancers**.
3. Select the Network Load Balancer.
4. On the **Security** tab, choose
   **Edit**.
5. To associate a security group with your Network Load Balancer, select it. To
   remove a security group from your Network Load Balancer, clear it.
6. Choose **Save changes**.

AWS CLI

###### To update the security groups

Use the [set-security-groups](../../../cli/latest/reference/elbv2/set-security-groups.md "../../../cli/latest/reference/elbv2/set-security-groups.md") command.

```
aws elbv2 set-security-groups \
    --load-balancer-arn `load-balancer-arn` \
    --security-groups `sg-1234567890abcdef0` `sg-0abcdef0123456789`
```

CloudFormation

###### To update the security groups

Update the [AWS::ElasticLoadBalancingV2::LoadBalancer](../../../AWSCloudFormation/latest/TemplateReference/aws-resource-elasticloadbalancingv2-loadbalancer.md "../../../AWSCloudFormation/latest/TemplateReference/aws-resource-elasticloadbalancingv2-loadbalancer.md") resource.

```
Resources:
  myLoadBalancer:
    Type: 'AWS::ElasticLoadBalancingV2::LoadBalancer'
    Properties:
      Name: my-nlb
      Type: network
      Scheme: internal
      Subnets:
        - !Ref subnet-AZ1
        - !Ref subnet-AZ2
      SecurityGroups:
        - !Ref mySecurityGroup
        - !Ref `myNewSecurityGroup`
```

## Update the security settings

By default, we apply the inbound security group rules to all traffic sent to the
Network Load Balancer. However, you might not want to apply these rules to traffic sent to
the Network Load Balancer through AWS PrivateLink, which can originate from overlapping IP
addresses. In this case, you can configure the Network Load Balancer so that we do not apply
the inbound rules for traffic sent to the Network Load Balancer through AWS PrivateLink.

Console

###### To update the security settings

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. On the navigation pane, under **Load Balancing**, choose
   **Load Balancers**.
3. Select the Network Load Balancer.
4. On the **Security** tab, choose
   **Edit**.
5. Under **Security setting**, clear **Enforce
   inbound rules on PrivateLink traffic**.
6. Choose **Save changes**.

AWS CLI

###### To update the security settings

Use the [set-security-groups](../../../cli/latest/reference/elbv2/set-security-groups.md "../../../cli/latest/reference/elbv2/set-security-groups.md") command.

```
aws elbv2 set-security-groups \
    --load-balancer-arn `load-balancer-arn` \
    --enforce-security-group-inbound-rules-on-private-link-traffic `off`
```

CloudFormation

###### To update the security settings

Update the [AWS::ElasticLoadBalancingV2::LoadBalancer](../../../AWSCloudFormation/latest/TemplateReference/aws-resource-elasticloadbalancingv2-loadbalancer.md "../../../AWSCloudFormation/latest/TemplateReference/aws-resource-elasticloadbalancingv2-loadbalancer.md") resource.

```
Resources:
  myLoadBalancer:
    Type: 'AWS::ElasticLoadBalancingV2::LoadBalancer'
    Properties:
      Name: my-nlb
      Type: network
      Scheme: internal
      EnforceSecurityGroupInboundRulesOnPrivateLinkTraffic: `off`
      Subnets:
        - !Ref subnet-AZ1
        - !Ref subnet-AZ2
      SecurityGroups:
        - !Ref mySecurityGroup
```

## Monitor Network Load Balancer security groups

Use the `SecurityGroupBlockedFlowCount_Inbound` and
`SecurityGroupBlockedFlowCount_Outbound` CloudWatch metrics to
monitor the count of flows that are blocked by the Network Load Balancer security
groups. Blocked traffic is not reflected in other metrics. For more information,
see [CloudWatch metrics for your Network Load Balancer](load-balancer-cloudwatch-metrics.md "load-balancer-cloudwatch-metrics.md").

Use VPC flow logs to monitor traffic that is accepted or rejected by the Network Load Balancer security groups. For more information, see [VPC flow logs](../../../vpc/latest/userguide/flow-logs.md "../../../vpc/latest/userguide/flow-logs.md") in the
_Amazon VPC User Guide_.
