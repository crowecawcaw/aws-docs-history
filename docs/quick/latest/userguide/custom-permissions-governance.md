# Deny by Default

###### Important

Test Deny by Default configurations in a development or staging account before
applying them to production users. Verify that the behavior matches your expectations
before broad deployment.

## Overview

### What is Deny by Default?

Without Deny by Default, any new capability that Amazon Quick ships is
automatically available to all users upon release. Administrators must manually
restrict each new capability after every release. This reactive approach can expose
regulated environments to unapproved capabilities before administrators have time
to evaluate them.

With Deny by Default enabled, new capabilities in a restricted category are
automatically denied on launch day without administrator action. Administrators
can then evaluate each new capability and explicitly allow it when ready.

### Point-in-time semantics

Capabilities that already exist when you enable Deny by Default remain
available. The restriction is not retroactive. Only capabilities launched after
enablement are denied. Think of it as a forward-looking filter that protects
against future changes without disrupting current workflows.

To restrict capabilities that already exist, you must explicitly set them to
`DENY` in the profile's capabilities configuration.

### When to use this feature

Deny by Default is designed for organizations that require explicit approval
before new capabilities reach users. Common use cases include:

- Financial services organizations with model risk management (MRM) policies
  that require review of AI capabilities before adoption
- Healthcare organizations that must evaluate capabilities for compliance
  before making them available to users
- Enterprises running controlled rollouts where new features are introduced
  incrementally
- Organizations with regulatory or compliance requirements that mandate
  review before capability adoption

## Key concepts

The following table describes the key terms and concepts for Deny by Default.

| Term                        | Definition                                                                                                                                                                                                         |
| --------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Custom permissions profile  | A named configuration object that defines which Amazon Quick capabilities are restricted for a set of users or roles. You can assign profiles at the user, role, or account level.                                 |
| Capability category         | A named grouping of Amazon Quick capabilities used as the unit of control for Deny by Default. At launch, the supported category is AI (all AI and LLM-powered capabilities).                                      |
| Deny by Default             | A setting you can enable within a custom permissions profile to automatically restrict any new capability that Quick launches within a designated category, without requiring administrator action at launch time. |
| Point-in-time semantics     | When you enable Deny by Default for a category, capabilities that already exist at the time of enablement are unaffected. Only capabilities launched after the enablement date are automatically denied.           |
| Forward-looking restriction | Deny by Default restrictions apply to future capabilities only, not to the current state. They do not remove access to capabilities already available to profile users.                                            |
| Precedence hierarchy        | Evaluation order when a user has permissions at multiple levels: User overrides Role, which overrides Account. The most specific level takes precedence.                                                           |
| DefaultCategoryEffects      | The API field that specifies Deny by Default behavior per capability category. Valid values are `DENY_BY_DEFAULT` (restricts new capabilities) and the default behavior when omitted (allow by default).           |
| Conflict resolution         | When a capability is denied at one level but explicitly allowed at another, the most specific permission (User > Role > Account) wins.                                                                             |

## Prerequisites

Before you configure Deny by Default, verify that the following prerequisites are
met.

- **IAM permissions** – You must be a
  Quick administrator with the following IAM permissions:

  - `quicksight:CreateCustomPermissions`
  - `quicksight:UpdateCustomPermissions`
  - `quicksight:DescribeCustomPermissions`
  - `quicksight:ListCustomPermissions`
  - `quicksight:DeleteCustomPermissions`
  - `quicksight:UpdateAccountCustomPermissions`
  - `quicksight:DescribeAccountCustomPermissions`
  - `quicksight:DeleteAccountCustomPermissions`

- **Identity configuration** – Your
  Quick account must be integrated with IAM Identity Center, Active Directory,
  or configured with Quick managed users.

###### Note

All API operations use Amazon QuickSight naming conventions. Permission strings use
the `quicksight:` prefix.

## How capabilities are evaluated

The following rules describe how capability evaluation works when Deny by Default is
enabled. The rules are evaluated in order.

1. If a capability belongs to a restricted category (for example, `AI`)
   with `DENY_BY_DEFAULT` and is not listed in Capabilities, the user is
   denied by default. This is the primary effect of Deny by Default.
