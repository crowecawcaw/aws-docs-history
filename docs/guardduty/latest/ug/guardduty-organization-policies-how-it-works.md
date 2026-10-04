

# How organization policies work
<a name="guardduty-organization-policies-how-it-works"></a>

A GuardDuty organization policy determines which GuardDuty features are enabled, in which Regions, and for which accounts. The following sections describe how a policy applies across Regions, how policies are inherited through your organization, how an active policy changes the way you manage GuardDuty accounts, and common ways to use a policy.

**Topics**
+ [Regional configuration](#guardduty-organization-policies-regional)
+ [Policy inheritance and precedence](#guardduty-organization-policies-inheritance)
+ [How a policy affects GuardDuty account management](#guardduty-organization-policies-effects)
+ [Example use cases](#guardduty-organization-policies-use-cases)

## Regional configuration
<a name="guardduty-organization-policies-regional"></a>

A GuardDuty organization policy sets enablement per Region. The default configuration applies in every Region where GuardDuty is available. You can add a Regional override to give a specific Region a different configuration. The default configuration is optional. If you omit it, only the Regions you specify are managed, and every other Region is left unmanaged.

When a policy enables GuardDuty broadly, such as a default configuration that covers every Region, GuardDuty processes AWS CloudTrail global service events in every Region where it is enabled, including Regions where you have no resources or workloads. For more information, see [How GuardDuty handles AWS CloudTrail global events](guardduty_data-sources.md#cloudtrail_global).

A policy manages GuardDuty and a protection plan only in Regions where they are available. If your policy enables GuardDuty or a protection plan in a Region where it is not available, the policy skips it in that Region without an error. Before you configure a policy, review where GuardDuty and each protection plan are available. For more information, see [Region-specific feature availability](guardduty_regions.md#gd-regional-feature-availability).

A Regional override fully replaces the default configuration for that Region. It does not merge with the default, so you must specify every protection plan you want managed in that Region. Any protection plan you leave out of an override is not managed in that Region, even if the default configuration manages it. Because of this, the protection plans a policy manages can differ from one Region to the next.

For the full policy structure and how Regions are resolved, see [GuardDuty policies](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_guardduty.html) in the AWS Organizations User Guide.

## Policy inheritance and precedence
<a name="guardduty-organization-policies-inheritance"></a>

GuardDuty organization policies follow the AWS Organizations inheritance model. A policy attached at the organization root applies to every account in the organization. Accounts also inherit any policy attached to a parent OU. When more than one policy applies to an account, AWS Organizations merges them into a single effective policy, and a policy attached closer to the account takes precedence over one attached higher in the hierarchy.

After you enable the `GUARDDUTY_POLICY` policy type, the policy takes precedence over the Regional GuardDuty auto-enablement settings. The auto-enablement settings no longer apply, whether or not a policy is attached.

For the full inheritance rules and how the effective policy is resolved, see [Understanding management policy inheritance](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_inheritance_mgmt.html) in the AWS Organizations User Guide.

## How a policy affects GuardDuty account management
<a name="guardduty-organization-policies-effects"></a>

When a GuardDuty organization policy is active, the following changes apply to how you manage GuardDuty accounts:
+ After the `GUARDDUTY_POLICY` policy type is enabled, the Regional GuardDuty auto-enablement settings no longer apply, whether or not a policy is attached.
+ When a policy manages a protection plan, that protection plan can no longer be changed through the GuardDuty console or API for the covered accounts. On the **Accounts** page it appears as **Policy managed**. To change a managed protection plan, update the policy. Protection plans that the policy does not manage remain editable through the console and API.
+ Only the delegated administrator account can create and manage GuardDuty policies. The **Organization policies** page in the GuardDuty console is available only to the delegated administrator.

**Note**  
Attaching a GuardDuty policy can enroll new accounts as GuardDuty members and turn on protection plans across your organization. Enabling GuardDuty and its protection plans incurs charges. For more information, see [Pricing in GuardDuty](guardduty-pricing.md).

## Example use cases
<a name="guardduty-organization-policies-use-cases"></a>

The following examples show common ways to use a GuardDuty organization policy. For the policy JSON that implements each pattern, see [GuardDuty policies](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_guardduty.html) in the AWS Organizations User Guide.
+ **Enable a protection baseline across the entire organization.** Attach a policy at the organization root with a default configuration that enables the foundational detector and the protection plans you require. Every account, including accounts that join later, enables those features automatically.
+ **Vary protection by organizational unit.** Use a broad policy at the root for your baseline, and attach more specific policies to individual OUs to adjust the protection plans for accounts with different compliance or workload requirements.
+ **Maintain coverage as your organization grows.** Because accounts that join the organization or move into a covered OU inherit the effective policy, a policy keeps newly created accounts aligned with your protection baseline without manual enablement.