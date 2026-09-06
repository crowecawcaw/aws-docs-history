

# Versioning
<a name="versioning"></a>

Amazon Quick Flows uses versioning to let you edit a flow without affecting the version that others are using. You can have up to three versions of a flow at any time.

## How versioning works
<a name="how-versioning-works"></a>

Your organization's setup determines which version types you see.

### If your organization uses approval review
<a name="with-approval-workflows"></a>

You work with three version types:
+ **Draft** — Your working copy. You can edit and test your flow without affecting the published version. As you edit, your flow is saved automatically. You can have one draft at a time.
+ **Pending Approval** — A version submitted for review. You can view it and check the approval status, but you cannot edit it. If changes are requested, update your draft and resubmit.
+ **Published** — The approved version that other users can access and run.

For more information about approval reviews, see [Approval review](approval-review.md).

### If your organization doesn't use approval review
<a name="without-approval-workflows"></a>

You work with two version types:
+ **Draft** — Your working copy. You can edit and test your flow without affecting the published version. As you edit, your flow is saved automatically. You can have one draft at a time.
+ **Published** — The version that other users can access and run. You can publish directly when your flow is ready.


| Version Type | Can Edit? | Visible to Users? | Next Step | 
| --- | --- | --- | --- | 
| Draft | Yes | No | Publish (or submit for approval) | 
| Pending Approval\* | No | No | Wait for approval | 
| Published | No | Yes | Create new draft for changes | 

\*Pending Approval only applies if your organization uses approval review.

## Publishing changes
<a name="publishing-your-flow"></a>

Any changes to a flow's title, description, steps, logic, or sharing permissions require publishing. When you publish, the new version replaces the current published version for all users. End users always see only the latest published version.

If your organization uses approval review, publishing submits your flow for review. Once approved, it becomes the new published version. Without approval review, publishing makes changes available immediately.

## Unpublishing flows
<a name="unpublishing-flows"></a>

You can unpublish a shared flow to remove it from general availability while keeping it accessible to co-owners. Viewers lose access, and the flow returns to draft state. Unpublishing does not require approval review.