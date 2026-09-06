

# Create a target group for your Gateway Load Balancer
<a name="create-target-group"></a>

You register targets for your Gateway Load Balancer using a target group.

To route traffic to the targets in a target group, create a listener and specify the target group in the default action for the listener. For more information, see [Listeners](gateway-listeners.md).

You can add or remove targets from your target group at any time. For more information, see [Register targets](target-group-register-targets.md). You can also modify the health check settings for your target group. For more information, see [Modify health check settings](health-checks.md#modify-health-check-settings).

**To create a target group using the console**

1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/).

1. In the navigation pane, under **Load Balancing**, choose **Target Groups**.

1. Choose **Create target group**.

1. **Basic configuration**

   1. For **Choose a target type**, select **Instances** to specify targets by instance ID, or select **IP addresses** to specify targets by IP address.

   1. For **Target group name**, enter a name for the target group. This name must be unique per Region per account, can have a maximum of 32 characters, must contain only alphanumeric characters or hyphens, and must not begin or end with a hyphen.

   1. Verify that **Protocol** is `GENEVE` and **Port** is `6081`. No other protocols or ports are supported.

   1. For **VPC**, select the virtual private cloud (VPC) with the security appliance instances to include in your target group.

1. (Optional) For **Health checks**, modify the settings and advanced settings as needed. If health checks consecutively exceed the **Unhealthy threshold** count, the load balancer takes the target out of service. If health checks consecutively exceed the **Healthy threshold** count, the load balancer puts the target back in service. For more information, see [Health checks for Gateway Load Balancer target groups](health-checks.md).

1. (Optional) Expand **Tags** and add the tags that you need.

1. Choose **Next**.

1. For **Register targets** add one or more targets as follows:
   + If the target type is **Instances**, select one or more instances, enter one or more ports, and then choose **Include as pending below**.
   + If the target type is **IP addresses**, select the network, enter the IP address and ports, and then choose **Include as pending below**.

1. Choose **Create target group**.

**To create a target group using the AWS CLI**  
Use the [create-target-group](https://docs.aws.amazon.com/cli/latest/reference/elbv2/create-target-group.html) command to create the target group, the [add-tags](https://docs.aws.amazon.com/cli/latest/reference/elbv2/add-tags.html) command to tag your target group, and the [register-targets](https://docs.aws.amazon.com/cli/latest/reference/elbv2/register-targets.html) command to add targets.