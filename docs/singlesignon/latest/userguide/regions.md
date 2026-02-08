# IAM Identity Center Region data storage and operations

Learn how IAM Identity Center handles data storage and operations across AWS Regions.

## Understand how IAM Identity Center stores data

When you enable IAM Identity Center, all the data that you configure in IAM Identity Center is stored in the Region
where you enabled it. This data includes directory configurations, permission sets,
application instances, and user assignments to AWS account applications. If you are using
the IAM Identity Center identity store, all users and groups that you create in IAM Identity Center are also stored in the
same Region. If you replicate your IAM Identity Center instance to additional Regions, IAM Identity Center automatically replicates users,
groups, permission sets and their assignments, and other metadata and configuration to those Regions.

## Cross-Region emails with Amazon SES

IAM Identity Center uses [Amazon Simple Email Service (Amazon SES)](../../../ses/latest/dg/Welcome.md "../../../ses/latest/dg/Welcome.md") to send emails to end users when they
attempt to sign-in with one-time password (OTP) as a second authentication factor. These
emails are also sent for certain identity and credential management events, such as when the
user is invited to set up an initial password, to verify an email address, and reset their
password. Amazon SES is available in a subset of AWS Regions that IAM Identity Center supports.

IAM Identity Center calls Amazon SES local endpoints when Amazon SES is available locally in an AWS Region.
When Amazon SES isn't available locally, IAM Identity Center calls Amazon SES endpoints in a different
AWS Region, as indicated in the following table.

| IAM Identity Center Region code | IAM Identity Center Region name | Amazon SES Region code | Amazon SES Region name   |
| ------------------------------- | ------------------------------- | ---------------------- | ------------------------ |
| ap-east-1                       | Asia Pacific (Hong Kong)        | ap-northeast-2         | Asia Pacific (Seoul)     |
| ap-east-2                       | Asia Pacific (Taipei)           | ap-northeast-1         | Asia Pacific (Tokyo)     |
| ap-south-2                      | Asia Pacific (Hyderabad)        | ap-south-1             | Asia Pacific (Mumbai)    |
| ap-southeast-4                  | Asia Pacific (Melbourne)        | ap-southeast-2         | Asia Pacific (Sydney)    |
| ap-southeast-5                  | Asia Pacific (Malaysia)         | ap-southeast-1         | Asia Pacific (Singapore) |
| ap-southeast-7                  | Asia Pacific (Thailand)         | ap-northeast-3         | Asia Pacific (Osaka)     |
| ca-west-1                       | Canada West (Calgary)           | ca-central-1           | Canada (Central)         |
| eu-south-2                      | Europe (Spain)                  | eu-west-3              | Europe (Paris)           |
| eu-central-2                    | Europe (Zurich)                 | eu-central-1           | Europe (Frankfurt)       |
| mx-central-1                    | Mexico (Central)                | us-east-2              | US East (Ohio)           |
| me-central-1                    | Middle East (UAE)               | eu-central-1           | Europe (Frankfurt)       |
| us-gov-east-1                   | AWS GovCloud (US-East)          | us-gov-west-1          | AWS GovCloud (US-West)   |

In these cross-Region calls, IAM Identity Center might
send the following user attributes:

- Email address
- First name
- Last name
- Account in AWS Organizations
- AWS access portal URL
- Username
- Directory ID
- User ID

## Managing IAM Identity Center in an opt-in Region (Region that is disabled by default)

Most AWS Regions are enabled for operations in all AWS services by default, but you
must enable the following [opt-in Regions](../../../glossary/latest/reference/glos-chap.md#optinregion "../../../glossary/latest/reference/glos-chap.md#optinregion") if you want to use IAM Identity Center:

- Africa (Cape Town)
- Asia Pacific (Hong Kong)
- Asia Pacific (Taipei)
- Asia Pacific (Hyderabad)
- Asia Pacific (Jakarta)
- Asia Pacific (Melbourne)
- Asia Pacific (Malaysia)
- Asia Pacific (Thailand)
- Canada West (Calgary)
- Europe (Milan)
- Europe (Spain)
- Europe (Zurich)
- Israel (Tel Aviv)
- Mexico (Central)
- Middle East (Bahrain)
- Middle East (UAE)

If you deploy IAM Identity Center in
an opt-in Region, then you must enable this Region in all the accounts for which you want to
manage access to IAM Identity Center. All accounts need this configuration, whether or not you'll create resources in that Region.
You can enable a Region for the current accounts in your organization and you must
repeat this action when you add new accounts. For instructions, see [Enable or disable a Region in your organization](../../../accounts/latest/reference/manage-acct-regions.md#manage-acct-regions-enable-organization "../../../accounts/latest/reference/manage-acct-regions.md#manage-acct-regions-enable-organization") in the _AWS Organizations User Guide_. To avoid
repeating these additional steps, you can choose to deploy your IAM Identity Center in a [Region enabled by
default](#regions-enabled-by-default "#regions-enabled-by-default").

###### Note

Your AWS member account must be opted into the same Region as the opt-in Region where
your IAM Identity Center instance is located, so you can access the AWS member account from the
AWS access portal.

###### Metadata stored in opt-in Regions

When you enable IAM Identity Center for a management account in an opt-in AWS Region, the
following IAM Identity Center metadata for any member accounts is stored in the Region.

- Account ID
- Account name
- Account email
- Amazon Resource Names (ARNs) of the IAM roles that IAM Identity Center creates in the member account

## AWS Regions that are enabled by default

The following Regions are enabled by default and you can enable IAM Identity Center in these Regions.

- US East (Ohio)
- US East (N. Virginia)
- US West (Oregon)
- US West (N. California)
- Europe (Paris)
- South America (São Paulo)
- Asia Pacific (Mumbai)
- Europe (Stockholm)
- Asia Pacific (Seoul)
- Asia Pacific (Tokyo)
- Europe (Ireland)
- Europe (Frankfurt)
- Europe (London)
- Asia Pacific (Singapore)
- Asia Pacific (Sydney)
- Canada (Central)
- Asia Pacific (Osaka)
