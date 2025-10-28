# Monitoring storage capacity increases

You can monitor the progress of a storage capacity increase using the Amazon FSx console, the API,
or the AWS CLI.

In the **Updates** tab in the file system details page, you can
view the 10 most recent updates for each update type.

You can view the following information:

\***\*Update type\*\***

Supported types are **Storage capacity** and **Storage
optimization**.

\***\*Target value\*\***

The desired value to update the file system's storage capacity to.

\***\*Status\*\***

The current status of the storage capacity updates. The possible values are as follows:

- **Pending** – Amazon FSx has received the update request, but
  has not started processing it.
- **In progress** – Amazon FSx is processing the update request.
- **Updated; Optimizing** – Amazon FSx has increased the file system's
  storage capacity. The storage optimization process is now rebalancing data across the file servers.
- **Completed** – The storage capacity increase completed
  successfully.
- **Failed** – The storage capacity increase failed. Choose the question
  mark (**?**) to see details on why the storage update failed.

\***\*Progress %\*\***

Displays the progress of the storage optimization process as percent complete.

\***\*Request time\*\***

The time that Amazon FSx received the update action request.

You can view and monitor file system storage capacity increase requests using the [describe-file-systems](../../../cli/latest/reference/fsx/describe-file-systems.md "../../../cli/latest/reference/fsx/describe-file-systems.md") AWS CLI command and the [DescribeFileSystems](../APIReference/API_DescribeFileSystems.md "../APIReference/API_DescribeFileSystems.md") API action. The `AdministrativeActions`
array lists the 10 most recent update actions for each administrative action type.
When you increase a file system's storage capacity, two
`AdministrativeActions` are generated: a
`FILE_SYSTEM_UPDATE` and a `STORAGE_OPTIMIZATION` action.

The following example shows an excerpt of the response of a
**describe-file-systems** CLI command. The file system has a
storage capacity of 4800 GB, and there is a pending administrative action to increase
the storage capacity to 9600 GB.

```
{
    "FileSystems": [
        {
            "OwnerId": "111122223333",
            .
            .
            .
            "StorageCapacity": 4800,
            "AdministrativeActions": [
                {
                     "AdministrativeActionType": "FILE_SYSTEM_UPDATE",
                     "RequestTime": 1581694764.757,
                     "Status": "PENDING",
                     "TargetFileSystemValues": {
                         "StorageCapacity": 9600
                     }
                },
                {
                    "AdministrativeActionType": "STORAGE_OPTIMIZATION",
                    "RequestTime": 1581694764.757,
                    "Status": "PENDING",
                }
            ]
```

Amazon FSx processes the `FILE_SYSTEM_UPDATE` action first, adding new file
servers to the file system. When the new storage is available to the file
system, the `FILE_SYSTEM_UPDATE` status changes to
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
            "StorageCapacity": 9600,
            "AdministrativeActions": [
                {
                    "AdministrativeActionType": "FILE_SYSTEM_UPDATE",
                    "RequestTime": 1581694764.757,
                    "Status": "UPDATED_OPTIMIZING",
                    "TargetFileSystemValues": {
                        "StorageCapacity": 9600
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

If the storage capacity increase fails, the status of the `FILE_SYSTEM_UPDATE`
action changes to `FAILED`. The `FailureDetails` property
provides information about the failure, shown in the following example.

```
{
    "FileSystems": [
        {
            "OwnerId": "111122223333",
            .
            .
            .
            "StorageCapacity": 4800,
            "AdministrativeActions": [
                {
                    "AdministrativeActionType": "FILE_SYSTEM_UPDATE",
                    "FailureDetails": {
                        "Message": "string"
                    },
                    "RequestTime": 1581694764.757,
                    "Status": "FAILED",
                    "TargetFileSystemValues":
                        "StorageCapacity": 9600
                }
            ]
```
