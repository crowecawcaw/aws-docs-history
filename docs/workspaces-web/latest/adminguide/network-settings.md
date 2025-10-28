# Configuring network settings for Amazon WorkSpaces Secure Browser

To configuring network settings for WorkSpaces Secure Browser follow these steps.

1. Open the WorkSpaces Secure Browser console at [https://console.aws.amazon.com/workspaces-web/home](https://console.aws.amazon.com/workspaces-web/home "https://console.aws.amazon.com/workspaces-web/home").
2. Choose **WorkSpaces Secure Browser**, then **Web portals**, and
   then choose **Create web portal**.
3. On the **Step 1: Specify networking connection** page, complete the
   following steps to connect your VPC to your web portal and configure your VPC and
   subnets.
   1. For **Networking details**, choose a VPC with a connection to the
      content you want your users to access with WorkSpaces Secure Browser.
   2. Choose up to three private subnets that meet the following requirements. For more
      information, see [Networking for Amazon WorkSpaces Secure Browser](setup-vpc.md "setup-vpc.md").
      - You must choose a minimum of two private subnets to create a portal.
      - To ensure high availability for your web portal, we recommend you provide the maximum
        number of private subnets in unique availability zones for your VPC.

   3. Choose a security group.
