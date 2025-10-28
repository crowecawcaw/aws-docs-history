# Viewing an Amazon FSx for OpenZFS file system

This section contains instructions on how to view the details of your FSx for OpenZFS file system using the Amazon FSx console,
the AWS CLI, and the Amazon FSx API, as well as information on the different file system statuses.

###### Topics

- [Viewing file system details (Amazon FSx console,
  AWS CLI, and Amazon FSx API)](#how-to-view-file-system "#how-to-view-file-system")
- [File system status](#file-system-lifecycle-states "#file-system-lifecycle-states")

## Viewing file system details (Amazon FSx console,

AWS CLI, and Amazon FSx API)

###### To view a file system's details (Amazon FSx console, CLI, and API):

- **Using the console** – Choose a file
  system to view the **File systems** detail page. The
  **Summary** panel shows the file system ID, lifecycle
  status, deployment type, Availability Zone, storage type, storage capacity,
  throughput capacity, provisioned IOPS, and creation time. The tabs provide detailed information and configuration functions for the
  file system's features, such as backups and volumes.
- **Using the CLI or API** – Use the
  [describe-file-systems](../../../cli/latest/reference/fsx/describe-file-systems.md "../../../cli/latest/reference/fsx/describe-file-systems.md") CLI command or the [DescribeFileSystems](../APIReference/API_DescribeFileSystems.md "../APIReference/API_DescribeFileSystems.md") API operation.

## File system status

Depending on what actions you have taken on it, your file system will have one of the following statuses. You can find the status of an Amazon FSx file system by viewing the file system details using the instructions in the previous section.

| File system status | Description                                                                                                                                         |
| ------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------- |
| AVAILABLE          | The file system has been successfully created and is available for use.                                                                             |
| CREATING           | Amazon FSx is creating a new file system.                                                                                                           |
| DELETING           | Amazon FSx is deleting an existing file system.                                                                                                     |
| MISCONFIGURED      | The file system is in a misconfigured but recoverable state.                                                                                        |
| FAILED             | 1. The file system has failed and Amazon FSx can't recover it. 2. When creating new file system, Amazon FSx was unable to create a new file system. |
