# Update the IPAM IP address pools for your Application Load Balancer

IPAM IP address pools must first be created within IPAM before they can be
used by your Application Load Balancer. For more information, see
[Bring your IP addresses to IPAM](../../../vpc/latest/ipam/tutorials-byoip-ipam.md "../../../vpc/latest/ipam/tutorials-byoip-ipam.md").

Console

###### To update the IPAM IP address pool

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. On the navigation pane, choose **Load Balancers**.
3. Select the load balancer.
4. On the **Network mapping** tab, choose **Edit IP pools**.
5. Under **IP pools**, select **Use IPAM pool for public IPv4 addresses**
   and choose an IPAM pool.
6. Choose **Save changes**.

AWS CLI

###### To update the IPAM IP address pool

Use the [modify-ip-pools](../../../cli/latest/reference/elbv2/modify-ip-pools.md "../../../cli/latest/reference/elbv2/modify-ip-pools.md") command.

```
aws elbv2 modify-ip-pools \
    --load-balancer-arn `load-balancer-arn` \
    --ipam-pools Ipv4IpamPoolId=`ipam-pool-1234567890abcdef0`
```

CloudFormation

###### To update the IPAM IP address pool

Update the [AWS::ElasticLoadBalancingV2::LoadBalancer](../../../AWSCloudFormation/latest/TemplateReference/aws-resource-elasticloadbalancingv2-loadbalancer.md "../../../AWSCloudFormation/latest/TemplateReference/aws-resource-elasticloadbalancingv2-loadbalancer.md") resource.

```
Resources:
  myLoadBalancer:
    Type: 'AWS::ElasticLoadBalancingV2::LoadBalancer'
    Properties:
      Name: my-alb
      Type: application
      Scheme: internet-facing
      IpAddressType: ipv4
      Subnets:
        - !Ref subnet-AZ1
        - !Ref subnet-AZ2
      SecurityGroups:
        - !Ref mySecurityGroup
      Ipv4IpamPoolId: !Ref myIPAMPool
```
