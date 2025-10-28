# Tagging Amazon Cognito resources

A _tag_ is a metadata label that you or AWS assigns to an AWS
resource. Each tag consists of a _key_ and a _value_. For tags that you assign, you define the key and value.
For example, you might define the key as `stage` and the value for one resource
as `test`.

Tags help you do the following:

- Identify and organize your AWS resources. Many AWS services support tagging,
  so that you can assign the same tag to resources from different services. This helps
  you indicate which resources are related. For example, you could assign the same tag
  to an Amazon Cognito user pool that you assign to an Amazon DynamoDB table.
- Track your AWS costs. You can activate these tags on the AWS Billing and Cost Management dashboard.
  AWS uses cost allocation tags to categorize your costs and deliver a monthly cost
  allocation report to you. For more information, see [Use
  cost allocation tags](../../../awsaccountbilling/latest/aboutv2/cost-alloc-tags.md "../../../awsaccountbilling/latest/aboutv2/cost-alloc-tags.md") in the _AWS Billing User Guide_.
- Control access to your resources based on the tags that are assigned to them. You
  can control access by specifying tag keys and values in the conditions for an
  AWS Identity and Access Management (IAM) policy. For example, you could allow a user to
  update a user pool only if the user pool has an `owner` tag with a
  value of that user's name. For more information, see [Controlling access using tags](../../../IAM/latest/UserGuide/access_tags.md "../../../IAM/latest/UserGuide/access_tags.md") in
  the _IAM User Guide_.
  You can use the AWS Command Line Interface or the Amazon Cognito API to add, edit, or delete tags for both user and
  identity pools. You can also manage tags for user pools by using the Amazon Cognito console.

