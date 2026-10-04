

Amazon WorkSpaces Secure Browser will no longer be open to new customers starting October 29, 2026. If you would like to use Amazon WorkSpaces Secure Browser, sign up prior to that date. Existing customers can continue to use the service as normal. For more information, see [Amazon WorkSpaces Secure Browser availability change](https://docs.aws.amazon.com/workspaces-web/latest/adminguide/workspaces-secure-browser-maintenance-mode.html). 

# Configuring network settings for Amazon WorkSpaces Secure Browser
<a name="network-settings"></a>

To configuring network settings for WorkSpaces Secure Browser follow these steps.

1. Open the WorkSpaces Secure Browser console at [https://console.aws.amazon.com/workspaces-web/home](https://console.aws.amazon.com/workspaces-web/home).

1. Choose **WorkSpaces Secure Browser**, then **Web portals**, and then choose **Create web portal**.

1. On the **Step 1: Specify networking connection** page, complete the following steps to connect your VPC to your web portal and configure your VPC and subnets.

   1. For **Networking details**, choose a VPC with a connection to the content you want your users to access with WorkSpaces Secure Browser.

   1. Choose up to three private subnets that meet the following requirements. For more information, see [Networking for Amazon WorkSpaces Secure Browser](setup-vpc.md).
      + You must choose a minimum of two private subnets to create a portal.
      + To ensure high availability for your web portal, we recommend you provide the maximum number of private subnets in unique availability zones for your VPC. 

   1. Choose a security group.