End of support notice: On November 13, 2025, AWS will discontinue support
for AWS Elemental MediaStore. After November 13, 2025, you will no longer be able to access the MediaStore console
or MediaStore resources. For more information, visit this
[blog post](https://aws.amazon.com/blogs/media/support-for-aws-elemental-mediastore-ending-soon/ "https://aws.amazon.com/blogs/media/support-for-aws-elemental-mediastore-ending-soon/").

# Deleting an object lifecycle policy

When you delete an object lifecycle policy, it takes up to 20 minutes for the service to apply the change to the container.

###### To delete an object lifecycle policy (console)

1. Open the MediaStore console at [https://console.aws.amazon.com/mediastore/](https://console.aws.amazon.com/mediastore/ "https://console.aws.amazon.com/mediastore/").
2. On the **Containers** page, choose the name of the container that you want to delete the object lifecycle policy
   for.

The container details page appears. 3. In the **Object lifecycle policy** section, choose **Delete lifecycle policy**. 4. Choose **Continue** to confirm, and then choose **Save**.

###### To delete an object lifecycle policy (AWS CLI)

- In the AWS CLI, use the `delete-lifecycle-policy` command:

```
aws mediastore delete-lifecycle-policy --container-name `LiveEvents` --region `us-west-2`
```

This command has no return value.
