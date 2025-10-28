# Tagging profiling groups

A _tag_ is a custom attribute label that you or AWS assigns to an AWS
resource. Each AWS tag has two parts:

- A _tag key_ (for example, `CostCenter`,
  `Environment`, `Project`, or `Secret`). Tag keys are case
  sensitive.
- An optional field known as a _tag value_. Omitting the tag value is
  the same as using an empty string. Like tag keys, tag values are case sensitive.
  Together these are known as key-value pairs.

Tags help you identify and organize your AWS resources. Many AWS services support tagging,
so you can assign the same tag to resources from different services to indicate that the
resources are related. For example, you can assign the same tag to a profiling group that you
assign to an S3 bucket. For more information about using tags, see the [Tagging best
practices](https://d1.awsstatic.com/whitepapers/aws-tagging-best-practices.pdf "https://d1.awsstatic.com/whitepapers/aws-tagging-best-practices.pdf") whitepaper.

In CodeGuru Profiler, the primary resource is the profiling group. You can use the CodeGuru Profiler console, the
AWS CLI, CodeGuru Profiler APIs, or AWS SDKs to add, manage, and remove tags for a profiling group. In
addition to identifying, organizing, and tracking your profiling group with tags, you can use
tags in IAM policies to help control who can view and interact with your profiling
group.

###### Topics

- [Add a tag to a profiling group](how-to-tag-profiling-group-add.md "how-to-tag-profiling-group-add.md")
- [View tags for a profiling group](how-to-tag-profiling-group-list.md "how-to-tag-profiling-group-list.md")
- [Edit tags for a profiling group](how-to-tag-profiling-group-update.md "how-to-tag-profiling-group-update.md")
- [Remove a tag from a profiling
  group](how-to-tag-profiling-group-delete.md "how-to-tag-profiling-group-delete.md")
