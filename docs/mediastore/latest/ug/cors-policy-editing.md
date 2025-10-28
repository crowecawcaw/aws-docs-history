End of support notice: On November 13, 2025, AWS will discontinue support
for AWS Elemental MediaStore. After November 13, 2025, you will no longer be able to access the MediaStore console
or MediaStore resources. For more information, visit this
[blog post](https://aws.amazon.com/blogs/media/support-for-aws-elemental-mediastore-ending-soon/ "https://aws.amazon.com/blogs/media/support-for-aws-elemental-mediastore-ending-soon/").

# Editing a CORS policy

Cross-origin resource sharing (CORS) defines a way for client web applications that are loaded in one domain to interact with resources in a
different domain.

###### To edit a CORS policy (console)

1. Open the MediaStore console at [https://console.aws.amazon.com/mediastore/](https://console.aws.amazon.com/mediastore/ "https://console.aws.amazon.com/mediastore/").
2. On the **Containers** page, choose the name of the container that you want to edit the CORS policy for.

The container details page appears. 3. In the **Container CORS policy** section, choose **Edit CORS policy**. 4. Make your changes to the policy, and then choose **Save**.

###### To edit a CORS policy (AWS CLI)

1. Create a file that defines the updated CORS policy:

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
      "https://www.example.com"
    ],
    "MaxAgeSeconds": 3000
  }
]
```

2. In the AWS CLI, use the `put-cors-policy` command.

```
aws mediastore put-cors-policy --container-name `ExampleContainer` --cors-policy file://`corsPolicy2.json` --region `us-west-2`
```

This command has no return value.
