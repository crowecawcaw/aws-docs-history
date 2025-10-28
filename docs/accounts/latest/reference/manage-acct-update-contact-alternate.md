# Update the alternate contacts for

your AWS account

Alternate contacts allows AWS to contact up to three alternate contacts associated with
the account. An alternate contact doesn't have to be a specific person. You could instead
add an email distribution list if you have a team that manages billing, operations and
security related issues. These are in addition to the email address associated with the
[root user](root-user.md "root-user.md") of the account. The [primary account contact](manage-acct-update-contact-primary.md "manage-acct-update-contact-primary.md") will
continue to receive all email communications sent to the root account’s email.

You can specify only one of each of the following contact types associated with an
account.

- Billing contact
- Operations contact
- Security contact
  You can add or edit alternate contacts differently, depending
  on whether or not the accounts are standalone, or part of an organization:

- **Standalone AWS accounts** – For
  AWS accounts not associated with an organization, you can update your own
  alternate contacts using the AWS Management Console, or via AWS CLI & SDKs.
  To learn how to do this, see [Update the alternate
  contacts for a standalone AWS account](#manage-acct-update-contact-alternate-edit "#manage-acct-update-contact-alternate-edit").
- **AWS accounts within an organization** –
  For member accounts that are part of an AWS organization, a user in the management
  account or delegated admin account can centrally update any member account in the
  organization from the AWS Organizations console, or programmatically via the AWS CLI &
  SDKs. To learn how to do this, see [Update the alternate
  contacts for any AWS account in your organization](#manage-acct-update-contact-alternate-orgs "#manage-acct-update-contact-alternate-orgs").

###### Topics

- [Phone number and
  email address requirements](#manage-acct-update-contact-alternate-requirements "#manage-acct-update-contact-alternate-requirements")
- [Update the alternate
  contacts for a standalone AWS account](#manage-acct-update-contact-alternate-edit "#manage-acct-update-contact-alternate-edit")
- [Update the alternate
  contacts for any AWS account in your organization](#manage-acct-update-contact-alternate-orgs "#manage-acct-update-contact-alternate-orgs")
- [account:AlternateContactTypes
  context key](#context-keys-AlternateContactTypes "#context-keys-AlternateContactTypes")

## Phone number and

email address requirements

Before you proceed with updating your account's alternate contacts information, we
recommend that you first review the following requirements when entering phone numbers
and email addresses.

- Phone numbers can only contain numbers, whitespaces and the following
  characters:"`+-()`".
- Email addresses can be up to 254 characters long and can include the following
  special characters in the local portion of the email address in addition to the
  standard alphanumeric ones: "`+=.#|!&-_`".

## Update the alternate

contacts for a standalone AWS account

To add or edit the alternate contacts for a standalone AWS account, perform the
steps in the following procedure. The AWS Management Console procedure below always works
_only_ in the standalone context. You can use the AWS Management Console to
access or change only the alternate contacts in the account you used to call the
operation.

AWS Management Console

###### To add or edit the alternate contacts for a standalone

AWS account

###### Minimum permissions

To perform the following steps, you must have at least the following IAM permissions:

- `account:GetAlternateContact` (to see the
  alternate contact details)

- `account:PutAlternateContact` (to set or
  update an alternate contact)

- `account:DeleteAlternateContact` (to delete
  an alternate contact)

1. Sign in to
   the [AWS Management Console](https://console.aws.amazon.com/ "https://console.aws.amazon.com/") as an IAM user or role that has the minimum
   permissions.
2. Choose your account name on the top right of the window, and
   then choose **Account**.
3. On the [**Account** page](https://console.aws.amazon.com/billing/home#/account "https://console.aws.amazon.com/billing/home#/account"), scroll down
   to **Alternate contacts**, and to the right of
   the title, choose **Edit**.

###### Note

If you don't see the **Edit** option, it
is likely that you are not signed in as the root user for your
account or as someone who has the minimum permissions
specified above. 4. Change the values in any of the available fields.

###### Important

For business AWS accounts, it's a best practice to enter
a company phone number and email address rather than one
belonging to an individual. 5. After you have made all of your changes, choose
**Update**.

AWS CLI & SDKs
You can retrieve, update, or delete the **_alternate_** contact
information by using the following AWS CLI commands or their AWS SDK
equivalent operations:

- [GetAlternateContact](API_GetAlternateContact.md "API_GetAlternateContact.md")
- [PutAlternateContact](API_PutAlternateContact.md "API_PutAlternateContact.md")
- [DeleteAlternateContact](API_GetAlternateContact.md "API_GetAlternateContact.md")

###### Notes

- To perform these operations from the management account or
  a delegated admin account in an organization against member
  accounts, you must [enable trusted access for the Account
  service](../../../organizations/latest/userguide/services-that-can-integrate-account.md#integrate-enable-ta-account "../../../organizations/latest/userguide/services-that-can-integrate-account.md#integrate-enable-ta-account").

###### Minimum permissions

For each operation, you must have the permission that maps to that
operation:

- `GetAlternateContact` (to see the alternate
  contact details)

- `PutAlternateContact` (to set or update an
  alternate contact)

- `DeleteAlternateContact` (to delete an
  alternate contact)
  If you use these individual permissions, you can grant some users
  the ability to only read the contact information, and grant others
  the ability to both read and write.

The following example retrieves the current Billing alternate
contact for the caller's account.

```
`$` `aws account get-alternate-contact \
 --alternate-contact-type=BILLING``{
 "AlternateContact": {
 "AlternateContactType": "BILLING",
 "EmailAddress": "saanvi.sarkar@amazon.com",
 "Name": "Saanvi Sarkar",
 "PhoneNumber": "+1(206)555-0123",
 "Title": "CFO"
 }
}`
```

The following example sets a new Operations alternate contact for
the caller's account.

```
`$` `aws account put-alternate-contact \
 --alternate-contact-type=OPERATIONS \
 --email-address=mateo_jackson@amazon.com \
 --name="Mateo Jackson" \
 --phone-number="+1(206)555-1234" \
 --title="Operations Manager"`
```

This command produces no output if it's successful.

###### Note

If you perform multiple `PutAlternateContact`
operations on the same AWS account and the same contact type,
the first adds the new contact, and all successive calls to the
same AWS account and contact type update the existing
contact.

The following example deletes the Security alternate contact for
the caller's account.

```
`$` `aws account delete-alternate-contact \
 --alternate-contact-type=SECURITY`
```

This command produces no output if it's successful.

###### Note

If you try to delete the same contact more than once, the
first succeeds silently. All later attempts generate a
`ResourceNotFound` exception.

## Update the alternate

contacts for any AWS account in your organization

To add or edit the alternate contact details for any AWS account in your
organization, perform the steps in the following procedure.

### Requirements

To update alternate contacts with the AWS Organizations console, you need to do some
preliminary settings:

- Your organization must enable _all features_ to manage settings on your
  member accounts. This allows admin control over the member accounts. This is
  set by default when you create your organization. If your organization is
  set to _consolidated billing_ only, and you want to enable all features, see
  [Enabling all features for an organization](../../../organizations/latest/userguide/orgs_manage_org_support-all-features.md "../../../organizations/latest/userguide/orgs_manage_org_support-all-features.md").
- You need to enable trusted access for the AWS Account Management service. To set this
  up, see [Enable trusted access for AWS Account Management](using-orgs-trusted-access.md "using-orgs-trusted-access.md").

###### Note

The AWS Organizations managed policies `AWSOrganizationsReadOnlyAccess` or
`AWSOrganizationsFullAccess` are updated to provide permission to
access the AWS Account Management APIs so you can access account data from the AWS Organizations
console. To view the updated managed policies, see [Updates to Organizations AWS managed policies](../../../organizations/latest/userguide/orgs_reference_available-policies.md#ref-iam-managed-policies-updates.html "../../../organizations/latest/userguide/orgs_reference_available-policies.md#ref-iam-managed-policies-updates.html").

AWS Management Console

###### To add or edit the alternate contacts for any AWS account in

your organization

1. Sign in to the [AWS Organizations console](https://console.aws.amazon.com/organizations/v2 "https://console.aws.amazon.com/organizations/v2") with the organization's management
   account credentials.
2. From **AWS accounts**, select
   the account that you want to update.
3. Choose **Contact info**, and
   under **Alternate contacts**,
   locate the type of contact: **Billing
   contact**, **Security
   contact**, or **Operations
   contact**.
4. To add a new contact, select **Add**, or to update an existing contact select
   **Edit**.
5. Change the values in any of the available fields.

###### Important

For business AWS accounts, it's a best practice to enter
a company phone number and email address rather than one
belonging to an individual. 6. After you have made all of your changes, choose
**Update**.

AWS CLI & SDKs
You can retrieve, update, or delete the **_alternate_** contact
information by using the following AWS CLI commands or their AWS SDK
equivalent operations:

- [GetAlternateContact](API_GetAlternateContact.md "API_GetAlternateContact.md")
- [PutAlternateContact](API_PutAlternateContact.md "API_PutAlternateContact.md")
- [DeleteAlternateContact](API_GetAlternateContact.md "API_GetAlternateContact.md")

###### Notes

- To perform these operations from the management account or
  a delegated admin account in an organization against member
  accounts, you must [enable trusted access for the Account
  service](../../../organizations/latest/userguide/services-that-can-integrate-account.md#integrate-enable-ta-account "../../../organizations/latest/userguide/services-that-can-integrate-account.md#integrate-enable-ta-account").
- You can't access an account in a different organization
  from the one you're using to call the operation.

###### Minimum permissions

For each operation, you must have the permission that maps to that
operation:

- `GetAlternateContact` (to see the alternate
  contact details)

- `PutAlternateContact` (to set or update an
  alternate contact)

- `DeleteAlternateContact` (to delete an
  alternate contact)
  If you use these individual permissions, you can grant some users
  the ability to only read the contact information, and grant others
  the ability to both read and write.

The following example retrieves the current Billing alternate
contact for the caller's account in an organization. The credentials
used must be from either the organization's management account, or
from the Account Management's delegated admin account.

```
`$` `aws account get-alternate-contact \
 --alternate-contact-type=BILLING \
 --account-id 123456789012``{
 "AlternateContact": {
 "AlternateContactType": "BILLING",
 "EmailAddress": "saanvi.sarkar@amazon.com",
 "Name": "Saanvi Sarkar",
 "PhoneNumber": "+1(206)555-0123",
 "Title": "CFO"
 }
}`
```

The following example sets the Operations alternate contact for
the specified member account in an organization. The credentials
used must be from either the organization's management account, or
from the Account Management's delegated admin account.

```
`$` `aws account put-alternate-contact \
 --account-id 123456789012 \
 --alternate-contact-type=OPERATIONS \
 --email-address=mateo_jackson@amazon.com \
 --name="Mateo Jackson" \
 --phone-number="+1(206)555-1234" \
 --title="Operations Manager"`
```

This command produces no output if it's successful.

###### Note

If you perform multiple `PutAlternateContact`
operations on the same AWS account and the same contact type,
the first adds the new contact, and all successive calls to the
same AWS account and contact type update the existing
contact.

The following example deletes the Security alternate contact for
the specified member account in an organization. The credentials
used must be from either the organization's management account, or
from the Account Management's delegated admin account.

```
`$` `aws account delete-alternate-contact \
 --account-id 123456789012 \
 --alternate-contact-type=SECURITY`
```

This command produces no output if it's successful.

###### Note

If you try to delete the same contact more than once, the first succeeds silently.
All later attempts generate a `ResourceNotFound` exception.

## account:AlternateContactTypes

context key

You can use the context key `account:AlternateContactTypes` to specify
which of the three billing types is allowed (or denied) by the IAM policy. For
example, the following example IAM permission policy uses this condition key to allow
the attached principals to retrieve, but not modify, only the `BILLING`
alternate contact for a specific account in an organization.

Because `account:AlternateContactTypes` is a multi-valued string type, you
must use the [`ForAnyValue` or `ForAllValues` multi-value string
operators](../../../IAM/latest/UserGuide/reference_policies_multi-value-conditions.md#reference_policies_multi-key-or-value-conditions "../../../IAM/latest/UserGuide/reference_policies_multi-value-conditions.md#reference_policies_multi-key-or-value-conditions").
