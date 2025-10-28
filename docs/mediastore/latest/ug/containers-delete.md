End of support notice: On November 13, 2025, AWS will discontinue support
for AWS Elemental MediaStore. After November 13, 2025, you will no longer be able to access the MediaStore console
or MediaStore resources. For more information, visit this
[blog post](https://aws.amazon.com/blogs/media/support-for-aws-elemental-mediastore-ending-soon/ "https://aws.amazon.com/blogs/media/support-for-aws-elemental-mediastore-ending-soon/").

# Deleting a container

You can delete a container only if it has no objects.

###### To delete a container (console)

1. Open the MediaStore console at [https://console.aws.amazon.com/mediastore/](https://console.aws.amazon.com/mediastore/ "https://console.aws.amazon.com/mediastore/").
2. On the **Containers** page, choose the option to the left of the container name.
3. Choose **Delete**.

###### To delete a container (AWS CLI)

- In the AWS CLI, use the `delete-container` command:

```
aws mediastore delete-container --container-name=`ExampleLiveDemo` --region `us-west-2`
```

This command has no return value.
