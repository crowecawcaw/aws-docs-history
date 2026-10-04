

# Update the primary contact for your AWS account
<a name="manage-acct-update-contact-primary"></a>

These instructions are for how to update the primary contact for your AWS account if you signed up for AWS using Sign up for AWS (advanced) or if you activated advanced features for your account. To compare sign-up options, see [Compare sign-up options](sign-up-for-aws.md).

You can update the primary contact information associated with your account, including your contact's full name, company name, mailing address, telephone number, and website address.

You can also verify the primary contact phone number. For more information, see [Verify the primary contact phone number](#manage-acct-update-contact-primary-verify).

You edit the primary account contact differently, depending on whether or not the accounts are standalone, or part of an organization:
+ **Standalone AWS accounts** – For AWS accounts not associated with an organization, you can update your own primary account contact using the AWS Management Console, or via AWS CLI & SDKs. To learn how to do this, see [Update standalone AWS account primary contact](#manage-acct-update-contact-primary-edit).
+ **AWS accounts within an organization** – For member accounts that are part of an AWS organization, a user in the management account or delegated admin account can centrally update any member account in the organization from the AWS Organizations console, or programmatically via the AWS CLI & SDKs. To learn how to do this, see [Update AWS account primary contact in your organization](#manage-acct-update-contact-primary-orgs).

**Topics**
+ [Phone number and email address requirements](#manage-acct-update-contact-primary-requirements)
+ [Update the primary contact for a standalone AWS account or management account](#manage-acct-update-contact-primary-edit)
+ [Update the primary contact for any AWS member account in your organization](#manage-acct-update-contact-primary-orgs)
+ [Verify the primary contact phone number](#manage-acct-update-contact-primary-verify)

## Phone number and email address requirements
<a name="manage-acct-update-contact-primary-requirements"></a>

Before you proceed with updating your account's primary contact information, we recommend that you first review the following requirements when entering phone numbers and email addresses.
+ Phone numbers should only contain numbers.
+ Phone numbers must start with a `+` and country code and must not have any leading zeros or additional spaces after the country code. For example, `+1` (US/Canada) or `+44` (UK).
+ Phone numbers must not include whitespaces between the area code, exchange code, and local code. For example, \+12025550179.
+ For security purposes, phone numbers must be capable of receiving SMS from AWS. Toll free numbers will not be accepted since most don't support SMS.
+ For business AWS accounts, it's a best practice to enter a company phone number and email address rather than one belonging to an individual. Configuring the account's [root user](root-user.md) with an individual's email address or phone number can make your account difficult to recover if that individual leaves the company.

## Update the primary contact for a standalone AWS account or management account
<a name="manage-acct-update-contact-primary-edit"></a>

To edit your primary contact details for a standalone AWS account or a management account, perform the steps in the following procedure. The following AWS Management Console procedure always works *only* in the standalone context. You can use the AWS Management Console to access or change only the primary contact information of the account you used to call the operation.

------
#### [ AWS Management Console ]

**To edit your primary contact for a standalone AWS account or management account**
**Minimum permissions**  
To perform the following steps, you must have at least the following IAM permissions:  
`account:GetContactInformation` (to see the primary contact details)
`account:PutContactInformation` (to update the primary contact details)

1. Sign in to the [AWS Management Console](https://console.aws.amazon.com/) as an IAM user or role that has the minimum permissions.

1. Choose your account name on the top right of the window, and then choose **Account**.

1. Scroll down to the section **Contact information**, and next to it choose **Edit**.

1. Change the values in any of the available fields.

1. After you have made all of your changes, choose **Update**.

------
#### [ AWS CLI & SDKs ]

You can retrieve, update, or delete the ***primary*** contact information by using the following AWS CLI commands or their AWS SDK equivalent operations:
+ [GetContactInformation](https://docs.aws.amazon.com/accounts/latest/APIReference/API_GetContactInformation.html)
+ [PutContactInformation](https://docs.aws.amazon.com/accounts/latest/APIReference/API_PutContactInformation.html)

**Notes**  
To perform these operations from the management account or a delegated admin account in an organization against member accounts, you must [enable trusted access for the Account service](https://docs.aws.amazon.com/organizations/latest/userguide/services-that-can-integrate-account.html#integrate-enable-ta-account).

**Minimum permissions**  
For each operation, you must have the permission that maps to that operation:  
`account:GetContactInformation`
`account:PutContactInformation`
If you use these individual permissions, you can grant some users the ability to only read the contact information, and grant others the ability to both read and write.

**Example**  
The following example retrieves the current primary contact information for the caller's account.  

```
$ aws account get-contact-information
{
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
}
```

**Example**  
The following example sets new primary contact information for the caller's account.  

```
$ aws account put-contact-information --contact-information \
'{"AddressLine1": "123 Any Street", "City": "Seattle", "CompanyName": "Example Corp, Inc.", "CountryCode": "US", "DistrictOrCounty": "King", 
"FullName": "Saanvi Sarkar", "PhoneNumber": "+15555550100", "PostalCode": "98101", "StateOrRegion": "WA", "WebsiteUrl": "https://www.examplecorp.com"}'
```
This command produces no output if it's successful.

------

## Update the primary contact for any AWS member account in your organization
<a name="manage-acct-update-contact-primary-orgs"></a>

To edit your primary contact details in any AWS member account in your organization, perform the steps in the following procedure. 

### Additional requirements
<a name="update-primary-contact-requirement"></a>

To update primary contact with the AWS Organizations console, you need to do some preliminary settings:
+ Your organization must enable *all features* to manage settings on your member accounts. This allows admin control over the member accounts. This is set by default when you create your organization. If your organization is set to *consolidated billing* only, and you want to enable all features, see [Enabling all features for an organization](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_org_support-all-features.html).
+ You need to enable trusted access for the AWS Account Management service. To set this up, see [Enable trusted access for AWS Account Management](using-orgs-trusted-access.md).

------
#### [ AWS Management Console ]

**To edit your primary contact for any AWS account in your organization**

1. Sign in to the [AWS Organizations console](https://console.aws.amazon.com/organizations/v2) with the organization's management account credentials.

1. From **AWS accounts**, select the account that you want to update.

1. Choose **Contact info**, and locate **Primary contact**.

1. Select **Edit**.

1. Change the values in any of the available fields.

1. After you have made all of your changes, choose **Save**.

If you change the phone number, we send a verification code to the new number when you choose **Save**. You can verify the number immediately or later. For more information, see [Verify the phone number for a member account in your organization](#manage-acct-update-contact-primary-verify-orgs).

------
#### [ AWS CLI & SDKs ]

You can retrieve, update, or delete the ***primary*** contact information by using the following AWS CLI commands or their AWS SDK equivalent operations:
+ [GetContactInformation](https://docs.aws.amazon.com/accounts/latest/APIReference/API_GetContactInformation.html)
+ [PutContactInformation](https://docs.aws.amazon.com/accounts/latest/APIReference/API_PutContactInformation.html)

**Notes**  
To perform these operations from the management account or a delegated admin account in an organization against member accounts, you must [enable trusted access for the Account service](https://docs.aws.amazon.com/organizations/latest/userguide/services-that-can-integrate-account.html#integrate-enable-ta-account).
You can't access an account in a different organization from the one you are using to call the operation.

**Minimum permissions**  
For each operation, you must have the permission that maps to that operation:  
`account:GetContactInformation`
`account:PutContactInformation`
If you use these individual permissions, you can grant some users the ability to only read the contact information, and grant others the ability to both read and write.

**Example**  
The following example retrieves the current primary contact information for the specified member account in an organization. The credentials used must be from either the organization's management account, or from the Account Management's delegated admin account.  

```
$ aws account get-contact-information --account-id 123456789012
{
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
}
```

**Example**  
The following example sets the primary contact information for the specified member account in an organization. The credentials used must be from either the organization's management account, or from the Account Management's delegated admin account.  

```
$ aws account put-contact-information --account-id 123456789012 \
--contact-information '{"AddressLine1": "123 Any Street", "City": "Seattle", "CompanyName": "Example Corp, Inc.", "CountryCode": "US", "DistrictOrCounty": "King", 
"FullName": "Saanvi Sarkar", "PhoneNumber": "+15555550100", "PostalCode": "98101", "StateOrRegion": "WA", "WebsiteUrl": "https://www.examplecorp.com"}'
```
This command produces no output if it's successful.

------

## Verify the primary contact phone number
<a name="manage-acct-update-contact-primary-verify"></a>

You can verify the phone number in the primary contact information for an AWS account. Verifying confirms that the phone number on file can receive SMS text messages from us.

When you start verification, we send a 6-digit verification code by SMS text message to the phone number that's currently on file for the account. You don't enter a phone number to start verification. To finish, you enter the code before it expires.

Keep the following in mind when you verify a phone number:
+ The code expires 5 minutes after we send it.
+ If you request a new code, codes that we sent earlier no longer work.
+ If the code is incorrect or has expired, request a new code and try again.
+ If the phone number changes after we send a code, you can't use that code. Request a new code for the current number.
+ The verification status always describes the phone number that's currently on file. If you change the phone number, the status describes the new number.
+ For a member account in an organization, the code goes to the member account's primary contact phone number, not to yours. Before you start, make sure that you can get the code from whoever has that phone.

To check the verification status, use the [GetContactInformation](https://docs.aws.amazon.com/accounts/latest/APIReference/API_GetContactInformation.html) operation. The `VerificationStatus` field in the response has one of the following values:
+ `VERIFIED` – The phone number on file is verified.
+ `UNVERIFIED` – The phone number on file isn't verified.
+ `NOT_SUPPORTED` – Phone number verification isn't available for this account.

### Verify the phone number for a standalone or management AWS account
<a name="manage-acct-update-contact-primary-verify-standalone"></a>

To verify the phone number of the account whose credentials you use, use the following AWS CLI commands or their AWS SDK equivalent operations:
+ [SendPhoneNumberVerification](https://docs.aws.amazon.com/accounts/latest/APIReference/API_SendPhoneNumberVerification.html)
+ [VerifyPhoneNumber](https://docs.aws.amazon.com/accounts/latest/APIReference/API_VerifyPhoneNumber.html)

**Minimum permissions**  
For each operation, you must have the permission that maps to that operation:  
`account:SendPhoneNumberVerification`
`account:VerifyPhoneNumber`
To check the verification status, you also need `account:GetContactInformation`.

**Example**  
The following AWS CLI example sends a verification code to the primary contact phone number of the caller's account:  

```
$ aws account send-phone-number-verification
{
    "Status": "PENDING"
}
```

**Example**  
The following AWS CLI example submits the code to finish verification:  

```
$ aws account verify-phone-number --otp 123456
{
    "Status": "VERIFIED"
}
```

**Example**  
The following AWS CLI example retrieves the verification status of the caller's primary contact phone number:  

```
$ aws account get-contact-information --query VerificationStatus
"VERIFIED"
```

### Verify the phone number for a member account in your organization
<a name="manage-acct-update-contact-primary-verify-orgs"></a>

You can verify the phone number of a member account by using the AWS Organizations console, the AWS CLI, or an AWS SDK. Before you start, complete the steps in [Additional requirements](#update-primary-contact-requirement).

------
#### [ AWS Management Console ]

**To verify the primary contact phone number for a member account**
**Minimum permissions**  
To perform the following steps, you must have at least the following IAM permissions:  
`account:GetContactInformation` (to see the phone number and whether it's verified)
`account:SendPhoneNumberVerification` (to send a verification code)
`account:VerifyPhoneNumber` (to submit the code)
The `AWSOrganizationsFullAccess` managed policy doesn't include `account:SendPhoneNumberVerification` or `account:VerifyPhoneNumber`. If you rely on that policy, grant these permissions separately.

1. Sign in to the [AWS Organizations console](https://console.aws.amazon.com/organizations/v2) with the organization's management account credentials.

1. From **AWS accounts**, select the member account.

1. Choose **Contact info**, and locate **Primary contact**.

1. If the phone number isn't verified, it appears with a warning. Choose the phone number, and then choose **Verify phone number**. We send a 6-digit code to the member account's phone number.

1. Enter the code in **Verification code**, and then choose **Verify**.

   If the code doesn't arrive, choose **Resend code** when that option becomes available.

------
#### [ AWS CLI & SDKs ]

To verify a member account's phone number, use the following AWS CLI commands or their AWS SDK equivalent operations, and specify the member account ID:
+ [SendPhoneNumberVerification](https://docs.aws.amazon.com/accounts/latest/APIReference/API_SendPhoneNumberVerification.html)
+ [VerifyPhoneNumber](https://docs.aws.amazon.com/accounts/latest/APIReference/API_VerifyPhoneNumber.html)

**Notes**  
The credentials that you use must be from either the organization's management account or the delegated admin account for AWS Account Management.
You can't access an account in a different organization from the one you are using to call the operation.

**Minimum permissions**  
For each operation, you must have the permission that maps to that operation:  
`account:SendPhoneNumberVerification`
`account:VerifyPhoneNumber`
To check the verification status, you also need `account:GetContactInformation`.

**Example**  
The following AWS CLI example sends a verification code to the primary contact phone number of the specified member account:  

```
$ aws account send-phone-number-verification --account-id 123456789012
{
    "Status": "PENDING"
}
```

**Example**  
The following AWS CLI example submits the code that we sent to the member account's phone number:  

```
$ aws account verify-phone-number --account-id 123456789012 --otp 123456
{
    "Status": "VERIFIED"
}
```

------