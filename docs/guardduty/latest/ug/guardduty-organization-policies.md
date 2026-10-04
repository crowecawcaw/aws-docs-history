

# Managing accounts using organization policies
<a name="guardduty-organization-policies"></a>

A GuardDuty organization policy lets you centrally enable and manage Amazon GuardDuty across the accounts in your organization. You use an AWS Organizations declarative policy to specify which organizational entities (the organization root, organizational units (OUs), or individual accounts) have the GuardDuty foundational detector and its protection plans automatically enabled and managed through the delegated GuardDuty administrator account. Accounts that join the organization, or move into an OU that has an attached policy, inherit the policy and have GuardDuty and its protection plans configured according to what the effective policy defines for them.

GuardDuty organization policies are a different mechanism from the auto-enable settings described in [Managing GuardDuty accounts with AWS Organizations](guardduty_organizations.md). For the policy concept, structure, inheritance, validation, and example policies, see [GuardDuty policies](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_guardduty.html) in the AWS Organizations User Guide.

**Topics**
+ [Prerequisites](#guardduty-organization-policies-prerequisites)
+ [How organization policies work](guardduty-organization-policies-how-it-works.md)
+ [Creating a policy in the console](guardduty-organization-policies-create-console.md)
+ [Reviewing a policy's impact before you apply it](guardduty-organization-policies-review-impact.md)
+ [Considerations and limitations](guardduty-organization-policies-considerations.md)

## Prerequisites
<a name="guardduty-organization-policies-prerequisites"></a>

Before you use GuardDuty organization policies, complete the following prerequisites:
+ Enable trusted access for the GuardDuty service in AWS Organizations.
+ Assign a delegated GuardDuty administrator account.
+ Attach the delegation policy that grants the delegated administrator permission to manage GuardDuty policies.
+ Enable the `GUARDDUTY_POLICY` policy type on the organization root. This happens automatically when the delegated administrator creates the first policy in the GuardDuty console.

**Warning**  
Enabling the `GUARDDUTY_POLICY` policy type stops the Regional GuardDuty auto-enablement settings from applying, even before you attach a policy. Because the console enables this policy type automatically when the delegated administrator creates the first policy, you can stop relying on auto-enablement without intending to. Review your existing auto-enablement configuration before you create your first policy.

For the detailed steps, see [GuardDuty policies](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_guardduty.html) in the AWS Organizations User Guide.