# Importing users into user pools from a

CSV file

When you have an external identity store and the time to prepare your user pool for new
local users, a bulk user import from a comma-separated values (CSV) file can be a low-effort,
low-cost option for a migration to an Amazon Cognito user pool. A CSV file import is a process of
downloading and populating a template file, then handing off the file to your user pool in an
import job. You can use a CSV import to quickly create test users. You can also programmatically
populate the file with read API requests to your external identity store, followed by parsing
their details and attributes into write operations to the file.

The import process sets values for all user attributes except **password**.
Password import is not supported, because security best practices require that passwords are not
available as plain text, and we don't support importing hashes. This means that your users must
change their passwords the first time they sign in. Your users are in a
`RESET_REQUIRED` state when imported using this method.

The lowest-effort way to import users from a CSV is to activate [passwordless
sign-in](amazon-cognito-user-pools-authentication-flow-methods.md#amazon-cognito-user-pools-authentication-flow-methods-passwordless "amazon-cognito-user-pools-authentication-flow-methods.md#amazon-cognito-user-pools-authentication-flow-methods-passwordless") in your user pool. With email address and phone number attributes and the right
user pool configuration, users can sign in with email or SMS one-time passwords (OTPs)
immediately after your import job completes. For more information, see [Requiring imported users
to reset their passwords](#cognito-user-pools-using-import-tool-password-reset "#cognito-user-pools-using-import-tool-password-reset").

You can also set your users' passwords with an [AdminSetUserPassword](../../../cognito-user-identity-pools/latest/APIReference/API_AdminSetUserPassword.md "../../../cognito-user-identity-pools/latest/APIReference/API_AdminSetUserPassword.md") API request that sets the
`Permanent` parameter to `true`. CSV import doesn't contribute to the
billed monthly active users (MAUs) in your user pool. However, password-reset operations do
generate MAUs. To manage costs when you import large numbers of users with password who might
not be immediately active, set up your application to prompt users for a new password when they
sign in and receive the `RESET_REQUIRED` challenge.

###### Note

The creation date for each user is the time when that user was imported into the user
pool. Creation date is not one of the imported attributes.

###### Steps to create a user import job

1. Create an Amazon CloudWatch Logs role in the AWS Identity and Access Management (IAM) console.
2. Create the user import .csv file.
3. Create and run the user import job.
4. Upload the user import .csv file.
5. Start and run the user import job.
6. Use CloudWatch to check the event log.
7. Require the imported users to reset their passwords.

###### More resources

- [Cognito User Profiles Export Reference Architecture](https://aws.amazon.com/solutions/implementations/cognito-user-profiles-export-reference-architecture/ "https://aws.amazon.com/solutions/implementations/cognito-user-profiles-export-reference-architecture/") for exporting user accounts
  between user pools

###### Topics

- [Creating the
  CloudWatch Logs IAM role](#cognito-user-pools-using-import-tool-cli-cloudwatch-iam-role "#cognito-user-pools-using-import-tool-cli-cloudwatch-iam-role")
- [Creating the user import CSV
  file](#cognito-user-pools-using-import-tool-csv-header "#cognito-user-pools-using-import-tool-csv-header")
- [Creating and running the Amazon Cognito user
  pool import job](#cognito-user-pools-creating-import-job "#cognito-user-pools-creating-import-job")
- [Viewing the user pool import
  results in the CloudWatch console](#cognito-user-pools-using-import-tool-cloudwatch "#cognito-user-pools-using-import-tool-cloudwatch")
- [Requiring imported users
  to reset their passwords](#cognito-user-pools-using-import-tool-password-reset "#cognito-user-pools-using-import-tool-password-reset")

## Creating the

CloudWatch Logs IAM role

If you're using the Amazon Cognito CLI or API, then you need to create a CloudWatch IAM role. The
following procedure describes how to create an IAM role that Amazon Cognito can use to write the
results of your import job to CloudWatch Logs.

###### Note

When you create an import job in the Amazon Cognito console, you can create the IAM role at the
same time. When you choose to **Create a new IAM role**, Amazon Cognito automatically
applies the appropriate trust policy and IAM policy to the role.

###### To create the CloudWatch Logs IAM role for user pool import (AWS CLI, API)

1. Sign in to the AWS Management Console and open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. Create a new IAM role for an AWS service. For detailed instructions, see [Creating a role for an AWS service](../../../IAM/latest/UserGuide/id_roles_create_for-service.md#roles-creatingrole-service-console "../../../IAM/latest/UserGuide/id_roles_create_for-service.md#roles-creatingrole-service-console") in the _AWS Identity and Access Management
   User Guide_.
   1. When you select a **Use case** for your **Trusted entity
      type**, choose any service. Amazon Cognito isn't currently listed in service use
      cases.
   2. In the **Add permissions** screen, choose **Create
      policy** and insert the following policy statement. Replace
      `REGION` with the AWS Region of your user pool, for example
      `us-east-1`. Replace `ACCOUNT` with your
      AWS account ID, for example `111122223333`.

   JSON

   ```
   `{
    "Version":"2012-10-17",
    "Statement": [
    {
    "Effect": "Allow",
    "Action": [
    "logs:CreateLogGroup",
    "logs:CreateLogStream",
    "logs:DescribeLogStreams",
    "logs:PutLogEvents"
    ],
    "Resource": [
    "arn:aws:logs:`us-east-1`:`111122223333`:log-group:/aws/cognito/*"
    ]
    }
    ]
   }`

   ```

3. Because you didn't choose Amazon Cognito as the trusted entity when you created the role, you now
   must manually edit the trust relationship of the role. Choose **Roles**
   from navigation pane of the IAM console, then choose the new role that you created.
4. Choose the **Trust relationships** tab.
5. Choose **Edit trust policy**.
6. Paste the following policy statement into **Edit trust policy**,
   replacing any existing text:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "Service": "cognito-idp.amazonaws.com"
 },
 "Action": "sts:AssumeRole"
 }
 ]
 }`

```

7. Choose **Update policy**.
8. Note the role ARN. You'll provide the ARN when you create your import job.

## Creating the user import CSV

file

Before you can import your existing users into your user pool, you must create a
comma-separated values (CSV) file that contains the users that you want to import, and their
attributes. From your user pool, you can retrieve a user import file with headers that reflect
the attribute schema of your user pool. You can then insert user information that matches the
formatting requirements in [Formatting the CSV
file](#cognito-user-pools-using-import-tool-formatting-csv-file "#cognito-user-pools-using-import-tool-formatting-csv-file").

### Downloading the CSV file header (console)

Use the following procedure to download the CSV header file.

###### To download the CSV file header

1. Go to the [Amazon Cognito console](https://console.aws.amazon.com/cognito/home "https://console.aws.amazon.com/cognito/home"). You
   might be prompted for your AWS credentials.
2. Choose **User Pools**.
3. Choose an existing user pool from the list.
4. Choose the **Users** menu.
5. In the **Import users** section, choose **Create an import
   job**.
6. Under **Upload CSV**, select the _template.csv_ link and download the CSV file.

### Downloading the CSV file header (AWS CLI)

To get a list of the correct headers, from the **Users menu** under
**Import users**, select **Create import job**. In the
dialog that follows, select the `template.csv` link to download a template file
with your user pool attributes.

You can also run the following CLI command, where
`USER_POOL_ID` is the user pool identifier for the user pool
you'll import users into:

```
aws cognito-idp get-csv-header --user-pool-id "`USER_POOL_ID`"
```

Sample response:

```
{
    "CSVHeader": [
        "name",
        "given_name",
        "family_name",
        "middle_name",
        "nickname",
        "preferred_username",
        "profile",
        "picture",
        "website",
        "email",
        "email_verified",
        "gender",
        "birthdate",
        "zoneinfo",
        "locale",
        "phone_number",
        "phone_number_verified",
        "address",
        "updated_at",
        "cognito:mfa_enabled",
        "cognito:username"
    ],
    "UserPoolId": "`USER_POOL_ID`"
}
```

### Formatting the CSV

file

The downloaded user import CSV header file looks like the following string. It also
includes any custom attributes you have added to your user pool.

```
cognito:username,name,given_name,family_name,middle_name,nickname,preferred_username,profile,picture,website,email,email_verified,gender,birthdate,zoneinfo,locale,phone_number,phone_number_verified,address,updated_at,cognito:mfa_enabled
```

Edit your CSV file so that it includes this header and the attribute values for your
users, and is formatted according to the following rules:

###### Note

For more information about attribute values, such as proper format for phone numbers,
see [Working with user attributes](user-pool-settings-attributes.md "user-pool-settings-attributes.md").

- The first row in the file is the downloaded header row, which contains the user
  attribute names.
- The order of columns in the CSV file doesn't matter.
- Each row after the first row contains the attribute values for a user.
- All columns in the header must be present, but you don't need to provide values in
  every column.
- The following attributes are required:
  - **cognito:username**
  - **email_verified** or
    **phone_number_verified**
    - At least one of the auto-verified attributes must be `true` for
      each user. An auto-verified attribute is an email address or phone number that
      Amazon Cognito automatically sends a code to when a new user joins your user pool.
    - The user pool must have at least one auto-verified attribute, either
      **email_verified** or
      **phone_number_verified**. If the user pool has no
      auto-verified attributes, the import job will not start.
    - If the user pool only has one auto-verified attribute, that attribute must be
      verified for each user. For example, if the user pool has only
      **phone_number** as an auto-verified attribute, the
      **phone_number_verified** value must be `true` for
      each user.

  ###### Note

  For users to reset their passwords, they must have a verified email or phone
  number. Amazon Cognito sends a message containing a reset password code to the email or phone
  number specified in the CSV file. If the message is sent to the phone number, it is
  sent by SMS message. For more information, see [Verifying contact
  information at sign-up](signing-up-users-in-your-app.md#allowing-users-to-sign-up-and-confirm-themselves "signing-up-users-in-your-app.md#allowing-users-to-sign-up-and-confirm-themselves").
  - **email** (if **email_verified** is
    `true`)
  - **phone_number** (if **phone_number_verified**
    is `true`)
  - Any attributes that you marked as required when you created the user pool

- Attribute values that are strings should _not_ be in quotation
  marks.
- If an attribute value contains a comma, you must put a backslash (\) before the
  comma. This is because the fields in a CSV file are separated by commas.
- The CSV file contents should be in UTF-8 format without byte order mark.
- The **cognito:username** field is required and must be unique within
  your user pool. It can be any Unicode string. However, it cannot contain spaces or
  tabs.
- The **birthdate** values, if present, must be in the format
  _`mm/dd/yyyy`_. This means, for example,
  that a birthdate of February 1, 1985 must be encoded as
  `02/01/1985`.
- The **cognito:mfa_enabled** field must correspond to the MFA
  requirements of your user pool. If you've set multi-factor authentication (MFA) to be
  required in your user pool, this field must be `true` or blank for all users.
  If you've set MFA to be off, this field must be `false` or blank for all
  users. A blank value sets imported users' MFA-enabled status to the state required by
  the user pool. You can import users in an MFA-required user pool without a valid MFA
  factor, regardless of whether you set a `cognito:mfa_enabled` value. Users in
  this state have MFA active but can't sign in until they configure an email attribute,
  phone number attribute, or a TOTP, and that configuration is a valid MFA factor in your
  user pool.
- The maximum row length is 16,000 characters.
- The maximum CSV file size is 100 MB.
- The maximum number of rows (users) in the file is 500,000. This maximum doesn't
  include the header row.
- The **updated_at** field value is expected to be epoch time in
  seconds, for example: `1471453471`.
- Any leading or trailing white space in an attribute value will be trimmed.

The following list is a example CSV import file for a user pool with no custom attributes.
Your user pool schema might differ from this example. In that case, you must provide test
values in the CSV template that you download from your user pool.

```
cognito:username,name,given_name,family_name,middle_name,nickname,preferred_username,profile,picture,website,email,email_verified,gender,birthdate,zoneinfo,locale,phone_number,phone_number_verified,address,updated_at,cognito:mfa_enabled
John,,John,Doe,,,,,,,johndoe@example.com,TRUE,,02/01/1985,,,+12345550100,TRUE,123 Any Street,,FALSE
Jane,,Jane,Roe,,,,,,,janeroe@example.com,TRUE,,01/01/1985,,,+12345550199,TRUE,100 Main Street,,FALSE

```

## Creating and running the Amazon Cognito user

pool import job

This section describes how to create and run the user pool import job by using the Amazon Cognito
console and the AWS Command Line Interface (AWS CLI).

###### Topics

- [Importing users from a CSV file
  (console)](#cognito-user-pools-using-import-tool-console "#cognito-user-pools-using-import-tool-console")
- [Importing users (AWS CLI)](#cognito-user-pools-using-import-tool-cli "#cognito-user-pools-using-import-tool-cli")

### Importing users from a CSV file

(console)

The following procedure describes how to import the users from the CSV file.

###### To import users from the CSV file (console)

1. Go to the [Amazon Cognito console](https://console.aws.amazon.com/cognito/home "https://console.aws.amazon.com/cognito/home"). You
   might be prompted for your AWS credentials.
2. Choose **User Pools**.
3. Choose an existing user pool from the list.
4. Choose the **Users** menu.
5. In the **Import users** section, choose **Create an import
   job**.
6. On the **Create import job** page, enter a **Job
   name**.
7. Choose to **Create a new IAM role** or to **Use an existing
   IAM role**.
   1. If you chose **Create a new IAM role**, enter a name for your
      new role. Amazon Cognito will automatically create a role with the correct permissions and
      trust relationship. The IAM principal that creates the import job must have
      permissions to create IAM roles.
   2. If you chose **Use an existing IAM role**, choose a role from
      the list under **IAM role selection**. This role must have the
      permissions and trust policy described in [Creating the
      CloudWatch Logs IAM role](#cognito-user-pools-using-import-tool-cli-cloudwatch-iam-role "#cognito-user-pools-using-import-tool-cli-cloudwatch-iam-role").

8. Under **Upload CSV**, choose **Choose file** and
   attach the CSV file that you prepared.
9. Choose **Create job** to submit your job, but start it later. Choose
   **Create and start job** to submit your job and start it
   immediately.
10. If you created your job but didn't start it, you can start it later. In the
    **Users** menu under **Import users**, choose your
    import job, then select **Start**. You can also submit a [StartUserImportJob](../../../cognito-user-identity-pools/latest/APIReference/API_StartUserImportJob.md "../../../cognito-user-identity-pools/latest/APIReference/API_StartUserImportJob.md") API request from an AWS SDK.
11. Monitor the progress of your user import job in the **Users** menu
    under **Import users**. If your job doesn't succeed, you can select the
    **Status** value. For additional details, select **View the
    CloudWatch logs for more details** and review any issues in the CloudWatch Logs
    console.

### Importing users (AWS CLI)

The following CLI commands are available for importing users into a user pool:

- `create-user-import-job`
- `get-csv-header`
- `describe-user-import-job`
- `list-user-import-jobs`
- `start-user-import-job`
- `stop-user-import-job`

To get the list of command line options for these commands, use the `help`
command line option. For example:

```
aws cognito-idp get-csv-header help
```

#### Creating

a user import job

After you create your CSV file, create a user import job by
running the following CLI command, where `JOB_NAME` is the name
you're choosing for the job, `USER_POOL_ID` is the user pool ID for
the user pool into which the new users will be added, and
`ROLE_ARN` is the role ARN you received in [Creating the
CloudWatch Logs IAM role](#cognito-user-pools-using-import-tool-cli-cloudwatch-iam-role "#cognito-user-pools-using-import-tool-cli-cloudwatch-iam-role"):

```
aws cognito-idp create-user-import-job --job-name "`JOB_NAME`" --user-pool-id "`USER_POOL_ID`" --cloud-watch-logs-role-arn "`ROLE_ARN`"
```

The `PRE_SIGNED_URL` returned in the response is valid for 15
minutes. After that time, it will expire and you must create a new user import job to get a
new URL.

###### Example response:

```
{
    "UserImportJob": {
        "Status": "Created",
        "SkippedUsers": 0,
        "UserPoolId": "`USER_POOL_ID`",
        "ImportedUsers": 0,
        "JobName": "`JOB_NAME`",
        "JobId": "`JOB_ID`",
        "PreSignedUrl": "`PRE_SIGNED_URL`",
        "CloudWatchLogsRoleArn": "`ROLE_ARN`",
        "FailedUsers": 0,
        "CreationDate": 1470957431.965
    }
}
```

#### Status values for a user import job

In the responses to your user import commands, you'll see one of the following
`Status` values:

- `Created` - The job was created but not started.
- `Pending` - A transition state. You have started the job, but it has not
  begun importing users yet.
- `InProgress` - The job has started, and users are being imported.
- `Stopping` - You have stopped the job, but the job has not stopped
  importing users yet.
- `Stopped` - You have stopped the job, and the job has stopped importing
  users.
- `Succeeded` - The job has completed successfully.
- `Failed` - The job has stopped due to an error.
- `Expired` - You created a job, but did not start the job within 24-48
  hours. All data associated with the job was deleted, and the job can't be
  started.

#### Uploading the

CSV file

Use the following `curl` command to upload the CSV file containing your user
data to the presigned URL that you obtained from the response of the
`create-user-import-job` command.

```
curl -v -T "`PATH_TO_CSV_FILE`" -H "x-amz-server-side-encryption:aws:kms" "`PRE_SIGNED_URL`"
```

In the output of this command, look for the phrase `"We are completely uploaded and
 fine"`. This phrase indicates that the file was uploaded successfully. Your user
pools don't keep the information in your import files after you run your import jobs.
After they complete or expire, Amazon Cognito deletes your uploaded CSV file.

#### Describing a user import job

To get a description of your user import job, use the following command, where
`USER_POOL_ID` is your user pool ID, and
`JOB_ID` is the job ID that was returned when you created the
user import job.

```
aws cognito-idp describe-user-import-job --user-pool-id "`USER_POOL_ID`" --job-id "`JOB_ID`"
```

###### Example Sample response:

```
{
    "UserImportJob": {
        "Status": "Created",
        "SkippedUsers": 0,
        "UserPoolId": "`USER_POOL_ID`",
        "ImportedUsers": 0,
        "JobName": "`JOB_NAME`",
        "JobId": "`JOB_ID`",
        "PreSignedUrl": "`PRE_SIGNED_URL`",
        "CloudWatchLogsRoleArn":"`ROLE_ARN`",
        "FailedUsers": 0,
        "CreationDate": 1470957431.965
    }
}
```

In the preceding sample output, the `PRE_SIGNED_URL` is the URL
that you uploaded the CSV file to. The
`ROLE_ARN` is the CloudWatch Logs role ARN that you received when you
created the role.

#### Listing

your user import jobs

To list your user import jobs, use the following command:

```
aws cognito-idp list-user-import-jobs --user-pool-id "`USER_POOL_ID`" --max-results 2
```

###### Example Sample response:

```
{
    "UserImportJobs": [
        {
            "Status": "Created",
            "SkippedUsers": 0,
            "UserPoolId": "`USER_POOL_ID`",
            "ImportedUsers": 0,
            "JobName": "`JOB_NAME`",
            "JobId": "`JOB_ID`",
            "PreSignedUrl":"`PRE_SIGNED_URL`",
            "CloudWatchLogsRoleArn":"`ROLE_ARN`",
            "FailedUsers": 0,
            "CreationDate": 1470957431.965
        },
        {
            "CompletionDate": 1470954227.701,
            "StartDate": 1470954226.086,
            "Status": "Failed",
            "UserPoolId": "`USER_POOL_ID`",
            "ImportedUsers": 0,
            "SkippedUsers": 0,
            "JobName": "`JOB_NAME`",
            "CompletionMessage": "Too many users have failed or been skipped during the import.",
            "JobId": "`JOB_ID`",
            "PreSignedUrl":"`PRE_SIGNED_URL`",
            "CloudWatchLogsRoleArn":"`ROLE_ARN`",
            "FailedUsers": 5,
            "CreationDate": 1470953929.313
        }
    ],
    "PaginationToken": "`PAGINATION_TOKEN`"
}
```

Jobs are listed in chronological order from last created to first created. The
`PAGINATION_TOKEN` string after the second job indicates that
there are additional results for this list command. To list the additional results, use the
`--pagination-token` option as follows:

```
aws cognito-idp list-user-import-jobs --user-pool-id "`USER_POOL_ID`" --max-results 10 --pagination-token "`PAGINATION_TOKEN`"
```

#### Starting

a user import job

To start a user import job, use the following command:

```
aws cognito-idp start-user-import-job --user-pool-id "`USER_POOL_ID`" --job-id "`JOB_ID`"
```

Only one import job can be active at a time per account.

###### Example Sample response:

```
{
    "UserImportJob": {
        "Status": "Pending",
        "StartDate": 1470957851.483,
        "UserPoolId": "`USER_POOL_ID`",
        "ImportedUsers": 0,
        "SkippedUsers": 0,
        "JobName": "`JOB_NAME`",
        "JobId": "`JOB_ID`",
        "PreSignedUrl":"`PRE_SIGNED_URL`",
        "CloudWatchLogsRoleArn": "`ROLE_ARN`",
        "FailedUsers": 0,
        "CreationDate": 1470957431.965
    }
}
```

#### Stopping

a user import job

To stop a user import job while it is in progress, use the following command. After you
stop the job, it cannot be restarted.

```
aws cognito-idp stop-user-import-job --user-pool-id "`USER_POOL_ID`" --job-id "`JOB_ID`"
```

###### Example Sample response:

```
{
    "UserImportJob": {
        "CompletionDate": 1470958050.571,
        "StartDate": 1470958047.797,
        "Status": "Stopped",
        "UserPoolId": "`USER_POOL_ID`",
        "ImportedUsers": 0,
        "SkippedUsers": 0,
        "JobName": "`JOB_NAME`",
        "CompletionMessage": "The Import Job was stopped by the developer.",
        "JobId": "`JOB_ID`",
        "PreSignedUrl":"`PRE_SIGNED_URL`",
        "CloudWatchLogsRoleArn": "`ROLE_ARN`",
        "FailedUsers": 0,
        "CreationDate": 1470957972.387
    }
}
```

## Viewing the user pool import

results in the CloudWatch console

You can view the results of your import job in the Amazon CloudWatch console.

###### Topics

- [Viewing the
  results](#cognito-user-pools-using-import-tool-viewing-the-results "#cognito-user-pools-using-import-tool-viewing-the-results")
- [Interpreting
  the results](#cognito-user-pools-using-import-tool-interpreting-the-results "#cognito-user-pools-using-import-tool-interpreting-the-results")

### Viewing the

results

The following steps describe how to view the user pool import results.

###### To view the results of the user pool import

1. Sign in to the AWS Management Console and open the CloudWatch console at
   [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. Choose **Logs**.
3. Choose the log group for your user pool import jobs. The log group name is in the form
   `/aws/cognito/userpools/`USER_POOL_ID`/`USER_POOL_NAME``.
4. Choose the log for the user import job you just ran. The log name is in the form
   `JOB_ID`/`JOB_NAME`. The results in
   the log refer to your users by line number. No user data is written to the log. For each
   user, a line similar to the following appears:
   - `[SUCCEEDED] Line Number 5956 - The import succeeded.`
   - `[SKIPPED] Line Number 5956 - The user already exists.`
   - `[FAILED] Line Number 5956 - The User Record does not set any of the auto
verified attributes to true. (Example: email_verified to true).`

### Interpreting

the results

Successfully imported users have their status set to "PasswordReset".

In the following cases, the user will not be imported, but the import job will
continue:

- No auto-verified attributes are set to `true`.
- The user data doesn't match the schema.
- The user couldn't be imported due to an internal error.

In the following cases, the import job will fail:

- The Amazon CloudWatch Logs role cannot be assumed, doesn't have the correct access policy, or has
  been deleted.
- The user pool has been deleted.
- Amazon Cognito is unable to parse the .csv file.

## Requiring imported users

to reset their passwords

If your user pool only offers password-based sign-in, users must reset their passwords
after they are imported. The first time they sign in, they can enter _any_ password. Amazon Cognito prompts them to enter a new password in the API response to
the sign-in request from your application.

If your user pool has passwordless authentication factors, Amazon Cognito defaults to those for
imported users. They're not prompted for a new password, and can sign in immediately with a
passwordless email or SMS OTP. You can also prompt users to set a password so that they can
complete other sign-in methods like username-password and passkey. The following conditions
apply to passwordless sign-in after user import.

1. You must import users with an attribute that corresponds to an available passwordless
   sign-in factor. If users can sign in with an email address, you must import an
   `email` attribute. If a phone number, you must import a
   `phone_number` attribute. If both, import a value for either
   attribute.
2. Normally, users import in a `RESET_REQUIRED` state where they must reset
   their password. If they are imported with the ability to sign in with a passwordless
   factor, Amazon Cognito sets their state to `CONFIRMED`.

For more information about passwordless authentication including how to set it up and how
to construct the authentication flow in your application, see [Authentication with Amazon Cognito user pools](authentication.md "authentication.md").

The following procedure describes the user experience in a custom-built login mechanism
with local users in a `RESET_REQUIRED` after you import a CSV file. If your users
sign in with managed login, instruct them to select the **Forgot password?**
option, provide the code from their email or text message, and set a password.

###### Requiring imported users to reset their passwords

1. In your app, silently attempt sign-in for the current user with
   `InitiateAuth` using a random password.
2. Amazon Cognito returns a `NotAuthorizedException` when
   `PreventUserExistenceErrors` is enabled. Otherwise, it returns
   `PasswordResetRequiredException`.
3. Your app makes a `ForgotPassword` API request and resets the user's
   password.
   1. The app submits the username in a `ForgotPassword` API request.
   2. Amazon Cognito sends a code to the verified email or phone number. The destination depends on
      the values you provided for `email_verified` and
      `phone_number_verified` in your CSV file. The response to the
      `ForgotPassword` request indicates the destination of the code.

   ###### Note

   Your user pool must be configured to verify emails or phone numbers. For more
   information, see [Signing up and confirming user accounts](signing-up-users-in-your-app.md "signing-up-users-in-your-app.md"). 3. Your app displays a message to your user to check the location where the code was
   sent, and prompts your user to enter the code and a new password. 4. The user enters the code and new password in the app. 5. The app submits the code and new password in a `ConfirmForgotPassword`
   API request. 6. Your app redirects your user to sign-in.
