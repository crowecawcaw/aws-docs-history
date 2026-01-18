# Prerequisites for integrating RDS for SQL Server with S3

Before you begin, find or create the S3 bucket that you want to use. Also, add permissions so that the RDS DB instance can access the S3 bucket.
To configure this access, you create both an IAM policy and an IAM role.

###### To create an IAM policy for access to Amazon S3

1. In the [IAM Management Console](https://console.aws.amazon.com/iam/home?#home "https://console.aws.amazon.com/iam/home?#home"), choose
   **Policies** in the navigation pane.
2. Create a new policy, and use the **Visual editor** tab for the following steps.
3. For **Service**, enter `S3` and then choose the **S3**
   service.
4. For **Actions**, choose the following to grant the access that your DB instance
   requires:
   - `ListAllMyBuckets` – required
   - `ListBucket` – required
   - `GetBucketAcl` – required
   - `GetBucketLocation` – required
   - `GetObject` – required for downloading files from S3 to
     `D:\S3\`
   - `PutObject` – required for uploading files from `D:\S3\` to
     S3
   - `ListMultipartUploadParts` – required for uploading files from
     `D:\S3\` to S3
   - `AbortMultipartUpload` – required for uploading files from
     `D:\S3\` to S3

5. For **Resources**, the options that display depend on which actions you choose in the
   previous step. You might see options for **bucket**, **object**, or both. For
   each of these, add the appropriate Amazon Resource Name (ARN).

For **bucket**, add the ARN for the bucket that you want to use. For example, if your bucket
is named `amzn-s3-demo-bucket`, set the ARN to `arn:aws:s3:::`amzn-s3-demo-bucket``.

For **object**, enter the ARN for the bucket and then choose one of the following:

    * To grant access to all files in the specified bucket, choose **Any** for both
     **Bucket name** and **Object name**.
    * To grant access to specific files or folders in the bucket, provide ARNs for the specific buckets and
     objects that you want SQL Server to access.

6. Follow the instructions in the console until you finish creating the policy.

The preceding is an abbreviated guide to setting up a policy. For more detailed instructions on creating IAM
policies, see [Creating IAM
policies](../../../IAM/latest/UserGuide/access_policies_create.md "../../../IAM/latest/UserGuide/access_policies_create.md") in the _IAM User Guide._

###### To create an IAM role that uses the IAM policy from the previous procedure

1.  In the [IAM Management Console](https://console.aws.amazon.com/iam/home?#home "https://console.aws.amazon.com/iam/home?#home"), choose
    **Roles** in the navigation pane.
2.  Create a new IAM role, and choose the following options as they appear in the console:

        * **AWS service**
        * **RDS**
        * **RDS – Add Role to Database**

    Then choose **Next:Permissions** at the bottom.

3.  For **Attach permissions policies**, enter the name of the IAM policy that you previously
    created. Then choose the policy from the list.
4.  Follow the instructions in the console until you finish creating the role.

The preceding is an abbreviated guide to setting up a role. If you want more detailed instructions on creating
roles, see [IAM roles](../../../IAM/latest/UserGuide/id_roles.md "../../../IAM/latest/UserGuide/id_roles.md") in the
_IAM User Guide._
To grant Amazon RDS access to an Amazon S3 bucket, use the following process:

1. Create an IAM policy that grants Amazon RDS access to an S3 bucket.
2. Create an IAM role that Amazon RDS can assume on your behalf to access your S3 buckets.

For more information, see [Creating a role to delegate
permissions to an IAM user](../../../IAM/latest/UserGuide/id_roles_create_for-user.md "../../../IAM/latest/UserGuide/id_roles_create_for-user.md") in the _IAM User Guide_. 3. Attach the IAM policy that you created to the IAM role that you created.

###### To create the IAM policy

Include the appropriate actions to grant the access your DB instance requires:

- `ListAllMyBuckets` – required
- `ListBucket` – required
- `GetBucketAcl` – required
- `GetBucketLocation` – required
- `GetObject` – required for downloading files from S3 to
  `D:\S3\`
- `PutObject` – required for uploading files from `D:\S3\` to S3
- `ListMultipartUploadParts` – required for uploading files from
  `D:\S3\` to S3
- `AbortMultipartUpload` – required for uploading files from `D:\S3\`
  to S3

1. The following AWS CLI command creates an IAM policy named `rds-s3-integration-policy` with these
   options. It grants access to a bucket named `amzn-s3-demo-bucket`.

For Linux, macOS, or Unix:

```
aws iam create-policy \
	 --policy-name `rds-s3-integration-policy` \
	 --policy-document '{
	        "Version": "2012-10-17",
	        "Statement": [
	            {
	                "Effect": "Allow",
	                "Action": "s3:ListAllMyBuckets",
	                "Resource": "*"
	            },
	            {
	                "Effect": "Allow",
	                "Action": [
	                    "s3:ListBucket",
	                    "s3:GetBucketAcl",
	                    "s3:GetBucketLocation"
	                ],
	                "Resource": "arn:aws:s3:::`amzn-s3-demo-bucket`"
	            },
	            {
	                "Effect": "Allow",
	                "Action": [
	                    "s3:GetObject",
	                    "s3:PutObject",
	                    "s3:ListMultipartUploadParts",
	                    "s3:AbortMultipartUpload"
	                ],
	                "Resource": "arn:aws:s3:::`amzn-s3-demo-bucket`/`key_prefix`/*"
	            }
	        ]
	    }'
