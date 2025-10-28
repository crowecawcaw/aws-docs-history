# Tagging resources

A _tag_ is a custom attribute label that you or AWS assigns to an
AWS resource. Each AWS tag has two parts:

- A _tag key_ (for example, `CostCenter`,
  `Environment`, `Project`, or `Secret`). Tag
  keys are case sensitive.
- An optional field known as a _tag value_ (for example,
  `111122223333`, `Production`, or a team name).
  Omitting the tag value is the same as using an empty string. Like tag keys, tag
  values are case sensitive.
  Together these are known as key-value pairs.

Tags help you identify and organize your AWS resources. Many AWS services support
tagging, so you can assign the same tag to resources from different services to indicate
that the resources are related. For example, you can assign the same tag to a pipeline that
you assign to an Amazon S3 source bucket.

For tips on using tags, see the [AWS
Tagging Strategies](https://aws.amazon.com/answers/account-management/aws-tagging-strategies/ "https://aws.amazon.com/answers/account-management/aws-tagging-strategies/") post on the _AWS Answers_
blog.

You can tag the following resource types in CodePipeline:

- [Tag a pipeline in CodePipeline](pipelines-tag.md "pipelines-tag.md")
- [Tag a custom action in CodePipeline](customactions-tag.md "customactions-tag.md")
  You can use the AWS CLI, CodePipeline APIs, or AWS SDKs to:

- Add tags to a pipeline, custom action, or webhook when you create it.
- Add, manage, and remove tags for a pipeline, custom action, or webhook.
  You can also use the console to add, manage, and remove tags for a pipeline.

In addition to identifying, organizing, and tracking your resource with tags, you can use
tags in IAM policies to help control who can view and interact with your resource. For
examples of tag-based access policies, see [Using tags to control access to CodePipeline
resources](tag-based-access-control.md "tag-based-access-control.md").
