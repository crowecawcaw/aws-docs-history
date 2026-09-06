

# Create or delete a traffic mirror target
<a name="create-traffic-mirroring-target"></a>

A traffic mirror target is the destination for mirrored traffic. For more information, see [Understand traffic mirror target concepts](traffic-mirroring-targets.md).

Before you can delete a traffic mirror target, you must remove it from any traffic mirror sessions.

After you create a target, assign it to a traffic mirror session. For more information, see [Create, modify, or delete a traffic mirror session](create-traffic-mirroring-session.md).

You must configure a security group for the traffic mirror target that allows VXLAN traffic (UDP port 4789) from the traffic mirror source.

You can share a traffic mirror target across accounts. For more information, see [Share a traffic mirror target](tm-sharing.md).

**To create a traffic mirror target using the console**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In the **Region** selector, choose the AWS Region that you used when you created the resource to use as the destination for the mirrored traffic.

1. On the navigation pane, choose **Traffic Mirroring**, **Mirror targets**.

1. Choose **Create traffic mirror target**.

1. (Optional) For **Name tag**, enter a name for the traffic mirror target.

1. (Optional) For **Description**, enter a description for the traffic mirror target.

1. For **Target type**, choose the type of the traffic mirror target:
   + **Network interface**
   + **Network Load Balancer**
   + **Gateway Load Balancer endpoint**

1. For **Target**, choose the destination resource. We display resources based on the target type that you selected in the previous step.

1. (Optional) For each tag to add, choose **Add new tag** and enter the tag key and tag value.

1. Choose **Create**.

**To create a traffic mirror target using the AWS CLI**  
Use the [create-traffic-mirror-target](https://docs.aws.amazon.com/cli/latest/reference/ec2/create-traffic-mirror-target.html) command.

**To delete a traffic mirror target using the console**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. On the navigation pane, choose **Traffic Mirroring**, **Mirror targets**.

1. Select the traffic mirror target and choose **Delete**.

1. When prompted for confirmation, enter **delete**, and then choose **Delete**.

**To delete a traffic mirror target using the AWS CLI**  
Use the [delete-traffic-mirror-target](https://docs.aws.amazon.com/cli/latest/reference/ec2/delete-traffic-mirror-target.html) command.