# Changing the Macie administrator account for an

organization

After an AWS Organizations organization is [integrated and
configured](accounts-mgmt-ao-integrate.md "accounts-mgmt-ao-integrate.md") in Amazon Macie, the AWS Organizations management account can designate a
different account as the delegated Macie administrator account for the organization. The new
Macie administrator can then configure the organization in Macie again.

As a user of the AWS Organizations management account for an organization, verify that you meet the
following permissions requirements before you designate a different Macie administrator account for
your organization:

- You must have the [same permissions](accounts-mgmt-ao-integrate.md#accounts-mgmt-ao-admin-designate-permissions "accounts-mgmt-ao-integrate.md#accounts-mgmt-ao-admin-designate-permissions") that were required to initially designate a
  Macie administrator account for your organization. You must also be allowed to perform the
  following AWS Organizations action:
  `organizations:DeregisterDelegatedAdministrator`. This additional
  action allows you to remove the current designation.
- If your account is currently a Macie member account, the current Macie administrator must
  remove your account as a Macie member account. Otherwise, you won't be allowed to
  access Macie operations for designating a different administrator account. After
  you designate a new administrator account, the new Macie administrator can add your
  account as a Macie member account again.
  If your organization uses Macie in multiple AWS Regions, also ensure that you change the
  designation in each Region in which your organization uses Macie. The delegated
  Macie administrator account must be the same in all of those Regions. If you manage multiple
  organizations in AWS Organizations, also note that an account can be the delegated Macie administrator account
  for only one organization at a time. To learn about additional requirements, see [Considerations for using Macie with
  AWS Organizations](accounts-mgmt-ao-notes.md "accounts-mgmt-ao-notes.md").

###### Note

When you designate a different Macie administrator account for your organization, you also disable
access to existing statistical data, inventory data, and other information that Macie
produced and directly provided while performing [automated sensitive data discovery](discovery-asdd.md "discovery-asdd.md") for accounts in the organization. The new Macie administrator can't
access the existing data. If you change the designation and the new Macie administrator enables
automated discovery for the accounts, Macie generates and maintains new data when it performs automated discovery
for the accounts.

###### To change the designation of a Macie administrator account

To designate a different Macie administrator account for your organization, you can use the
Amazon Macie console or a combination of the Amazon Macie and AWS Organizations APIs. Only a user of
the AWS Organizations management account can change the designation for their
organization.

Console
Follow these steps to change the designation by using the Amazon Macie console.

###### To change the designation

1. Sign in to the AWS Management Console by using your AWS Organizations management account.
2. By using the AWS Region selector in the upper-right corner of the page, choose the Region in which you want to change the designation.
3. Open the Amazon Macie console at [https://console.aws.amazon.com/macie/](https://console.aws.amazon.com/macie/ "https://console.aws.amazon.com/macie/").
4. Do one of the following, depending on whether Macie is enabled for
   your management account in the current Region:
   - If Macie isn’t enabled, choose **Get
     started** on the welcome page.
   - If Macie is enabled, choose **Settings** in
     the navigation pane.

5. Under **Delegated administrator**, choose
   **Remove**. To change the designation, you must
   first remove the current designation.
6. Confirm that you want to remove the current designation.
7. Under **Delegated administrator**, enter the 12-digit
   account ID for the AWS account to designate as the new
   Macie administrator account for the organization.
8. Choose **Delegate**.

Repeat the preceding steps in each additional Region in which you integrated
Macie with AWS Organizations.

API
To change the designation programmatically, you use two operations of the
Amazon Macie API and one operation of the AWS Organizations API. This is because you have to
remove the current designation in both Macie and AWS Organizations before you submit the
new designation.

To remove the current designation:

1. Use the [DisableOrganizationAdminAccount](../APIReference/admin.md "../APIReference/admin.md") operation of the Macie API.
   For the required `adminAccountId` parameter, specify the
   12-digit account ID for the AWS account that’s currently designated as
   the Macie administrator account for the organization.
2. Use the [DeregisterDelegatedAdministrator](../../../organizations/latest/APIReference/API_DeregisterDelegatedAdministrator.md "../../../organizations/latest/APIReference/API_DeregisterDelegatedAdministrator.md") operation of the AWS Organizations
   API. For the `AccountId` parameter, specify the 12-digit
   account ID for the account that’s currently designated as the
   Macie administrator account for the organization. This value should match the
   account ID that you specified in the preceding Macie request. For the
   `ServicePrincipal` parameter, specify the Macie service
   principal (`macie.amazonaws.com`).

After you remove the current designation, submit the new designation by using
the [EnableOrganizationAdminAccount](../APIReference/admin.md "../APIReference/admin.md") operation of the Macie API. For the
required `adminAccountId` parameter, specify the 12-digit account ID
for the AWS account to designate as the new Macie administrator account for the
organization.

To change the designation by using the AWS Command Line Interface (AWS CLI), run the [disable-organization-admin-account](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/macie2/disable-organization-admin-account.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/macie2/disable-organization-admin-account.html") command of the Macie API and the
[deregister-delegated-administrator](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/organizations/deregister-delegated-administrator.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/organizations/deregister-delegated-administrator.html") command of the AWS Organizations API.
These commands remove the current designation in Macie and AWS Organizations,
respectively. For the `admin-account-id` and `account-id`
parameters, specify the 12-digit account ID for the AWS account to remove as
the current Macie administrator account. Use the `region` parameter to specify
the Region that the removal applies to. For example:

```
`C:\>` `aws macie2 disable-organization-admin-account --region `us-east-1` --admin-account-id `111122223333` && aws organizations deregister-delegated-administrator --region `us-east-1` --account-id `111122223333` --service-principal macie.amazonaws.com`
```

Where:

- `us-east-1` is the Region that the removal
  applies to, the US East (N. Virginia) Region.
- `111122223333` is the account ID
  for the account to remove as the Macie administrator account.
- `macie.amazonaws.com` is the Macie service
  principal.

After you remove the current designation, submit the new designation by
running the [enable-organization-admin-account](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/macie2/enable-organization-admin-account.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/macie2/enable-organization-admin-account.html") command of the Macie API. For the
`admin-account-id` parameter, specify the 12-digit account ID for
the AWS account to designate as the new Macie administrator account for the organization.
Use the `region` parameter to specify the Region that the designation
applies to. For example:

```
`C:\>` `aws macie2 enable-organization-admin-account --region `us-east-1` --admin-account-id `444455556666``
```

Where `us-east-1` is the Region that the designation
applies to (the US East (N. Virginia) Region) and
`444455556666` is the account ID for the
account to designate as the new Macie administrator account.
