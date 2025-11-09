# Add tags to resources in Amazon Connect

A _tag_ is a custom metadata label that you can add to a resource in
order to make it easier to identify, organize, and find in a search. Tags are comprised of
two individual parts: A tag key and a tag value. This is referred to as a
_key:value_ pair.

A _tag key_ typically represents a larger category, while a tag value
represents a subset of that category. For example you could have _tag key=Color_ and _tag value=Blue_, which would produce the key:value pair
`Color:Blue`. Note that you can set the value of a tag to an empty string,
but you can't set the value of a tag to null. Omitting the tag value is the same as using an
empty string.

Tag keys can be up to 128 characters in length and tag values can be up to 256 characters
in length; both are case sensitive. For more information, see:

- [Amazon Connect TagResource](../APIReference/API_TagResource.md "../APIReference/API_TagResource.md")
- [Amazon Connect Customer
  Profiles TagResource](../../../customerprofiles/latest/APIReference/API_TagResource.md "../../../customerprofiles/latest/APIReference/API_TagResource.md")
- [Amazon Connect Voice ID TagResource](../../../voiceid/latest/APIReference/API_TagResource.md "../../../voiceid/latest/APIReference/API_TagResource.md"): You can add tags to the Voice ID domain.
- [Amazon AppIntegrations
  TagResource](../../../appintegrations/latest/APIReference/API_TagResource.md "../../../appintegrations/latest/APIReference/API_TagResource.md")
  Amazon Connect services support up to 50 tags per resource. For a given resource, each tag key must
  be unique with only one value.

###### Note

Your tags cannot begin with `aws:` because AWS reserves this prefix for
system-generated tags. You cannot add, modify, or delete `aws:*` tags, and
they don't count against your tags-per-resource limit.

The following table describes the Amazon Connect resources that can be tagged using the AWS CLI or an
AWS SDK.

| Tagging support for Amazon Connect resources | Resource | Supports tagging using the Amazon Connect admin website | Supports tagging using the CLI/SDK | Supports tagging on creation |
| -------------------------------------------- | -------- | ------------------------------------------------------- | ---------------------------------- | ---------------------------- |
| Agent                                        | Yes      | Yes                                                     | Yes                                |
| Agent group                                  | No       | Yes                                                     | Yes                                |
| Agent group level                            | No       | No                                                      | Yes                                |
| Agent state                                  | No       | Yes                                                     | Yes                                |
| Contact                                      | No       | No                                                      | No                                 |
| Contact evaluations                          | No       | Yes                                                     | No                                 |
| Email addresses                              | Yes      | Yes                                                     | Yes                                |
| Evaluation forms                             | No       | Yes                                                     | No                                 |
| Flow                                         | Yes      | Yes                                                     | Yes                                |
| Flow module                                  | Yes      | Yes                                                     | Yes                                |
| Hours of operation                           | Yes      | Yes                                                     | Yes                                |
| Instance                                     | Yes      | Yes                                                     | Yes                                |
| Integration association                      | No       | Yes                                                     | Yes                                |
| Outbound campaign                            | No       | Yes                                                     | Yes                                |
| Phone number                                 | No       | Yes                                                     | Yes                                |
| Prompts                                      | Yes      | Yes                                                     | Yes                                |
| Queue agent                                  | No       | No                                                      | Yes                                |
| Queues                                       | Yes      | Yes                                                     | Yes                                |
| Quick connects                               | No       | Yes                                                     | Yes                                |
| Routing Profile                              | Yes      | Yes                                                     | Yes                                |
| Security profile                             | Yes      | Yes                                                     | Yes                                |
| Task template                                | No       | No                                                      | Yes                                |
| Traffic distribution group                   | No       | Yes                                                     | Yes                                |
| Transfer destination                         | No       | Yes                                                     | Yes                                |
| Use case                                     | No       | Yes                                                     | Yes                                |
| Vocabulary                                   | No       | Yes                                                     | Yes                                |

To learn more about tagging, including best practices, see [Tagging AWS resources](../../../general/latest/gr/aws_tagging.md "../../../general/latest/gr/aws_tagging.md") in the
_AWS General Reference_.

## Tag metadata are removed only when the Amazon Connect instance is

deleted

Amazon Connect retains tag metadata for resources even after the resource is deleted. The
metadata is retained as long as the Amazon Connect instance is active.

This design supports
historical reporting and access control (TBAC) use cases. Specifically, Amazon Connect uses
tag-based access control for historical metrics. If tags were removed immediately when a resource was
deleted, users who did not previously have access to those resources could
inadvertently gain access to historical metrics involving them. Retaining tags ensures
that access boundaries remain consistent over time.

Tags are removed only after the
entire Amazon Connect instance is deleted, at which point historical data access is no longer
applicable.

## Tag-based access control

To use tags to control access to resources within your AWS accounts, you need to
provide tag information in the condition element of an IAM policy. For example, to
control access to your Voice ID domain based on the tags you've assigned to it, use the
`aws:ResourceTag/key-name` condition key to specify which tag key:value
pair must be attached to the domain, in order to allow given actions for it.

For more detailed information on tag-based access control in the Amazon Connect console, see
[Apply tag-based access control in
Amazon Connect](tag-based-access-control.md "tag-based-access-control.md").

For more detailed information on tag-based access control in IAM, see [Controlling access
to AWS resources using tags](../../../IAM/latest/UserGuide/access_tags.md "../../../IAM/latest/UserGuide/access_tags.md") in the _IAM User Guide_
