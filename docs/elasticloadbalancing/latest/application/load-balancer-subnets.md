# Update the Availability Zones for your Application Load Balancer

You can enable or disable the Availability Zones for your load balancer at any time.
After you enable an Availability Zone, the load balancer starts routing requests to the
registered targets in that Availability Zone. Application Load Balancers have cross-zone load balancing on
by default, resulting in requests being routed to all registered targets across all
Availability Zones. When cross-zone load balancing is off, the load balancer only
routes request to targets in the same Availability Zone. For more information, see
[Cross-zone load balancing](application-load-balancers.md#cross-zone-load-balancing "application-load-balancers.md#cross-zone-load-balancing").
Your load balancer is most effective if you ensure that each enabled Availability Zone
has at least one registered target.

After you disable an Availability Zone, the targets in that Availability Zone remain
registered with the load balancer, but the load balancer will not route requests to
them.

For more information, see [Subnets for your load balancer](application-load-balancers.md#subnets-load-balancer "application-load-balancers.md#subnets-load-balancer").

Console

###### To update Availability Zones

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. On the navigation pane, choose **Load Balancers**.
3. Select the load balancer.
4. On the **Network mapping** tab, choose **Edit subnets**.
5. To enable an Availability Zone, select its check box and select one subnet. If
   there is only one available subnet, it is selected for you.
6. To change the subnet for an enabled Availability Zone, choose one of the other
   subnets from the list.
7. To disable an Availability Zone, clear its check box.
8. Choose **Save changes**.

AWS CLI

###### To update Availability Zones

Use the [set-subnets](../../../cli/latest/reference/elbv2/set-subnets.md "../../../cli/latest/reference/elbv2/set-subnets.md")
command.

```
aws elbv2 set-subnets \
    --load-balancer-arn `load-balancer-arn` \
    --subnets `subnet-8360a9e7EXAMPLE` `subnet-b7d581c0EXAMPLE`
```

CloudFormation

###### To update Availability Zones

Update the [AWS::ElasticLoadBalancingV2::LoadBalancer](../../../AWSCloudFormation/latest/TemplateReference/aws-resource-elasticloadbalancingv2-loadbalancer.md "../../../AWSCloudFormation/latest/TemplateReference/aws-resource-elasticloadbalancingv2-loadbalancer.md")
resource.

```
Resources:
  myLoadBalancer:
    Type: 'AWS::ElasticLoadBalancingV2::LoadBalancer'
    Properties:
      Name: my-alb
      Type: application
      Scheme: internal
      IpAddressType: dualstack
      Subnets:
        - !Ref subnet-AZ1
        - !Ref `new-subnet-AZ2`
      SecurityGroups:
        - !Ref mySecurityGroup
```
