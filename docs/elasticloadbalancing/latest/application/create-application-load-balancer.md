# Create an Application Load Balancer

An Application Load Balancer takes requests from clients and distributes them across targets in a
target group, such as EC2 instances. For more information, see [How ELB works.](../userguide/how-elastic-load-balancing-works.md "../userguide/how-elastic-load-balancing-works.md") in the _Elastic Load Balancing User Guide_.

###### Tasks

- [Prerequisites](#load-balancer-prereqs "#load-balancer-prereqs")
- [Create the load balancer](#create-load-balancer "#create-load-balancer")
- [Test the load balancer](#test-load-balancer "#test-load-balancer")
- [Next steps](#application-load-balancer-next-steps "#application-load-balancer-next-steps")

## Prerequisites

- Decide which Availability Zones and IP address types your application will support.
  Configure the load balancer VPC with subnets in each of these Availability Zones. If
  the application will support both IPv4 and IPv6 traffic, ensure that the subnets have
  both IPv4 and IPv6 CIDRs. Deploy at least one target in each Availability Zone. For
  more information, see [Subnets for your load balancer](application-load-balancers.md#subnets-load-balancer "application-load-balancers.md#subnets-load-balancer").
- Ensure that the security groups for target instances allow traffic on
  the listener port from client IP addresses (if targets are specified by
  instance ID) or load balancer nodes (if targets are specified by IP
  address). For more information, see [Recommended rules](load-balancer-update-security-groups.md#security-group-recommended-rules "load-balancer-update-security-groups.md#security-group-recommended-rules").
- Ensure that the security groups for target instances allow traffic
  from the load balancer on the health check port using the health check
  protocol.

## Create the load balancer

As part of creating an Application Load Balancer, you'll create the load balancer, at least one
listener, and at least one target group. Your load balancer is ready to handle
client requests when there is at least one healthy registered target in each
of its enabled Availability Zones.

Console

###### To create an Application Load Balancer

1.  Open the Amazon EC2 console at
    [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2.  In the navigation pane, choose **Load Balancers**.
3.  Choose **Create load balancer**.
4.  Under **Application Load Balancer**, choose **Create**.
5.  **Basic configuration**
    1. For **Load balancer name**, enter a name for your
       load balancer. The name must be unique within your set of load
       balancers for the Region. Names can have a maximum of 32 characters,
       and can contain only alphanumeric characters and hyphens. They can
       not begin or end with a hyphen, or with `internal-`. You
       can't change the name of your Application Load Balancer after it's created.
    2. For **Scheme**, choose
       **Internet-facing** or
       **Internal**. An internet-facing load balancer
       routes requests from clients to targets over the internet. An
       internal load balancer routes requests to targets using private IP
       addresses.
    3. For **Load balancer IP address type**, choose
       **IPv4** if your clients use IPv4 addresses to
       communicate with the load balancer or **Dualstack**
       if your clients use both IPv4 and IPv6 addresses to communicate with
       the load balancer. Choose **Dualstack without public
       IPv4** if your clients use only IPv6 addresses to
       communicate with the load balancer.

6.  **Network mapping**
    1.  For **VPC**, select the VPC that you prepared for
        your load balancer. With an internet-facing load balancer, only VPCs
        with an internet gateway are available for selection.
    2.  (Optional) For **IP pools**, you can select
        **Use IPAM pool for public IPv4 addresses**. For more
        information, see [IPAM IP address pools](application-load-balancers.md#ip-pools "application-load-balancers.md#ip-pools").
    3.  For **Availability Zones and subnets**, enable zones
        for your load balancer as follows:

            * Select subnets from at least two Availability Zones
            * Select subnets from at least one Local Zone
            * Select one Outpost subnet

        For more information, see [Subnets for your load balancer](application-load-balancers.md#subnets-load-balancer "application-load-balancers.md#subnets-load-balancer").

    With a **Dualstack** load balancer, you must
    select subnets with both IPv4 and IPv6 CIDR blocks.

7.  **Security groups**

We preselect the default security group for the load balancer VPC.
You can select additional security groups as needed.
If you don't have a security group that meets your needs, choose
**create a new security group** to create one now.
For more information, see [Create a security group](../../../vpc/latest/userguide/creating-security-groups.md "../../../vpc/latest/userguide/creating-security-groups.md") in the
_Amazon VPC User Guide_. 8. **Listeners and routing**

    1. The default is a listener that accepts HTTP traffic on port 80.
     You can keep the default listener settings, or modify
     **Protocol** and **Port** as
     needed.
    2. For **Default action**, select a target group to
     forward traffic. If you don't have a target group that meets your
     needs, choose **Create target group** to create one
     now. For more information, see [Create a target group](create-target-group.md "create-target-group.md").
    3. (Optional) Choose **Add listener tag** and enter
     a tag key and a tag value.
    4. (Optional) Choose **Add listener** to add another
     listener (for example, an HTTPS listener).

9. **Secure listener settings**

This section appears only if you add an HTTPS listener.

    1. For **Security policy**, choose a security
     policy that meets your requirements. For more information, see
     [Security policies](describe-ssl-policies.md "describe-ssl-policies.md").
    2. For **Default SSL/TLS certificate**, the following options are available:




    	* If you created or imported a certificate using AWS Certificate Manager,
    	 choose **From ACM**, then choose the
    	 certificate.
    	* If you imported a certificate using IAM, choose
    	 **From IAM**, and then choose your
    	 certificate.
    	* If you don't have an available certificate in
    	 ACM but do have a certificate for use with your load
    	 balancer, select **Import certificate** and
    	 provide the required information. Otherwise, choose
    	 **Request new ACM certificate**. For
    	 more information, see [AWS Certificate Manager certificates](../../../acm/latest/userguide/gs.md "../../../acm/latest/userguide/gs.md") in the
    	 *AWS Certificate Manager User Guide*.
    3. (Optional) Select **Mutual authentication (mTLS)**, choose a
     policy to enable ALPN.


    For more information, see [Mutual TLS authentication](mutual-authentication.md "mutual-authentication.md").

10. **Optimize with service integrations**

(Optional) You can integrate other AWS with your load balancer. For more information,
see [Load balancer integrations](load-balancer-integrations.md "load-balancer-integrations.md"). 11. **Load balancer tags**

(Optional) Expand **Load balancer tags**. Choose
**Add new tag** and enter a tag key and a tag value.
For more information, see [Tags](load-balancer-tags.md "load-balancer-tags.md"). 12. **Summary**

Review your configuration, and choose **Create load
balancer**. A few default attributes are applied to
your Network Load Balancer during creation. You can view and edit them after
creating the Network Load Balancer. For more information, see [Load balancer attributes](application-load-balancers.md#load-balancer-attributes "application-load-balancers.md#load-balancer-attributes").

AWS CLI

###### To create an Application Load Balancer

Use the [create-load-balancer](../../../cli/latest/reference/elbv2/create-load-balancer.md "../../../cli/latest/reference/elbv2/create-load-balancer.md") command.

The following example creates an internet-facing load balancer
with two enabled Availability Zones and a security group.

```
aws elbv2 create-load-balancer \
    --name `my-load-balancer` \
    --type application \
    --subnets `subnet-1234567890abcdef0` `subnet-0abcdef1234567890` \
    --security-groups `sg-1111222233334444`
```

###### To create an internal Application Load Balancer

Include the `--scheme` option as shown in the
following example.

```
aws elbv2 create-load-balancer \
    --name `my-load-balancer` \
    --type application \
    --scheme internal \
    --subnets `subnet-1234567890abcdef0` `subnet-0abcdef1234567890` \
    --security-groups `sg-1111222233334444`
```

###### To create a dualstack Application Load Balancer

Include the `--ip-address-type` option as shown
in the following example.

```
aws elbv2 create-load-balancer \
    --name `my-load-balancer` \
    --type application \
    --ip-address-type dualstack \
    --subnets `subnet-1234567890abcdef0` `subnet-0abcdef1234567890` \
    --security-groups `sg-1111222233334444`
```

###### To add a listener

Use the [create-listener](../../../cli/latest/reference/elbv2/create-listener.md "../../../cli/latest/reference/elbv2/create-listener.md") command. For examples, see
[Create an HTTP listener](create-listener.md "create-listener.md")
and [Create an HTTPS listener](create-https-listener.md "create-https-listener.md").

CloudFormation

###### To create an Application Load Balancer

Define a resource of type [AWS::ElasticLoadBalancingV2::LoadBalancer](../../../AWSCloudFormation/latest/TemplateReference/aws-resource-elasticloadbalancingv2-loadbalancer.md "../../../AWSCloudFormation/latest/TemplateReference/aws-resource-elasticloadbalancingv2-loadbalancer.md").

```
Resources:
  myLoadBalancer:
    Type: 'AWS::ElasticLoadBalancingV2::LoadBalancer'
    Properties:
      Name: `my-alb`
      Type: application
      Scheme: `internal`
      IpAddressType: `dualstack`
      Subnets:
        - !Ref subnet-AZ1
        - !Ref subnet-AZ2
      SecurityGroups:
        - !Ref mySecurityGroup
      Tags:
        - Key: "`department`"
          Value: "`123`"
```

###### To add a listener

Define a resource of type [AWS::ElasticLoadBalancingV2::Listener](../../../AWSCloudFormation/latest/TemplateReference/aws-resource-elasticloadbalancingv2-listener.md "../../../AWSCloudFormation/latest/TemplateReference/aws-resource-elasticloadbalancingv2-listener.md"). For examples, see
[Create an HTTP listener](create-listener.md "create-listener.md") and
[Create an HTTPS listener](create-https-listener.md "create-https-listener.md").

## Test the load balancer

After creating your load balancer, you can verify that your EC2 instances pass
the initial health check. You can then check that the load balancer is sending
traffic to your EC2 instance. To delete the load balancer, see [Delete an Application Load Balancer](load-balancer-delete.md "load-balancer-delete.md").

###### To test the load balancer

1.  After the load balancer is created, choose
    **Close**.
2.  In the navigation pane, choose **Target Groups**.
3.  Select the newly created target group.
4.  Choose **Targets** and verify that your instances are
    ready. If the status of an instance is `initial`, it's typically
    because the instance is still in the process of being registered. This
    status can also indicate that the instance has not passed the minimum number
    of health checks to be considered healthy. After the status of at least one
    instance is healthy, you can test your load balancer. For more information,
    see [Target health status](target-group-health-checks.md#target-health-states "target-group-health-checks.md#target-health-states").
5.  In the navigation pane, choose **Load Balancers**.
6.  Select the newly created load balancer.
7.  Choose **Description** and copy the DNS name of the internet
    facing or internal load balancer (for example,
    my-load-balancer-1234567890abcdef.elb.us-east-2.amazonaws.com).

        * For internet facing load balancers, paste the DNS name into the
         address field of an internet connected web browser.
        * For internal load balancers, paste the DNS name into the address
         field of a web browser which has private connectivity to the VPC.

    If everything is configured correctly, the browser displays the default page of your server.

8.  If the web page does not display, refer to the following documents for additional
    configuration help and troubleshooting steps.
    - For DNS related issues, see [Routing traffic to an ELB load balancer](../../../Route53/latest/DeveloperGuide/routing-to-elb-load-balancer.md "../../../Route53/latest/DeveloperGuide/routing-to-elb-load-balancer.md") in the _Amazon Route 53 Developer Guide_.
    - For Load Balancer related issues, see [Troubleshoot your Application Load Balancers](load-balancer-troubleshooting.md "load-balancer-troubleshooting.md").

## Next steps

After you create your load balancer, you might want to do the following:

- Add [listener rules](listener-rules.md "listener-rules.md").
- Configure [load balancer attributes](edit-load-balancer-attributes.md "edit-load-balancer-attributes.md").
- Configure [target group attributes](edit-target-group-attributes.md "edit-target-group-attributes.md").
- [HTTPS listeners] Add certificates to the
  [optional certificate list](listener-update-certificates.md#add-certificates "listener-update-certificates.md#add-certificates").
- Configure [monitoring features](load-balancer-monitoring.md "load-balancer-monitoring.md").
