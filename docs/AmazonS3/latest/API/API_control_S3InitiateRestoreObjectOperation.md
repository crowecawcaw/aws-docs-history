# S3InitiateRestoreObjectOperation

Contains the configuration parameters for
 a
 POST Object restore job. S3 Batch Operations passes every object to the
 underlying
 `RestoreObject`
 API
 operation. For more information about the parameters for this operation,
 see [RestoreObject](RESTObjectPOSTrestore.md#RESTObjectPOSTrestore-restore-request "RESTObjectPOSTrestore.md#RESTObjectPOSTrestore-restore-request").


## Contents





**ExpirationInDays** 


This argument specifies how long the S3 Glacier or S3 Glacier Deep Archive object remains
 available in Amazon S3. S3 Initiate Restore Object jobs that target S3 Glacier and S3 Glacier Deep Archive
 objects require `ExpirationInDays` set to 1 or greater.


Conversely, do *not* set `ExpirationInDays` when creating
 S3 Initiate Restore Object jobs that target S3 Intelligent-Tiering Archive Access and
 Deep Archive Access tier objects. Objects in S3 Intelligent-Tiering archive access tiers are
 not subject to restore expiry, so specifying `ExpirationInDays` results in
 restore request failure.


S3 Batch Operations jobs can operate either on S3 Glacier and S3 Glacier Deep Archive storage class
 objects or on S3 Intelligent-Tiering Archive Access and Deep Archive Access storage tier
 objects, but not both types in the same job. If you need to restore objects of both types
 you *must* create separate Batch Operations jobs. 


Type: Integer


Valid Range: Minimum value of 1.


Required: No




**GlacierJobTier** 


S3 Batch Operations supports `STANDARD` and `BULK` retrieval tiers, but
 not the `EXPEDITED` retrieval tier.


Type: String


Valid Values: `BULK | STANDARD`



Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/S3InitiateRestoreObjectOperation "https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/S3InitiateRestoreObjectOperation")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/S3InitiateRestoreObjectOperation "https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/S3InitiateRestoreObjectOperation")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/S3InitiateRestoreObjectOperation "https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/S3InitiateRestoreObjectOperation")
