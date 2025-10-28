# Monitoring throughput capacity

changes

You can monitor the progress of a throughput capacity modification using the Amazon FSx
console, the API, and the AWS CLI.

## Monitoring throughput capacity changes

in the console

On the **Updates** tab in the **File system details**
window, you can view the 10 most recent update actions for each update action type.

For throughput capacity update actions, you can view the following information.

\***\*Update type\*\***

Supported types are **Throughput capacity**, **Storage
capacity**, and **Storage optimization**.

\***\*Target value\*\***

The desired value to change the file system's throughput capacity to.

\***\*Status\*\***

The current status of the update. For throughput capacity updates, the possible
values are as follows:

- **Pending** – Amazon FSx has received the update request,
  but has not started processing it.
- **In progress** – Amazon FSx is processing the update
  request.
- **Completed** – The throughput capacity update
  completed successfully.
- **Failed** – The throughput capacity update failed.
  Choose the question mark (**?**) to see details on why the
  throughput update failed.

\***\*Request time\*\***

The time when Amazon FSx received the update request.

## Monitoring changes with the AWS CLI and

API

You can view and monitor file system throughput capacity modification requests using the
[describe-file-systems](../../../cli/latest/reference/fsx/describe-file-systems.md "../../../cli/latest/reference/fsx/describe-file-systems.md") CLI command and the [DescribeFileSystems](../APIReference/API_DescribeFileSystems.md "../APIReference/API_DescribeFileSystems.md") API
action. The `AdministrativeActions` array lists the 10 most recent update actions
for each administrative action type. When you modify a file system's throughput capacity, a
`FILE_SYSTEM_UPDATE` administrative action is generated.

The following example shows the response excerpt of a `describe-file-systems`
CLI command. The file system has a throughput capacity of 128 MBps, and a target throughput
capacity of 256 MBps.

```
.
.
.
    "ThroughputCapacity": 128,
"AdministrativeActions": [
    {
        "AdministrativeActionType": "FILE_SYSTEM_UPDATE",
        "RequestTime": 1581694764.757,
        "Status": "PENDING",
        "TargetFileSystemValues": {
          "OntapConfiguration": {
            "ThroughputCapacity": 256
          }
        }
    }
]
```

When Amazon FSx processes the action successfully, the status changes to
`COMPLETED`. The new throughput capacity is then available to the file system,
and shows in the `ThroughputCapacity` property. This is shown in the following
response excerpt of a **describe-file-systems** CLI command.

```
.
.
.
    "ThroughputCapacity": 256,
"AdministrativeActions": [
    {
        "AdministrativeActionType": "FILE_SYSTEM_UPDATE",
        "RequestTime": 1581694764.757,
        "Status": "COMPLETED",
        "TargetFileSystemValues": {
          "OntapConfiguration": {
            "ThroughputCapacity": 256
          }
        }
    }
]
```

If the throughput capacity modification fails, the status changes to
`FAILED`, and the `FailureDetails` property provides information about
the failure.
