# Enabling Security Hub CSPM

There are two ways to enable AWS Security Hub CSPM, by integrating with AWS Organizations or manually.

We strongly recommend integrating with Organizations for multi-account and multi-Region environments.
If you have a standalone account, it's necessary to set up Security Hub CSPM manually.

## Verifying necessary permissions

After you sign up for Amazon Web Services (AWS), you must enable Security Hub CSPM to use its capabilities and features. To enable Security Hub CSPM, you first have to set up permissions that allow you to access the Security Hub CSPM
console and API operations. You or your AWS administrator can do this by using AWS Identity and Access Management (IAM) to attach the AWS
managed policy called `AWSSecurityHubFullAccess` to your IAM identity.

To enable and manage Security Hub CSPM through the Organizations integration, you also should attach the AWS managed
policy called `AWSSecurityHubOrganizationsAccess`.

For more information, see [AWS managed policies for Security Hub](security-iam-awsmanpol.md "security-iam-awsmanpol.md").

## Enabling Security Hub CSPM with Organizations integration

To start using Security Hub CSPM with AWS Organizations, the AWS Organizations management account for the organization designates an account
as the delegated Security Hub CSPM administrator account for the organization. Security Hub CSPM is automatically enabled in the delegated administrator
account in the current Region.

Choose your preferred method, and follow the steps to designate the delegated administrator.

Security Hub CSPM console

###### To designate the delegated Security Hub CSPM administrator when onboarding

