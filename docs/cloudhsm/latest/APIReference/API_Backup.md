# Backup

Contains information about a backup of an AWS CloudHSM cluster. All backup objects
 contain the `BackupId`, `BackupState`, `ClusterId`, and
 `CreateTimestamp` parameters. Backups that were copied into a destination region
 additionally contain the `CopyTimestamp`, `SourceBackup`,
 `SourceCluster`, and `SourceRegion` parameters. A backup that is
 pending deletion will include the `DeleteTimestamp` parameter.


## Contents





**BackupId** 


The identifier (ID) of the backup.


Type: String


Pattern: `backup-[2-7a-zA-Z]{11,16}`



Required: Yes




**BackupArn** 


The Amazon Resource Name (ARN) of the backup.


Type: String


Pattern: `^(arn:aws(-(us-gov))?:cloudhsm:([a-z]{2}(-(gov|isob|iso))?-(east|west|north|south|central){1,2}-[0-9]{1}):[0-9]{12}:backup/)?backup-[2-7a-zA-Z]{11,16}`



Required: No




**BackupState** 


The state of the backup.


Type: String


Valid Values: `CREATE_IN_PROGRESS | READY | DELETED | PENDING_DELETION`



Required: No




**ClusterId** 


The identifier (ID) of the cluster that was backed up.


Type: String


Pattern: `cluster-[2-7a-zA-Z]{11,16}`



Required: No




**CopyTimestamp** 


The date and time when the backup was copied from a source backup.


Type: Timestamp


Required: No




**CreateTimestamp** 


The date and time when the backup was created.


Type: Timestamp


Required: No




**DeleteTimestamp** 


The date and time when the backup will be permanently deleted.


Type: Timestamp


Required: No




**HsmType** 


The HSM type used to create the backup.


Type: String


Length Constraints: Maximum length of 32.


Pattern: `((p|)hsm[0-9][a-z.]*\.[a-zA-Z]+)`



Required: No




**Mode** 


The mode of the cluster that was backed up.


Type: String


Valid Values: `FIPS | NON_FIPS`



Required: No




**NeverExpires** 


Specifies whether the service should exempt a backup from the retention policy for the cluster. `True` exempts 
 a backup from the retention policy. `False` means the service applies the backup retention policy defined at the cluster.


Type: Boolean


Required: No




**SourceBackup** 


The identifier (ID) of the source backup from which the new backup was
 copied.


Type: String


Pattern: `backup-[2-7a-zA-Z]{11,16}`



Required: No




**SourceCluster** 


The identifier (ID) of the cluster containing the source backup from which the new
 backup was copied.


Type: String


Pattern: `cluster-[2-7a-zA-Z]{11,16}`



Required: No




**SourceRegion** 


The AWS Region that contains the source backup from which the new backup was
 copied.


Type: String


Pattern: `[a-z]{2}(-(gov))?-(east|west|north|south|central){1,2}-\d`



Required: No




**TagList** 


The list of tags for the backup.


Type: Array of [Tag](API_Tag.md "API_Tag.md") objects


Array Members: Minimum number of 1 item. Maximum number of 50 items.


Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/cloudhsmv2-2017-04-28/Backup "https://docs.aws.amazon.com/goto/SdkForCpp/cloudhsmv2-2017-04-28/Backup")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudhsmv2-2017-04-28/Backup "https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudhsmv2-2017-04-28/Backup")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudhsmv2-2017-04-28/Backup "https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudhsmv2-2017-04-28/Backup")
