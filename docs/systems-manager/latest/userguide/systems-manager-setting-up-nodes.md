

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see [Amazon CloudWatch Dashboard documentation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.html). 

# Setting up managed nodes for AWS Systems Manager
<a name="systems-manager-setting-up-nodes"></a>

Complete the tasks in this section to set up and configure roles, user accounts, permissions, and initial resources for using AWS Systems Manager tools. The tasks described in this section are typically performed by AWS account and systems administrators. After these steps are complete, users in your organization can use Systems Manager to configure, manage, and access your *managed nodes*. A managed node is any machine configured for use with Systems Manager in a [hybrid and multicloud](operating-systems-and-machine-types.md#supported-machine-types) environment.

**Note**  
If you plan to use Amazon EC2 instances *and* your own computing resources in a [hybrid and multicloud](operating-systems-and-machine-types.md#supported-machine-types) environment, follow the steps in [Managing EC2 instances with Systems Manager](systems-manager-setting-up-ec2.md). That topic presents steps in the best order for completing Systems Manager setup for EC2 instances and non-EC2 machines.

If you already use other AWS services, you have completed some of these steps. However, other steps are specific to Systems Manager. Therefore, we recommend reviewing this entire section to make sure that you're ready to use all Systems Manager tools. 

**Topics**
+ [Managing EC2 instances with Systems Manager](systems-manager-setting-up-ec2.md)
+ [Managing nodes in hybrid and multicloud environments with Systems Manager](systems-manager-hybrid-multicloud.md)
+ [Set up a Cloud Connector for Microsoft Azure in Systems Manager](systems-manager-cloud-connector.md)
+ [Managing edge devices with Systems Manager](systems-manager-setting-up-edge-devices.md)
+ [Creating an AWS Organizations delegated administrator for Systems Manager](setting_up_delegated_admin.md)
+ [General setup for AWS Systems Manager](#setting_up_prerequisites)

## General setup for AWS Systems Manager
<a name="setting_up_prerequisites"></a>

### Sign up for an AWS account
<a name="sign-up-for-aws"></a>

To get started with AWS, you need an AWS account. For information about creating an AWS account, see [Getting started with an AWS account](https://docs.aws.amazon.com/accounts/latest/reference/getting-started.html) in the *AWS Account Management Reference Guide*.