

# Approval review
<a name="approval-review"></a>

When approval review is enabled, users must submit their flows for review before they can be shared. This gives administrators oversight of what flows are available in the organization.

## How approvals work
<a name="how-approval-review-works"></a>

When approval review is enabled, sharing a flow follows a three-stage cycle:
+ **Submitted** — The flow is waiting for review. You can view it and check the status, but cannot edit it. You can withdraw the request if needed.
+ **Rejected** — The flow was not approved. You can view the reviewer's feedback, update your draft, and resubmit.
+ **Approved** — The flow is shared with your intended audience. Any future changes require a new approval cycle.

## Who can review flows
<a name="admin-and-author-pro-view"></a>

Users with Amazon Quick Enterprise subscriptions (Author Pro or Admin Pro roles) can review and approve flows. Users with Amazon Quick Professional subscriptions cannot review flows.

Reviewers can:
+ View all submitted flows in the **Pending approval** tab
+ Approve or reject flows individually or in bulk
+ Provide feedback when rejecting a flow

## Submitting a flow for approval
<a name="working-with-approval-review"></a>

1. Complete and test your flow.

1. Choose **Share** and specify who should have access.

1. Choose **Submit for review**.

1. Monitor the approval status in the **Pending approval** tab.

If your flow is rejected, review the feedback, update your draft, and resubmit.

## Enabling and disabling approval review
<a name="enabling-and-disabling-approval-review"></a>

Administrators control approval review through the Custom Permissions page.

**When enabled:**
+ All future flow sharing requires approval.
+ Existing shared flows remain accessible.
+ Users can still create and edit flows in draft mode.

**When disabled:**
+ All pending approval requests are automatically rejected.
+ Users can share flows immediately without approval.
+ Previously approved flows remain shared.

## Approval states reference
<a name="reference-approval-review-states"></a>


| State | Can edit? | Visible to users? | Available actions | 
| --- | --- | --- | --- | 
| Draft | Yes | No | Submit for approval | 
| Submitted | No | No | View status, withdraw request | 
| Rejected | Yes | No | Update and resubmit | 
| Approved | No | Yes | Create new draft for changes | 