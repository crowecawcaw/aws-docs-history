

# Managing tags in Amazon Braket
<a name="tag-managing"></a>

You set tags as *properties* on a *resource*. You can view, add, modify, list, and delete tags through the Amazon Braket console, the Amazon Braket API, or the AWS CLI. For more information, see the [Amazon Braket API reference](https://docs.aws.amazon.com/braket/latest/APIReference/Welcome.html).

**Topics**
+ [Adding tags](#add-tags)
+ [Viewing tags](#view-tags)
+ [Editing tags](#edit-tags)
+ [Removing tags](#remove-tags)

## Adding tags
<a name="add-tags"></a>

You can add tags to taggable resources at the following times:
+  **When you create the resource:** Use the console, or include the `Tags` parameter with the `Create` operation in the [AWS API](https://docs.aws.amazon.com/braket/latest/APIReference/API_Operations.html).
+  **After you create the resource:** Use the console to navigate to the quantum task or notebook resource, or call the `TagResource` operation in the [AWS API](https://docs.aws.amazon.com/braket/latest/APIReference/API_Operations.html).

To add tags to a resource when you create it, you also need permission to create a resource of the specified type.

## Viewing tags
<a name="view-tags"></a>

You can view the tags on any of the taggable resources in Amazon Braket by using the console to navigate to the task or notebook resource, or by calling the AWS `ListTagsForResource` API operation.

You can use the following AWS API command to view tags on a resource:
+  ** AWS API:** `ListTagsForResource` 

## Editing tags
<a name="edit-tags"></a>

You can edit tags by using the console to navigate to the quantum task or notebook resource or you can use the following command to modify the value for a tag attached to a taggable resource. When you specify a tag key that already exists, the value for that key is overwritten:
+  ** AWS API:** `TagResource` 

## Removing tags
<a name="remove-tags"></a>

You can remove tags from a resource by specifying the keys to remove, by using the console to navigate to the quantum task or notebook resource, or when calling the `UntagResource` operation.
+  ** AWS API:** `UntagResource` 