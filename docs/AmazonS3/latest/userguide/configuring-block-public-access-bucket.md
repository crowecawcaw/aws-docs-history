

# Configuring block public access settings for your S3 buckets
<a name="configuring-block-public-access-bucket"></a>

Amazon S3 Block Public Access provides settings for access points, buckets, organizations, and accounts to help you manage public access to Amazon S3 resources. By default, new buckets, access points, and objects do not allow public access. For more information, see [Blocking public access to your Amazon S3 storage](access-control-block-public-access.md).

**Note**  
Bucket-level Block Public Access settings work alongside organization and account-level policies. S3 applies the most restrictive setting between bucket-level and effective account-level configurations (which may be enforced by organization policies if present).

You can use the S3 console, AWS CLI, AWS SDKs, and REST API to grant public access to one or more buckets. You can also block public access to buckets that are already public. For more information, see the sections below.

To configure block public access settings for every bucket in your account, see [Configuring block public access settings for your account](configuring-block-public-access-account.md). For organization-wide centralized management, see [S3 policy](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_s3.html) in the *AWS Organizations user guide*.

For information about configuring block public access for access points, see [Performing block public access operations on an access point](access-control-block-public-access.md#access-control-block-public-access-examples-access-point).

## Using the AWS CLI
<a name="configuring-block-public-access-bucket-cli"></a>

To block public access on a bucket or to delete the public access block, use the AWS CLI service `s3api`. The bucket-level operations that use this service are as follows:
+ `PutPublicAccessBlock` (for a bucket)
+ `GetPublicAccessBlock` (for a bucket)
+ `DeletePublicAccessBlock` (for a bucket)
+ `GetBucketPolicyStatus`

For more information and examples, see [put-public-access-block](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/put-public-access-block.html) in the *AWS CLI Reference*.

**Note**  
These bucket-level operations are not restricted by organization-level policies. However, the effective public access behavior will still be governed by the most restrictive combination of bucket, account, and organization settings. For more information about the hierarchy and policy interactions, see [Using the S3 console](block-public-access-bucket.md).

## Using the AWS SDKs
<a name="configuring-block-public-access-bucket-sdk"></a>

------
#### [ Java ]

```
AmazonS3 client = AmazonS3ClientBuilder.standard()
	  .withCredentials({{<credentials>}})
	  .build();

client.setPublicAccessBlock(new SetPublicAccessBlockRequest()
		.withBucketName({{<bucket-name>}})
		.withPublicAccessBlockConfiguration(new PublicAccessBlockConfiguration()
				.withBlockPublicAcls({{<value>}})
				.withIgnorePublicAcls({{<value>}})
				.withBlockPublicPolicy({{<value>}})
				.withRestrictPublicBuckets({{<value>}})));
```

**Important**  
This example pertains only to bucket-level operations, which use the `AmazonS3` client class. For account-level operations, see the following example.

------
#### [ Other SDKs ]

For information about using the other AWS SDKs, see [Developing with Amazon S3 using the AWS SDKs](https://docs.aws.amazon.com/AmazonS3/latest/API/sdk-general-information-section.html) in the *Amazon S3 API Reference*.

------

## Using the REST API
<a name="configuring-block-public-access-bucket-api"></a>

For information about using Amazon S3 Block Public Access through the REST APIs, see the following topics in the *Amazon Simple Storage Service API Reference*.
+ Bucket-level operations
  + [PutPublicAccessBlock](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutPublicAccessBlock.html)
  + [GetPublicAccessBlock](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetPublicAccessBlock.html)
  + [DeletePublicAccessBlock](https://docs.aws.amazon.com/AmazonS3/latest/API/API_DeletePublicAccessBlock.html)
  + [GetBucketPolicyStatus](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketPolicyStatus.html)