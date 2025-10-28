# Create a Network Load Balancer

A Network Load Balancer takes requests from clients and distributes them across targets in a
target group, such as EC2 instances. For more information, see the [Network Load Balancer overview](introduction.md#network-load-balancer-overview "introduction.md#network-load-balancer-overview").

###### Tasks

- [Prerequisites](#load-balancer-prereqs "#load-balancer-prereqs")
- [Create the load balancer](#create-load-balancer "#create-load-balancer")
- [Test the load balancer](#test-load-balancer "#test-load-balancer")
- [Next steps](#create-load-balancer-next-steps "#create-load-balancer-next-steps")

## Prerequisites

- Decide which Availability Zones and IP address types your application
  will support. Configure your load balancer VPC with subnets in each of
  these Availability Zones. If the application will support both IPv4 and
  IPv6 traffic, ensure that the subnets have both IPv4 and IPv6 CIDRs.
  Deploy at least one target in each Availability Zone.
- Ensure that the security groups for target instances allow traffic on
  the listener port from client IP addresses (if targets are specified by
  instance ID) or load balancer nodes (if targets are specified by IP
  address). For more information, see [Target security groups](target-group-register-targets.md#target-security-groups "target-group-register-targets.md#target-security-groups").
- Ensure that the security groups for target instances allow traffic
  from the load balancer on the health check port using the health check
  protocol.
- If you plan to provide your load balancer with static IP addresses,
  ensure that each Elastic IP address is from Amazon's pool of IPv4
  addresses and that it has the same network border group as the load
  balancer.

## Create the load balancer

As part of creating a Network Load Balancer, you'll create the load balancer, at least one
listener, and at least one target group. Your load balancer is ready to handle
client requests when there is at least one healthy registered target in each
of its enabled Availability Zones.

Console

###### To create a Network Load Balancer

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation pane, choose **Load Balancers**.
3. Choose **Create load balancer**.
4. Under **Network Load Balancer**, choose **Create**.
5. **Basic configuration**
   1. For **Load balancer name**, enter a name for your
      Network Load Balancer. The name must be unique within your set of load balancers in
      the Region. It can have a maximum of 32 characters, and contain
      only alphanumeric characters and hyphens. It must not begin or end
      with a hyphen, or with `internal-`.
   2. For **Scheme**, choose
      **Internet-facing** or
      **Internal**. An internet-facing Network Load Balancer
      routes requests from clients to targets over the internet. An
      internal Network Load Balancer routes requests to targets using private IP
      addresses.
   3. For **Load balancer IP address type**, choose
      **IPv4** if your clients use IPv4 addresses to
      communicate with the Network Load Balancer or **Dualstack** if
      your clients use both IPv4 and IPv6 addresses to communicate with
      the Network Load Balancer.

6. **Network mapping**
   1. For **VPC**, select the VPC that you prepared
      for your load balancer. With an internet-facing load balancer,
      only VPCs with an internet gateway are available for selection.
   2. With a dualstack load balancer, you can't add a UDP listener
      unless **Enable prefix for IPv6 source NAT**
      is **On (source NAT prefixes per subnet)**.
   3. For **Availability Zones and subnets**, select
      at least one Availability Zone, and select one subnet per zone.
      Note that subnets that were shared with you are available for
      selection.

   If you select multiple Availability Zones and ensure that you have
   registered targets in each selected zone, this increases the fault
   tolerance of your application. 4. With an internet-facing load balancer, you can select an Elastic IP
   address for each Availability Zone. This provides your load balancer
   with static IP addresses.

   With an internal load balancer, you can enter a private IPv4 address
   from the address range of each subnet or let AWS select one for you.

   With a dualstack load balancer, you can enter an IPv6 address from
   the address range of each subnet or let AWS select one for you.

   For a load balancer with source NAT enabled, you can enter a custom
   IPv6 prefix or let AWS select one for you.

7. **Security groups**

We preselect the default security group for the load balancer VPC.
You can select additional security groups as needed.
If you don't have a security group that meets your needs, choose
**create a new security group** to create one now.
For more information, see [Create a security group](../../../vpc/latest/userguide/creating-security-groups.md "../../../vpc/latest/userguide/creating-security-groups.md") in the
_Amazon VPC User Guide_.

###### Warning

If you don't associate any security groups with your Network Load Balancer
now, you can't associate them later on. 8. **Listeners and routing**

    1. The default is a listener that accepts TCP traffic on port 80. You
     can keep the default listener settings, or modify
     **Protocol** and **Port** as
     needed.
    2. For **Default action**, select a target group to
     forward traffic. If you don't have a target group that meets your
     needs, choose **Create target group** to create one
     now. For more information, see [Create a target group](create-target-group.md "create-target-group.md").
    3. (Optional) Choose **Add listener tag** and enter
     a tag key and a tag value.
    4. (Optional) Choose **Add listener** to add another
     listener (for example, a TLS listener).

9. **Secure listener settings**

This section appears only if you add a TLS listener.

    1. For **Security policy**, choose a security
     policy that meets your requirements. For more information, see
     [Security policies](describe-ssl-policies.md "describe-ssl-policies.md").
    2. For **Default SSL/TLS server
     certificate**, choose **From
     ACM** as the certificate source. Select a
     certificate that you provisioned or imported using
     AWS Certificate Manager. If you don't have an available certificate in
     ACM but do have a certificate for use with your load
     balancer, select **Import certificate** and
     provide the required information. Otherwise, choose
     **Request new ACM certificate**. For
     more information, see [AWS Certificate Manager certificates](../../../acm/latest/userguide/gs.md "../../../acm/latest/userguide/gs.md") in the
     *AWS Certificate Manager User Guide*.
    3. (Optional) For **ALPN policy**, choose a
     policy to enable ALPN. For more information, see [ALPN policies](load-balancer-listeners.md#alpn-policies "load-balancer-listeners.md#alpn-policies").

10. **Load balancer tags**

(Optional) Expand **Load balancer tags**. Choose
**Add new tag** and enter a tag key and a tag value.
For more information, see [Tags](load-balancer-tags.md "load-balancer-tags.md"). 11. **Summary**

Review your configuration, and choose **Create load
balancer**. A few default attributes are applied to
your Network Load Balancer during creation. You can view and edit them after
creating the Network Load Balancer. For more information, see [Load balancer attributes](network-load-balancers.md#load-balancer-attributes "network-load-balancers.md#load-balancer-attributes").

AWS CLI

###### To create a Network Load Balancer

Use the [create-load-balancer](../../../cli/latest/reference/elbv2/create-load-balancer.md "../../../cli/latest/reference/elbv2/create-load-balancer.md") command.

The following example creates an internet-facing load balancer
with two enabled Availability Zones and a security group.

```
aws elbv2 create-load-balancer \
    --name `my-load-balancer` \
    --type network \
    --subnets `subnet-1234567890abcdef0` `subnet-0abcdef1234567890` \
    --security-groups `sg-1111222233334444`
```

###### To create an internal Network Load Balancer

Include the `--scheme` option as shown in the
following example.

```
aws elbv2 create-load-balancer \
    --name `my-load-balancer` \
    --type network \
    --scheme internal \
    --subnets `subnet-1234567890abcdef0` `subnet-0abcdef1234567890` \
    --security-groups `sg-1111222233334444`
```

###### To create a dualstack Network Load Balancer

Include the `--ip-address-type` option as shown
in the following example.

```
aws elbv2 create-load-balancer \
    --name `my-load-balancer` \
    --type network \
    --ip-address-type dualstack \
    --subnets `subnet-1234567890abcdef0` `subnet-0abcdef1234567890` \
    --security-groups `sg-1111222233334444`
```

###### To add a listener

Use the [create-listener](../../../cli/latest/reference/elbv2/create-listener.md "../../../cli/latest/reference/elbv2/create-listener.md") command. For examples, see
[Create a listener](create-listener.md "create-listener.md").

CloudFormation

###### To create a Network Load Balancer

Define a resource of type [AWS::ElasticLoadBalancingV2::LoadBalancer](../../../AWSCloudFormation/latest/TemplateReference/aws-resource-elasticloadbalancingv2-loadbalancer.md "../../../AWSCloudFormation/latest/TemplateReference/aws-resource-elasticloadbalancingv2-loadbalancer.md").

```
Resources:
  myLoadBalancer:
    Type: 'AWS::ElasticLoadBalancingV2::LoadBalancer'
    Properties:
      Name: `my-nlb`
      Type: network
      Scheme: `internal`
      IpAddressType: `dualstack`
      Subnets:
        - !Ref subnet-AZ1
        - !Ref subnet-AZ2
      SecurityGroups:
        - !Ref mySecurityGroup
      Tags:
        - Key: '`department`'
          Value: '`123`'
```

###### To add a listener

Define a resource of type [AWS::ElasticLoadBalancingV2::Listener](../../../AWSCloudFormation/latest/TemplateReference/aws-resource-elasticloadbalancingv2-listener.md "../../../AWSCloudFormation/latest/TemplateReference/aws-resource-elasticloadbalancingv2-listener.md"). For examples,
see [Create a listener](create-listener.md "create-listener.md").

## Test the load balancer

After creating your Network Load Balancer, you can verify that your EC2 instances have
passed the initial health check, and then test that the Network Load Balancer is sending
traffic to your EC2 instances. To delete the Network Load Balancer, see [Delete a Network Load Balancer](load-balancer-delete.md "load-balancer-delete.md").

###### To test the Network Load Balancer

1. After the Network Load Balancer is created, choose **Close**.
2. In the left navigation pane, choose **Target Groups**.
3. Select the new target group.
4. Choose **Targets** and verify that your instances are
   ready. If the status of an instance is `initial`, it's probably
   because the instance is still in the process of being registered or it has
   not passed the minimum number of health checks to be considered healthy.
   After the status of at least one instance is healthy, you can test your Network Load Balancer. For more information, see [Target health status](target-group-health-checks.md#target-health-states "target-group-health-checks.md#target-health-states").
5. In the navigation pane, choose **Load Balancers**.
6. Select the new Network Load Balancer.
7. Copy the DNS name of the Network Load Balancer (for example,
   my-load-balancer-1234567890abcdef.elb.us-east-2.amazonaws.com).
   Paste the DNS name into the address field of an internet-connected web
   browser. If everything is working, the browser displays the default page of
   your server.

## Next steps

After you create your load balancer, you might want to do the following:

- Configure [load balancer attributes](edit-load-balancer-attributes.md "edit-load-balancer-attributes.md").
- Configure [target group attributes](edit-target-group-attributes.md "edit-target-group-attributes.md").
- [TLS listeners] Add certificates to the
  [optional certificate list](listener-update-certificates.md#add-certificates "listener-update-certificates.md#add-certificates").
- Configure [monitoring features](load-balancer-monitoring.md "load-balancer-monitoring.md").
