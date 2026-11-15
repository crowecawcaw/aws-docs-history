

# How declarative policies work in Security Hub CSPM
<a name="orgs-policies-how-they-work"></a>

An AWS Security Hub CSPM declarative policy determines where Security Hub CSPM is enabled, by account and AWS Region. It also determines which standards and controls are enabled and which control parameter values apply. The following sections describe how a declarative policy applies across Regions, how it's inherited, and how it changes Security Hub CSPM account management after you attach it. They also provide common use cases.

## Regional configuration
<a name="orgs-policies-regional-config"></a>

A Security Hub CSPM declarative policy sets configuration per Region in two parts:
+ **Enablement.** The declarative policy lists the Regions where Security Hub CSPM is enabled and the Regions where it is disabled. If a Region is in both lists, Security Hub CSPM is disabled there. You can use `ALL_SUPPORTED` to include all current and future Regions. A Region in neither list is ungoverned, and the declarative policy doesn't change Security Hub CSPM in that Region.
+ **Standards and controls.** In each Region where the declarative policy enables Security Hub CSPM, a default configuration sets the enabled standards, control statuses, and custom control parameters. You can add a Regional override to give a specific Region a different configuration.

A Regional override fully replaces the default configuration for that Region. It doesn't merge with the default, so you must specify every standard, control setting, and parameter that you want in that Region. As a result, the standards and controls that a declarative policy enables can differ from one Region to the next.

A declarative policy applies standards and controls only in Regions where they're available. If a declarative policy enables a standard or control in a Region where it isn't available, Security Hub CSPM skips it in that Region without an error. Before you configure a declarative policy, review [Regional limits for Security Hub CSPM](securityhub-regions.md).

Declarative policies don't have a home Region. Controls that evaluate global resources generate findings in every Region where they're enabled. To evaluate global resources once, enable those controls in a single Region by using a Regional override. For an example, see [Security Hub CSPM policy syntax and examples](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_securityhub-cspm_syntax.html) in the *AWS Organizations User Guide*.

For more information about the declarative policy structure and how Regions are resolved, see [Security Hub CSPM policies](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_securityhub-cspm.html) in the *AWS Organizations User Guide*.

## Declarative policy inheritance and precedence
<a name="orgs-policies-inheritance"></a>

Security Hub CSPM declarative policies follow the AWS Organizations inheritance model. A declarative policy attached at the organization root applies to every account in the organization. Accounts also inherit any declarative policy attached to a parent OU. When more than one applies to an account, Organizations merges them into a single effective declarative policy. The one attached closest to the account takes precedence over those attached higher in the hierarchy, unless a parent declarative policy restricts the inheritance operators that child declarative policies can use.

Within the effective declarative policy, a disabled setting takes precedence over an enabled setting at the same level. A Region in both Region lists is disabled, and a control in both `enabled_controls` and `disabled_controls` is disabled.

For more information about inheritance rules, see [Understanding declarative policy inheritance](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_inheritance_mgmt.html) in the *AWS Organizations User Guide*.

## How a declarative policy affects Security Hub CSPM account management
<a name="orgs-policies-account-mgmt"></a>

When a Security Hub CSPM declarative policy governs an account in a Region, the following changes apply:
+ The declarative policy governs Security Hub CSPM completely in that Region. Security Hub CSPM enablement, standards, control statuses, custom control parameters, and the setting that automatically enables new controls all come from the declarative policy.
+ The account can't change these settings through the Security Hub CSPM console or API. For example, Security Hub CSPM denies calls to [EnableSecurityHub](https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_EnableSecurityHub.html), [DisableSecurityHub](https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_DisableSecurityHub.html), [BatchEnableStandards](https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_BatchEnableStandards.html), [BatchDisableStandards](https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_BatchDisableStandards.html), [UpdateStandardsControl](https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_UpdateStandardsControl.html), [BatchUpdateStandardsControlAssociations](https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_BatchUpdateStandardsControlAssociations.html), [UpdateSecurityControl](https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_UpdateSecurityControl.html), and [UpdateSecurityHubConfiguration](https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_UpdateSecurityHubConfiguration.html) from governed accounts and Regions. To change a governed setting, update the declarative policy.
+ The delegated administrator can't disassociate a governed account from its administrator.
+ Accounts and Regions that no declarative policy governs remain self-managed. You can change their settings through the console and API.
+ Central configuration is disabled for the entire organization. For more information, see [Declarative policies and central configuration in Security Hub CSPM](orgs-policies-and-central-config.md).

