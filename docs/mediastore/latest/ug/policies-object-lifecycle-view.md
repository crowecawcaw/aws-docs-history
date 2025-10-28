End of support notice: On November 13, 2025, AWS will discontinue support
for AWS Elemental MediaStore. After November 13, 2025, you will no longer be able to access the MediaStore console
or MediaStore resources. For more information, visit this
[blog post](https://aws.amazon.com/blogs/media/support-for-aws-elemental-mediastore-ending-soon/ "https://aws.amazon.com/blogs/media/support-for-aws-elemental-mediastore-ending-soon/").

# Viewing an object lifecycle policy

An object lifecycle policy specifies how long objects should be kept in a container.

###### To view an object lifecycle policy (console)

1. Open the MediaStore console at [https://console.aws.amazon.com/mediastore/](https://console.aws.amazon.com/mediastore/ "https://console.aws.amazon.com/mediastore/").
2. On the **Containers** page, choose the name of the container that you want to view the object lifecycle policy
   for.

The container details page appears, with the object lifecycle policy in the **Object lifecycle policy** section.

###### To view an object lifecycle policy (AWS CLI)

- In the AWS CLI, use the `get-lifecycle-policy` command:

```
aws mediastore get-lifecycle-policy --container-name `LiveEvents` --region `us-west-2`
```

The following example shows the return value:

```
{
    "LifecyclePolicy": "{
        "rules": [
            {
                "definition": {
                    "path": [
                        {"prefix": "`Football/`"},
                        {"prefix": "`Baseball/`"}
                    ],
                    "days_since_create": [
                        {"numeric": [">" , `28`]}
                    ]
                },
             "action": "EXPIRE"
            }
        ]
    }"
}
```
