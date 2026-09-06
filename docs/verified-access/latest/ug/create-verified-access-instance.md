

# Create and manage a Verified Access instance
<a name="create-verified-access-instance"></a>

You use a Verified Access instance to organize your trust providers and Verified Access groups. Use the following procedures to create a Verified Access instance, and then attach a trust provider to Verified Access or detach a trust provider from Verified Access.

**Topics**
+ [Create a Verified Access instance](#create-instance)
+ [Attach a trust provider to a Verified Access instance](#attach-trust-provider)
+ [Detach a trust provider from a Verified Access instance](#detach-trust-provider)
+ [Add a custom subdomain](#modify-custom-subdomain)

## Create a Verified Access instance
<a name="create-instance"></a>

Use the following procedure to create a Verified Access instance.

**To create a Verified Access instance using the console**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, choose **Verified Access instances**, and then **Create Verified Access instance**.

1. (Optional) For **Name** and **Description**, enter a name and description for the Verified Access instance.

1. (Network CIDR endpoints) For **Custom subdomain for network CIDR endpoint**, enter a custom subdomain.

1. (Optional) Choose **Enable** for **Federal Information Process Standards (FIPS)** if you require Verified Access to be FIPS compliant.

1. (Optional) For **Verified Access trust provider**, choose a trust provider to attach to the Verified Access instance.

1. (Optional) To add a tag, choose **Add new tag** and enter the tag key and the tag value.

1. Choose **Create Verified Access instance**.

**To create a Verified Access instance using the AWS CLI**  
Use the [create-verified-access-instance](https://docs.aws.amazon.com/cli/latest/reference/ec2/create-verified-access-instance.html) command.

## Attach a trust provider to a Verified Access instance
<a name="attach-trust-provider"></a>

Use the following procedure to attach a trust provider to a Verified Access instance.

**To attach a trust provider to a Verified Access instance using the console**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, choose **Verified Access instances**.

1. Select the instance.

1. Choose **Actions**, **Attach Verified Access trust provider**.

1. For **Verified Access trust provider**, choose a trust provider.

1. Choose **Attach Verified Access trust provider**.

**To attach a trust provider to a Verified Access instance using the AWS CLI**  
Use the [attach-verified-access-trust-provider](https://docs.aws.amazon.com/cli/latest/reference/ec2/attach-verified-access-trust-provider.html) command.

## Detach a trust provider from a Verified Access instance
<a name="detach-trust-provider"></a>

Use the following procedure to detach a trust provider from a Verified Access instance.

**To detach a trust provider from a Verified Access instance using the console**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, choose **Verified Access instances**.

1. Select the instance.

1. Choose **Actions**, **Detach Verified Access trust provider**.

1. For **Verified Access trust provider**, choose the trust provider.

1. Choose **Detach Verified Access trust provider**.

**To detach a trust provider from a Verified Access instance using the AWS CLI**  
Use the [detach-verified-access-trust-provider](https://docs.aws.amazon.com/cli/latest/reference/ec2/detach-verified-access-trust-provider.html) command.

## Add a custom subdomain
<a name="modify-custom-subdomain"></a>

Use the following procedure to add or update a custom subdomain. This subdomain is used only when you create a [network CIDR endpoint](create-network-cidr-endpoint.md).

**To add a custom subdomain using the console**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, choose **Verified Access instances**.

1. Select the instance.

1. Choose **Actions**, **Modify Verified Access instance**.

1. For **Custom subdomain for network CIDR endpoint**, enter a custom subdomain.

1. Choose **Modify Verified Access instance**.

1. Update the nameservers for your subdomain, entering the nameservers provided by Verified Access. This list is available under **Nameservers** on the **Details** tab for the instance.

**To add a custom subdomain using the AWS CLI**  
Use the [modify-verified-access-instance](https://docs.aws.amazon.com/cli/latest/reference/ec2/modify-verified-access-instance.html) command.