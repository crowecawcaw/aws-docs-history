# Generate credential reports for your

AWS account

You can generate and download a _credential report_ that lists all users
in your account and the status of their various credentials, including passwords, access keys,
and MFA devices. You can get a credential report from the AWS Management Console, the [AWS SDKs](https://aws.amazon.com/tools "https://aws.amazon.com/tools") and [Command Line Tools](https://aws.amazon.com/tools/#Command_Line_Tools "https://aws.amazon.com/tools/#Command_Line_Tools"), or the IAM API.

You can use credential reports to assist in your auditing and compliance efforts. You can
use the report to audit the effects of credential lifecycle requirements, such as password and
access key updates. You can provide the report to an external auditor, or grant permissions to
an auditor so that he or she can download the report directly.

You can generate a credential report as often as once every four hours. When you request a
report, IAM first checks whether a report for the AWS account has been generated within the
past four hours. If so, the most recent report is downloaded. If the most recent report for the
account is older than four hours, or if there are no previous reports for the account, IAM
generates and downloads a new report.

###### Topics

- [Required permissions](#id_credentials_required_permissions "#id_credentials_required_permissions")
- [Understanding the report
  format](#id_credentials_understanding_the_report_format "#id_credentials_understanding_the_report_format")
- [Getting credential reports
  (console)](#getting-credential-reports-console "#getting-credential-reports-console")
- [Getting credential reports (AWS CLI)](#getting-credential-reports-cliapi "#getting-credential-reports-cliapi")
- [Getting credential reports (AWS
  API)](#getting-credential-reports-api "#getting-credential-reports-api")

## Required permissions

The following permissions are needed to create and download reports:

- To create a credential report: `iam:GenerateCredentialReport`
- To download the report: `iam:GetCredentialReport`

## Understanding the report

format

Credential reports are formatted as comma-separated values (CSV) files. You can open CSV
files with common spreadsheet software to perform analysis, or you can build an application
that consumes the CSV files programmatically and performs custom analysis.

The CSV file contains the following columns:

**user**

The friendly name of the user.

**arn**

The Amazon Resource Name (ARN) of the user. For more information about ARNs, see
[IAM ARNs](reference_identifiers.md#identifiers-arns "reference_identifiers.md#identifiers-arns").

**user_creation_time**

The date and time when the user was created, in [ISO 8601 date-time format](https://en.wikipedia.org/wiki/ISO_8601 "https://en.wikipedia.org/wiki/ISO_8601").

**password_enabled**

When the user has a password, this value is `TRUE`. Otherwise it is
`FALSE`. This value is `FALSE` for new member accounts created
as part of your organization as they have no root user credentials by default.

**password_last_used**

The date and time when the AWS account root user or user's password was last used to sign in to
an AWS website, in [ISO 8601 date-time
format](http://www.iso.org/iso/iso8601 "http://www.iso.org/iso/iso8601"). AWS websites that capture a user's last sign-in time are the
AWS Management Console, the AWS Discussion Forums, and the AWS Marketplace. When a password is
used more than once in a 5-minute span, only the first use is recorded in this field.

- The value in this field is `no_information` in these cases:
  - The user's password has never been used.
  - There is no sign-in data associated with the password, such as when user's
    password has not been used after IAM started tracking this information on
    October 20, 2014.

- The value in this field is `N/A` (not applicable) when the user does
  not have a password.

###### Important

Due to a service issue, password last used data does not include password use from May
3rd 2018 22:50 PDT to May 23rd 2018 14:08 PDT. This affects [last sign-in](id_credentials_finding-unused.md "id_credentials_finding-unused.md") dates shown in
the IAM console and password last used dates in the [IAM credential
report](SupportedTypes.md "SupportedTypes.md"), and returned by the [GetUser API
operation](../APIReference/API_GetUser.md "../APIReference/API_GetUser.md"). If users signed in during the affected time, the password last used
date that is returned is the date the user last signed in before May 3rd 2018. For users
that signed in after May 23rd 2018 14:08 PDT, the returned password last used date is
accurate.

If you use password last used information to identify unused credentials for deletion,
such as deleting users who did not sign in to AWS in the last 90 days, we recommend that
you adjust your evaluation window to include dates after May 23rd 2018. Alternatively, if
your users use access keys to access AWS programmatically you can refer to access key last
used information because it is accurate for all dates.

**password_last_changed**

The date and time when the user's password was last set, in [ISO 8601 date-time format](https://en.wikipedia.org/wiki/ISO_8601 "https://en.wikipedia.org/wiki/ISO_8601"). If the
user does not have a password, the value in this field is `N/A` (not
applicable).

**password_next_rotation**

When the account has a [password policy](Using_ManagingPasswordPolicies.md "Using_ManagingPasswordPolicies.md") that
requires password rotation, this field contains the date and time, in [ISO 8601 date-time format](https://en.wikipedia.org/wiki/ISO_8601 "https://en.wikipedia.org/wiki/ISO_8601"), when
the user is required to set a new password. The value for the AWS account (root) is
always `not_supported`.

**mfa_active**

When a [multi-factor authentication](id_credentials_mfa.md "id_credentials_mfa.md") (MFA)
device has been enabled for the user, this value is `TRUE`. Otherwise it is
`FALSE`.

**access_key_1_active**

When the user has an access key and the access key's status is `Active`,
this value is `TRUE`. Otherwise it is `FALSE`. Applies to both
account root user and IAM users.

**access_key_1_last_rotated**

The date and time, in [ISO 8601
date-time format](https://en.wikipedia.org/wiki/ISO_8601 "https://en.wikipedia.org/wiki/ISO_8601"), when the user's access key was created or last changed. If
the user does not have an active access key, the value in this field is `N/A`
(not applicable). Applies to both account root user and IAM users.

**access_key_1_last_used_date**

The date and time, in [ISO 8601
date-time format](https://en.wikipedia.org/wiki/ISO_8601 "https://en.wikipedia.org/wiki/ISO_8601"), when the user's access key was most recently used to sign an
AWS API request. When an access key is used more than once in a 15-minute span, only
the first use is recorded in this field. Applies to both account root user and
IAM users.

The value in this field is `N/A` (not applicable) in these cases:

- The user does not have an access key.
- The access key has never been used.
- The access key has not been used after IAM started tracking this information
  on April 22, 2015.

**access_key_1_last_used_region**

The [AWS Region](../../../general/latest/gr/rande.md "../../../general/latest/gr/rande.md") in which the access key was
most recently used. When an access key is used more than once in a 15-minute span, only
the first use is recorded in this field. Applies to both account root user and
IAM users.

The value in this field is `N/A` (not applicable) in these cases:

- The user does not have an access key.
- The access key has never been used.
- The access key was last used before IAM started tracking this information on
  April 22, 2015.
- The last used service is not Region-specific, such as Amazon S3.

**access_key_1_last_used_service**

The AWS service that was most recently accessed with the access key. The value in
this field uses the service's namespace—for example, `s3` for Amazon S3 and
`ec2` for Amazon EC2. When an access key is used more than once in a 15-minute
span, only the first use is recorded in this field. Applies to both account root user and
IAM users.

The value in this field is `N/A` (not applicable) in these cases:

- The user does not have an access key.
- The access key has never been used.
- The access key was last used before IAM started tracking this information on
  April 22, 2015.

**access_key_2_active**

When the user has a second access key and the second key's status is
`Active`, this value is `TRUE`. Otherwise it is
`FALSE`. Applies to both account root user and IAM users.

###### Note

Users can have up to two access keys, to make rotation easier by updating the key
first and then deleting the previous key. For more information about updating access
keys, see [Update access keys](id-credentials-access-keys-update.md "id-credentials-access-keys-update.md").

**access_key_2_last_rotated**

The date and time, in [ISO 8601
date-time format](https://en.wikipedia.org/wiki/ISO_8601 "https://en.wikipedia.org/wiki/ISO_8601"), when the user's second access key was created or last
updated. If the user does not have a second active access key, the value in this field
is `N/A` (not applicable). Applies to both account root user and
IAM users.

**access_key_2_last_used_date**

The date and time, in [ISO 8601
date-time format](https://en.wikipedia.org/wiki/ISO_8601 "https://en.wikipedia.org/wiki/ISO_8601"), when the user's second access key was most recently used to
sign an AWS API request. When an access key is used more than once in a 15-minute
span, only the first use is recorded in this field. Applies to both account root user and
IAM users.

The value in this field is `N/A` (not applicable) in these cases:

- The user does not have a second access key.
- The user's second access key has never been used.
- The user's second access key was last used before IAM started tracking this
  information on April 22, 2015.

**access_key_2_last_used_region**

The [AWS Region](../../../general/latest/gr/rande.md "../../../general/latest/gr/rande.md") in which the user's second
access key was most recently used. When an access key is used more than once in a
15-minute span, only the first use is recorded in this field. Applies to both account
root user and IAM users. The value in this field is `N/A` (not applicable) in
these cases:

- The user does not have a second access key.
- The user's second access key has never been used.
- The user's second access key was last used before IAM started tracking this
  information on April 22, 2015.
- The last used service is not Region-specific, such as Amazon S3.

**access_key_2_last_used_service**

The AWS service that was most recently accessed with the user's second access key.
The value in this field uses the service's namespace—for example, `s3`
for Amazon S3 and `ec2` for Amazon EC2. When an access key is used more than once in a
15-minute span, only the first use is recorded in this field. Applies to both account
root user and IAM users. The value in this field is `N/A` (not applicable) in
these cases:

- The user does not have a second access key.
- The user's second access key has never been used.
- The user's second access key was last used before IAM started tracking this
  information on April 22, 2015.

**cert_1_active**

When the user has an X.509 signing certificate and that certificate's status is
`Active`, this value is `TRUE`. Otherwise it is
`FALSE`.

**cert_1_last_rotated**

The date and time, in [ISO 8601
date-time format](https://en.wikipedia.org/wiki/ISO_8601 "https://en.wikipedia.org/wiki/ISO_8601"), when the user's signing certificate was created or last
changed. If the user does not have an active signing certificate, the value in this
field is `N/A` (not applicable).

**cert_2_active**

When the user has a second X.509 signing certificate and that certificate's status
is `Active`, this value is `TRUE`. Otherwise it is
`FALSE`.

###### Note

Users can have up to two X.509 signing certificates, to make certificate rotation
easier.

**cert_2_last_rotated**

The date and time, in [ISO 8601
date-time format](https://en.wikipedia.org/wiki/ISO_8601 "https://en.wikipedia.org/wiki/ISO_8601"), when the user's second signing certificate was created or
last changed. If the user does not have a second active signing certificate, the value
in this field is `N/A` (not applicable).

**additional_credentials_info**

When the user has more than two access keys or certificates, this value is the
number of additional access keys or certificates and the actions you can use to list the
access keys or certificates associated with the user.

## Getting credential reports

(console)

You can use the AWS Management Console to download a credential report as a comma-separated values
(CSV) file.

###### To download a credential report (console)

1. Sign in to the AWS Management Console and open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. In the navigation pane, choose **Credential report**.
3. Choose **Download Report**.

## Getting credential reports (AWS CLI)

###### To download a credentials report (AWS CLI)

1. Generate a credentials report. AWS stores a single report. If a report exists,
   generating a credentials report overwrites the previous report. [`aws iam
generate-credential-report`](../../../cli/latest/reference/iam/generate-credential-report.md "../../../cli/latest/reference/iam/generate-credential-report.md")
2. View the last report that was generated: [`aws iam
get-credential-report`](../../../cli/latest/reference/iam/get-credential-report.md "../../../cli/latest/reference/iam/get-credential-report.md")

## Getting credential reports (AWS

API)

###### To download a credentials report (AWS API)

1. Generate a credentials report. AWS stores a single report. If a report exists,
   generating a credentials report overwrites the previous report. [`GenerateCredentialReport`](../APIReference/API_GenerateCredentialReport.md "../APIReference/API_GenerateCredentialReport.md")
2. View the last report that was generated: [`GetCredentialReport`](../APIReference/API_GetCredentialReport.md "../APIReference/API_GetCredentialReport.md")
