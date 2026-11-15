

# Declarative policies and central configuration in Security Hub CSPM
<a name="orgs-policies-and-central-config"></a>

With both AWS Security Hub CSPM declarative policies and Security Hub CSPM [central configuration](central-configuration-intro.md), a delegated administrator can configure Security Hub CSPM across an organization. The two mechanisms are mutually exclusive, so they can't apply conflicting configurations to the same accounts. Declarative policies are the recommended mechanism. This topic describes how the two interact and how to move from central configuration to declarative policies.

## How mutual exclusivity works
<a name="orgs-policies-first-attach"></a>

When a Security Hub CSPM declarative policy first governs an account in your organization, Security Hub CSPM disables central configuration for the entire organization. This happens even if the declarative policy governs only a single account. If you attach a declarative policy to an organizational unit (OU) that doesn't contain any accounts, central configuration remains enabled. When central configuration is disabled:
+ The organization configuration status, returned by [DescribeOrganizationConfiguration](https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_DescribeOrganizationConfiguration.html), is `DISABLED`, with a message that indicates that declarative policies are in use.
+ Your configuration policies and policy associations aren't deleted. Each association shows an `AssociationStatus` of `DISABLED` and is no longer applied.
+ Declarative policies configure the accounts that they govern.
+ Accounts that central configuration governed but that no declarative policy covers keep their current settings and become self-managed.
+ Security Hub CSPM records the change to central configuration as an AWS CloudTrail event.

