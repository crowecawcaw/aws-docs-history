# Using tags on Lambda functions

You can tag functions to organize and manage your resources.
Tags are free-form key-value pairs associated with your resources that are supported across AWS services.
For more information about use cases for tags, see [Common
tagging strategies](../../../tag-editor/latest/userguide/best-practices-and-strats.md#tag-strategies "../../../tag-editor/latest/userguide/best-practices-and-strats.md#tag-strategies") in the _Tagging AWS Resources and Tag Editor Guide_.

Tags apply at the function level, not to versions or aliases. Tags are not part of the version-specific
configuration that AWS Lambda creates a snapshot of when you publish a version. You can use the Lambda API to view and
update tags. You can also view and update tags while managing a specific function in the Lambda console.

###### Sections

- [Permissions required for working with tags](#fxn-tags-required-permissions "#fxn-tags-required-permissions")
- [Using tags with the Lambda console](#using-tags-with-the-console "#using-tags-with-the-console")
- [Using tags with the AWS CLI](#configuration-tags-cli "#configuration-tags-cli")

## Permissions required for working with tags

To allow an AWS Identity and Access Management
(IAM) identity (user,
group, or role) to read or set tags on a resource, grant it the corresponding permissions:

- **lambda:ListTags**–When a resource has tags, grant this permission
  to anyone who needs to call `ListTags` on it. For tagged functions, this permission is also necessary for `GetFunction`.
- **lambda:TagResource**–Grant this permission to anyone who needs to
  call `TagResource` or perform a tag on create.

Optionally, consider granting the **lambda:UntagResource** permission as well to
allow `UntagResource` calls to the resource.

For more information, see [Identity-based IAM policies for Lambda](access-control-identity-based.md "access-control-identity-based.md").

## Using tags with the Lambda console

You can use the Lambda console to create functions that have tags, add tags to existing functions, and filter
functions by tags that you add.

###### To add tags when you create a function

1. Open the [Functions page](https://console.aws.amazon.com/lambda/home#/functions "https://console.aws.amazon.com/lambda/home#/functions") of the Lambda console.
2. Choose **Create function**.
3. Choose **Author from scratch** or **Container image**.
4. Under **Basic information**, set up your function. For more information about configuring functions, see [Configuring AWS Lambda functions](lambda-functions.md "lambda-functions.md").
5. Expand **Advanced
   settings**,
   and then select **Enable tags**.
6. Choose **Add new tag**, and then enter a **Key** and an optional
   **Value**. To add more tags, repeat this step.
7. Choose **Create function**.

###### To add tags to an existing function

1. Open the [Functions page](https://console.aws.amazon.com/lambda/home#/functions "https://console.aws.amazon.com/lambda/home#/functions") of the Lambda console.
2. Choose the name of a function.
3. Choose
   **Configuration**,
   and then choose **Tags**.
4. Under **Tags**, choose **Manage tags**.
5. Choose **Add new tag**, and then enter a **Key** and an optional
   **Value**. To add more tags, repeat this step.
6. Choose **Save**.

###### To filter functions with tags

1. Open the [Functions page](https://console.aws.amazon.com/lambda/home#/functions "https://console.aws.amazon.com/lambda/home#/functions") of the Lambda console.
2. Choose the search box to see a list of function properties and tag keys.
3. Choose a tag key to see a list of values that are in use in the current AWS Region.
4. Select **Use: "tag-name"** to see all functions tagged with this key, or choose an
   **Operator** to further filter by value.
5. Select your tag value to filter by a combination of tag key and value.

The search bar also supports searching for tag keys. Enter `tag` to see only a list of tag keys,
or enter the name of a key to find it in the list.

## Using tags with the AWS CLI

You can add and remove tags on existing Lambda resources, including functions, with the Lambda API. You can also
add tags when creating a function, which allows you to keep a
resource tagged through its entire lifecycle.

### Updating tags with the Lambda tag APIs

You can add and remove tags for supported Lambda resources through the [TagResource](../api/API_TagResource.md "../api/API_TagResource.md") and [UntagResource](../api/API_UntagResource.md "../api/API_UntagResource.md") API operations.

You can call these operations using the AWS CLI. To add tags to an existing resource, use the `tag-resource`
command. This example adds two tags, one with the key `Department` and one with the key `CostCenter`.

```
`aws lambda tag-resource \
--resource arn:aws:lambda:`us-east-2:123456789012:resource-type:my-resource` \
--tags `Department`=`Marketing`,`CostCenter`=`1234ABCD``
```

To remove tags, use the `untag-resource`
command. This example removes the tag with the key `Department`.

```
`aws lambda untag-resource --resource `arn:aws:lambda:us-east-1:123456789012:resource-type:resource-identifier` \
--tag-keys `Department``
```

### Adding tags when creating a function

To create a new Lambda function with tags, use the [CreateFunction](../api/API_CreateFunction.md "../api/API_CreateFunction.md") API operation. Specify the `Tags` parameter. You can call
this operation with the `create-function` CLI command and the --tags option. Before using the tags
parameter with `CreateFunction`, ensure that your role has permission to tag resources alongside the
usual permissions needed for this operation. For more information about permissions for tagging, see [Permissions required for working with tags](#fxn-tags-required-permissions "#fxn-tags-required-permissions"). This example adds two tags, one with the key
`Department` and one with the key `CostCenter`.

```
`aws lambda create-function --function-name `my-function`
--handler index.js --runtime nodejs24.x \
--role arn:aws:iam::`123456789012`:role/`lambda-role` \
--tags Department=Marketing,CostCenter=1234ABCD`
```

### Viewing tags on a function

To view the tags that are applied to a specific Lambda resource, use the `ListTags` API operation. For more information, see [ListTags](../api/API_ListTags.md "../api/API_ListTags.md").

You can call this operation with the `list-tags` AWS CLI command by providing an ARN (Amazon Resource Name).

```
`aws lambda list-tags --resource `arn:aws:lambda:us-east-1:123456789012:resource-type:resource-identifier``
```

You can view the tags that are applied to a specific resource with the
[GetFunction](../api/API_GetFunction.md "../api/API_GetFunction.md") API operation. Comparable functionality is not available for other resource types.

You can call this operation with the `get-function` CLI command:

```
`aws lambda get-function --function-name `my-function``
```

### Filtering resources by tag

You can use the AWS Resource Groups Tagging API [GetResources](../../../resourcegroupstagging/latest/APIReference/API_GetResources.md "../../../resourcegroupstagging/latest/APIReference/API_GetResources.md") API operation to
filter your resources by tags. The `GetResources`
operation receives up to 10 filters, with each filter containing a tag key and up to 10 tag values. You
provide `GetResources`
with a
`ResourceType` to filter by specific resource types.

You can call this operation using the `get-resources` AWS CLI command. For examples of using `get-resources`, see [get-resources](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/resourcegroupstaggingapi/get-resources.html#examples "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/resourcegroupstaggingapi/get-resources.html#examples") in the _AWS CLI Command Reference_.
