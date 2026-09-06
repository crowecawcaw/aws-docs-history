

# Update the IP address types for your Network Load Balancer
<a name="load-balancer-ip-address-type"></a>

You can configure your Network Load Balancer so that clients can communicate with the Network Load Balancer using IPv4 addresses only, or using both IPv4 and IPv6 addresses (dualstack). The Network Load Balancer communicates with targets based on the IP address type of the target group. For more information, see [IP address type](network-load-balancers.md#ip-address-type).

**Dualstack requirements**
+ You can set the IP address type when you create the Network Load Balancer and update it at any time.
+ The virtual private cloud (VPC) and subnets that you specify for the Network Load Balancer must have associated IPv6 CIDR blocks. For more information, see [IPv6 addresses](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-instance-addressing.html#ipv6-addressing) in the *Amazon EC2 User Guide*.
+ The route tables for the Network Load Balancer subnets must route IPv6 traffic.
+ The network ACLs for the Network Load Balancer subnets must allow IPv6 traffic.
+ There are no QUIC or TCP\_QUIC listeners attached to the Network Load Balancer.

------
#### [ Console ]

**To update the IP address type**

1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/).

1. In the navigation pane, choose **Load Balancers**.

1. Select the check box for the Network Load Balancer.

1. Choose **Actions**, **Edit IP address type**.

1. For **IP address type**, choose **IPv4** to support IPv4 addresses only or **Dualstack** to support both IPv4 and IPv6 addresses.

1. Choose **Save changes**.

------
#### [ AWS CLI ]

**To update the IP address type**  
Use the [set-ip-address-type](https://docs.aws.amazon.com/cli/latest/reference/elbv2/set-ip-address-type.html) command.

```
aws elbv2 set-ip-address-type \
    --load-balancer-arn {{load-balancer-arn}} \
    --ip-address-type {{dualstack}}
```

------
#### [ CloudFormation ]

**To update the IP address type**  
Update the [AWS::ElasticLoadBalancingV2::LoadBalancer](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-elasticloadbalancingv2-loadbalancer.html) resource.

```
Resources:
  myLoadBalancer:
    Type: 'AWS::ElasticLoadBalancingV2::LoadBalancer'
    Properties:
      Name: my-nlb
      Type: network
      Scheme: internal
      IpAddressType: {{dualstack}}
      Subnets: 
        - !Ref subnet-AZ1
        - !Ref subnet-AZ2
      SecurityGroups: 
        - !Ref mySecurityGroup
```

------