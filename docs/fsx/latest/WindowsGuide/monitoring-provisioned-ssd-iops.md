# Monitoring provisioned SSD IOPS updates

After you update the amount of provisioned SSD IOPS for your file system, you can monitor the progress of the SSD IOPS update
using the Amazon FSx console, the AWS CLI, and the API, as described in the following procedures.

## Monitoring updates in the console

In the **Updates** tab in the **File system details**
window, you can view the 10 most recent updates for each update type.

For provisioned SSD IOPS updates, you can view the following information.

\***\*Update type\*\***

Possible values are **IOPS Mode** and **SSD IOPS**.

\***\*Target value\*\***

The desired value to update the file system's IOPS mode and SSD IOPS to.

\***\*Status\*\***

The current status of the update. For SSD IOPS updates, the possible values are as follows:

- **Pending** – Amazon FSx has received the update request, but has not
  started processing it.
- **In progress** – Amazon FSx is processing the update request.
- **Updated optimizing** – The new IOPS level is available for your
  workload's write operations. Your update enters an
  **Updated optimizing** state, which
  typically lasts a few hours, during which your workload's read
  operations have IOPS performance between the previous level and
  the new level. After your update action is complete, your new
  IOPS level is available for both reads and writes.
- **Completed** – The SSD IOPS update completed
  successfully.
- **Failed** – The SSD IOPS update failed. Choose the question
  mark (**?**) to see details on why the storage
  update failed.

\***\*Progress %\*\***

Displays the progress of the storage optimization process as percent complete.

\***\*Request time\*\***

The time that Amazon FSx received the update action request.

## Monitoring updates with the AWS CLI and

API

You can view and monitor file system SSD IOPS update requests using the [describe-file-systems](../../../cli/latest/reference/fsx/describe-file-systems.md "../../../cli/latest/reference/fsx/describe-file-systems.md") AWS CLI command and the [DescribeFileSystems](../APIReference/API_DescribeFileSystems.md "../APIReference/API_DescribeFileSystems.md") API action. The `AdministrativeActions`
array lists the 10 most recent update actions for each administrative action type.
When you increase a file system's SSD IOPS, two
`AdministrativeActions` are generated: a
`FILE_SYSTEM_UPDATE` and an `IOPS_OPTIMIZATION` action.
