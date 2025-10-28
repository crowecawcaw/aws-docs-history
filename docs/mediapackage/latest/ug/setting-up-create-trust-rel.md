# Allowing AWS Elemental MediaPackage to access other

AWS services

Some features require you to allow MediaPackage to access other AWS services, such as
Amazon S3 and AWS Secrets Manager (Secrets Manager). To allow this access, create an IAM role and policy with the
appropriate permissions. The following steps describe how to create roles and policies for
MediaPackage features.

###### Topics

- [Step 1: Create a policy](#setting-up-create-trust-rel-policy "#setting-up-create-trust-rel-policy")
- [Step 2: Create a role](#setting-up-create-trust-rel-role "#setting-up-create-trust-rel-role")
- [Step 3: Modify the trust relationship](#setting-up-create-trust-rel-trust "#setting-up-create-trust-rel-trust")

## Step 1: Create a policy

The IAM policy defines the permissions that AWS Elemental MediaPackage (MediaPackage) requires to access
other services.

- For video on demand (VOD) workflows, create a policy that allows MediaPackage to read from
  the Amazon S3 bucket, verify the billing method, and retrieve content. For the
  billing method, MediaPackage must verify that the bucket _does not_ require the requester to pay for requests.
  If the bucket has **requestPayment** enabled, MediaPackage
  can't ingest content from that bucket.
- For live-to-VOD workflows, create a policy that allows MediaPackage to read from the Amazon S3
  bucket and store the live-to-VOD asset in it.
- For content delivery network (CDN) authorization, create a policy
  that allows MediaPackage to read from a secret in Secrets Manager.

The following sections describe how to create these policies.

If you're using MediaPackage to ingest a VOD asset from an Amazon S3 bucket and to
package and deliver that asset, you need a policy that allows you to do these things
in Amazon S3:

- `GetObject` - MediaPackage can retrieve the VOD asset from the bucket.
- `GetBucketLocation` - MediaPackage can retrieve the Region for the bucket. The bucket must be in the same region as the MediaPackage VOD resources.
- `GetBucketRequestPayment` - MediaPackage can retrieve the payment request information. MediaPackage uses this information to verify that the bucket doesn't require the requester to pay for the content requests.
  If you also use MediaPackage for live-to-VOD asset harvesting, add the
  `PutObject` action to the policy. For more information the required
  policy for live-to-VOD workflows, see [Policy for live-to-VOD workflows](#setting-up-create-trust-rel-policy-ltov "#setting-up-create-trust-rel-policy-ltov").

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
                "s3:GetObject",
                "s3:GetBucketLocation",
                "s3:GetBucketRequestPayment",
                "s3:ListBucket"
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
If you use MediaPackage to harvest a live-to-VOD asset from a live stream, you need a
policy that allows you to do these things in Amazon S3:

- `PutObject`: MediaPackage can save the VOD asset in the bucket.
- `GetBucketLocation`: MediaPackage can retrieve the Region for the
  bucket. The bucket must be in the same AWS Region as the MediaPackage VOD
  resources.
  If you also use MediaPackage for VOD asset delivery, add these actions to the policy:
  `GetObject` and `GetBucketRequestPayment`. For more information
  about the required policy for VOD workflows, see [Policy for Amazon S3 access for VOD
  workflows](#setting-up-create-trust-rel-policy-vod "#setting-up-create-trust-rel-policy-vod").

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

- `GetSecretValue` - MediaPackage can retrieve the encrypted
  authorization code from a version of the secret.
- `DescribeSecret` - MediaPackage can retrieve the details of the secret,
  excluding encrypted fields.
- `ListSecrets` - MediaPackage can retrieve a list of secrets in the AWS
  account.
- `ListSecretVersionIds`: MediaPackage can retrieve all of the versions that are
  attached to the specified secret.

###### Note

You don't need a separate policy for each secret that you store in Secrets Manager. If you
create a policy like the one described in the following procedure, MediaPackage can
access all secrets in your account in this Region.

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
      "Effect": "Allow",
      "Action": [
        "secretsmanager:GetSecretValue",
        "secretsmanager:DescribeSecret",
        "secretsmanager:ListSecrets",
        "secretsmanager:ListSecretVersionIds"
      ],
      "Resource": [
        "arn:aws:secretsmanager:`region`:`account-id`:secret:`secret-name`"
      ]
    },
    {
      "Effect": "Allow",
      "Action": [
         "iam:GetRole",
         "iam:PassRole"
       ],
       "Resource": "arn:aws:iam::`account-id`:role/`role-name`"
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

## Step 2: Create a role

An [IAM role](../../../IAM/latest/UserGuide/id_roles.md "../../../IAM/latest/UserGuide/id_roles.md") is an IAM identity that
you can create in your account that has specific permissions. An IAM role is similar to
an IAM user in that it is an AWS identity with permissions policies that determine
what the identity can and cannot do in AWS. However, instead of being uniquely associated
with one person, a role is intended to be assumable by anyone who needs it. Also, a role
does not have standard long-term credentials such as a password or access keys associated
with it. Instead, when you assume a role, it provides you with temporary security credentials
for your role session.
Create a role that AWS Elemental MediaPackage assumes when ingesting
source content from Amazon S3.

When you create the role, you choose Amazon Elastic Compute Cloud (Amazon EC2) as the trusted entity that can assume the
role because MediaPackage isn't available for selection. In [Step 3: Modify the trust relationship](#setting-up-create-trust-rel-trust "#setting-up-create-trust-rel-trust"), you change the trusted entity
to MediaPackage.

For information about creating a service role, see [Creating a Role to Delegate Permissions to an AWS Service](../../../IAM/latest/UserGuide/id_roles_create_for-service.md "../../../IAM/latest/UserGuide/id_roles_create_for-service.md") in the _IAM User Guide_.

## Step 3: Modify the trust relationship

The trust relationship defines what entities can assume the role that you created in
[Step 2: Create a role](#setting-up-create-trust-rel-role "#setting-up-create-trust-rel-role"). When you created the role and
established the trusted relationship, you chose Amazon EC2 as the trusted entity. Modify the
role so that the trusted relationship is between your AWS account and
AWS Elemental MediaPackage.

###### To change the trust relationship to MediaPackage

1. Access the role that you created in [Step 2: Create a role](#setting-up-create-trust-rel-role "#setting-up-create-trust-rel-role").

If you're not already displaying the role, in the navigation pane of the IAM
console, choose **Roles**. Search for and choose the role that
you created. 2. On the **Summary** page for the role, choose **Trust
relationships**. 3. Choose **Edit trust relationship**. 4. On the **Edit Trust Relationship** page, in the
**Policy Document**, change `ec2.amazonaws.com`
to `mediapackage.amazonaws.com`.

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
 "Service": "mediapackage.amazonaws.com"
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
 "Service": [
 "mediapackage.amazonaws.com",
 "mediapackage.ap-southeast-4.amazonaws.com"
 ]
 },
 "Action": "sts:AssumeRole"
 }
 ]
}`

```

5. Choose **Update Trust Policy**.
6. On the **Summary** page, make a note of the value in
   **Role ARN**. You use this ARN when you ingest source
   content for video on demand (VOD) workflows. The ARN looks like this:

`arn:aws:iam::`111122223333`:role/`role-name``

In the example, `111122223333` is your AWS account
number.
