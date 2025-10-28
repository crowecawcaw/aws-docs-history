# Modify Connect attachment and Connect peer tags in AWS Transit Gateway

You can modify the tags for your Connect attachment.

###### To modify your Connect attachment tags using the console

1. Open the Amazon VPC console at
   [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
2. In the navigation pane, choose **Transit Gateway
   Attachments**.
3. Select the Connect attachment, and then choose **Actions**,
   **Manage tags**.
4. To add a tag, choose **Add new tag** and specify the key
   name and key value.
5. To remove a tag, choose **Remove**.
6. Choose **Save**.
   You can modify the tags for your Connect peer.

###### To modify your Connect peer tags using the console

1. Open the Amazon VPC console at
   [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
2. In the navigation pane, choose **Transit Gateway
   Attachments**.
3. Select the Connect attachment, and then choose **Connect
   peers**.
4. Select the Connect peer and then choose **Actions**,
   **Manage tags**.
5. To add a tag, choose **Add new tag** and specify the key
   name and key value.
6. To remove a tag, choose **Remove**.
7. Choose **Save**.

###### To modify your Connect attachment and Connect peer tags using the

AWS CLI

Use the [create-tags](../../../cli/latest/reference/ec2/create-tags.md "../../../cli/latest/reference/ec2/create-tags.md") and
[delete-tags](../../../cli/latest/reference/ec2/delete-tags.md "../../../cli/latest/reference/ec2/delete-tags.md")
commands.
