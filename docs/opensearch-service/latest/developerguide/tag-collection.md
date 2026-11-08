

# Tagging Amazon OpenSearch Serverless collections
<a name="tag-collection"></a>

Tags let you assign arbitrary information to an Amazon OpenSearch Serverless collection so you can categorize and filter on that information. A *tag* is a metadata label that you assign or that AWS assigns to an AWS resource. 

Each tag consists of a *key* and a *value*. For tags that you assign, you define the key and value. For example, you might define the key as `stage` and the value for one resource as `test`.

With tags, you can identify and organize your AWS resources. Many AWS services support tagging, so you can assign the same tag to resources from different services to indicate that the resources are related. For example, you could assign the same tag to an OpenSearch Serverless collection that you assign to an Amazon OpenSearch Service domain.

In OpenSearch Serverless, the primary resource is a collection. You can use the OpenSearch Service console, the AWS CLI, the OpenSearch Serverless API operations, or the AWS SDKs to add, manage, and remove tags from a collection.

## Permissions required
<a name="collection-tag-permissions"></a>

OpenSearch Serverless uses the following AWS Identity and Access Management (IAM) permissions for tagging collections:
+ `aoss:TagResource`
+ `aoss:ListTagsForResource`
+ `aoss:UntagResource`

AWS CloudFormation and AWS Cloud Control API call `aoss:ListTagsForResource` whenever they read a collection, such as when you create, update, or import a collection, detect drift, or call `GetResource`. If the IAM principal that performs the operation doesn't have this permission, the operation fails with an `AccessDenied` error. Deleting or listing collections doesn't require it.

When CloudFormation adds, changes, or removes tags, including tags that it propagates from the stack, the principal needs `aoss:TagResource` or `aoss:UntagResource`. CloudFormation updates tags in place, without replacing the collection. For more information, see [AWS::OpenSearchServerless::Collection](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-opensearchserverless-collection.html) in the *CloudFormation Template Reference Guide*.