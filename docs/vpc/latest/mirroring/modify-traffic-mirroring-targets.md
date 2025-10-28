# View traffic mirror targets and modify target tags

A traffic mirror target is the destination for mirrored traffic. For more information, see
[Understand traffic mirror target concepts](traffic-mirroring-targets.md "traffic-mirroring-targets.md").

Complete the steps in this section to view traffic mirror targets or modify target tags.

###### To view your traffic mirror targets and modify tags using the console

1. Open the Amazon VPC console at
   [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
2. On the navigation pane, choose **Traffic Mirroring**,
   **Mirror targets**.
3. To view a target, select the ID of the traffic mirror target to open its details page.
4. To modify the tags, on the **Tags** tab, choose **Manage
   tags**.
5. (Optional) For each tag to add, choose **Add new tag** and enter the tag key
   and tag value. For each tag to remove, choose **Remove**.
6. Choose **Save**.

###### To view your traffic mirror targets using the AWS CLI

Use the [describe-traffic-mirror-targets](../../../cli/latest/reference/ec2/describe-traffic-mirror-targets.md "../../../cli/latest/reference/ec2/describe-traffic-mirror-targets.md") command.

###### To modify your traffic mirror target tags using the AWS CLI

Use the [create-tags](../../../cli/latest/reference/ec2/create-tags.md "../../../cli/latest/reference/ec2/create-tags.md") command
to add a tag. Use the [delete-tags](../../../cli/latest/reference/ec2/delete-tags.md "../../../cli/latest/reference/ec2/delete-tags.md")
command to remove a tag.