```

For Windows:

Make sure to change the line endings to the ones supported by your interface (`^` instead of
`\`). Also, in Windows, you must escape all double quotes with a `\`. To avoid the
need to escape the quotes in the JSON, you can save it to a file instead and pass that in as a parameter.

First, create the `policy.json` file with the following permission policy:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": "s3:ListAllMyBuckets",
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "s3:ListBucket",
 "s3:GetBucketACL",
 "s3:GetBucketLocation"
 ],
 "Resource": "arn:aws:s3:::`amzn-s3-demo-bucket`"
 },
 {
 "Effect": "Allow",
 "Action": [
 "s3:GetObject",
 "s3:PutObject",
 "s3:ListMultipartUploadParts",
 "s3:AbortMultipartUpload"
 ],
 "Resource": "arn:aws:s3:::`amzn-s3-demo-bucket`/`key_prefix`/*"
 }
 ]
}`

```

Then use the following command to create the policy:

```
aws iam create-policy ^
     --policy-name `rds-s3-integration-policy` ^
     --policy-document file://`file_path`/assume_role_policy.json
```

2. After the policy is created, note the Amazon Resource Name (ARN) of the policy. You need the ARN for a later
   step.

###### To create the IAM role

- The following AWS CLI command creates the `rds-s3-integration-role` IAM role for this
  purpose.

For Linux, macOS, or Unix:

```
aws iam create-role \
	   --role-name `rds-s3-integration-role` \
	   --assume-role-policy-document '{
	     "Version": "2012-10-17",
	     "Statement": [
	       {
	         "Effect": "Allow",
	         "Principal": {
	            "Service": "rds.amazonaws.com"
	          },
	         "Action": "sts:AssumeRole"
	       }
	     ]
	   }'
```

For Windows:

Make sure to change the line endings to the ones supported by your interface (`^` instead of
`\`). Also, in Windows, you must escape all double quotes with a `\`. To avoid the
need to escape the quotes in the JSON, you can save it to a file instead and pass that in as a parameter.

First, create the `assume_role_policy.json` file with the following policy:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "Service": [
 "rds.amazonaws.com"
 ]
 },
 "Action": "sts:AssumeRole"
 }
 ]
}`

```

Then use the following command to create the IAM role:

```
aws iam create-role ^
     --role-name `rds-s3-integration-role` ^
     --assume-role-policy-document file://`file_path`/assume_role_policy.json
```

###### Example of using the global condition context key to create the IAM role

We recommend using the [`aws:SourceArn`](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-sourcearn "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-sourcearn") and [`aws:SourceAccount`](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-sourceaccount "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-sourceaccount") global condition context keys in
resource-based policies to limit the service's permissions to a specific resource. This is the most
effective way to protect against the [confused deputy problem](../../../IAM/latest/UserGuide/confused-deputy.md "../../../IAM/latest/UserGuide/confused-deputy.md").

You might use both global condition context keys and have the `aws:SourceArn` value contain the
account ID. In this case, the `aws:SourceAccount` value and the account in the
`aws:SourceArn` value must use the same account ID when used in the same policy
statement.

    + Use `aws:SourceArn` if you want cross-service access for a single resource.
    + Use `aws:SourceAccount` if you want to allow any resource in that account to be
     associated with the cross-service use.In the policy, make sure to use the `aws:SourceArn` global condition context key with the full

Amazon Resource Name (ARN) of the resources accessing the role. For S3 integration, make sure to include the
DB instance ARNs, as shown in the following example.

For Linux, macOS, or Unix:

```
aws iam create-role \
	   --role-name `rds-s3-integration-role` \
	   --assume-role-policy-document '{
	     "Version": "2012-10-17",
	     "Statement": [
	       {
	         "Effect": "Allow",
	         "Principal": {
	            "Service": "rds.amazonaws.com"
	          },
	         "Action": "sts:AssumeRole",
                "Condition": {
                    "StringEquals": {
                        "aws:SourceArn":"arn:aws:rds:`Region`:`my_account_ID`:db:`db_instance_identifier`"
                    }
                }
	       }
	     ]
	   }'
```

For Windows:

Add the global condition context key to `assume_role_policy.json`.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "Service": [
 "rds.amazonaws.com"
 ]
 },
 "Action": "sts:AssumeRole",
 "Condition": {
 "StringEquals": {
 "aws:SourceArn":"arn:aws:rds:`Region`:`my_account_ID`:db:`db_instance_identifier`"
 }
 }
 }
 ]
}`

```

###### To attach the IAM policy to the IAM role

- The following AWS CLI command attaches the policy to the role named `rds-s3-integration-role`.
  Replace `your-policy-arn` with the policy ARN that you noted in a previous
  step.

For Linux, macOS, or Unix:

```
aws iam attach-role-policy \
	   --policy-arn `your-policy-arn` \
	   --role-name `rds-s3-integration-role`
```

For Windows:

```
aws iam attach-role-policy ^
	   --policy-arn `your-policy-arn` ^
	   --role-name `rds-s3-integration-role`
```
