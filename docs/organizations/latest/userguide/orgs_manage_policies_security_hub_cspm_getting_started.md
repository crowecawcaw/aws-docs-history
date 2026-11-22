

# Getting started with Security Hub CSPM policies

Before you configure Security Hub CSPM policies, make sure that you understand the prerequisites and implementation requirements. This topic guides you through the process of setting up and managing these policies in your organization.

## Learn about required permissions
<a name="security_hub_cspm_getting_started-permissions"></a>

To enable and attach Security Hub CSPM policies, you need the following permissions in the management account:
+ `organizations:EnableAWSServiceAccess` for `securityhub.amazonaws.com`
+ `organizations:RegisterDelegatedAdministrator` for `securityhub.amazonaws.com`
+ `organizations:EnablePolicyType` for the `SECURITYHUB_CSPM_POLICY` policy type
+ `organizations:CreatePolicy`, `organizations:AttachPolicy`, and `organizations:DescribeEffectivePolicy`
+ `securityhub:EnableOrganizationAdminAccount` (to designate the delegated administrator)
+ `securityhub:EnableSecurityHub` (to create the Security Hub CSPM service-linked role in the management account)

## Prerequisites for Security Hub CSPM policies
<a name="security_hub_cspm_getting_started-before-begin"></a>

Review the following requirements before implementing Security Hub CSPM policies:
+ Your account must be part of an AWS Organizations organization
+ You must be signed in as either:
  + The management account for the organization
  + A delegated administrator account with permissions to manage Security Hub CSPM policies
+ You must enable trusted access for Security Hub CSPM in your organization
+ You must enable the Security Hub CSPM policy type in the root of your organization

Additionally, make sure that:
+ Security Hub CSPM is supported in the Regions where you want to apply policies.
+ AWS Config is enabled and recording resources in the accounts and Regions where you plan to enable Security Hub CSPM. Security Hub CSPM uses AWS Config rules to evaluate most controls. A Security Hub CSPM policy doesn't configure AWS Config.
+ You have the `AWSServiceRoleForSecurityHub` service-linked role configured in your management account or delegated administrator account. To make sure that this role exists, run `aws iam get-role --role-name AWSServiceRoleForSecurityHub`. If you need to create this role, you can either run `aws securityhub enable-security-hub` in any Region from your management account or delegated administrator account, or create it directly by running `aws iam create-service-linked-role --aws-service-name securityhub.amazonaws.com`.

**Note**  
If you use Security Hub CSPM central configuration, attaching your first Security Hub CSPM policy disables central configuration for the entire organization. For more information about moving from central configuration, see [Managing accounts using organization policies in Security Hub CSPM](https://docs.aws.amazon.com/securityhub/latest/userguide/accounts-orgs-policies.html) in the AWS Security Hub CSPM User Guide.

## Implementation steps
<a name="security_hub_cspm_getting_started-implementation"></a>

To implement Security Hub CSPM policies effectively, follow these steps in sequence. Each step ensures proper configuration and helps prevent common issues during setup. The management account or delegated administrator can perform these steps through the AWS Organizations console, AWS Command Line Interface (AWS CLI), or AWS SDKs.

1. [Enable trusted access for Security Hub CSPM](orgs_integrate_services.md#orgs_how-to-enable-disable-trusted-access).

1. (Recommended) Designate a delegated administrator for Security Hub CSPM, and attach a delegation policy that allows it to manage Security Hub CSPM policies.

1. [Enable Security Hub CSPM policies for your organization](enable-policy-type.md).

1. [Create a Security Hub CSPM policy](orgs_policies_create.md#create-security-hub-cspm-policy-procedure).

1. [Attach the Security Hub CSPM policy to your organization's root, OU, or account](orgs_policies_attach.md).

1. [View the combined effective Security Hub CSPM policy that applies to an account](orgs_manage_policies_effective.md).

For all of these steps, you sign in as an AWS Identity and Access Management (IAM) user, assume an IAM role, or sign in as the root user ([not recommended](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#lock-away-credentials)) in the organization's management account.

A delegated administrator can perform steps 4–6.

## Example: Get started by using the AWS CLI
<a name="security_hub_cspm_getting_started-cli-example"></a>

The following AWS CLI commands show the end-to-end flow from the management account. Replace `{{r-examplerootid111}}`, `{{p-examplepolicyid111}}`, and `{{111122223333}}` with your own values.

The following commands enable trusted access for Security Hub CSPM, enable the Security Hub CSPM policy type on the organization root, create a policy, and attach it to the organization root:

```bash
# 1. Enable trusted access for Security Hub CSPM.
aws organizations enable-aws-service-access \
    --service-principal securityhub.amazonaws.com

# 2. Enable the Security Hub CSPM policy type on the organization root.
aws organizations enable-policy-type \
    --root-id {{r-examplerootid111}} \
    --policy-type SECURITYHUB_CSPM_POLICY

# 3. Create a policy from a local JSON file.
aws organizations create-policy \
    --name "cspm-org-baseline" \
    --description "Security Hub CSPM baseline for all accounts" \
    --type SECURITYHUB_CSPM_POLICY \
    --content file://cspm-org-baseline.json

# 4. Attach the policy to the organization root.
aws organizations attach-policy \
    --policy-id {{p-examplepolicyid111}} \
    --target-id {{r-examplerootid111}}
```

The preceding commands use the following replaceable values:
+ `{{r-examplerootid111}}` – The ID of your organization root.
+ `{{p-examplepolicyid111}}` – The ID of the policy that the `create-policy` command returns.

Use the following command to view the effective policy for an account:

```bash
# 5. View the effective policy for an account.
aws organizations describe-effective-policy \
    --policy-type SECURITYHUB_CSPM_POLICY \
    --target-id {{111122223333}}
```

In the preceding command, replace `{{111122223333}}` with the ID of the member account whose effective policy you want to view.

You now have a Security Hub CSPM policy attached to your organization root. The policy applies to all accounts in your organization. To verify the configuration that applies to an account, run the `describe-effective-policy` command in the preceding example.

For the policy structure and example policies, see [Security Hub CSPM policy syntax and examples](orgs_manage_policies_security_hub_cspm_syntax.md).

### Clean up
<a name="security_hub_cspm_getting_started-cli-cleanup"></a>

If you no longer want the changes from this example, use the following commands to undo them in reverse order.

When you detach the policy, the accounts that it covered become self-managed, and the policy no longer configures Security Hub CSPM in those accounts. If you disable the policy type, AWS Organizations detaches all Security Hub CSPM policies from every target in the root. For more information, see [Detachment behavior](orgs_manage_policies_security_hub_cspm.md#security-hub-cspm-policies-detachment).

```bash
# 1. Detach the policy from the organization root.
aws organizations detach-policy \
    --policy-id {{p-examplepolicyid111}} \
    --target-id {{r-examplerootid111}}

# 2. Delete the policy.
aws organizations delete-policy \
    --policy-id {{p-examplepolicyid111}}

# 3. Disable the Security Hub CSPM policy type on the organization root.
aws organizations disable-policy-type \
    --root-id {{r-examplerootid111}} \
    --policy-type SECURITYHUB_CSPM_POLICY

# 4. Disable trusted access for Security Hub CSPM.
aws organizations disable-aws-service-access \
    --service-principal securityhub.amazonaws.com
```