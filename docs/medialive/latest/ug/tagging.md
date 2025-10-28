# Tagging resources

A _tag_ is a metadata label that you assign or that AWS assigns to an
AWS resource. Each tag consists of a _key_ and a
_value_. For tags that you assign, you define the key
and value. For example, you might define the key as `stage` and the value for one
resource as `test`.

Tags help you do the following:

- Identify and organize your AWS resources. Many AWS services support tagging,
  so you can assign the same tag to resources from different services to indicate that
  the resources are related. For example, you could assign the same tag to an
  AWS Elemental MediaLive channel and an endpoint that you assign to an AWS Elemental MediaTailor
  configuration.
- Track your AWS costs. You activate these tags on the AWS Billing and Cost Management dashboard. AWS
  uses the tags to categorize your costs and deliver a monthly cost allocation report
  to you. For more information, see [Use
  Cost Allocation Tags](../../../awsaccountbilling/latest/aboutv2/cost-alloc-tags.md "../../../awsaccountbilling/latest/aboutv2/cost-alloc-tags.md") in the [AWS Billing User Guide](../../../awsaccountbilling/latest/aboutv2.md "../../../awsaccountbilling/latest/aboutv2.md").
  The following sections provide more information about tags for AWS Elemental MediaLive.

## Supported resources in MediaLive

The following resources in AWS Elemental MediaLive support tagging:

- Channels
- Inputs
- Input security groups
- AWS Elemental Link devices
- Multiplexes
- Reservations

For information about adding and managing tags, see [Managing tags](#tagging-add-edit-delete "#tagging-add-edit-delete").

## Tag restrictions

The following basic restrictions apply to tags on AWS Elemental MediaLive resources:

- Maximum number of tags that you can assign to a resource – 50
- Maximum key length – 128 Unicode characters
- Maximum value length – 256 Unicode characters
- Valid characters for key and value – a-z, A-Z, 0-9, space, and the
  following characters: \_ . : / = + - and @
- Keys and values are case sensitive
- Don't use `aws:` as a prefix for keys; it's reserved for AWS
  use

Additionally, AWS Elemental MediaLive doesn't support the tag-based access control feature
of AWS Identity and Access Management (IAM).

## Managing tags

Tags are made up of the `Key` and `Value` properties on a
resource.

You can use the AWS Management Console to manage tags. You can also use the AWS Elemental MediaLive
console, the AWS CLI, or the MediaLive API to add, edit, or delete the values for
these properties.

### Tagging using the AWS Management Console

We recommend that you manage tags by using the Tag Editor on the AWS Management Console. The
Tag Editor provides a central, unified way to create and manage your tags. The Tag
Editor provides the best results, including consistency between tags within MediaLive
and between MediaLive and other services.

For more information, see [Working with
Tag Editor](../../../awsconsolehelpdocs/latest/gsg/tag-editor.md "../../../awsconsolehelpdocs/latest/gsg/tag-editor.md") in [Getting Started with the AWS Management Console](../../../awsconsolehelpdocs/latest/gsg/getting-started.md "../../../awsconsolehelpdocs/latest/gsg/getting-started.md").

### Tagging using MediaLive

For information about managing tags using the MediaLive console, see the
following:

- [Complete channel and input details](creating-a-channel-step1.md "creating-a-channel-step1.md") – for information about
  including tags when you create a channel
- [Editing and deleting a channel](editing-deleting-channel.md "editing-deleting-channel.md") – for information about
  modifying tags in an existing channel
- [Working with inputs](creating-input.md "creating-input.md") – for information about including
  tags in an input
- [Working with input security groups](working-with-input-security-groups.md "working-with-input-security-groups.md") – for
  information about including tags in an input security group
- [Creating a multiplex and program](multiplex-create.md "multiplex-create.md") – for information about
  including tags in a multiplex

For information about managing tags using the MediaLive API, see the
following:

- [Resources](../../../mediapackage/latest/apireference/resources.md "../../../mediapackage/latest/apireference/resources.md") in the
  _AWS Elemental MediaLive API
  Reference_
