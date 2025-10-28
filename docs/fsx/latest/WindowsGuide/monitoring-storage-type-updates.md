# Monitoring storage type updates

After you update your file system's storage type from HDD to SSD storage, you can monitor the progress of the storage
type update using the Amazon FSx console, the AWS CLI, or the API, as described in the following procedures.

On the **Updates** tab in the **File system
details** window, you can view the 10 most recent updates for each
update type.

For storage type updates, you can view the following information.

\***\*Update type\*\***

Possible value is **Storage type**.

\***\*Target value\*\***

**SSD**

\***\*Status\*\***

The current status of the update. For storage type updates, the possible values are as follows:

- **Pending** – Amazon FSx received the update request, but has not started
  processing it.
- **In progress** – Amazon FSx is processing the update request.
- **Updated optimizing** – The SSD storage performance is available for
  write operations. The update enters an
  **Updated optimizing** state, which
  typically lasts a few hours, during which
  read operations will have performance levels between HDD and
  SSD. Once your update action is complete, your new SSD
  performance is available for both reads and writes.
- **Completed** – The storage type update completed
  successfully.
- **Failed** – The storage type update failed. Choose the question mark
  (**?**) to see details.

\***\*Progress %\*\***

Displays the progress of the storage optimization process by
the percentage that's complete.

\***\*Request time\*\***

The time that Amazon FSx received the update action request.

You can view and monitor file system storage type update requests using the [describe-file-systems](../../../cli/latest/reference/fsx/describe-file-systems.md "../../../cli/latest/reference/fsx/describe-file-systems.md") AWS CLI command and the [DescribeFileSystems](../APIReference/API_DescribeFileSystems.md "../APIReference/API_DescribeFileSystems.md") API action. The `AdministrativeActions`
array lists the 10 most recent update actions for each administrative action type. When you increase a file system's SSD IOPS, two
`AdministrativeActions` are generated: a
`FILE_SYSTEM_UPDATE` and a `STORAGE_TYPE_OPTIMIZATION` action.
