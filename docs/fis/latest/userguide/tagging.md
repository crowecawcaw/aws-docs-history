# Tagging your AWS FIS resources

A _tag_ is a metadata label that either you or AWS
assigns to an AWS resource. Each tag consists of a _key_
and a _value_. For tags that you assign, you define the key
and the value. For example, you might define the key as `purpose` and the value
as `test` for a resource.

Tags help you do the following:

- Identify and organize your AWS resources. Many AWS services support tagging,
  so you can assign the same tag to resources from different services to indicate that
  the resources are related.
- Control access to your AWS resources. For more information, see [Controlling Access Using Tags](../../../IAM/latest/UserGuide/access_tags.md "../../../IAM/latest/UserGuide/access_tags.md") in the _IAM User Guide_.

## Tagging restrictions

The following basic restrictions apply to tags on AWS FIS resources:

- Maximum number of tags that you can assign to a resource: 50
- Maximum key length: 128 Unicode characters
- Maximum value length: 256 Unicode characters
- Valid characters for keys and values: a-z, A-Z, 0-9, space, and the following
  characters: \_ . : / = + - and @
- Keys and values are case sensitive
- You cannot use `aws:` as a prefix for keys, because it's reserved for AWS
  use

## Work with tags

The following AWS Fault Injection Service (AWS FIS) resources support tagging:

- Actions
- Experiments
- Experiment templates

You can use the console to work with tags for experiments and experiment templates.
For more information, see the following:

- [Tag an experiment](tag-experiment.md "tag-experiment.md")
- [Tag experiment templates](tag-experiment-template.md "tag-experiment-template.md")

You can use the following AWS CLI commands to work with tags for actions, experiments,
and experiment templates:

- [tag-resource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/fis/tag-resource.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/fis/tag-resource.html") –
  Add tags to a resource.
- [untag-resource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/fis/untag-resource.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/fis/untag-resource.html") –
  Remove tags from a resource.
- [list-tags-for-resource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/fis/list-tags-for-resource.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/fis/list-tags-for-resource.html") –
  List the tags for a specific resource.
