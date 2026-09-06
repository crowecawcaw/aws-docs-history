

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see [Amazon CloudWatch Dashboard documentation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.html). 

# Create manual approval policies for just-in-time node access
<a name="systems-manager-just-in-time-node-access-create-manual-policies"></a>

The following procedure describes how to create manual approval policies. Systems Manager lets you create up to 50 manual approval policies per AWS account and AWS Region.

**To create a manual approval policy**

1. Open the AWS Systems Manager console at [https://console.aws.amazon.com/systems-manager/](https://console.aws.amazon.com/systems-manager/).

1. Select **Manage node access** in the navigation pane.

1. In the **Policy details** section of the **Create manual approval policy** step, enter a name and description for the approval policy.

1. Enter a value for the **Access duration**. This is the maximum amount of time a user can start sessions to a node after an access request is approved. The value must be between 1 and 336 hours. 

1. In the **Node targets** section, enter tag key-value pairs associated with the nodes you want the policy to apply to. If none of the tags specified in the policy are associated with a node, the policy isn't applied to the node.

1. In the **Access request approvers** section, enter the users or groups you want to be able to approve access requests to the node targets in the policy. Access request approvers can be IAM Identity Center users and groups or IAM roles. You can specify up to 5 approvers per level, and up to 5 levels of approvers.

1. Select **Create manual approval policy**.