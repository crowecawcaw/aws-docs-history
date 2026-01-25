# Register targets for your Gateway Load Balancer

When your target is ready to handle requests, you register it with one or more target
groups. You can register targets by instance ID or by IP address. The Gateway Load Balancer starts
routing requests to the target as soon as the registration process completes and the
target passes the initial health checks. It can take a few minutes for the registration
process to complete and health checks to start. For more information, see [Health checks for Gateway Load Balancer target groups](health-checks.md "health-checks.md").

If demand on your currently registered targets increases, you can register additional
targets in order to handle the demand. If demand on your registered targets decreases,
you can deregister targets from your target group. It can take a few minutes for the
deregistration process to complete and for the Gateway Load Balancer to stop routing requests to the
target. If demand increases subsequently, you can register targets that you deregistered
with the target group again. If you need to service a target, you can deregister it and
then register it again when servicing is complete.

###### Contents

- [Considerations](#register-target-groups-considerations "#register-target-groups-considerations")
- [Target security groups](#target-security-groups "#target-security-groups")
- [Network ACLs](#network-acls "#network-acls")
- [Register targets by instance ID](#register-instances "#register-instances")
- [Register targets by IP address](#register-ip-addresses "#register-ip-addresses")
- [Deregister targets](#deregister-targets "#deregister-targets")

## Considerations

- Each target group must have at least one registered target in each Availability
  Zone that is enabled for the Gateway Load Balancer.
- The target type of your target group determines how you register targets with that
  target group. For more information, see [Target type](target-groups.md#target-type "target-groups.md#target-type").
- You can't register targets across an inter-Region VPC peering.
- You can't register instances by instance ID across an intra-Region VPC peering,
  but you can register them by IP address.

## Target security groups

When you register EC2 instances as targets, you must ensure that the security
groups for these instances allow inbound and outbound traffic on port 6081.

Gateway Load Balancers do not have associated security groups. Therefore, the security groups for
your targets must use IP addresses to allow traffic from the load balancer.

## Network ACLs

When you register EC2 instances as targets, you must ensure that the network
access control lists (ACL) for the subnets for your instances allow traffic on port 6081. The default network ACL for a VPC allows all inbound and outbound traffic. If
you create custom network ACLs, verify that they allow the appropriate
traffic.

## Register targets by instance ID

An instance must be in the `running` state when you register
it.

###### To register targets by instance ID using the console

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. On the navigation pane, under **Load Balancing**,
   choose **Target Groups**.
3. Choose the name of the target group to open its details
   page.
4. On the **Targets** tab, choose **Register targets**.
5. Select the instances, and then choose **Include as pending below**.
6. When you are finished adding instances, choose
   **Register pending targets**.

###### To register targets by instance ID using the AWS CLI

Use the [register-targets](../../../cli/latest/reference/elbv2/register-targets.md "../../../cli/latest/reference/elbv2/register-targets.md") command with the IDs of the instances.

## Register targets by IP address

An IP address that you register must be from one of the following CIDR
blocks:

- The subnets of the VPC for the target group
- 10.0.0.0/8 (RFC 1918)
- 100.64.0.0/10 (RFC 6598)
- 172.16.0.0/12 (RFC 1918)
- 192.168.0.0/16 (RFC 1918)

###### To register targets by IP address using the console

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. On the navigation pane, under **Load Balancing**, choose **Target
   Groups**.
3. Chose the name of the target group to open its details page.
4. On the **Targets** tab, choose **Register targets**.
5. Choose the network, IP addresses, and ports, and then
   choose **Include as pending below**.
6. When you are finished specifying addresses, choose
   **Register pending targets**.

###### To register targets by IP address using the AWS CLI

Use the [register-targets](../../../cli/latest/reference/elbv2/register-targets.md "../../../cli/latest/reference/elbv2/register-targets.md") command with the IP addresses of the targets.

## Deregister targets

When you deregister a target, Elastic Load Balancing waits until in-flight requests have completed.
This is known as _connection draining_. The status of a target is
`draining` while connection draining is in progress. After deregistration
is complete, status of the target changes to `unused`. For more information,
see [Deregistration delay](edit-target-group-attributes.md#deregistration-delay "edit-target-group-attributes.md#deregistration-delay").

###### To deregister targets using the console

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. On the navigation pane, under **Load Balancing**, choose **Target
   Groups**.
3. Choose the name of the target group to open its details
   page.
4. Choose the **Targets** tab.
5. Select the targets and then choose **Deregister**.

###### To deregister targets using the AWS CLI

Use the [deregister-targets](../../../cli/latest/reference/elbv2/deregister-targets.md "../../../cli/latest/reference/elbv2/deregister-targets.md")
command to remove targets.
