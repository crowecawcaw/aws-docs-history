# Update the Availability Zones for your Network Load Balancer

You can enable or disable the Availability Zones for your Network Load Balancer at any time. When you
enable an Availability Zone, you must specify one subnet from that Availability Zone.
After you enable an Availability Zone, the load balancer starts routing requests to the
registered targets in that Availability Zone. Your load balancer is most effective if
you ensure that each enabled Availability Zone has at least one registered target.
Enabling multiple Availability Zones helps improve the fault tolerance of your applications.

Elastic Load Balancing creates a Network Load Balancer node in the Availability Zone you choose, and a network interface
for the selected subnet in that Availability Zone. Each Network Load Balancer node in the Availability
Zone uses the network interface to get an IPv4 address. You can view these network
interfaces, but they can't be modified.

###### Considerations

- For internet-facing Network Load Balancers, the subnets that you specify must have at
  least 8 available IP addresses. For internal Network Load Balancers, this is only
  required if you let AWS select a private IPv4 address from the subnet.
- You can't specify a subnet in a constrained Availability Zone.
  However, you can specify a subnet in a non-constrained Availability
  Zone and use cross-zone load balancing to distribute traffic to
  targets in the constrained Availability Zone.
- You can't specify a subnet in a Local Zone.
- You can't remove a subnet if the Network Load Balancer has active Amazon VPC
  endpoint associations.
- When adding back a previously removed subnet, a new network
  interface is created with a different ID.
- Subnet changes within the same Availability Zone must be
  independent actions. You first complete removing the existing
  subnet, then you can add the new subnet.
- Subnet removal can take up to 3 minutes to complete.
  When creating an internet-facing Network Load Balancer, you can choose to specify an Elastic IP address
  for each Availability Zone. Elastic IP addresses provide your Network Load Balancer with static IP addresses.
  If you choose not to specify an Elastic IP address, AWS will assign one Elastic IP address
  for each Availability Zone.

When creating an internal Network Load Balancer, you can choose to specify a private IP address from each
subnet. Private IP addresses provide your Network Load Balancer with static IP addresses. If you choose not
to specify a private IP address, AWS assigns one for you.

Before updating the Availability Zones for your Network Load Balancer, we recommend you evaluate for any
potential impact on existing connections, traffic flows, or production workloads.

###### Updating an Availability Zone can be disruptive

- When a subnet is removed, its associated Elastic Network
  Interface (ENI) is deleted. This causes all active connections
  in the Availability Zone to be terminated.
- After a subnet is removed, all targets within the Availability
  Zone it was associated with are marked as `unused`.
  This results in those targets being removed from the available
  target pool, and all active connections to those targets being
  terminated. This includes any connections originating from
  other Availability Zones when utilizing cross-zone load
  balancing.
- Network Load Balancers have a 60 second Time To Live (TTL) for their Fully
  Qualified Domain Name (FQDN). When an Availability Zone that
  contains active targets is removed any existing client
  connections may experience timeouts until DNS resolution
  occurs again, and traffic is shifted to any remaining
  Availability Zones.

Console

###### To modify the Availability Zones

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

###### To modify the Availability Zones

Use the [set-subnets](../../../cli/latest/reference/elbv2/set-subnets.md "../../../cli/latest/reference/elbv2/set-subnets.md")
command.

```
aws elbv2 set-subnets \
    --load-balancer-arn `load-balancer-arn` \
    --subnets subnet-1234567890abcdef0 subnet-0abcdef1234567890
```

CloudFormation

###### To modify the Availability Zones

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
      Subnets:
        - !Ref subnet-AZ1
        - !Ref `new-subnet-AZ2`
      SecurityGroups:
        - !Ref mySecurityGroup
```
