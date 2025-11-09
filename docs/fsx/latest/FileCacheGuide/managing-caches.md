# Managing caches

A cache is the primary Amazon File Cache resource. You can create, list,
update, and delete an Amazon File Cache using the AWS Management Console, AWS Command Line Interface (AWS CLI), and API.

## Creating caches

You can create an Amazon File Cache using the AWS Management Console, AWS CLI, or the AWS API.

###### Note

You can link your cache to data repositories only when you create the cache. You can link up
to 8 data repositories of the same type (all Amazon S3 or all NFS0.

- For information about how to create a cache from the console, see
  [Step 1: Create your cache](getting-started-step1.md "getting-started-step1.md").
- To create an Amazon File Cache, use the [create-file-cache](../../../cli/latest/reference/fsx/create-file-cache.md "../../../cli/latest/reference/fsx/create-file-cache.md") CLI command (or the equivalent [CreateFileCache](../APIReference/API_CreateFileCache.md "../APIReference/API_CreateFileCache.md") API operation). The following example
  creates an Amazon File Cache. Use the
  `--data-repository-associations` option to specify links
  to up to 8 data repositories. This example creates links to three
  Amazon S3 buckets.

```
fsx create-file-cache \
--storage-capacity 1200 \
--subnet-ids subnet-0156f2909ff21e78b \
--security-group-ids sg-0123456789abcdef3 \
--file-cache-type LUSTRE \
--file-cache-type-version 2.12 \
--lustre-configuration "DeploymentType=CACHE_1,PerUnitStorageThroughput=1000,MetadataConfiguration={StorageCapacity=2400}" \
--data-repository-associations FileCachePath=/ns2/,DataRepositoryPath=s3://s3cache2/fsx/ \
  FileCachePath=/ns3/,DataRepositoryPath=s3://s3cache3/fsx/ \
  FileCachePath=/ns4/,DataRepositoryPath=s3://s3cache4/fsx/
```

After successfully creating the cache, Amazon File Cache returns the cache
description in JSON format, as shown in the following example.

```
{
    "FileCache": {
        "OwnerId": "1234567890120",
        "CreationTime": 1661841150.136,
        "FileCacheId": "fc-0123456789abcdef0",
        "FileCacheType": "LUSTRE",
        "FileCacheTypeVersion": "2.12",
        "Lifecycle": "CREATING",
        "StorageCapacity": 1200,
        "VpcId": "vpc-0222d95ad3328a351",
        "SubnetIds": [
            "sg-0123456789abcdef3"
        ],
        "DNSName": "fc-0123456789abcdef0.fsx.us-east-1.amazonaws.com",
        "KmsKeyId": "arn:aws:kms:us-east-1:123456789012:key/71726ts-r4sd-98gs-9ist-35w7tbs",
        "ResourceARN": "arn:aws:fsx:us-east-1:123456789012:file-cache/fc-0123456789abcdef0",
        "Tags": [],
        "CopyTagsToDataRepositoryAssociations": false,
        "LustreConfiguration": {
            "PerUnitStorageThroughput": 1000,
            "DeploymentType": "CACHE_1",
            "MountName": "fmvszbmv",
            "WeeklyMaintenanceStartTime": "5:06:00",
            "MetadataConfiguration": {
                "StorageCapacity": 2400
            },
            "LogConfiguration": {
                "Level": "WARN_ERROR",
                "Destination": "arn:aws:logs:us-east-1:123456789012:log-group:/aws/fsx/filecache/lustre:log-stream:datarepo_fc-0123456789abcdef0"
            }
        },
        "DataRepositoryAssociationIds": [
            "dra-04d15aa012bdcf0f8",
            "dra-036182e206928928c",
            "dra-07a25a1250582261e"
        ]
    }
}
```

## Updating caches

You can update the **Weekly maintenance window**
configuration that sets the day of the week and time that Amazon File Cache performs
cache maintenance and updates. You can update the configuration of an Amazon File Cache
resource using the AWS Management Console, the AWS CLI, and the AWS API.

- For information about how to change the configuration of
  the weekly maintenance window, see
  [Amazon File Cache maintenance windows](maintenance-windows.md "maintenance-windows.md").
- To update the configuration of an Amazon File Cache, use the
  [update-file-cache](../../../cli/latest/reference/fsx/update-file-cache.md "../../../cli/latest/reference/fsx/update-file-cache.md") CLI command (or the equivalent
  [UpdateFileCache](../APIReference/API_UpdateFileCache.md "../APIReference/API_UpdateFileCache.md") API operation), as shown in the
  following example.

```
`aws fsx update-file-cache \
 --file-cache-id fc-0123456789abcdef0 \
 --lustre-configuration WeeklyMaintenanceStartTime=1:01:30`
```

## Deleting caches

You can delete an Amazon File Cache using the AWS Management Console, the AWS CLI, and
the AWS API and SDKs.

###### To delete a cache:

- **Using the console** – Follow the
  procedure described in [Step 4: Clean up resources](getting-started-step4.md "getting-started-step4.md").
- **Using the CLI or API** – Use the [delete-file-cache](../../../cli/latest/reference/fsx/delete-file-cache.md "../../../cli/latest/reference/fsx/delete-file-cache.md") CLI command or the [DeleteFileCache](../APIReference/API_DeleteFileCache.md "../APIReference/API_DeleteFileCache.md") API operation. The following example shows how to use
  the CLI to delete an Amazon File Cache resource.

```
aws fsx delete-file-cache --file-cache-id fc-0123456789abcdef0
```

## Viewing caches

You can view the details of your cache using the AWS Management Console,
the AWS CLI, and the AWS API and SDKs.

###### To view a cache:

- **Using the console** – Choose a cache
  to view the cache detail page. The **Summary** panel shows the
  cache ID, lifecycle state, cache type, deployment type, storage type, storage
  capacity, metadata storage capacity, throughput per unit of storage, total
  throughput, Lustre version, Availability Zones, creation time, and mount name.

The tabs provide detailed information about the cache's features, such as
your linked data repositories.

- **Using the CLI or API** – Use the
  [describe-file-caches](../../../cli/latest/reference/fsx/describe-file-caches.md "../../../cli/latest/reference/fsx/describe-file-caches.md") CLI command or the [DescribeFileCaches](../APIReference/API_DescribeFileCaches.md "../APIReference/API_DescribeFileCaches.md") API operation. The following example
  shows how to use the CLI to return the description of a specific Amazon File Cache.

```
aws fsx describe-file-caches \
    --file-cache-ids fc-0123456789abcdef0
```

To return descriptions of all existing caches, omit the
`--file-cache-ids` option.

## Amazon File Cache status

You can view the status of a cache by using the AWS Management Console, the AWS CLI command [describe-caches](../../../cli/latest/reference/fsx/describe-file-caches.md "../../../cli/latest/reference/fsx/describe-file-caches.md"), or the
[DescribeFileCaches](../APIReference/API_DescribeFileCaches.md "../APIReference/API_DescribeFileCaches.md") API operation.

| Cache status | Description                                                                                                                          |
| ------------ | ------------------------------------------------------------------------------------------------------------------------------------ |
| AVAILABLE    | The cache has been successfully created and is available for use.                                                                    |
| CREATING     | A new cache is being created.                                                                                                        |
| DELETING     | An existing cache is being deleted.                                                                                                  |
| UPDATING     | The cache is undergoing a customer-initiated update.                                                                                 |
| FAILED       | This status can mean either of the following:<br>• The cache has failed and cannot be recovered.<br>• The cache couldn't be created. |
