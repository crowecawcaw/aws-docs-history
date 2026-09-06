

# Importing users into user pools from a CSV file
<a name="cognito-user-pools-using-import-tool"></a>

When you have an external identity store and the time to prepare your user pool for new local users, a bulk user import from a comma-separated values (CSV) file can be a low-effort, low-cost option for a migration to an Amazon Cognito user pool. A CSV file import is a process of downloading and populating a template file, then handing off the file to your user pool in an import job. You can use a CSV import to quickly create test users. You can also programmatically populate the file with read API requests to your external identity store, followed by parsing their details and attributes into write operations to the file.

By default, the import process sets values for all user attributes except **password**. This means that your users must change their passwords the first time they sign in. Your users are in a `RESET_REQUIRED` state when imported using this method.

Alternatively, you can import users with their existing password hashes. When you specify a password hashing algorithm during import job creation and include password hashes in your CSV file, Amazon Cognito imports the users with their existing passwords. These users are created with a `CONFIRMED` status and can sign in immediately without resetting their passwords. For more information, see [Importing users with password hashes](#cognito-user-pools-import-password-hash).

The lowest-effort way to import users from a CSV is to activate [passwordless sign-in](amazon-cognito-user-pools-authentication-flow-methods.md#amazon-cognito-user-pools-authentication-flow-methods-passwordless) in your user pool. With email address and phone number attributes and the right user pool configuration, users can sign in with email or SMS one-time passwords (OTPs) immediately after your import job completes. For more information, see [Requiring imported users to reset their passwords](#cognito-user-pools-using-import-tool-password-reset).

You can also set your users' passwords with an [AdminSetUserPassword](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_AdminSetUserPassword.html) API request that sets the `Permanent` parameter to `true`. CSV import doesn't contribute to the billed monthly active users (MAUs) in your user pool. However, password-reset operations do generate MAUs. To manage costs when you import large numbers of users with password who might not be immediately active, set up your application to prompt users for a new password when they sign in and receive the `RESET_REQUIRED` challenge.

**Note**  
The creation date for each user is the time when that user was imported into the user pool. Creation date is not one of the imported attributes.

**Steps to create a user import job**

1. Create an Amazon CloudWatch Logs role in the AWS Identity and Access Management (IAM) console.

1. Create the user import .csv file.

1. Create and run the user import job. Optionally, specify a password hashing algorithm to import users with their existing password hashes.

1. Upload the user import .csv file.

1. Start and run the user import job.

1. Use CloudWatch to check the event log.

1. If you didn't import password hashes, require the imported users to reset their passwords.

**More resources**
+ [Cognito User Profiles Export Reference Architecture](https://aws.amazon.com/solutions/implementations/cognito-user-profiles-export-reference-architecture/) for exporting user accounts between user pools

**Topics**
+ [Creating the CloudWatch Logs IAM role](#cognito-user-pools-using-import-tool-cli-cloudwatch-iam-role)
+ [Creating the user import CSV file](#cognito-user-pools-using-import-tool-csv-header)
+ [Creating and running the Amazon Cognito user pool import job](#cognito-user-pools-creating-import-job)
+ [Viewing the user pool import results in the CloudWatch console](#cognito-user-pools-using-import-tool-cloudwatch)
+ [Requiring imported users to reset their passwords](#cognito-user-pools-using-import-tool-password-reset)
+ [Importing users with password hashes](#cognito-user-pools-import-password-hash)

## Creating the CloudWatch Logs IAM role
<a name="cognito-user-pools-using-import-tool-cli-cloudwatch-iam-role"></a>

If you're using the Amazon Cognito CLI or API, then you need to create a CloudWatch IAM role. The following procedure describes how to create an IAM role that Amazon Cognito can use to write the results of your import job to CloudWatch Logs. 

**Note**  
When you create an import job in the Amazon Cognito console, you can create the IAM role at the same time. When you choose to **Create a new IAM role**, Amazon Cognito automatically applies the appropriate trust policy and IAM policy to the role.

**To create the CloudWatch Logs IAM role for user pool import (AWS CLI, API)**

1. Sign in to the AWS Management Console and open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/).

1. Create a new IAM role for an AWS service. For detailed instructions, see [Creating a role for an AWS service](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-service.html#roles-creatingrole-service-console) in the *AWS Identity and Access Management User Guide*.

   1. When you select a **Use case** for your **Trusted entity type**, choose any service. Amazon Cognito isn't currently listed in service use cases.

   1. In the **Add permissions** screen, choose **Create policy** and insert the following policy statement. Replace {{REGION}} with the AWS Region of your user pool, for example `us-east-1`. Replace {{ACCOUNT}} with your AWS account ID, for example `111122223333`.

------
#### [ JSON ]

****  

      ```
      {
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
                      "arn:aws:logs:{{us-east-1}}:{{111122223333}}:log-group:/aws/cognito/*"
                  ]
              }
          ]
      }
      ```

------

1. Because you didn't choose Amazon Cognito as the trusted entity when you created the role, you now must manually edit the trust relationship of the role. Choose **Roles** from navigation pane of the IAM console, then choose the new role that you created.

1. Choose the **Trust relationships** tab.

1. Choose **Edit trust policy**.

1. Paste the following policy statement into **Edit trust policy**, replacing any existing text: 

------
#### [ JSON ]

****  

   ```
   {
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
       }
   ```

------

1. Choose **Update policy**. 

1. Note the role ARN. You'll provide the ARN when you create your import job.

## Creating the user import CSV file
<a name="cognito-user-pools-using-import-tool-csv-header"></a>

Before you can import your existing users into your user pool, you must create a comma-separated values (CSV) file that contains the users that you want to import, and their attributes. From your user pool, you can retrieve a user import file with headers that reflect the attribute schema of your user pool. You can then insert user information that matches the formatting requirements in [Formatting the CSV file](#cognito-user-pools-using-import-tool-formatting-csv-file). 

### Downloading the CSV file header (console)
<a name="cognito-user-pools-using-import-tool-downloading-csv-header-console"></a>

Use the following procedure to download the CSV header file.

**To download the CSV file header**

1. Go to the [Amazon Cognito console](https://console.aws.amazon.com/cognito/home). You might be prompted for your AWS credentials.

1. Choose **User Pools**.

1. Choose an existing user pool from the list.

1. Choose the **Users** menu.

1. In the **Import users** section, choose **Create an import job**.

1. Under **Upload CSV**, select the *template.csv* link and download the CSV file.

### Downloading the CSV file header (AWS CLI)
<a name="cognito-user-pools-using-import-tool-downloading-csv-header-using-cli"></a>

To get a list of the correct headers, from the **Users menu** under **Import users**, select **Create import job**. In the dialog that follows, select the `template.csv` link to download a template file with your user pool attributes.

You can also run the following CLI command, where {{USER\_POOL\_ID}} is the user pool identifier for the user pool you'll import users into:

```
aws cognito-idp get-csv-header --user-pool-id "{{USER_POOL_ID}}"
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
    "UserPoolId": "{{USER_POOL_ID}}"
}
```

### Formatting the CSV file
<a name="cognito-user-pools-using-import-tool-formatting-csv-file"></a>

 The downloaded user import CSV header file looks like the following string. It also includes any custom attributes you have added to your user pool.

```
cognito:username,name,given_name,family_name,middle_name,nickname,preferred_username,profile,picture,website,email,email_verified,gender,birthdate,zoneinfo,locale,phone_number,phone_number_verified,address,updated_at,cognito:mfa_enabled
```

Edit your CSV file so that it includes this header and the attribute values for your users, and is formatted according to the following rules:

**Note**  
For more information about attribute values, such as proper format for phone numbers, see [Working with user attributes](user-pool-settings-attributes.md).
+ The first row in the file is the downloaded header row, which contains the user attribute names.
+ The order of columns in the CSV file doesn't matter.
+ Each row after the first row contains the attribute values for a user.
+ All columns in the header must be present, but you don't need to provide values in every column.
+ The following attributes are required:
  + **cognito:username**
  + **email\_verified** or **phone\_number\_verified**
    + At least one of the auto-verified attributes must be `true` for each user. An auto-verified attribute is an email address or phone number that Amazon Cognito automatically sends a code to when a new user joins your user pool.
    + The user pool must have at least one auto-verified attribute, either **email\_verified** or **phone\_number\_verified**. If the user pool has no auto-verified attributes, the import job will not start.
    + If the user pool only has one auto-verified attribute, that attribute must be verified for each user. For example, if the user pool has only **phone\_number** as an auto-verified attribute, the **phone\_number\_verified** value must be `true` for each user.
**Note**  
For users to reset their passwords, they must have a verified email or phone number. Amazon Cognito sends a message containing a reset password code to the email or phone number specified in the CSV file. If the message is sent to the phone number, it is sent by SMS message. For more information, see [Verifying contact information at sign-up](signing-up-users-in-your-app.md#allowing-users-to-sign-up-and-confirm-themselves).
  + **email** (if **email\_verified** is `true`)
  + **phone\_number** (if **phone\_number\_verified** is `true`)
  + Any attributes that you marked as required when you created the user pool
+ Attribute values that are strings should *not* be in quotation marks.
+ If an attribute value contains a comma, you must put a backslash (\\) before the comma. This is because the fields in a CSV file are separated by commas.
+ The CSV file contents should be in UTF-8 format without byte order mark.
+ The **cognito:username** field is required and must be unique within your user pool. It can be any Unicode string. However, it cannot contain spaces or tabs.
+ The **birthdate** values, if present, must be in the format *{{mm/dd/yyyy}}*. This means, for example, that a birthdate of February 1, 1985 must be encoded as **02/01/1985**.
+ The **cognito:mfa\_enabled** field must correspond to the MFA requirements of your user pool. If you've set multi-factor authentication (MFA) to be required in your user pool, this field must be `true` or blank for all users. If you've set MFA to be off, this field must be `false` or blank for all users. A blank value sets imported users' MFA-enabled status to the state required by the user pool. You can import users in an MFA-required user pool without a valid MFA factor, regardless of whether you set a `cognito:mfa_enabled` value. Users in this state have MFA active but can't sign in until they configure an email attribute, phone number attribute, or a TOTP, and that configuration is a valid MFA factor in your user pool.
+ The maximum row length is 16,000 characters.
+ The maximum CSV file size is 100 MB.
+ The maximum number of rows (users) in the file is 500,000. This maximum doesn't include the header row.
+ The **updated\_at** field value is expected to be epoch time in seconds, for example: **1471453471**.
+ Any leading or trailing white space in an attribute value will be trimmed.

The following list is a example CSV import file for a user pool with no custom attributes. Your user pool schema might differ from this example. In that case, you must provide test values in the CSV template that you download from your user pool.

```
cognito:username,name,given_name,family_name,middle_name,nickname,preferred_username,profile,picture,website,email,email_verified,gender,birthdate,zoneinfo,locale,phone_number,phone_number_verified,address,updated_at,cognito:mfa_enabled
John,,John,Doe,,,,,,,johndoe@example.com,TRUE,,02/01/1985,,,+12345550100,TRUE,123 Any Street,,FALSE
Jane,,Jane,Roe,,,,,,,janeroe@example.com,TRUE,,01/01/1985,,,+12345550199,TRUE,100 Main Street,,FALSE
```

## Creating and running the Amazon Cognito user pool import job
<a name="cognito-user-pools-creating-import-job"></a>

This section describes how to create and run the user pool import job by using the Amazon Cognito console and the AWS Command Line Interface (AWS CLI).

**Topics**
+ [Importing users from a CSV file (console)](#cognito-user-pools-using-import-tool-console)
+ [Importing users (AWS CLI)](#cognito-user-pools-using-import-tool-cli)

### Importing users from a CSV file (console)
<a name="cognito-user-pools-using-import-tool-console"></a>

The following procedure describes how to import the users from the CSV file.

**To import users from the CSV file (console)**

1. Go to the [Amazon Cognito console](https://console.aws.amazon.com/cognito/home). You might be prompted for your AWS credentials.

1. Choose **User Pools**.

1. Choose an existing user pool from the list.

1. Choose the **Users** menu.

1. In the **Import users** section, choose **Create an import job**.

1. On the **Create import job** page, enter a **Job name**.

1. Choose to **Create a new IAM role** or to **Use an existing IAM role**.

   1. If you chose **Create a new IAM role**, enter a name for your new role. Amazon Cognito will automatically create a role with the correct permissions and trust relationship. The IAM principal that creates the import job must have permissions to create IAM roles.

   1. If you chose **Use an existing IAM role**, choose a role from the list under **IAM role selection**. This role must have the permissions and trust policy described in [Creating the CloudWatch Logs IAM role](#cognito-user-pools-using-import-tool-cli-cloudwatch-iam-role).

1. Under **Upload CSV**, choose **Choose file** and attach the CSV file that you prepared.

1. Choose **Create job** to submit your job, but start it later. Choose **Create and start job** to submit your job and start it immediately.

1. If you created your job but didn't start it, you can start it later. In the **Users** menu under **Import users**, choose your import job, then select **Start**. You can also submit a [StartUserImportJob](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_StartUserImportJob.html) API request from an AWS SDK.

1. Monitor the progress of your user import job in the **Users** menu under **Import users**. If your job doesn't succeed, you can select the **Status** value. For additional details, select **View the CloudWatch logs for more details** and review any issues in the CloudWatch Logs console.

### Importing users (AWS CLI)
<a name="cognito-user-pools-using-import-tool-cli"></a>

The following CLI commands are available for importing users into a user pool:
+ `create-user-import-job`
+ `get-csv-header`
+ `describe-user-import-job`
+ `list-user-import-jobs`
+ `start-user-import-job`
+ `stop-user-import-job`

To get the list of command line options for these commands, use the `help` command line option. For example:

```
aws cognito-idp get-csv-header help
```

#### Creating a user import job
<a name="cognito-user-pools-using-import-tool-cli-creating-user-import-job"></a>

After you create your CSV file, create a user import job by running the following CLI command, where {{JOB\_NAME}} is the name you're choosing for the job, {{USER\_POOL\_ID}} is the user pool ID for the user pool into which the new users will be added, and {{ROLE\_ARN}} is the role ARN you received in [Creating the CloudWatch Logs IAM role](#cognito-user-pools-using-import-tool-cli-cloudwatch-iam-role): 

```
aws cognito-idp create-user-import-job --job-name "{{JOB_NAME}}" --user-pool-id "{{USER_POOL_ID}}" --cloud-watch-logs-role-arn "{{ROLE_ARN}}"
```

The {{PRE\_SIGNED\_URL}} returned in the response is valid for 15 minutes. After that time, it will expire and you must create a new user import job to get a new URL.

**Example response:**  

```
{
    "UserImportJob": {
        "Status": "Created",
        "SkippedUsers": 0,
        "UserPoolId": "{{USER_POOL_ID}}",
        "ImportedUsers": 0,
        "JobName": "{{JOB_NAME}}",
        "JobId": "{{JOB_ID}}",
        "PreSignedUrl": "{{PRE_SIGNED_URL}}",
        "CloudWatchLogsRoleArn": "{{ROLE_ARN}}",
        "FailedUsers": 0,
        "CreationDate": 1470957431.965
    }
}
```

#### Status values for a user import job
<a name="cognito-user-pools-using-import-tool-cli-status-values-for-user-import-job"></a>

In the responses to your user import commands, you'll see one of the following `Status` values:
+ `Created` - The job was created but not started.
+ `Pending` - A transition state. You have started the job, but it has not begun importing users yet.
+ `InProgress` - The job has started, and users are being imported.
+ `Stopping` - You have stopped the job, but the job has not stopped importing users yet.
+ `Stopped` - You have stopped the job, and the job has stopped importing users.
+ `Succeeded` - The job has completed successfully.
+ `Failed` - The job has stopped due to an error.
+ `Expired` - You created a job, but did not start the job within 24-48 hours. All data associated with the job was deleted, and the job can't be started.

#### Uploading the CSV file
<a name="cognito-user-pools-using-import-tool-cli-uploading-csv-file"></a>

Use the following `curl` command to upload the CSV file containing your user data to the presigned URL that you obtained from the response of the `create-user-import-job` command.

```
curl -v -T "{{PATH_TO_CSV_FILE}}" -H "x-amz-server-side-encryption:aws:kms" "{{PRE_SIGNED_URL}}"
```

In the output of this command, look for the phrase `"We are completely uploaded and fine"`. This phrase indicates that the file was uploaded successfully. Your user pools don't keep the information in your import files after you run your import jobs. After they complete or expire, Amazon Cognito deletes your uploaded CSV file.

#### Describing a user import job
<a name="cognito-user-pools-using-import-tool-cli-describing-user-import-job"></a>

To get a description of your user import job, use the following command, where {{USER\_POOL\_ID}} is your user pool ID, and {{JOB\_ID}} is the job ID that was returned when you created the user import job. 

```
aws cognito-idp describe-user-import-job --user-pool-id "{{USER_POOL_ID}}" --job-id "{{JOB_ID}}"
```

**Example Sample response:**  

```
{
    "UserImportJob": {
        "Status": "Created",
        "SkippedUsers": 0,
        "UserPoolId": "{{USER_POOL_ID}}",
        "ImportedUsers": 0,
        "JobName": "{{JOB_NAME}}",
        "JobId": "{{JOB_ID}}",
        "PreSignedUrl": "{{PRE_SIGNED_URL}}",
        "CloudWatchLogsRoleArn":"{{ROLE_ARN}}",
        "FailedUsers": 0,
        "CreationDate": 1470957431.965
    }
}
```

In the preceding sample output, the {{PRE\_SIGNED\_URL}} is the URL that you uploaded the CSV file to. The {{ROLE\_ARN}} is the CloudWatch Logs role ARN that you received when you created the role.

#### Listing your user import jobs
<a name="cognito-user-pools-using-import-tool-cli-listing-user-import-jobs"></a>

To list your user import jobs, use the following command:

```
aws cognito-idp list-user-import-jobs --user-pool-id "{{USER_POOL_ID}}" --max-results 2
```

**Example Sample response:**  

```
{
    "UserImportJobs": [
        {
            "Status": "Created",
            "SkippedUsers": 0,
            "UserPoolId": "{{USER_POOL_ID}}",
            "ImportedUsers": 0,
            "JobName": "{{JOB_NAME}}",
            "JobId": "{{JOB_ID}}",
            "PreSignedUrl":"{{PRE_SIGNED_URL}}",
            "CloudWatchLogsRoleArn":"{{ROLE_ARN}}",
            "FailedUsers": 0,
            "CreationDate": 1470957431.965
        },
        {
            "CompletionDate": 1470954227.701,
            "StartDate": 1470954226.086,
            "Status": "Failed",
            "UserPoolId": "{{USER_POOL_ID}}",
            "ImportedUsers": 0,
            "SkippedUsers": 0,
            "JobName": "{{JOB_NAME}}",
            "CompletionMessage": "Too many users have failed or been skipped during the import.",
            "JobId": "{{JOB_ID}}",
            "PreSignedUrl":"{{PRE_SIGNED_URL}}",
            "CloudWatchLogsRoleArn":"{{ROLE_ARN}}",
            "FailedUsers": 5,
            "CreationDate": 1470953929.313
        }
    ],
    "PaginationToken": "{{PAGINATION_TOKEN}}"
}
```

Jobs are listed in chronological order from last created to first created. The {{PAGINATION\_TOKEN}} string after the second job indicates that there are additional results for this list command. To list the additional results, use the `--pagination-token` option as follows:

```
aws cognito-idp list-user-import-jobs --user-pool-id "{{USER_POOL_ID}}" --max-results 10 --pagination-token "{{PAGINATION_TOKEN}}"
```

#### Starting a user import job
<a name="cognito-user-pools-using-import-tool-cli-starting-user-import-job"></a>

To start a user import job, use the following command:

```
aws cognito-idp start-user-import-job --user-pool-id "{{USER_POOL_ID}}" --job-id "{{JOB_ID}}"
```

Only one import job can be active at a time per account.

**Example Sample response:**  

```
{
    "UserImportJob": {
        "Status": "Pending",
        "StartDate": 1470957851.483,
        "UserPoolId": "{{USER_POOL_ID}}",
        "ImportedUsers": 0,
        "SkippedUsers": 0,
        "JobName": "{{JOB_NAME}}",
        "JobId": "{{JOB_ID}}",
        "PreSignedUrl":"{{PRE_SIGNED_URL}}",
        "CloudWatchLogsRoleArn": "{{ROLE_ARN}}",
        "FailedUsers": 0,
        "CreationDate": 1470957431.965
    }
}
```

#### Stopping a user import job
<a name="cognito-user-pools-using-import-tool-cli-stopping-user-import-job"></a>

To stop a user import job while it is in progress, use the following command. After you stop the job, it cannot be restarted.

```
aws cognito-idp stop-user-import-job --user-pool-id "{{USER_POOL_ID}}" --job-id "{{JOB_ID}}"
```

**Example Sample response:**  

```
{
    "UserImportJob": {
        "CompletionDate": 1470958050.571,
        "StartDate": 1470958047.797,
        "Status": "Stopped",
        "UserPoolId": "{{USER_POOL_ID}}",
        "ImportedUsers": 0,
        "SkippedUsers": 0,
        "JobName": "{{JOB_NAME}}",
        "CompletionMessage": "The Import Job was stopped by the developer.",
        "JobId": "{{JOB_ID}}",
        "PreSignedUrl":"{{PRE_SIGNED_URL}}",
        "CloudWatchLogsRoleArn": "{{ROLE_ARN}}",
        "FailedUsers": 0,
        "CreationDate": 1470957972.387
    }
}
```

## Viewing the user pool import results in the CloudWatch console
<a name="cognito-user-pools-using-import-tool-cloudwatch"></a>

You can view the results of your import job in the Amazon CloudWatch console.

**Topics**
+ [Viewing the results](#cognito-user-pools-using-import-tool-viewing-the-results)
+ [Interpreting the results](#cognito-user-pools-using-import-tool-interpreting-the-results)

### Viewing the results
<a name="cognito-user-pools-using-import-tool-viewing-the-results"></a>

The following steps describe how to view the user pool import results.

**To view the results of the user pool import**

1. Sign in to the AWS Management Console and open the CloudWatch console at [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/).

1. Choose **Logs**.

1. Choose the log group for your user pool import jobs. The log group name is in the form `/aws/cognito/userpools/{{USER_POOL_ID}}/{{USER_POOL_NAME}}`.

1. Choose the log for the user import job you just ran. The log name is in the form {{JOB\_ID}}/{{JOB\_NAME}}. The results in the log refer to your users by line number. No user data is written to the log. For each user, a line similar to the following appears:
   + `[SUCCEEDED] Line Number 5956 - The import succeeded.`
   + `[SKIPPED] Line Number 5956 - The user already exists.`
   + `[FAILED] Line Number 5956 - The User Record does not set any of the auto verified attributes to true. (Example: email_verified to true).`

### Interpreting the results
<a name="cognito-user-pools-using-import-tool-interpreting-the-results"></a>

Successfully imported users have their status set to "PasswordReset".

In the following cases, the user will not be imported, but the import job will continue:
+ No auto-verified attributes are set to `true`.
+ The user data doesn't match the schema.
+ The user couldn't be imported due to an internal error.

In the following cases, the import job will fail:
+ The Amazon CloudWatch Logs role cannot be assumed, doesn't have the correct access policy, or has been deleted.
+ The user pool has been deleted.
+ Amazon Cognito is unable to parse the .csv file.

## Requiring imported users to reset their passwords
<a name="cognito-user-pools-using-import-tool-password-reset"></a>

If your user pool only offers password-based sign-in, users must reset their passwords after they are imported. The first time they sign in, they can enter *any* password. Amazon Cognito prompts them to enter a new password in the API response to the sign-in request from your application.

If your user pool has passwordless authentication factors, Amazon Cognito defaults to those for imported users. They're not prompted for a new password, and can sign in immediately with a passwordless email or SMS OTP. You can also prompt users to set a password so that they can complete other sign-in methods like username-password and passkey. The following conditions apply to passwordless sign-in after user import.

1. You must import users with an attribute that corresponds to an available passwordless sign-in factor. If users can sign in with an email address, you must import an `email` attribute. If a phone number, you must import a `phone_number` attribute. If both, import a value for either attribute.

1. Normally, users import in a `RESET_REQUIRED` state where they must reset their password. If they are imported with the ability to sign in with a passwordless factor, Amazon Cognito sets their state to `CONFIRMED`.

For more information about passwordless authentication including how to set it up and how to construct the authentication flow in your application, see [Authentication with Amazon Cognito user pools](authentication.md).

The following procedure describes the user experience in a custom-built login mechanism with local users in a `RESET_REQUIRED` after you import a CSV file. If your users sign in with managed login, instruct them to select the **Forgot password?** option, provide the code from their email or text message, and set a password.

**Requiring imported users to reset their passwords**

1. In your app, silently attempt sign-in for the current user with `InitiateAuth` using a random password.

1. Amazon Cognito returns a `NotAuthorizedException` when `PreventUserExistenceErrors` is enabled. Otherwise, it returns `PasswordResetRequiredException`.

1. Your app makes a `ForgotPassword` API request and resets the user's password.

   1. The app submits the username in a `ForgotPassword` API request.

   1. Amazon Cognito sends a code to the verified email or phone number. The destination depends on the values you provided for `email_verified` and `phone_number_verified` in your CSV file. The response to the `ForgotPassword` request indicates the destination of the code.
**Note**  
Your user pool must be configured to verify emails or phone numbers. For more information, see [Signing up and confirming user accounts](signing-up-users-in-your-app.md).

   1. Your app displays a message to your user to check the location where the code was sent, and prompts your user to enter the code and a new password.

   1. The user enters the code and new password in the app.

   1. The app submits the code and new password in a `ConfirmForgotPassword` API request.

   1. Your app redirects your user to sign-in.

## Importing users with password hashes
<a name="cognito-user-pools-import-password-hash"></a>

When you migrate users from an existing authentication system to Amazon Cognito, you can import their password hashes along with their user attributes. Your users can then sign in immediately with their existing passwords, without a password reset. After users sign in for the first time, Amazon Cognito transparently migrates their credentials to the native Amazon Cognito authentication system.

**Important**  
Password hash import is not available for all user pools at this time. Password hash import requires the modern Amazon Cognito infrastructure with enhanced capabilities and scalability. Some user pools are still on a previous infrastructure and AWS will upgrade them to the new infrastructure, which unlocks this feature. In the Amazon Cognito console, eligible user pools display the password hashing algorithm option when creating import jobs, and ineligible pools do not display this option. For more information, see [Amazon Cognito unlocks advanced capabilities with next-generation infrastructure](https://aws.amazon.com/blogs/security/amazon-cognito-unlocks-advanced-capabilities-with-next-generation-infrastructure/) in the AWS Security Blog.

### How password hash import works
<a name="cognito-user-pools-import-password-hash-overview"></a>

With password hash import, you can migrate users while preserving their ability to sign in with their existing passwords. The import process works as follows:

1. You create an import job and specify the password hashing algorithm that your source system used to create the password hashes.

1. You include the `password_hash` column in your CSV file with each user's password hash value.

1. Amazon Cognito imports users with their password hashes and creates them with a `CONFIRMED` status. Users can sign in immediately.

1. When a user signs in for the first time, Amazon Cognito verifies their password against the imported hash. After successful verification, Amazon Cognito migrates the user's credentials to the native authentication system.

1. All subsequent sign-ins use the native Amazon Cognito authentication system.

**Important**  
All password hashes in a single import job must use the same algorithm. You specify the algorithm at the job level when you create the import job.

**Note**  
Until a user completes their first sign-in and Amazon Cognito migrates their credentials, you can't use Secure Remote Password (SRP) authentication for that user. Use `USER_PASSWORD_AUTH` or `ADMIN_USER_PASSWORD_AUTH` flows for users with imported password hashes who haven't yet signed in.

### Supported password hashing algorithms
<a name="cognito-user-pools-import-password-hash-algorithms"></a>

Amazon Cognito supports the following password hashing algorithms for import:

`BCRYPT`  
The bcrypt adaptive hash function. Amazon Cognito extracts all required parameters (salt, cost factor) from the hash string.  
**Format:** `$2<a/b/x/y>$[cost]$[22-char salt][31-char hash]`  
**Example:** `$2b$10$CtA.Rcu/szzn9U00wpUjOuN3vrgJRZycv4aOzcP3GzqzO8UDPEFq6`  
**Maximum cost factor:** 12

`SCRYPT`  
The scrypt password-based key derivation function. Amazon Cognito extracts all required parameters from the hash string.  
**Format:** `N$r$p$hexSalt$hexHash`  
**Example:** `65536$8$1$304dbaef7c5e828dc19c98f0600d18fe$4f69c498c12cd102d057356facf8d77e8d42407090491ea32c5b038f5a18c099`  
**Maximum parameters:** N (CPU/memory cost) = 65536, r (block size) = 8, p (parallelism) = 1

`ARGON2ID`  
The Argon2id password hashing algorithm. Amazon Cognito extracts all required parameters from the hash string.  
**Format:** `$argon2id$v=N$m=M,t=T,p=P$salt$hash`  
**Example:** `$argon2id$v=19$m=19456,t=2,p=1$ko/G5o1ms+ML08P95sQ8DA$AkVbvWSOqz7Hs3qthhWKxicOWnGLN+MBmpwc3emi5VA`  
**Maximum parameters:** m (memory in KiB) = 19456, t (iterations) = 2, p (parallelism) = 1

`PBKDF2_SHA256`  
Password-Based Key Derivation Function 2 with SHA-256. Amazon Cognito extracts all required parameters from the hash string.  
**Format:** `$pbkdf2-sha256$iterations$salt$hash`  
**Example:** `$pbkdf2-sha256$600000$1XZlmwLQ2hhM3JYuCPiArQ$Pfheg9Zi/v5lXU4yyLA0WFUYEd/rlaVbzrM9oMD6IrA`  
**Maximum iterations:** 600000

**Note**  
All supported algorithms are self-describing, which means Amazon Cognito can extract all required parameters (such as salt, cost factor, and iterations) directly from the hash string. You only need to specify the algorithm name when you create the import job.

If your password hash has parameter values that exceed the maximum bounds listed above, the import fails for that user. Review your source system's password hashing configuration before importing to ensure compatibility.

### Adding password hashes to your CSV file
<a name="cognito-user-pools-import-password-hash-csv"></a>

When you download the CSV template for user import, the template includes a `password_hash` column. Populate this column with the password hash values for users you want to import with their existing passwords.

**CSV formatting rules for password hash import**
+ The `password_hash` column is required when your import job specifies a password hashing algorithm. If you leave the value empty for a specific user, Amazon Cognito imports that user without a password and sets the user to the `RESET_REQUIRED` state.
+ If your import job specifies a password hashing algorithm but your CSV file doesn't include a `password_hash` column, the job fails.
+ If a password hash value is malformed or doesn't match the expected format for the specified algorithm, the import fails for that user. Amazon Cognito doesn't create the user and records the failure in your Amazon CloudWatch Logs logs.
+ Password hash values are case-sensitive. Make sure they match the exact format that the algorithm expects.

**Example Sample CSV with password hashes**  
The following example shows a CSV file that imports users with bcrypt password hashes:  

```
cognito:username,email,email_verified,phone_number,phone_number_verified,password_hash
alejandro_rosalez,alejandro_rosalez@example.com,TRUE,+12345550100,TRUE,$2b$10$CtA.Rcu/szzn9U00wpUjOuN3vrgJRZycv4aOzcP3GzqzO8UDPEFq6
mary_major,mary_major@example.com,TRUE,+12345550199,TRUE,$2b$10$CtA.Rcu/szzn9U00wpUjOuN3vrgJRZycv4aOzcP3GzqzO8UDPEFq6
```

### Creating an import job with password hashes (AWS CLI)
<a name="cognito-user-pools-import-password-hash-create-job"></a>

To import users with password hashes, you must specify the password hashing algorithm when you create the import job. All users in the import job must use the same algorithm.

Use the following AWS Command Line Interface command to create an import job with password hashes. The `--password-hashing-algorithm` parameter specifies the algorithm used to create the password hashes in your CSV file.

```
aws cognito-idp create-user-import-job \
    --job-name "{{JOB_NAME}}" \
    --user-pool-id "{{USER_POOL_ID}}" \
    --cloud-watch-logs-role-arn "{{ROLE_ARN}}" \
    --password-hashing-algorithm {{BCRYPT}}
```

Replace {{BCRYPT}} with one of the supported algorithms: `BCRYPT`, `SCRYPT`, `ARGON2ID`, or `PBKDF2_SHA256`.

**Example Sample response**  

```
{
    "UserImportJob": {
        "Status": "Created",
        "SkippedUsers": 0,
        "UserPoolId": "{{USER_POOL_ID}}",
        "ImportedUsers": 0,
        "JobName": "{{JOB_NAME}}",
        "JobId": "{{JOB_ID}}",
        "PreSignedUrl": "{{PRE_SIGNED_URL}}",
        "CloudWatchLogsRoleArn": "{{ROLE_ARN}}",
        "PasswordHashingAlgorithm": "BCRYPT",
        "FailedUsers": 0,
        "CreationDate": 1470957431.965
    }
}
```

The response includes the `PasswordHashingAlgorithm` field confirming the algorithm you specified. Upload your CSV file to the presigned URL and start the job as described in [Uploading the CSV file](#cognito-user-pools-using-import-tool-cli-uploading-csv-file).

### User experience after password hash import
<a name="cognito-user-pools-import-password-hash-user-experience"></a>

Users imported with password hashes have the following experience:
+ **Immediate sign-in:** Users can sign in with their existing passwords immediately after import. Users don't receive a prompt to reset their passwords.
+ **User status:** Amazon Cognito creates these users with a `CONFIRMED` status instead of `RESET_REQUIRED`.
+ **Transparent migration:** When users sign in for the first time, Amazon Cognito verifies their password against the imported hash. After successful verification, Amazon Cognito migrates their credentials to the native authentication system. All subsequent sign-ins use the native system.
+ **Initial sign-in latency:** The first sign-in for users with imported password hashes might take slightly longer than subsequent sign-ins. Amazon Cognito must verify the password against the imported hash and migrate the credentials to the native authentication system.
+ **Password reset:** If a user resets their password before their first sign-in, their imported password hash is replaced with a new password using the native Amazon Cognito authentication system.

### Troubleshooting password hash import errors
<a name="cognito-user-pools-import-password-hash-errors"></a>

If a password hash import fails for a user, Amazon Cognito records the failure in your Amazon CloudWatch Logs logs. Common error scenarios include:

Malformed hash  
The password hash doesn't match the expected format for the specified algorithm. Verify that the hash format is correct and matches one of the formats listed in [Supported password hashing algorithms](#cognito-user-pools-import-password-hash-algorithms).

Parameter out of bounds  
The password hash contains parameter values (such as cost factor or iterations) that exceed the maximum allowed values. For users with incompatible hashes, choose one of the following options:  
+ Import those users without a password hash by leaving the `password_hash` field empty. Amazon Cognito sets them to the `RESET_REQUIRED` state and they must reset their passwords on first sign-in.
+ Use a [user migration Lambda trigger](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-lambda-migrate-user.html) to migrate those users at sign-in time instead of through CSV import.
+ Before decommissioning your source system, re-hash passwords with compatible parameters when users sign in to your existing system.

Algorithm mismatch  
The password hash was created with a different algorithm than the one specified in the import job. All hashes in a single import job must use the same algorithm. If you have users with different algorithms, create separate import jobs for each algorithm.

Missing password\_hash column  
You specified a password hashing algorithm when creating the job, but your CSV file doesn't include the `password_hash` column. Add the column to your CSV file or create a new job without specifying an algorithm.

When a password hash import fails for a user, Amazon Cognito doesn't create the user. Other users in the import job continue to be processed. Review your Amazon CloudWatch Logs logs to identify which users failed and the reason for each failure.

### Security considerations for password hash import
<a name="cognito-user-pools-import-password-hash-security"></a>

Amazon Cognito applies additional security measures to imported password hashes:
+ **Double hashing:** Amazon Cognito re-hashes all imported password hashes with an additional layer of cryptographic protection before storage, regardless of the original algorithm's strength.
+ **Automatic migration:** After successful first authentication, Amazon Cognito migrates the user's credentials to the native Secure Remote Password (SRP) protocol used by Amazon Cognito. This ensures all users eventually use the native high-security authentication mechanism.
+ **Data cleanup:** After the import job completes, Amazon Cognito removes the uploaded CSV file containing password hashes from temporary storage.

**Important**  
Treat your CSV file containing password hashes as sensitive data. Protect it in transit and delete it securely after the import completes.