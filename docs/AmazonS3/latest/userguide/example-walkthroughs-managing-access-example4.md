# Example 4 - Bucket owner granting

cross-account permission to objects it does not own

###### Topics

- [Understanding
  cross-account permissions and using IAM roles](#access-policies-walkthrough-example4-overview "#access-policies-walkthrough-example4-overview")
- [Step 0: Preparing for the
  walkthrough](#access-policies-walkthrough-example4-step0 "#access-policies-walkthrough-example4-step0")
- [Step 1: Do the account A
  tasks](#access-policies-walkthrough-example4-step1 "#access-policies-walkthrough-example4-step1")
- [Step 2: Do the Account B tasks](#access-policies-walkthrough-example4-step2 "#access-policies-walkthrough-example4-step2")
- [Step 3: Do the Account C tasks](#access-policies-walkthrough-example4-step3 "#access-policies-walkthrough-example4-step3")
- [Step 4: Clean up](#access-policies-walkthrough-example4-step6 "#access-policies-walkthrough-example4-step6")
- [Related resources](#RelatedResources-managing-access-example4 "#RelatedResources-managing-access-example4")
  In this example scenario, you own a bucket and you have enabled other AWS accounts to
  upload objects. If you have applied the bucket owner enforced setting for
  S3 Object Ownership for the bucket, you will own all objects in the bucket, including
  objects written by another AWS account. This approach resolves the issue that objects are
  not owned by you, the bucket owner. Then, you can delegate permission to users in your own
  account or to other AWS accounts. Suppose the bucket owner enforced setting for
  S3 Object Ownership is not enabled. That is, your bucket can have objects that other
  AWS accounts own.

Now, suppose as a bucket owner, you need to grant cross-account permission on objects,
regardless of who the owner is, to a user in another account. For example, that user could
be a billing application that needs to access object metadata. There are two core
issues:

- The bucket owner has no permissions on those objects created by other AWS accounts. For
  the bucket owner to grant permissions on objects it doesn't own, the object owner
  must first grant permission to the bucket owner. The object owner is the
  AWS account that created the objects. The bucket owner can then delegate those
  permissions.
- The bucket owner account can delegate permissions to users in its own account (see [Example 3: Bucket owner
  granting permissions to objects it does not own](example-walkthroughs-managing-access-example3.md "example-walkthroughs-managing-access-example3.md")). However, the
  bucket owner account can't delegate permissions to other AWS accounts because
  cross-account delegation isn't supported.
  In this scenario, the bucket owner can create an AWS Identity and Access Management (IAM) role with permission to
  access objects Then, the bucket owner can grant another AWS account permission to assume
  the role, temporarily enabling it to access objects in the bucket.

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

## Understanding

cross-account permissions and using IAM roles

IAM roles enable several scenarios to delegate access to your resources, and
cross-account access is one of the key scenarios. In this example, the bucket owner,
Account A, uses an IAM role to temporarily delegate object access cross-account to
users in another AWS account, Account C. Each IAM role that you create has the
following two policies attached to it:

- A trust policy identifying another AWS account that can assume the
  role.
- An access policy defining what permissions—for example,
  `s3:GetObject`—are allowed when someone assumes the role.
  For a list of permissions you can specify in a policy, see [Policy actions
  for Amazon S3](security_iam_service-with-iam.md#security_iam_service-with-iam-id-based-policies-actions "security_iam_service-with-iam.md#security_iam_service-with-iam-id-based-policies-actions").

The AWS account identified in the trust policy then grants its user permission to
assume the role. The user can then do the following to access objects:

- Assume the role and, in response, get temporary security credentials.
- Using the temporary security credentials, access the objects in the
  bucket.

For more information about IAM roles, see [IAM Roles](../../../IAM/latest/UserGuide/id_roles.md "../../../IAM/latest/UserGuide/id_roles.md") in the _IAM User Guide_.

The following is a summary of the walkthrough
steps:

![Cross-account permissions using IAM roles.](images/access-policy-ex4.png)

1. Account A administrator user attaches a bucket policy granting Account B
   conditional permission to upload objects.
2. Account A administrator creates an IAM role, establishing trust with Account
   C, so users in that account can access Account A. The access policy attached to
   the role limits what user in Account C can do when the user accesses Account
   A.
3. Account B administrator uploads an object to the bucket owned by Account A,
   granting full-control permission to the bucket owner.
4. Account C administrator creates a user and attaches a user policy that allows
   the user to assume the role.
5. User in Account C first assumes the role, which returns the user temporary
   security credentials. Using those temporary credentials, the user then accesses
   objects in the bucket.

For this example, you need three accounts. The following table shows how we refer to
these accounts and the administrator users in these accounts. In accordance with the
IAM guidelines (see [About using an administrator user to create resources
and grant permissions](example-walkthroughs-managing-access.md#about-using-root-credentials "example-walkthroughs-managing-access.md#about-using-root-credentials")), we don't use the AWS account root user
credentials in this walkthrough. Instead, you create an administrator user in each
account and use those credentials when creating resources and granting them
permissions.

| AWS account ID   | Account referred to as | Administrator user in the account |
| ---------------- | ---------------------- | --------------------------------- |
| `1111-1111-1111` | Account A              | AccountAadmin                     |
| `2222-2222-2222` | Account B              | AccountBadmin                     |
| `3333-3333-3333` | Account C              | AccountCadmin                     |

## Step 0: Preparing for the

walkthrough

###### Note

You might want to open a text editor, and write down some of the information as you go
through the steps. In particular, you will need account IDs, canonical user IDs,
IAM user Sign-in URLs for each account to connect to the console, and Amazon
Resource Names (ARNs) of the IAM users, and roles.

1. Make sure that you have three AWS accounts and each account has one administrator user
   as shown in the table in the preceding section.
   1. Sign up for AWS accounts, as needed. We refer to these accounts as
      Account A, Account B, and Account C.
   2. Using Account A credentials, sign in to the [IAM console](https://console.aws.amazon.com/iam/home?#home "https://console.aws.amazon.com/iam/home?#home") and
      do the following to create an administrator user:
      - Create user `AccountAadmin` and note its security credentials.
        For more information about adding users, see [Creating an
        IAM user in your AWS account](../../../IAM/latest/UserGuide/id_users_create.md "../../../IAM/latest/UserGuide/id_users_create.md") in the
        _IAM User Guide_.
      - Grant administrator privileges to **AccountAadmin** by attaching a
        user policy giving full access. For instructions, see [Managing
        IAM policies](../../../IAM/latest/UserGuide/access_policies_manage.md "../../../IAM/latest/UserGuide/access_policies_manage.md") in the
        _IAM User Guide_.
      - In the IAM Console **Dashboard**, note the **IAM User
        Sign-In URL**. Users in this account must use this
        URL when signing in to the AWS Management Console. For more information, see
        [Sign in to the AWS Management Console as an IAM user](../../../IAM/latest/UserGuide/getting-started_how-users-sign-in.md "../../../IAM/latest/UserGuide/getting-started_how-users-sign-in.md") in the
        _IAM User Guide_.

   3. Repeat the preceding step to create administrator users in Account B
      and Account C.

2. For Account C, note the canonical user ID.

When you create an IAM role in Account A, the trust policy grants Account C
permission to assume the role by specifying the account ID. You can find account
information as follows:

    1. Use your AWS account ID or account alias, your IAM user name, and your password to
     sign in to the [Amazon S3
     console](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
    2. Choose the name of an Amazon S3 bucket to view the details about that
     bucket.
    3. Choose the **Permissions** tab and then choose
     **Access Control List**.
    4. In the **Access for your AWS account** section, in
     the **Account** column is a long identifier, such as
     `c1daexampleaaf850ea79cf0430f33d72579fd1611c97f7ded193374c0b163b6`.
     This is your canonical user ID.

3.  When creating a bucket policy, you will need the following information. Note these
    values:
    - **Canonical user ID of Account A**
      – When the Account A administrator grants conditional upload
      object permission to the Account B administrator, the condition
      specifies the canonical user ID of the Account A user that must get
      full-control of the objects.

    ###### Note

    The canonical user ID is the Amazon S3–only concept. It is a
    64-character obfuscated version of the account ID.
    - **User ARN for Account B administrator**
      – You can find the user ARN in the
      [IAM Console](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").You
      must select the user and find the user's ARN in the
      **Summary** tab.

    In the bucket policy, you grant `AccountBadmin` permission to upload objects
    and you specify the user using the ARN. Here's an example ARN
    value:

    ```
    arn:aws:iam::`AccountB-ID`:user/AccountBadmin
    ```

4.  Set up either the AWS Command Line Interface (CLI) or the AWS Tools for Windows PowerShell. Make sure that you save administrator
    user credentials as follows:

        * If using the AWS CLI, create profiles, `AccountAadmin` and
         `AccountBadmin`, in the config file.
        * If using the AWS Tools for Windows PowerShell, make sure that you store credentials for the session as
         `AccountAadmin` and `AccountBadmin`.

    For instructions, see [Setting up the tools for the
    walkthroughs](policy-eval-walkthrough-download-awscli.md "policy-eval-walkthrough-download-awscli.md").

## Step 1: Do the account A

tasks

In this example, Account A is the bucket owner. So user AccountAadmin in Account A
will do the following:

- Create a bucket.
- Attach a bucket policy that grants the Account B administrator permission to
  upload objects.
- Create an IAM role that grants Account C permission to assume the role so it
  can access objects in the bucket.

### Step 1.1: Sign in to the AWS Management Console

Using the IAM user Sign-in URL for Account A, first sign in to the AWS Management Console as
`AccountAadmin` user. This user will create a bucket and
attach a policy to it.

### Step 1.2: Create a

bucket and attach a bucket policy

In the Amazon S3 console, do the following:

1. Create a bucket. This exercise assumes the bucket name is
   `amzn-s3-demo-bucket1`.

For instructions, see [Creating a general purpose bucket](create-bucket-overview.md "create-bucket-overview.md"). 2. Attach the following bucket policy. The policy grants conditional
permission to the Account B administrator permission to upload
objects.

Update the policy by providing your own values for
`amzn-s3-demo-bucket1`,
`AccountB-ID`, and the
`CanonicalUserId-of-AWSaccountA-BucketOwner`.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "111",
 "Effect": "Allow",
 "Principal": {
 "AWS": "arn:aws:iam::`111122223333`:user/AccountBadmin"
 },
 "Action": "s3:PutObject",
 "Resource": "arn:aws:s3:::`amzn-s3-demo-bucket1`/*"
 },
 {
 "Sid": "112",
 "Effect": "Deny",
 "Principal": {
 "AWS": "arn:aws:iam::`111122223333`:user/AccountBadmin"
 },
 "Action": "s3:PutObject",
 "Resource": "arn:aws:s3:::`amzn-s3-demo-bucket1`/*",
 "Condition": {
 "StringNotEquals": {
 "s3:x-amz-grant-full-control": "id=`CanonicalUserId-of-AWSaccountA-BucketOwner`"
 }
 }
 }
 ]
}`

```

### Step 1.3: Create an

IAM role to allow Account C cross-account access in Account A

In the [IAM Console](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/"), create an IAM role
(`examplerole`) that grants Account C permission to assume
the role. Make sure that you are still signed in as the Account A administrator
because the role must be created in Account A.

1. Before creating the role, prepare the managed policy that defines the
   permissions that the role requires. You attach this policy to the role in a
   later step.
   1. In the navigation pane on the left, choose
      **Policies** and then choose **Create
      Policy**.
   2. Next to **Create Your Own Policy**, choose
      **Select**.
   3. Enter `access-accountA-bucket` in the
      **Policy Name** field.
   4. Copy the following access policy and paste it into the
      **Policy Document** field. The access policy
      grants the role `s3:GetObject` permission so, when the
      Account C user assumes the role, it can only perform the
      `s3:GetObject` operation.

   JSON

   ```
   `{
    "Version":"2012-10-17",
    "Statement": [
    {
    "Effect": "Allow",
    "Action": "s3:GetObject",
    "Resource": "arn:aws:s3:::`amzn-s3-demo-bucket1`/*"
    }
    ]
   }`

   ```

   5. Choose **Create Policy**.

   The new policy appears in the list of managed policies.

2. In the navigation pane on the left, choose **Roles** and
   then choose **Create New Role**.
3. Under **Select Role Type**, select **Role for
   Cross-Account Access**, and then choose the
   **Select** button next to **Provide access
   between AWS accounts you own**.
4. Enter the Account C account ID.

For this walkthrough, you don't need to require users to have multi-factor
authentication (MFA) to assume the role, so leave that option
unselected. 5. Choose **Next Step** to set the permissions that will be
associated with the role. 6. Select the checkbox next to the
**access-accountA-bucket** policy that you created, and
then choose **Next Step**.

The Review page appears so you can confirm the settings for the role
before it's created. One very important item to note on this page is the
link that you can send to your users who need to use this role. Users who
use the link go straight to the **Switch Role** page with
the Account ID and Role Name fields already filled in. You can also see this
link later on the **Role Summary** page for any
cross-account role. 7. Enter `examplerole` for the role name, and then choose
**Next
Step**. 8. After reviewing the role, choose **Create Role**.

The `examplerole` role is displayed in the list of
roles. 9. Choose the role name `examplerole`. 10. Select the **Trust Relationships** tab. 11. Choose **Show policy document** and verify the trust
policy shown matches the following policy.

The following trust policy establishes trust with Account C, by allowing
it the `sts:AssumeRole` action. For more information, see [AssumeRole](../../../STS/latest/APIReference/API_AssumeRole.md "../../../STS/latest/APIReference/API_AssumeRole.md")
in the _AWS Security Token Service API Reference_.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "",
 "Effect": "Allow",
 "Principal": {
 "AWS": "arn:aws:iam::`111122223333`:root"
 },
 "Action": "sts:AssumeRole"
 }
 ]
}`

```

12. Note the Amazon Resource Name (ARN) of the `examplerole` role
    that you created.

Later in the following steps, you attach a user policy to allow an
IAM user to assume this role, and you identify the role by the ARN value.

## Step 2: Do the Account B tasks

The example bucket owned by Account A needs objects owned by other accounts. In this step, the
Account B administrator uploads an object using the command line tools.

- Using the `put-object` AWS CLI command, upload an object to
  `amzn-s3-demo-bucket1`.

```
aws s3api put-object --bucket ``amzn-s3-demo-bucket1`` --key `HappyFace.jpg` --body `HappyFace.jpg` --grant-full-control id="`canonicalUserId-ofTheBucketOwner`" --profile `AccountBadmin`
```

Note the following:

    + The `--Profile` parameter specifies the `AccountBadmin` profile,
     so the object is owned by Account B.
    + The parameter `grant-full-control`
     grants the bucket owner full-control permission on the object as
     required by the bucket policy.
    + The `--body` parameter identifies the source file to upload. For example, if
     the file is on the C: drive of a Windows computer, you
     specify `c:\HappyFace.jpg`.

## Step 3: Do the Account C tasks

In the preceding steps, Account A has already created a role, `examplerole`,
establishing trust with Account C. This role allows users in Account C to access Account
A. In this step, the Account C administrator creates a user (Dave) and delegates him the
`sts:AssumeRole` permission it received from Account A. This approach
allows Dave to assume the `examplerole` and temporarily gain access to
Account A. The access policy that Account A attached to the role limits what Dave can do
when he accesses Account A—specifically, get objects in
`amzn-s3-demo-bucket1`.

### Step 3.1: Create a user in Account C and

delegate permission to assume examplerole

1. Using the IAM user sign-in URL for Account C, first sign in to the AWS Management Console as
   `AccountCadmin` user.
2. In the [IAM Console](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/"), create a user, Dave.

For step-by-step instructions, see
[Creating IAM users (AWS Management Console)](../../../IAM/latest/UserGuide/id_users_create.md#id_users_create_console "../../../IAM/latest/UserGuide/id_users_create.md#id_users_create_console") in the _IAM User Guide_. 3. Note the Dave credentials. Dave will need these credentials to assume the
`examplerole` role. 4. Create an inline policy for the Dave IAM user to delegate the
`sts:AssumeRole` permission to Dave on the
`examplerole` role in Account A.

    1. In the navigation pane on the left, choose **Users**.
    2. Choose the user name **Dave**.
    3. On the user details page, select the **Permissions** tab and then expand the
     **Inline Policies** section.
    4. Choose **click here** (or **Create User Policy**).
    5. Choose **Custom Policy**, and then choose **Select**.
    6. Enter a name for the policy in the **Policy Name** field.
    7. Copy the following policy into the **Policy Document** field.


    You must update the policy by providing the
     ``AccountA-ID``.



    JSON





    ```
    `{
     "Version":"2012-10-17",
     "Statement": [
     {
     "Effect": "Allow",
     "Action": [
     "sts:AssumeRole"
     ],
     "Resource": "arn:aws:iam::`111122223333`:role/examplerole"
     }
     ]
    }`

    ```
    8. Choose **Apply Policy**.

5. Save Dave's credentials to the config file of the AWS CLI by adding another profile,
   `AccountCDave`.

```
[profile AccountCDave]
aws_access_key_id = `UserDaveAccessKeyID`
aws_secret_access_key = `UserDaveSecretAccessKey`
region = us-west-2
```

### Step 3.2: Assume role

(examplerole) and access objects

Now Dave can access objects in the bucket owned by Account A as follows:

- Dave first assumes the `examplerole` using his own credentials. This
  will return temporary credentials.
- Using the temporary credentials, Dave will then access objects in Account A's
  bucket.

1. At the command prompt, run the following AWS CLI `assume-role` command using the
   `AccountCDave` profile.

You must update the ARN value in the command by providing the
`AccountA-ID` where
`examplerole` is defined.

```
aws sts assume-role --role-arn arn:aws:iam::`AccountA-ID`:role/examplerole --profile AccountCDave --role-session-name test
```

In response, AWS Security Token Service (AWS STS) returns temporary security credentials (access key ID,
secret access key, and a session token). 2. Save the temporary security credentials in the AWS CLI config file under the
`TempCred` profile.

```
[profile TempCred]
aws_access_key_id = `temp-access-key-ID`
aws_secret_access_key = `temp-secret-access-key`
aws_session_token = `session-token`
region = us-west-2
```

3. At the command prompt, run the following AWS CLI command to access objects using the
   temporary credentials. For example, the command specifies the head-object
   API to retrieve object metadata for the `HappyFace.jpg`
   object.

```
aws s3api get-object --bucket ``amzn-s3-demo-bucket1`` --key `HappyFace.jpg` `SaveFileAs.jpg` --profile TempCred
```

Because the access policy attached to `examplerole` allows the actions, Amazon S3
processes the request. You can try any other action on any other object in
the bucket.

If you try any other action—for example, `get-object-acl`—you will
get permission denied because the role isn't allowed that action.

```
aws s3api get-object-acl --bucket ``amzn-s3-demo-bucket1`` --key `HappyFace.jpg` --profile TempCred
```

We used user Dave to assume the role and access the object using temporary credentials.
It could also be an application in Account C that accesses objects in
`amzn-s3-demo-bucket1`. The application can obtain temporary
security credentials, and Account C can delegate the application permission
to assume `examplerole`.

## Step 4: Clean up

1. After you're done testing, you can do the following to clean up:
   1. Sign in to the [AWS Management Console](https://console.aws.amazon.com/ "https://console.aws.amazon.com/") using Account A
      credentials, and do the following:
      - In the Amazon S3 console, remove the bucket policy attached to
        `amzn-s3-demo-bucket1`. In the bucket
        **Properties**, delete the policy in the
        **Permissions** section.
      - If the bucket is created for this exercise, in the Amazon S3
        console, delete the objects and then delete the bucket.
      - In the [IAM Console](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/"), remove the `examplerole` you created in Account
        A. For step-by-step instructions, see [Deleting an IAM user](../../../IAM/latest/UserGuide/id_users_manage.md#id_users_deleting "../../../IAM/latest/UserGuide/id_users_manage.md#id_users_deleting") in the
        _IAM User Guide_.
      - In the [IAM Console](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/"), remove the **AccountAadmin** user.

2. Sign in to the [IAM Console](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/") by using Account B credentials. Delete the user
   **AccountBadmin**.
3. Sign in to the [IAM Console](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/") by using Account C credentials. Delete
   **AccountCadmin** and the user Dave.

## Related resources

For more information that's related to this walkthrough, see the following resources
in the _IAM User Guide_:

- [Creating a role to
  delegate permissions to an IAM user](../../../IAM/latest/UserGuide/id_roles_create_for-user.md "../../../IAM/latest/UserGuide/id_roles_create_for-user.md")
- [Tutorial:
  Delegate Access Across AWS accounts Using IAM Roles](../../../IAM/latest/UserGuide/tutorial-cross-account-with-roles.md "../../../IAM/latest/UserGuide/tutorial-cross-account-with-roles.md")
- [Managing IAM
  policies](../../../IAM/latest/UserGuide/access_policies_manage.md "../../../IAM/latest/UserGuide/access_policies_manage.md")
