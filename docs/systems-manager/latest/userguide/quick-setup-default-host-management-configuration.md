

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see [Amazon CloudWatch Dashboard documentation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.html). 

# Set up the Default Host Management Configuration for an organization using Quick Setup
<a name="quick-setup-default-host-management-configuration"></a>

With Quick Setup, you can activate Default Host Management Configuration for all accounts and Regions that have been added to your organization in AWS Organizations. This ensures that SSM Agent is kept up to date on all Amazon Elastic Compute Cloud (EC2) instances in the organization, and that they can connect to Systems Manager.

**Before you begin**  
Make sure that the following requirements are met before enabling this setting.
+ The latest version of SSM Agent is already installed on all EC2 instances to be managed in your organization.
+ Your EC2 instances to be managed are using Instance Metadata Service Version 2 (IMDSv2).
+ You are signed in to the management account for your organization, as specified in AWS Organizations, using an AWS Identity and Access Management (IAM) identity (user, role, or group) with administrator permissions.

**Using the default EC2 instance management role**  
Default Host Management Configuration makes use of the `default-ec2-instance-management-role` service setting for Systems Manager. This is a role with permissions that you want made available to all accounts in your organization to allow communication between SSM Agent on the instance and the Systems Manager service in the cloud.

If you have already set this role using the [update-service-setting](https://docs.aws.amazon.com/cli/latest/reference/ssm/update-service-setting.html) CLI command, Default Host Management Configuration uses that role. If you have not set this role yet, Quick Setup will create and apply the role for you. 

To check whether this role has already been specified for your organization, use the [get-service-setting](https://docs.aws.amazon.com/cli/latest/reference/ssm/get-service-setting.html) command.

## Enable automatic updates of SSM Agent every two weeks
<a name="dhmc-enable-automatic-updates"></a>

Use the following procedure to enable the Default Host Management Configuration option for your entire AWS Organizations organization.

**To enable automatic updates of SSM Agent every two weeks**

1. Open the AWS Systems Manager console at [https://console.aws.amazon.com/systems-manager/](https://console.aws.amazon.com/systems-manager/).

1. In the navigation pane, choose **Quick Setup**.

1. On the **Default Host Management Configuration** card, choose **Create**.
**Tip**  
If you already have one or more configurations in your account, first choose the **Library** tab or the **Create** button in the **Configurations** section to view the cards.

1. In the **Configuration options** section, select **Enable automatic updates of SSM Agent every two weeks**.

1. Choose **Create**