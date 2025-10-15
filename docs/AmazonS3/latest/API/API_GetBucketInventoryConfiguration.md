# GetBucketInventoryConfiguration

###### Note

This operation is not supported for directory buckets.

Returns an S3 Inventory configuration (identified by the inventory configuration ID) from the
 bucket.

To use this operation, you must have permissions to perform the
 `s3:GetInventoryConfiguration` action. The bucket owner has this permission by default and
 can grant this permission to others. For more information about permissions, see [Permissions Related to Bucket Subresource Operations](../userguide/using-with-s3-actions.md#using-with-s3-actions-related-to-bucket-subresources "../userguide/using-with-s3-actions.md#using-with-s3-actions-related-to-bucket-subresources") and [Managing Access Permissions to Your Amazon S3
 Resources](../userguide/s3-access-control.md "../userguide/s3-access-control.md").

For information about the Amazon S3 inventory feature, see [Amazon S3 Inventory](https://docs.aws.amazon.com/AmazonS3/latest/dev/storage-inventory.html "https://docs.aws.amazon.com/AmazonS3/latest/dev/storage-inventory.html").

The following operations are related to `GetBucketInventoryConfiguration`:


* [DeleteBucketInventoryConfiguration](API_DeleteBucketInventoryConfiguration.md "API_DeleteBucketInventoryConfiguration.md")
* [ListBucketInventoryConfigurations](API_ListBucketInventoryConfigurations.md "API_ListBucketInventoryConfigurations.md")
* [PutBucketInventoryConfiguration](API_PutBucketInventoryConfiguration.md "API_PutBucketInventoryConfiguration.md")
###### Important

You must URL encode any signed header values that contain spaces. For example, if your header value is `my file.txt`, containing two spaces after `my`, you must URL encode this value to `my%20%20file.txt`.


## Request Syntax



```
GET /?inventory&id=`Id` HTTP/1.1
Host: `Bucket`.s3.amazonaws.com
x-amz-expected-bucket-owner: `ExpectedBucketOwner`

```

## URI Request Parameters


The request uses the following URI parameters.





**[Bucket](#API_GetBucketInventoryConfiguration_RequestSyntax "#API_GetBucketInventoryConfiguration_RequestSyntax")**


The name of the bucket containing the inventory configuration to retrieve.


Required: Yes




**[id](#API_GetBucketInventoryConfiguration_RequestSyntax "#API_GetBucketInventoryConfiguration_RequestSyntax")**


The ID used to identify the inventory configuration.


Required: Yes




**[x-amz-expected-bucket-owner](#API_GetBucketInventoryConfiguration_RequestSyntax "#API_GetBucketInventoryConfiguration_RequestSyntax")**


The account ID of the expected bucket owner. If the account ID that you provide does not match the actual owner of the bucket, the request fails with the HTTP status code `403 Forbidden` (access denied).




## Request Body


The request does not have a request body.


## Response Syntax



```
HTTP/1.1 200
<?xml version="1.0" encoding="UTF-8"?>
<[InventoryConfiguration](#AmazonS3-GetBucketInventoryConfiguration-response-InventoryConfiguration "#AmazonS3-GetBucketInventoryConfiguration-response-InventoryConfiguration")>
   <[Destination](#AmazonS3-GetBucketInventoryConfiguration-response-Destination "#AmazonS3-GetBucketInventoryConfiguration-response-Destination")>
      <[S3BucketDestination](API_InventoryDestination.md#AmazonS3-Type-InventoryDestination-S3BucketDestination "API_InventoryDestination.md#AmazonS3-Type-InventoryDestination-S3BucketDestination")>
         <[AccountId](API_InventoryS3BucketDestination.md#AmazonS3-Type-InventoryS3BucketDestination-AccountId "API_InventoryS3BucketDestination.md#AmazonS3-Type-InventoryS3BucketDestination-AccountId")>***string***</[AccountId](API_InventoryS3BucketDestination.md#AmazonS3-Type-InventoryS3BucketDestination-AccountId "API_InventoryS3BucketDestination.md#AmazonS3-Type-InventoryS3BucketDestination-AccountId")>
         <[Bucket](API_InventoryS3BucketDestination.md#AmazonS3-Type-InventoryS3BucketDestination-Bucket "API_InventoryS3BucketDestination.md#AmazonS3-Type-InventoryS3BucketDestination-Bucket")>***string***</[Bucket](API_InventoryS3BucketDestination.md#AmazonS3-Type-InventoryS3BucketDestination-Bucket "API_InventoryS3BucketDestination.md#AmazonS3-Type-InventoryS3BucketDestination-Bucket")>
         <[Encryption](API_InventoryS3BucketDestination.md#AmazonS3-Type-InventoryS3BucketDestination-Encryption "API_InventoryS3BucketDestination.md#AmazonS3-Type-InventoryS3BucketDestination-Encryption")>
            <[SSE-KMS](API_InventoryEncryption.md#AmazonS3-Type-InventoryEncryption-SSEKMS "API_InventoryEncryption.md#AmazonS3-Type-InventoryEncryption-SSEKMS")>
               <[KeyId](API_SSEKMS.md#AmazonS3-Type-SSEKMS-KeyId "API_SSEKMS.md#AmazonS3-Type-SSEKMS-KeyId")>***string***</[KeyId](API_SSEKMS.md#AmazonS3-Type-SSEKMS-KeyId "API_SSEKMS.md#AmazonS3-Type-SSEKMS-KeyId")>
            </[SSE-KMS](API_InventoryEncryption.md#AmazonS3-Type-InventoryEncryption-SSEKMS "API_InventoryEncryption.md#AmazonS3-Type-InventoryEncryption-SSEKMS")>
            <[SSE-S3](API_InventoryEncryption.md#AmazonS3-Type-InventoryEncryption-SSES3 "API_InventoryEncryption.md#AmazonS3-Type-InventoryEncryption-SSES3")>
            </[SSE-S3](API_InventoryEncryption.md#AmazonS3-Type-InventoryEncryption-SSES3 "API_InventoryEncryption.md#AmazonS3-Type-InventoryEncryption-SSES3")>
         </[Encryption](API_InventoryS3BucketDestination.md#AmazonS3-Type-InventoryS3BucketDestination-Encryption "API_InventoryS3BucketDestination.md#AmazonS3-Type-InventoryS3BucketDestination-Encryption")>
         <[Format](API_InventoryS3BucketDestination.md#AmazonS3-Type-InventoryS3BucketDestination-Format "API_InventoryS3BucketDestination.md#AmazonS3-Type-InventoryS3BucketDestination-Format")>***string***</[Format](API_InventoryS3BucketDestination.md#AmazonS3-Type-InventoryS3BucketDestination-Format "API_InventoryS3BucketDestination.md#AmazonS3-Type-InventoryS3BucketDestination-Format")>
         <[Prefix](API_InventoryS3BucketDestination.md#AmazonS3-Type-InventoryS3BucketDestination-Prefix "API_InventoryS3BucketDestination.md#AmazonS3-Type-InventoryS3BucketDestination-Prefix")>***string***</[Prefix](API_InventoryS3BucketDestination.md#AmazonS3-Type-InventoryS3BucketDestination-Prefix "API_InventoryS3BucketDestination.md#AmazonS3-Type-InventoryS3BucketDestination-Prefix")>
      </[S3BucketDestination](API_InventoryDestination.md#AmazonS3-Type-InventoryDestination-S3BucketDestination "API_InventoryDestination.md#AmazonS3-Type-InventoryDestination-S3BucketDestination")>
   </[Destination](#AmazonS3-GetBucketInventoryConfiguration-response-Destination "#AmazonS3-GetBucketInventoryConfiguration-response-Destination")>
   <[IsEnabled](#AmazonS3-GetBucketInventoryConfiguration-response-IsEnabled "#AmazonS3-GetBucketInventoryConfiguration-response-IsEnabled")>***boolean***</[IsEnabled](#AmazonS3-GetBucketInventoryConfiguration-response-IsEnabled "#AmazonS3-GetBucketInventoryConfiguration-response-IsEnabled")>
   <[Filter](#AmazonS3-GetBucketInventoryConfiguration-response-Filter "#AmazonS3-GetBucketInventoryConfiguration-response-Filter")>
      <[Prefix](API_InventoryFilter.md#AmazonS3-Type-InventoryFilter-Prefix "API_InventoryFilter.md#AmazonS3-Type-InventoryFilter-Prefix")>***string***</[Prefix](API_InventoryFilter.md#AmazonS3-Type-InventoryFilter-Prefix "API_InventoryFilter.md#AmazonS3-Type-InventoryFilter-Prefix")>
   </[Filter](#AmazonS3-GetBucketInventoryConfiguration-response-Filter "#AmazonS3-GetBucketInventoryConfiguration-response-Filter")>
   <[Id](#AmazonS3-GetBucketInventoryConfiguration-response-Id "#AmazonS3-GetBucketInventoryConfiguration-response-Id")>***string***</[Id](#AmazonS3-GetBucketInventoryConfiguration-response-Id "#AmazonS3-GetBucketInventoryConfiguration-response-Id")>
   <[IncludedObjectVersions](#AmazonS3-GetBucketInventoryConfiguration-response-IncludedObjectVersions "#AmazonS3-GetBucketInventoryConfiguration-response-IncludedObjectVersions")>***string***</[IncludedObjectVersions](#AmazonS3-GetBucketInventoryConfiguration-response-IncludedObjectVersions "#AmazonS3-GetBucketInventoryConfiguration-response-IncludedObjectVersions")>
   <[OptionalFields](#AmazonS3-GetBucketInventoryConfiguration-response-OptionalFields "#AmazonS3-GetBucketInventoryConfiguration-response-OptionalFields")>
      <Field>***string***</Field>
   </[OptionalFields](#AmazonS3-GetBucketInventoryConfiguration-response-OptionalFields "#AmazonS3-GetBucketInventoryConfiguration-response-OptionalFields")>
   <[Schedule](#AmazonS3-GetBucketInventoryConfiguration-response-Schedule "#AmazonS3-GetBucketInventoryConfiguration-response-Schedule")>
      <[Frequency](API_InventorySchedule.md#AmazonS3-Type-InventorySchedule-Frequency "API_InventorySchedule.md#AmazonS3-Type-InventorySchedule-Frequency")>***string***</[Frequency](API_InventorySchedule.md#AmazonS3-Type-InventorySchedule-Frequency "API_InventorySchedule.md#AmazonS3-Type-InventorySchedule-Frequency")>
   </[Schedule](#AmazonS3-GetBucketInventoryConfiguration-response-Schedule "#AmazonS3-GetBucketInventoryConfiguration-response-Schedule")>
</[InventoryConfiguration](#AmazonS3-GetBucketInventoryConfiguration-response-InventoryConfiguration "#AmazonS3-GetBucketInventoryConfiguration-response-InventoryConfiguration")>
```

## Response Elements


If the action is successful, the service sends back an HTTP 200 response.


The following data is returned in XML format by the service.





**[InventoryConfiguration](#API_GetBucketInventoryConfiguration_ResponseSyntax "#API_GetBucketInventoryConfiguration_ResponseSyntax")**


Root level tag for the InventoryConfiguration parameters.


Required: Yes




**[Destination](#API_GetBucketInventoryConfiguration_ResponseSyntax "#API_GetBucketInventoryConfiguration_ResponseSyntax")**


Contains information about where to publish the inventory results.


Type: [InventoryDestination](API_InventoryDestination.md "API_InventoryDestination.md") data type




**[Filter](#API_GetBucketInventoryConfiguration_ResponseSyntax "#API_GetBucketInventoryConfiguration_ResponseSyntax")**


Specifies an inventory filter. The inventory only includes objects that meet the filter's
 criteria.


Type: [InventoryFilter](API_InventoryFilter.md "API_InventoryFilter.md") data type




**[Id](#API_GetBucketInventoryConfiguration_ResponseSyntax "#API_GetBucketInventoryConfiguration_ResponseSyntax")**


The ID used to identify the inventory configuration.


Type: String




**[IncludedObjectVersions](#API_GetBucketInventoryConfiguration_ResponseSyntax "#API_GetBucketInventoryConfiguration_ResponseSyntax")**


Object versions to include in the inventory list. If set to `All`, the list includes all
 the object versions, which adds the version-related fields `VersionId`,
 `IsLatest`, and `DeleteMarker` to the list. If set to `Current`, the
 list does not contain these version-related fields.


Type: String


Valid Values: `All | Current`





**[IsEnabled](#API_GetBucketInventoryConfiguration_ResponseSyntax "#API_GetBucketInventoryConfiguration_ResponseSyntax")**


Specifies whether the inventory is enabled or disabled. If set to `True`, an inventory
 list is generated. If set to `False`, no inventory list is generated.


Type: Boolean




**[OptionalFields](#API_GetBucketInventoryConfiguration_ResponseSyntax "#API_GetBucketInventoryConfiguration_ResponseSyntax")**


Contains the optional fields that are included in the inventory results.


Type: Array of strings


Valid Values: `Size | LastModifiedDate | StorageClass | ETag | IsMultipartUploaded | ReplicationStatus | EncryptionStatus | ObjectLockRetainUntilDate | ObjectLockMode | ObjectLockLegalHoldStatus | IntelligentTieringAccessTier | BucketKeyStatus | ChecksumAlgorithm | ObjectAccessControlList | ObjectOwner`





**[Schedule](#API_GetBucketInventoryConfiguration_ResponseSyntax "#API_GetBucketInventoryConfiguration_ResponseSyntax")**


Specifies the schedule for generating inventory results.


Type: [InventorySchedule](API_InventorySchedule.md "API_InventorySchedule.md") data type




## Examples


### Sample Request: Configure an inventory report


The following GET request for the bucket `examplebucket` returns the inventory
 configuration with the ID `list1`.



```

            GET /?inventory&id=list1 HTTP/1.1
            Host: examplebucket.s3.<Region>.amazonaws.com
            Date: Mon, 31 Oct 2016 12:00:00 GMT
            Authorization: authorization string 
         
```

### Sample Response


This example illustrates one usage of GetBucketInventoryConfiguration.



```

         HTTP/1.1 200 OK
         x-amz-id-2: YgIPIfBiKa2bj0KMgUAdQkf3ShJTOOpXUueF6QKo
         x-amz-request-id: 236A8905248E5A02
         Date: Mon, 31 Oct 2016 12:00:00 GMT
         Server: AmazonS3
         Content-Length: length

         <?xml version="1.0" encoding="UTF-8"?>
         <InventoryConfiguration xmlns="http://s3.amazonaws.com/doc/2006-03-01/">
            <Id>report1</Id>
           <IsEnabled>true</IsEnabled>
           <Destination>
              <S3BucketDestination>
                 <Format>CSV</Format>
                  <AccountId>123456789012</AccountId>
                  <Bucket>arn:aws:s3:::destination-bucket</Bucket>
                 <Prefix>prefix1</Prefix>
                 <SSE-S3/>
               </S3BucketDestination>
            </Destination>
            <Schedule>
               <Frequency>Daily</Frequency>
           </Schedule>
           <Filter>
             <Prefix>myprefix/</Prefix>
           </Filter>
           <IncludedObjectVersions>All</IncludedObjectVersions>
           <OptionalFields>
             <Field>Size</Field>
             <Field>LastModifiedDate</Field>
               <Field>ETag</Field>
               <Field>StorageClass</Field>
               <Field>IsMultipartUploaded</Field>
             <Field>ReplicationStatus</Field>
               <Field>ObjectLockRetainUntilDate</Field>
               <Field>ObjectLockMode</Field>
             <Field>ObjectLockLegalHoldStatus</Field> 
          </OptionalFields>
         </InventoryConfiguration>
         
```

## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface](https://docs.aws.amazon.com/goto/cli2/s3-2006-03-01/GetBucketInventoryConfiguration "https://docs.aws.amazon.com/goto/cli2/s3-2006-03-01/GetBucketInventoryConfiguration")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/s3-2006-03-01/GetBucketInventoryConfiguration "https://docs.aws.amazon.com/goto/DotNetSDKV3/s3-2006-03-01/GetBucketInventoryConfiguration")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/GetBucketInventoryConfiguration "https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/GetBucketInventoryConfiguration")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/s3-2006-03-01/GetBucketInventoryConfiguration "https://docs.aws.amazon.com/goto/SdkForGoV2/s3-2006-03-01/GetBucketInventoryConfiguration")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/GetBucketInventoryConfiguration "https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/GetBucketInventoryConfiguration")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3-2006-03-01/GetBucketInventoryConfiguration "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3-2006-03-01/GetBucketInventoryConfiguration")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/s3-2006-03-01/GetBucketInventoryConfiguration "https://docs.aws.amazon.com/goto/SdkForKotlin/s3-2006-03-01/GetBucketInventoryConfiguration")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/s3-2006-03-01/GetBucketInventoryConfiguration "https://docs.aws.amazon.com/goto/SdkForPHPV3/s3-2006-03-01/GetBucketInventoryConfiguration")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/s3-2006-03-01/GetBucketInventoryConfiguration "https://docs.aws.amazon.com/goto/boto3/s3-2006-03-01/GetBucketInventoryConfiguration")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/GetBucketInventoryConfiguration "https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/GetBucketInventoryConfiguration")
