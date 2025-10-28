# Tagging Amazon OpenSearch Serverless collections

Tags let you assign arbitrary information to an Amazon OpenSearch Serverless collection so you can
categorize and filter on that information. A _tag_ is a metadata label
that you assign or that AWS assigns to an AWS resource.

Each tag consists of a _key_ and a _value_. For tags that you assign, you define the key and value.
For example, you might define the key as `stage` and the value for one resource
as `test`.

With tags, you can identify and organize your AWS resources. Many AWS services support
tagging, so you can assign the same tag to resources from different services to indicate
that the resources are related. For example, you could assign the same tag to an OpenSearch Serverless
collection that you assign to an Amazon OpenSearch Service domain.

In OpenSearch Serverless, the primary resource is a collection. You can use the OpenSearch Service console, the AWS CLI,
the OpenSearch Serverless API operations, or the AWS SDKs to add, manage, and remove tags from a
collection.

## Permissions required

OpenSearch Serverless uses the following AWS Identity and Access Management Access Analyzer (IAM) permissions for tagging
collections:

- `aoss:TagResource`
- `aoss:ListTagsForResource`
- `aoss:UntagResource`
