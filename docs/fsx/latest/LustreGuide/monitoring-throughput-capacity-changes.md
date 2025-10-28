# Monitoring throughput capacity

changes

You can monitor the progress of a throughput capacity modification using the Amazon FSx
console, the API, and the AWS CLI.

###### Monitoring throughput capacity changes (console)

- On the **Updates** tab in the file system details page, you can
  view the 10 most recent update actions for each update action type.

For throughput capacity update actions, you can view the following information.

\***\*Update type\*\***

Supported type is **Per unit storage throughput**.

\***\*Target value\*\***

The desired value to change the file system's throughput per unit of storage to.

\***\*Status\*\***

The current status of the update. For throughput capacity updates, the possible
values are as follows:

    + **Pending** – Amazon FSx has received the update request,
     but has not started processing it.
    + **In progress** – Amazon FSx is processing the update
     request.
    + **Updated; Optimizing** – Amazon FSx has updated
     the file system's network I/O, CPU, and memory resources. The new disk I/O
     performance level is available for write operations. Your read operations will see
     disk I/O performance between the previous level and the new level until your file
     system is no longer in the this state.
    + **Completed** – The throughput capacity update
     completed successfully.
    + **Failed** – The throughput capacity update failed.
     Choose the question mark (**?**) to see details on why the
     throughput update failed.

\***\*Request time\*\***

The time when Amazon FSx received the update request.

###### Monitoring file system updates (CLI)

- You can view and monitor file system throughput capacity modification requests using the
  [describe-file-systems](../../../cli/latest/reference/fsx/describe-file-systems.md "../../../cli/latest/reference/fsx/describe-file-systems.md") CLI command and the [DescribeFileSystems](../APIReference/API_DescribeFileSystems.md "../APIReference/API_DescribeFileSystems.md") API
  action. The `AdministrativeActions` array lists the 10 most recent update actions
  for each administrative action type. When you modify a file system's throughput capacity, a
  `FILE_SYSTEM_UPDATE` administrative action is generated.

The following example shows the response excerpt of a `describe-file-systems`
CLI command. The file system has a target throughput per unit of storage of 500 MBps/TiB.

```
.
.
.
"AdministrativeActions": [
    {
        "AdministrativeActionType": "FILE_SYSTEM_UPDATE",
        "RequestTime": 1581694764.757,
        "Status": "PENDING",
        "TargetFileSystemValues": {
          "LustreConfiguration": {
            "PerUnitStorageThroughput": 500
          }
        }
    }
]
```

When Amazon FSx processes the action successfully, the status changes to
`COMPLETED`. The new throughput capacity is then available to the file system,
and shows in the `PerUnitStorageThroughput` property.

If the throughput capacity modification fails, the status changes to
`FAILED`, and the `FailureDetails` property provides information about
the failure.
