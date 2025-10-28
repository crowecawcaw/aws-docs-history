# Integrating and configuring an organization in

Macie

To start using Amazon Macie with AWS Organizations, the AWS Organizations management account for the organization
designates an account as the delegated Macie administrator account for the organization. This enables
Macie as a trusted service in AWS Organizations. It also enables Macie in the current AWS Region
for the designated administrator account, and it allows the designated
administrator account to enable and manage Macie for other accounts in the organization
in that Region. For information about how these permissions are granted, see [Using AWS Organizations with other AWS services](../../../organizations/latest/userguide/orgs_integrate_services.md "../../../organizations/latest/userguide/orgs_integrate_services.md") in the _AWS Organizations User Guide_.

The delegated Macie administrator then configures the organization in Macie, primarily by adding the
organization’s accounts as Macie member accounts in the Region. The administrator can then
access certain Macie settings, data, and resources for those accounts in that Region. They
can also perform automated sensitive data discovery and run sensitive data discovery jobs to detect sensitive data
in Amazon Simple Storage Service (Amazon S3) buckets that the accounts own.

This topic explains how to designate a delegated Macie administrator for an organization and how to
add the organization's accounts as Macie member accounts. Before you perform these tasks,
ensure that you understand the [relationship
between Macie administrator and member accounts](accounts-mgmt-relationships.md "accounts-mgmt-relationships.md"). It’s also a good idea to review
the [considerations and recommendations](accounts-mgmt-ao-notes.md "accounts-mgmt-ao-notes.md") for
using Macie with AWS Organizations.

###### Tasks

