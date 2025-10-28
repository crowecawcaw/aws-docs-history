# Create a new private re:Post

To create a new private re:Post, follow these steps:

1. Open the re:Post Private console at [https://console.aws.amazon.com/repost-private/](https://console.aws.amazon.com/repost-private/ "https://console.aws.amazon.com/repost-private/").
2. On the console's homepage, choose **Create private re:Post**.
3. If you don’t have IAM Identity Center configured for your account yet, then choose **Open Identity Center**. Follow the instructions in [Getting started](../../../singlesignon/latest/userguide/getting-started.md "../../../singlesignon/latest/userguide/getting-started.md") in the _AWS IAM Identity Center User Guide_.
4. On the **Create private re:Post** page, for **Pricing**, select **Free tier** or **Standard tier** based on your use case. If you already used Free Tier for your account, then **Free tier** option isn't available to you.
5. Under **Details**, do the following:

For **Name**, enter a unique name for your private re:Post.

(Optional) For **Description**, enter a brief description for your private re:Post.

For **Custom subdomain**, enter a custom name for your subdomain. 6. (Optional) To customize your data encryption settings, under **Data encryption**, select **Customize encryption settings**. Then, do either of the following actions:

For **Choose an AWS KMS key**, select an AWS Key Management Service key or an Amazon Resource Name (ARN).

-or-

Choose **Create an AWS KMS key**. Then, [create the AWS KMS key](../../../kms/latest/developerguide/create-keys.md "../../../kms/latest/developerguide/create-keys.md"). 7. (Optional) Under **Service access for Support case integration**, select **Enable service access for this re:Post**.

###### Note

You can also turn on this option after you create the private re:Post.

For **Please select an existing IAM role below or create a new role in IAM console**, use the search bar to find your existing IAM role.

-or-

Choose **create a new role in IAM console**.

If you choose to create a new role, then follow the instructions in [Create an IAM role](repost-manage-permissions.md#creating-an-iam-role-for-repost "repost-manage-permissions.md#creating-an-iam-role-for-repost").

If you choose to use an existing service role, then in the search bar, enter the ARN of the role that you want to use. Choose the role from the dropdown list.

For more information, see [Manage access to Support case creation and management in re:Post Private](repost-manage-permissions.md "repost-manage-permissions.md"). 8. (Optional) Under **Tags**, choose **Add new tag**. Then enter the following information:

For **Key**, enter your custom tag key.

For **Value**, enter your custom tag value.

To add more tags, choose **Add new tag**. 9. Choose **Create this re:Post**.
A confirmation page will let you know that your private re:Post is being created. You can view the status of the private re:Post in the **Status** field. When your private re:Post is created, the **Status** field displays **Creating**.

It takes approximately 30 minutes for the private re:Post to be created. When your private re:Post is ready, the **Status** field displays **Online**. You can use the **AWS generated subdomain** for your private re:Post that's listed under the **Settings** tab to access your private re:Post. You can view the **Custom subdomain** for your private re:Post under the **Settings** tab after the review is completed.

###### Note

From April 18, 2025, all new re:Post Private instances support dual stack networking with both IPv4 and IPv6 connectivity.
