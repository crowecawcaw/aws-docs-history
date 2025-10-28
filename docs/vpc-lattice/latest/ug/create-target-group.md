# Create a VPC Lattice target group

You register your targets with a target group. By default, the VPC Lattice service sends
requests to registered targets using the port and protocol that you specified for the
target group. You can override this port when you register each target with the target
group.

To route traffic to the targets in a target group, specify the target group in an
action when you create a listener or create a rule for your listener. For more
information, see [Listener rules for your VPC Lattice service](listener-rules.md "listener-rules.md"). You
can specify the same target group in multiple listeners, but these listeners must belong
to the same service. To use a target group with a service, you must verify that the
target group is not in use by a listener for any other service.

You can add or remove targets from your target group at any time. For more
information, see [Register targets with a VPC Lattice target group](register-targets.md "register-targets.md").
You can also modify the health check settings for your target group. For more
information, see [Health checks for your VPC Lattice target groups](target-group-health-checks.md "target-group-health-checks.md").

## Create a target group

You can create a target group and optionally register targets as follows.

###### To create a target group using the console

1. Open the Amazon VPC console at
   [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
2. On the navigation pane, under **VPC Lattice**, choose
   **Target groups**.
3. Choose **Create target group**.
4. For **Choose a target type**, do one of the following:
   - Choose **Instances** to register targets by instance ID.
   - Choose **IP addresses** to register targets by IP address.
   - Choose **Lambda function** to register a Lambda function as a target.
   - Choose **Application Load Balancer** to register an Application Load Balancer as a target.

5. For **Target group name**, enter a name for the target group.
   This name must be unique for your account in each AWS Region, can have a
   maximum of 32 characters, must contain only alphanumeric characters or hyphens,
   and must not begin or end with a hyphen.
6. For **Protocol** and **Port**, you can
   modify the default values as needed. The default protocol is
   **HTTPS** and the default port is
   **443**.

If the target type is **Lambda function**, you can't specify
a protocol or a port. 7. For **IP address type**, choose **IPv4** to register
targets with IPv4 addresses or choose **IPv6** to register targets
with IPv6 addresses. You can't change this setting after the target group is created.

This option is available only if the target type is **IP addresses**. 8. For **VPC**, select a virtual private cloud (VPC).

This option is not available if the target type is **Lambda function**. 9. For **Protocol version**, modify the default value as needed.
The default is **HTTP1**.

This option is not available if the target type is **Lambda function**. 10. For **Health checks**, modify the default settings as needed.
For more information, see [Health checks for your VPC Lattice target groups](target-group-health-checks.md "target-group-health-checks.md").

Health checks are not available if the target type is **Lambda
function**. 11. For **Lambda event structure version**, choose a version.
For more information, see [Receive events from the VPC Lattice
service](lambda-functions.md#receive-event-from-service "lambda-functions.md#receive-event-from-service").

This option is available only if the target type is **Lambda function** 12. (Optional) To add tags, expand **Tags**, choose **Add
new tag**, and enter the tag key and tag value. 13. Choose **Next**. 14. For **Register targets**, you can either skip this step or
add targets as follows:

    * If the target type is **Instances**, select the
     instances, enter the ports, and then choose **Include as pending
     below**.
    * If the target type is **IP addresses**, do the
     following:


    	1. For **Choose a network**, keep the VPC that
    	 you selected for the target group or choose **Other
    	 private IP address**.
    	2. For **Specify IPs and define ports**, enter
    	 the IP address and enter the ports. The default port is the
    	 target group port.
    	3. Choose **Include as pending below**.
    * If the target type is a **Lambda function**, choose a
     Lambda function. To create a Lambda function, choose **Create a
     new Lambda function**.
    * If the target type is a **Application Load Balancer**, choose an Application Load Balancer.
     To create an Application Load Balancer, choose **create an Application Load Balancer**.

15. Choose **Create target group**.

It might take a few minutes for VPC Lattice to register the targets. For more information see, [Why is it taking so long for my DNS changes to propagate in Route 53 and public resolvers?](https://repost.aws/knowledge-center/route-53-propagate-dns-changes "https://repost.aws/knowledge-center/route-53-propagate-dns-changes")

###### To create a target group using the AWS CLI

Use the [create-target-group](../../../cli/latest/reference/vpc-lattice/create-target-group.md "../../../cli/latest/reference/vpc-lattice/create-target-group.md")
command to create the target group and the [register-targets](../../../cli/latest/reference/vpc-lattice/register-targets.md "../../../cli/latest/reference/vpc-lattice/register-targets.md")
command to add targets.

## Shared subnets

Participants can create VPC Lattice target groups in a shared VPC. The following
rules apply to shared subnets:

- All parts of a VPC Lattice service, such as listeners, target groups, and
  targets, must be created by the same account. They can be created in
  subnets owned by or shared with the owner of the VPC Lattice service.
- The targets registered with a target group must be created by the same
  account as the target group.
- Only the owner of a VPC can associate the VPC with a service network.
  Participant resources in a shared VPC that is associated with a service
  network can send requests to services that are associated with the
  service network. However, the administrator can prevent this by using
  security groups, network ACLs, or auth policies.

For more information about the shareable resources for VPC Lattice, see
[Share your VPC Lattice entities](sharing.md "sharing.md").
