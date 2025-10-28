# Managing tags in Amazon Braket

You set tags as _properties_ on a _resource_.
You can view, add, modify, list, and delete tags through the Amazon Braket console,
the Amazon Braket API, or the AWS CLI. For more information, see the
[Amazon Braket API reference](../APIReference/Welcome.md "../APIReference/Welcome.md").

###### In this section:

- [Adding tags](#add-tags "#add-tags")
- [Viewing tags](#view-tags "#view-tags")
- [Editing tags](#edit-tags "#edit-tags")
- [Removing tags](#remove-tags "#remove-tags")

## Adding tags

You can add tags to taggable resources at the following times:

- **When you create the resource:** Use the console, or include the `Tags` parameter with the `Create` operation in the [AWS API](../APIReference/API_Operations.md "../APIReference/API_Operations.md").
- **After you create the resource:** Use the console to navigate to the quantum task or notebook resource, or call the `TagResource` operation in the [AWS API](../APIReference/API_Operations.md "../APIReference/API_Operations.md").

To add tags to a resource when you create it, you also need permission to create a resource of the specified type.

## Viewing tags

You can view the tags on any of the taggable resources in Amazon Braket by using the console
to navigate to the task or notebook resource, or by calling the AWS
`ListTagsForResource` API operation.

You can use the following AWS
API command to view tags on a resource:

- **AWS
  API:**
  `ListTagsForResource`

## Editing tags

You can edit tags by using the console to navigate to the quantum task or notebook
resource or you can use the following command to modify the value for a tag attached to
a taggable resource. When you specify a tag key that already exists, the value for that
key is overwritten:

- **AWS
  API:**
  `TagResource`

## Removing tags

You can remove tags from a resource by specifying the keys to
remove, by using the console to navigate to the quantum task or notebook
resource, or when calling the `UntagResource` operation.

- **AWS
  API:**
  `UntagResource`
