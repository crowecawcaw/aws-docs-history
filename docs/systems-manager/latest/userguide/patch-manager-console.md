

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see [Amazon CloudWatch Dashboard documentation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.html). 

# Working with Patch Manager resources and compliance using the console
<a name="patch-manager-console"></a>

To use Patch Manager, complete the following tasks. These tasks are described in more detail in this section.

1. Verify that the AWS predefined patch baseline for each operating system type that you use meets your needs. If it doesn't, create a patch baseline that defines a standard set of patches for that managed node type and set it as the default instead.

1. Organize managed nodes into patch groups by using Amazon Elastic Compute Cloud (Amazon EC2) tags (optional, but recommended).

1. Do one of the following:
   + (Recommended) Configure a patch policy in Quick Setup, that lets you install missing patches on a schedule for an entire organization, a subset of organizational units, or a single AWS account. For more information, see [Configure patching for instances in an organization using a Quick Setup patch policy](quick-setup-patch-manager.md).
   + Create a maintenance window that uses the Systems Manager document (SSM document) `AWS-RunPatchBaseline` in a Run Command task type. For more information, see [Tutorial: Create a maintenance window for patching using the console](maintenance-window-tutorial-patching.md).
   + Manually run `AWS-RunPatchBaseline` in a Run Command operation. For more information, see [Running commands from the console](running-commands-console.md).
   + Manually patch nodes on demand using the **Patch now** feature. For more information, see [Patching managed nodes on demand](patch-manager-patch-now-on-demand.md).

1. Monitor patching to verify compliance and investigate failures.