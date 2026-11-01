

# Smart Approvals
<a name="smart-approvals"></a>


|  | 
| --- |
|    Intended audience:  System administrators and Amazon Quick administrators  | 

**Important**  
Smart Approvals is available in the Amazon Quick desktop app and mobile app. It is not currently available in the web version.

## How Smart Approvals works
<a name="smart-approvals-overview"></a>

When an agent proposes an action on a user's behalf – such as sending email, updating a record, or creating a ticket – Smart Approvals reviews the action and decides whether it can proceed automatically or needs the user's approval. Smart Approvals reviews only the actions that your existing controls already make eligible for automated review. It does not grant new access or change what a user is permitted to do.

Quick evaluates each proposed action in the following order:

1. Quick checks the action against your existing controls: permissions, custom permissions, guardrails, connector action permissions, and the user's own settings. Actions that your policies deny stay denied. Actions that your policies require a person to approve always go to the user.

1. For an action that is eligible for automated review, Smart Approvals evaluates it against the user's request and the conversation. If the action is low-risk and consistent with what the user asked for, Smart Approvals approves it and Quick labels the automatic approval in the conversation.

1. If the action is consequential – for example, it sends content outside the organization, changes permissions, deletes or overwrites content, or initiates a payment – Smart Approvals refers it to the user for review. Review failures, such as timeouts, also go to the user.

**Note**  
Automated review reduces prompts for eligible actions, but it is not a substitute for policy. For any action that must always receive human approval, consider requiring review through connector action permission settings rather than relying on automated review.

### Which actions Smart Approvals reviews
<a name="smart-approvals-eligibility"></a>

Whether Smart Approvals reviews an action depends on the connector's **Action permissions** setting for that action. Smart Approvals reviews an action only when both of the following are true:
+ The connector author set the action to **Let user choose**.
+ The user's permission for the action is **Ask each time**.

In all other cases, the action follows its configured **Action permissions** setting directly and is not reviewed by Smart Approvals first. For example, an action that the connector has set to **Always Allow** proceeds without review, and an action that is set to **Always Ask** goes to the user for approval.

## Enabling or disabling Smart Approvals for users
<a name="smart-approvals-admin"></a>

Smart Approvals is on by default for all users. As an administrator, you control whether users can use Smart Approvals with custom permissions profiles. When you restrict the Smart Approvals feature in a profile, users assigned to that profile cannot use Smart Approvals, and their eligible actions go to a person for review. For more information about custom permissions, see [Custom permissions](custom-permissions.md).

**To enable or disable Smart Approvals in a custom permissions profile**

1. Open the [Quick console](https://aws.amazon.com/quicksight/).

1. Choose **Manage Quick**.

1. In the left navigation, choose **Permissions**, and then choose **Custom permissions**.

1. Create a new profile, or locate an existing profile and choose **Edit**.

1. In the **Capabilities & features** section, expand **AI capabilities**.

1. Set the **Smart Approvals** feature:
   + To **disable** Smart Approvals for users assigned to this profile, restrict the feature.
   + To **enable** Smart Approvals, leave the feature unrestricted.

1. Save the profile, and assign it to the users, roles, or account as needed. For more information, see [Assigning custom permissions profiles](custom-permissions-assign.md).

## Turning Smart Approvals on or off as a user
<a name="smart-approvals-user"></a>

If your administrator allows Smart Approvals for you, you can turn it on or off for yourself from the chat menu. This is a global setting: it applies to all of your conversations and to actions that your scheduled runs take on your behalf.

**To turn Smart Approvals on or off**

1. In chat, choose the **\+** icon to open the chat menu.

1. Turn **Smart Approvals** on or off.

**Note**  
When you turn Smart Approvals off, your eligible actions need your review instead of being approved automatically. Because the setting is global, turning it off also affects the eligible actions that your schedules take on your behalf: those actions wait for your review rather than proceeding automatically.

## Auditing Smart Approvals activity
<a name="smart-approvals-audit"></a>

Amazon Quick records Smart Approvals activity in AWS CloudTrail. CloudTrail records each action that Smart Approvals approves and each change that a user makes to their Smart Approvals setting. Each review event identifies the user, the agent, the connector and action, and the time. All Smart Approvals events use the event source `quicksight.amazonaws.com`.

### Changes to a user's Smart Approvals setting
<a name="smart-approvals-audit-setting"></a>

When a user turns Smart Approvals on or off, CloudTrail records a `BatchUpdatePreferencesInternal` event. In this event, `scope` is set to `USER` and `scopeId` identifies the user. The `preferenceKeys` field is set to `UseSmartApprovals`. The `updatedValues` field shows the new setting: `ON` when the user turned Smart Approvals on, and `OFF` when the user turned it off.

### Actions that Smart Approvals approved
<a name="smart-approvals-audit-approved"></a>

When Smart Approvals approves an action, CloudTrail records a `BatchUpdatePermissionsInternal` event. In this event, the `connectorId` and `actionId` fields identify the connector and the action – for example, `jira` and `jira_create_issue`. The `approvalSource` field is set to `SMART_APPROVALS`.

**Note**  
An event with `approvalSource` set to `SMART_APPROVALS` shows that Smart Approvals approved the action. It does not confirm that the action ran.