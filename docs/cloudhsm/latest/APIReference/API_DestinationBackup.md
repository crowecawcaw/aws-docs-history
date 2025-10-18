# DestinationBackup

Contains information about the backup that will be copied and created by the [CopyBackupToRegion](API_CopyBackupToRegion.md "API_CopyBackupToRegion.md") operation.


## Contents





**CreateTimestamp** 


The date and time when both the source backup was created.


Type: Timestamp


Required: No




**SourceBackup** 


The identifier (ID) of the source backup from which the new backup was copied.


Type: String


Pattern: `backup-[2-7a-zA-Z]{11,16}`



Required: No




**SourceCluster** 


The identifier (ID) of the cluster containing the source backup from which the new backup was copied.


Type: String


Pattern: `cluster-[2-7a-zA-Z]{11,16}`



Required: No




**SourceRegion** 


The AWS region that contains the source backup from which the new backup was copied.


Type: String


Pattern: `[a-z]{2}(-(gov))?-(east|west|north|south|central){1,2}-\d`



Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/cloudhsmv2-2017-04-28/DestinationBackup "https://docs.aws.amazon.com/goto/SdkForCpp/cloudhsmv2-2017-04-28/DestinationBackup")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudhsmv2-2017-04-28/DestinationBackup "https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudhsmv2-2017-04-28/DestinationBackup")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudhsmv2-2017-04-28/DestinationBackup "https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudhsmv2-2017-04-28/DestinationBackup")
