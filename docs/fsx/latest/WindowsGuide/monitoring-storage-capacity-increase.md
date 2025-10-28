# Monitoring storage capacity

increases

After increasing your file system's storage capacity, you can monitor the progress of the storage capacity increase using the Amazon FSx console,
the API, or the AWS CLI as described in the following procedures.

In the **Updates** tab in the **File system
details** window, you can view the 10 most recent updates for each
update type.

For storage capacity updates, you can view the following information.

\***\*Update type\*\***

Possible values are **Storage capacity**.

\***\*Target value\*\***

The desired value to update the file system's storage capacity
to.

\***\*Status\*\***

The current status of the update. For storage capacity updates, the
possible values are as follows:

- **Pending** – Amazon FSx has received the
  update request, but has not started processing it.
- **In progress** – Amazon FSx is processing
  the update request.
- **Updated optimizing** – Amazon FSx has
  increased the file system's storage capacity. The storage
  optimization process is now moving the file system data to the
  new larger disks.
- **Completed** – The storage capacity
  increase completed successfully.
- **Failed** – The storage capacity
  increase failed. Choose the question mark
  (**?**) to see details on why the storage
  update failed.

\***\*Progress %\*\***

Displays the progress of the storage optimization process as percent
complete.

\***\*Request time\*\***

The time that Amazon FSx received the update action request.

You can view and monitor file system storage capacity increase requests using the
[describe-file-systems](../../../cli/latest/reference/fsx/describe-file-systems.md "../../../cli/latest/reference/fsx/describe-file-systems.md") AWS CLI command and the [DescribeFileSystems](../APIReference/API_DescribeFileSystems.md "../APIReference/API_DescribeFileSystems.md") API action. The `AdministrativeActions`
array lists the 10 most recent update actions for each administrative action type.
When you increase a file system's storage capacity, two
`AdministrativeActions` are generated: a
`FILE_SYSTEM_UPDATE` and a `STORAGE_OPTIMIZATION` action.

The following example shows an excerpt of the response of a
**describe-file-systems** CLI command. The file system has a
storage capacity of 300 GB, and there is a pending administrative action to increase
the storage capacity to 1000 GB.

```
{
    "FileSystems": [
        {
            "OwnerId": "111122223333",
            .
            .
            .
            "StorageCapacity": 300,
            "AdministrativeActions": [
                {
                     "AdministrativeActionType": "FILE_SYSTEM_UPDATE",
                     "RequestTime": 1581694764.757,
                     "Status": "PENDING",
                     "TargetFileSystemValues": {
                         "StorageCapacity": 1000
                     }
                },
                {
                    "AdministrativeActionType": "STORAGE_OPTIMIZATION",
                    "RequestTime": 1581694764.757,
                    "Status": "PENDING",
                }
            ]
```

Amazon FSx processes the `FILE_SYSTEM_UPDATE` action first, adding the new
larger storage disks to the file system. When the new storage is available to the
file system, the `FILE_SYSTEM_UPDATE` status changes to
`UPDATED_OPTIMIZING`. The storage capacity shows the new larger
value, and Amazon FSx begins processing the `STORAGE_OPTIMIZATION`
administrative action. This is shown in the following excerpt of the response of a
**describe-file-systems** CLI command.

The `ProgressPercent` property displays the progress of the storage
optimization process. After the storage optimization process completes successfully,
the status of the `FILE_SYSTEM_UPDATE` action changes to
`COMPLETED`, and the `STORAGE_OPTIMIZATION` action no
longer appears.

```
{
    "FileSystems": [
        {
            "OwnerId": "111122223333",
            .
            .
            .
            "StorageCapacity": 1000,
            "AdministrativeActions": [
                {
                    "AdministrativeActionType": "FILE_SYSTEM_UPDATE",
                    "RequestTime": 1581694764.757,
                    "Status": "UPDATED_OPTIMIZING",
                    "TargetFileSystemValues": {
                        "StorageCapacity": 1000
                }
                },
                {
                    "AdministrativeActionType": "STORAGE_OPTIMIZATION",
                    "RequestTime": 1581694764.757,
                    "Status": "IN_PROGRESS",
                    "ProgressPercent": 50,
                }
            ]
```

If the storage capacity increase fails, the status of the
`FILE_SYSTEM_UPDATE` action changes to `FAILED`. The
`FailureDetails` property provides information about the failure,
shown in the following example.

```
{
    "FileSystems": [
        {
            "OwnerId": "111122223333",
            .
            .
            .
            "StorageCapacity": 300,
            "AdministrativeActions": [
                {
                    "AdministrativeActionType": "FILE_SYSTEM_UPDATE",
                    "FailureDetails": {
                        "Message": "string"
                    },
                    "RequestTime": 1581694764.757,
                    "Status": "FAILED",
                    "TargetFileSystemValues":
                        "StorageCapacity": 1000
                }
            ]
```

For information about troubleshooting failed actions, see [Storage or throughput capacity updates fail](admin-actions-ts.md "admin-actions-ts.md").
