# How SnapLock works

SnapLock can help you meet regulatory and governance purposes by
preventing your files from being deleted, changed, or renamed. When you create a
SnapLock volume, you commit your files to write once, read many
(WORM) storage and set retention periods for the data. Your files can be stored in a
non-erasable, non-writable state for a designated period, or indefinitely.

###### Important

You must specify whether a volume will use SnapLock settings at the
time of creation. A non-SnapLock volume can't be converted to a
SnapLock volume after creation.

## Retention modes

SnapLock has two retention modes: Compliance and Enterprise.
Amazon FSx for NetApp ONTAP supports both of them. They have different use cases and some of the
features differ, but they both protect your data from modification or deletion using
the WORM model. The following table explains some of the similarities and
differences between these retention modes.

| SnapLock feature                                                                                               | [Understanding SnapLock Compliance](snaplock-compliance.md "snaplock-compliance.md")                                                                                          | [Understanding SnapLock Enterprise](snaplock-enterprise.md "snaplock-enterprise.md")                                                                       |
| -------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Description                                                                                                    | Files transitioned to WORM on a Compliance volume can't be<br>deleted until their retention periods expire.                                                                   | Files transitioned to WORM on an Enterprise volume can be deleted<br>by authorized users before their retention periods expire using<br>privileged delete. |
| Use cases                                                                                                      | • To address government or industry-specific mandates<br>such as SEC Rule 17a-4(f), FINRA Rule 4511, and CFTC<br>Regulation 1.31.<br>• To protect against ransomware attacks. | • To advance an organization's data integrity and<br>internal compliance.<br>• To test retention settings before using<br>SnapLock Compliance.             |
| [Autocommit](worm-state.md#worm-state-autocommit "worm-state.md#worm-state-autocommit")                        | Yes                                                                                                                                                                           | Yes                                                                                                                                                        |
| [Event-based retention (EBR)](worm-state.md#worm-state-ebr "worm-state.md#worm-state-ebr")1                    | Yes                                                                                                                                                                           | Yes                                                                                                                                                        |
| [Legal Hold](worm-state.md#worm-state-legal-hold "worm-state.md#worm-state-legal-hold")1                       | Yes                                                                                                                                                                           | No                                                                                                                                                         |
| [Using privileged delete](snaplock-enterprise.md#privileged-delete "snaplock-enterprise.md#privileged-delete") | No                                                                                                                                                                            | Yes                                                                                                                                                        |
| [Volume-append mode](worm-state.md#worm-state-append "worm-state.md#worm-state-append")                        | Yes                                                                                                                                                                           | Yes                                                                                                                                                        |
| [SnapLock audit log volumes](#snaplock-audit-log-volume "#snaplock-audit-log-volume")                          | Yes                                                                                                                                                                           | Yes                                                                                                                                                        |

###### Note

1EBR and Legal Hold operations are supported in the
ONTAP CLI and REST API.

###### Note

FSx for ONTAP supports tiering data to the capacity pool on all SnapLock volumes, regardless of the SnapLock type.
For more information, see [Volume data tiering](volume-storage-capacity.md#volume-data-tiering "volume-storage-capacity.md#volume-data-tiering").

## SnapLock administrator

You must have SnapLock administrator privileges to perform certain
actions on SnapLock volumes. SnapLock administrator
privileges are defined in the `vsadmin-snaplock` role in the ONTAP CLI.
You must be a cluster administrator to create
a storage virtual machine (SVM)
administrator account with the SnapLock administrator role.

You can perform the following actions with the `vsadmin-snaplock` role in the ONTAP CLI:

- Manage your own user account, local password, and key information
- Manage volumes, except moving volumes
- Manage quotas, qtrees, snapshot copies, and files
- Perform SnapLock actions, including privileged delete and
  Legal Hold
- Configure
  Network File System (NFS) and Server Message Block (SMB)
  protocols
- Configure Domain Name System (DNS), Lightweight Directory Access Protocol (LDAP), and Network Information Service (NIS)
  services
- Monitor jobs

The following procedure details how to create a SnapLock
administrator in the ONTAP CLI. You must be logged in as a cluster administrator on
a secure connection, such as Secure Shell Protocol (SSH) to perform this task.

###### To create an SVM administrator account with the vsadmin-snaplock role in the ONTAP CLI

- Run the following command. Replace `SVM_name` and `SnapLockAdmin` with your own information.

```
`cluster1::>` `security login create -vserver `SVM_name` -user-or-group-name `SnapLockAdmin` -application ssh -authentication-method password -role vsadmin-snaplock`
```

For more information, see [ONTAP roles and users](roles-and-users.md "roles-and-users.md").

## SnapLock audit log volumes

A SnapLock audit log volume contains SnapLock audit logs, which
contain timestamps of events such as when a SnapLock administrator was created, when
privileged delete operations were executed, or when a Legal Hold was placed on
files. The SnapLock audit log volume is a non-erasable record of events.

You must create a SnapLock audit log volume in the same SVM as the SnapLock volume for the
following actions:

- To turn on or turn off privileged delete on a SnapLock Enterprise volume.
- To apply Legal Hold on a file in a SnapLock Compliance volume.

###### Warning

- The minimum retention period for a SnapLock audit log volume is six
  months. Until this retention period expires, the SnapLock audit log
  volume and the SVM and file system that are associated with it can't be
  deleted even if the volume was created in SnapLock Enterprise mode.
- If a file is deleted using privileged delete and its retention period is
  longer than the retention period of the volume, then the audit log
  volume inherits the file's retention period. For example, if a file that
  has a retention period of 10 months is deleted using privileged delete
  and the retention period of the audit log volume is six months, the
  retention period of the audit log volume is extended to 10 months.

You can have only one active SnapLock audit log volume in an SVM, but it can be shared by multiple SnapLock
volumes in the SVM. To mount a SnapLock audit log volume successfully, set the junction path to
`/snaplock_audit_log`. No other volumes can use this junction path, including volumes that aren't
audit log volumes.

You can find SnapLock audit logs in the `/snaplock_log` directory
under the root of the audit log volume. Privileged delete operations are logged in
the `privdel_log` subdirectory. Legal Hold begin and end operations are
logged in `/snaplock_log/legal_hold_logs/`. All other logs are stored in
the `system_log` subdirectory.

You can create a SnapLock audit log volume with the
Amazon FSx console, the AWS CLI, the Amazon FSx API, and the ONTAP CLI and REST API.

###### Note

A data protection (DP)
volume can't be used as a SnapLock audit log volume.

To turn on the SnapLock audit log volume with the Amazon FSx API, use
`AuditLogVolume` in the [`CreateSnaplockConfiguration`](../APIReference/API_CreateSnaplockConfiguration.md "../APIReference/API_CreateSnaplockConfiguration.md"). In the Amazon FSx console, for **Audit log volume**, choose **Enabled**. Make sure that the **Junction path** is set to
`/snaplock_audit_log`.

## Accessing your data in a SnapLock volume

You can use open file protocols such as NFS and SMB to access your data in a
SnapLock volume. There is no performance impact from writing data to a SnapLock
volume or from reading data that's protected by WORM.

You can copy files across SnapLock volumes with NFS and SMB, but they
won't retain their WORM properties on the destination SnapLock volume. You must recommit the copied
files to WORM to prevent them from being modified or deleted. For more information,
see [Committing files to WORM state](worm-state.md "worm-state.md").

You can also replicate SnapLock data with SnapMirror,
but the source and destination volumes must be SnapLock
volumes with the same retention mode (for example, both must be Compliance or Enterprise).

## SnapLock and SSD capacity decrease operations

Consider these points about SSD decreases before creating a SnapLock volume:

- Amazon FSx will reject SSD capacity decrease requests on file systems that contain SnapLock volumes.
- You can't create SnapLock volumes during an SSD capacity decrease operation.

These limitations exist because ONTAP enforces a minimum retention period of 6 months for the SnapLock audit log volume, which would prevent file system deletion during that period if a SnapLock volume were moved as part of an SSD decrease operation.

If you need to decrease SSD capacity on a file system with SnapLock volumes, you would need to migrate your data to a new file system with smaller SSD capacity. For more information about SSD capacity decrease operations, including limitations and considerations, see [Updating file system SSD storage and IOPS](storage-capacity-and-IOPS.md#increase-primary-storage "storage-capacity-and-IOPS.md#increase-primary-storage").
