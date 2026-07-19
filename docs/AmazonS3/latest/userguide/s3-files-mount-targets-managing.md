# Managing mount targets

You can add or remove security groups associated with a mount target. Security groups
define inbound and outbound access. When you change security groups associated with a mount
target, make sure that you authorize necessary inbound and outbound access. Doing so enables
your compute resource to communicate with the file system. See [Security groups](s3-files-prereq-policies.md#s3-files-prereq-security-groups "s3-files-prereq-policies.md#s3-files-prereq-security-groups") in the prerequisites to understand the
security group configurations required to start using your file system.

This section explains how to use the Amazon S3 console to add or remove security
groups for a mount target in S3 Files.

1. Sign in to the AWS Management Console and open the Amazon S3
   console at [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. In the navigation bar, verify you are in the
   desired AWS Region where your mount target
   exists.
3. In the left navigation pane, choose **General
   purpose buckets**.
4. Choose a general purpose bucket your file system is attached
   to.
5. Select the **File systems** tab and
   select your desired file system.
6. Select the **Mount targets** tab and
   select the mount target that you want to edit.
7. Choose **Edit**. You will see details
   of your mount target.
8. Add or remove security groups from the security group drop
   down.
9. Choose **Save**.
   The following `update-mount-target` example command shows how you can
   use the AWS CLI to add or remove security groups for a mount target in S3
   Files.

```
aws s3files update-mount-target --region `aws-region` --mount-target-id `mount-target-id` --security-groups `security-group-ids-separated-by-space`
```
