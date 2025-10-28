# Versioning

Versions help you manage your Amazon Quick Flows as you build, test, and share them with others. Think of versions like saving different copies of your work - you can have a working copy while keeping a clean, published version for others to use. Amazon Quick Flows keep it simple with no more than three versions for any given flow.

## How versioning works

Your organization's setup determines which version types you'll see:

### If your organization uses approval review

You'll work with three types of versions. For detailed information about how approval reviews work, see the Amazon Quick Flows - Approval reviews documentation.

🔧 Draft

**What it is:** your working copy where you build and test your flow. You can continue to run Drafts as private flows without ever sharing them.

**What you can do:**

- Edit and modify your flow freely
- Add cards like Amazon Quick Sight cards, file upload cards, and output cards
- Test your changes before sharing
- Save your work automatically as you go
- Create multiple drafts to try different approaches

⏳ Pending Approval

**What it is:** this version of the flow is waiting for an eligible user to review and approve it for sharing.

**What you can do:**

- View your submitted flow (but can't edit it)
- Check the approval status
- Respond to reviewer feedback
- Wait for approval or address requested changes before re-submitting it for review

✅ Published

**What it is:** Your approved flow that others can now use

**What you can do:**

- See your live, published flow
- Use it as a starting point for new drafts

### If your organization doesn't use approval review

You'll work with two types of versions:

🔧 Draft

**What it is:** Your private workspace for building flows

**What you can do:**

- Edit and test your flow
- Save changes automatically
- Keep your work private until ready to share

✅ Published

**What it is:** Your published flow that others can use immediately

**What you can do:**

- Publish directly when your flow is ready
- Make it available to users right away
- Use it as a baseline for future changes

## Key versioning concepts

Understanding these core concepts will help you work effectively with Amazon Quick Flows versioning:

**Multi-versioning for creators:** As a flow creator, you can see and work with multiple versions of your flow (draft, pending approval, shared). This allows you to continue developing while users access the stable published version.

**Single version for users:** End users always see only one version of your flow - the currently published version. This prevents confusion and ensures everyone has the same experience.

**Publish changes workflow:** When you make changes to an existing shared flow, you must "publish changes" to make those updates available to users. This creates a new version and may trigger approval review.

**Version replacement:** Each time you publish changes, the new version replaces the previous published version for all users. Historical versions are maintained for creators but users always see the latest approved version.

**App definition versioning:** Changes to core flow elements like title, description, and structure are considered app definition changes and require going through the full publishing process.

## Creating and editing flows

All new flows begin as drafts in your private workspace. You can build and test your flow, adding cards, configuring settings, and iterating as needed. Your work saves automatically, but you can manually save important milestones. When you're ready to share your flow with others, you'll need to "publish changes" to make it available to your intended audience.

## Publishing your flow

**With approval review:** When your draft is ready, you "publish changes" to submit it for review. Your flow moves to "Pending Approval" status where reviewers can evaluate it. If changes are requested, you'll need to create a new draft with updates and resubmit. Once approved, your flow becomes "Published" and available to users. Any future changes to a shared flow require republishing and going through the approval process again.

**Without approval review:** When your draft is ready, you "publish changes" to share it immediately. Your flow becomes "Published" and available to users right away. You can continue making changes in draft mode and publish updates as needed.

## Making changes to shared flows

Once you've shared a flow, any changes you make require going through the "publish changes" process to make them available to users. This ensures that users always have access to a stable, tested version while you continue developing improvements.

### The publish changes workflow

When you modify a shared flow, you're working in a new draft version. Users continue to see and use the current published version until you complete the publish changes process. This approach prevents users from seeing incomplete or untested changes.

**Title and description changes:** Updates to your flow's title or description are considered app definition changes. These require publishing changes and, if approval review is enabled, going through the approval process again.

**Content changes:** Modifications to cards, prompts, or flow logic also require publishing changes. Each published update creates a new version that replaces the previous version for all users.

**Sharing permission changes:** Adding new users or changing permissions (such as converting viewers to co-owners) may require approval depending on your organization's settings.

## Unpublishing flows

You can unpublish a shared flow to remove it from general availability while keeping it accessible to co-owners. When you unpublish a flow:

- **Viewers lose access:** Users with viewer permissions can no longer see or use the flow
- **Co-owners retain access:** Co-owners can still access and work with the unpublished flow
- **Draft state:** The flow returns to draft state for further development
- **No approval required:** Unpublishing does not require going through approval review

This feature is useful when you need to make significant changes to a widely-shared flow or temporarily remove access while addressing issues.

## Tips for success

Follow these best practices to ensure your flows work reliably and provide a great experience for your users.

### Before you submit or publish

- ✅ Test your flow thoroughly with different scenarios and inputs
- ✅ Check that all steps work as expected
- ✅ Verify data permissions are set up correctly for your intended users
- ✅ Add clear descriptions and help text for users
- ✅ Review any error handling or edge cases

### Managing multiple versions

- Keep track of what changes you made in each version
- Use descriptive names or notes to identify different versions
- Don't delete important drafts until you're sure you won't need them

### Working with your team

- Communicate with teammates about who's working on what
- Coordinate timing for publishing shared flows
- Let users know when important flows are being updated
- Ensure proper access permissions are in place before sharing

## Version reference

Use this table as a quick reference to understand what you can do with each version type and what the next steps are in your workflow.

| #   | Version Type     | Can Edit? | Visible to Users? | Next Step                    |
| --- | ---------------- | --------- | ----------------- | ---------------------------- |
| 1   | Draft            | ✅ Yes    | ❌ No             | Submit/Publish               |
| 2   | Pending Approval | ❌ No     | ❌ No             | Wait for approval            |
| 3   | Shared           | ❌ No     | ✅ Yes            | Create new draft for changes |
