# Approval review

Approval reviews provide administrators with governance control over how flows are shared within your organization. When approval review is enabled, all users must submit their flows for review and approval before they can be shared with others. This helps prevent flow sprawl, ensures quality control, and maintains oversight of what flows are available to your users.

Think of approval reviews as a quality gate - it allows your organization to review flows before they become available to everyone, ensuring that only appropriate, well-designed flows are shared broadly.

## How approvals work

Your organization's administrators decide whether to enable approval review. Once enabled, it applies to all flows submitted for sharing, requiring an approval before any other users see them in their library.

### If your organization uses approval reviews

When approval reviews are enabled, you'll work with a three-stage approval cycle:

📝 Submitted

**What it means:** Your flow has been submitted for review and is waiting for approval

**What you can do:**

- View the submitted flow (but cannot edit it)
- Check the approval status
- Add comments about what changes were made
- Withdraw the request if needed
- Wait for reviewer feedback

❌ Rejected

**What it means:** Your flow was reviewed but not approved for sharing

**What you can do:**

- See the reason for rejection (if provided by the reviewer)
- Make necessary changes to address feedback
- Resubmit the updated flow for approval
- View rejection comments from the reviewer

✅ Approved

**What it means:** Your flow has been approved and is now shared with your intended audience

**What you can do:**

- See your flow available to users
- View approval details and who approved it
- Make new changes (which will require a new approval cycle)

### Admin Pro and Author Pro view in the library

Administrators and Author Pro users have special access to manage the approval process:

###### Note

This review ability is not provided to users with promotional Enterprise access (Authors). Only users with full Admin Pro or Author Pro subscriptions can review and approve flows.

#### Review flows tab

**Purpose:** Central location to review all submitted flows

**What you can see:**

- All flows submitted for approval
- Flow details and what changes were made
- Comments from flow creators about their changes
- Approval history and status

#### Approval actions

- **Approve flows:** Accept flows for sharing with intended audiences
- **Reject flows:** Decline flows with optional feedback for improvement
- **Bulk actions:** Approve or reject multiple flows at once
- **View details:** See what specific changes were made or who is being added

## Enabling and disabling approval review

Administrators have full control over when approval review is active in your organization.

### Enabling approval review

When administrators enable approval review:

- All future Flow sharing requires approval
- Existing shared flows remain accessible
- Users can still create and edit flows in draft mode
- Only Admin Pro and Author Pro users can approve flows

### Disabling approval review

When administrators disable approval review:

- All pending approval requests are automatically rejected
- Users can immediately share flows without approval
- Previously approved flows remain shared
- The approval process is bypassed for all future sharing

### Configuration options

Administrators can configure approval review to require approval for:

- Sharing with individuals
- Sharing with groups
- Sharing with everyone in the organization
- Publishing changes to existing shared flows
- Adding new users to existing flows

## Working with approval reviews - step by step

Understanding the approval process helps you navigate it efficiently and get your flows approved quickly.

### For flow creators

#### Submitting for approval

- **Complete your flow** - Ensure it's fully built and tested
- **Add sharing details** - Specify who should have access
- **Include change notes** - Explain what you built or changed
- **Submit for review** - Send to the approval queue
- **Monitor status** - Check for updates and feedback

#### If your flow is rejected

- **Review feedback** - Read the reviewer's comments carefully
- **Make necessary changes** - Address the specific concerns raised
- **Test your updates** - Ensure changes work as expected
- **Resubmit with notes** - Explain how you addressed the feedback
- **Follow up if needed** - Contact reviewers for clarification

### For reviewers (Admin Pro and Author Pro users)

#### Reviewing submitted flows

- **Access the review tab** - Find submitted flows in the library
- **Examine the flow** - Test functionality and review design
- **Check sharing scope** - Verify who will have access
- **Review change notes** - Understand what the creator built or modified
- **Make a decision** - Approve or reject with clear feedback

#### Best practices for reviewers

- **Be timely** - Review submissions promptly to avoid delays
- **Be specific** - Provide clear, actionable feedback for rejections
- **Be consistent** - Apply the same standards across all reviews
- **Be collaborative** - Work with creators to improve flows rather than just rejecting

## Approval review states reference

Use this table to understand the approval review states and what actions are available:

| #   | Flow State | Can Edit?              | Visible to Users? | Available Actions              |
| --- | ---------- | ---------------------- | ----------------- | ------------------------------ |
| 1   | Draft      | ✅ Yes                 | ❌ No             | Submit for approval            |
| 2   | Submitted  | ❌ No                  | ❌ No             | View status, withdraw request  |
| 3   | Rejected   | ✅ Yes (after changes) | ❌ No             | Make changes, resubmit         |
| 4   | Approved   | ❌ No                  | ✅ Yes            | Create new version for changes |
