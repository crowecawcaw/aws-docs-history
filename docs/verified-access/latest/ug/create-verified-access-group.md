

# Create and manage a Verified Access group
<a name="create-verified-access-group"></a>

You use Verified Access groups to organize endpoints by their security requirements. When you create a Verified Access endpoint, you associate the endpoint with a group.

**Topics**
+ [Create a Verified Access group](#create-group)
+ [Modify a Verified Access group](#modify-group)

## Create a Verified Access group
<a name="create-group"></a>

Use the following procedures to create a Verified Access group. Before you create a Verified Access group, you must create a Verified Access instance. For more information, see [Create a Verified Access instance](create-verified-access-instance.md#create-instance).

**To create a Verified Access group using the console**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, choose **Verified Access groups**, and then **Create Verified Access group**.

1. (Optional) For **Name tag** and **Description**, enter a name and description for the group.

1. For **Verified Access instance**, select a Verified Access instance to associate with the group.

1. (Optional) For **Policy definition**, enter a Verified Access policy to apply to the group.

1. (Optional) To add a tag, choose **Add new tag** and enter the tag key and the tag value.

1. Choose **Create Verified Access group**.

**To create a Verified Access group using the AWS CLI**  
Use the [create-verified-access-group](https://docs.aws.amazon.com/cli/latest/reference/ec2/create-verified-access-group.html) command.

## Modify a Verified Access group
<a name="modify-group"></a>

Use the following procedure to modify a Verified Access group.

**To modify a Verified Access group using the console**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, choose **Verified Access groups**, and then **Create Verified Access group**.

1. Select the group and then choose **Actions**, **Modify Verified Access group**.

1. (Optional) Update the description.

1. Choose **Create Verified Access group**.

1. Choose the Verified Access instance to associate with the group.

**To modify a Verified Access group using the AWS CLI**  
Use the [modify-verified-access-group](https://docs.aws.amazon.com/cli/latest/reference/ec2/modify-verified-access-group.html) command.