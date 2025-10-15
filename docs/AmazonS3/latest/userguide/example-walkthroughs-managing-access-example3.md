# Example 3: Bucket owner
 granting permissions to objects it does not own

###### Important

Granting permissions to IAM roles is a better practice than granting permissions to
 individual users. To learn how to do this, see [Understanding
 cross-account permissions and using IAM roles](example-walkthroughs-managing-access-example4.md#access-policies-walkthrough-example4-overview "example-walkthroughs-managing-access-example4.md#access-policies-walkthrough-example4-overview").

###### Topics

* [Step 0: Preparing
 for the walkthrough](#access-policies-walkthrough-cross-account-acl-step0 "#access-policies-walkthrough-cross-account-acl-step0")
* [Step 1: Do
 the Account A tasks](#access-policies-walkthrough-cross-account-acl-acctA-tasks "#access-policies-walkthrough-cross-account-acl-acctA-tasks")
* [Step 2: Do
 the Account B tasks](#access-policies-walkthrough-cross-account-acl-acctB-tasks "#access-policies-walkthrough-cross-account-acl-acctB-tasks")
* [Step 3: Test
 permissions](#access-policies-walkthrough-cross-account-acl-verify "#access-policies-walkthrough-cross-account-acl-verify")
* [Step 4: Clean
 up](#access-policies-walkthrough-cross-account-acl-cleanup "#access-policies-walkthrough-cross-account-acl-cleanup")
The scenario for this example is that a bucket owner wants to grant permission to access
 objects, but the bucket owner doesn't own all objects in the bucket. For this example, the
 bucket owner is trying to grant permission to users in its own account.

A bucket owner can enable other AWS accounts to upload objects. By default, the bucket
 owner doesn't own objects written to a bucket by another AWS account. Objects are owned by
 the accounts that write them to an S3 bucket. If the bucket owner doesn't own objects in the
 bucket, the object owner must first grant permission to the bucket owner using an object
 access control list (ACL). Then, the bucket owner can grant permissions to an object that
 they don't own. For more information, see [Amazon S3 bucket and object ownership](access-policy-language-overview.md#about-resource-owner "access-policy-language-overview.md#about-resource-owner").

If the bucket owner applies the bucket owner enforced setting for S3 Object Ownership for
 the bucket, the bucket owner will own all objects in the bucket, including objects written
 by another AWS account. This approach resolves the issue that objects are not owned by
 the bucket owner. Then, you can delegate permission to users in your own account or to other
 AWS accounts.

###### Note

S3 Object Ownership is an Amazon S3 bucket-level setting that you can use to both control ownership of the objects that are 
 uploaded to your bucket and to disable or enable ACLs. By default, Object Ownership is set to the Bucket owner enforced setting, 
 and all ACLs are disabled. When ACLs are disabled, the bucket owner owns all the objects in the bucket and manages access to them 
 exclusively by using access-management policies.

 A majority of modern use cases in Amazon S3 no longer require the use of ACLs. We recommend that you keep ACLs disabled, except 
 in circumstances where you need to control access for each object individually. With ACLs disabled, you can use policies 
 to control access to all objects in your bucket, regardless of who uploaded the objects to your bucket. 
 For more information, see [Controlling ownership of objects and disabling ACLs
 for your bucket](about-object-ownership.md "about-object-ownership.md").

In this example, we assume the bucket owner has not applied the
 bucket
 owner enforced setting for Object Ownership. The bucket owner delegates
 permission to users in its own account. The following is a summary of the walkthrough
 steps:


![A bucket owner granting permissions to objects it does not own.](../../../images/AmazonS3/latest/userguide/images/access-policy-ex3.png)

1. Account A administrator user attaches a bucket policy with two statements.




	* Allow cross-account permission to Account B to upload objects.
	* Allow a user in its own account to access objects in the bucket.
2. Account B administrator user uploads objects to the bucket owned by Account
 A.
3. Account B administrator updates the object ACL adding grant that gives the bucket
 owner full-control permission on the object.
4. User in Account A verifies by accessing objects in the bucket, regardless of who
 owns them.
For this example, you need two accounts. The following table shows how we refer to these
 accounts and the administrator users in these accounts. In this walkthrough, you don't use
 the account root user credentials, according to the recommended IAM guidelines. For more
 information, see [About using an administrator user to create resources
 and grant permissions](example-walkthroughs-managing-access.md#about-using-root-credentials "example-walkthroughs-managing-access.md#about-using-root-credentials"). Instead, you create an administrator in
 each account and use those credentials in creating resources and granting them
 permissions.



| AWS account ID | Account referred to as | Administrator in the account  |
| --- | --- | --- |
| `1111-1111-1111` | Account A | AccountAadmin |
| `2222-2222-2222` | Account B | AccountBadmin |

All the tasks of creating users and granting permissions are done in the AWS Management Console. To
 verify permissions, the walkthrough uses the command line tools, AWS Command Line Interface (AWS CLI) and
 AWS Tools for Windows PowerShell, so you don't need to write any code. 


## Step 0: Preparing
 for the walkthrough


1. Make sure that you have two AWS accounts and each account has one
 administrator as shown in the table in the preceding section.


	1. Sign up for an AWS account, if needed.
	2. Using Account A credentials, sign in to the [IAM Console](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/") and do
	 the following to create an administrator user:
	
	
	
	
		* Create user `AccountAadmin` and note the user's security
		 credentials. For more information about adding users, see [Creating an
		 IAM user in your AWS account](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users_create.html "https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users_create.html") in the
		 *IAM User Guide*.
		* Grant administrator permissions to **AccountAadmin** by attaching a
		 user policy that gives full access. For instructions, see [Managing
		 IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage.html "https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage.html") in the
		 *IAM User Guide*.
		* In the [IAM Console](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/") **Dashboard**, note the **IAM
		 User Sign-In URL**. Users in this account must use
		 this URL when signing in to the AWS Management Console. For more information,
		 see [How users sign in to your account](https://docs.aws.amazon.com/IAM/latest/UserGuide/getting-started_how-users-sign-in.html "https://docs.aws.amazon.com/IAM/latest/UserGuide/getting-started_how-users-sign-in.html") in
		 *IAM User Guide*.
	3. Repeat the preceding step using Account B credentials and create administrator user
	 `AccountBadmin`.
2. Set up either the AWS CLI or the Tools for Windows PowerShell. Make sure that you save the
 administrator credentials as follows:




	* If using the AWS CLI, create two profiles, `AccountAadmin`
	 and `AccountBadmin`, in the config file.
	* If using the Tools for Windows PowerShell, make sure that you store credentials for the
	 session as `AccountAadmin` and
	 `AccountBadmin`.
For instructions, see [Setting up the tools for the
 walkthroughs](policy-eval-walkthrough-download-awscli.md "policy-eval-walkthrough-download-awscli.md").

## Step 1: Do
 the Account A tasks


Perform the following steps for Account A:


### Step 1.1: Sign in to the console


Using the IAM user sign-in URL for Account A, sign in to the AWS Management Console as
 `AccountAadmin` user. This user will create a bucket and
 attach a policy to it. 


### Step
 1.2: Create a bucket and user, and add a bucket policy to grant user
 permissions


1. In the Amazon S3 console, create a bucket. This exercise assumes that the bucket is created in
 the US East (N. Virginia) AWS Region, and the name is
 ``amzn-s3-demo-bucket1``.


For instructions, see [Creating a general purpose bucket](create-bucket-overview.md "create-bucket-overview.md").
2. In the [IAM Console](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/"), create a user `Dave`. 


For step-by-step instructions, see [Creating IAM users (console)](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users_create.html#id_users_create_console "https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users_create.html#id_users_create_console") in the
 *IAM User Guide*.
3. Note the user Dave credentials.
4. In the Amazon S3 console, attach the following bucket policy to
 ``amzn-s3-demo-bucket1`` bucket. For instructions, see [Adding a bucket policy by using the Amazon S3 console](add-bucket-policy.md "add-bucket-policy.md").
 Follow
 the steps to add a bucket policy. For information about
 how to find account IDs, see [Finding your AWS account ID](https://docs.aws.amazon.com/general/latest/gr/acct-identifiers.html#FindingYourAccountIdentifiers "https://docs.aws.amazon.com/general/latest/gr/acct-identifiers.html#FindingYourAccountIdentifiers"). 


The policy grants Account B the `s3:PutObject` and `s3:ListBucket`
 permissions. The policy also grants user `Dave` the
 `s3:GetObject` permission. 



JSON





```
`{
 "Version":"2012-10-17", 
 "Statement": [
 {
 "Sid": "Statement1",
 "Effect": "Allow",
 "Principal": {
 "AWS": "arn:aws:iam::`111122223333`:root"
 },
 "Action": [
 "s3:PutObject",
 "s3:ListBucket"
 ],
 "Resource": [
 "arn:aws:s3:::amzn-s3-demo-bucket1/*",
 "arn:aws:s3:::amzn-s3-demo-bucket1"
 ]
 },
 {
 "Sid": "Statement3",
 "Effect": "Allow",
 "Principal": {
 "AWS": "arn:aws:iam::`111122223333`:user/Dave"
 },
 "Action": [
 "s3:GetObject"
 ],
 "Resource": [
 "arn:aws:s3:::amzn-s3-demo-bucket1/*"
 ]
 }
 ]
}`

```

## Step 2: Do
 the Account B tasks


Now that Account B has permissions to perform operations on Account A's bucket, the Account
 B administrator does the following:



* Uploads an object to Account A's bucket
* Adds a grant in the object ACL to allow Account A, the bucket owner, full control

###### Using the AWS CLI

1. Using the `put-object` AWS CLI command, upload an object. The `--body`
 parameter in the command identifies the source file to upload. For example, if
 the file is on the `C:` drive of a Windows machine,
 specify `c:\HappyFace.jpg`. The `--key` parameter provides
 the key name for the object. 



```
aws s3api put-object --bucket `amzn-s3-demo-bucket1` --key HappyFace.jpg --body HappyFace.jpg --profile AccountBadmin
```
2. Add a grant to the object ACL to allow the bucket owner full control of the
 object. For information about how to find a canonical user ID, see [Find the canonical user ID for your AWS account](https://docs.aws.amazon.com/accounts/latest/reference/manage-acct-identifiers.html#FindCanonicalId "https://docs.aws.amazon.com/accounts/latest/reference/manage-acct-identifiers.html#FindCanonicalId") in the *AWS Account Management Reference Guide*.



```
aws s3api put-object-acl --bucket `amzn-s3-demo-bucket1` --key HappyFace.jpg --grant-full-control id="AccountA-CanonicalUserID" --profile AccountBadmin
```

###### Using the Tools for Windows PowerShell

1. Using the `Write-S3Object` command, upload an object. 



```
Write-S3Object -BucketName `amzn-s3-demo-bucket1` -key HappyFace.jpg -file HappyFace.jpg -StoredCredentials AccountBadmin
```
2. Add a grant to the object ACL to allow the bucket owner full control of the
 object.



```
Set-S3ACL -BucketName `amzn-s3-demo-bucket1` -Key HappyFace.jpg -CannedACLName "bucket-owner-full-control" -StoredCreden
```

## Step 3: Test
 permissions


Now verify that user Dave in Account A can access the object owned by Account
 B.


###### Using the AWS CLI

1. Add user Dave credentials to the AWS CLI config file and create a new profile,
 `UserDaveAccountA`. For more information, see [Setting up the tools for the
 walkthroughs](policy-eval-walkthrough-download-awscli.md "policy-eval-walkthrough-download-awscli.md").



```
[profile UserDaveAccountA]
aws_access_key_id = `access-key`
aws_secret_access_key = `secret-access-key`
region = `us-east-1`
```
2. Run the `get-object` CLI command to download
 `HappyFace.jpg` and save it locally. You provide user Dave
 credentials by adding the `--profile` parameter.



```
aws s3api get-object --bucket `amzn-s3-demo-bucket1` --key HappyFace.jpg `Outputfile.jpg` --profile UserDaveAccountA
```

###### Using the Tools for Windows PowerShell

1. Store user Dave AWS credentials, as `UserDaveAccountA`, to
 persistent store. 



```
Set-AWSCredentials -AccessKey `UserDave-AccessKey` -SecretKey `UserDave-SecretAccessKey` -storeas UserDaveAccountA
```
2. Run the `Read-S3Object` command to download the
 `HappyFace.jpg` object and save it locally. You provide
 user Dave credentials by adding the `-StoredCredentials` parameter. 



```
Read-S3Object -BucketName `amzn-s3-demo-bucket1` -Key HappyFace.jpg -file HappyFace.jpg  -StoredCredentials UserDaveAccountA
```

## Step 4: Clean
 up


1. After you're done testing, you can do the following to clean up:


	1. Sign in to the [AWS Management Console](https://console.aws.amazon.com/ "https://console.aws.amazon.com/")
	 using Account A credentials, and do the following:
	
	
	
	
		* In the Amazon S3 console, remove the bucket policy attached to
		 `amzn-s3-demo-bucket1`. In the bucket
		 **Properties**, delete the policy in the
		 **Permissions** section.
		* If the bucket is created for this exercise, in the Amazon S3
		 console, delete the objects and then delete the bucket.
		* In the [IAM Console](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/"), remove the **AccountAadmin** user. For
		 step-by-step instructions, see [Deleting an IAM user](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users_manage.html#id_users_deleting "https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users_manage.html#id_users_deleting") in the
		 *IAM User Guide*.
2. Sign in to the [AWS Management Console](https://console.aws.amazon.com/ "https://console.aws.amazon.com/") using
 Account B credentials. In the [IAM Console](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/"), delete the user
 **AccountBadmin**.
