

# Using tags on code signing configurations
<a name="tags-csc"></a>

You can tag code signing configurations to organize and manage your resources. Tags are free-form key-value pairs associated with your resources that are supported across AWS services. For more information about use cases for tags, see [Common tagging strategies](https://docs.aws.amazon.com/tag-editor/latest/userguide/best-practices-and-strats.html#tag-strategies) in the *Tagging AWS Resources and Tag Editor Guide*. 

 You can use the AWS Lambda API to view and update tags. You can also view and update tags while managing a specific code signing configuration in the Lambda console.

**Topics**
+ [Permissions required for working with tags](#csc-tags-required-permissions)
+ [Using tags with the Lambda console](#tags-csc-console)
+ [Using tags with the AWS CLI](#tags-csc-cli)

## Permissions required for working with tags
<a name="csc-tags-required-permissions"></a>

To allow an AWS Identity and Access Management (IAM) identity (user, group, or role) to read or set tags on a resource, grant it the corresponding permissions:
+ **lambda:ListTags**–When a resource has tags, grant this permission to anyone who needs to call `ListTags` on it. For tagged Event Functions, this permission is also necessary for `GetFunction`.
+ **lambda:TagResource**–Grant this permission to anyone who needs to call `TagResource` or perform a tag on create.

Optionally, consider granting the **lambda:UntagResource** permission as well to allow `UntagResource` calls to the resource.

For more information, see [Identity-based IAM policies for Lambda](access-control-identity-based.md).

## Using tags with the Lambda console
<a name="tags-csc-console"></a>

You can use the Lambda console to create code signing configurations that have tags, add tags to existing code signing configurations, and filter code signing configurations by tag.

**To add a tag when you create a code signing configuration**

1. Open [Code signing configurations](https://console.aws.amazon.com/lambda/home#/code-signing-configurations) in the Lambda console.

1. From the header of the content pane, Choose **Create configuration**.

1. In the section at the top of the content pane, set up your code signing configuration. For more information about configuring code signing configurations, see [Using code signing to verify code integrity with Lambda](configuration-codesigning.md).

1. In the **Tags** section, choose **Add new tag**.

1. In the **Key** field, enter your tag key. For information about tagging restrictions, see [Tag naming limits and requirements](https://docs.aws.amazon.com/tag-editor/latest/userguide/best-practices-and-strats.html#id_tags_naming_best_practices) in the *Tagging AWS Resources and Tag Editor Guide*.

1. Choose **Create configuration**.

**To add a tag to an existing code signing configuration**

1. Open [Code signing configurations](https://console.aws.amazon.com/lambda/home#/code-signing-configurations) in the Lambda console.

1. Choose the name of your code signing configuration.

1. In the tabs below the **Detail** pane, choose **Tags**.

1. Choose **Manage tags**.

1. Choose **Add new tag**.

1. In the **Key** field, enter your tag key. For information about tagging restrictions, see [Tag naming limits and requirements](https://docs.aws.amazon.com/tag-editor/latest/userguide/best-practices-and-strats.html#id_tags_naming_best_practices) in the *Tagging AWS Resources and Tag Editor Guide*.

1. Choose **Save**.

**To filter code signing configurations by tag**

1. Open [Code signing configurations](https://console.aws.amazon.com/lambda/home#/code-signing-configurations) in the Lambda console.

1. Choose the search box.

1. From the dropdown list, select your tag from below the **Tags** subheading.

1. Select **Use: "tag-name"** to see all code signing configurations tagged with this key, or choose an **Operator** to further filter by value.

1. Select your tag value to filter by a combination of tag key and value.

The search box also supports searching for tag keys. Enter the name of a key to find it in the list.

## Using tags with the AWS CLI
<a name="tags-csc-cli"></a>

You can add and remove tags on existing Lambda resources, including code signing configurations, with the Lambda API. You can also add tags when creating an code signing configuration to keep a resource tagged through its entire lifecycle.

### Updating tags with the Lambda tag APIs
<a name="tags-csc-api-config"></a>

You can add and remove tags for supported Lambda resources through the [TagResource](https://docs.aws.amazon.com/lambda/latest/api/API_TagResource.html) and [UntagResource](https://docs.aws.amazon.com/lambda/latest/api/API_UntagResource.html) API operations.

You can call these operations using the AWS CLI. To add tags to an existing resource, use the `tag-resource` command. This example adds two tags, one with the key {{Department}} and one with the key {{CostCenter}}.

```
aws lambda tag-resource \
--resource arn:aws:lambda:{{us-east-2:123456789012:resource-type:my-resource}} \
--tags {{Department}}={{Marketing}},{{CostCenter}}={{1234ABCD}}
```

To remove tags, use the `untag-resource` command. This example removes the tag with the key {{Department}}.

```
aws lambda untag-resource --resource {{arn:aws:lambda:us-east-1:123456789012:resource-type:resource-identifier}} \
--tag-keys {{Department}}
```

### Adding tags when creating a code signing configuration
<a name="tags-csc-on-create"></a>

To create a new Lambda code signing configuration with tags, use the [CreateCodeSigningConfig](https://docs.aws.amazon.com/lambda/latest/api/API_CreateCodeSigningConfig.html) API operation. Specify the `Tags` parameter. You can call this operation with the `create-code-signing-config` AWS CLI command and the `--tags` option. For more information about the CLI command, see [create-code-signing-config](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/create-code-signing-config.html) in the *AWS CLI Command Reference*.

Before using the `Tags` parameter with `CreateCodeSigningConfig`, ensure that your role has permission to tag resources alongside the usual permissions needed for this operation. For more information about permissions for tagging, see [Permissions required for working with tags](#csc-tags-required-permissions).

### Viewing tags with the Lambda tag APIs
<a name="tags-csc-api-view"></a>

To view the tags that are applied to a specific Lambda resource, use the `ListTags` API operation. For more information, see [ListTags](https://docs.aws.amazon.com/lambda/latest/api/API_ListTags.html).

You can call this operation with the `list-tags` AWS CLI command by providing an ARN (Amazon Resource Name).

```
aws lambda list-tags --resource {{arn:aws:lambda:us-east-1:123456789012:resource-type:resource-identifier}}
```

### Filtering resources by tag
<a name="tags-csc-filtering"></a>

You can use the AWS Resource Groups Tagging API [GetResources](https://docs.aws.amazon.com/resourcegroupstagging/latest/APIReference/API_GetResources.html) API operation to filter your resources by tags. The `GetResources` operation receives up to 10 filters, with each filter containing a tag key and up to 10 tag values. You provide `GetResources` with a `ResourceType` to filter by specific resource types.

You can call this operation using the `get-resources` AWS CLI command. For examples of using `get-resources`, see [get-resources](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/resourcegroupstaggingapi/get-resources.html#examples) in the *AWS CLI Command Reference*. 