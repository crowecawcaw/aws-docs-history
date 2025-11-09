# Using an IAM Role to Grant Permissions to Applications and Scripts Running on WorkSpaces Applications Streaming Instances

Applications and scripts that run on WorkSpaces Applications streaming instances must include AWS credentials in their AWS API requests. You can create an IAM role to manage these credentials. An IAM role specifies a set of permissions that you can use to access AWS resources. This role is not uniquely associated with one person, however. Instead, it can be assumed by anyone that needs it.

You can apply an IAM role to an WorkSpaces Applications streaming instance. When the streaming instance switches to (assumes) the role, the role provides temporary security credentials. Your application or scripts use these credentials to perform API actions and management tasks on the streaming instance. WorkSpaces Applications manages the temporary credential switch for you.

###### Contents

- [Best Practices for Using IAM Roles With WorkSpaces Applications Streaming Instances](best-practices-for-using-iam-role-with-streaming-instances.md "best-practices-for-using-iam-role-with-streaming-instances.md")
- [Configuring an Existing IAM Role to Use With WorkSpaces Applications Streaming Instances](configuring-existing-iam-role-to-use-with-streaming-instances.md "configuring-existing-iam-role-to-use-with-streaming-instances.md")
- [How to Create an IAM Role to Use With WorkSpaces Applications Streaming Instances](how-to-create-iam-role-to-use-with-streaming-instances.md "how-to-create-iam-role-to-use-with-streaming-instances.md")
- [How to Use the IAM Role With WorkSpaces Applications Streaming Instances](how-to-use-iam-role-with-streaming-instances.md "how-to-use-iam-role-with-streaming-instances.md")