- [Step 1:
  Verify your permissions](#accounts-mgmt-ao-admin-designate-permissions "#accounts-mgmt-ao-admin-designate-permissions")
- [Step 2: Designate the delegated
  Macie administrator account](#accounts-mgmt-ao-admin-designate "#accounts-mgmt-ao-admin-designate")
- [Step 3: Automatically
  enable and add new organization accounts](#accounts-mgmt-ao-members-autoenable "#accounts-mgmt-ao-members-autoenable")
- [Step 4: Enable and add
  existing organization accounts](#accounts-mgmt-ao-members-add-existing "#accounts-mgmt-ao-members-add-existing")
  To integrate and configure the organization in multiple Regions, the AWS Organizations management
  account and the delegated Macie administrator repeat these steps in each additional Region.

## Step 1: Verify your

permissions

Before you designate the delegated Macie administrator account for your organization, verify that
you (as a user of the AWS Organizations management account) are allowed to perform the following
Macie action: `macie2:EnableOrganizationAdminAccount`. This action allows you
to designate the delegated Macie administrator account for your organization by using Macie.

Also verify that you're allowed to perform the following AWS Organizations actions:

- `organizations:DescribeOrganization`
- `organizations:EnableAWSServiceAccess`
- `organizations:ListAWSServiceAccessForOrganization`
- `organizations:RegisterDelegatedAdministrator`

These actions allow you to: retrieve information about your organization; integrate
Macie with AWS Organizations; retrieve information about which AWS services you've integrated
with AWS Organizations; and, designate a delegated Macie administrator account for your organization.

To grant these permissions, include the following statement in an AWS Identity and Access Management (IAM)
policy for your account:

```
{
   "Sid": "Grant permissions to designate a delegated Macie administrator",
   "Effect": "Allow",
   "Action": [
      "macie2:EnableOrganizationAdminAccount",
      "organizations:DescribeOrganization",
      "organizations:EnableAWSServiceAccess",
      "organizations:ListAWSServiceAccessForOrganization",
      "organizations:RegisterDelegatedAdministrator"
   ],
   "Resource": "*"
}
```

If you want to designate your AWS Organizations management account as the delegated
Macie administrator account for the organization, your account also needs permission to perform the
following IAM action: `CreateServiceLinkedRole`. This action allows you to
enable Macie for the management account. However, based on AWS security best practices
and the principle of least privilege, we don't recommend that you do this.

If you decide to grant this permission, add the following statement to the IAM
policy for your AWS Organizations management account:

```
{
   "Sid": "Grant permissions to enable Macie",
   "Effect": "Allow",
   "Action": [
      "iam:CreateServiceLinkedRole"
   ],
   "Resource": "arn:aws:iam::`111122223333`:role/aws-service-role/macie.amazonaws.com/AWSServiceRoleForAmazonMacie",
   "Condition": {
      "StringLike": {
         "iam:AWSServiceName": "macie.amazonaws.com"
      }
   }
}
```

In the statement, replace `111122223333` with the
account ID for the management account.

If you want to administer Macie in an opt-in AWS Region (Region that's disabled by
default), also update the value for the Macie service principal in the
`Resource` element and the `iam:AWSServiceName` condition. The
value must specify the Region code for the Region. For example, to administer Macie in
the Middle East (Bahrain) Region, which has the Region code _me-south-1_, do the following:

- In the `Resource` element, replace

`arn:aws:iam::`111122223333`:role/aws-service-role/macie.amazonaws.com/AWSServiceRoleForAmazonMacie`

with

`arn:aws:iam::`111122223333`:role/aws-service-role/macie.`me-south-1`.amazonaws.com/AWSServiceRoleForAmazonMacie`

Where `111122223333` specifies the account ID for the
management account and `me-south-1` specifies the
Region code for the Region.

- In the `iam:AWSServiceName` condition, replace `macie.amazonaws.com`
  with `macie.`me-south-1`.amazonaws.com`,
  where `me-south-1` specifies the Region code for the
  Region.

For a list of Regions where Macie is currently available and the Region code for each one,
see [Amazon Macie endpoints and quotas](../../../general/latest/gr/macie.md "../../../general/latest/gr/macie.md") in the
_AWS General Reference_. To determine whether a Region is
an opt-in Region, see [Enable or disable
AWS Regions in your account](../../../accounts/latest/reference/manage-acct-regions.md "../../../accounts/latest/reference/manage-acct-regions.md") in the _AWS Account Management User
Guide_.

## Step 2: Designate the delegated

Macie administrator account for the organization

After you verify your permissions, you (as a user of the AWS Organizations management account) can
designate the delegated Macie administrator account for your organization.

###### To designate the delegated Macie administrator account for an organization

To designate the delegated Macie administrator account for your organization, you can use the
Amazon Macie console or the Amazon Macie API. Only a user of the AWS Organizations management account
can perform this task.

Console
Follow these steps to designate the delegated Macie administrator account by using the
Amazon Macie console.

###### To designate the delegated Macie administrator account

1. Sign in to the AWS Management Console using your AWS Organizations management account.
2. By using the AWS Region selector in the upper-right corner of the page, choose the Region in which you want to designate the delegated Macie administrator account for your
   organization.
3. Open the Amazon Macie console at [https://console.aws.amazon.com/macie/](https://console.aws.amazon.com/macie/ "https://console.aws.amazon.com/macie/").
4. Do one of the following, depending on whether Macie is enabled for your
   management account in the current Region:
   - If Macie isn’t enabled, choose **Get started** on
     the welcome page.
   - If Macie is enabled, choose **Settings** in the
     navigation pane.

5. Under **Delegated administrator**, enter the 12-digit
   account ID for the AWS account that you want to designate as the
   Macie administrator account.
6. Choose **Delegate**.

Repeat the preceding steps in each additional Region in which you want to
integrate your organization with Macie. You must designate the same
Macie administrator account in each of those Regions.

API
To designate the delegated Macie administrator account programmatically, use the [EnableOrganizationAdminAccount](../APIReference/admin.md "../APIReference/admin.md") operation of the Amazon Macie API. To
designate the account in multiple Regions, submit the designation for each Region
in which you want to integrate your organization with Macie. You must designate
the same Macie administrator account in each of those Regions.

When you submit the designation, use the required `adminAccountId`
parameter to specify the 12-digit account ID for the AWS account to designate as
the Macie administrator account for the organization. Also ensure that you specify the Region
that the designation applies to.

To designate the Macie administrator account by using the [AWS Command Line Interface (AWS CLI)](../../../cli/latest/userguide/cli-chap-welcome.md "../../../cli/latest/userguide/cli-chap-welcome.md"), run
the [enable-organization-admin-account](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/macie2/enable-organization-admin-account.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/macie2/enable-organization-admin-account.html") command. For the
`admin-account-id` parameter, specify the 12-digit account ID for
the AWS account to designate. Use the `region` parameter to specify
the Region that the designation applies to. For example:

```
`C:\>` `aws macie2 enable-organization-admin-account --region `us-east-1` --admin-account-id `111122223333``
```

Where `us-east-1` is the Region that the designation
applies to (the US East (N. Virginia) Region) and
`111122223333` is the account ID for the
account to designate.

After you designate the Macie administrator account for your organization, the Macie administrator can begin
configuring the organization in Macie.

## Step 3: Automatically enable and

add new organization accounts as Macie member accounts

By default, Macie isn’t automatically enabled for new accounts when the accounts are
added to your organization in AWS Organizations. In addition, the accounts aren’t automatically
added as Macie member accounts. The accounts appear in the Macie administrator's account
inventory. However, Macie isn't necessarily enabled for the accounts and the Macie administrator
can’t necessarily access Macie settings, data, and resources for the accounts.

If you’re the delegated Macie administrator for the organization, you can change this
configuration setting. You can turn on automatic enablement for your organization. If
you do this, Macie is automatically enabled for new accounts when the accounts are added
to your organization in AWS Organizations. In addition, the accounts are automatically associated
with your Macie administrator account as member accounts. Turning on this setting doesn't affect
existing accounts in your organization. To enable and manage Macie for existing
accounts, you must manually add the accounts as Macie member accounts. The [next step](#accounts-mgmt-ao-members-add-existing "#accounts-mgmt-ao-members-add-existing") explains how to do
this.

###### Note

If you turn on automatic enablement, note the following exception. If a new
account is already associated with a different Macie administrator account, Macie doesn’t
automatically add the account as a member account in your organization. The account
must disassociate from its current Macie administrator account before it can be part of your
organization in Macie. You can then manually add the account. To identify accounts
where this is the case, you can [review the
account inventory](accounts-mgmt-ao-review.md "accounts-mgmt-ao-review.md") for your organization.

###### To automatically enable and add new organization accounts as Macie member

accounts

To automatically enable and add new accounts as Macie member accounts, you can use
the Amazon Macie console or the Amazon Macie API. Only the delegated Macie administrator for the
organization can perform this task.

Console
To perform this task by using the console, you must be allowed to perform
the following AWS Organizations action: `organizations:ListAccounts`. This
action allows you to retrieve and display information about the accounts in
your organization. If you have these permissions, follow these steps to
automatically enable and add new organization accounts as Macie member
accounts.

###### To automatically enable and add new organization accounts

1. Open the Amazon Macie console at [https://console.aws.amazon.com/macie/](https://console.aws.amazon.com/macie/ "https://console.aws.amazon.com/macie/").
2. By using the AWS Region selector in the upper-right corner of the page, choose the Region in which you want to automatically enable and add new
   accounts as Macie member accounts.
3. In the navigation pane, choose
   **Accounts**.
4. On the **Accounts** page, in the **New
   accounts** section, choose
   **Edit**.
5. In the **Edit settings for new accounts** dialog
   box, select **Enable Macie**.

To also enable automated sensitive data discovery automatically for new member accounts,
select **Enable automated sensitive data discovery**. If you enable this
feature for an account, Macie continually selects sample objects
from the account's S3 buckets and analyzes the objects to determine
whether they contain sensitive data. For more information, see [Performing automated sensitive data
discovery](discovery-asdd.md "discovery-asdd.md"). 6. Choose **Save**.

Repeat the preceding steps in each additional Region in which you want to
configure your organization in Macie.

To subsequently change these settings, repeat the preceding steps and
clear the checkbox for each setting.

API
To automatically enable and add new Macie member accounts
programmatically, use the [UpdateOrganizationConfiguration](../APIReference/admin-configuration.md "../APIReference/admin-configuration.md") operation of the Amazon Macie API.
When you submit your request, set the value for the `autoEnable`
parameter to `true`. (The default value is `false`.)
Also ensure that you specify the Region that your request applies to. To
automatically enable and add new accounts in additional Regions, submit the
request for each additional Region.

If you use the AWS CLI to submit the request, run the [update-organization-configuration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/macie2/update-organization-configuration.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/macie2/update-organization-configuration.html") command and specify the
`auto-enable` parameter to enable and add new accounts
automatically. For example:

```
`$` `aws macie2 update-organization-configuration --region `us-east-1` --auto-enable`
```

Where `us-east-1` is the Region in which to
automatically enable and add new accounts, the US East (N. Virginia)
Region.

To subsequently change this setting and stop enabling and adding new
accounts automatically, run the same command again and use the
`no-auto-enable` parameter, instead of the
`auto-enable` parameter, in each applicable Region.

You can also enable automated sensitive data discovery automatically for new member accounts. If
you enable this feature for an account, Macie continually selects sample
objects from the account's S3 buckets and analyzes the objects to determine
whether they contain sensitive data. For more information, see [Performing automated sensitive data
discovery](discovery-asdd.md "discovery-asdd.md"). To
enable this feature automatically for member accounts, use the [UpdateAutomatedDiscoveryConfiguration](../APIReference/automated-discovery-configuration.md "../APIReference/automated-discovery-configuration.md") operation or, if you're
using the AWS CLI, run the [update-automated-discovery-configuration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/macie2/update-automated-discovery-configuration.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/macie2/update-automated-discovery-configuration.html") command.

## Step 4: Enable and add existing

organization accounts as Macie member accounts

When you integrate Macie with AWS Organizations, Macie isn’t automatically enabled for all the
existing accounts in your organization. In addition, the accounts aren’t automatically
associated with the delegated Macie administrator account as Macie member accounts. Therefore, the
final step of integrating and configuring your organization in Macie is to add existing
organization accounts as Macie member accounts. When you add an existing account as a
Macie member account, Macie is automatically enabled for the account and you (as the
delegated Macie administrator) gain access to certain Macie settings, data, and resources for
the account.

Note that you can’t add an account that’s currently associated with another
Macie administrator account. To add the account, work with the account owner to first disassociate
the account from its current administrator account. In addition, you can’t add an
existing account if Macie is currently suspended for the account. The account owner must
first re-enable Macie for the account. Finally, if you want to add the AWS Organizations
management account as a member account, a user of that account must first enable Macie
for the account.

###### To enable and add existing organization accounts as Macie member accounts

To enable and add existing organization accounts as Macie member accounts, you can use the
Amazon Macie console or the Amazon Macie API. Only the delegated Macie administrator for the
organization can perform this task.

Console
To perform this task by using the console, you must be allowed to perform
the following AWS Organizations action: `organizations:ListAccounts`. This
action allows you to retrieve and display information about the accounts in
your organization. If you have these permissions, follow these steps to
enable and add existing accounts as Macie member accounts.

###### To enable and add existing organization accounts

1. Open the Amazon Macie console at [https://console.aws.amazon.com/macie/](https://console.aws.amazon.com/macie/ "https://console.aws.amazon.com/macie/").
2. By using the AWS Region selector in the upper-right corner of the page, choose the Region in which you want to enable and add existing accounts
   as Macie member accounts.
3. In the navigation pane, choose **Accounts**. The
   **Accounts** page opens and displays a table of
   the accounts that are associated with your Macie account.

If an account is part of your organization in AWS Organizations, its
**Type** is **Via AWS Organizations**.
If an account is already a Macie member account, its
**Status** is **Enabled** or
**Paused (suspended)**. 4. In the **Existing accounts** table, select the checkbox for each
account that you want to add as a Macie member account. 5. On the **Actions** menu, choose **Add
member**. 6. Confirm that you want to add the selected accounts as member
accounts.

After you confirm the addition of the selected accounts, the status of the accounts
changes to **Enabling in process** and then
**Enabled**. After you add a member account, you can
also enable automated sensitive data discovery for the account: in the **Existing
accounts** table, select the checkbox for each account to
enable it for, and then choose **Enable automated sensitive data discovery** on the
**Actions** menu. If you enable this feature for an
account, Macie continually selects sample objects from the account's S3
buckets and analyzes the objects to determine whether they contain sensitive
data. For more information, see [Performing automated sensitive data
discovery](discovery-asdd.md "discovery-asdd.md").

Repeat the preceding steps in each additional Region in which you want to
configure your organization in Macie.

API
To programmatically enable and add one or more existing accounts as Macie
member accounts, use the [CreateMember](../APIReference/members.md "../APIReference/members.md")
operation of the Amazon Macie API. When you submit your request, use the
supported parameters to specify the 12-digit account ID and email address of
each AWS account to enable and add. Also specify the Region that the
request applies to. To enable and add existing accounts in additional
Regions, submit the request for each additional Region.

To retrieve the account ID and email address of an AWS account to enable and add, you
can optionally use the [ListMembers](../APIReference/members.md "../APIReference/members.md")
operation of the Amazon Macie API. This operation provides details about the
accounts that are associated with your Macie account, including accounts
that aren’t Macie member accounts. If the value for the
`relationshipStatus` property of an account isn’t
`Enabled` or `Paused`, the account isn’t a Macie
member account.

To enable and add one or more existing accounts by using the AWS CLI, run
the [create-member](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/macie2/create-member.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/macie2/create-member.html") command. Use the `region` parameter to
specify the Region in which to enable and add the accounts. Use the
`account` parameters to specify the account ID and email
address for each AWS account to add. For example:

```
`C:\>` `aws macie2 create-member --region `us-east-1` --account={\"accountId\":\"`123456789012`\",\"email\":\"`janedoe@example.com`\"}`
```

Where `us-east-1` is the Region in which to
enable and add the account as a Macie member account (the US East (N. Virginia)
Region), and the `account` parameters specify the account ID
(`123456789012`) and email address
(`janedoe@example.com`) for the account.

If your request succeeds, the status (`relationshipStatus`) of
the specified account changes to `Enabled` in your account
inventory.

To also enable automated sensitive data discovery for one or more of the accounts, use the [BatchUpdateAutomatedDiscoveryAccounts](../APIReference/automated-discovery-accounts.md "../APIReference/automated-discovery-accounts.md") operation or, if you're
using the AWS CLI, run the [batch-update-automated-discovery-accounts](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/macie2/batch-update-automated-discovery-accounts.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/macie2/batch-update-automated-discovery-accounts.html") command. If you
enable this feature for an account, Macie continually selects sample objects
from the account's S3 buckets and analyzes the objects to determine whether
they contain sensitive data. For more information, see [Performing automated sensitive data
discovery](discovery-asdd.md "discovery-asdd.md").
