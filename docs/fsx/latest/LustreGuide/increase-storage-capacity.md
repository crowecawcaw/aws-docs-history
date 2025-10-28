# Increasing storage capacity

You can increase a file system's storage capacity using the Amazon FSx console, the AWS CLI,
or the Amazon FSx API.

###### To increase storage capacity for a file system (console)

1. Open the Amazon FSx console at [https://console.aws.amazon.com/fsx/](https://console.aws.amazon.com/fsx/ "https://console.aws.amazon.com/fsx/").
2. Navigate to **File systems**, and choose the Lustre file system
   that you want to increase storage capacity for.
3. For **Actions**, choose **Update storage capacity**.
   Or, in the **Summary** panel, choose **Update** next to the file
   system's **Storage capacity** to display the **Increase storage capacity**
   dialog box.
4. For **Desired storage capacity**, provide a new storage capacity
   in GiB that is greater than the current storage capacity of the file system:
   - For a persistent SSD or scratch 2 file system, this value must be
     in multiples of 2400 GiB.
   - For a persistent HDD file system, this value must be in multiples
     of 6000 GiB for 12 MBps/TiB file systems and multiples of 1800 GiB for 40 MBps/TiB
     file systems.
   - For an EFA-enabled file system, this value must be in
     multiples of 38400 GiB for 125 MBps/TiB file systems, multiples of 19200 GiB for
     250 MBps/TiB file systems, multiples of 9600 GiB for 500 MBps/TiB file systems,
     and multiples of 4800 GiB for 1000 MBps/TiB file systems.

###### Note

You cannot increase the storage capacity of scratch 1 file systems. 5. Choose **Update** to initiate the storage capacity update. 6. You can monitor the update progress on the file systems detail page in
the **Updates** tab.

###### To increase storage capacity for a file system (CLI)

1. To increase the storage capacity for an FSx for Lustre file system, use the AWS CLI command
   [update-file-system](../../../cli/latest/reference/fsx/update-file-system.md "../../../cli/latest/reference/fsx/update-file-system.md").
   Set the following parameters:

Set `--file-system-id` to the ID of the file system you are updating.

Set `--storage-capacity` to an integer value that is the amount, in GiB, of the
storage capacity increase. For a persistent SSD or scratch 2 file system,
this value must be in multiples of 2400. For a persistent HDD file system,
this value must be in multiples of 6000 for 12 MBps/TiB file systems and
multiples of 1800 for 40 MBps/TiB file systems. The new target value
must be greater than the current storage capacity of the file system.

This command specifies a storage capacity target value of 9600 GiB for a persistent SSD or scratch 2
file system.

```
$ aws fsx update-file-system \
    --file-system-id fs-0123456789abcdef0 \
    --storage-capacity 9600

```

2. You can monitor the progress of the update by using the AWS CLI command [describe-file-systems](../../../cli/latest/reference/fsx/describe-file-systems.md "../../../cli/latest/reference/fsx/describe-file-systems.md"). Look for
   the `administrative-actions` in the output.

For more information, see [AdministrativeAction](../APIReference/API_AdministrativeAction.md "../APIReference/API_AdministrativeAction.md").
