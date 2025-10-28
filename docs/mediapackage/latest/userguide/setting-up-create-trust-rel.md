# Allowing MediaPackage to access other

AWS services

Some features require you to allow MediaPackage to access other AWS services, such as
Amazon S3 and AWS Secrets Manager (Secrets Manager). To allow this access, create an IAM role and policy with the
appropriate permissions. The following steps describe how to create roles and policies for
MediaPackage features.

###### Steps

- [Step 1: Create a policy](#setting-up-create-trust-rel-policy "#setting-up-create-trust-rel-policy")
- [Step 2: Create a role](#setting-up-create-trust-rel-role "#setting-up-create-trust-rel-role")
- [Step 3: Modify the trust relationship](#setting-up-create-trust-rel-trust "#setting-up-create-trust-rel-trust")

## Step 1: Create a policy

The IAM policy defines the permissions that AWS Elemental MediaPackage (MediaPackage) requires to access
other services.

- For live-to-VOD workflows, create a policy that allows MediaPackage to read from the Amazon S3
  bucket and store the live-to-VOD asset in it.
- For content delivery network (CDN) authorization with static headers, create a policy that
  allows MediaPackage to read from a secret in Secrets Manager and a key in AWS Key Management Service (AWS KMS). This
  policy is _not_ needed if you're using AWS
  Signature Version 4 (SigV4) authentication.

Use the following instructions to set up the policies that you need.

If you use MediaPackage to harvest a live-to-VOD asset from a live stream, you need a
policy that allows you to do these things in Amazon S3:

- `PutObject`: MediaPackage can save the VOD asset in the bucket.
- `GetBucketLocation`: MediaPackage can retrieve the Region for the
  bucket. The bucket must be in the same AWS Region as the MediaPackage VOD
  resources.

###### To use the JSON policy editor to create a policy

1. Sign in to the AWS Management Console and open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. In the navigation pane on the left, choose **Policies**.

If this is your first time choosing **Policies**, the
**Welcome to Managed Policies** page appears. Choose **Get
Started**. 3. At the top of the page, choose **Create policy**. 4. In the **Policy editor** section, choose the
**JSON** option. 5. Enter the following JSON policy document:

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Action": [
                "s3:PutObject",
                "s3:ListBucket",
                "s3:GetBucketLocation"
            ],
            "Resource": [
                "arn:aws:s3:::`bucket_name`/*",
                "arn:aws:s3:::`bucket_name`"
            ],
            "Effect": "Allow"
        }
    ]
}
```

6. Choose **Next**.

###### Note

You can switch between the **Visual** and **JSON**
editor options anytime. However, if you make changes or choose **Next**
in the **Visual** editor, IAM might restructure your policy to
optimize it for the visual editor. For more information, see [Policy restructuring](../../../IAM/latest/UserGuide/troubleshoot_policies.md#troubleshoot_viseditor-restructure "../../../IAM/latest/UserGuide/troubleshoot_policies.md#troubleshoot_viseditor-restructure")
in the _IAM User Guide_. 7. On the **Review and create** page, enter a **Policy
name** and a **Description** (optional) for the policy that
you are creating. Review **Permissions defined in this policy** to see
the permissions that are granted by your policy. 8. Choose **Create policy** to save your new policy.
If you use content delivery network (CDN) authorization headers to restrict access to
your endpoints in MediaPackage, you need a policy that allows you to do these things in
Secrets Manager:

- `GetSecretValue` - MediaPackage can retrieve the encrypted authorization code
  from a version of the secret that's in Secrets Manager.
- `DescribeSecret` - MediaPackage can retrieve the details of the secret from
  Secrets Manager, excluding encrypted fields.
- `BatchGetSecretValue` - MediaPackage can retrieve a list of secrets from
  Secrets Manager.
  The following permissions are required only if you customer-managed AWS KMS key. If you use
  the default key that AWS KMS creates, you don't need to manually add permissions. AWS KMS
  automatically adds the appropriate permissions for default keys.

- `Decrypt`: MediaPackage can decrypt the key from AWS KMS.
- `DescribeKey`: MediaPackage can retrieve the details of the key from
  AWS KMS.

###### To use the JSON policy editor to create a policy

1. Sign in to the AWS Management Console and open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. In the navigation column on the left, choose **Policies**.

If this is your first time choosing **Policies**, the
**Welcome to Managed Policies** page appears. Choose **Get
Started**. 3. At the top of the page, choose **Create policy**. 4. Choose the **JSON** tab. 5. Enter the following JSON policy document, replacing
`region`, `account-id`,
`secret-name`, and `key-name`
with your own information:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "secretsmanager:GetSecretValue",
 "secretsmanager:DescribeSecret"
 ],
 "Resource": "arn:aws:secretsmanager:`us-east-1`:`111122223333`:secret:`secret-name`-AbCDeF"
 },
 {
 "Effect": "Allow",
 "Action": [
 "secretsmanager:BatchGetSecretValue"
 ],
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "kms:Decrypt",
 "kms:DescribeKey"
 ],
 "Resource": "arn:aws:kms:`us-east-1`:`111122223333`:key/`key-name`"
 }
 ]
}`

