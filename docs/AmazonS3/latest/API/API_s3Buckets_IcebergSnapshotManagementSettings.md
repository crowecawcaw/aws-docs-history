# IcebergSnapshotManagementSettings

Contains details about the snapshot management settings for an Iceberg table. The oldest snapshot expires when its age exceeds the `maxSnapshotAgeHours` and the total number of snapshots exceeds the value for the minimum number of snapshots to keep `minSnapshotsToKeep`.


## Contents





**maxSnapshotAgeHours** 


The maximum age of a snapshot before it can be expired.


Type: Integer


Valid Range: Minimum value of 1. Maximum value of 2147483647.


Required: No




**minSnapshotsToKeep** 


The minimum number of snapshots to keep.


Type: Integer


Valid Range: Minimum value of 1. Maximum value of 2147483647.


Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/s3tables-2018-05-10/IcebergSnapshotManagementSettings "https://docs.aws.amazon.com/goto/SdkForCpp/s3tables-2018-05-10/IcebergSnapshotManagementSettings")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3tables-2018-05-10/IcebergSnapshotManagementSettings "https://docs.aws.amazon.com/goto/SdkForJavaV2/s3tables-2018-05-10/IcebergSnapshotManagementSettings")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3tables-2018-05-10/IcebergSnapshotManagementSettings "https://docs.aws.amazon.com/goto/SdkForRubyV3/s3tables-2018-05-10/IcebergSnapshotManagementSettings")