**Note**  
Attaching a Security Hub CSPM declarative policy can enable Security Hub CSPM, standards, and controls across many accounts and Regions in your organization. Enabling Security Hub CSPM and its controls incurs charges, including charges for AWS Config rule evaluations. For more information, see [AWS Security Hub pricing](https://aws.amazon.com/security-hub/pricing/).

## Automatic administrator and member account management
<a name="orgs-policies-auto-association"></a>

Security Hub CSPM uses administrator and member account associations to give a delegated administrator visibility into member accounts' findings. These associations are Regional. When a declarative policy governs an account, Security Hub CSPM aligns these associations with your organization, in the same way that central configuration does. You don't need to send or accept invitations.

When a declarative policy enables Security Hub CSPM in a Region, Security Hub CSPM manages associations as follows:
+ **Delegated administrator designation.** If your organization has a Security Hub CSPM delegated administrator, Security Hub CSPM designates that account as the Security Hub CSPM administrator in the Region. This happens only if no other administrator is designated in that Region and no declarative policy disables Security Hub CSPM for the delegated administrator in that Region.
+ **Member associations.** Security Hub CSPM associates each governed account as a member of the Region's administrator account. Security Hub CSPM doesn't associate the administrator account with itself.
+ **Invitation-based associations.** If a governed account is a member of an administrator through an invitation, Security Hub CSPM removes that association and associates the account with the delegated administrator instead. If a governed account is itself an invitation-based administrator, Security Hub CSPM first disassociates its member accounts.

When a declarative policy disables Security Hub CSPM in a Region, Security Hub CSPM must first remove administrator and member associations, because you typically can't disable Security Hub CSPM in an account that has them. When you attach a declarative policy that disables Security Hub CSPM to an organization target, Security Hub CSPM removes the associations as follows:
+ For a member account, Security Hub CSPM disassociates the account from its administrator.
+ For an administrator account, including an invitation-based administrator, Security Hub CSPM disassociates all of its member accounts.
+ For the delegated administrator, Security Hub CSPM also removes its administrator designation in that Region. The delegated administrator designation in Organizations doesn't change.

**Important**  
Security Hub CSPM doesn't restore invitation-based associations that it removes. If you need them again, you must re-create them manually. Before you attach a declarative policy that disables Security Hub CSPM, review which accounts are administrators or members. For more information, see [Reviewing a declarative policy's impact before you apply it in Security Hub CSPM](orgs-policies-review-impact.md).

Security Hub CSPM manages these associations on a best-effort basis and repairs missing associations over time. If your organization has no Security Hub CSPM delegated administrator, Security Hub CSPM still applies the declarative policy but doesn't create associations. Security Hub CSPM records administrator designation changes as AWS CloudTrail events in your account.

A declarative policy doesn't manage cross-Region aggregation. To view findings from multiple Regions in one Region, configure [cross-Region aggregation](finding-aggregation.md) from the delegated administrator account.

## Example use cases
<a name="orgs-policies-use-cases"></a>

The following examples show common ways to use a Security Hub CSPM declarative policy. For the declarative policy JSON that implements each pattern, see [Security Hub CSPM policy syntax and examples](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_securityhub-cspm_syntax.html) in the *AWS Organizations User Guide*.
+ **Enable a security baseline across the entire organization.** Attach a declarative policy at the organization root that enables Security Hub CSPM in all Regions and enables the standards you require. Security Hub CSPM automatically configures every account, including accounts that join later, and associates it with the delegated administrator.
+ **Vary configuration by organizational unit.** Use a broad declarative policy at the root for your baseline. Then attach more specific declarative policies to individual OUs to add standards or adjust controls for accounts that have different compliance or workload requirements.
+ **Vary configuration by Region.** Use Regional overrides to enable additional standards in Regions with specific compliance requirements, or to evaluate global resources in only one Region.
+ **Maintain coverage as your organization grows.** Accounts that join the organization or move into a covered OU inherit the effective declarative policy, so new accounts match your baseline without manual setup.