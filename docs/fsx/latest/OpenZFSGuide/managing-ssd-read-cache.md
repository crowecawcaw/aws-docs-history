# Modifying provisioned SSD read cache

When you create a file system with the Intelligent-Tiering storage class, you have the option to also provision an SSD read cache that provides
SSD latencies for reads of frequently accessed data, up to 3 IOPS per GiB. The SSD read cache has three sizing modes: Automatic, Custom, and None.
After your file system is created, you can modify your SSD read cache's sizing mode at any time.

###### Topics

- [Considerations when updating SSD read cache sizing mode](#considerations-update-ssd-read-cache "#considerations-update-ssd-read-cache")
- [Updating the provisioned SSD read cache](#how-to-update-ssd-read-cache "#how-to-update-ssd-read-cache")
- [Monitoring SSD read cache updates](#monitoring-ssd-read-cache-update "#monitoring-ssd-read-cache-update")

## Considerations when updating SSD read cache sizing mode

Here are a few important considerations when modifying your SSD read cache:

- Any time you modify the SSD read cache, all of its contents will be erased.
  This means that you may see a decrease in performance levels until the SSD read cache is populated again.
- You can both increase and decrease the size of the SSD read cache. However, you can only do this once every six hours. There is no time restriction when adding or removing the SSD read cache from your file system.
- You must increase or decrease the size of your SSD read cache by a minimum of 10% every time you modify it.

## Updating the provisioned SSD read cache

You can update your SSD read cache using the Amazon FSx console, the AWS CLI, or the Amazon FSx API.

1. Open the Amazon FSx console at [https://console.aws.amazon.com/fsx/](https://console.aws.amazon.com/fsx/ "https://console.aws.amazon.com/fsx/").
2. In the left navigation pane, choose **File systems**. In the **File
   systems** list, choose the FSx for OpenZFS file system that you
   want to update the SSD read cache for.
3. On the **Summary** panel, choose **Update** next to the file system's
   **SSD read cache configuration** value.

The **Update SSD read cache** panel appears. 4. Select the new sizing mode that you would like for your SSD read cache, as follows:

    * Choose **Automatic (Proportional to throughput capacity)** to have your SSD read cache automatically sized based on your throughput capacity.
    * Choose **Custom (User-provisioned)** if you know the approximate size of your dataset and would like to customize your SSD read cache. If you select Custom, you will also need to specify the **Desired read cache capacity** in GiB.
    * Choose **None** if you do not want to use an SSD read cache with your Intelligent-Tiering file system.

5. Choose **Update**.
   To update the SSD read cache for an Intelligent-Tiering file system,
   use the AWS CLI command [update-file-system](../../../cli/latest/reference/fsx/update-file-system.md "../../../cli/latest/reference/fsx/update-file-system.md") or the equivalent UpdateFileSystem API action. Set the following parameters:

- Set `--file-system-id` to the ID of the file system that you are updating.
- To modify your SSD read cache, use the `--open-zfs-configuration
 ReadCacheConfiguration` property. This property has two
  parameters, `SizeGiB` and `SizingMode`:

      + **SizeGiB** ‐ Sets the size of your SSD read cache in GiB when using `USER_PROVISIONED` mode.
      + **SizingMode** ‐ Sets the sizing mode of your SSD read cache.




      	- Set to `NO_CACHE` if you do not want to use an SSD read cache with your Intelligent-Tiering file system.
      	- Set to `USER_PROVISIONED` to specify the exact size of your SSD read cache.
      	- Set to `PROPORTIONAL_TO_THROUGHPUT_CAPACITY` to have your SSD read cache automatically sized based on your throughput capacity.

  The following example updates the SSD read cache sizing mode to **USER_PROVISIONED** and sets the size to 524288 GiB.

```
`aws fsx update-file-system \
 --open-zfs-configuration 'ReadCacheConfiguration={SizeGiB=`524288`,SizingMode=`USER_PROVISIONED`}'`
```

To monitor the progress of the update, use the [describe-file-systems](../../../cli/latest/reference/fsx/describe-file-systems.md "../../../cli/latest/reference/fsx/describe-file-systems.md") AWS CLI command. Look for the `AdministrativeActions` section in the output.

For more information, see [AdministrativeAction](../APIReference/API_AdministrativeAction.md "../APIReference/API_AdministrativeAction.md") in the _Amazon FSx for OpenZFS API Reference_.

## Monitoring SSD read cache updates

You can monitor the progress of an SSD read cache update by using the Amazon FSx
console, the API, or the AWS CLI.

### Monitoring updates in the console

You can monitor file system updates in the **Updates** tab on the **File system details** page.

For SSD read cache updates, you can view the following information:

\***\*Update type\*\***

Supported types are **SSD read cache sizing mode** and **SSD read cache size**.

\***\*Target value\*\***

The updated value for the file system's SSD read cache sizing mode or SSD read cache size.

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

### Monitoring SSD read cache updates with the AWS CLI and API

You can view and monitor file system SSD read cache update requests using the
[describe-file-systems](../../../cli/latest/reference/fsx/describe-file-systems.md "../../../cli/latest/reference/fsx/describe-file-systems.md") AWS CLI command and the
[DescribeFileSystems](../APIReference/API_DescribeFileSystems.md "../APIReference/API_DescribeFileSystems.md") API operation. The `AdministrativeActions` array
lists the 10 most recent update actions for each administrative action type. When you
update a file system's SSD read cache, a `FILE_SYSTEM_UPDATE`
`AdministrativeActions` is generated.

The following example shows an excerpt of the response of a `describe-file-systems`
CLI command. The file system has a pending administrative action to change the SSD read cache sizing mode to `USER_PROVISIONED` and
the SSD read cache size to 524288.

```
"AdministrativeActions": [
    {
        "AdministrativeActionType": "FILE_SYSTEM_UPDATE",
        "RequestTime": 1586797629.095,
        "Status": "PENDING",
        "TargetFileSystemValues": {
            "OpenZFSConfiguration": {
                "ReadCacheConfiguration": {
                     "SizingMode": "USER_PROVISIONED"
                     "SizeGiB": 524288,
                }
            }
        }
    }
]
```

When the new SSD read cache configuration is available to the file system, the
`FILE_SYSTEM_UPDATE` status changes to `COMPLETED`. If the SSD read cache update request fails, the status of the
`FILE_SYSTEM_UPDATE` action changes to `FAILED`.
