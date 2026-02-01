• AWS Systems Manager Change Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see
[AWS Systems Manager Change Manager availability change](change-manager-availability-change.md "change-manager-availability-change.md").

 

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see
[Amazon CloudWatch Dashboard documentation](../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md "../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md").

# Just-in-time node access using

Systems Manager

Systems Manager helps you to improve the security of your nodes by supporting
_just-in-time_ access. Just-in-time node access allows users to
request temporary, time-bound access to nodes that you can approve only when access is truly
needed. This removes the need to provide long standing access to nodes managed by IAM
policies. Additionally, Systems Manager provides session recording for RDP sessions to Windows Server nodes
to help you meet compliance requirements, perform root cause analysis, and more. To use
just-in-time node access, you must set up the unified Systems Manager console.

With just-in-time node access, you create granular IAM policies to ensure only the users
you permit can submit access requests to your nodes. Then you create _approval
policies_ which define the approvals required to connect to your nodes. For
just-in-time node access, there are _auto-approval_ policies and
_manual approval_ policies. An auto-approval policy defines which
nodes users can connect to automatically. Manual approval policies define the number and
levels of manual approvals that must be provided to access the nodes you specify. Also, you
can create a _deny-access_ policy. A deny-access policy explicitly
prevents the auto-approval of access requests to the nodes you specify. A deny-access policy
applies to all accounts in an AWS Organizations organization. Auto-approval and manual approval
policies apply only to the AWS accounts and AWS Regions where they're created.

When a user attempts to connect to a node, they're prompted to enter a reason for
accessing the node. Then your approval policies are evaluated. Depending on your policies,
users either connect automatically to the target node or Systems Manager automatically creates a
manual approval request on the requester's behalf. The approvers specified in the manual
approval policy that applies to the node are then notified of the access request, and can
approve or deny the request. Approvers and requesters can be notified by email, or through
Amazon Q Developer in chat applications integration with Slack or Microsoft Teams. Systems Manager only grants access to requested nodes
when the specified approvers provide all required approvals. Once all of the required
approvals are received, the user can start as many sessions to the node as needed for the
duration of the access window specified in the approval policy. Systems Manager doesn't automatically
terminate just-in-time node access sessions. As a best practice, specify values for the
_maximum session duration_ and _idle session
timeout_ session preferences. These preferences prevent users from staying
connected to nodes beyond their approved access window.

We recommend using a combination of approval policies to help you secure nodes with more
critical data while allowing users to connect to less critical nodes without intervention.
For example, you can require manual approvals for access requests to database nodes, and
auto-approve sessions to non-persistent presentation tier nodes.

Systems Manager supports just-in-time node access for users federated with IAM Identity Center or
IAM. When a federated user submits an access request, they specify the target node, and
the reason for needing to connect to the node. Systems Manager compares the user's identity to the
parameters defined in your organization's approval policies. When the auto-approval policy
conditions are met, or approvers manually provide approvals, the requester is able to
connect to the target node. When a user attempts to connect to an approved node, Systems Manager
creates and uses a temporary token to establish the session.

Since the Systems Manager service handles the authentication for access requests and establishing
sessions, you don't have to use IAM policies to manage access to your nodes. By using
just-in-time node access, Systems Manager helps your organization move closer to zero standing
privileges since you only need to allow users to create access requests instead of allowing
them to start sessions with persistent permissions to your nodes. To help you meet
compliance requirements, Systems Manager retains all access requests for 1 year. Systems Manager also emits EventBridge
events for just-in-time node access for failed access requests and status updates to access
requests for manual approvals. For more information see, [Monitoring Systems Manager events with
Amazon EventBridge](monitoring-eventbridge-events.md "monitoring-eventbridge-events.md").

###### Topics

- [Setting up
  just-in-time access with Systems Manager](systems-manager-just-in-time-node-access-setting-up.md "systems-manager-just-in-time-node-access-setting-up.md")
- [Start a
  just-in-time node access session](systems-manager-just-in-time-node-access-start-session.md "systems-manager-just-in-time-node-access-start-session.md")
- [Managing
  just-in-time access requests](systems-manager-just-in-time-node-access-manage-requests.md "systems-manager-just-in-time-node-access-manage-requests.md")
- [Moving to just-in-time node access from Session Manager](systems-manager-just-in-time-node-access-moving-from-session-manager.md "systems-manager-just-in-time-node-access-moving-from-session-manager.md")
- [Disabling just-in-time
  access with Systems Manager](systems-manager-just-in-time-node-access-disable.md "systems-manager-just-in-time-node-access-disable.md")
- [Just-in-time node access frequently asked
  questions](just-in-time-node-access-faq.md "just-in-time-node-access-faq.md")
