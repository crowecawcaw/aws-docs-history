AWS Systems Manager Change Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see
[AWS Systems Manager Change Manager availability change](change-manager-availability-change.md "change-manager-availability-change.md").

# Create manual approval policies for just-in-time node access

The following procedure describes how to create manual approval policies.
Systems Manager allows you to create up to 50 manual approval policies per AWS account
and AWS Region.

###### To create a manual approval policy

1. Open the AWS Systems Manager console at [https://console.aws.amazon.com/systems-manager/](https://console.aws.amazon.com/systems-manager/ "https://console.aws.amazon.com/systems-manager/").
2. Select **Manage node access** in the navigation
   pane.
3. In the **Policy details** section of the
   **Create manual approval policy** step, enter a
   name and description for the approval policy.
4. Enter a value for the **Access duration**. This is
   the maximum amount of time a user can start sessions to a node after an
   access request is approved. The value must be between 1 and 336 hours.
5. In the **Node targets** section, enter tag key-value
   pairs associated with the nodes you want the policy to apply to. If none
   of the tags specified in the policy are associated with a node, the
   policy isn't applied to the node.
6. In the **Access request approvers** section, enter
   the users or groups you want to be able to approve access requests to
   the node targets in the policy. Access request approvers can be IAM Identity Center
   users and groups or IAM roles. You can specify up to 5 approvers per
   level, and up to 5 levels of approvers.
7. Select **Create manual approval policy**.
