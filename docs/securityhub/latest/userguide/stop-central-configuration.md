# Disabling central configuration in Security Hub CSPM

When you disable central configuration in AWS Security Hub CSPM, the delegated administrator loses the ability to configure Security Hub CSPM,
security standards, and security controls across multiple AWS accounts, organizational units (OUs), and AWS Regions.
Instead, you must configure most settings separately for each account in each Region.

###### Important

Before you can disable central configuration, you must first [disassociate your accounts and OUs](disassociate-policy.md "disassociate-policy.md") from their current configuration, whether that's
a configuration policy or self-managed behavior.

Before you can disable central configuration, you must also [delete existing configuration policies](delete-policy.md "delete-policy.md").

When you disable central configuration, the following changes occur:

- The delegated administrator can no longer create configuration policies for the organization.
- Accounts that had an applied or inherited configuration policy retain their current settings, but become self-managed.
- Your organization switches to _local configuration_. Under local configuration, the majority of Security Hub CSPM
  settings must be configured separately in each organization account and Region. The delegated administrator can choose to
  automatically enable Security Hub CSPM, [default security standards](securityhub-auto-enabled-standards.md "securityhub-auto-enabled-standards.md"), and all controls that are part of the default standards in new organization accounts. The default
  standards are AWS Foundational Security Best Practices (FSBP) and Center for Internet Security (CIS) AWS Foundations
  Benchmark v1.2.0. These settings take effect in the current Region only and impact new organization accounts only. The delegated administrator can't change which standards are default. Local
  configuration doesn't support the use of configuration policies or configuration at the OU level.
  The identity of the delegated administrator account remains the same when you stop using central configuration. Your home Region and linked Regions also
  remain the same (your home Region is now called the aggregation Region, and can be used for finding aggregation).

Choose your preferred method, and follow the steps to stop using central configuration and switch to local configuration.

Security Hub CSPM console

###### To disable central configuration (console)

1. Open the AWS Security Hub CSPM console at [https://console.aws.amazon.com/securityhub/](https://console.aws.amazon.com/securityhub/ "https://console.aws.amazon.com/securityhub/").

Sign in using the credentials of the delegated Security Hub CSPM administrator account in the home Region. 2. On the navigation pane, choose **Settings** and **Configuration**. 3. In the **Overview** section, choose **Edit**. 4. In the **Edit organization configuration** box, choose **Local configuration**.
If you haven't already, you're prompted to disassociate and delete your current configuration policies before you can stop central configuration. Accounts or OUs
that are designated as self-managed must be disassociated from their self-managed configuration. You can do this in the console by
[changing the management type](central-configuration-management-type.md#choose-management-type "central-configuration-management-type.md#choose-management-type") of each self-managed account or OU to **Centrally managed** and
**Inherit from my organization**. 5. Optionally, select the local configuration default settings for new organization accounts. 6. Choose **Confirm**.

Security Hub CSPM API

###### To disable central configuration (API)

1. Invoke the [UpdateOrganizationConfiguration](../../1.0/APIReference/API_UpdateOrganizationConfiguration.md "../../1.0/APIReference/API_UpdateOrganizationConfiguration.md") API.
2. Set the
   `ConfigurationType` field in the `OrganizationConfiguration` object to
   `LOCAL`.
   The API returns an error if you have existing configuration policies or policy associations. To disassociate a configuration policy, invoke the
   `StartConfigurationPolicyDisassociation` API. To delete a configuration policy, invoke the `DeleteConfigurationPolicy` API.
3. If you want to automatically enable Security Hub CSPM in new organization accounts, set the `AutoEnable` field to `true`.
   By default, the value of this field is `false`, and Security Hub CSPM isn't automatically enabled in new organization accounts. Optionally, if you want to automatically
   enable default security standards in new organization accounts, set the `AutoEnableStandards` field to `DEFAULT`. This the default value. If you don't
   want to automatically enable default security standards in new organization accounts, set the `AutoEnableStandards` field to `NONE`.

**Example API request:**

```
{
    "AutoEnable": true,
    "OrganizationConfiguration": {
        "ConfigurationType" : "LOCAL"
    }
}

```

AWS CLI

###### To disable central configuration (AWS CLI)

1. Run the [update-organization-configuration](../../../cli/latest/reference/securityhub/update-organization-configuration.md "../../../cli/latest/reference/securityhub/update-organization-configuration.md") command.
2. Set the
   `ConfigurationType` field in the `organization-configuration` object to
   `LOCAL`.
   The command returns an error if you have existing configuration policies or policy associations. To disassociate a configuration policy, run the
   `start-configuration-policy-disassociation` command. To delete a configuration policy, run the `delete-configuration-policy` command.
3. If you want to automatically enable Security Hub CSPM in new organization accounts, include the `auto-enable` parameter.
   By default, the value of this parameter is `no-auto-enable`, and Security Hub CSPM isn't automatically enabled in new organization accounts. Optionally, if you want to automatically
   enable default security standards in new organization accounts, set the `auto-enable-standards` field to `DEFAULT`. This the default value. If you don't
   want to automatically enable default security standards in new organization accounts, set the `auto-enable-standards` field to `NONE`.

```
aws securityhub --region us-east-1 update-organization-configuration \
--`auto-enable` \
--organization-configuration '{"ConfigurationType": "`LOCAL`"}'

```
