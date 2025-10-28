End of support notice: On November 13, 2025, AWS will discontinue support
for AWS Elemental MediaStore. After November 13, 2025, you will no longer be able to access the MediaStore console
or MediaStore resources. For more information, visit this
[blog post](https://aws.amazon.com/blogs/media/support-for-aws-elemental-mediastore-ending-soon/ "https://aws.amazon.com/blogs/media/support-for-aws-elemental-mediastore-ending-soon/").

# Enabling access logging for

a container

By default, AWS Elemental MediaStore doesn't collect access logs. When you enable
access logging on a container, MediaStore delivers access logs for objects
stored in that container to Amazon CloudWatch. The access logs provide detailed records
for requests that are made to any object stored in the container. This
information can include the request type, the resources that are specified in
the request, and the time and date that the request was processed.

###### Important

There is no extra charge for enabling access logging on an MediaStore
container. However, any log files that the service delivers to you accrues
the usual charges for storage. (You can delete the log files at any time.)
AWS doesn't assess data transfer charges for log file delivery, but does
charge the normal data transfer rate for accessing the log files.

###### To enable access logging (AWS CLI)

- In the AWS CLI, use the `start-access-logging`
  command:

```
aws mediastore start-access-logging --container-name `LiveEvents` --region `us-west-2`
```

This command has no return value.
