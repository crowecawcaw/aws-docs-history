# Example 1: Bucket owner granting its users bucket permissions

###### Important

Granting permissions to IAM roles is a better practice than granting permissions to
individual users.For more information about how to grant permissions to IAM roles, see
[Understanding cross-account permissions and using IAM roles](example-walkthroughs-managing-access-example4.md#access-policies-walkthrough-example4-overview "example-walkthroughs-managing-access-example4.md#access-policies-walkthrough-example4-overview").

###### Topics

- [Preparing for the walkthrough](#grant-permissions-to-user-in-your-account-step0 "#grant-permissions-to-user-in-your-account-step0")
- [Step 1: Create resources in Account A and grant permissions](#grant-permissions-to-user-in-your-account-step1 "#grant-permissions-to-user-in-your-account-step1")
- [Step 2: Test permissions](#grant-permissions-to-user-in-your-account-test "#grant-permissions-to-user-in-your-account-test")
  In this walkthrough, an AWS account owns a bucket, and the account includes an IAM user
  By default, the user has no permissions. For the user to perform any tasks, the parent
  account must grant them permissions. The bucket owner and parent account are the same.
  Therefore, to grant the user permissions on the bucket, the AWS account can use a bucket
  policy, a user policy, or both. The account owner will grant some permissions using a bucket
  policy and other permissions using a user policy.

The following steps summarize the
walkthrough:

![Diagram showing an AWS account granting permissions.](images/access-policy-ex1.png)

1. Account administrator creates a bucket policy granting a set of permissions to the
   user.
2. Account administrator attaches a user policy to the user granting additional
   permissions.
3. User then tries permissions granted via both the bucket policy and the user
   policy.
   For this example, you will need an AWS account. Instead of using the root user credentials of
   the account, you will create an administrator user (see [About using an administrator user to create resources and grant permissions](example-walkthroughs-managing-access.md#about-using-root-credentials "example-walkthroughs-managing-access.md#about-using-root-credentials")).
   We refer to the AWS account and the administrator user as shown in the following
   table.

| Account ID       | Account referred to as | Administrator user in the account |
| ---------------- | ---------------------- | --------------------------------- |
| `1111-1111-1111` | Account A              | AccountAadmin                     |

###### Note

The administrator user in this example is **AccountAadmin**, which refers to Account A, and not **AccountAdmin**.

All the tasks of creating users and granting permissions are done in the AWS Management Console. To verify
permissions, the walkthrough uses the command line tools, AWS Command Line Interface (AWS CLI) and AWS Tools for Windows PowerShell,
so you don't need to write any code.

## Preparing for the walkthrough

1.  Make sure you have an AWS account and that it has a user with administrator
    privileges.
    1. Sign up for an AWS account, if needed. We refer to this account as Account A.
       1. Go to [https://aws.amazon.com/s3](https://aws.amazon.com/s3 "https://aws.amazon.com/s3") and choose
          **Create
          an AWS account**.
       2. Follow the on-screen instructions.

       AWS will notify you by email when your account is active and
       available for you to use.

    2. In Account A, create an administrator user `AccountAadmin`. Using
       Account A credentials, sign in to the [IAM console](https://console.aws.amazon.com/iam/home?#home "https://console.aws.amazon.com/iam/home?#home") and
       do the following:
       1. Create user `AccountAadmin` and note the user security
          credentials.

       For instructions, see [Creating an
       IAM user in your AWS account](../../../IAM/latest/UserGuide/id_users_create.md "../../../IAM/latest/UserGuide/id_users_create.md") in the
       _IAM User Guide_. 2. Grant administrator privileges to **AccountAadmin** by attaching a
       user policy giving full access.

       For instructions, see [Managing
       IAM policies](../../../IAM/latest/UserGuide/access_policies_manage.md "../../../IAM/latest/UserGuide/access_policies_manage.md") in the
       _IAM User Guide_. 3. Note the **IAM user Sign-In URL** for
       **AccountAadmin**. You will need to use
       this URL when signing in to the AWS Management Console. For more information
       about where to find the sign-in URL, see [Sign in to the AWS Management Console as an IAM user](../../../IAM/latest/UserGuide/getting-started_how-users-sign-in.md "../../../IAM/latest/UserGuide/getting-started_how-users-sign-in.md") in
       _IAM User Guide_. Note the URL for each
       of the accounts.

2.  Set up either the AWS CLI or the AWS Tools for Windows PowerShell. Make sure that you save administrator user
    credentials as follows:

        * If using the AWS CLI, create a profile, `AccountAadmin`, in the config
         file.
        * If using the AWS Tools for Windows PowerShell, make sure you store credentials for the session as
         `AccountAadmin`.

    For instructions, see [Setting up the tools for the walkthroughs](policy-eval-walkthrough-download-awscli.md "policy-eval-walkthrough-download-awscli.md").

## Step 1: Create resources in Account A and grant permissions

Using the credentials of user `AccountAadmin` in Account A, and the special
IAM user sign-in URL, sign in to the AWS Management Console and do the following:

1. Create resources of a bucket and an IAM user
   1. In the Amazon S3 console, create a bucket. Note the AWS Region in which you created the
      bucket. For instructions, see [Creating a general purpose bucket](create-bucket-overview.md "create-bucket-overview.md").
   2. In the
      [IAM Console](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/"),
      do the following:
      1. Create a user named Dave.

      For step-by-step instructions, see [Creating IAM users (console)](../../../IAM/latest/UserGuide/id_users_create.md#id_users_create_console "../../../IAM/latest/UserGuide/id_users_create.md#id_users_create_console") in the
      _IAM User Guide_. 2. Note the `UserDave` credentials. 3. Note the Amazon Resource Name (ARN) for user Dave. In the [IAM Console](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/"), select
      the user, and the **Summary** tab provides the
      user ARN.

2. Grant permissions.

Because the bucket owner and the parent account to which the user belongs are
the same, the AWS account can grant user permissions using a bucket policy, a
user policy, or both. In this example, you do both. If the object is also owned
by the same account, the bucket owner can grant object permissions in the bucket
policy (or an IAM policy).

    1. In the Amazon S3 console, attach the following bucket policy to
     `awsexamplebucket1`.



    The policy has two statements.




    	* The first statement grants Dave the bucket operation
    	 permissions `s3:GetBucketLocation` and
    	 `s3:ListBucket`.
    	* The second statement grants the `s3:GetObject`
    	 permission. Because Account A also owns the object, the account
    	 administrator is able to grant the `s3:GetObject`
    	 permission.
    In the `Principal` statement, Dave is identified by his
     user ARN. For more information about policy elements, see [Policies and permissions in Amazon S3](access-policy-language-overview.md "access-policy-language-overview.md").



    JSON





    ```
    `{
     "Version":"2012-10-17",
     "Statement": [
     {
     "Sid": "statement1",
     "Effect": "Allow",
     "Principal": {
     "AWS": "arn:aws:iam::`111122223333`:user/Dave"
     },
     "Action": [
     "s3:GetBucketLocation",
     "s3:ListBucket"
     ],
     "Resource": [
     "arn:aws:s3:::`awsexamplebucket1`"
     ]
     },
     {
     "Sid": "statement2",
     "Effect": "Allow",
     "Principal": {
     "AWS": "arn:aws:iam::`111122223333`:user/Dave"
     },
     "Action": [
     "s3:GetObject"
     ],
     "Resource": [
     "arn:aws:s3:::`awsexamplebucket1`/*"
     ]
     }
     ]
    }`

    ```
    2. Create an inline policy for the user Dave by using the following
     policy. The policy grants Dave the `s3:PutObject` permission.
     You need to update the policy by providing your bucket name.



    JSON





    ```
    `{
     "Version":"2012-10-17",
     "Statement": [
     {
     "Sid": "PermissionForObjectOperations",
     "Effect": "Allow",
     "Action": [
     "s3:PutObject"
     ],
     "Resource": [
     "arn:aws:s3:::`awsexamplebucket1`/*"
     ]
     }
     ]
    }`

    ```





    For instructions, see [Managing IAMpolicies](../../../IAM/latest/UserGuide/access_policies_inline-using.md "../../../IAM/latest/UserGuide/access_policies_inline-using.md") in the
     *IAM User Guide*.
     Note
     you need to sign in to the console using Account A
     credentials.

## Step 2: Test permissions

Using Dave's credentials, verify that the permissions work. You can use either of the
following two procedures.

###### Test permissions using the AWS CLI

1. Update the AWS CLI config file by adding the following `UserDaveAccountA`
   profile. For more information, see [Setting up the tools for the walkthroughs](policy-eval-walkthrough-download-awscli.md "policy-eval-walkthrough-download-awscli.md").

```
[profile UserDaveAccountA]
aws_access_key_id = `access-key`
aws_secret_access_key = `secret-access-key`
region = `us-east-1`
```

2. Verify that Dave can perform the operations as granted in the user policy.
   Upload a sample object using the following AWS CLI `put-object`
   command.

The `--body` parameter in the command identifies the source file to upload. For
example, if the file is in the root of the C: drive on a Windows
machine, you specify `c:\HappyFace.jpg`. The
`--key` parameter provides the key name for the object.

```
aws s3api put-object --bucket `awsexamplebucket1` --key `HappyFace.jpg` --body `HappyFace.jpg` --profile UserDaveAccountA
```

Run the following AWS CLI command to get the object.

```
aws s3api get-object --bucket awsexamplebucket1 --key `HappyFace.jpg` `OutputFile.jpg` --profile UserDaveAccountA
```

###### Test permissions using the AWS Tools for Windows PowerShell

1. Store Dave's credentials as `AccountADave`. You then use these credentials to
   `PUT` and `GET` an object.

```
set-awscredentials -AccessKey `AccessKeyID` -SecretKey `SecretAccessKey` -storeas AccountADave
```

2. Upload a sample object using the AWS Tools for Windows PowerShell `Write-S3Object` command
   using user Dave's stored credentials.

```
Write-S3Object -bucketname `awsexamplebucket1` -key `HappyFace.jpg` -file `HappyFace.jpg` -StoredCredentials AccountADave
```

Download the previously uploaded object.

```
Read-S3Object -bucketname `awsexamplebucket1` -key `HappyFace.jpg` -file `Output.jpg` -StoredCredentials AccountADave
```
