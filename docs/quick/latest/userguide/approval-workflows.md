

# Approval workflows
<a name="approval-workflows"></a>


|  | 
| --- |
|  Applies to:  Enterprise Edition  | 


|  | 
| --- |
|    Intended audience:  System administrators and Amazon Quick administrators  | 

## Approval workflow overview
<a name="approval-workflows-overview"></a>

With approval workflows, you require a designated approver group to review and approve certain actions on assets in Amazon Quick before those actions take effect. Use approval workflows when you want a trusted reviewer to validate a sharing decision before the approver grants access. This reduces the risk of unauthorized access to sensitive assets.

Currently, approval workflows support sharing actions. The target user receives access only after the approver approves the request.

Approval workflows support the following asset types:
+ Knowledge bases
+ Spaces
+ Custom chat agents

## How it works
<a name="approval-workflows-how-it-works"></a>

Approval workflows are opt-in. Sharing requires approval only after an administrator creates and enables a policy for an asset type.

An approval workflow involves three personas:

Administrator  
Creates and manages approval policies.

Requester  
Submits share requests that require approval.

Approver  
Reviews and acts on pending approval requests.

## For administrators: setting up approval policies
<a name="approval-workflows-admin"></a>

As an administrator, you create and manage approval policies in the **Approval Policies** section of the account management console.

**To navigate to approval policies**

1. Sign in to Quick as an administrator.

1. Choose your account name, and then choose **Manage Account**.

1. In the left navigation pane, choose **Approval Policies**.

**To create an approval policy**

1. Choose **Create Policy**.

1. Enter a policy name and an optional description.

1. Select the asset types that the policy applies to.

1. Choose one or more approver groups. These are existing identity groups from IAM Identity Center, IAM federation, or Active Directory.

1. In **Assign Policy**, select the user groups whose members must go through the approval workflow when sharing.

1. Choose **Create Policy**.

To manage existing policies, choose a policy to view its details in the side panel. From there, you can edit the policy name, description, asset types, and approver groups. You can also delete policies that are no longer needed.

## For requesters: submitting a share request
<a name="approval-workflows-requester"></a>

Approval requirements depend on the sharing action:

Add a new person to an asset  
Requires approval.

Upgrade access (for example, Viewer to Owner)  
Requires approval.

Downgrade access  
Takes effect immediately; no approval required.

Remove access  
Takes effect immediately; no approval required.

**To submit a share request**

1. Locate the asset that you want to share.

1. Choose **Share**.

1. Add a person or group, or change an existing role.

1. If an approval policy is active, an approval request form appears with the following fields:
   + (Required) **Notes** – Context for the approver.
   + (Optional) **Severity** – For example, Low, Medium, or High.
   + (Required) ****Approval needed by**** – The date by which a decision is needed. This must be a future date.

1. Choose **Send Request**.

### What happens after submission
<a name="approval-workflows-after-submission"></a>

After you submit a request, the following occurs:
+ The approver group receives viewer-level access to the asset so they can review it. Quick grants this access when you submit the request and does not remove it automatically afterward. The asset owner removes the approver group manually.
+ The request enters *Pending* status.
+ The target user does not receive access until the request is approved.

### Tracking requests
<a name="approval-workflows-tracking"></a>

To track your submitted requests, navigate to **My stuff**, and then choose the **My Tasks** widget. Choose **Submitted By Me**.

Opening a request shows the status (Pending, Approved, or Denied), the asset and target user, your submitted notes, severity, date, and any approver comments or decision history.

## For approvers: reviewing and acting on requests
<a name="approval-workflows-approver"></a>

To access pending requests, navigate to **My stuff**, and then choose **My Tasks**. You can view requests under **All** and **Assigned To Me** (requests routed to your approver group).

Before you can act on a request, you must claim it. Choose **Claim Request** to move the request to **Assigned To Me**. This exposes the **Approve** and **Deny** actions.

The access that approvers receive depends on the asset type:

Executable assets (agents)  
Execution access to test. The asset runs in the creator's context, so the approver does not gain direct access to underlying data sources.

Content assets (spaces, knowledge bases)  
Read access to review content.

After reviewing the asset, choose one of the following actions:
+ **Approve** – The target user receives access. The request status changes to Closed – Approved.
+ **Deny** – The request is declined. The requester receives reason codes and written feedback. The request status changes to Closed – Denied.

## Verifying access after approval
<a name="approval-workflows-verify"></a>

After the approver approves a request, you can verify that Quick granted access correctly.
+ **Target user** – The shared asset appears under the relevant section. Refresh the page if it does not appear immediately.
+ **Requester** – In **My stuff**, choose **My Tasks**, and then choose **Submitted By Me**. The request shows *Approved* status. The details panel shows the history and timestamp.
+ **Administrator** – Check the asset's sharing settings. The audit trail in AWS CloudTrail captures Submit, Approve, Deny, and Revoke actions with user, asset, timestamps, and notes.

## Package sharing for custom chat agents
<a name="approval-workflows-package-sharing"></a>

When you share a custom chat agent, you can submit a package share request that includes the agent and its dependencies (knowledge bases, connectors, and spaces) as a single all-or-nothing approval.
+ **Approve** – The target user gets the agent and all listed dependencies.
+ **Deny** – No access to any component is granted.

Approvers can view the full dependency list on the asset page before deciding.

## API reference
<a name="approval-workflows-api"></a>

For programmatic management of approval policies, see the Amazon Quick API Reference.

## Frequently asked questions
<a name="approval-workflows-faq"></a>

Is approval required by default?  
No. Approval workflows are opt-in only. No approval is required unless an administrator creates and enables a policy.

Which edition supports approval workflows?  
Approval workflows are available in Quick Enterprise edition.

Who can be an approver?  
Both Professional and Enterprise users can be approvers. Professional and Enterprise are user subscriptions within Quick Enterprise edition, not separate editions of Quick.

What groups can I use as approver groups?  
You can use existing identity groups from IAM Identity Center, IAM federation, or Active Directory.

What happens if a request is denied?  
The requester receives reason codes and written feedback. They can revise and resubmit the request.

Is approver access to the asset removed after a decision?  
No. The approver group retains viewer-level access. The asset owner removes the approver group manually.

What happens if I delete an approval policy?  
In-flight pending requests continue to completion. New share requests for those asset types no longer require approval.

Can a requester cancel a pending request?  
Yes. In **My stuff**, choose **My Tasks**, choose **Submitted By Me**, and then choose **Cancel request**.

Are approvers notified of new requests?  
Yes. Approvers are notified when new requests are submitted.

Can I audit approval events?  
Yes. All approval events (Submit, Approve, Deny, and Revoke) are logged in AWS CloudTrail.