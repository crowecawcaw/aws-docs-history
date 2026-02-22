# Update the primary contact for your

AWS account

You can update the primary contact information associated with your account, including
your contact's full name, company name, mailing address, telephone number, and website
address.

You edit the primary account contact differently, depending
on whether or not the accounts are standalone, or part of an organization:

- **Standalone AWS accounts** – For
  AWS accounts not associated with an organization, you can update your own primary
  account contact using the AWS Management Console, or via AWS CLI & SDKs. To
  learn how to do this, see [Update standalone AWS account primary contact](#manage-acct-update-contact-primary-edit "#manage-acct-update-contact-primary-edit").
- **AWS accounts within an organization** –
  For member accounts that are part of an AWS organization, a user in the management
  account or delegated admin account can centrally update any member account in the
  organization from the AWS Organizations console, or programmatically via the AWS CLI &
  SDKs. To learn how to do this, see [Update AWS account primary
  contact in your organization](#manage-acct-update-contact-primary-orgs "#manage-acct-update-contact-primary-orgs").

###### Topics

- [Phone number and email
  address requirements](#manage-acct-update-contact-primary-requirements "#manage-acct-update-contact-primary-requirements")
- [Update the primary contact for
  a standalone AWS account or management account](#manage-acct-update-contact-primary-edit "#manage-acct-update-contact-primary-edit")
- [Update the primary contact for
  any AWS member account in your organization](#manage-acct-update-contact-primary-orgs "#manage-acct-update-contact-primary-orgs")

## Phone number and email

address requirements

Before you proceed with updating your account's primary contact information, we
recommend that you first review the following requirements when entering phone numbers
and email addresses.

- Phone numbers should only contain numbers.
- Phone numbers must start with a `+` and country code and must not
  have any leading zeros or additional spaces after the country code. For example,
  `+1` (US/Canada) or `+44` (UK).
- Phone numbers must not include whitespaces between
  the area code, exchange code, and local code. For example, +12025550179.
- For security purposes, phone numbers must be capable of receiving SMS from
  AWS. Toll free numbers will not be accepted since most don't support
  SMS.
- For business AWS accounts, it's a best practice to enter a company phone
  number and email address rather than one belonging to an individual. Configuring
  the accounts [root user](root-user.md "root-user.md") with an individual's
  email address or phone number can make your account difficult to recover if that
  individual leaves the company.

## Update the primary contact for

a standalone AWS account or management account

To edit your primary contact details for a standalone AWS account, perform the steps
in the following procedure. The AWS Management Console procedure below always works
_only_ in the standalone context. You can use the AWS Management Console to
access or change only the primary contact information of the account you used to call
the operation.

AWS Management Console

###### To edit your primary contact for a standalone

AWS account

###### Minimum permissions

To perform the following steps, you must have at least the following IAM permissions:

- `account:GetContactInformation` (to see the
  primary contact details)

- `account:PutContactInformation` (to update
  the primary contact details)

1. Sign in to
   the [AWS Management Console](https://console.aws.amazon.com/ "https://console.aws.amazon.com/") as an IAM user or role that has the minimum
   permissions.
2. Choose your account name on the top right of the window, and
   then choose **Account**.
3. Scroll down to the section **Contact
   information**, and next to it choose
   **Edit**.
4. Change the values in any of the available fields.
5. After you have made all of your changes, choose
   **Update**.

AWS CLI & SDKs
You can retrieve, update, or delete the **_primary_** contact
information by using the following AWS CLI commands or their AWS SDK
equivalent operations:

- [GetContactInformation](API_GetContactInformation.md "API_GetContactInformation.md")
- [PutContactInformation](API_PutContactInformation.md "API_PutContactInformation.md")

###### Notes

- To perform these operations from the management account or
  a delegated admin account in an organization against member
  accounts, you must [enable trusted access for the Account
  service](../../../organizations/latest/userguide/services-that-can-integrate-account.md#integrate-enable-ta-account "../../../organizations/latest/userguide/services-that-can-integrate-account.md#integrate-enable-ta-account").

###### Minimum permissions

For each operation, you must have the permission that maps to that
operation:

- `account:GetContactInformation`
- `account:PutContactInformation`
  If you use these individual permissions, you can grant some users
  the ability to only read the contact information, and grant others
  the ability to both read and write.

###### Example

The following example retrieves the current primary contact
information for the caller's account.

```
`$` `aws account get-contact-information``{
 "ContactInformation": {
 "AddressLine1": "123 Any Street",
 "City": "Seattle",
 "CompanyName": "Example Corp, Inc.",
 "CountryCode": "US",
 "DistrictOrCounty": "King",
 "FullName": "Saanvi Sarkar",
 "PhoneNumber": "+15555550100",
 "PostalCode": "98101",
 "StateOrRegion": "WA",
 "WebsiteUrl": "https://www.examplecorp.com"
 }
}`
```

###### Example

The following example sets new primary contact information for the
caller's account.

```
`$` `aws account put-contact-information --contact-information \
'{"AddressLine1": "123 Any Street", "City": "Seattle", "CompanyName": "Example Corp, Inc.", "CountryCode": "US", "DistrictOrCounty": "King",
"FullName": "Saanvi Sarkar", "PhoneNumber": "+15555550100", "PostalCode": "98101", "StateOrRegion": "WA", "WebsiteUrl": "https://www.examplecorp.com"}'`
```

This command produces no output if it's successful.

## Update the primary contact for

any AWS member account in your organization

To edit your primary contact details in any AWS member account in your organization,
perform the steps in the following procedure.

### Additional requirements

To update primary contact with the AWS Organizations console, you need to do some
preliminary settings:

- Your organization must enable _all features_ to manage settings on your
  member accounts. This allows admin control over the member accounts. This is
  set by default when you create your organization. If your organization is
  set to _consolidated billing_ only, and you want to enable all features, see
  [Enabling all features for an organization](../../../organizations/latest/userguide/orgs_manage_org_support-all-features.md "../../../organizations/latest/userguide/orgs_manage_org_support-all-features.md").
- You need to enable trusted access for the AWS Account Management service. To set this
  up, see [Enable trusted access for AWS Account Management](using-orgs-trusted-access.md "using-orgs-trusted-access.md").

AWS Management Console

###### To edit your primary contact for any AWS account in your

organization

1. Sign in to the [AWS Organizations console](https://console.aws.amazon.com/organizations/v2 "https://console.aws.amazon.com/organizations/v2") with the
   organization's management account credentials.
2. From **AWS accounts**,
   select the account that you want to update.
3. Choose **Contact info**, and
   locate **Primary
   contact**,
4. Select **Edit**.
5. Change the values in any of the available fields.
6. After you have made all of your changes, choose
   **Update**.

AWS CLI & SDKs
You can retrieve, update, or delete the **_primary_**
contact information by using the following AWS CLI commands or their
AWS SDK equivalent operations:

- [GetContactInformation](API_GetContactInformation.md "API_GetContactInformation.md")
- [PutContactInformation](API_PutContactInformation.md "API_PutContactInformation.md")

###### Notes

- To perform these operations from the management
  account or a delegated admin account in an organization
  against member accounts, you must [enable trusted access for the Account
  service](../../../organizations/latest/userguide/services-that-can-integrate-account.md#integrate-enable-ta-account "../../../organizations/latest/userguide/services-that-can-integrate-account.md#integrate-enable-ta-account").
- You can't access an account in a different
  organization from the one you're using to call the
  operation.

###### Minimum permissions

For each operation, you must have the permission that maps to
that operation:

- `account:GetContactInformation`
- `account:PutContactInformation`
  If you use these individual permissions, you can grant some
  users the ability to only read the contact information, and
  grant others the ability to both read and write.

###### Example

The following example retrieves the current primary contact
information for the specified member account in an organization.
The credentials used must be from either the organization's
management account, or from the Account Management's delegated
admin account.

```
`$` `aws account get-contact-information --account-id 123456789012``{
 "ContactInformation": {
 "AddressLine1": "123 Any Street",
 "City": "Seattle",
 "CompanyName": "Example Corp, Inc.",
 "CountryCode": "US",
 "DistrictOrCounty": "King",
 "FullName": "Saanvi Sarkar",
 "PhoneNumber": "+15555550100",
 "PostalCode": "98101",
 "StateOrRegion": "WA",
 "WebsiteUrl": "https://www.examplecorp.com"
 }
}`
```

###### Example

The following example sets the primary contact information for
the specified member account in an organization. The credentials
used must be from either the organization's management account,
or from the Account Management's delegated admin account.

```
`$` `aws account put-contact-information --account-id 123456789012 \
--contact-information '{"AddressLine1": "123 Any Street", "City": "Seattle", "CompanyName": "Example Corp, Inc.", "CountryCode": "US", "DistrictOrCounty": "King",
"FullName": "Saanvi Sarkar", "PhoneNumber": "+15555550100", "PostalCode": "98101", "StateOrRegion": "WA", "WebsiteUrl": "https://www.examplecorp.com"}'`
```

This command produces no output if it's successful.
