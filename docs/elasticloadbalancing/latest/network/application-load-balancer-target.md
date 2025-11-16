# Use an Application Load Balancer as a target of a Network Load Balancer

You can create a target group with a single Application Load Balancer as the target, and configure your
Network Load Balancer to forward traffic to it. In this scenario, the Application Load Balancer takes over the load
balancing decision as soon as traffic reaches it. This configuration combines the
features of both load balancers and offers the following advantages:

- You can use the layer 7 request-based routing feature of the Application Load Balancer in
  combination with features that the Network Load Balancer supports, such as endpoint services
  (AWS PrivateLink) and static IP addresses.
- You can use this configuration for applications that need a single endpoint
  for multi-protocols, such as media services using HTTP for signaling and RTP
  to stream content.
  You can use this feature with an internal or internet-facing Application Load Balancer as the target of an
  internal or internet-facing Network Load Balancer.

###### Considerations

- You can only register one Application Load Balancer per target group.
- To associate an Application Load Balancer as a target of a Network Load Balancer, the load balancers must be in the same VPC
  within the same account.
- You can associate an Application Load Balancer as a target of up to two Network Load Balancers. To do this,
  register the Application Load Balancer with a separate target group for each Network Load Balancer.
- Each Application Load Balancer that you register with a Network Load Balancer decreases the maximum number of targets
  per Availability Zone per Network Load Balancer by 50. You can disable cross-zone load
  balancing in both load balancers to minimize latency and avoid Regional data transfer
  charges. For more information, see [Quotas for your Network Load Balancers](load-balancer-limits.md "load-balancer-limits.md").
- When the target group type is `alb`, you can't modify the target
  group attributes. These attributes always use their default values.
- After you register an Application Load Balancer as a target, you can't delete the Application Load Balancer
  until you deregister it from all target groups.
- The communication between a Network Load Balancer and an Application Load Balancer always uses IPv4.

###### Tasks

