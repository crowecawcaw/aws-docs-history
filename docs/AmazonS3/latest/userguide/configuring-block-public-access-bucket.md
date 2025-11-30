# Configuring block public access

settings for your S3 buckets

Amazon S3 Block Public Access provides settings for access points, buckets, organizations,
and accounts to help you manage public access to Amazon S3 resources. By default, new
buckets, access points, and objects do not allow public access. For more information,
see [Blocking public access to your Amazon S3
storage](access-control-block-public-access.md "access-control-block-public-access.md").

###### Note

Bucket-level Block Public Access settings work alongside organization and
account-level policies. S3 applies the most restrictive setting between bucket-level
and effective account-level configurations (which may be enforced by organization
policies if present).

You can use the S3 console, AWS CLI, AWS SDKs, and REST API to grant public access to one or more buckets. You can also block public access to buckets that are already public. For more information, see the sections below.

To configure block public access settings for every bucket in your account, see [Configuring block public
access settings for your account](configuring-block-public-access-account.md "configuring-block-public-access-account.md"). For organization-wide
centralized management, see [S3 policy](../../../organizations/latest/userguide/orgs_manage_policies_s3.md "../../../organizations/latest/userguide/orgs_manage_policies_s3.md") in the _AWS Organizations user
guide_.

For information about configuring block public access for access points, see [Performing
block public access operations on an access point](access-control-block-public-access.md#access-control-block-public-access-examples-access-point "access-control-block-public-access.md#access-control-block-public-access-examples-access-point").

Amazon S3 Block Public Access prevents the application of any settings that allow public access
to data within S3 buckets. This section describes how to edit Block Public Access settings for
one or more S3 buckets. For information about blocking public access using the AWS CLI, AWS SDKs,
and the Amazon S3 REST APIs, see [Blocking public access to your Amazon S3
storage](access-control-block-public-access.md "access-control-block-public-access.md").

You can see if your bucket is publicly accessible from the **Buckets** list, in the **IAM Access Analyzer** column. For more information, see [Reviewing bucket access using IAM Access Analyzer for S3](access-analyzer.md "access-analyzer.md").

If you see an `Error` when you list your buckets and their public
access settings, you might not have the required permissions. Check to make sure you
have the following permissions added to your user or role policy:

```
`s3:GetAccountPublicAccessBlock
s3:GetBucketPublicAccessBlock
s3:GetBucketPolicyStatus
s3:GetBucketLocation
s3:GetBucketAcl
s3:ListAccessPoints
s3:ListAllMyBuckets`
```

In some rare cases, requests can also fail because of an AWS Region
outage.

###### To edit the Amazon S3 block public access settings for a single S3 bucket

Follow these steps if you need to change the public access settings for a single S3
bucket.

1. Sign in to the AWS Management Console and open the Amazon S3 console at
   [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. In the **Bucket name** list, choose the name of the bucket that you
   want.
3. Choose **Permissions**.
4. Choose **Edit** next to **Block public access (bucket settings)** to change the public access settings for the bucket.
   For more information about the four Amazon S3 Block Public Access Settings, see [Block public access settings](access-control-block-public-access.md#access-control-block-public-access-options "access-control-block-public-access.md#access-control-block-public-access-options").
5. Choose one of the settings, and then choose
   **Save changes**.
6. When you're asked for confirmation, enter `confirm`. Then choose
   **Confirm** to save your changes.

###### Important

Even if you disable bucket-level Block Public Access settings, your bucket may still be
protected by account-level or organization-level policies. S3 always applies the most
restrictive combination of settings across all levels.

You can also change Amazon S3 Block Public Access settings when you create a bucket. For more
information, see [Creating a general purpose bucket](create-bucket-overview.md "create-bucket-overview.md").

To block public access on a bucket or to delete the public access block, use the AWS CLI service `s3api`. The bucket-level operations that use this service are as follows:

- `PutPublicAccessBlock` (for a bucket)
- `GetPublicAccessBlock` (for a bucket)
- `DeletePublicAccessBlock` (for a bucket)
- `GetBucketPolicyStatus`
  For more information and examples, see [put-public-access-block](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/put-public-access-block.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/put-public-access-block.html") in the _AWS CLI
  Reference_.

###### Note

These bucket-level operations are not restricted by organization-level
policies. However, the effective public access behavior will still be
governed by the most restrictive combination of bucket, account, and
organization settings. For more information about the hierarchy and policy
interactions, see [Using the S3 console](block-public-access-bucket.md "block-public-access-bucket.md").

Java

```

AmazonS3 client = AmazonS3ClientBuilder.standard()
	  .withCredentials(`<credentials>`)
	  .build();

client.setPublicAccessBlock(new SetPublicAccessBlockRequest()
		.withBucketName(`<bucket-name>`)
		.withPublicAccessBlockConfiguration(new PublicAccessBlockConfiguration()
				.withBlockPublicAcls(`<value>`)
				.withIgnorePublicAcls(`<value>`)
				.withBlockPublicPolicy(`<value>`)
				.withRestrictPublicBuckets(`<value>`)));

```

###### Important

This example pertains only to bucket-level operations, which
use the `AmazonS3` client class. For account-level
operations, see the following example.

Other SDKs
For information about using the other AWS SDKs, see [Developing with Amazon S3 using the AWS SDKs](../API/sdk-general-information-section.md "../API/sdk-general-information-section.md") in the _Amazon S3 API Reference_.

For information about using Amazon S3 Block Public Access through the REST APIs,
see the following topics in the _Amazon Simple Storage Service API Reference_.

- Bucket-level operations
  - [PutPublicAccessBlock](../API/API_PutPublicAccessBlock.md "../API/API_PutPublicAccessBlock.md")
  - [GetPublicAccessBlock](../API/API_GetPublicAccessBlock.md "../API/API_GetPublicAccessBlock.md")
  - [DeletePublicAccessBlock](../API/API_DeletePublicAccessBlock.md "../API/API_DeletePublicAccessBlock.md")
  - [GetBucketPolicyStatus](../API/API_GetBucketPolicyStatus.md "../API/API_GetBucketPolicyStatus.md")
