

# Update the IPAM IP address pools for your Application Load Balancer
<a name="load-balancer-ip-pools"></a>

IPAM IP address pools must first be created within IPAM before they can be used by your Application Load Balancer. For more information, see [Bring your IP addresses to IPAM](https://docs.aws.amazon.com/vpc/latest/ipam/tutorials-byoip-ipam.html).

------
#### [ Console ]

**To update the IPAM IP address pool**

1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/).

1. On the navigation pane, choose **Load Balancers**.

1. Select the load balancer.

1. On the **Network mapping** tab, choose **Edit IP pools**.

1. Under **IP pools**, select **Use IPAM pool for public IPv4 addresses** and choose an IPAM pool.

1. Choose **Save changes**.

------
#### [ AWS CLI ]

**To update the IPAM IP address pool**  
Use the [modify-ip-pools](https://docs.aws.amazon.com/cli/latest/reference/elbv2/modify-ip-pools.html) command.

```
aws elbv2 modify-ip-pools \
    --load-balancer-arn {{load-balancer-arn}} \
    --ipam-pools Ipv4IpamPoolId={{ipam-pool-1234567890abcdef0}}
```

------
#### [ CloudFormation ]

**To update the IPAM IP address pool**  
Update the [AWS::ElasticLoadBalancingV2::LoadBalancer](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-elasticloadbalancingv2-loadbalancer.html) resource.

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

------