For tips on using tags, see the [AWS
tagging strategies](https://aws.amazon.com/answers/account-management/aws-tagging-strategies/ "https://aws.amazon.com/answers/account-management/aws-tagging-strategies/") post on the _AWS Answers_
blog.

The following sections provide more information about tags for Amazon Cognito.

## Supported resources in Amazon Cognito

The following resources in Amazon Cognito support tagging:

- User pools
- Identity pools

## Tag restrictions

The following restrictions apply to tags on Amazon Cognito resources:

- Maximum number of tags that you can assign to a resource – 50
- Maximum key length – 128 Unicode characters
- Maximum value length – 256 Unicode characters
- Valid characters for keys and values – a-z, A-Z, 0-9, space, and the
  following characters: \_ . : / = + - @
- Keys and values are case sensitive
- Don't use `aws:` as a prefix for keys; it's reserved for AWS
  use

## Managing tags using the Amazon Cognito console

You can use the Amazon Cognito console to manage the tags that are assigned to your user
pools.

###### To add tags to a user pool

1. Navigate to the [Amazon Cognito
   console](https://console.aws.amazon.com/cognito/home "https://console.aws.amazon.com/cognito/home"). If prompted, enter your AWS credentials.
2. Choose **User Pools**.
3. Choose an existing user pool from the list, or [create a user
   pool](cognito-user-pool-as-user-directory.md "cognito-user-pool-as-user-directory.md").
4. Choose the **Settings** menu and locate
   the **Tags** tab.
5. Choose **Add tags** to add your first tag. If you have
   previously assigned tags to this user pool, in **Manage tags**,
   chose **Add another**.
6. Specify values for **Tag Key** and **Tag
   Value**.
7. For each additional tag that you want to add, choose **Add
   another**.
8. When you are finished adding tags, choose **Save
   changes**.

To tag an identity pool, navigate to the **Identity pools** menu and
select or create an identity pool. In the **Identity pool properties**
tab, locate **Tags**. Choose **Add tag**.

## AWS CLI examples

The AWS CLI provides commands that help you manage the tags that you assign to your
Amazon Cognito user pools and identity pools.

### Assigning tags

Use the following commands to assign tags to your existing user pools and identity
pools.

###### Example `tag-resource` Command for user pools

Assign tags to a user pool by using [`tag-resource`](../../../cli/latest/reference/cognito-idp/tag-resource.md "../../../cli/latest/reference/cognito-idp/tag-resource.md") within the `cognito-idp` set
of commands:

```
`$` aws cognito-idp tag-resource \
`>` --resource-arn `user-pool-arn` \
`>` --tags `Stage=Test`
```

This command includes the following parameters:

- `resource-arn` – The Amazon Resource Name (ARN) of
  the user pool that you are applying tags to. To look up the ARN, choose
  the user pool in the Amazon Cognito console, and view the **Pool
  ARN** value on the **General settings**
  tab.
- `tags` – The key-value pairs of the tags, in the
  format
  ``key`=`value``.
  To assign multiple tags at once, specify them in a comma-separated
  list:

```
`$` aws cognito-idp tag-resource \
`>` --resource-arn `user-pool-arn` \
`>` --tags `Stage=Test,CostCenter=80432,Owner=SysEng`
```

###### Example `tag-resource` Command for identity pools

Assign tags to an identity pool by using [`tag-resource`](../../../cli/latest/reference/cognito-identity/tag-resource.md "../../../cli/latest/reference/cognito-identity/tag-resource.md") within the
`cognito-identity` set of commands:

```
`$` aws cognito-identity tag-resource \
`>` --resource-arn `identity-pool-arn` \
`>` --tags `Stage=Test`
```

This command includes the following parameters:

- `resource-arn` – The Amazon Resource Name (ARN) of
  the identity pool that you are applying tags to. To look up the ARN,
  choose the identity pool in the Amazon Cognito console, and choose **Edit
  identity pool**. Then, at **Identity pool
  ID**, choose **Show ARN**.
- `tags` – The key-value pairs of the tags, in the
  format
  ``key`=`value``.
  To assign multiple tags at once, specify them in a comma-separated
  list:

```
`$` aws cognito-identity tag-resource \
`>` --resource-arn `identity-pool-arn` \
`>` --tags `Stage=Test,CostCenter=80432,Owner=SysEng`
```

### Viewing tags

Use the following commands to view the tags that you have assigned to your user
pools and identity pools.

###### Example `list-tags-for-resource` Command for user pools

View the tags that are assigned to a user pool by using [`list-tags-for-resource`](../../../cli/latest/reference/cognito-idp/list-tags-for-resource.md "../../../cli/latest/reference/cognito-idp/list-tags-for-resource.md") within the
`cognito-idp` set of commands:

```
`$` aws cognito-idp list-tags-for-resource --resource-arn `user-pool-arn`
```

###### Example `list-tags-for-resource` Command for identity pools

View the tags that are assigned to an identity pool by using [`list-tags-for-resource`](../../../cli/latest/reference/cognito-identity/list-tags-for-resource.md "../../../cli/latest/reference/cognito-identity/list-tags-for-resource.md") within the
`cognito-identity` set of commands:

```
`$` aws cognito-identity list-tags-for-resource --resource-arn `identity-pool-arn`
```

### Removing tags

Use the following commands to remove tags from your user pools and identity
pools.

###### Example `untag-resource` Command for user pools

Remove tags from a user pool by using [`untag-resource`](../../../cli/latest/reference/cognito-idp/untag-resource.md "../../../cli/latest/reference/cognito-idp/untag-resource.md") within the `cognito-idp`
set of commands:

```
`$` aws cognito-idp untag-resource \
`>` --resource-arn `user-pool-arn` \
`>` --tag-keys `Stage CostCenter Owner`
```

For the `--tag-keys` parameter, specify one or more tag keys. Don't
include the tag values. Separate keys with spaces.

###### Example `untag-resource` Command for identity pools

Remove tags from an identity pool by using [`untag-resource`](../../../cli/latest/reference/cognito-identity/untag-resource.md "../../../cli/latest/reference/cognito-identity/untag-resource.md") within the
`cognito-identity` set of commands:

```
`$` aws cognito-identity untag-resource \
`>` --resource-arn `identity-pool-arn` \
`>` --tag-keys `Stage CostCenter Owner`
```

For the `--tag-keys` parameter, specify one or more tag keys. Don't
include the tag values.

###### Important

After you delete a user or identity pool, tags related to the deleted pool can still appear in
the console or API calls for up to 30 days after deletion.

### Applying tags when you create

resources

Use the following commands to assign tags at the moment you create a user pool or
identity pool.

###### Example `create-user-pool` Command with tags

When you create a user pool by using the [`create-user-pool`](../../../cli/latest/reference/cognito-idp/create-user-pool.md "../../../cli/latest/reference/cognito-idp/create-user-pool.md") command, you can specify tags
with the `--user-pool-tags` parameter:

```
`$` aws cognito-idp create-user-pool \
`>` --pool-name `user-pool-name` \
`>` --user-pool-tags `Stage=Test,CostCenter=80432,Owner=SysEng`
```

Key-value pairs for tags must be in the format
``key`=`value``.
If you are adding multiple tags, specify them in a comma-separated list.

###### Example `create-identity-pool` Command with tags

When you create an identity pool by using the [`create-identity-pool`](../../../cli/latest/reference/cognito-identity/create-identity-pool.md "../../../cli/latest/reference/cognito-identity/create-identity-pool.md") command, you can specify tags
with the `--identity-pool-tags` parameter:

```
`$` aws cognito-identity create-identity-pool \
`>` --identity-pool-name `identity-pool-name` \
`>` --allow-unauthenticated-identities \
`>` --identity-pool-tags `Stage=Test,CostCenter=80432,Owner=SysEng`
```

Key-value pairs for tags must be in the format
``key`=`value``.
If you are adding multiple tags, specify them in a comma-separated list.

## Managing tags using the Amazon Cognito API

You can use the following actions in the Amazon Cognito API to manage the tags for your user
pools and identity pools.

### API actions for user pool tags

Use the following API actions to assign, view, and remove tags for user
pools.

- [TagResource](../../../cognito-user-identity-pools/latest/APIReference/API_TagResource.md "../../../cognito-user-identity-pools/latest/APIReference/API_TagResource.md")
- [ListTagsForResource](../../../cognito-user-identity-pools/latest/APIReference/API_ListTagsForResource.md "../../../cognito-user-identity-pools/latest/APIReference/API_ListTagsForResource.md")
- [UntagResource](../../../cognito-user-identity-pools/latest/APIReference/API_UntagResource.md "../../../cognito-user-identity-pools/latest/APIReference/API_UntagResource.md")
- [CreateUserPool](../../../cognito-user-identity-pools/latest/APIReference/API_CreateUserPool.md "../../../cognito-user-identity-pools/latest/APIReference/API_CreateUserPool.md")

### API actions for identity pool

tags

Use the following API actions to assign, view, and remove tags for identity
pools.

- [TagResource](../../../cognitoidentity/latest/APIReference/API_TagResource.md "../../../cognitoidentity/latest/APIReference/API_TagResource.md")
- [ListTagsForResource](../../../cognitoidentity/latest/APIReference/API_ListTagsForResource.md "../../../cognitoidentity/latest/APIReference/API_ListTagsForResource.md")
- [UntagResource](../../../cognitoidentity/latest/APIReference/API_UntagResource.md "../../../cognitoidentity/latest/APIReference/API_UntagResource.md")
- [CreateIdentityPool](../../../cognitoidentity/latest/APIReference/API_CreateIdentityPool.md "../../../cognitoidentity/latest/APIReference/API_CreateIdentityPool.md")