- [Prerequisite](#application-load-balancer-target-prerequisite "#application-load-balancer-target-prerequisite")
- [Step 1: Create a target group of type alb](#register-application-load-balancer-target "#register-application-load-balancer-target")
- [Step 2: Create a Network Load Balancer and configure routing](#configure-application-load-balancer-target "#configure-application-load-balancer-target")
- [Step 3: (Optional) Create a VPC endpoint service](#enable-privatelink "#enable-privatelink")

## Prerequisite

If you don't already have an Application Load Balancer to use as a target, create the load balancer,
its listeners, and its target groups. For more information, see
[Create an Application Load Balancer](../application/create-application-load-balancer.md "../application/create-application-load-balancer.md")
in the _User Guide for Application Load Balancers_.

## Step 1: Create a target group of type alb

Create a target group of type `alb`. You can register your Application Load Balancer as a
target when you create the target group or later on.

Console

###### To create a target group for an Application Load Balancer as a target

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. On the navigation pane, under **Load Balancing**, choose
   **Target Groups**.
3. Choose **Create target group**.
4. In the **Basic configuration** pane, for
   **Choose a target type**, choose
   **Application Load Balancer**.
5. For **Target group name**, enter a name for the
   target group.
6. For **Protocol**, only TCP is allowed. Select the
   **Port** for your target group. The port for this target
   group must match the listener port of the Application Load Balancer. If you choose a different
   port for this target group, you can update the listener port on the Application Load Balancer
   to match it.
7. For **VPC**, select the virtual private cloud (VPC)
   for the target group. This must be the same VPC used by the Application Load Balancer.
8. For **Health checks**, choose HTTP or HTTPS as the
   **Health check protocol**. Health checks are sent to
   the Application Load Balancer and forwarded to its targets using the specified port, protocol,
   and ping path. Ensure that your Application Load Balancer can receive these health checks by
   having a listener with a port and protocol that matches the health check
   port and protocol.
9. (Optional) Expand **Tags**. For each tag, choose
   **Add new tag** and enter a tag key and a tag value.
10. Choose **Next**.
11. If you are ready to register the Application Load Balancer, choose **Register now**,
    override the default port if needed, and select the Application Load Balancer. The Application Load Balancer must
    have a listener on the same port as the target group. You can add or edit
    a listener on this load balancer to match the target group port, or
    return to the previous step and change the port for the target group.

If you are not ready to register the Application Load Balancer as a target, choose
**Register later** and register the target later on.
For more information, see [Register targets](target-group-register-targets.md#register-targets "target-group-register-targets.md#register-targets"). 12. Choose **Create target group**.

AWS CLI

###### To create a target group of type alb

Use the [create-target-group](../../../cli/latest/reference/elbv2/create-target-group.md "../../../cli/latest/reference/elbv2/create-target-group.md") command. The protocol must be
TCP and the port must match the listener port of the Application Load Balancer.

```
aws elbv2 create-target-group \
    --name `my-target-group` \
    --protocol TCP \
    --port 80 \
    --target-type alb \
    --vpc-id `vpc-1234567890abcdef0` \
    --tags Key=`department`,Value=`123`
```

CloudFormation

###### To create a target group of type alb

Define a resource of type [AWS::ElasticLoadBalancingV2::TargetGroup](../../../AWSCloudFormation/latest/TemplateReference/aws-resource-elasticloadbalancingv2-targetgroup.md "../../../AWSCloudFormation/latest/TemplateReference/aws-resource-elasticloadbalancingv2-targetgroup.md"). The
protocol must be TCP and the port must match the listener
port of the Application Load Balancer.

```
Resources:
  myTargetGroup:
    Type: 'AWS::ElasticLoadBalancingV2::TargetGroup'
    Properties:
      Name: `my-target-group`
      Protocol: TCP
      Port: 80
      TargetType: alb
      VpcId: !Ref myVPC
      Tags:
        - Key: '`department`'
          Value: '`123`'
      Targets:
        - Id: !Ref myApplicationLoadBalancer
          Port: 80
```

## Step 2: Create a Network Load Balancer and configure routing

When you create the Network Load Balancer, you can configure the default action to forward
traffic to the Application Load Balancer.

Console

###### To create the Network Load Balancer

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. On the navigation pane, under **Load Balancing**,
   choose **Load Balancers**.
3. Choose **Create load balancer**.
4. Under **Network Load Balancer**, choose **Create**.
5. **Basic configuration**
   1. For **Load balancer name**, enter a name for your Network Load Balancer.
   2. For **Scheme**, choose **Internet-facing**
      or **Internal**. An internet-facing Network Load Balancer routes requests
      from clients to targets over the internet. An internal Network Load Balancer routes requests
      to targets using private IP addresses.
   3. For **Load balancer IP address type**, choose
      **IPv4** if your clients use IPv4 addresses to
      communicate with the Network Load Balancer or **Dualstack** if
      your clients use both IPv4 and IPv6 addresses to communicate with
      the Network Load Balancer.

6. **Network mapping**
   1. For **VPC**, select the same VPC that you used
      for your Application Load Balancer. With an internet-facing load balancer, only VPCs with
      an internet gateway are available for selection.
   2. For **Availability Zones and subnets**, select at
      least one Availability Zones, and select one subnet per zone. We
      recommend that you select the same Availability Zones that are
      enabled for your Application Load Balancer. This optimizes availability, scaling, and
      performance.

   (Optional) To use static IP addresses, choose **Use an
   Elastic IP address** in the **IPv4
   settings** for each Availability Zone. With static IP
   addresses you can add certain IP addresses to an allow list for
   firewalls, or you can hard code IP addresses with clients.

7. **Security groups**

We preselect the default security group for the load balancer VPC.
You can select additional security groups as needed.
If you don't have a security group that meets your needs, choose
**create a new security group** to create one now.
For more information, see [Create a security group](../../../vpc/latest/userguide/creating-security-groups.md "../../../vpc/latest/userguide/creating-security-groups.md") in the
_Amazon VPC User Guide_.

###### Warning

If you don't associate any security groups with your Network Load Balancer
now, you can't associate them later on.

###### Warning

To utilize QUIC or TCP_QUIC listeners, your Network Load Balancer must have no
security groups. 8. **Listeners and routing**

    1. The default is a listener that accepts TCP traffic on port 80.
     Only TCP listeners can forward traffic to an Application Load Balancer target group. You
     must keep **Protocol** as **TCP**,
     but you can modify **Port** as needed.


    With this configuration, you can use HTTPS listeners on the Application Load Balancer
     to terminate TLS traffic.
    2. For **Default action**, select the target group
     that you created in the previous step.
    3. (Optional) Choose **Add listener tag** and enter
     a tag key and a tag value.

9. **Load balancer tags**

(Optional) Expand **Load balancer tags**. Choose
**Add new tag** and enter a tag key and a tag value. For
more information, see [Tags](load-balancer-tags.md "load-balancer-tags.md"). 10. **Summary**

Review your configuration and choose **Create load
balancer**.

AWS CLI

###### To create the Network Load Balancer

Use the [create-load-balancer](../../../cli/latest/reference/elbv2/create-load-balancer.md "../../../cli/latest/reference/elbv2/create-load-balancer.md") command. We recommend that you use
the same Availability Zones that are enabled for your Application Load Balancer.

```
aws elbv2 create-load-balancer \
    --name my-load-balancer \
    --type network \
    --scheme `internal` \
    --subnets `subnet-1234567890abcdef0` `subnet-0abcdef1234567890` \
    --security-groups `sg-1111222233334444`
```

###### To add a TCP listener

Use the [create-listener](../../../cli/latest/reference/elbv2/create-load-balancer.md "../../../cli/latest/reference/elbv2/create-load-balancer.md") command to add a TCP listener.
Only TCP listeners can forward traffic to an Application Load Balancer.
For the default action, use the target group that
you created in the previous step.

```
aws elbv2 create-listener \
    --load-balancer-arn `load-balancer-arn` \
    --protocol TCP \
    --port `80` \
    --default-actions Type=forward,TargetGroupArn=`target-group-arn`
```

CloudFormation

###### To create the Network Load Balancer

Define a resource of type [AWS::ElasticLoadBalancingV2::LoadBalancer](../../../AWSCloudFormation/latest/TemplateReference/aws-resource-elasticloadbalancingv2-loadbalancer.md "../../../AWSCloudFormation/latest/TemplateReference/aws-resource-elasticloadbalancingv2-loadbalancer.md")
and a resource of type [AWS::ElasticLoadBalancingV2::Listener](../../../AWSCloudFormation/latest/TemplateReference/aws-resource-elasticloadbalancingv2-listener.md "../../../AWSCloudFormation/latest/TemplateReference/aws-resource-elasticloadbalancingv2-listener.md").
Only TCP listeners can forward traffic to an Application Load Balancer.
For the default action, use the target group that
you created in the previous step.

```
Resources:
  myLoadBalancer:
    Type: 'AWS::ElasticLoadBalancingV2::LoadBalancer'
    Properties:
      Name: `my-load-balancer`
      Type: network
      Scheme: `internal`
      Subnets:
        - !Ref subnet-AZ1
        - !Ref subnet-AZ2
      SecurityGroups:
        - !Ref mySecurityGroup

  myTCPListener:
    Type: 'AWS::ElasticLoadBalancingV2::Listener'
    Properties:
      LoadBalancerArn: !Ref myLoadBalancer
      Protocol: TCP
      Port: `80`
      DefaultActions:
        - Type: forward
          TargetGroupArn: !Ref myTargetGroup
```

## Step 3: (Optional) Create a VPC endpoint service

To use the Network Load Balancer that you set up in the previous step as an endpoint for private
connectivity, you can enable AWS PrivateLink. This establishes a private connection to
your load balancer as an endpoint service.

###### To create a VPC endpoint service using your Network Load Balancer

1. On the navigation pane, choose **Load Balancers**.
2. Select the name of the Network Load Balancer to open its details page.
3. On the **Integrations** tab, expand **VPC Endpoint
   Services (AWS PrivateLink)**.
4. Choose **Create endpoint services** to open the
   **Endpoint services** page. For the remaining
   steps, see [Create an endpoint service](../../../vpc/latest/privatelink/create-endpoint-service.md#create-endpoint-service-nlb "../../../vpc/latest/privatelink/create-endpoint-service.md#create-endpoint-service-nlb") in the _AWS PrivateLink Guide_.
