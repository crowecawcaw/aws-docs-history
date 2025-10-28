# Viewing storage class size

You can view how much data is stored in each storage class of your file system using
the Amazon EFS console, the AWS CLI, or the EFS API.

The **Metered size** tab on the **File system
details** page displays the current metered size of the file system in
binary multiples of bytes (kibibytes, mebibytes, gibibytes, and tebibytes). The metric
is emitted every 15 minutes and lets you view your file system's metered size
over time. **Metered size** displays the following information for
the file system storage size:

- **Total size** is the size (in binary bytes) of data stored
  in the file system, including all storage classes.
- **Size in Standard** is the size (in binary bytes) of
  data stored in the EFS Standard storage class.
- **Size in IA** is the size (in binary bytes) of data
  stored in the EFS Infrequent Access storage class. Files smaller than 128KiB are rounded
  up to 128KiB.
- **Size in Archive** is the size (in binary bytes) of
  data stored in the EFS Archive storage class. Files smaller than 128KiB are
  rounded up to 128KiB.
  You can also view the `Storage bytes` metric on the
  **Monitoring** tab on the **File system details**
  page in the Amazon EFS console. For more information, see [Accessing CloudWatch metrics for Amazon EFS](accessingmetrics.md "accessingmetrics.md").

You can view how much data is stored in each storage class of your file system
using the AWS CLI or EFS API. View data storage details by calling the
`describe-file-systems` CLI command (the corresponding API
operation is [DescribeFileSystems](API_DescribeFileSystems.md "API_DescribeFileSystems.md")).

```
`$` `aws efs describe-file-systems \
--region us-west-2 \
--profile adminuser`
```

In the response, `ValueInIA` displays the last metered size in bytes in
the file system's Infrequent Access storage class. `ValueInStandard` displays
the last metered size in bytes in the Standard storage class.
`ValueInArchive` displays the last metered size in bytes in the
Archive storage class. The sum of the three values equals the size of the
entire file system, which is displayed in `Value`.

```
{
   "FileSystems":[
      {
         "OwnerId":"251839141158",
         "CreationToken":"MyFileSystem1",
         "FileSystemId":"fs-47a2c22e",
         "PerformanceMode" : "generalPurpose",
         "CreationTime": 1403301078,
         "LifeCycleState":"created",
         "NumberOfMountTargets":1,
         "SizeInBytes":{
            "Value": 29313746702,
            "ValueInIA": 675432,
            "ValueInStandard": 29312741784,
            "ValueInArchive":329486
        },
        "ThroughputMode": "elastic"
      }
   ]
}

```

For additional ways to view and measure disk usage, see [Metering EFS file system
objects](metered-sizes.md#metered-sizes-fs-objects "metered-sizes.md#metered-sizes-fs-objects").
