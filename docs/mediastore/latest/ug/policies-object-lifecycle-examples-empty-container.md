End of support notice: On November 13, 2025, AWS will discontinue support
for AWS Elemental MediaStore. After November 13, 2025, you will no longer be able to access the MediaStore console
or MediaStore resources. For more information, visit this
[blog post](https://aws.amazon.com/blogs/media/support-for-aws-elemental-mediastore-ending-soon/ "https://aws.amazon.com/blogs/media/support-for-aws-elemental-mediastore-ending-soon/").

# Example object lifecycle policy: Empty container

The following object lifecycle policy specifies that MediaStore deletes all
objects in the container, including folders and subfolders, 1 day after they are
added to the container. If the container holds any objects before this policy is
applied, MediaStore deletes the objects 1 day after the policy becomes effective. It
takes up to 20 minutes for the service to apply the new policy to the
container.

```
{
    "rules": [
        {
            "definition": {
                "path": [
                    {"wildcard": "*"}
                ],
                "days_since_create": [
                    {"numeric": [ ">=", 1 ]}
                ]
            },
            "action": "EXPIRE"
        }
    ]
}
```
