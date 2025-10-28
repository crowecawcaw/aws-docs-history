# Add tags to a multicast domain in AWS Transit Gateway

Add tags to your resources to help organize and identify them, such as by purpose, owner,
or environment. You can add multiple tags to each multicast domain. Tag keys must
be unique for each multicast domain. If you add a tag with a key that is already
associated with the multicast domain, it updates the value of that tag. For more
information, see [Tagging your Amazon EC2
Resources](../../../AWSEC2/latest/UserGuide/Using_Tags.md "../../../AWSEC2/latest/UserGuide/Using_Tags.md").

###### To add tags to a multicast domain using the console

1. Open the Amazon VPC console at
   [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
2. On the navigation pane, choose **Transit Gateway Multicast**.
3. Select the multicast domain.
4. Choose **Actions**, **Manage tags**.
5. For each tag, choose **Add new tag** and enter a **Key** and
   **Value** for the tag.
6. Choose **Save**.

###### To add tags to a multicast domain using the AWS CLI

Use the [create-tags](../../../cli/latest/reference/ec2/create-tags.md "../../../cli/latest/reference/ec2/create-tags.md") command.
