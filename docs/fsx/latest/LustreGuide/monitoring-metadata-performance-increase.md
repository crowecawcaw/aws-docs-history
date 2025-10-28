# Monitoring metadata configuration updates

You can monitor the progress of metadata configuration updates by using the Amazon FSx console,
the API, or the AWS CLI.

You can monitor metadata configuration updates in the **Updates** tab on the
**File system details** page.

For metadata configuration updates, you can view the following information:

\***\*Update type\*\***

Supported types are **Metadata IOPS** and
**Metadata configuration mode**.

\***\*Target value\*\***

The updated value for the file system's Metadata IOPS or
Metadata configuration mode.

\***\*Status\*\***

The current status of the update. The possible values are as follows:

- **Pending** – Amazon FSx has received the update request, but has not
  started processing it.
- **In progress** – Amazon FSx is processing the update request.
- **Completed** – The update finished successfully.
- **Failed** – The update request failed. Choose the question
  mark (**?**) to see details on why the request failed.

\***\*Request time\*\***

The time that Amazon FSx received the update action request.

You can view and monitor metadata configuration update requests using the
[describe-file-systems](../../../cli/latest/reference/fsx/describe-file-systems.md "../../../cli/latest/reference/fsx/describe-file-systems.md") AWS CLI command and the
[DescribeFileSystems](../APIReference/API_DescribeFileSystems.md "../APIReference/API_DescribeFileSystems.md") API operation. The `AdministrativeActions` array
lists the 10 most recent update actions for each administrative action type. When you
update a file system's metadata performance or metadata configuration mode,
a `FILE_SYSTEM_UPDATE` `AdministrativeActions` is generated.

The following example shows an excerpt of the response of a `describe-file-systems`
CLI command. The file system has a pending administrative action to increase the Metadata IOPS
to 96000 and the metadata configuration mode to USER_PROVISIONED.

```
"AdministrativeActions": [
    {
        "AdministrativeActionType": "FILE_SYSTEM_UPDATE",
        "RequestTime": 1678840205.853,
        "Status": "PENDING",
        "TargetFileSystemValues": {
            "LustreConfiguration": {
                "MetadataConfiguration": {
                    "Iops": 96000,
                    "Mode": USER_PROVISIONED
                }
            }
        }
    }
]
```

Amazon FSx processes the `FILE_SYSTEM_UPDATE` action, modifying the file system's
Metadata IOPS and metadata configuration mode. When the new metadata resources are available
to the file system the `FILE_SYSTEM_UPDATE` status changes to `COMPLETED`.

If the metadata configuration update request fails, the status of the `FILE_SYSTEM_UPDATE`
action changes to `FAILED`, as shown in the following example. The `FailureDetails`
property provides information about the failure.

```
"AdministrativeActions": [
    {
        "AdministrativeActionType": "FILE_SYSTEM_UPDATE",
        "RequestTime": 1678840205.853,
        "Status": "FAILED",
        "TargetFileSystemValues": {
            "LustreConfiguration": {
                "MetadataConfiguration": {
                    "Iops": 96000,
                    "Mode": USER_PROVISIONED
                }
            }
        },
        "FailureDetails": {
            "Message": "`failure-message`"
        }
    }
]
```
