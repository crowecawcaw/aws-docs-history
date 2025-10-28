# Updating a file system's SSD IOPS

For file systems configured with SSD storage, the level of provisioned SSD IOPS determines the amount of disk I/O
available when your file system has to read data from and write data to disk, as opposed to reading or writing data that is in cache.
You can update SSD IOPS for a file system using the Amazon FSx console, the AWS CLI,
or the Amazon FSx API, as described in the following procedures. For more information about managing SSD IOPS, see
[Managing SSD IOPS](managing-storage-configuration.md#managing-provisioned-ssd-iops "managing-storage-configuration.md#managing-provisioned-ssd-iops").

1. Open the Amazon FSx console at [https://console.aws.amazon.com/fsx/](https://console.aws.amazon.com/fsx/ "https://console.aws.amazon.com/fsx/").
2. Navigate to **File systems** and choose the Windows file system that you want to update SSD IOPS for.
3. Under **Actions**, choose **Update SSD IOPS**. Or, in the
   **Summary** panel, select the
   **Update** button next to **Provisioned SSD
   IOPS**. The **Update IOPS provisioning** window opens.
4. For **Mode**, choose **Automatic** or
   **User-provisioned**. If you choose
   **Automatic**, Amazon FSx automatically provisions 3 SSD
   IOPS per GiB of storage capacity for your file system. If you choose
   **User-provisioned**, enter any whole number in the
   range of 96–400,000.
5. Choose **Update** to initiate the provisioned SSD IOPS update.
6. You can monitor the update progress on the **File systems** detail page, on
   the **Updates** tab.
   To update SSD IOPS for an FSx for Windows File Server file system, use the `--windows-configuration
 DiskIopsConfiguration` property. This property has two
   parameters, `Iops` and `Mode`:

- If you want to specify the number of SSD IOPS, use
  `Iops=`number_of_IOPS``, up
to a maximum of 400,000 in supported AWS Regions and
`Mode=USER_PROVISIONED`.
- If you want Amazon FSx to increase your SSD IOPS automatically, use `Mode=AUTOMATIC` and
  don't use the `Iops` parameter. Amazon FSx automatically maintains
  3 SSD IOPS per GiB of storage capacity on your file system, up to a
  maximum of 400,000 in supported AWS Regions.
  You can monitor the progress of the update by using the AWS CLI command [describe-file-systems](../../../cli/latest/reference/fsx/describe-file-systems.md "../../../cli/latest/reference/fsx/describe-file-systems.md"). Look for the
  `administrative-actions` in the output.

For more information, see [AdministrativeAction](../APIReference/API_AdministrativeAction.md "../APIReference/API_AdministrativeAction.md").
