

# Modifying throughput capacity
<a name="increase-throughput-capacity"></a>

You can modify an FSx for Lustre file system's throughput capacity using the Amazon FSx console, the AWS Command Line Interface (AWS CLI), or the Amazon FSx API.

## To modify an SSD file system's throughput capacity (console)
<a name="update-throughput-console"></a>

1. Open the Amazon FSx console at [https://console.aws.amazon.com/fsx/](https://console.aws.amazon.com/fsx/).

1. Navigate to **File systems**, and choose the FSx for Lustre file system that you want to modify the throughput capacity for.

1. For **Actions**, choose **Update throughput tier**. Or, in the **Summary** panel, choose **Update** next to the file system's **Throughput per unit of storage**.

   The **Update throughput tier** window appears.

1. Choose the new value for **Desired throughput per unit of storage** from the list.

1. Choose **Update** to initiate the throughput capacity update.
**Note**  
Your file system may experience a very brief period of unavailability during the update.

## To modify an SSD file system's throughput capacity (CLI)
<a name="update-throughput-cli"></a>
+ To modify a file system's throughput capacity, use the [update-file-system](https://docs.aws.amazon.com/cli/latest/reference/fsx/update-file-system.html) CLI command (or the equivalent [UpdateFileSystem](https://docs.aws.amazon.com/fsx/latest/APIReference/API_UpdateFileSystem.html) API operation). Set the following parameters:
  + Set `--file-system-id` to the ID of the file system that you are updating.
  + Set `--lustre-configuration PerUnitStorageThroughput` to a value of `50`, `100`, or `200` MBps/TiB for Persistent 1 SSD file systems, or to a value of `125`, `250`, `500`, or `1000` MBps/TiB for Persistent 2 SSD file systems.

  This command specifies that throughput capacity be set to 1000 MBps/TiB for the file system.

  ```
  aws fsx update-file-system \
      --file-system-id fs-0123456789abcdef0 \
      --lustre-configuration PerUnitStorageThroughput=1000
  ```

## To modify an Intelligent-Tiering file system's throughput capacity (console)
<a name="update-int-throughput-console"></a>

1. Open the Amazon FSx console at [https://console.aws.amazon.com/fsx/](https://console.aws.amazon.com/fsx/).

1. Navigate to **File systems**, and choose the FSx for Lustre file system that you want to modify the throughput capacity for.

1. For **Actions**, choose **Update throughput capacity**. Or, in the **Summary** panel, choose **Update** next to the file system's **Throughput capacity**.

   The **Update throughput capacity** dialog box appears.

1. Choose the new value for **Desired throughput capacity** from the list.

   Amazon FSx will automatically scale your data read cache to avoid clearing the cache contents.

1. Choose **Update** to initiate the throughput capacity update.
**Note**  
Your file system may experience a very brief period of unavailability during the update.

## To modify an Intelligent-Tiering file system's throughput capacity (CLI)
<a name="update-int-throughput-cli"></a>
+ To modify a file system's throughput capacity, use the [update-file-system](https://docs.aws.amazon.com/cli/latest/reference/fsx/update-file-system.html) CLI command (or the equivalent [UpdateFileSystem](https://docs.aws.amazon.com/fsx/latest/APIReference/API_UpdateFileSystem.html) API operation). Set the following parameters:
  + Set `--file-system-id` to the ID of the file system that you are updating.
  + If your data read cache is configured in proportional to throughput capacity mode, set `--lustre-configuration ThroughputCapacity` to a throughput level of increments of `4000` MBps, up to a maximum of `2000000` MBps.

    If your data read cache is configured in user-provisioned mode, you also need to use the `--lustre-configuration DataReadCacheConfiguration` property to specify the data read cache. You need to maintain the same cache storage per server ratio and specify the new SizeGiB, or the request will be rejected.

  This command specifies that throughput capacity be set to 8000 MBps for a file system that uses a read cache configured in proportional to throughput capacity mode.

  ```
  aws fsx update-file-system \
      --file-system-id fs-0123456789abcdef0 \
      --lustre-configuration '{
        "ThroughputCapacity": 8000
        }'
  ```

  This command specifies that throughput capacity be set to 8000 MBps for a file system that uses a read cache configured in user-provisioned mode.

  ```
  aws fsx update-file-system \
      --file-system-id fs-0123456789abcdef0 \
      --lustre-configuration { 
          "ThroughputCapacity": 8000, 
          "DataReadCacheConfiguration": '{ 
               "SizingMode":"USER_PROVISIONED"
               "SizeGiB":1000
               # New size should be cache storage allocated per server multiplied by number of file servers
           }
  }'
  ```