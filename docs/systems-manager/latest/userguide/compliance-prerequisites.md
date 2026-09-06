

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see [Amazon CloudWatch Dashboard documentation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.html). 

# Getting started with Compliance
<a name="compliance-prerequisites"></a>

To get started with Compliance, complete the following tasks.



| Task | For more information | 
| --- | --- | 
| Compliance works with patch data in Patch Manager and associations in State Manager. (Patch Manager and State Manager are also both tools in AWS Systems Manager.) Compliance also works with custom compliance types on managed nodes that are managed using Systems Manager. Verify that you have completed the setup requirements for your Amazon Elastic Compute Cloud (Amazon EC2) instances and non-EC2 machines in a [hybrid and multicloud](operating-systems-and-machine-types.md#supported-machine-types) environment. | [Setting up Systems Manager unified console for an organization](systems-manager-setting-up-organizations.md) | 
| Update the AWS Identity and Access Management (IAM) role used by your managed nodes to restrict Compliance permissions. | [Configuring permissions for Compliance](compliance-permissions.md) | 
| If you plan to monitor patch compliance, verify that you've configured Patch Manager. You must perform patching operations by using Patch Manager before Compliance can display patch compliance data. | [AWS Systems Manager Patch Manager](patch-manager.md) | 
| If you plan to monitor association compliance, verify that you've created State Manager associations. You must create associations before Compliance can display association compliance data. | [AWS Systems Manager State Manager](systems-manager-state.md) | 
| (Optional) Configure the system to view compliance history and change tracking.  | [Viewing compliance configuration history and change tracking](compliance-about.md#compliance-history) | 
| (Optional) Create custom compliance types.  | [Assign custom compliance metadata using the AWS CLI](compliance-custom-metadata-cli.md) | 
| (Optional) Create a resource data sync to aggregate all compliance data in a target Amazon Simple Storage Service (Amazon S3) bucket. | [Creating a resource data sync for Compliance](compliance-datasync-create.md) | 