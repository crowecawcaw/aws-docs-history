# Export details for all accounts in

AWS Organizations

With AWS Organizations, management account users and delegated administrators for an organization
can export a .csv file with all account details within an organization. As a result,
organization administrators can easily view accounts and filter by state:
`PENDING_ACTIVATION`, `ACTIVE`, `SUSPENDED`,
`PENDING_CLOSURE`, or `CLOSED`. If your organization has many
accounts, the .csv file download option provides an easy way to view and sort account
details in a spreadsheet. We recommend generating new CSV exports rather than using
previously saved versions to maintain current account information.

###### Important

We retired the account `Status` parameter in the `Accounts`
object from the AWS Organizations console on September 9, 2025. The account export file will now
display the `State` parameter instead of the `Status` parameter.
Any downstream processes using the exported file
`Organization_accounts_information.csv` should be updated to use
the `State` parameter instead of `Status`.

###### Note

Only principals in the management account can download the account list.

## Export a list of all AWS accounts in

your organization

When you sign in to the organization's management account, you can get a list of all
accounts that are part of your organization as a .csv file. The list contains individual
account details; however, it doesn't specify to which organizational unit (OU) the
account belongs.

The .csv file contains the following information for each account:

- **Account ID** - Numeric account identifier. For
  example: 123456789012
- **ARN** - Amazon Resource Name for the account.
  For example:
  `arn:aws:organizations::123456789012account/o-o1gb0d1234/123456789012`
- **Email** - Email address associated with the
  account. For example: marymajor@example.com
- **Name** - Account name provided by account
  creator. For example: stage testing account
- **Status** - Account status within the
  organization. Value can be `PENDING`, `ACTIVE` or
  `SUSPENDED`.
- **State** - Operational account state within the
  organization. Value can be `PENDING_ACTIVATION`, `ACTIVE`,
  `SUSPENDED`, `PENDING_CLOSURE`, or
  `CLOSED`.
- **Joined method** - Specifies how the account was
  created. Value can be `INVITED` or `CREATED`.
- **Joined timestamp** - Date and time the account
  joined the organization.

###### Minimum permissions

To export a .csv file with all member accounts in your organization, you must have
the following permissions:

- `organizations:DescribeOrganization`
- `organizations:ListAccounts`

AWS Management Console

###### To export a .csv file for all AWS accounts in your

organization

1. Sign in to the [AWS Organizations console](https://console.aws.amazon.com/organizations/v2 "https://console.aws.amazon.com/organizations/v2"). You must sign in as an IAM user, assume an IAM role, or
   sign in as the root user ([not
   recommended](../../../IAM/latest/UserGuide/best-practices.md#lock-away-credentials "../../../IAM/latest/UserGuide/best-practices.md#lock-away-credentials")) in the organization’s management account.
2. Choose **Actions**, then for
   **AWS account** choose **Export
   account list**. The blue banner at the top of the page
   indicates "Export is in progress!"
3. When the file is ready, the banner turns green and indicates:
   "Download is ready!" Choose **Download CSV**. The
   file `Organization_accounts_information.csv`
   downloads to your device.

AWS CLI & AWS SDKs
The only way to export the .csv file with account details is by using
the AWS Management Console. You can't export the account list .csv file using the
AWS CLI.
