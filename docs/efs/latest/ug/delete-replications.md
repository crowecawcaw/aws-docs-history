# Deleting replication configurations

If you need to fail over to the destination file system, delete the replication
configuration of which it is a member. After you delete a replication configuration, the
destination file system becomes writeable and its replication overwrite protection is re-enabled.
For more information, see [Using the replica](replication-fail-over.md "replication-fail-over.md").

Deleting a replication configuration and changing the destination file system to be
writeable can take several minutes to complete. After the configuration is deleted, Amazon EFS might
write some data to a `lost+found` directory in the root directory of the destination
file system, using the following naming convention:

```
efs-replication-lost+found-`source-file-system-id-TIMESTAMP`
```

###### Note

You cannot delete a file system that is part of a replication configuration. You must
delete the replication configuration before deleting the file system.

You can delete an existing replication configuration from either the source or the
destination file system by using the Amazon EFS console, the AWS CLI, or the API.

For cross-account or cross-Region replications, Amazon EFS deletes the replication
configuration from both the source and destination accounts or Regions. If there's a
configuration or permissions issue that prevents Amazon EFS from deleting the replication
configuration from both sides, you can delete the configuration from only the local side (the
account or Region from which the delete is performed). Deleting the local configuration leaves
the configuration in the other account or Region unrecoverable.

1. Open the Amazon Elastic File System console at
   [https://console.aws.amazon.com/efs/](https://console.aws.amazon.com/efs/ "https://console.aws.amazon.com/efs/").
2. In the left navigation pane, choose **File systems**.
3. Choose either the source or the destination file system that is in the replication
   configuration that you want to delete.
4. Choose the **Replication** tab to display the
   **Replication** section.
5. Choose **Delete replication** to delete the replication configuration.
   When prompted, confirm your choice.

If you are deleting a cross-account replication configuration, and there's a problem
that prevents you from deleting the configuration from both the source and destination side,
then you can choose the option to delete this file system's configuration only.

###### Note

Delete the file system's configuration only if Amazon EFS is unable to delete the
replication configuration in both the source and destination account or
Region. Deleting the local configuration leaves the configuration in the
other account or Region unrecoverable.
To delete a replication configuration, use the
`delete-replication-configuration` CLI. The equivalent API command is [DeleteReplicationConfiguration](API_DeleteReplicationConfiguration.md "API_DeleteReplicationConfiguration.md").

The following example deletes the replication configuration for source file system
`fs-0123456789abcdef1`.

```
`aws efs --region `us-west-2` delete-replication-configuration \
--source-file-system-id `fs-0123456789abcdef1``
```

If a configuration or permissions issue prevents Amazon EFS from deleting the replication
configuration from both sides, you can delete the configuration from only the local side (the
account or Region from which the delete is performed). Deleting the local
configuration leaves the configuration in the other account or Region
unrecoverable. The equivalent API parameter is `DeletionMode` and the value is
`LOCAL_CONFIGURATION_ONLY`.

The following example deletes the replication configuration for source file system
`fs-0123456789abcdef1` from the local side only.

```
`aws efs --region `us-west-2` delete-replication-configuration \
--source-file-system-id `fs-0123456789abcdef1`
--deletion-mode LOCAL_CONFIGURATION_ONLY`
```