**Warning**  
Because the change applies to the entire organization, attaching a narrow declarative policy, such as a test declarative policy on one account, replaces all of your central configuration governance. To move your full configuration without coverage gaps, use the [import tool](#orgs-policies-import-tool).

## Central configuration API behavior while disabled
<a name="orgs-policies-cc-api-behavior"></a>

While central configuration is disabled, the following API behavior applies:


| API operations | Behavior | 
| --- | --- | 
| `CreateConfigurationPolicy`, `UpdateConfigurationPolicy`, `StartConfigurationPolicyAssociation` | Denied with an error that states that central configuration is disabled. | 
| `GetConfigurationPolicy`, `ListConfigurationPolicies`, `GetConfigurationPolicyAssociation`, `BatchGetConfigurationPolicyAssociations`, `ListConfigurationPolicyAssociations` | Allowed. Associations return `DISABLED`. | 
| `DeleteConfigurationPolicy`, `StartConfigurationPolicyDisassociation` | Allowed, so that you can clean up central configuration resources. | 
| `UpdateFindingAggregator` | Allowed, so that you can adjust cross-Region aggregation. | 
| `UpdateOrganizationConfiguration` with `ConfigurationType` set to `CENTRAL` | Denied with a `ConflictException` while any Security Hub CSPM declarative policy is attached in the organization. | 
| Security Hub CSPM APIs for self-managed accounts | Not restricted by the central configuration status. | 

## Migrating your central configuration policies to AWS Organizations declarative policies by using the import tool
<a name="orgs-policies-import-tool"></a>

The Security Hub console provides an import tool that converts your central configuration setup to equivalent Security Hub CSPM declarative policies. Only the delegated administrator can use the tool. The tool is available only in the console and only while central configuration is enabled.

The import tool does the following:
+ Shows your current configuration policies and associations, and previews the equivalent Security Hub CSPM declarative policies.
+ Asks you to acknowledge that the resulting declarative policies become the source of truth for governed accounts and can overwrite existing member settings.
+ Creates a Security Hub CSPM declarative policy for each configuration policy, with the same description and tags. Each declarative policy name uses the format `{{ID}}_{{original-policy-name}}`, where {{ID}} is the central configuration policy ID and {{original-policy-name}} is the name of the central configuration policy. The maximum length of a declarative policy name is 128 characters, so the tool might truncate the name of your central configuration policy to fit this limit. If a declarative policy with that name exists, the tool overwrites it.
+ Attaches each declarative policy to the same targets as the original association. If a target is ungoverned, the tool attaches an ungoverned (empty) policy to that target. The tool also detaches Security Hub CSPM declarative policies from targets that your central configuration doesn't cover.
+ Preserves protections that central configuration provides. Central configuration doesn't disable Security Hub CSPM in the delegated administrator account, and it doesn't apply to invitation-based administrator accounts. Declarative policies don't make these exceptions, so the tool attaches a declarative policy that governs no Regions to these accounts. As a result, these accounts become self-managed.
+ Translates home Region behavior for controls that apply to global resources. If a central configuration policy enables controls for global resources, the tool enables those controls only in your Security Hub CSPM home Region. The tool expresses this behavior with Regional overrides, and in the declarative policy's default configuration, it disables all controls for global resources that belong to your enabled standards.

To migrate your central configuration policies to Security Hub CSPM declarative policies, use the import tool in the Security Hub console.

**To migrate central configuration policies by using the console**

1.  Sign in using your AWS account with your delegated administrator credentials. Open the Security Hub console at [https://console.aws.amazon.com/securityhub/v2/home](https://console.aws.amazon.com/securityhub/v2/home). 

1.  From the navigation pane, choose **Management**, and then choose **Configurations**. 

1.  In the **Import your Central Configuration policies** banner, choose **Import**. If the banner isn't shown, you don't have central configuration policies to import, and you can start using Security Hub CSPM declarative policies. 

1.  On the **Before you begin** page, review **What happens during import**. Under **Prerequisites**, confirm that all prerequisites are met. If a prerequisite isn't met, resolve the issue before you continue. Then, choose **Next**. 

1.  On the **Review existing policies** page, review the **Target Regions** and the central configuration policies that the tool will import. Then, choose **Next**. 

1.  On the **Review import plan** page, review the ungoverned policy assignments, the new declarative policy that applies to your home Region for each central configuration policy, and the post-import state. Then, select **I have reviewed the import plan**, and choose **Import**. 

    After you choose **Import**, a progress banner at the top of the page shows the status of the import. Keep the console page open until the import completes. When the import completes, the banner shows the results, including any errors. 

Until the import is complete, you can't create or edit Security Hub CSPM policies in the Security Hub console. You can view policies that the import tool has already created or attached.

For large organizations, the import can take several minutes because the tool attaches many declarative policies. Keep the console page open until the import completes. If you leave the page or your session expires, your declarative policy coverage can be smaller than your central configuration coverage was. In that case, the console prompts you to run the import again from the beginning.

After a successful import, the delegated administrator is self-managed if no central configuration policy is applied to it or if it inherits a policy where central configuration is disabled. All other accounts have the same configuration that central configuration applies.

If central configuration is disabled and your import isn't complete, Security Hub CSPM sends an AWS Health notification to the delegated administrator. To resolve the issue, run the import tool again or return to central configuration.

If you attach Security Hub CSPM declarative policies through the Organizations console, the AWS CLI, or an API before you run the import tool, the Security Hub console continues to show an import alert until you complete the import. We recommend that you use the import tool to implement declarative policies.

Consider the following after you migrate:
+ Declarative policies and cross-Region aggregation are configured independently. If a declarative policy enables Security Hub CSPM in a Region that isn't a linked Region in your cross-Region aggregation for Security Hub, the delegated administrator doesn't see findings from that Region. To see those findings, update your cross-Region aggregation configuration to include the Region.

  After central configuration is disabled, adding a linked Region to cross-Region aggregation doesn't enable Security Hub CSPM in that Region. For example, suppose that your declarative policies govern Regions A, B, and C after you migrate. If you later add Region D to cross-Region aggregation, you must also update your declarative policies to include Region D.
+ When a declarative policy governs a member account that isn't the delegated administrator for Security Hub CSPM, Security Hub CSPM removes any invitation-based administrator-member associations for that account and associates the member account with the delegated administrator. To restore the associations, revert the member account to self-managed, disassociate it from the delegated administrator, and then invite its members again.
+ If a declarative policy disables Security Hub CSPM in an account that's an invitation-based member, Security Hub CSPM removes the account's association with its administrator. To restore the association, enable Security Hub CSPM in the account and invite it again.

## Return to using central configuration over declarative policies
<a name="orgs-policies-return-to-cc"></a>

To return to central configuration, do the following:

1. Detach every Security Hub CSPM declarative policy from every target in your organization. You can do this from the AWS Organizations console or APIs. For more information, see [Detaching organization policies with AWS Organizations](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_policies_detach.html) in the *AWS Organizations User Guide*.

1. From the delegated administrator account, in your home Region, call [UpdateOrganizationConfiguration](https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_UpdateOrganizationConfiguration.html) with `ConfigurationType` set to `CENTRAL`, or turn on central configuration in the console.

When central configuration is enabled again, Security Hub CSPM reapplies your previous configuration policy associations. Each association moves from `DISABLED` to `PENDING`, and then to `SUCCESS` or `FAILED`. Allow time for your configuration to converge.

While central configuration is disabled, Security Hub CSPM doesn't create inherited associations for accounts that joined the organization or moved between OUs. Security Hub CSPM creates those associations after you return to central configuration. If you returned after using the import tool, you must run the import again to move back to declarative policies.

To turn off central configuration without moving to declarative policies, see [Disabling central configuration in Security Hub CSPM](stop-central-configuration.md).