1. Open the AWS Security Hub CSPM console at [https://console.aws.amazon.com/securityhub/](https://console.aws.amazon.com/securityhub/ "https://console.aws.amazon.com/securityhub/").
2. Choose **Go to Security Hub CSPM**. You're prompted to sign in to the
   Organizations management account.
3. On the **Designate delegated administrator** page, in the
   **Delegated administrator account** section, specify the delegated administrator
   account. We recommend choosing the same delegated administrator that you have set for other AWS
   security and compliance services.
4. Choose **Set delegated administrator**.

Security Hub CSPM API
Invoke the [`EnableOrganizationAdminAccount`](../../1.0/APIReference/API_EnableOrganizationAdminAccount.md "../../1.0/APIReference/API_EnableOrganizationAdminAccount.md") API from the Organizations management account. Provide the
AWS account ID of the Security Hub CSPM delegated administrator account.

AWS CLI
Run the [`enable-organization-admin-account`](../../../cli/latest/reference/securityhub/enable-organization-admin-account.md "../../../cli/latest/reference/securityhub/enable-organization-admin-account.md") command from the Organizations management account. Provide the
AWS account ID of the Security Hub CSPM delegated administrator account.

**Example command:**

```
aws securityhub enable-organization-admin-account --admin-account-id 777788889999
```

For more information about the integration with Organizations, see [Integrating Security Hub CSPM with AWS Organizations](designate-orgs-admin-account.md "designate-orgs-admin-account.md").

### Central configuration

When you integrate Security Hub CSPM and Organizations, you have the option to use a feature called [central configuration](central-configuration-intro.md "central-configuration-intro.md") to set up and manage Security Hub CSPM
for your organization. We strongly recommend using central configuration because it lets the administrator customize security coverage
for the organization. Where appropriate, the delegated administrator can allow a member account to configure its own security coverage settings.

Central configuration lets the delegated administrator configure Security Hub CSPM across accounts, OUs, and AWS Regions. The delegated
administrator configures Security Hub CSPM by creating configuration policies. Within a configuration policy, you can specify
the following settings:

- Whether Security Hub CSPM is enabled or disabled
- Which security standards are enabled and disabled
- Which security controls are enabled and disabled
- Whether to customize parameters for select controls

As the delegated
administrator, you can create a single configuration policy for your entire organization or different configuration policies for your various accounts and OUs.
For example, test accounts and production accounts can use different configuration policies.

Member accounts and OUs that use a configuration policy are _centrally managed_ and can be configured only by the delegated
administrator. The delegated administrator can designate specific member accounts and OUs as _self-managed_ to give
the member the ability to configure its own settings on a Region-by-Region basis.

If you don't use central configuration, you must largely configure Security Hub CSPM separately in each account and Region. This is called
[local configuration](local-configuration.md "local-configuration.md"). Under local configuration, the delegated administrator can automatically enable
Security Hub CSPM and a limited set of security standards in new organization accounts in the current Region. Local configuration doesn't apply to
existing organization accounts or to Regions other than the current Region. Local configuration also doesn't support the use of configuration policies.

## Enabling Security Hub CSPM manually

You must enable Security Hub CSPM manually if you have a standalone account, or
if you don't integrate with AWS Organizations. Standalone accounts can't integrate with AWS Organizations and must
use manual enablement.

When you enable Security Hub CSPM manually, you designate a Security Hub CSPM
administrator account and invite other accounts to become member accounts. The
administrator-member relationship is established when a prospective member account accepts
the invitation.

Choose your preferred method, and follow the steps to enable Security Hub CSPM. When you enable Security Hub CSPM from the console,
you also have the option to enable the supported security standards.

Security Hub CSPM console

1. Open the AWS Security Hub CSPM console at [https://console.aws.amazon.com/securityhub/](https://console.aws.amazon.com/securityhub/ "https://console.aws.amazon.com/securityhub/").
2. When you open the Security Hub CSPM console for the first time, choose
   **Go to Security Hub CSPM**.
3. On the welcome page, the **Security standards** section lists the
   security standards that Security Hub CSPM supports.

Select the check box for a standard to enable it, and clear the check box to disable it.

You can enable or disable a standard or its individual controls at any
time. For information about managing security standards,
see [Understanding security standards in Security Hub CSPM](standards-view-manage.md "standards-view-manage.md"). 4. Choose **Enable Security Hub**.

Security Hub CSPM API
Invoke the [`EnableSecurityHub`](../../1.0/APIReference/API_EnableSecurityHub.md "../../1.0/APIReference/API_EnableSecurityHub.md") API. When you enable
Security Hub CSPM from the API, it automatically enables the following default security
standards:

- AWS Foundational Security Best Practices
- Center for Internet Security (CIS) AWS Foundations Benchmark v1.2.0

If you do not want to enable these standards, then set
`EnableDefaultStandards` to `false`.

You can also use the `Tags` parameter to assign tag values to
the hub resource.

AWS CLI
Run
the [`enable-security-hub`](../../../cli/latest/reference/securityhub/enable-security-hub.md "../../../cli/latest/reference/securityhub/enable-security-hub.md") command. To enable the
default standards, include `--enable-default-standards`. To not
enable the default standards, include
`--no-enable-default-standards`. The default security standards are as follows:

- AWS Foundational Security Best Practices
- Center for Internet Security (CIS) AWS Foundations Benchmark v1.2.0

```
aws securityhub enable-security-hub [--tags `<tag values>`] [--enable-default-standards | --no-enable-default-standards]
```

**Example**

```
aws securityhub enable-security-hub --enable-default-standards --tags '{"Department": "Security"}'
```

### Multi-account enablement script

###### Note

Instead of this script, we recommend using central configuration to enable and
configure Security Hub CSPM across multiple accounts and Regions.

The [Security Hub CSPM multi-account enablement script in GitHub](https://github.com/awslabs/aws-securityhub-multiaccount-scripts "https://github.com/awslabs/aws-securityhub-multiaccount-scripts") allows you to enable
Security Hub CSPM across accounts and Regions. The script also automates the process of sending
invitations to member accounts and enabling AWS Config.

The script automatically enables AWS Config resource recording for all resources, including
global resources, in all Regions. It does not limit recording of global resources to
a single Region. To conserve costs, we recommend recording global resources in a single Region only. If
you use central configuration or cross-Region aggregation, this should be your home Region. For more information,
see [Recording resources in AWS Config](securityhub-setup-prereqs.md#config-resource-recording "securityhub-setup-prereqs.md#config-resource-recording").

There is a corresponding script to disable Security Hub CSPM across accounts and
Regions.

## Next steps: Posture management and integrations

After enabling Security Hub CSPM, we recommend enabling security standards and controls to monitor your security posture. After you enable controls, Security Hub CSPM begins running security checks and generating control
findings that help you detect misconfigurations in your AWS environment. To receive control findings, you must enable and
configure AWS Config for Security Hub CSPM. For more information, see [Enabling and configuring AWS Config for Security Hub CSPM](securityhub-setup-prereqs.md "securityhub-setup-prereqs.md").

After enabling Security Hub CSPM, you can also leverage integrations between Security Hub CSPM and other AWS services and third-party
solutions to see their findings in Security Hub CSPM. Security Hub CSPM aggregates findings from different sources and ingests them in a consistent format.
For more information, see [Understanding integrations in Security Hub CSPM](securityhub-findings-providers.md "securityhub-findings-providers.md").
