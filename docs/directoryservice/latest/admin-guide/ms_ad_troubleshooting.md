# Troubleshooting AWS Managed Microsoft AD

The following can help you troubleshoot some common problems you might encounter when
creating or using your AWS Managed Microsoft AD Active Directory.

## Problems with your AWS Managed Microsoft AD

Some troubleshooting tasks can only be completed by Support. Here are some of the
tasks:

- Restarting your Directory Service-provided domain controllers.
- [Upgrading your AWS Managed Microsoft AD](ms_ad_upgrade_edition.md "ms_ad_upgrade_edition.md").

To create a support case, see [Creating support cases and case
management](../../../awssupport/latest/user/case-management.md "../../../awssupport/latest/user/case-management.md").

## Problems with Netlogon and secure channel

communications

As a mitigation against [CVE-2020-1472](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-1472 "https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-1472"), Microsoft has released patching which modifies the way that
Netlogon secure channel communications are processed by domain controllers. Since the
introduction of these secure Netlogon changes, some Netlogon connections (servers,
workstations, and trust validations) may not be accepted by your AWS Managed Microsoft AD.

To verify if your issue is related to Netlogon or secure channel communications,
search your Amazon CloudWatch Logs for event IDs 5827 (for device authentication related issues) or
5828 (for AD trust validation related issues). For information about CloudWatch in
AWS Managed Microsoft AD, see [Enabling Amazon CloudWatch Logs log forwarding for
AWS Managed Microsoft AD](ms_ad_enable_log_forwarding.md "ms_ad_enable_log_forwarding.md").

For more information about the mitigation against CVE-2020-1472, see [How to manage the changes in Netlogon secure channel connections associated with
CVE-2020-1472](https://support.microsoft.com/en-us/topic/how-to-manage-the-changes-in-netlogon-secure-channel-connections-associated-with-cve-2020-1472-f7e8cc17-0309-1d6a-304e-5ba73cd1a11e "https://support.microsoft.com/en-us/topic/how-to-manage-the-changes-in-netlogon-secure-channel-connections-associated-with-cve-2020-1472-f7e8cc17-0309-1d6a-304e-5ba73cd1a11e") on Microsoft 's website.

## You receive a 'Response Status: 400

Bad Request' error when attempting to reset a user's password

You receive an error message similar to the following when attempting to reset a
user's password:

`Response Status: 400 Bad Request`

You may experience this issue when there are duplicate objects in your AWS Managed Microsoft AD
Organizational Unit (OU) with identical user logon names. User logon names must be
unique. See [Troubleshooting Directory Data problems](<https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-2000-server/bb727059(v=technet.10)?redirectedfrom=MSDN> "https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-2000-server/bb727059(v=technet.10)?redirectedfrom=MSDN") in Microsoft documentation for more
information.

## Password recovery

If a user forgets a password or is having trouble signing in to your
AWS Managed Microsoft AD directory, you can reset their password using either the
AWS Management Console, PowerShell or the AWS CLI.

For more information, see [Resetting an AWS Managed Microsoft AD user password](ms_ad_manage_users_groups_reset_password.md "ms_ad_manage_users_groups_reset_password.md").

## Additional resources

The following resources can help you troubleshoot as you work with AWS.

- **[AWS Knowledge
  Center](https://aws.amazon.com/premiumsupport/knowledge-center/ "https://aws.amazon.com/premiumsupport/knowledge-center/")**–Find FAQs and links to other resources to
  help you troubleshoot issues.
- **[AWS Support
  Center](https://console.aws.amazon.com/support/home#/ "https://console.aws.amazon.com/support/home#/")**–Get technical support.
- **[AWS Premium Support
  Center](https://aws.amazon.com/premiumsupport/ "https://aws.amazon.com/premiumsupport/")**–Get premium technical support.

The following resources can help you troubleshoot common Active Directory issues.

- [Active Directory Documentation](https://learn.microsoft.com/en-us/troubleshoot/windows-server/active-directory/active-directory-overview "https://learn.microsoft.com/en-us/troubleshoot/windows-server/active-directory/active-directory-overview")
- [AD DS Troubleshooting](https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/manage/ad-ds-troubleshooting "https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/manage/ad-ds-troubleshooting")

###### Topics

- [Amazon EC2 Linux instance domain join errors](ms_ad_troubleshooting_join_linux.md "ms_ad_troubleshooting_join_linux.md")
- [AWS Managed Microsoft AD low available storage
  space](ms_ad_troubleshooting_low_storage_space.md "ms_ad_troubleshooting_low_storage_space.md")
- [Schema extension errors](ms_ad_troubleshooting_schema.md "ms_ad_troubleshooting_schema.md")
- [Trust creation status reasons](ms_ad_troubleshooting_trusts.md "ms_ad_troubleshooting_trusts.md")
