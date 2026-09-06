

# Modify Connect attachment and Connect peer tags in AWS Transit Gateway
<a name="modify-connect-attachment-tag"></a>

You can modify the tags for your Connect attachment.

**To modify your Connect attachment tags using the console**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, choose **Transit Gateway Attachments**.

1. Select the Connect attachment, and then choose **Actions**, **Manage tags**.

1. To add a tag, choose **Add new tag** and specify the key name and key value.

1. To remove a tag, choose **Remove**.

1. Choose **Save**. 

You can modify the tags for your Connect peer.

**To modify your Connect peer tags using the console**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, choose **Transit Gateway Attachments**.

1. Select the Connect attachment, and then choose **Connect peers**.

1. Select the Connect peer and then choose **Actions**, **Manage tags**.

1. To add a tag, choose **Add new tag** and specify the key name and key value.

1. To remove a tag, choose **Remove**.

1. Choose **Save**. 

**To modify your Connect attachment and Connect peer tags using the AWS CLI**  
Use the [create-tags](https://docs.aws.amazon.com/cli/latest/reference/ec2/create-tags.html) and [delete-tags](https://docs.aws.amazon.com/cli/latest/reference/ec2/delete-tags.html) commands.