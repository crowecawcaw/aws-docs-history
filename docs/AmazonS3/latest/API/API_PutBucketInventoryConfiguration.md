# PutBucketInventoryConfiguration

###### Note

This operation is not supported for directory buckets.

This implementation of the `PUT` action adds an S3 Inventory configuration (identified by
 the inventory ID) to the bucket. You can have up to 1,000 inventory configurations per bucket. 

Amazon S3 inventory generates inventories of the objects in the bucket on a daily or weekly basis, and
 the results are published to a flat file. The bucket that is inventoried is called the
 *source* bucket, and the bucket where the inventory flat file is stored is called
 the *destination* bucket. The *destination* bucket must be in the
 same AWS Region as the *source* bucket. 

When you configure an inventory for a *source* bucket, you specify the
 *destination* bucket where you want the inventory to be stored, and whether to
 generate the inventory daily or weekly. You can also configure what object metadata to include and
 whether to inventory all object versions or only current versions. For more information, see [Amazon S3 Inventory](https://docs.aws.amazon.com/AmazonS3/latest/dev/storage-inventory.html "https://docs.aws.amazon.com/AmazonS3/latest/dev/storage-inventory.html") in the
 Amazon S3 User Guide.

###### Important

You must create a bucket policy on the *destination* bucket to grant
 permissions to Amazon S3 to write objects to the bucket in the defined location. For an example policy, see
  [Granting
 Permissions for Amazon S3 Inventory and Storage Class Analysis](https://docs.aws.amazon.com/AmazonS3/latest/dev/example-bucket-policies.html#example-bucket-policies-use-case-9 "https://docs.aws.amazon.com/AmazonS3/latest/dev/example-bucket-policies.html#example-bucket-policies-use-case-9").



Permissions

To use this operation, you must have permission to perform the
 `s3:PutInventoryConfiguration` action. The bucket owner has this permission by
 default and can grant this permission to others. 


The `s3:PutInventoryConfiguration` permission allows a user to create an [S3 Inventory](../userguide/storage-inventory.md "../userguide/storage-inventory.md")
 report that includes all object metadata fields available and to specify the destination bucket to
 store the inventory. A user with read access to objects in the destination bucket can also access
 all object metadata fields that are available in the inventory report. 


To restrict access to an inventory report, see [Restricting access to an Amazon S3 Inventory report](../userguide/example-bucket-policies.md#example-bucket-policies-use-case-10 "../userguide/example-bucket-policies.md#example-bucket-policies-use-case-10") in the
 *Amazon S3 User Guide*. For more information about the metadata fields available
 in S3 Inventory, see [Amazon S3 Inventory
 lists](../userguide/storage-inventory.md#storage-inventory-contents "../userguide/storage-inventory.md#storage-inventory-contents") in the *Amazon S3 User Guide*. For more information about
 permissions, see [Permissions related to bucket subresource operations](../userguide/using-with-s3-actions.md#using-with-s3-actions-related-to-bucket-subresources "../userguide/using-with-s3-actions.md#using-with-s3-actions-related-to-bucket-subresources") and [Identity and access management in
 Amazon S3](../userguide/s3-access-control.md "../userguide/s3-access-control.md") in the *Amazon S3 User Guide*.




`PutBucketInventoryConfiguration` has the following special errors:



HTTP 400 Bad Request Error


*Code:* InvalidArgument



*Cause:* Invalid Argument



HTTP 400 Bad Request Error


*Code:* TooManyConfigurations



*Cause:* You are attempting to create a new configuration but have already
 reached the 1,000-configuration limit. 



HTTP 403 Forbidden Error


*Cause:* You are not the owner of the specified bucket, or you do not have
 the `s3:PutInventoryConfiguration` bucket permission to set the configuration on the
 bucket. 



The following operations are related to `PutBucketInventoryConfiguration`:


* [GetBucketInventoryConfiguration](API_GetBucketInventoryConfiguration.md "API_GetBucketInventoryConfiguration.md")
* [DeleteBucketInventoryConfiguration](API_DeleteBucketInventoryConfiguration.md "API_DeleteBucketInventoryConfiguration.md")
* [ListBucketInventoryConfigurations](API_ListBucketInventoryConfigurations.md "API_ListBucketInventoryConfigurations.md")
###### Important

You must URL encode any signed header values that contain spaces. For example, if your header value is `my file.txt`, containing two spaces after `my`, you must URL encode this value to `my%20%20file.txt`.


## Request Syntax



```
PUT /?inventory&id=`Id` HTTP/1.1
Host: `Bucket`.s3.amazonaws.com
x-amz-expected-bucket-owner: `ExpectedBucketOwner`
<?xml version="1.0" encoding="UTF-8"?>
<[InventoryConfiguration](#AmazonS3-PutBucketInventoryConfiguration-request-InventoryConfiguration "#AmazonS3-PutBucketInventoryConfiguration-request-InventoryConfiguration") xmlns="http://s3.amazonaws.com/doc/2006-03-01/">
   <[Destination](#AmazonS3-PutBucketInventoryConfiguration-request-Destination "#AmazonS3-PutBucketInventoryConfiguration-request-Destination")>
      <[S3BucketDestination](API_InventoryDestination.md#AmazonS3-Type-InventoryDestination-S3BucketDestination "API_InventoryDestination.md#AmazonS3-Type-InventoryDestination-S3BucketDestination")>
         <[AccountId](API_InventoryS3BucketDestination.md#AmazonS3-Type-InventoryS3BucketDestination-AccountId "API_InventoryS3BucketDestination.md#AmazonS3-Type-InventoryS3BucketDestination-AccountId")>`string`</[AccountId](API_InventoryS3BucketDestination.md#AmazonS3-Type-InventoryS3BucketDestination-AccountId "API_InventoryS3BucketDestination.md#AmazonS3-Type-InventoryS3BucketDestination-AccountId")>
         <[Bucket](API_InventoryS3BucketDestination.md#AmazonS3-Type-InventoryS3BucketDestination-Bucket "API_InventoryS3BucketDestination.md#AmazonS3-Type-InventoryS3BucketDestination-Bucket")>`string`</[Bucket](API_InventoryS3BucketDestination.md#AmazonS3-Type-InventoryS3BucketDestination-Bucket "API_InventoryS3BucketDestination.md#AmazonS3-Type-InventoryS3BucketDestination-Bucket")>
         <[Encryption](API_InventoryS3BucketDestination.md#AmazonS3-Type-InventoryS3BucketDestination-Encryption "API_InventoryS3BucketDestination.md#AmazonS3-Type-InventoryS3BucketDestination-Encryption")>
            <[SSE-KMS](API_InventoryEncryption.md#AmazonS3-Type-InventoryEncryption-SSEKMS "API_InventoryEncryption.md#AmazonS3-Type-InventoryEncryption-SSEKMS")>
               <[KeyId](API_SSEKMS.md#AmazonS3-Type-SSEKMS-KeyId "API_SSEKMS.md#AmazonS3-Type-SSEKMS-KeyId")>`string`</[KeyId](API_SSEKMS.md#AmazonS3-Type-SSEKMS-KeyId "API_SSEKMS.md#AmazonS3-Type-SSEKMS-KeyId")>
            </[SSE-KMS](API_InventoryEncryption.md#AmazonS3-Type-InventoryEncryption-SSEKMS "API_InventoryEncryption.md#AmazonS3-Type-InventoryEncryption-SSEKMS")>
            <[SSE-S3](API_InventoryEncryption.md#AmazonS3-Type-InventoryEncryption-SSES3 "API_InventoryEncryption.md#AmazonS3-Type-InventoryEncryption-SSES3")>
            </[SSE-S3](API_InventoryEncryption.md#AmazonS3-Type-InventoryEncryption-SSES3 "API_InventoryEncryption.md#AmazonS3-Type-InventoryEncryption-SSES3")>
         </[Encryption](API_InventoryS3BucketDestination.md#AmazonS3-Type-InventoryS3BucketDestination-Encryption "API_InventoryS3BucketDestination.md#AmazonS3-Type-InventoryS3BucketDestination-Encryption")>
         <[Format](API_InventoryS3BucketDestination.md#AmazonS3-Type-InventoryS3BucketDestination-Format "API_InventoryS3BucketDestination.md#AmazonS3-Type-InventoryS3BucketDestination-Format")>`string`</[Format](API_InventoryS3BucketDestination.md#AmazonS3-Type-InventoryS3BucketDestination-Format "API_InventoryS3BucketDestination.md#AmazonS3-Type-InventoryS3BucketDestination-Format")>
         <[Prefix](API_InventoryS3BucketDestination.md#AmazonS3-Type-InventoryS3BucketDestination-Prefix "API_InventoryS3BucketDestination.md#AmazonS3-Type-InventoryS3BucketDestination-Prefix")>`string`</[Prefix](API_InventoryS3BucketDestination.md#AmazonS3-Type-InventoryS3BucketDestination-Prefix "API_InventoryS3BucketDestination.md#AmazonS3-Type-InventoryS3BucketDestination-Prefix")>
      </[S3BucketDestination](API_InventoryDestination.md#AmazonS3-Type-InventoryDestination-S3BucketDestination "API_InventoryDestination.md#AmazonS3-Type-InventoryDestination-S3BucketDestination")>
   </[Destination](#AmazonS3-PutBucketInventoryConfiguration-request-Destination "#AmazonS3-PutBucketInventoryConfiguration-request-Destination")>
   <[IsEnabled](#AmazonS3-PutBucketInventoryConfiguration-request-IsEnabled "#AmazonS3-PutBucketInventoryConfiguration-request-IsEnabled")>`boolean`</[IsEnabled](#AmazonS3-PutBucketInventoryConfiguration-request-IsEnabled "#AmazonS3-PutBucketInventoryConfiguration-request-IsEnabled")>
   <[Filter](#AmazonS3-PutBucketInventoryConfiguration-request-Filter "#AmazonS3-PutBucketInventoryConfiguration-request-Filter")>
      <[Prefix](API_InventoryFilter.md#AmazonS3-Type-InventoryFilter-Prefix "API_InventoryFilter.md#AmazonS3-Type-InventoryFilter-Prefix")>`string`</[Prefix](API_InventoryFilter.md#AmazonS3-Type-InventoryFilter-Prefix "API_InventoryFilter.md#AmazonS3-Type-InventoryFilter-Prefix")>
   </[Filter](#AmazonS3-PutBucketInventoryConfiguration-request-Filter "#AmazonS3-PutBucketInventoryConfiguration-request-Filter")>
   <[Id](#AmazonS3-PutBucketInventoryConfiguration-request-Id "#AmazonS3-PutBucketInventoryConfiguration-request-Id")>`string`</[Id](#AmazonS3-PutBucketInventoryConfiguration-request-Id "#AmazonS3-PutBucketInventoryConfiguration-request-Id")>
   <[IncludedObjectVersions](#AmazonS3-PutBucketInventoryConfiguration-request-IncludedObjectVersions "#AmazonS3-PutBucketInventoryConfiguration-request-IncludedObjectVersions")>`string`</[IncludedObjectVersions](#AmazonS3-PutBucketInventoryConfiguration-request-IncludedObjectVersions "#AmazonS3-PutBucketInventoryConfiguration-request-IncludedObjectVersions")>
   <[OptionalFields](#AmazonS3-PutBucketInventoryConfiguration-request-OptionalFields "#AmazonS3-PutBucketInventoryConfiguration-request-OptionalFields")>
      <Field>`string`</Field>
   </[OptionalFields](#AmazonS3-PutBucketInventoryConfiguration-request-OptionalFields "#AmazonS3-PutBucketInventoryConfiguration-request-OptionalFields")>
   <[Schedule](#AmazonS3-PutBucketInventoryConfiguration-request-Schedule "#AmazonS3-PutBucketInventoryConfiguration-request-Schedule")>
      <[Frequency](API_InventorySchedule.md#AmazonS3-Type-InventorySchedule-Frequency "API_InventorySchedule.md#AmazonS3-Type-InventorySchedule-Frequency")>`string`</[Frequency](API_InventorySchedule.md#AmazonS3-Type-InventorySchedule-Frequency "API_InventorySchedule.md#AmazonS3-Type-InventorySchedule-Frequency")>
   </[Schedule](#AmazonS3-PutBucketInventoryConfiguration-request-Schedule "#AmazonS3-PutBucketInventoryConfiguration-request-Schedule")>
</[InventoryConfiguration](#AmazonS3-PutBucketInventoryConfiguration-request-InventoryConfiguration "#AmazonS3-PutBucketInventoryConfiguration-request-InventoryConfiguration")>
```

## URI Request Parameters


The request uses the following URI parameters.





**[Bucket](#API_PutBucketInventoryConfiguration_RequestSyntax "#API_PutBucketInventoryConfiguration_RequestSyntax")**


The name of the bucket where the inventory configuration will be stored.


Required: Yes




**[id](#API_PutBucketInventoryConfiguration_RequestSyntax "#API_PutBucketInventoryConfiguration_RequestSyntax")**


The ID used to identify the inventory configuration.


Required: Yes




**[x-amz-expected-bucket-owner](#API_PutBucketInventoryConfiguration_RequestSyntax "#API_PutBucketInventoryConfiguration_RequestSyntax")**


The account ID of the expected bucket owner. If the account ID that you provide does not match the actual owner of the bucket, the request fails with the HTTP status code `403 Forbidden` (access denied).




## Request Body


The request accepts the following data in XML format.





**[InventoryConfiguration](#API_PutBucketInventoryConfiguration_RequestSyntax "#API_PutBucketInventoryConfiguration_RequestSyntax")**


Root level tag for the InventoryConfiguration parameters.


Required: Yes




**[Destination](#API_PutBucketInventoryConfiguration_RequestSyntax "#API_PutBucketInventoryConfiguration_RequestSyntax")**


Contains information about where to publish the inventory results.


Type: [InventoryDestination](API_InventoryDestination.md "API_InventoryDestination.md") data type


Required: Yes




**[Filter](#API_PutBucketInventoryConfiguration_RequestSyntax "#API_PutBucketInventoryConfiguration_RequestSyntax")**


Specifies an inventory filter. The inventory only includes objects that meet the filter's
 criteria.


Type: [InventoryFilter](API_InventoryFilter.md "API_InventoryFilter.md") data type


Required: No




**[Id](#API_PutBucketInventoryConfiguration_RequestSyntax "#API_PutBucketInventoryConfiguration_RequestSyntax")**


The ID used to identify the inventory configuration.


Type: String


Required: Yes




**[IncludedObjectVersions](#API_PutBucketInventoryConfiguration_RequestSyntax "#API_PutBucketInventoryConfiguration_RequestSyntax")**


Object versions to include in the inventory list. If set to `All`, the list includes all
 the object versions, which adds the version-related fields `VersionId`,
 `IsLatest`, and `DeleteMarker` to the list. If set to `Current`, the
 list does not contain these version-related fields.


Type: String


Valid Values: `All | Current`



Required: Yes




**[IsEnabled](#API_PutBucketInventoryConfiguration_RequestSyntax "#API_PutBucketInventoryConfiguration_RequestSyntax")**


Specifies whether the inventory is enabled or disabled. If set to `True`, an inventory
 list is generated. If set to `False`, no inventory list is generated.


Type: Boolean


Required: Yes




**[OptionalFields](#API_PutBucketInventoryConfiguration_RequestSyntax "#API_PutBucketInventoryConfiguration_RequestSyntax")**


Contains the optional fields that are included in the inventory results.


Type: Array of strings


Valid Values: `Size | LastModifiedDate | StorageClass | ETag | IsMultipartUploaded | ReplicationStatus | EncryptionStatus | ObjectLockRetainUntilDate | ObjectLockMode | ObjectLockLegalHoldStatus | IntelligentTieringAccessTier | BucketKeyStatus | ChecksumAlgorithm | ObjectAccessControlList | ObjectOwner`



Required: No




**[Schedule](#API_PutBucketInventoryConfiguration_RequestSyntax "#API_PutBucketInventoryConfiguration_RequestSyntax")**


Specifies the schedule for generating inventory results.


Type: [InventorySchedule](API_InventorySchedule.md "API_InventorySchedule.md") data type


Required: Yes




## Response Syntax



```
HTTP/1.1 200

```

## Response Elements


If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.


## Examples


### Example: Create an inventory configuration


The following `PUT` request and response for the bucket `examplebucket`
 creates a new or replaces an existing inventory configuration with the ID `report1`. The
 configuration is defined in the request body. 



```
PUT /?inventory&id=report1 HTTP/1.1
Host: examplebucket.s3.<Region>.amazonaws.com
Date: Mon, 31 Oct 2016 12:00:00 GMT
Authorization: authorization string
Content-Length: length
 
<?xml version="1.0" encoding="UTF-8"?>
<InventoryConfiguration xmlns="http://s3.amazonaws.com/doc/2006-03-01/">
   <Id>report1</Id>
   <IsEnabled>true</IsEnabled>
   <Filter>
      <Prefix>filterPrefix</Prefix>
   </Filter>
   <Destination>
      <S3BucketDestination>
         <Format>CSV</Format>
         <AccountId>123456789012</AccountId>
         <Bucket>arn:aws:s3:::destination-bucket</Bucket>
         <Prefix>prefix1</Prefix>
         <Encryption>
            <SSE-KMS>
               <KeyId>arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab</KeyId>
            </SSE-KMS>
         </Encryption>
      </S3BucketDestination>
   </Destination>
   <Schedule>
      <Frequency>Daily</Frequency>
   </Schedule>
   <IncludedObjectVersions>All</IncludedObjectVersions>
   <OptionalFields>
      <Field>Size</Field>
      <Field>LastModifiedDate</Field>
      <Field>ETag</Field>
      <Field>StorageClass</Field>
      <Field>IsMultipartUploaded</Field>
      <Field>ReplicationStatus</Field>
      <Field>EncryptionStatus</Field>
      <Field>ObjectLockRetainUntilDate</Field> 
      <Field>ObjectLockMode</Field>
      <Field>ObjectLockLegalHoldStatus</Field>      
   </OptionalFields>
</InventoryConfiguration>
           
```


```

HTTP/1.1 200 OK
x-amz-id-2: YgIPIfBiKa2bj0KMg95r/0zo3emzU4dzsD4rcKCHQUAdQkf3ShJTOOpXUueF6QKo
x-amz-request-id: 236A8905248E5A01
Date: Mon, 31 Oct 2016 12:00:00 GMT
Content-Length: 0
Server: AmazonS3
           
```

## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface](https://docs.aws.amazon.com/goto/cli2/s3-2006-03-01/PutBucketInventoryConfiguration "https://docs.aws.amazon.com/goto/cli2/s3-2006-03-01/PutBucketInventoryConfiguration")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/s3-2006-03-01/PutBucketInventoryConfiguration "https://docs.aws.amazon.com/goto/DotNetSDKV3/s3-2006-03-01/PutBucketInventoryConfiguration")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/PutBucketInventoryConfiguration "https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/PutBucketInventoryConfiguration")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/s3-2006-03-01/PutBucketInventoryConfiguration "https://docs.aws.amazon.com/goto/SdkForGoV2/s3-2006-03-01/PutBucketInventoryConfiguration")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/PutBucketInventoryConfiguration "https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/PutBucketInventoryConfiguration")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3-2006-03-01/PutBucketInventoryConfiguration "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3-2006-03-01/PutBucketInventoryConfiguration")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/s3-2006-03-01/PutBucketInventoryConfiguration "https://docs.aws.amazon.com/goto/SdkForKotlin/s3-2006-03-01/PutBucketInventoryConfiguration")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/s3-2006-03-01/PutBucketInventoryConfiguration "https://docs.aws.amazon.com/goto/SdkForPHPV3/s3-2006-03-01/PutBucketInventoryConfiguration")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/s3-2006-03-01/PutBucketInventoryConfiguration "https://docs.aws.amazon.com/goto/boto3/s3-2006-03-01/PutBucketInventoryConfiguration")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/PutBucketInventoryConfiguration "https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/PutBucketInventoryConfiguration")
