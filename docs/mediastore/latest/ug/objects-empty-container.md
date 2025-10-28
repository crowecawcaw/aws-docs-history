End of support notice: On November 13, 2025, AWS will discontinue support
for AWS Elemental MediaStore. After November 13, 2025, you will no longer be able to access the MediaStore console
or MediaStore resources. For more information, visit this
[blog post](https://aws.amazon.com/blogs/media/support-for-aws-elemental-mediastore-ending-soon/ "https://aws.amazon.com/blogs/media/support-for-aws-elemental-mediastore-ending-soon/").

# Emptying a container

You can empty a container to delete all objects that are stored within the container. Alternatively, you can add an [object lifecycle policy](policies-object-lifecycle-examples-empty-container.md "policies-object-lifecycle-examples-empty-container.md") to automatically delete objects after they reach
a certain age in a container, or you can [delete objects individually](objects-delete.md "objects-delete.md").

###### To empty a container (console)

1. Open the MediaStore console at [https://console.aws.amazon.com/mediastore/](https://console.aws.amazon.com/mediastore/ "https://console.aws.amazon.com/mediastore/").
2. On the **Containers** page, choose the option for the
   container that you want to empty.
3. Choose **Empty container**. A confirmation message
   appears.
4. Confirm that you want to empty the container by entering the container name into the text field, then choose
   **Empty**.
