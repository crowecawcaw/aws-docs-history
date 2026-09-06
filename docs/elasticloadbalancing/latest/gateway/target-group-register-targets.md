

# Register targets for your Gateway Load Balancer
<a name="target-group-register-targets"></a>

When your target is ready to handle requests, you register it with one or more target groups. You can register targets by instance ID or by IP address. The Gateway Load Balancer starts routing requests to the target as soon as the registration process completes and the target passes the initial health checks. It can take a few minutes for the registration process to complete and health checks to start. For more information, see [Health checks for Gateway Load Balancer target groups](health-checks.md).

If demand on your currently registered targets increases, you can register additional targets in order to handle the demand. If demand on your registered targets decreases, you can deregister targets from your target group. It can take a few minutes for the deregistration process to complete and for the Gateway Load Balancer to stop routing requests to the target. If demand increases subsequently, you can register targets that you deregistered with the target group again. If you need to service a target, you can deregister it and then register it again when servicing is complete.

**Topics**
+ [Considerations](#register-target-groups-considerations)
+ [Target security groups](#target-security-groups)
+ [Network ACLs](#network-acls)
+ [Register targets by instance ID](#register-instances)
+ [Register targets by IP address](#register-ip-addresses)
+ [Deregister targets](#deregister-targets)

## Considerations
<a name="register-target-groups-considerations"></a>
+ Each target group must have at least one registered target in each Availability Zone that is enabled for the Gateway Load Balancer.
+ The target type of your target group determines how you register targets with that target group. For more information, see [Target type](target-groups.md#target-type).
+ You can't register targets across an inter-Region VPC peering.
+ You can't register instances by instance ID across an intra-Region VPC peering, but you can register them by IP address.

## Target security groups
<a name="target-security-groups"></a>

When you register EC2 instances as targets, you must ensure that the security groups for these instances allow inbound and outbound traffic on port 6081.

Gateway Load Balancers do not have associated security groups. Therefore, the security groups for your targets must use IP addresses to allow traffic from the load balancer.

## Network ACLs
<a name="network-acls"></a>

When you register EC2 instances as targets, you must ensure that the network access control lists (ACL) for the subnets for your instances allow traffic on port 6081. The default network ACL for a VPC allows all inbound and outbound traffic. If you create custom network ACLs, verify that they allow the appropriate traffic.

## Register targets by instance ID
<a name="register-instances"></a>

An instance must be in the `running` state when you register it.

**To register targets by instance ID using the console**

1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/).

1. On the navigation pane, under **Load Balancing**, choose **Target Groups**.

1. Choose the name of the target group to open its details page.

1. On the **Targets** tab, choose **Register targets**.

1. Select the instances, and then choose **Include as pending below**.

1. When you are finished adding instances, choose **Register pending targets**.

**To register targets by instance ID using the AWS CLI**  
Use the [register-targets](https://docs.aws.amazon.com/cli/latest/reference/elbv2/register-targets.html) command with the IDs of the instances.

## Register targets by IP address
<a name="register-ip-addresses"></a>

An IP address that you register must be from one of the following CIDR blocks:
+ The subnets of the VPC for the target group
+ 10.0.0.0/8 (RFC 1918)
+ 100.64.0.0/10 (RFC 6598)
+ 172.16.0.0/12 (RFC 1918)
+ 192.168.0.0/16 (RFC 1918)

**To register targets by IP address using the console**

1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/).

1. On the navigation pane, under **Load Balancing**, choose **Target Groups**.

1. Chose the name of the target group to open its details page.

1. On the **Targets** tab, choose **Register targets**.

1. Choose the network, IP addresses, and ports, and then choose **Include as pending below**.

1. When you are finished specifying addresses, choose **Register pending targets**.

**To register targets by IP address using the AWS CLI**  
Use the [register-targets](https://docs.aws.amazon.com/cli/latest/reference/elbv2/register-targets.html) command with the IP addresses of the targets.

## Deregister targets
<a name="deregister-targets"></a>

When you deregister a target, Elastic Load Balancing waits until in-flight requests have completed. This is known as *connection draining*. The status of a target is `draining` while connection draining is in progress. After deregistration is complete, status of the target changes to `unused`. For more information, see [Deregistration delay](edit-target-group-attributes.md#deregistration-delay).

**To deregister targets using the console**

1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/).

1. On the navigation pane, under **Load Balancing**, choose **Target Groups**.

1. Choose the name of the target group to open its details page.

1. Choose the **Targets** tab.

1. Select the targets and then choose **Deregister**.

**To deregister targets using the AWS CLI**  
Use the [deregister-targets](https://docs.aws.amazon.com/cli/latest/reference/elbv2/deregister-targets.html) command to remove targets.