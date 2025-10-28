End of support notice: On November 13, 2025, AWS will discontinue support
for AWS Elemental MediaStore. After November 13, 2025, you will no longer be able to access the MediaStore console
or MediaStore resources. For more information, visit this
[blog post](https://aws.amazon.com/blogs/media/support-for-aws-elemental-mediastore-ending-soon/ "https://aws.amazon.com/blogs/media/support-for-aws-elemental-mediastore-ending-soon/").

# Deleting a CORS policy

Cross-origin resource sharing (CORS) defines a way for client web applications that are loaded in one domain to interact with resources in a
different domain. Deleting the CORS policy from a container removes permissions for cross-origin requests.

###### To delete a CORS policy (console)

1. Open the MediaStore console at [https://console.aws.amazon.com/mediastore/](https://console.aws.amazon.com/mediastore/ "https://console.aws.amazon.com/mediastore/").
2. On the **Containers** page, choose the name of the container that you want to delete the CORS policy for.

The container details page appears. 3. In the **Container CORS policy** section, choose **Delete CORS policy**. 4. Choose **Continue** to confirm, and then choose **Save**.

###### To delete a CORS policy (AWS CLI)

- In the AWS CLI, use the `delete-cors-policy` command:

```
aws mediastore delete-cors-policy --container-name `ExampleContainer` --region `us-west-2`
```

This command has no return value.
