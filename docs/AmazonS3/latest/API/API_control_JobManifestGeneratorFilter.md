# JobManifestGeneratorFilter

The filter used to describe a set of objects for the job's manifest.


## Contents





**CreatedAfter** 


If provided, the generated manifest includes only source bucket objects that were
 created after this time.


Type: Timestamp


Required: No




**CreatedBefore** 


If provided, the generated manifest includes only source bucket objects that were
 created before this time.


Type: Timestamp


Required: No




**EligibleForReplication** 


Include objects in the generated manifest only if they are eligible for replication
 according to the Replication configuration on the source bucket.


Type: Boolean


Required: No




**KeyNameConstraint** 


If provided, the generated manifest includes only source bucket objects whose object
 keys match the string constraints specified for `MatchAnyPrefix`,
 `MatchAnySuffix`, and `MatchAnySubstring`.


Type: [KeyNameConstraint](API_control_KeyNameConstraint.md "API_control_KeyNameConstraint.md") data type


Required: No




**MatchAnyObjectEncryption** 


If provided, the generated object list includes 
 only source bucket objects with the indicated server-side encryption type (SSE-S3, SSE-KMS, DSSE-KMS, SSE-C, or NOT-SSE). 
 If you select SSE-KMS or DSSE-KMS, you can optionally further filter your results by specifying a specific KMS Key ARN. 
 If you select SSE-KMS, you can also optionally further filter your results by Bucket Key enabled status.


Type: Array of [ObjectEncryptionFilter](API_control_ObjectEncryptionFilter.md "API_control_ObjectEncryptionFilter.md") data types


Array Members: Fixed number of 1 item.


Required: No




**MatchAnyStorageClass** 


If provided, the generated manifest includes only source bucket objects that are stored
 with the specified storage class.


Type: Array of strings


Valid Values: `STANDARD | STANDARD_IA | ONEZONE_IA | GLACIER | INTELLIGENT_TIERING | DEEP_ARCHIVE | GLACIER_IR`



Required: No




**ObjectReplicationStatuses** 


If provided, the generated manifest includes only source bucket objects that have one of
 the specified Replication statuses.


Type: Array of strings


Valid Values: `COMPLETED | FAILED | REPLICA | NONE`



Required: No




**ObjectSizeGreaterThanBytes** 


If provided, the generated manifest includes only source bucket objects whose file size
 is greater than the specified number of bytes.


Type: Long


Required: No




**ObjectSizeLessThanBytes** 


If provided, the generated manifest includes only source bucket objects whose file size
 is less than the specified number of bytes.


Type: Long


Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/JobManifestGeneratorFilter "https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/JobManifestGeneratorFilter")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/JobManifestGeneratorFilter "https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/JobManifestGeneratorFilter")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/JobManifestGeneratorFilter "https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/JobManifestGeneratorFilter")
