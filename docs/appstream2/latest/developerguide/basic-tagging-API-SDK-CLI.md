# Working with Tags by Using the Amazon WorkSpaces Applications API, an AWS SDK, or AWS CLI

If you're using the WorkSpaces Applications API, an AWS SDK, or the AWS Command Line Interface (AWS
CLI), you can use the following WorkSpaces Applications operations with the `tags` parameter
to add tags when you create new resources.

###### Note

You can use spaces in tag keys and values. To indicate a space when you use the AWS CLI, use "\s" (without the quotation marks).

| Task                                         | AWS CLI                                                                                                                                                | API Operation                                                                                                                                                                                     |
| -------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Add one or more tags for a new fleet         | [create-fleet](../../../cli/latest/reference/appstream/create-fleet.md "../../../cli/latest/reference/appstream/create-fleet.md")                      | [CreateFleet](../APIReference/API_CreateFleet.md#AppStream2-CreateFleet-request-Tags "../APIReference/API_CreateFleet.md#AppStream2-CreateFleet-request-Tags")                                    |
| Add one or more tags for a new image builder | [create-imagebuilder](../../../cli/latest/reference/appstream/create-imagebuilder.md "../../../cli/latest/reference/appstream/create-imagebuilder.md") | [CreateImageBuilder](../APIReference/API_CreateImageBuilder.md#AppStream2-CreateImageBuilder-request-Tags "../APIReference/API_CreateImageBuilder.md#AppStream2-CreateImageBuilder-request-Tags") |
| Add one or more tags for a new stack         | [create-stack](../../../cli/latest/reference/appstream/create-stack.md "../../../cli/latest/reference/appstream/create-stack.md")                      | [CreateStack](../APIReference/API_CreateStack.md#AppStream2-CreateStack-request-Tags "../APIReference/API_CreateStack.md#AppStream2-CreateStack-request-Tags")                                    |

You can use the following WorkSpaces Applications operations to add, edit, remove, or list tags for existing
resources:

| Task                                             | AWS CLI                                                                                                                                                         | API Operation                                                                                                  |
| ------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| Add or overwrite one or more tags for a resource | [tag-resource](../../../cli/latest/reference/appstream/tag-resource.md "../../../cli/latest/reference/appstream/tag-resource.md")                               | [TagResource](../APIReference/API_TagResource.md "../APIReference/API_TagResource.md")                         |
| Remove one or more tags for a resource           | [untag-resource](../../../cli/latest/reference/appstream/untag-resource.md "../../../cli/latest/reference/appstream/untag-resource.md")                         | [UntagResource](../APIReference/API_UntagResource.md "../APIReference/API_UntagResource.md")                   |
| List one or more tags for a resource             | [list-tags-for-resource](../../../cli/latest/reference/appstream/list-tags-for-resource.md "../../../cli/latest/reference/appstream/list-tags-for-resource.md") | [ListTagsForResource](../APIReference/API_ListTagsForResource.md "../APIReference/API_ListTagsForResource.md") |

When you use the WorkSpaces Applications API, an AWS SDK, or AWS CLI actions to add, edit, remove, or
list tags for an existing WorkSpaces Applications resource, specify the resource by using its Amazon Resource Name
(ARN). An ARN uniquely identifies an AWS resource and uses the following general
syntax.

```
`arn:aws:appstream:`region`:`account`:`resourceType`/`resourceName``
```

**`region`**

The AWS Region in which the resource was created (for example,
`us-east-1`).

**`account`**

The AWS account ID, with no hyphens (for example, `123456789012`).

**`resourceType`**

The type of resource. You can tag the following WorkSpaces Applications resource types:
`image-builder`, `image`, `fleet`, and
`stack`.

**`resourceName`**

The name of the resource.

For example, you can obtain the ARN for an WorkSpaces Applications fleet by using the AWS CLI [describe-fleets](../../../cli/latest/reference/appstream/describe-fleets.md "../../../cli/latest/reference/appstream/describe-fleets.md") command.
Copy the following command.

```
`aws appstream describe-fleets`
```

For an environment that contains a single fleet named `TestFleet`, the ARN
for this resource would appear in the JSON output similar to the following.

```
"Arn": "arn:aws:appstream:us-east-1:123456789012:fleet/TestFleet"
```

After you obtain the ARN for this resource, you can add two tags by using the [tag-resource](../../../cli/latest/reference/appstream/tag-resource.md "../../../cli/latest/reference/appstream/tag-resource.md") command:

```
`aws appstream tag-resource --resource arn:awsappstream:us-east-1:123456789012:fleet/TestFleet --tags Environment=Test,Department=IT`
```

The first tag, `Environment=Test`, indicates that the fleet is in a test
environment. The second tag, `Department=IT`, indicates that the fleet is in
the IT department.

You can use the following command to list the two tags that you added to the
fleet.

```
`aws appstream list-tags-for-resource --resource arn:aws:appstream:us-east-1:123456789012:fleet/TestFleet`
```

For this example, the JSON output appears as follows:

```
{
    "Tags": {
       "Environment" : "Test",
       "Department" : "IT"
    }
}
```