2. If a capability is explicitly listed in Capabilities with `ALLOW`, the
   user is permitted for that specific capability. This overrides the
   `DENY_BY_DEFAULT` category default for that capability only. Other
   capabilities in the same category remain denied unless they are also explicitly
   set to `ALLOW`.
3. If a capability is explicitly listed in Capabilities with `DENY`, the
   user is denied.
4. If a capability is not listed and does not belong to a restricted category, the user
   is permitted (allow-by-default behavior is unchanged).

This means that when Quick launches a new capability in a restricted category,
that capability is automatically denied for all users whose profile has
`DENY_BY_DEFAULT` enabled for that category. No administrator action is required.
The restriction takes effect on the day the capability launches.

###### Note

Custom permission profiles are resolved in this priority order: user-level, then
role-level, then account-level (first match wins). A user with a user-level
allow-by-default profile is not subject to an account-level Deny by Default profile.
Assign Deny by Default profiles at the appropriate level for your
requirements.

## Supported categories

The following table describes the supported categories for Deny by Default.

| Category | Covers                                                                                                                                                                   |
| -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `AI`     | All AI and LLM-powered capabilities in Quick, including<br>chat agents, flows, spaces, knowledge bases, apps AI inference, Q<br>analyses, and Quick Desktop AI features. |

###### Note

The category system is modeled using tags. A capability can carry multiple category
tags. If a capability is tagged with more than one category and more than one has Deny
by Default enabled, the most restrictive setting applies.

## Configuring Deny by Default (Quick console)

You configure Deny by Default as part of creating or editing a custom permissions
profile. The setting is controlled by the **Restrict
capabilities** section on the profile configuration page.

###### To enable Deny by Default on a custom permissions profile

