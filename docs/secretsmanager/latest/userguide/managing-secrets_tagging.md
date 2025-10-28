# Tagging secrets in AWS Secrets Manager

In AWS Secrets Manager, you can assign metadata to your secrets using tags. A tag is a key-value
pair that you define for a secret. Tags help you manage AWS resources and organize data,
including billing information.

With tags, you can:

- Manage, search, and filter secrets and other resources in your AWS
  account
- Control access to secrets based on attached tags
- Track and categorize expenses associated with specific secrets or projects
  For more information about using tags to control access, see [Control access to secrets using attribute-based access control (ABAC)](auth-and-access-abac.md "auth-and-access-abac.md").

To learn about cost allocation tags, see [Using AWS cost allocation
tags](../../../awsaccountbilling/latest/aboutv2/cost-alloc-tags.md "../../../awsaccountbilling/latest/aboutv2/cost-alloc-tags.md") in the AWS Billing User Guide.

For information about tag quotas and naming restrictions, see [Service quotas for Tagging](../../../general/latest/gr/arg.md#taged-reference-quotas "../../../general/latest/gr/arg.md#taged-reference-quotas")
in the _AWS General Reference guide_. Tags are case-sensitive.

Secrets Manager generates a CloudTrail log entry when you tag or untag a secret. For more information, see
[Log AWS Secrets Manager events with AWS CloudTrail](monitoring-cloudtrail.md "monitoring-cloudtrail.md").

###### Tip

Use a consistent tagging scheme across all your AWS resources. For best practices,
see the [Tagging Best
Practices](../../../whitepapers/latest/tagging-best-practices/tagging-best-practices.md "../../../whitepapers/latest/tagging-best-practices/tagging-best-practices.md") whitepaper.

## Review tag basics

You can find secrets by tags in the console, AWS CLI, and SDKs. AWS also provides the
[Resource
Groups](../../../ARG/latest/userguide/resource-groups.md "../../../ARG/latest/userguide/resource-groups.md") tool to create a custom console that consolidates and organizes your
resources based on their tags. To find secrets with a specific tag, see [Find secrets in AWS Secrets Manager](manage_search-secret.md "manage_search-secret.md").

You can use the Secrets Manager console, AWS CLI, or Secrets Manager API to:

- Create a secret with tags
- Add tags to a secret
- List the tags for your secrets
- Remove tags from a secret

You can use tags to categorize your secrets. For example, you can categorize secrets
by purpose, owner, or environment. Because you define the key and value for each tag,
you can create a custom set of categories to meet your specific needs. Here are several
examples of tags:

- `Project: Project name`
- `Owner: Name`
- `Purpose: Load testing`
- `Application: Application name`
- `Environment: Production`

## Track costs using tagging

You can use tags to categorize and track your AWS costs. When you apply tags to your
AWS resources, including secrets, your AWS cost allocation report includes usage and
costs aggregated by tags. You can apply tags that represent business categories (such as
cost centers, application names, or owners) to organize your costs across multiple
services. For more information, see [Use
Cost Allocation Tags for Custom Billing Reports](../../../awsaccountbilling/latest/aboutv2/cost-alloc-tags.md "../../../awsaccountbilling/latest/aboutv2/cost-alloc-tags.md") in the
_AWS Billing User Guide_.

## Understand tag restrictions

The following restrictions apply to tags.

###### Basic restrictions

- The maximum number of tags per resource (secret) is 50.
- Tag keys and values are case-sensitive.
- You can't change or edit tags for a deleted secret.

###### Tag key restrictions

- Each tag key must be unique. If you add a tag with a key that's already in
  use, your new tag overwrites the existing key-value pair.
- You can't start a tag key with `aws:` because this prefix is
  reserved for use by AWS. AWS creates tags that begin with this prefix on
  your behalf, but you can't edit or delete them.
- Tag keys must be between 1 and 128 Unicode characters in length.
- Tag keys must consist of the following characters: Unicode letters, digits,
  white space, and the following special characters: `_ . / = + -
@`.

###### Tag value restrictions

- Tag values must be between 0 and 255 Unicode characters in length.
- Tag values can be blank. Otherwise, they must consist of the following
  characters: Unicode letters, digits, white space, and any of the following
  special characters: `_ . / = + - @`.

## Tag secrets using the Secrets Manager console

You can manage tags for your secrets using the [Secrets Manager console](https://console.aws.amazon.com/secretsmanager "https://console.aws.amazon.com/secretsmanager").

To access the tagging features, do the following:

1. Open the Secrets Manager console.
2. In the navigation bar, choose your preferred Region.
3. On the **Secrets** page, select a secret.

###### To view the tags for a secret

- On the **Secret Details** page, choose the
  **Tags** tab.

###### To create a secret with a tag

- Follow the steps in [Create secrets](create_secret.md "create_secret.md").

###### To add or edit tags for a secret

1. On the **Secret Details** page, choose the
   **Tags** tab and then choose **Edit
   tags**.
2. Enter the tag key in the **Key** field. Optionally, enter a
   tag value in the **Value** field.
3. Choose **Save**. The new or updated tag appears in the list
   of tags.

###### Note

If the **Save** button is not enabled, the tag key or
value might not meet the tag restrictions. For more information, see [Understand tag restrictions](#tagging-restrictions "#tagging-restrictions").

###### To remove a tag from a secret

1. On the **Secret details** page, choose the
   **Tags** tab, and then choose the **Remove**
   icon next to the tag you want to remove.
2. Choose **Save** to confirm the removal, or select
   **Undo** to cancel.

## Tag secrets using the AWS CLI

### AWS CLI examples

###### Example Add a tag to a secret

The following [`tag-resource`](../../../cli/latest/reference/secretsmanager/tag-resource.md "../../../cli/latest/reference/secretsmanager/tag-resource.md") example shows how to attach a tag with
shorthand syntax.

```
aws secretsmanager tag-resource \
            --secret-id MyTestSecret \
            --tags Key=FirstTag,Value=FirstValue
```

###### Example Add multiple tags to a secret

The following [`tag-resource`](../../../cli/latest/reference/secretsmanager/tag-resource.md "../../../cli/latest/reference/secretsmanager/tag-resource.md") example attaches two key-value tags to a
secret.

```
aws secretsmanager tag-resource \
            --secret-id MyTestSecret \
            --tags '[{"Key": "FirstTag", "Value": "FirstValue"}, {"Key": "SecondTag", "Value": "SecondValue"}]'
```

###### Example Remove tags from a secret

The following [`untag-resource`](../../../cli/latest/reference/secretsmanager/untag-resource.md "../../../cli/latest/reference/secretsmanager/untag-resource.md") example removes two tags from a secret. For
each tag, both key and value are removed.

```
aws secretsmanager untag-resource \
            --secret-id MyTestSecret \
            --tag-keys '[ "FirstTag", "SecondTag"]'
```

## Tag secrets using the Secrets Manager

API

You can add, list, and remove tags using the Secrets Manager API. For examples, see the
following documentation:

- [ListSecrets](../apireference/API_ListSecrets.md "../apireference/API_ListSecrets.md"): Use
  `ListSecrets` to view the tags applied to a secret
- [TagResource](../apireference/API_TagResource.md "../apireference/API_TagResource.md"): Add tags
  to a secret
- [Untag](../apireference/API_UntagResource.md "../apireference/API_UntagResource.md"): Remove tags
  from a secret

## Tag secrets using the Secrets Manager AWS

SDK

To change tags for your secret, use the following API operations:

- [ListSecrets](../apireference/API_ListSecrets.md "../apireference/API_ListSecrets.md"): Use
  `ListSecrets` to view the tags applied to a secret
- [`TagResource`](../apireference/API_TagResource.md "../apireference/API_TagResource.md"): Add tags to a secret
- [`UntagResource`](../apireference/API_UntagResource.md "../apireference/API_UntagResource.md"): Remove tags from a secret

For more information about using the SDK, see [AWS SDKs](asm_access.md#asm-sdks "asm_access.md#asm-sdks").
