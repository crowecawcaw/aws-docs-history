

# Add tags to a multicast domain in AWS Transit Gateway
<a name="tgw-domain-tagging"></a>

Add tags to your resources to help organize and identify them, such as by purpose, owner, or environment. You can add multiple tags to each multicast domain. Tag keys must be unique for each multicast domain. If you add a tag with a key that is already associated with the multicast domain, it updates the value of that tag. For more information, see [Tagging your Amazon EC2 Resources](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Using_Tags.html).

**To add tags to a multicast domain using the console**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. On the navigation pane, choose **Transit Gateway Multicast**.

1. Select the multicast domain.

1. Choose **Actions**, **Manage tags**.

1. For each tag, choose **Add new tag** and enter a **Key** and **Value** for the tag.

1. Choose **Save**.

**To add tags to a multicast domain using the AWS CLI**  
Use the [create-tags](https://docs.aws.amazon.com/cli/latest/reference/ec2/create-tags.html) command.