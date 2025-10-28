# Understand tag basics

You can use the Amazon Data Firehose API operations to complete the following tasks:

- Add tags to a Firehose stream.
- List the tags for your Firehose streams.
- Remove tags from a Firehose stream.
  You can use tags to categorize your Firehose streams. For example, you can
  categorize Firehose streams by purpose, owner, or environment. Because you define the
  key and value for each tag, you can create a custom set of categories to meet your
  specific needs. For example, you might define a set of tags that helps you track
  Firehose streams by owner and associated application.

The following are several examples of tags:

- `Project: `Project name``
- `Owner: `Name``
- `Purpose: Load testing`
- `Application: `Application name``
- `Environment: Production`
  If you specify tags in the `CreateDeliveryStream` action, Amazon Data Firehose
  performs an additional authorization on the
  `firehose:TagDeliveryStream` action to verify if users have
  permissions to create tags. If you do not provide this permission, requests to
  create new Firehose streams with IAM resource tags will fail with an
  `AccessDeniedException` such as following.

```
AccessDeniedException
User: arn:aws:sts::x:assumed-role/x/x is not authorized to perform: firehose:TagDeliveryStream on resource: arn:aws:firehose:us-east-1:x:deliverystream/x with an explicit deny in an identity-based policy.
```

The following example demonstrates a policy that allows users to create a
Firehose stream and apply tags.
