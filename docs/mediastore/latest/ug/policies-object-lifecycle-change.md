End of support notice: On November 13, 2025, AWS will discontinue support
for AWS Elemental MediaStore. After November 13, 2025, you will no longer be able to access the MediaStore console
or MediaStore resources. For more information, visit this
[blog post](https://aws.amazon.com/blogs/media/support-for-aws-elemental-mediastore-ending-soon/ "https://aws.amazon.com/blogs/media/support-for-aws-elemental-mediastore-ending-soon/").

# Editing an object lifecycle policy

You can't edit an existing object lifecycle policy. However, you can change an existing policy by uploading a replacement policy. It takes up to
20 minutes for the service to apply the updated policy to the container.

###### To edit an object lifecycle policy (console)

1. Open the MediaStore console at [https://console.aws.amazon.com/mediastore/](https://console.aws.amazon.com/mediastore/ "https://console.aws.amazon.com/mediastore/").
2. On the **Containers** page, choose the name of the container that you want to edit the object lifecycle policy
   for.

The container details page appears. 3. In the **Object lifecycle policy** section, choose **Edit object lifecycle policy**. 4. Make your changes to the policy, and then choose **Save**.

###### To edit an object lifecycle policy (AWS CLI)

1. Create a file that defines the updated object lifecycle policy:

```
{
    "rules": [
         {
            "definition": {
                "path": [
                    {"prefix": "`Football/`"},
                    {"prefix": "`Baseball/`"}
                    {"prefix": "`Basketball/`"}
                ],
                "days_since_create": [
                    {"numeric": [">" , `28`]}
                ]
            },
            "action": "EXPIRE"
        }
    ]
}
```

2. In the AWS CLI, use the `put-lifecycle-policy` command:

```
aws mediastore put-lifecycle-policy --container-name `LiveEvents` --lifecycle-policy `file://LiveEvents2LifecyclePolicy` --region `us-west-2`
```

This command has no return value. The service attaches the specified policy to the container, replacing the previous policy.
