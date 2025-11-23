# Tags in AMS Accelerate

###### Contents

- [What are tags?](acc-tag-intro.md#acc-tag-what-is "acc-tag-intro.md#acc-tag-what-is")
- [How tagging works](acc-tag-intro.md#acc-tag-how-works "acc-tag-intro.md#acc-tag-how-works")
- [Customer-managed tags in Accelerate](acc-tag-req.md "acc-tag-req.md")
  - [Monitoring in Accelerate](acc-tag-req-mon.md "acc-tag-req-mon.md")
  - [Configuring tags for EC2 instances in Accelerate](acc-tag-req-ins-config.md "acc-tag-req-ins-config.md")
  - [Managing tags for backups in Accelerate](acc-tag-req-backup.md "acc-tag-req-backup.md")

- [Accelerate-managed tags](acc-tag-infra.md "acc-tag-infra.md")
- [Customer-provided tags in Accelerate](acc-tag-cust-provided.md "acc-tag-cust-provided.md")

## What are tags?

A tag is a label that you assign to an AWS resource. Each tag consists of a key and an optional value, both of
which you define.

You use tags to categorize your AWS resources in different ways, for example, by
purpose, owner, or environment. For example, you could define a set of tags for your account's
Amazon EC2 instances, which helps you track each instance's owner and stack level.

Tags don't have any semantic meaning to Amazon EC2 and are interpreted strictly as a string of characters.

To learn more, see [Tagging AWS resources](../../../general/latest/gr/aws_tagging.md "../../../general/latest/gr/aws_tagging.md").

## How tagging works

There are multiple ways to apply tags to your resources. You can tag resources directly in
the console of each AWS service when you create the resource; use AWS [Tag Editor](../../../ARG/latest/userguide/tag-editor.md "../../../ARG/latest/userguide/tag-editor.md") to
add, remove, or edit tags for multiple resources; or use provisioning tools such as CloudFormation
[Resource tag](../../../AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.md "../../../AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.md"). AMS Accelerate also provides the AMS Accelerate Resource Tagger that you use
to define rules for an automated tag lifecycle manager. For information about using Resource Tagger in AMS Accelerate, see [Accelerate Resource Tagger](acc-resource-tagger.md "acc-resource-tagger.md"). AMS Accelerate also provides customer-provided tags to add and remove custom tags to your AMS resources. For more information about customer-provided tags, see [Customer-provided tags in Accelerate](acc-tag-cust-provided.md "acc-tag-cust-provided.md").
