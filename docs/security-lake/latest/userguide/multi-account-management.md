# Managing multiple accounts with AWS Organizations in Security Lake

You can use Amazon Security Lake to collect security logs and events from multiple AWS accounts. To help automate and
streamline the management of multiple accounts, we strongly recommend that you integrate Security Lake with [AWS Organizations](../../../organizations/latest/userguide/orgs_introduction.md "../../../organizations/latest/userguide/orgs_introduction.md").

In Organizations, the
account that you use
to create the organization
is called the management account. To integrate Security Lake with Organizations, the management account
must designate a delegated Security Lake administrator account for the organization.

The delegated Security Lake administrator can enable Security Lake and configure Security Lake
settings for member accounts. The delegated administrator can collect logs and events across
the organization in all AWS Regions where Security Lake is enabled (regardless of which
Regional endpoint they're currently using). The delegated administrator can also configure
Security Lake to automatically collect log and event data for new organization accounts.

The delegated Security Lake administrator has access to log and event data for associated
member accounts. Accordingly, they can configure Security Lake to collect data owned by
associated member accounts. They can also grant subscribers permission to consume data owned
by associated member accounts.

To enable Security Lake for multiple accounts in an organization, the organization
management account must first designate a delegated Security Lake administrator account for the
organization. The delegated administrator can then enable and configure Security Lake for the
organization.

###### Important

Use Security Lake's [RegisterDataLakeDelegatedAdministrator](../APIReference/API_RegisterDataLakeDelegatedAdministrator.md "../APIReference/API_RegisterDataLakeDelegatedAdministrator.md")
API to allow Security Lake access to your organization and register Organizations's delegated administrator.

If you use Organizations' APIs to register a delegated administrator, service-linked roles for the Organizations might not be created successfully.
To ensure full functionality, use the Security Lake APIs.

For information about setting up Organizations, see [Creating and managing an
organization](../../../organizations/latest/userguide/orgs_manage_org.md "../../../organizations/latest/userguide/orgs_manage_org.md") in the _AWS Organizations User Guide_.

###### For existing Security Lake accounts

If you enabled Security Lake before April 17, 2025, we recommend you to enable the [Service-linked role (SLR) permissions for resource management](AWSServiceRoleForSecurityLakeResourceManagement.md "AWSServiceRoleForSecurityLakeResourceManagement.md"). By using this SLR, you can continue to perform
ongoing monitoring and performance improvements, that can potentially reduce latency and costs. For information about
the permissions associated with this SLR, see [Service-linked role (SLR) permissions for resource management](AWSServiceRoleForSecurityLakeResourceManagement.md "AWSServiceRoleForSecurityLakeResourceManagement.md").

If you use Security Lake console, you will receive a notification prompting you to enable
the AWSServiceRoleForSecurityLakeResourceManagement. If you use AWS CLI,
see [Creating the Security Lake
service-linked role](AWSServiceRoleForSecurityLakeResourceManagement.md#create-slr "AWSServiceRoleForSecurityLakeResourceManagement.md#create-slr").

## Important considerations for delegated Security Lake administrators

Take note of the following factors that define how a delegated administrator behaves in Security Lake:

**The delegated administrator is the same in all Regions.**

When you create the delegated administrator, it becomes the delegated administrator for every Region in which
you enable Security Lake.

**We recommend setting the Log Archive account as the Security Lake delegated administrator.**

The Log Archive account is an AWS account that is dedicated to ingesting and archiving all security-related
logs. Access to this account is typically limited to a few users, such as auditors and security teams for
compliance investigations. We recommend setting the Log Archive account as the Security Lake delegated
administrator so that you can view security-related logs and events with minimal context switching.

In addition, we recommend that only a minimal set of users have direct
access to the Log Archive account. Outside of this select group, if a user
needs access to the data that Security Lake collects, you can add them as a
Security Lake subscriber. For information about adding a subscriber, see [Subscriber management in Security Lake](subscriber-management.md "subscriber-management.md").

If you don't use the AWS Control Tower service, you may not have a Log Archive account. For more information
about the Log Archive account, see [Security OU – Log Archive account](../../../prescriptive-guidance/latest/security-reference-architecture/log-archive.md "../../../prescriptive-guidance/latest/security-reference-architecture/log-archive.md") in the _AWS Security Reference
Architecture_.

**An organization can have only one delegated administrator.**

You can have only one delegated Security Lake administrator for each organization.

**The organization management account cannot be the delegated administrator.**

Based on AWS Security best practices and the principle of least privilege, your organization management account cannot be the delegated administrator.

**The delegated administrator must be part of an active organization.**

When you delete an organization, the delegated administrator account can no longer manage Security Lake. You
must designate a delegated administrator from a different organization or use Security Lake with a standalone account
that's not part of an organization.

## IAM permissions required to designate the delegated administrator

When designating the delegated Security Lake administrator, you must have permissions to
enable Security Lake and use certain AWS Organizations API operations listed in the following policy
statement.

You can add the following statement to the end of an AWS Identity and Access Management (IAM) policy to grant
these
permissions.

```
{
    "Sid": "Grant permissions to designate a delegated Security Lake administrator",
    "Effect": "Allow",
    "Action": [
        "securitylake:RegisterDataLakeDelegatedAdministrator",
        "organizations:EnableAWSServiceAccess",
        "organizations:RegisterDelegatedAdministrator",
        "organizations:ListAccounts",
        "organizations:ListDelegatedAdministrators",
        "organizations:ListAWSServiceAccessForOrganization",
        "organizations:DescribeOrganizationalUnit",
        "organizations:DescribeAccount",
        "organizations:DescribeOrganization"
    ],
    "Resource": "*"
}
```

## Designating the delegated Security Lake administrator and adding member accounts

Choose your access method to designate the delegated Security Lake administrator account
for your organization. Only the organization management account can designate the
delegated administrator account for their organization. The organization
management account cannot be the delegated administrator account for their
organization.

###### Note

- The organization management account should use the Security Lake `RegisterDataLakeDelegatedAdministrator` operation
  to designate the delegated Security Lake administrator account. Designating the delegated Security Lake administrator through Organizations isn't supported.
- If you want to change the delegated administrator for the organization, you must first [remove the current delegated
  administrator](#remove-delegated-admin "#remove-delegated-admin"). You can then designate a new delegated
  administrator.

Console

1. Open the Security Lake console at [https://console.aws.amazon.com/securitylake/](https://console.aws.amazon.com/securitylake/ "https://console.aws.amazon.com/securitylake/").

Sign in using the credentials of the management account for your organization. 2. _ If Security Lake is not yet enabled, select **Get
Started**, and then designate the delegated Security Lake administrator on the **Enable
Security Lake** page.
_ If Security Lake is already enabled, designate the delegated Security Lake administrator on the **Settings**
page. 3. Under **Delegate administration to another
account**, enter the 12-digit AWS account ID of your Log Archive account.

We recommend using the Log Archive as delegated Security Lake administrator.
For more information, see [Important considerations for delegated Security Lake administrators](#delegated-admin-important "#delegated-admin-important"). 4. Choose **Delegate**. If Security Lake is not already
enabled, designating the delegated administrator will enable
Security Lake for that account in your current Region.

API
To designate the delegated administrator programmatically, use the [RegisterDataLakeDelegatedAdministrator](../APIReference/API_RegisterDataLakeDelegatedAdministrator.md "../APIReference/API_RegisterDataLakeDelegatedAdministrator.md") operation of the
Security Lake API. You must invoke the operation from the organization management account. If you're using
the AWS CLI, run the [register-data-lake-delegated-administrator](../../../cli/latest/reference/securitylake/register-data-lake-delegated-administrator.md "../../../cli/latest/reference/securitylake/register-data-lake-delegated-administrator.md") command from the organization management account. In your request, use the `accountId` parameter to
specify the 12-digit account ID of the AWS account to designate as the
delegated administrator account for the organization.

For example, the following AWS CLI command designates the delegated administrator. This example is formatted for Linux, macOS, or Unix, and it uses the backslash (\) line-continuation character to improve readability.

```
`$` `aws securitylake register-data-lake-delegated-administrator \
--account-id `123456789012``
```

The delegated administrator can also choose to automate the collection of
AWS log and event data for new organization accounts. With this
configuration, Security Lake is automatically enabled in new accounts when the
accounts are added to the organization in AWS Organizations. As the delegated
administrator, you can enable this configuration by using the [CreateDataLakeOrganizationConfiguration](../APIReference/API_CreateDataLakeOrganizationConfiguration.md "../APIReference/API_CreateDataLakeOrganizationConfiguration.md") operation of the
Security Lake API or, if you’re using the AWS CLI, by running the [create-data-lake-organization-configuration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securitylake/create-data-lake-organization-configuration.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securitylake/create-data-lake-organization-configuration.html") command. In your
request, you can also specify certain configuration settings for new
accounts.

For example, the following AWS CLI command automatically enables Security Lake and the collection of Amazon Route 53 resolver query logs, AWS Security Hub findings, and Amazon Virtual Private Cloud (Amazon VPC) Flow Logs in new organization accounts. This example is formatted for Linux, macOS, or Unix, and it uses the backslash (\) line-continuation character to improve readability.

```
`$` `aws securitylake create-data-lake-organization-configuration \
--auto-enable-new-account '[{"region":"`us-east-1`","sources":[{"sourceName":"`ROUTE53`"},{"sourceName":"`SH_FINDINGS`"},{"sourceName":"`VPC_FLOW`"}]}]'`
```

After the organization management account designates the delegated administrator, the
administrator can enable and configure Security Lake for the organization. This includes
enabling and configuring Security Lake to collect AWS log and event data for individual
accounts in the organization. For more information, see [Collecting data from AWS services in Security Lake](internal-sources.md "internal-sources.md").

You can use the [GetDataLakeOrganizationConfiguration](../APIReference/API_GetDataLakeOrganizationConfiguration.md "../APIReference/API_GetDataLakeOrganizationConfiguration.md")
operation to get details about your organization's current configuration for new member accounts.

## Editing auto-enable configuration for new organization accounts

A delegated Security Lake administrator can view and edit the auto-enable settings for
accounts when they join your organization. Security Lake ingests data based on these settings
for new accounts only, not existing accounts.

Use the following steps to edit the configuration for new organization accounts:

1. Open the Security Lake console at [https://console.aws.amazon.com/securitylake/](https://console.aws.amazon.com/securitylake/ "https://console.aws.amazon.com/securitylake/").
2. In the navigation pane, choose **Accounts**.
3. On the **Accounts** page, expand the **New account configuration**
   section. You can view which **Sources** Security Lake ingests
   from each **Region**.
4. Choose **Edit** to edit this configuration.
5. On the **Edit new account configuration** page, perform the following steps:
   1. For **Select Regions**, select one or more Regions for which you want to
      update the sources to ingest the data from. Then, choose **Next**.
   2. For **Select sources**, choose one of the following options
      for **Source selection**:
      1. **Ingest default AWS sources** – When
         you choose the recommended option, CloudTrail - S3 data events and AWS WAF are not included
         for ingestion by default. This is because ingesting high volume of both source types
         might significantly impact usage costs.
         To ingest these sources, first select the **Ingest specific
         AWS sources** option, and then select these sources from the
         **Log and event sources** list.
      2. **Ingest specific
         AWS sources** –
         With this option, you can select one or more log and event sources that you want to ingest.
      3. **Do not ingest any sources** –
         Select this option when you do not want to ingest any sources from the
         Regions that you selected in the previous step.
      4. Choose **Next**.###### Note

   When you enable Security Lake in an account for the first time, all the
   selected log and event sources will be a part of a 15-day free trial period. For more
   information about usage statistics, see
   [Reviewing usage and estimated costs](reviewing-usage-costs.md "reviewing-usage-costs.md"). 3. After you review the changes, choose **Apply**.

   When an AWS account joins your organization, these settings will apply to that account by default.

## Removing the delegated Security Lake administrator

Only the organization management account can remove the delegated Security Lake
administrator for their organization. If you want to change the delegated administrator
for the organization, remove the current delegated administrator, and then designate the
new delegated administrator.

###### Important

Removing the delegated Security Lake administrator deletes your data lake and disables
Security Lake for the accounts in your organization.

You can't change or remove the delegated
administrator by using the Security Lake console. These tasks can only be performed
programmatically.

To remove the delegated administrator programmatically, use the [DeregisterDataLakeDelegatedAdministrator](../APIReference/API_DeregisterDataLakeDelegatedAdministrator.md "../APIReference/API_DeregisterDataLakeDelegatedAdministrator.md") operation of the
Security Lake API. You must invoke the operation from the organization management account. The If you're using
the AWS CLI, run the [deregister-data-lake-delegated-administrator](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securitylake/deregister-data-lake-delegated-administrator.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securitylake/deregister-data-lake-delegated-administrator.html") command from the organization management account.

For example, the following AWS CLI command removes the delegated Security Lake administrator.

```
`$` `aws securitylake deregister-data-lake-delegated-administrator`
```

To keep the delegated administrator designation but change the
automatic configuration settings of new member accounts, use the [DeleteDataLakeOrganizationConfiguration](../APIReference/API_DeleteDataLakeOrganizationConfiguration.md "../APIReference/API_DeleteDataLakeOrganizationConfiguration.md") operation of the
Security Lake API, or, if you're using the AWS CLI, the [delete-data-lake-organization-configuration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securitylake/delete-data-lake-organization-configuration.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securitylake/delete-data-lake-organization-configuration.html") command. Only the delegated administrator can change these settings for
the organization.

For example, the following AWS CLI command stops the automatic collection of Security Hub findings from new member accounts that join the organization. New
member accounts won't contribute Security Hub findings to the data lake after the delegated administrator invokes this operation. This example is formatted for Linux, macOS, or Unix, and it uses the backslash (\) line-continuation character to improve readability.

```
`$` `aws securitylake delete-data-lake-organization-configuration \
--auto-enable-new-account '[{"region":"`us-east-1`","sources":[{"sourceName":"`SH_FINDINGS`"}]}]'`
```

## Security Lake trusted access

After you set up Security Lake for an organization, the AWS Organizations management account can
enable trusted access with Security Lake. Trusted access allows Security Lake to create an IAM
service-linked role and perform tasks in your organization and its accounts on your
behalf. For more information, see [Using AWS Organizations
with other AWS services](../../../organizations/latest/userguide/orgs_integrate_services.md "../../../organizations/latest/userguide/orgs_integrate_services.md") in the
_AWS Organizations User Guide_.

As a user of the organization management account, you can disable trusted access for Security Lake in AWS Organizations. For instructions on
disabling trusted access, see [How to enable or disable trusted access](../../../organizations/latest/userguide/orgs_integrate_services.md#orgs_how-to-enable-disable-trusted-access "../../../organizations/latest/userguide/orgs_integrate_services.md#orgs_how-to-enable-disable-trusted-access") in the _AWS Organizations User Guide_.

We recommend disabling trusted access if the delegated administrator's AWS account is suspended, isolated, or closed.
