# JobOperation

The operation that you want this job to perform on every object listed in the manifest.
 For more information about the available operations, see [Operations](https://docs.aws.amazon.com/AmazonS3/latest/dev/batch-ops-operations.html "https://docs.aws.amazon.com/AmazonS3/latest/dev/batch-ops-operations.html") in the
 *Amazon S3 User Guide*.


## Contents





**LambdaInvoke** 


Directs the specified job to invoke an AWS Lambda function on every object in the
 manifest.


Type: [LambdaInvokeOperation](API_control_LambdaInvokeOperation.md "API_control_LambdaInvokeOperation.md") data type


Required: No




**S3ComputeObjectChecksum** 


Directs the specified job to compute checksum values for every object in the
 manifest.


Type: [S3ComputeObjectChecksumOperation](API_control_S3ComputeObjectChecksumOperation.md "API_control_S3ComputeObjectChecksumOperation.md") data type


Required: No




**S3DeleteObjectTagging** 


Directs the specified job to execute a DELETE Object tagging call on every object in the
 manifest.


###### Note

This functionality is not supported by directory buckets.


Type: [S3DeleteObjectTaggingOperation](API_control_S3DeleteObjectTaggingOperation.md "API_control_S3DeleteObjectTaggingOperation.md") data type


Required: No




**S3InitiateRestoreObject** 


Directs the specified job to initiate restore requests for every archived object in the
 manifest.


###### Note

This functionality is not supported by directory buckets.


Type: [S3InitiateRestoreObjectOperation](API_control_S3InitiateRestoreObjectOperation.md "API_control_S3InitiateRestoreObjectOperation.md") data type


Required: No




**S3PutObjectAcl** 


Directs the specified job to run a `PutObjectAcl` call on every object in the
 manifest.


###### Note

This functionality is not supported by directory buckets.


Type: [S3SetObjectAclOperation](API_control_S3SetObjectAclOperation.md "API_control_S3SetObjectAclOperation.md") data type


Required: No




**S3PutObjectCopy** 


Directs the specified job to run a PUT Copy object call on every object in the
 manifest.


Type: [S3CopyObjectOperation](API_control_S3CopyObjectOperation.md "API_control_S3CopyObjectOperation.md") data type


Required: No




**S3PutObjectLegalHold** 


Contains the configuration for an S3 Object Lock legal hold operation that an
 S3 Batch Operations job passes
 to
 every object to the underlying
 `PutObjectLegalHold`
 API
 operation. For more information, see [Using S3 Object Lock legal hold
 with S3 Batch Operations](https://docs.aws.amazon.com/AmazonS3/latest/dev/batch-ops-legal-hold.html "https://docs.aws.amazon.com/AmazonS3/latest/dev/batch-ops-legal-hold.html") in the *Amazon S3 User Guide*.


###### Note

This functionality is not supported by directory buckets.


Type: [S3SetObjectLegalHoldOperation](API_control_S3SetObjectLegalHoldOperation.md "API_control_S3SetObjectLegalHoldOperation.md") data type


Required: No




**S3PutObjectRetention** 


Contains the configuration parameters for the Object Lock retention action for an
 S3 Batch Operations job. Batch Operations passes every object to the underlying
 `PutObjectRetention`
 API
 operation. For more information, see [Using S3 Object Lock retention
 with S3 Batch Operations](https://docs.aws.amazon.com/AmazonS3/latest/dev/batch-ops-retention-date.html "https://docs.aws.amazon.com/AmazonS3/latest/dev/batch-ops-retention-date.html") in the *Amazon S3 User Guide*.


###### Note

This functionality is not supported by directory buckets.


Type: [S3SetObjectRetentionOperation](API_control_S3SetObjectRetentionOperation.md "API_control_S3SetObjectRetentionOperation.md") data type


Required: No




**S3PutObjectTagging** 


Directs the specified job to run a PUT Object tagging call on every object in the
 manifest.


###### Note

This functionality is not supported by directory buckets.


Type: [S3SetObjectTaggingOperation](API_control_S3SetObjectTaggingOperation.md "API_control_S3SetObjectTaggingOperation.md") data type


Required: No




**S3ReplicateObject** 


Directs the specified job to invoke `ReplicateObject` on every object in the
 job's manifest.


###### Note

This functionality is not supported by directory buckets.


Type: [S3ReplicateObjectOperation](API_control_S3ReplicateObjectOperation.md "API_control_S3ReplicateObjectOperation.md") data type


Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/JobOperation "https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/JobOperation")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/JobOperation "https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/JobOperation")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/JobOperation "https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/JobOperation")
