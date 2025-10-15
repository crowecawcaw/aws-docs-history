# PartitionedPrefix

Amazon S3 keys for log objects are partitioned in the following format:


`[DestinationPrefix][SourceAccountId]/[SourceRegion]/[SourceBucket]/[YYYY]/[MM]/[DD]/[YYYY]-[MM]-[DD]-[hh]-[mm]-[ss]-[UniqueString]`


PartitionedPrefix defaults to EventTime delivery when server access logs are delivered.


## Contents





**PartitionDateSource** 


Specifies the partition date source for the partitioned prefix. `PartitionDateSource` can
 be `EventTime` or `DeliveryTime`.


For `DeliveryTime`, the time in the log file names corresponds to the delivery time for
 the log files. 


 For `EventTime`, The logs delivered are for a specific day only. The year, month, and
 day correspond to the day on which the event occurred, and the hour, minutes and seconds are set to 00
 in the key.


Type: String


Valid Values: `EventTime | DeliveryTime`



Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/PartitionedPrefix "https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/PartitionedPrefix")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/PartitionedPrefix "https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/PartitionedPrefix")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/PartitionedPrefix "https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/PartitionedPrefix")
