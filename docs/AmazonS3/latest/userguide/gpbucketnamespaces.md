

# Namespaces for general purpose buckets
<a name="gpbucketnamespaces"></a>

By default, general purpose buckets exist in a global namespace. This means that each bucket name must be unique across all AWS accounts in all the AWS Regions within a partition. A partition is a grouping of Regions. AWS currently has four partitions: `aws` (Standard Regions), `aws-cn` (China Regions), `aws-us-gov` (AWS GovCloud (US)), and `aws-eusc` (European Sovereign Cloud). When you create a general purpose bucket, you can choose to create a bucket in the shared global namespace. You can also choose to create a bucket in your account regional namespace. Your account regional namespace is a subdivision of the global namespace that only your account can create buckets in.

**Topics**
+ [Global general purpose buckets](#global-gp-buckets)
+ [Account regional namespace general purpose buckets](#account-regional-gp-buckets)
+ [Restrictions and considerations](#namespace-restrictions)
+ [AWS Region Code Format](#region-code-format)
+ [Requiring the creation of buckets in your account regional namespace](#require-account-regional)
+ [Creating a bucket in your account regional namespace](#create-account-regional-bucket)

## Global general purpose buckets
<a name="global-gp-buckets"></a>

By default, you create global general purpose buckets in the shared global namespace. After creating a general purpose bucket in the shared global namespace, that bucket name is unavailable for anyone else to create within the partition. When you delete a global general purpose bucket, the bucket name becomes available again in the global namespace for anyone to re-create.

When creating global general purpose buckets, you can request any name that adheres to the bucket naming rules. These rules include specifying a name between 3 (minimum) and 63 (maximum) characters long. The name can only consist of lowercase letters, numbers, periods (.), and hyphens (-). Bucket names must begin and end with a letter or number and cannot contain two adjacent periods. For more information on bucket naming rules, see [General purpose bucket naming rules](bucketnamingrules.md).

When specifying a global general purpose bucket name, you must select a unique name that is not already in use for the partition. If you attempt to create a bucket that already exists and is owned by someone else, you will receive an HTTP 409 BucketAlreadyExists error. If you attempt to create a bucket that already exists and is owned by you, you will receive an HTTP 409 BucketAlreadyOwnedByYou error.

You can create global general purpose buckets to have the most flexibility in selecting your requested bucket names. Since it's a shared global namespace, other accounts can create similar bucket names. Other accounts can also re-create bucket names that you previously deleted. You should not depend on specific bucket naming conventions for availability or security verification purposes. Don't write code assuming your chosen bucket name is available unless you have already created the bucket. One method for creating bucket names that aren't predictable is to append a Globally Unique Identifier (GUID) to your bucket name. For example, `amzn-s3-demo-bucket-a1b2c3d4-5678-90ab-cdef-example11111`. For more information, see [Creating a bucket that uses a GUID in the bucket name](bucketnamingrules.md#create-bucket-name-guid).

## Account regional namespace general purpose buckets
<a name="account-regional-gp-buckets"></a>

Although Amazon S3 general purpose buckets exist in a shared global namespace, you can optionally create buckets in your account regional namespace. The account regional namespace is a reserved subdivision of the global bucket namespace. Only your account can create general purpose buckets in this namespace. New general purpose buckets created in your account regional namespace are unique to your account. These buckets can never be re-created by another account. These buckets support all the S3 features and AWS services that general purpose buckets in the shared global namespace already support. Your applications require no change to interact with buckets in your account regional namespace.

**Note**  
You can create buckets in your account regional namespace in all AWS Regions except Middle East (Bahrain) and Middle East (UAE).

Creating buckets in your account regional namespace is a security best practice. These bucket names can only ever be used by your account. You can create buckets in your account regional namespace to easily template general purpose bucket names across multiple AWS Regions. You can have assurance that no other account can create bucket names in your namespace. If another account attempts to create a bucket with your account regional suffix, the CreateBucket request will be rejected.

### Account regional namespace naming convention
<a name="account-regional-naming"></a>

General purpose buckets in your account regional namespace must follow a specific naming convention. These buckets consist of a bucket name prefix that you create and a suffix that contains your 12-digit AWS Account ID, the AWS Region code, and ends with `-an`.

```
{{bucket-name-prefix}}-accountId-region-an
```

For example, the following general purpose bucket exists in the account regional namespace for AWS Account 111122223333 in the us-west-2 Region:

```
{{amzn-s3-demo-bucket}}-111122223333-us-west-2-an
```

To create a bucket in your account regional namespace, you make a CreateBucket request. Specify the `x-amz-bucket-namespace` request header with the value set to `account-regional`. Also specify an account regional namespace formatted bucket name: `<customer-chosen-name>-<AWS-Account-ID>-<AWS-Region>-an`.

**Note**  
When you create a general purpose bucket in your account regional namespace using the console, a suffix is automatically added to the bucket name prefix that you provide. This suffix includes your AWS Account ID and the AWS Region that you selected to create your bucket in. When you create a general purpose bucket in your account regional namespace using the CreateBucket API, you must provide the full suffix. This includes your AWS Account ID and the AWS Region in your request. For a list of the AWS Region codes, see [AWS Region Code Format](#region-code-format).

### Integrating the account regional namespace to your CloudFormation templates
<a name="cfn-integration"></a>

You can update your infrastructure-as-code tools, like CloudFormation, to simplify creating buckets in your account regional namespace. CloudFormation offers the pseudo parameters `AWS::AccountId` and `AWS::Region`. These parameters make it easy to build CloudFormation templates that create account regional namespace buckets. For more information, see [Get AWS values using pseudo parameters](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/pseudo-parameter-reference.html#available-pseudo-parameters).

**Example 1 using BucketName with Sub:**

```
BucketName: !Sub "amzn-s3-demo-bucket-${AWS::AccountId}-${AWS::Region}-an"
BucketNamespace: "account-regional"
```

**Example 2 using BucketNamePrefix:**

```
BucketNamePrefix: 'amzn-s3-demo-bucket'
BucketNamespace: "account-regional"
```

Alternatively, you can also use the BucketNamePrefix property to update your CloudFormation template. The BucketNamePrefix lets you simply provide the customer-defined portion of the bucket name. It then automatically adds the account regional namespace suffix based on the requesting AWS Account and AWS Region specified.

Using these options, you can build a custom CloudFormation template to easily create general purpose buckets in your account regional namespace. For more information, see [AWS::S3::Bucket](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3-bucket.html) in the CloudFormation User Guide.

## Restrictions and considerations
<a name="namespace-restrictions"></a>

When creating buckets in the shared global namespace, the following considerations apply:
+ A bucket name in the shared global namespace can't be used by another AWS account in the same partition until the bucket is deleted. After you delete a bucket in the shared global namespace, be aware that another AWS account in the same partition can use the same bucket name for a new bucket and can therefore potentially receive requests intended for the deleted bucket.
+ When building applications that will create buckets in the shared global namespace, make sure to consider that your desired bucket names may be already taken by another account and that other accounts may have bucket names that are similar to yours.
+ Because Amazon S3 identifies buckets based on their names, an application that uses an incorrect bucket name in a request could inadvertently perform operations against a different bucket than expected. To help avoid unintentional bucket interactions in situations like this, you can use bucket owner condition. For more information, see [Verifying bucket ownership with bucket owner condition](bucket-owner-condition.md).

When creating buckets in your account regional namespace, the following restrictions and considerations apply:
+ Any attempt to re-create an account regional namespace bucket that you already own in any AWS Region will return an HTTP 409 BucketAlreadyOwnedByYou error.
+ You should use the S3 regional endpoints to create buckets in your account regional namespace. For [backwards compatibility](https://docs.aws.amazon.com/AmazonS3/latest/userguide/VirtualHosting.html#VirtualHostingBackwardsCompatibility), you can use the legacy global endpoint to create buckets in your account regional namespace in the US East (N. Virginia) Region.
+ Your account regional suffix counts towards the maximum number of 63-characters allowed in general purpose bucket names. So if your account regional suffix is `-012345678910-us-east-1-an`, then you have 37-characters available for your bucket name prefix.

## AWS Region Code Format
<a name="region-code-format"></a>

To create a bucket in your account regional namespace, you must include the AWS Region in the suffix where you want to create the general purpose bucket. You must specify the full AWS Region code (for example, `us-west-2`) in the suffix. See [AWS Regions](https://docs.aws.amazon.com/global-infrastructure/latest/regions/aws-regions.html#available-regions) for an entire list of the AWS Region codes. The following bucket names show two examples of the AWS Region code format that you must use when creating buckets in your account regional namespace:
+ `amzn-s3-demo-bucket-012345678910-ap-southeast-1-an`
+ `amzn-s3-demo-bucket-987654321012-eu-north-1-an`

## Requiring the creation of buckets in your account regional namespace
<a name="require-account-regional"></a>

You can enforce that your IAM principals only create buckets in your account regional namespace. Use the `s3:x-amz-bucket-namespace` condition key. The following examples show how you can enforce account regional bucket creation in an IAM policy, Resource Control Policy, or Service Control Policy.

### IAM policy
<a name="require-iam-policy"></a>

The following IAM policy denies the s3:CreateBucket permission to the IAM principal if the request does not include the x-amz-bucket-namespace header set to account-regional.

```
{
  "Version": "2012-10-17",		 	 	 
  "Statement": [
    {
      "Sid": "RequireAccountRegionalBucketCreation",
      "Effect": "Deny",
      "Action": "s3:CreateBucket",
      "Resource": "*",
      "Condition": {
        "StringNotEquals": {
          "s3:x-amz-bucket-namespace": "account-regional"
        }
      }
    }
  ]
}
```

### Resource Control Policy
<a name="require-rcp"></a>

The following Resource Control Policy denies the s3:CreateBucket permission to everyone if the request does not include the x-amz-bucket-namespace header set to account-regional.

```
{
    "Version": "2012-10-17",		 	 	 
    "Statement": [
        {
            "Sid": "OnlyCreateBucketsInAccountRegionalNamespace",
            "Effect": "Deny",
            "Principal": "*",
            "Action": "s3:CreateBucket",
            "Resource": "*",
            "Condition": {
                "StringNotEquals": {
                    "s3:x-amz-bucket-namespace": "account-regional"
                }
            }
        }
    ]
}
```

### Service Control Policy
<a name="require-scp"></a>

The following Service Control Policy denies the s3:CreateBucket permission to everyone if the request does not include the x-amz-bucket-namespace header set to account-regional.

```
{
    "Version": "2012-10-17",		 	 	 
    "Statement": [
        {
            "Sid": "RequireAccountRegionalBucketCreation",
            "Effect": "Deny",
            "Action": "s3:CreateBucket",
            "Resource": "*",
            "Condition": {
                "StringNotEquals": {
                    "s3:x-amz-bucket-namespace": "account-regional"
                }
            }
        }
    ]
}
```

## Creating a bucket in your account regional namespace
<a name="create-account-regional-bucket"></a>

The following examples show you how to create a general purpose bucket in your account regional namespace.

### Using the AWS CLI
<a name="create-account-regional-cli"></a>

The following AWS CLI example creates a general purpose bucket in the account regional namespace for AWS Account 012345678910 in the US West (N. California) Region (us-west-1). To use this example command, replace the {{user input placeholders}} with your own information.

```
aws s3api create-bucket \
    --bucket {{amzn-s3-demo-bucket-012345678910-us-west-1-an}} \
    --bucket-namespace account-regional
    --region {{us-west-1}} \
    --create-bucket-configuration LocationConstraint={{us-west-1}}
```