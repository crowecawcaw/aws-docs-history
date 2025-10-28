# Deleting mount targets

When you delete a mount target, the operation forcibly breaks any mounts of the file
system, which might disrupt instances or applications using those mounts. To avoid
application disruption, stop applications and unmount the file system before deleting the
mount target. For more information, see [Unmounting file systems](unmounting-fs.md "unmounting-fs.md").

You can delete mount targets for a file system by using the AWS Management Console, AWS CLI, or
programmatically by using the AWS SDKs.

Use the following procedure to delete mount targets for an existing EFS
file system.

###### To delete mount targets on an EFS file system

1. Unmount the file system. For instructions, see [Unmounting file systems](unmounting-fs.md "unmounting-fs.md").
2. Open the Amazon Elastic File System console at
   [https://console.aws.amazon.com/efs/](https://console.aws.amazon.com/efs/ "https://console.aws.amazon.com/efs/").
3. In the left navigation pane, choose **File systems**, and
   then select the file system for which you want to delete the mount target.
4. Choose **Network** and then choose
   **Manage** to display the mount targets for the file
   system.
5. For each mount target you want to delete, choose
   **Remove**.
6. Choose **Save**.
   To delete an existing mount target, use the `delete-mount-target` AWS CLI
   command (corresponding operation is [DeleteMountTarget](API_DeleteMountTarget.md "API_DeleteMountTarget.md")), as shown following.

###### Note

Before deleting a mount target, first unmount the file system.

```
`$` aws efs delete-mount-target \
--mount-target-id `mount-target-ID-to-delete` \
--region `aws-region-where-mount-target-exists`
```

The following is an example with sample data.

```
`$` aws efs delete-mount-target \
--mount-target-id fsmt-5751852e \
--region us-east-2 \
```
