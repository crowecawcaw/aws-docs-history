• AWS Systems Manager Change Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see
[AWS Systems Manager Change Manager availability change](change-manager-availability-change.md "change-manager-availability-change.md").

 

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see
[Amazon CloudWatch Dashboard documentation](../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md "../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md").

# Create

approval policies for your nodes

Approval policies define what approvals users need to access a node. Since
just-in-time node access removes the need for long standing permissions to nodes
through IAM policies, you must create approval policies to allow access to your
nodes. If there are no approval policies that apply to a node, users are unable to
request access to the node.

In just-in-time node access, there are three types of policies. The policy types
are _auto-approval_, _deny-access_, and
_manual approval_.

###### Just-in-time node access policy types

- An auto-approval policy defines which nodes users can connect to
  automatically.
- Manual approval policies define the number and levels of manual approvals
  that must be provided to access the nodes you specify.
- A deny-access policy explicitly prevents the auto-approval of access
  requests to the nodes you specify.
  A deny-access policy applies to all accounts in an AWS Organizations organization. For
  example, you could explicitly deny auto-approvals for the `Intern` group
  to nodes tagged with the `Production` key. Auto-approval and manual
  approval policies apply only to the AWS accounts and AWS Regions where they're
  created. Each member account in your organization manages their own approval
  policies. Approval policies are evaluated in the following order:

1. Deny-access
2. Auto-approval
3. Manual
   While you can only have one deny-access policy per organization, and one
   auto-approval policy per account and Region, you'll likely have several manual
   approval policies in an account. When evaluating manual approval policies,
   just-in-time node access always favors the more specific policy for a node. Manual
   approval policies are evaluated in the following order:

4. Tag specific target
5. All nodes target
   For example, you have a node tagged with the `Demo` key. In the same
   account, you have a manual approval policy that targets all nodes and requires one
   approval from one level. You also have a manual approval policy that requires two
   approvals from two levels for nodes tagged with the `Demo` key. Systems Manager
   applies the policy that targets the `Demo` tag to the node since it's
   more specific than the policy that targets all nodes. This allows you to create a
   general policy for all nodes in your account, ensuring users can submit access
   requests while enabling you to create more granular policies as needed.

Depending on your organization, there might be multiple tags applied to your
nodes. In this scenario, if multiple manual approval policies apply to a node,
access requests fail. For example, a node is tagged with the `Production`
and `Database` keys. In the same account, you have a manual approval
policy that applies to nodes tagged with the `Production` key and another
manual approval policy that applies to nodes tagged with the `Database`
key. This results in a conflict for the node tagged with both keys and access
requests fail. Systems Manager redirects the user to the failed request. There, they can view
details about the conflicting policies and tags so they can make the necessary
adjustments if they have the required permissions. Otherwise, they can notify a
colleague in their organization with the required permissions to modify the
policies. Policy conflicts resulting in failed access requests emit EventBridge events
allowing you flexibility in building your own response workflows. Additionally,
Systems Manager sends email notifications for policy conflicts resulting in failed access
requests to the recipients you specify. For more information about configuring email
notifications for policy conflicts, see [Configure
notifications for just-in-time access requests](systems-manager-just-in-time-node-access-notifications.md "systems-manager-just-in-time-node-access-notifications.md").

In a _deny-access_ policy, you use the Cedar policy language to
define which nodes users explicitly can't automatically connect to in your
organization. This policy is created and shared from the delegated administrator
account for your organization. The deny-access policy supercedes all auto-approval
policies. You can only have one deny-access policy per organization.

In an _auto-approval_ policy, you use the Cedar policy language
to define which users can automatically connect to the specified nodes without
manual approval. The access duration for an access request that is automatically
approved is 1 hour. This value can't be changed. You can only have one auto-approval
policy per account and Region.

In a _manual_ approval policy, you specify the access duration,
how many levels of approvals are required, the number of approvers required per
level, and the nodes they can approve just-in-time access requests to. The access
duration for a manual approval policy must be between 1 and 336 hours. If you
specify multiple levels of approvals, the approvals for the access request process
one level at a time. This means all approvals you require for one level must be
provided before the approval process moves to subsequent levels. If you specify
multiple tags in a manual approval policy, they are evaluated as `or`
statements not `and` statements. For example, if you create a manual
approval policy that includes the tags `Application`, `Web`,
and `Test`, the policy applies to any node that is tagged with one of
those keys. The policy doesn't apply only to nodes that are tagged with all three
keys.

We recommend using a combination of manual policies with your auto-approval policy
to help you secure nodes with more critical data while allowing users to connect to
less critical nodes without intervention. For example, you can require manual
approvals for access requests to database nodes, and auto-approve sessions to
non-persistent presentation tier nodes.

The following procedures describe how to create approval policies for just-in-time
node access.

###### Topics

- [Create manual approval policies for just-in-time node access](systems-manager-just-in-time-node-access-create-manual-policies.md "systems-manager-just-in-time-node-access-create-manual-policies.md")
- [Statement
  structure and built-in operators for auto-approval and deny-access
  policies](auto-approval-deny-access-policy-statement-structure.md "auto-approval-deny-access-policy-statement-structure.md")
- [Create an auto-approval policy for just-in-time node access](systems-manager-just-in-time-node-access-create-auto-approval-policies.md "systems-manager-just-in-time-node-access-create-auto-approval-policies.md")
- [Create a deny-access policy for just-in-time node access](systems-manager-just-in-time-node-access-create-deny-access-policies.md "systems-manager-just-in-time-node-access-create-deny-access-policies.md")
- [Create approval policies for just-in-time node access with Amazon Q](systems-manager-just-in-time-node-access-create-approval-policies-q-ide-cli.md "systems-manager-just-in-time-node-access-create-approval-policies-q-ide-cli.md")
