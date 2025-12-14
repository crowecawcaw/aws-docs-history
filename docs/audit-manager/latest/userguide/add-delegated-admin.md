# Adding a delegated administrator

If you use AWS Organizations and want to enable multi-account support for AWS Audit Manager, you can
designate a member account in your organization as the delegated administrator for Audit Manager.

If you want to use Audit Manager in more than one AWS Region, you must designate a delegated
administrator account separately in each Region. In your Audit Manager settings, you should use
the same delegated administrator account across all Regions.

## Prerequisites

Take note of the following factors that define how the delegated administrator
operates in Audit Manager:

- Your account must be part of an organization.
- Before you designate a delegated administrator, you must [enable all features in your organization](../../../organizations/latest/userguide/orgs_manage_org_support-all-features.md "../../../organizations/latest/userguide/orgs_manage_org_support-all-features.md"). You must also [configure your organization's Security Hub CSPM settings](setup-recommendations.md#securityhub-recommendations "setup-recommendations.md#securityhub-recommendations"). This way, Audit Manager
  can collect Security Hub CSPM evidence from your member accounts.
- The delegated administrator account must have access on the KMS key that
  you provided when setting up Audit Manager.
- You can't use your AWS Organizations management account as a delegated
  administrator in Audit Manager.

## Procedure

You can add a delegated administrator using the Audit Manager console, the AWS Command Line Interface
(AWS CLI), or the Audit Manager API.

###### Note

After you add a delegated administrator in your Audit Manager settings, your management
account can no longer create additional assessments in Audit Manager. Additionally,
evidence collection stops for any existing assessments created by the management
account. Audit Manager collects and attaches evidence to the delegated administrator
account, which is the main account for managing your organization's
assessments.

Audit Manager console

###### To add a delegated administrator on the Audit Manager console

1. From the **General** settings tab, go to the
   **Delegated administrator** section.
2. Under **Delegated administrator account ID**,
   enter the account ID of the delegated administrator.
3. Choose **Delegate**.

AWS CLI

###### To add a delegated administrator in the AWS CLI

Run the [register-organization-admin-account](../../../cli/latest/reference/auditmanager/register-organization-admin-account.md "../../../cli/latest/reference/auditmanager/register-organization-admin-account.md") command and use the
`--admin-account-id` parameter to specify the account
ID of the delegated administrator.

In the following example, replace the `placeholder
 text` with your own information.

```
aws auditmanager register-organization-admin-account --admin-account-id `111122223333`
```

Audit Manager API

###### To add a delegated administrator using the API

Call the [RegisterOrganizationAdminAccount](../APIReference/API_RegisterOrganizationAdminAccount.md "../APIReference/API_RegisterOrganizationAdminAccount.md") operation and use the
[adminAccountId](../APIReference/API_RegisterOrganizationAdminAccount.md#auditmanager-RegisterOrganizationAdminAccount-request-adminAccountId "../APIReference/API_RegisterOrganizationAdminAccount.md#auditmanager-RegisterOrganizationAdminAccount-request-adminAccountId") parameter to specify the account ID of
the delegated administrator.

For more information, choose the previous links to read more in the
_Audit Manager API Reference_. This includes
information about how to use this operation and parameter in one of the
language-specific AWS SDKs.

## Next steps

To change your delegated administrator account, see [Changing a delegated administrator](change-delegated-admin.md "change-delegated-admin.md").

To remove your delegated administrator account, see [Removing a delegated administrator](remove-delegated-admin.md "remove-delegated-admin.md").

## Additional

resources

- [Creating and
  managing an organization](../../../organizations/latest/userguide/orgs_manage_org.md "../../../organizations/latest/userguide/orgs_manage_org.md")
- [Troubleshooting delegated administrator and
  AWS Organizations issues](delegated-admin-issues.md "delegated-admin-issues.md")
