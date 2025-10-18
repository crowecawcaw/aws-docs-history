# Sharing CloudTrail log files between AWS accounts

This section explains how to share CloudTrail log files between multiple AWS accounts. The
 approach you use to share logs between AWS accounts depends on the configuration of your
 S3 bucket. These are the options for sharing log files:


* **[Bucket owner enforced](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-ownership-existing-bucket.html "https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-ownership-existing-bucket.html")** – [S3 Object Ownership](https://docs.aws.amazon.com/AmazonS3/latest/userguide/about-object-ownership.html "https://docs.aws.amazon.com/AmazonS3/latest/userguide/about-object-ownership.html") is an Amazon S3 bucket-level setting that you can use to
 control ownership of objects uploaded to your bucket and to disable or enable access
 control lists (ACLs). By default, Object Ownership is set to the **Bucket
 owner enforced** setting and all ACLs are disabled. When ACLs are
 disabled, the bucket owner owns all the objects in the bucket and manages access to
 data exclusively using access management policies. When the **Bucket
 owner enforced** option is set, access is managed through the bucket policy, 
 eliminating the need for users to assume a role.
* **[Assume a role to share log files](#cloudtrail-sharing-logs-assumerole "#cloudtrail-sharing-logs-assumerole")** – If you
 haven't chosen the **Bucket owner enforced** setting, users will
 need to assume a role to access the log files in your S3 bucket.

## Share log files between accounts by assuming a role


###### Note

This section applies only to Amazon S3 buckets that are not using 
 the **Bucket owner enforced** setting.


This section explains how to share CloudTrail log files between multiple AWS accounts by assuming a role and describes 
 the scenarios for sharing log files.



* **Scenario 1**: Grant read-only access to the
 accounts that generated the log files that have been placed into your Amazon S3
 bucket.
* **Scenario 2**: Grant access to all of the log
 files in your Amazon S3 bucket to a third-party account that can analyze the log
 files for you.

###### To grant read-only access to the log files in your Amazon S3 bucket

1. [Create an IAM role](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-user.html "https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-user.html") for each account you want to share log files with. 
 You must be an administrator to grant permission.


When you create the role, do the following:




	* Choose the **Another AWS account** option.
	* Enter the twelve-digit account ID of the account to
	 be granted access.
	* Check the **Require MFA** box if you want the
	 user to provide multi-factor authentication before assuming the
	 role.
	* Choose the
	 **AmazonS3ReadOnlyAccess** policy.
	
	
	###### Note
	
	By default, the **AmazonS3ReadOnlyAccess** policy grants
	 retrieval and list rights to all Amazon S3 buckets within your account.
For details about permissions management for IAM roles, see [IAM roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html "https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html") in the IAM User Guide.
2. [Create an access policy](#cloudtrail-sharing-logs-your-accounts "#cloudtrail-sharing-logs-your-accounts") that grants read-only access to the account you want to share the log files with.
3. Instruct each account to [assume a role](#cloudtrail-sharing-logs-assume-role "#cloudtrail-sharing-logs-assume-role") to retrieve the log files.

###### To grant read-only access to the log files with a third-party account

1. [Create an IAM role](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-user.html "https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-user.html") for the third-party account you want to share log files with. 
 You must be an administrator to grant permission.


When you create the role, do the following:




	* Choose the **Another AWS account** option.
	* Enter the twelve-digit account ID of the account to
	 be granted access.
	* Enter an external ID that provides additional control over who can assume the role. 
	 For more information, see 
	 [How to Use an External ID When Granting Access to Your AWS Resources to a Third Party](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-user_externalid.html "https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-user_externalid.html") in the 
	 *IAM User Guide*.
	* Choose the
	 **AmazonS3ReadOnlyAccess** policy.
	
	
	###### Note
	
	By default, the **AmazonS3ReadOnlyAccess** policy grants
	 retrieval and list rights to all Amazon S3 buckets within your account.
2. [Create an access policy](#cloudtrail-sharing-logs-third-party "#cloudtrail-sharing-logs-third-party") that grants read-only access to the third-party account you want to share the log files with.
3. Instruct the third-party account to [assume a role](#cloudtrail-sharing-logs-assume-role "#cloudtrail-sharing-logs-assume-role") to retrieve the log files.

The following sections provide more detail about these steps.


###### Topics

* [Creating an access policy to grant access to accounts you own](#cloudtrail-sharing-logs-your-accounts "#cloudtrail-sharing-logs-your-accounts")
* [Creating an access policy to grant access to a third party](#cloudtrail-sharing-logs-third-party "#cloudtrail-sharing-logs-third-party")
* [Assuming a role](#cloudtrail-sharing-logs-assume-role "#cloudtrail-sharing-logs-assume-role")
* [Stop sharing CloudTrail log files between AWS accounts](#cloudtrail-sharing-logs-stop-sharing "#cloudtrail-sharing-logs-stop-sharing")

### Creating an access policy to grant access to accounts you own


As the Amazon S3 bucket owner, you have full control over the Amazon S3 bucket 
 to which CloudTrail writes log files for the other accounts. You want to share each business unit's log files back to
 business unit that created them. But, you don't want a unit to be able to read any other unit's log files.
 


For example, to share account B's log files with account B but not with account C, you
 must create a new IAM role in your account that specifies that account B is a trusted account.
 This role trust policy specifies that account B is trusted to assume the role created by your account, 
 and should look like the following example. The trust policy is automatically created if you
 create the role by using the console. If you use the SDK to create the role, you must supply the
 trust policy as a parameter to the `CreateRole` API. If you use the CLI to create the
 role, you must specify the trust policy in the `create-role` CLI command. 



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





You must also create an access policy to specify that account B can read from only the location to 
 which B wrote its log files. The access policy will look something like the following. Note that the
 **Resource** ARN includes the twelve-digit account ID for account B, and the prefix you 
 specified, if any, when you turned on CloudTrail for account B during the aggregation process. For more 
 information about specifying a prefix, see 
 [Create trails in additional accounts](turn-on-cloudtrail-in-additional-accounts.md "turn-on-cloudtrail-in-additional-accounts.md"). 
 


###### Important

You must ensure that the prefix in the access policy is exactly the same as the prefix
 that you specified when you turned on CloudTrail for account B. If it is not, then you must edit the
 IAM role access policy in your account to incorporate the actual prefix for account B. If the
 prefix in the role access policy is not exactly the same as the prefix you specified when you
 turned on CloudTrail in account B, then account B will not be able to access its log files. 



JSON





```
`{
 "Version":"2012-10-17", 
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "s3:Get*",
 "s3:List*"
 ],
 "Resource": "arn:aws:s3:::`amzn-s3-demo-bucket`/prefix/AWSLogs/`account-B-id`/*"
 }, 
 {
 "Effect": "Allow",
 "Action": [
 "s3:Get*",
 "s3:List*"
 ],
 "Resource": "arn:aws:s3:::`amzn-s3-demo-bucket`"
 }
 ]
}`

```





Use the preceding process for any additional accounts.


After you create roles for each account and specify the appropriate trust and access
 policies, and after an IAM user in each account has been granted access by the administrator
 of that account, an IAM user in accounts B or C can programmatically assume the role. 


For more information, see 
 [Assuming a role](#cloudtrail-sharing-logs-assume-role "#cloudtrail-sharing-logs-assume-role").
 


### Creating an access policy to grant access to a third party


You must create a separate IAM role for a third-party account. When you create the role, 
 AWS automatically creates the trust relationship,
 which specifies that third-party account will be trusted to assume the role. The access policy for the
 role specifies what actions that account can take. For more information about creating roles, 
 see [Create an IAM role](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-user.html "https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-user.html").


For example, the trust relationship created by AWS specifies that the third-party account (account Z in this example) is
 trusted to assume the role that you've created. The following is an example trust policy:



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





If you specified an external ID when you created the role for the third-party account, your access
 policy contains an added `Condition` element that tests the unique ID
 assigned by that account. The test is performed when the role is assumed. The following example
 access policy has a `Condition` element.


For more information, see [How to use an external ID when granting access 
 to your AWS resources to a third party](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-user_externalid.html "https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-user_externalid.html") in the
 *IAM User Guide*.



JSON





```
`{
 "Version":"2012-10-17", 
 "Statement": [{
 "Sid": "",
 "Effect": "Allow",
 "Principal": {"AWS": "arn:aws:iam::`111111111111`:root"},
 "Action": "sts:AssumeRole",
 "Condition": {"StringEquals": {"sts:ExternalId": "`external-ID-issued-by-account-Z`"}}
 }]
}`

```





You must also create an access policy for your account to specify that the third-party account can
 read all logs from the Amazon S3 bucket. The access policy should look something like the following
 example. The wild card (\*) at the end of the `Resource` value indicates that the third-party account 
 can access any log file in the S3 bucket to which it has been granted access.



JSON





```
`{
 "Version":"2012-10-17", 
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "s3:Get*",
 "s3:List*"
 ],
 "Resource": "arn:aws:s3:::`amzn-s3-demo-bucket`/*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "s3:Get*",
 "s3:List*"
 ],
 "Resource": "arn:aws:s3:::`amzn-s3-demo-bucket`"
 }
 ]
}`

```





After you create a role for the third-party account and specify the appropriate trust relationship and
 access policy, an IAM user in the third-party account must programmatically assume the role to be able
 to read log files from the bucket. For more information, see [Assuming a role](#cloudtrail-sharing-logs-assume-role "#cloudtrail-sharing-logs-assume-role"). 


### Assuming a role


You must designate a separate IAM user to assume each role you create in each account.
 You must then ensure that each IAM user has appropriate permissions.


#### IAM users and roles


After you create the necessary roles and policies,
 you must designate an IAM user in each of the account with which you want to share files. Each IAM user
 programmatically assumes the appropriate role to access the log files. When a user assumes a role, 
 AWS returns temporary security credentials to
 that user. They can then make requests to list, retrieve, copy, or delete log files
 depending on the permissions granted by the access policy associated with the role. 


For more information about working with IAM identities, see [IAM Identities (users, user groups, and roles)](https://docs.aws.amazon.com/IAM/latest/UserGuide/id.html "https://docs.aws.amazon.com/IAM/latest/UserGuide/id.html"). 


The primary difference in the access policy that you create
 for each IAM role in each scenario.



* In scenario 1, the access policy limits each account to reading only its
 own log files. For more information, see [Creating an access policy to grant access to accounts you own](#cloudtrail-sharing-logs-your-accounts "#cloudtrail-sharing-logs-your-accounts").
* In scenario 2, the access policy allows a third-party it to read all the
 log files that are aggregated in the Amazon S3 bucket. For more information, see
 [Creating an access policy to grant access to a third party](#cloudtrail-sharing-logs-third-party "#cloudtrail-sharing-logs-third-party").

#### Creating permissions policies for IAM users


To perform the actions permitted by a role, the IAM user must have permission to
 call the AWS STS [`AssumeRole`](https://docs.aws.amazon.com/STS/latest/APIReference/API_AssumeRole.html "https://docs.aws.amazon.com/STS/latest/APIReference/API_AssumeRole.html") API. You must edit the policy for each user to grant them the appropriate
 permissions. To do this, you set a **Resource** element in the policy
 that you attach to the IAM user. The following example shows a policy for an
 IAM user in another account that allows that user to assume a role named `Test`
 created earlier by Account A. 



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
 "Resource": "arn:aws:iam::`111122223333`:role/Test"
 }
 ]
}`

```





###### To edit a customer managed policy (console)

1. Sign in to the AWS Management Console and open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. In the navigation pane, choose **Policies**.
3. In the list of policies, choose the policy name of the policy to edit. You can use the
 search box to filter the list of policies.
4. Choose the **Permissions** tab, and then choose
 **Edit**.
5. Do one of the following:




	* Choose the **Visual** option to change your policy without
	 understanding JSON syntax. You can make changes to the service, actions, resources, or
	 optional conditions for each permission block in your policy. You can also import a
	 policy to add additional permissions to the bottom of your policy. When you are
	 finished making changes, choose **Next** to continue.
	* Choose the **JSON** option to modify your policy by typing or
	 pasting text in the JSON text box. You can also import a policy to add additional
	 permissions to the bottom of your policy. Resolve any security warnings, errors, or general warnings generated during [policy validation](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_policy-validator.html "https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_policy-validator.html"), and then choose **Next**.
	
	
	###### Note
	
	You can switch between the **Visual** and
	 **JSON** editor options any time. However, if you make changes or
	 choose **Next** in the **Visual** editor, IAM
	 might restructure your policy to optimize it for the visual editor. For more
	 information, see [Policy restructuring](https://docs.aws.amazon.com/IAM/latest/UserGuide/troubleshoot_policies.html#troubleshoot_viseditor-restructure "https://docs.aws.amazon.com/IAM/latest/UserGuide/troubleshoot_policies.html#troubleshoot_viseditor-restructure") in the *IAM User Guide*.
6. On the **Review and save** page, review **Permissions defined
 in this policy** and then choose **Save changes** to save your
 work.
7. If the managed policy already has the maximum of five versions, choosing
 **Save changes** displays a dialog box. To save your new version, the
 oldest non-default version of the policy is removed and replaced with this new version.
 Optionally, you can set the new version as the default policy version.


Choose **Save changes** to save your new policy version.

#### Calling AssumeRole


A user can assume a role by creating an application that calls the
 AWS STS [`AssumeRole`](https://docs.aws.amazon.com/STS/latest/APIReference/API_AssumeRole.html "https://docs.aws.amazon.com/STS/latest/APIReference/API_AssumeRole.html")
 API and passes the role session name, the Amazon Resource Number (ARN) of the role to
 assume, and an optional external ID. The role session name is defined by the account 
 that created the role to assume. The external ID, if any, is defined by the third-party account and
 passed to owning account for inclusion during role creation. For more information, see [How to Use an External
 ID When Granting Access to Your AWS Resources to a Third Party](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-user_externalid.html "https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-user_externalid.html") in the
 *IAM User Guide*. You can retrieve the ARN from the Account A
 by opening the IAM console.


###### To find the ARN Value in Account A with the IAM console

1. Choose **Roles**
2. Choose the role you want to examine.
3. Look for the **Role ARN** in the **Summary** section.

The AssumeRole API returns temporary credentials to use to access resources in owning
 account. In this example, the resources you want to access are the Amazon S3 bucket and the
 log files that the bucket contains. The temporary credentials have the permissions that
 you defined in the role access policy.


The following Python example (using the 
 [AWS SDK for Python (Boto)](https://aws.amazon.com/developer/tools/ "https://aws.amazon.com/developer/tools/")) 
 shows how to call `AssumeRole` and how to use the
 temporary security credentials returned to list all Amazon S3 buckets controlled by Account
 A.



```
def list_buckets_from_assumed_role(user_key, assume_role_arn, session_name):
    """
    Assumes a role that grants permission to list the Amazon S3 buckets in the account.
    Uses the temporary credentials from the role to list the buckets that are owned
    by the assumed role's account.

    :param user_key: The access key of a user that has permission to assume the role.
    :param assume_role_arn: The Amazon Resource Name (ARN) of the role that
                            grants access to list the other account's buckets.
    :param session_name: The name of the STS session.
    """
    sts_client = boto3.client(
        "sts", aws_access_key_id=user_key.id, aws_secret_access_key=user_key.secret
    )
    try:
        response = sts_client.assume_role(
            RoleArn=assume_role_arn, RoleSessionName=session_name
        )
        temp_credentials = response["Credentials"]
        print(f"Assumed role {assume_role_arn} and got temporary credentials.")
    except ClientError as error:
        print(
            f"Couldn't assume role {assume_role_arn}. Here's why: "
            f"{error.response['Error']['Message']}"
        )
        raise

    # Create an S3 resource that can access the account with the temporary credentials.
    s3_resource = boto3.resource(
        "s3",
        aws_access_key_id=temp_credentials["AccessKeyId"],
        aws_secret_access_key=temp_credentials["SecretAccessKey"],
        aws_session_token=temp_credentials["SessionToken"],
    )
    print(f"Listing buckets for the assumed role's account:")
    try:
        for bucket in s3_resource.buckets.all():
            print(bucket.name)
    except ClientError as error:
        print(
            f"Couldn't list buckets for the account. Here's why: "
            f"{error.response['Error']['Message']}"
        )
        raise



```

### Stop sharing CloudTrail log files between AWS accounts


To stop sharing log files to another AWS account, delete the role that you created
 for that account. For information about how to delete a role, see [Deleting roles or instance profiles](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_manage_delete.html "https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_manage_delete.html").
