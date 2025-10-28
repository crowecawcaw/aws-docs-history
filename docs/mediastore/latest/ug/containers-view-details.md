End of support notice: On November 13, 2025, AWS will discontinue support
for AWS Elemental MediaStore. After November 13, 2025, you will no longer be able to access the MediaStore console
or MediaStore resources. For more information, visit this
[blog post](https://aws.amazon.com/blogs/media/support-for-aws-elemental-mediastore-ending-soon/ "https://aws.amazon.com/blogs/media/support-for-aws-elemental-mediastore-ending-soon/").

# Viewing the details for a container

Details for a container include the container policy, endpoint, ARN, and creation
time.

###### To view the details for a container (console)

1. Open the MediaStore console at [https://console.aws.amazon.com/mediastore/](https://console.aws.amazon.com/mediastore/ "https://console.aws.amazon.com/mediastore/").
2. On the **Containers** page, choose the name of the container.

The container details page appears. This page is divided into two sections:

    * The **Objects** section, which lists the
     objects and folders in the container.
    * The **Container** policy section, which
     shows the resource-based policy that is associated with this container.
     For information about resource policies, see [Container policies](policies.md "policies.md").

###### To view the details for a container (AWS CLI)

- In the AWS CLI, use the `describe-container` command:

```
aws mediastore describe-container --container-name `ExampleContainer` --region `us-west-2`
```

The following example shows the return value:

```
{
    "Container": {
        "CreationTime": 1563558086.0,
        "AccessLoggingEnabled": false,
        "ARN": "arn:aws:mediastore:us-west-2:111122223333:container/ExampleContainer",
        "Status": "ACTIVE",
        "Name": "ExampleContainer",
        "Endpoint": "https://aaabbbcccdddee.data.mediastore.us-west-2.amazonaws.com"
    }
}
```
