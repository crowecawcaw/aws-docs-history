# Updating file systems

This topic explains which properties of an existing
file system that you can update, and provides procedures to do so using the Amazon FSx console and CLI.
You can update the following FSx for ONTAP file system properties using the Amazon FSx
console, AWS CLI, and API:

- **Automatic daily backups**.
  Turns automatic daily backups on or off, modifies the backup window and the backup
  retention period. For more information, see
  [Automatic daily backups](using-backups.md#automatic-backups "using-backups.md#automatic-backups").
- **Weekly maintenance window**. Sets the day of
  the week and time that Amazon FSx performs file system maintenance and updates. For more
  information, see [Optimizing performance with Amazon FSx maintenance windows](maintenance-windows.md "maintenance-windows.md").
- **File system administrative password**. Changes
  the password for the file system's `fsxadmin` user. You can use the
  `fsxadmin` user to administer your file system using the ONTAP CLI and REST API.
  For more information about the `fsxadmin` user,
  see [Managing file systems with the ONTAP CLI](managing-resources-ontap-apps.md#fsxadmin-ontap-cli "managing-resources-ontap-apps.md#fsxadmin-ontap-cli").
- **Amazon VPC route tables**.
  With Multi-AZ FSx for ONTAP file systems, the endpoints you use to access data over NFS or SMB
  and the management endpoints to access the ONTAP CLI, API, and NetApp Console use floating IP addresses
  in the Amazon VPC route tables that you associate with your file system.
  You can associate new route tables that you create with your existing Multi-AZ file systems—allowing
  you to configure which clients can access your data even as your network evolves. You can
  also disassociate (remove) existing route tables from your file system.

###### Note

Amazon FSx manages VPC route tables for Multi-AZ file systems using tag-based authentication.
These route tables are tagged with `Key: AmazonFSx; Value: ManagedByAmazonFSx`.
When creating or updating FSx for ONTAP Multi-AZ file systems using CloudFormation we recommend that you add the
`Key: AmazonFSx; Value: ManagedByAmazonFSx` tag manually.
The following procedures provide you with instructions on how to make updates to an existing FSx for ONTAP
file system using the AWS Management Console.

###### To update automatic daily backups

1. Open the Amazon FSx console at [https://console.aws.amazon.com/fsx/](https://console.aws.amazon.com/fsx/ "https://console.aws.amazon.com/fsx/").
2. To display the file system details page, in the left navigation pane,
   choose **File systems**, and then choose the
   FSx for ONTAP file system that you want to update.
3. Choose the **Backups** tab in the second panel on the page.
4. Choose **Update**.
5. Modify the automatic daily backup settings for this file system.
6. Choose **Save** to save your changes.

###### To update the weekly maintenance window

1. Open the Amazon FSx console at [https://console.aws.amazon.com/fsx/](https://console.aws.amazon.com/fsx/ "https://console.aws.amazon.com/fsx/").
2. To display the file system details page, in the left navigation pane,
   choose **File systems**, and then choose the
   FSx for ONTAP file system that you want to update.
3. Choose the **Administration** tab in the second panel on the page.
4. In the **Maintenance** pane, choose **Update**.
5. Modify when the weekly maintenance window occurs for this file system.
6. Choose **Save** to save your changes.

###### To change the file system administrative password

1. Open the Amazon FSx console at [https://console.aws.amazon.com/fsx/](https://console.aws.amazon.com/fsx/ "https://console.aws.amazon.com/fsx/").
2. To display the file system details page, in the left navigation pane,
   choose **File systems**, and then choose the
   FSx for ONTAP file system that you want to update.
3. Choose the **Administration** tab.
4. In the **ONTAP administration** panel,
   choose **Update** under
   **ONTAP administrator password**.
5. In the **Update ONTAP administrator credentials**
   dialog box, enter a new password in the **ONTAP administrative password** field.
6. Use the **Confirm password** field to confirm the password.
7. Choose **Update credentials** to save your change.

###### Note

If you receive an error stating that the new password does not meet the password requirements,
you can use the
[`security login role config show`](https://docs.netapp.com/us-en/ontap-cli-9141/security-login-role-config-show.html#description "https://docs.netapp.com/us-en/ontap-cli-9141/security-login-role-config-show.html#description")
ONTAP CLI command to view the password requirement settings on the file system.
For more information, including instructions on how to change password setting, see
[Updating the fsxadmin account password fails](updating-admin-password.md "updating-admin-password.md").

###### To update VPC route tables on Multi-AZ file systems

1. Open the Amazon FSx console at [https://console.aws.amazon.com/fsx/](https://console.aws.amazon.com/fsx/ "https://console.aws.amazon.com/fsx/").
2. To display the file system details page, in the left navigation pane,
   choose **File systems**, and then choose the
   FSx for ONTAP file system that you want to update.
3. For **Actions**, choose **Update file system > Update route tables**.
   Or, in the **Network & security** panel, choose
   **Manage** next to the file system's **Route tables**.
4. In the **Manage route tables** dialog box. do
   one of the following:
   - To associate a new VPC route table, select a route table
     from the **Associate new route tables** dropdown
     list, and then choose **Associate**.
   - To disassociate an existing VPC route table, select a route table
     from the **Current route tables** pane, and then
     choose **Disassociate**.

5. Choose **Close**.
   The following procedure illustrates how to make updates to an existing FSx for ONTAP file system
   using the AWS CLI.

6. To update the configuration of an FSx for ONTAP file system, use the
   [update-file-system](../../../cli/latest/reference/fsx/update-file-system.md "../../../cli/latest/reference/fsx/update-file-system.md") CLI command (or the equivalent
   [UpdateFileSystem](../APIReference/API_UpdateFileSystem.md "../APIReference/API_UpdateFileSystem.md") API operation), as shown in the
   following example.

```
`aws fsx update-file-system \
 --file-system-id fs-0123456789abcdef0 \
 --ontap-configuration AutomaticBackupRetentionDays=30,DailyAutomaticBackupStartTime=01:00, \
 WeeklyMaintenanceStartTime=1:01:30,AddRouteTableIds=rtb-0123abcd, \
 FsxAdminPassword=`new-fsx-admin-password``
```

2. To disable automatic daily backups, set the
   `AutomaticBackupRetentionDays` property to 0.

```
`aws fsx update-file-system \
 --file-system-id fs-0123456789abcdef0 \
 --ontap-configuration AutomaticBackupRetentionDays=0`
```
