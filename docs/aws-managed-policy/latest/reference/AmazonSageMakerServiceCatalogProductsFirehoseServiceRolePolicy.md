

# AmazonSageMakerServiceCatalogProductsFirehoseServiceRolePolicy
<a name="AmazonSageMakerServiceCatalogProductsFirehoseServiceRolePolicy"></a>

**Description**: Service role policy used by the AWS Firehose within the AWS ServiceCatalog provisioned products from Amazon SageMaker portfolio of products. Grants permissions to a set of related services including Firehose and others.

`AmazonSageMakerServiceCatalogProductsFirehoseServiceRolePolicy` is an [AWS managed policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies).

## Using this policy
<a name="AmazonSageMakerServiceCatalogProductsFirehoseServiceRolePolicy-how-to-use"></a>

You can attach `AmazonSageMakerServiceCatalogProductsFirehoseServiceRolePolicy` to your users, groups, and roles.

## Policy details
<a name="AmazonSageMakerServiceCatalogProductsFirehoseServiceRolePolicy-details"></a>
+ **Type**: Service role policy 
+ **Creation time**: February 22, 2022, 09:54 UTC 
+ **Edited time:** February 22, 2022, 09:54 UTC
+ **ARN**: `arn:aws:iam::aws:policy/service-role/AmazonSageMakerServiceCatalogProductsFirehoseServiceRolePolicy`

## Policy version
<a name="AmazonSageMakerServiceCatalogProductsFirehoseServiceRolePolicy-version"></a>

**Policy version:** v1 (default)

The policy's default version is the version that defines the permissions for the policy. When a user or role with the policy makes a request to access an AWS resource, AWS checks the default version of the policy to determine whether to allow the request. 

## JSON policy document
<a name="AmazonSageMakerServiceCatalogProductsFirehoseServiceRolePolicy-json"></a>

```
{
  "Version" : "2012-10-17",
  "Statement" : [
    {
      "Effect" : "Allow",
      "Action" : [
        "firehose:PutRecord",
        "firehose:PutRecordBatch"
      ],
      "Resource" : "arn:aws:firehose:*:*:deliverystream/sagemaker-*"
    }
  ]
}
```

## Learn more
<a name="AmazonSageMakerServiceCatalogProductsFirehoseServiceRolePolicy-learn-more"></a>
+ [Create a permission set using AWS managed policies in IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/howtocreatepermissionset.html) 
+ [Adding and removing IAM identity permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-attach-detach.html) 
+ [Understand versioning for IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-versioning.html)
+ [Get started with AWS managed policies and move toward least-privilege permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#bp-use-aws-defined-policies)