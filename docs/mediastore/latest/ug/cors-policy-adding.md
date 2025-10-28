End of support notice: On November 13, 2025, AWS will discontinue support
for AWS Elemental MediaStore. After November 13, 2025, you will no longer be able to access the MediaStore console
or MediaStore resources. For more information, visit this
[blog post](https://aws.amazon.com/blogs/media/support-for-aws-elemental-mediastore-ending-soon/ "https://aws.amazon.com/blogs/media/support-for-aws-elemental-mediastore-ending-soon/").

# Adding a CORS policy to a container

This section explains how to add a cross-origin resource sharing (CORS) configuration to an AWS Elemental MediaStore container. CORS allows client web
applications that are loaded in one domain to interact with resources in another domain.

To configure your container to allow cross-origin requests, you add a CORS policy to the container. A CORS policy defines rules that identify the
origins that you allow to access your container, the operations (HTTP methods) supported for each origin, and other operation-specific
information.

When you add a CORS policy to the container, the [container policies](policies.md "policies.md") (that govern access rights to the container)
continue to apply.

###### To add a CORS policy (console)

1. Open the MediaStore console at [https://console.aws.amazon.com/mediastore/](https://console.aws.amazon.com/mediastore/ "https://console.aws.amazon.com/mediastore/").
2. On the **Containers** page, choose the name of the container that you want to create a CORS policy for.

The container details page appears. 3. In the **Container CORS policy** section, choose **Create CORS policy**. 4. Insert the policy in JSON format, and then choose **Save**.

###### To add a CORS policy (AWS CLI)

1. Create a file that defines the CORS policy:

```
[
  {
    "AllowedHeaders": [
      "*"
    ],
    "AllowedMethods": [
      "GET",
      "HEAD"
    ],
    "AllowedOrigins": [
      "*"
    ],
    "MaxAgeSeconds": 3000
  }
]
```

2. In the AWS CLI, use the `put-cors-policy` command.

```
aws mediastore put-cors-policy --container-name `ExampleContainer` --cors-policy file://`corsPolicy.json` --region `us-west-2`
```

This command has no return value.
