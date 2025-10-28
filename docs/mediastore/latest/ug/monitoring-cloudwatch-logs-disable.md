End of support notice: On November 13, 2025, AWS will discontinue support
for AWS Elemental MediaStore. After November 13, 2025, you will no longer be able to access the MediaStore console
or MediaStore resources. For more information, visit this
[blog post](https://aws.amazon.com/blogs/media/support-for-aws-elemental-mediastore-ending-soon/ "https://aws.amazon.com/blogs/media/support-for-aws-elemental-mediastore-ending-soon/").

# Disabling access logging

for a container

When you disable access logging on a container, AWS Elemental MediaStore stops
sending access logs to Amazon CloudWatch. These access logs are not saved and are not
retrievable.

###### To disable access logging (AWS CLI)

- In the AWS CLI, use the `stop-access-logging` command:

```
aws mediastore stop-access-logging --container-name `LiveEvents` --region `us-west-2`
```

This command has no return value.