1. ###### Step 1: Open the custom permissions settings
   1. Open the [Quick console](https://aws.amazon.com//quicksight/ "https://aws.amazon.com//quicksight/").
   2. Choose **Manage Quick**.
   3. In the left navigation, choose **Permissions**, and
      then choose **Custom permissions**.
   4. Create a new profile by choosing **Create profile**,
      or edit an existing profile by choosing the actions menu and
      then **Edit**.

2. ###### Step 2: Configure the restriction
   1. In the **Restrict capabilities** section, select the
      checkbox for the category you want to restrict (for example,
      **Restrict AI Capabilities**). Selecting this checkbox
      enables Deny by Default for that category. Any capability in this
      category that is not explicitly allowed in the profile is automatically
      denied for users assigned to this profile.
   2. In the **Capabilities & features** section,
      explicitly allow any capabilities within the restricted category that you
      want users to retain access to. Only capabilities you explicitly allow
      are available. All others in the category, including any new
      capabilities that Quick launches in the future, are
      denied.
   3. Review the live preview panel on the right to verify your
      configuration matches your intent.

3. ###### Step 3: Save the profile

Choose **Create** or **Update** to
save the profile.

To remove Deny by Default from a profile, edit the profile and clear the
category checkbox in the **Restrict capabilities** section.
Capabilities that were previously denied become available to users assigned to
the profile.

## Configuring Deny by Default (AWS CLI)

You can use the AWS Command Line Interface to create and manage custom permissions profiles with
Deny by Default enabled.

The following example creates a custom permissions profile with the `AI`
category set to `DENY_BY_DEFAULT`, with the `ChatAgent`
capability explicitly allowed.

```
aws quicksight create-custom-permissions \
--aws-account-id `AWSACCOUNTID` \
--custom-permissions-name `PERMISSIONNAME` \
--capabilities '{"ChatAgent": "ALLOW"}' \
--governance '{"DefaultCategoryEffects": {"AI": "DENY_BY_DEFAULT"}}'
```

The following example updates the Deny by Default settings on an existing profile.

```
aws quicksight update-custom-permissions \
--aws-account-id `AWSACCOUNTID` \
--custom-permissions-name `PERMISSIONNAME` \
--capabilities '{"ChatAgent": "ALLOW", "Flow": "ALLOW"}' \
--governance '{"DefaultCategoryEffects": {"AI": "DENY_BY_DEFAULT"}}'
```

###### Important

`UpdateCustomPermissions` performs a full replacement. You must send
all `--capabilities` and `--governance` values, not just the
delta. Any capability or setting you omit from the update call is removed from the
profile.

The following example describes a profile with Deny by Default enabled.

```
aws quicksight describe-custom-permissions \
--aws-account-id `AWSACCOUNTID` \
--custom-permissions-name `PERMISSIONNAME`
```

###### Note

`DescribeCustomPermissions` returns the `Governance` field
only if the profile was created or updated with Deny by Default settings. Profiles
without Deny by Default return only the `Capabilities` field.

To remove Deny by Default from a profile entirely using the CLI, omit the
`--governance` flag on the update call.

## Examples

### Example 1: Converting an existing profile to Deny by Default

This example shows how to convert an existing allow-by-default profile that
explicitly denies certain AI capabilities to a Deny by Default profile.

**Scenario:** You have a custom permissions profile
that explicitly denies Flow, Automate, and ChatAgent capabilities. All other
capabilities are available by default.

Run the following command to view your current profile configuration:

```
aws quicksight describe-custom-permissions \
--aws-account-id `AWSACCOUNTID` \
--custom-permissions-name "RestrictAI-Finance"
```

The command returns output similar to the following:

```
{
    "CustomPermissions": {
        "CustomPermissionsName": "RestrictAI-Finance",
        "Capabilities": {
            "Flow": "DENY",
            "Automate": "DENY",
            "ChatAgent": "DENY"
        }
    }
}
```

**The problem:** When Quick launches a
new AI capability, it is automatically available to users with this profile because
the profile only blocks explicitly listed capabilities. New capabilities are not
listed, so they are allowed by default.

**The solution:** Convert the profile to Deny by
Default. When you convert, you invert the logic. Instead of listing capabilities
to deny, you list capabilities to allow. Everything not explicitly allowed is denied.

First, determine which AI capabilities you want to allow. In this case, you want
users to retain access to Research, Topics, KnowledgeBase, and Spaces.

Run the following command to update the profile with Deny by Default:

```
aws quicksight update-custom-permissions \
--aws-account-id `AWSACCOUNTID` \
--custom-permissions-name "RestrictAI-Finance" \
--capabilities '{"Research": "ALLOW", "Topics": "ALLOW", "KnowledgeBase": "ALLOW", "Spaces": "ALLOW"}' \
--governance '{"DefaultCategoryEffects": {"AI": "DENY_BY_DEFAULT"}}'
```

**Result:** Now when Quick launches any
new AI capability, it is automatically denied for users with this profile. Only
Research, Topics, KnowledgeBase, and Spaces are available. Flow, Automate,
ChatAgent, and any future AI capabilities are denied.

###### Important

Remember that `UpdateCustomPermissions` performs a full replacement.
Include all capabilities you want to set, not just the ones related to the
conversion.

### Example 2: Setting up Deny by Default for a new account

This example shows how to lock down all AI capabilities from day one for a new
Quick account.

**Scenario:** You are onboarding a new account and
want to restrict all AI capabilities until your team evaluates each one
individually.

Run the following command to create a profile that denies all AI capabilities by
default with no explicit allows:

```
aws quicksight create-custom-permissions \
--aws-account-id `AWSACCOUNTID` \
--custom-permissions-name "DenyAllAI-NewAccount" \
--governance '{"DefaultCategoryEffects": {"AI": "DENY_BY_DEFAULT"}}'
```

Run the following command to assign the profile at the account level so it applies
to all users:

```
aws quicksight update-account-custom-permission \
--aws-account-id `AWSACCOUNTID` \
--custom-permissions-name "DenyAllAI-NewAccount"
```

**Result:** All AI capabilities are denied for every
user in the account. As you evaluate and approve individual capabilities, you can
update the profile to add them to the allow list.

### Example 3: Allowing a specific new capability after launch

This example shows how to approve a new capability that Quick has
launched after you enabled Deny by Default.

**Scenario:** Quick launches a new AI
capability called `NewAIFeature`. Your team evaluates it and decides to
approve it for users.

First, describe the current profile to get the current state:

```
aws quicksight describe-custom-permissions \
--aws-account-id `AWSACCOUNTID` \
--custom-permissions-name "RestrictAI-Finance"
```

The command returns the following output:

```
{
    "CustomPermissions": {
        "CustomPermissionsName": "RestrictAI-Finance",
        "Capabilities": {
            "Research": "ALLOW",
            "Topics": "ALLOW",
            "KnowledgeBase": "ALLOW",
            "Spaces": "ALLOW"
        },
        "Governance": {
            "DefaultCategoryEffects": {
                "AI": "DENY_BY_DEFAULT"
            }
        }
    }
}
```

Update the profile to include the new capability in the allow list. You must
include all existing capabilities plus the new one, because the update performs a
full replacement:

```
aws quicksight update-custom-permissions \
--aws-account-id `AWSACCOUNTID` \
--custom-permissions-name "RestrictAI-Finance" \
--capabilities '{"Research": "ALLOW", "Topics": "ALLOW", "KnowledgeBase": "ALLOW", "Spaces": "ALLOW", "NewAIFeature": "ALLOW"}' \
--governance '{"DefaultCategoryEffects": {"AI": "DENY_BY_DEFAULT"}}'
```

**Result:** The new capability is now available to
users with this profile. All other unlisted AI capabilities remain denied.

### Example 4: Multi-level precedence with Deny by Default

This example shows how Deny by Default interacts with the precedence hierarchy
when profiles are assigned at multiple levels.

**Scenario:** You want most users locked down with
Deny by Default for AI, but you want authors to have access to more capabilities.
A specific data scientist needs full access to all AI capabilities.

**Account-level (most restrictive):** Create a
profile that denies all AI by default with no allows. Assign it at the account
level.

```
aws quicksight create-custom-permissions \
--aws-account-id `AWSACCOUNTID` \
--custom-permissions-name "Account-DenyAllAI" \
--governance '{"DefaultCategoryEffects": {"AI": "DENY_BY_DEFAULT"}}'

aws quicksight update-account-custom-permission \
--aws-account-id `AWSACCOUNTID` \
--custom-permissions-name "Account-DenyAllAI"
```

**Role-level (Author):** Create a profile with Deny
by Default but with more capabilities allowed for power users. Assign it to the
Author role.

```
aws quicksight create-custom-permissions \
--aws-account-id `AWSACCOUNTID` \
--custom-permissions-name "Author-LimitedAI" \
--capabilities '{"Research": "ALLOW", "Topics": "ALLOW", "ChatAgent": "ALLOW"}' \
--governance '{"DefaultCategoryEffects": {"AI": "DENY_BY_DEFAULT"}}'

aws quicksight update-role-custom-permission \
--role AUTHOR \
--aws-account-id `AWSACCOUNTID` \
--namespace default \
--custom-permissions-name "Author-LimitedAI"
```

**User-level (data scientist):** Create an
allow-by-default profile with no restrictions. Assign it to the specific user.

```
aws quicksight create-custom-permissions \
--aws-account-id `AWSACCOUNTID` \
--custom-permissions-name "DataScientist-FullAccess"

aws quicksight update-user-custom-permission \
--aws-account-id `AWSACCOUNTID` \
--namespace default \
--user-name `DATA_SCIENTIST_USERNAME` \
--custom-permissions-name "DataScientist-FullAccess"
```

**Result:**

- Most users (Readers, Admins without user-level overrides) receive the
  account-level profile with all AI capabilities denied.
- Authors receive the role-level profile with Research, Topics, and
  ChatAgent allowed. All other AI capabilities are denied.
- The data scientist receives the user-level profile with no restrictions.
  They are not subject to the account-level or role-level Deny by Default
  settings because user-level takes highest precedence.

## Troubleshooting

###### A user can still access a capability I expected to be denied

Verify the following:

- Use the Check permissions feature to verify that the correct
  profile is assigned to the user.
- Check the precedence hierarchy. A user-level or role-level profile
  might override your account-level Deny by Default profile.
- Confirm that the capability was launched after you enabled Deny by
  Default. Capabilities that existed before enablement are not
  affected.
- Check if the capability is explicitly set to `ALLOW`
  in the profile.

###### I enabled Deny by Default but existing capabilities were not blocked

This is expected behavior. Deny by Default is forward-looking only. It
restricts capabilities launched after enablement. To block capabilities
that already exist, explicitly set them to `DENY` in the
profile's capabilities configuration.