```

6. Choose **Review policy**.

###### Note

You can switch between the **Visual editor** and
**JSON** tabs any time. However, if you make changes or choose
**Review policy** in the **Visual editor** tab,
IAM might restructure your policy to optimize it for the visual editor. For more
information, see [Policy restructuring](../../../IAM/latest/UserGuide/troubleshoot_policies.md#troubleshoot_viseditor-restructure "../../../IAM/latest/UserGuide/troubleshoot_policies.md#troubleshoot_viseditor-restructure")
in the _IAM User Guide_. 7. On the **Review policy** page, enter a **Name** and an optional
**Description** for the policy that you are creating. Review
the policy **Summary** to see the permissions that are granted by your
policy. Then choose **Create policy** to save your work.

## Step 2: Create a role

An [IAM role](../../../IAM/latest/UserGuide/id_roles.md "../../../IAM/latest/UserGuide/id_roles.md") is an IAM identity that
you can create in your account that has specific permissions. An IAM role is similar to
an IAM user in that it is an AWS identity with permissions policies that determine
what the identity can and cannot do in AWS. However, instead of being uniquely associated
with one person, a role is intended to be assumable by anyone who needs it. Also, a role
does not have standard long-term credentials such as a password or access keys associated
with it. Instead, when you assume a role, it provides you with temporary security credentials
for your role session.

Create a role that AWS Elemental MediaPackage assumes when ingesting source content or reading secrets
and keys for CDN authorization. When you create the role, MediaPackage isn't available to pick
as the trusted entity to assume the role. Choose Amazon Elastic Compute Cloud (Amazon EC2) temporarily instead.
In the [next step](#setting-up-create-trust-rel-trust "#setting-up-create-trust-rel-trust"), you change
the trusted entity to MediaPackage.

For information about creating a service role, see [Creating a Role to Delegate
Permissions to an AWS Service](../../../IAM/latest/UserGuide/id_roles_create_for-service.md "../../../IAM/latest/UserGuide/id_roles_create_for-service.md") in the
_IAM User Guide_.

## Step 3: Modify the trust relationship

The trust relationship defines what entities can assume the role that you created in
[Step 2: Create a role](#setting-up-create-trust-rel-role "#setting-up-create-trust-rel-role"). When you created the role and
established the trusted relationship, you chose Amazon EC2 as the trusted entity. Modify the
role so that the trusted relationship is between your AWS account and
AWS Elemental MediaPackage.

###### To change the trust relationship to MediaPackage

1. Access the role that you created in [the previous step](#setting-up-create-trust-rel-role "#setting-up-create-trust-rel-role").

If you're not already displaying the role, in the navigation pane of the IAM
console, choose **Roles**. Search for and choose the role that
you created. 2. On the **Summary** page for the role, choose **Trust
relationships**. 3. Choose **Edit trust relationship**. 4. On the **Edit Trust Relationship** page, in the
**Policy Document**, change `ec2.amazonaws.com`
to `mediapackagev2.amazonaws.com`.

The policy document should now look like this:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "",
 "Effect": "Allow",
 "Principal": {
 "Service": "mediapackagev2.amazonaws.com"
 },
 "Action": "sts:AssumeRole"
 }
 ]
}`

```

If you're using MediaPackage and related services in an opt-in Region, the Region
must be listed in the `Service` section of the policy document. For
example, if you're using services in the Asia Pacific (Melbourne) Region, the
policy document looks like this:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "",
 "Effect": "Allow",
 "Principal": {
 "Service": ["mediapackagev2.amazonaws.com","mediapackagev2.ap-southeast-4.amazonaws.com"]
 },
 "Action": "sts:AssumeRole"
 }
 ]
}`

```

For a list of opt-in Regions, see [AWS opt-in Regions](regions-and-endpoints.md#opt-in-region-considerations "regions-and-endpoints.md#opt-in-region-considerations"). 5. Choose **Update Trust Policy**. 6. On the **Summary** page, make a note of the value in
**Role ARN**. You use this ARN when you ingest source
content for video on demand (VOD) workflows or set up CDN authorization. The ARN
looks like this:

`arn:aws:iam::`111122223333`:role/`role-name``

In the example, `111122223333` is your AWS account
number.
