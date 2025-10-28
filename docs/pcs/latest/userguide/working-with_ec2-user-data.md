# Working with Amazon EC2 user data for AWS PCS

You can supply EC2 user data in your launch template that `cloud-init` runs when
your instances launch. User data blocks with the content type `cloud-config` run before
the instance registers with the AWS PCS API, while user data blocks with content type
`text/x‑shellscript` run after registration completes, but before the Slurm
daemon starts. For more information about content types, see the [cloud-init
documentation](https://cloudinit.readthedocs.io/en/latest/explanation/format.html "https://cloudinit.readthedocs.io/en/latest/explanation/format.html").

our user data can perform common configuration scenarios, including but not limited to the
following:

- [Including users or groups](https://cloudinit.readthedocs.io/en/latest/topics/examples.html#including-users-and-groups "https://cloudinit.readthedocs.io/en/latest/topics/examples.html#including-users-and-groups")
- [Installing packages](https://cloudinit.readthedocs.io/en/latest/topics/examples.html#install-arbitrary-packages "https://cloudinit.readthedocs.io/en/latest/topics/examples.html#install-arbitrary-packages")
- [Creating partitions and file systems](https://cloudinit.readthedocs.io/en/latest/topics/examples.html#create-partitions-and-filesystems "https://cloudinit.readthedocs.io/en/latest/topics/examples.html#create-partitions-and-filesystems")
- Mounting network file systems
  User data in launch templates must be in the [MIME
  multi-part archive](https://cloudinit.readthedocs.io/en/latest/topics/format.html#mime-multi-part-archive "https://cloudinit.readthedocs.io/en/latest/topics/format.html#mime-multi-part-archive") format. This is because your user data is merged with other
  AWS PCS user data that is required to configure nodes in your node group. You can combine
  multiple user data blocks together into a single MIME multi-part file.

A MIME multi-part file consists of the following components:

- The content type and part boundary declaration: `Content-Type: multipart/mixed;
boundary="==BOUNDARY=="`
- The MIME version declaration: `MIME-Version: 1.0`
- One or more user data blocks that contain the following components:
  - The opening boundary that signals the beginning of a user data block:
    `--==BOUNDARY==`. You must keep the line before this boundary blank.
  - The content type declaration for the block: `Content-Type: text/cloud-config;
charset="us-ascii"` or `Content-Type: text/x-shellscript;
charset="us-ascii"`. You must keep the line after the content type declaration blank.
  - The content of the user data, such as a list of shell commands or
    `cloud-config` directives.

- The closing boundary that signals the end of the MIME multi-part file:
  `--==BOUNDARY==--`. You must keep the line before the closing boundary blank.

###### Note

If you add user data to a launch template in the Amazon EC2 console, you can paste it in as
plain text. Or, you can upload it from a file. If you use the AWS CLI or an AWS SDK, you must
first base64 encode the user data and submit that string as the value of the
`UserData` parameter when you call [CreateLaunchTemplate](../../../AWSEC2/latest/APIReference/API_CreateLaunchTemplate.md "../../../AWSEC2/latest/APIReference/API_CreateLaunchTemplate.md"), as
shown in this JSON file.

```
{
    "LaunchTemplateName": "base64-user-data",
    "LaunchTemplateData": {
        "UserData": "ewogICAgIkxhdW5jaFRlbXBsYXRlTmFtZSI6ICJpbmNyZWFzZS1jb250YWluZXItdm9sdW..."
    }
}
```

###### Examples

- [Example: Install software from a package repository](working-with_ec2-user-data_repo.md "working-with_ec2-user-data_repo.md")
- [Example: Run scripts from an S3 bucket](working-with_ec2-user-data_s3.md "working-with_ec2-user-data_s3.md")
- [Example: Set global environment variables](working-with_ec2-user-data_env.md "working-with_ec2-user-data_env.md")
- [Using network file systems with AWS PCS](working-with_file-systems.md "working-with_file-systems.md")
- [Example: Use an EFS file system as a shared home directory](working-with_ec2-user-data_efs.md "working-with_ec2-user-data_efs.md")
