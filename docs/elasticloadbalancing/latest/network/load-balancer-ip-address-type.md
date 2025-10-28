# Update the IP address types for your Network Load Balancer

You can configure your Network Load Balancer so that clients can communicate with the Network Load Balancer
using IPv4 addresses only, or using both IPv4 and IPv6 addresses (dualstack). The Network Load Balancer
communicates with targets based on the IP address type of the target group. For
more information, see [IP address type](network-load-balancers.md#ip-address-type "network-load-balancers.md#ip-address-type").

###### Dualstack requirements

- You can set the IP address type when you create the Network Load Balancer and update
  it at any time.
- The virtual private cloud (VPC) and subnets that you specify for the Network Load Balancer
  must have associated IPv6 CIDR blocks. For more information, see [IPv6
  addresses](../../../AWSEC2/latest/UserGuide/using-instance-addressing.md#ipv6-addressing "../../../AWSEC2/latest/UserGuide/using-instance-addressing.md#ipv6-addressing") in the _Amazon EC2 User Guide_.
- The route tables for the Network Load Balancer subnets must route IPv6 traffic.
- The network ACLs for the Network Load Balancer subnets must allow IPv6 traffic.

Console

###### To update the IP address type

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation pane, choose **Load Balancers**.
3. Select the check box for the Network Load Balancer.
4. Choose **Actions**, **Edit IP address
   type**.
5. For **IP address type**, choose **IPv4** to
   support IPv4 addresses only or **Dualstack** to support both
   IPv4 and IPv6 addresses.
6. Choose **Save changes**.

AWS CLI

###### To update the IP address type

Use the [set-ip-address-type](../../../cli/latest/reference/elbv2/set-ip-address-type.md "../../../cli/latest/reference/elbv2/set-ip-address-type.md") command.

```
aws elbv2 set-ip-address-type \
    --load-balancer-arn `load-balancer-arn` \
    --ip-address-type `dualstack`
```

CloudFormation

###### To update the IP address type

Update the [AWS::ElasticLoadBalancingV2::LoadBalancer](../../../AWSCloudFormation/latest/TemplateReference/aws-resource-elasticloadbalancingv2-loadbalancer.md "../../../AWSCloudFormation/latest/TemplateReference/aws-resource-elasticloadbalancingv2-loadbalancer.md")
resource.

```
Resources:
  myLoadBalancer:
    Type: 'AWS::ElasticLoadBalancingV2::LoadBalancer'
    Properties:
      Name: my-nlb
      Type: network
      Scheme: internal
      IpAddressType: `dualstack`
      Subnets:
        - !Ref subnet-AZ1
        - !Ref subnet-AZ2
      SecurityGroups:
        - !Ref mySecurityGroup
```
