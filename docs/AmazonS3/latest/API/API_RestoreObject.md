# RestoreObject

###### Note

This operation is not supported for directory buckets.

Restores an archived copy of an object back into Amazon S3

This functionality is not supported for Amazon S3 on Outposts.

This action performs the following types of requests: 


* `restore an archive` - Restore an archived object
For more information about the `S3` structure in the request body, see the
 following:


* [PutObject](API_PutObject.md "API_PutObject.md")
* [Managing Access
 with ACLs](https://docs.aws.amazon.com/AmazonS3/latest/dev/S3_ACLs_UsingACLs.html "https://docs.aws.amazon.com/AmazonS3/latest/dev/S3_ACLs_UsingACLs.html") in the *Amazon S3 User Guide*
* [Protecting Data
 Using Server-Side Encryption](https://docs.aws.amazon.com/AmazonS3/latest/dev/serv-side-encryption.html "https://docs.aws.amazon.com/AmazonS3/latest/dev/serv-side-encryption.html") in the *Amazon S3 User Guide*


Permissions

To use this operation, you must have permissions to perform the `s3:RestoreObject`
 action. The bucket owner has this permission by default and can grant this permission to others.
 For more information about permissions, see [Permissions Related to Bucket Subresource Operations](../userguide/using-with-s3-actions.md#using-with-s3-actions-related-to-bucket-subresources "../userguide/using-with-s3-actions.md#using-with-s3-actions-related-to-bucket-subresources") and [Managing Access Permissions to Your Amazon S3
 Resources](../userguide/s3-access-control.md "../userguide/s3-access-control.md") in the *Amazon S3 User Guide*.



Restoring objects

Objects that you archive to the S3 Glacier Flexible Retrieval or S3 Glacier Deep Archive
 storage class, and S3 Intelligent-Tiering Archive or S3 Intelligent-Tiering Deep Archive tiers, are not accessible in
 real time. For objects in the S3 Glacier Flexible Retrieval or S3 Glacier Deep Archive
 storage classes, you must first initiate a restore request, and then wait until a temporary copy
 of the object is available. If you want a permanent copy of the object, create a copy of it in the
 Amazon S3 Standard storage class in your S3 bucket. To access an archived object, you must restore the
 object for the duration (number of days) that you specify. For objects in the Archive Access or
 Deep Archive Access tiers of S3 Intelligent-Tiering, you must first initiate a restore request, and
 then wait until the object is moved into the Frequent Access tier.


To restore a specific object version, you can provide a version ID. If you don't provide a
 version ID, Amazon S3 restores the current version.


When restoring an archived object, you can specify one of the following data access tier
 options in the `Tier` element of the request body: 



* `Expedited` - Expedited retrievals allow you to quickly access your data stored
 in the S3 Glacier Flexible Retrieval storage class or S3 Intelligent-Tiering Archive tier when occasional
 urgent requests for restoring archives are required. For all but the largest archived objects
 (250 MB+), data accessed using Expedited retrievals is typically made available within 1–5
 minutes. Provisioned capacity ensures that retrieval capacity for Expedited retrievals is
 available when you need it. Expedited retrievals and provisioned capacity are not available
 for objects stored in the S3 Glacier Deep Archive storage class or
 S3 Intelligent-Tiering Deep Archive tier.
* `Standard` - Standard retrievals allow you to access any of your archived
 objects within several hours. This is the default option for retrieval requests that do not
 specify the retrieval option. Standard retrievals typically finish within 3–5 hours for
 objects stored in the S3 Glacier Flexible Retrieval storage class or S3 Intelligent-Tiering Archive tier.
 They typically finish within 12 hours for objects stored in the
 S3 Glacier Deep Archive storage class or S3 Intelligent-Tiering Deep Archive tier. Standard
 retrievals are free for objects stored in S3 Intelligent-Tiering.
* `Bulk` - Bulk retrievals free for objects stored in the S3 Glacier Flexible
 Retrieval and S3 Intelligent-Tiering storage classes, enabling you to retrieve large amounts,
 even petabytes, of data at no cost. Bulk retrievals typically finish within 5–12 hours for
 objects stored in the S3 Glacier Flexible Retrieval storage class or S3 Intelligent-Tiering Archive tier.
 Bulk retrievals are also the lowest-cost retrieval option when restoring objects from
 S3 Glacier Deep Archive. They typically finish within 48 hours for objects stored in
 the S3 Glacier Deep Archive storage class or S3 Intelligent-Tiering Deep Archive tier.

For more information about archive retrieval options and provisioned capacity for
 `Expedited` data access, see [Restoring Archived Objects](https://docs.aws.amazon.com/AmazonS3/latest/dev/restoring-objects.html "https://docs.aws.amazon.com/AmazonS3/latest/dev/restoring-objects.html") in the
 *Amazon S3 User Guide*. 


You can use Amazon S3 restore speed upgrade to change the restore speed to a faster speed while it
 is in progress. For more information, see [Upgrading the speed of an in-progress restore](https://docs.aws.amazon.com/AmazonS3/latest/dev/restoring-objects.html#restoring-objects-upgrade-tier.title.html "https://docs.aws.amazon.com/AmazonS3/latest/dev/restoring-objects.html#restoring-objects-upgrade-tier.title.html") in the
 *Amazon S3 User Guide*. 


To get the status of object restoration, you can send a `HEAD` request. Operations
 return the `x-amz-restore` header, which provides information about the restoration
 status, in the response. You can use Amazon S3 event notifications to notify you when a restore is
 initiated or completed. For more information, see [Configuring Amazon S3 Event Notifications](https://docs.aws.amazon.com/AmazonS3/latest/dev/NotificationHowTo.html "https://docs.aws.amazon.com/AmazonS3/latest/dev/NotificationHowTo.html") in
 the *Amazon S3 User Guide*.


After restoring an archived object, you can update the restoration period by reissuing the
 request with a new period. Amazon S3 updates the restoration period relative to the current time and
 charges only for the request-there are no data transfer charges. You cannot update the
 restoration period when Amazon S3 is actively processing your current restore request for the
 object.


If your bucket has a lifecycle configuration with a rule that includes an expiration action,
 the object expiration overrides the life span that you specify in a restore request. For example,
 if you restore an object copy for 10 days, but the object is scheduled to expire in 3 days, Amazon S3
 deletes the object in 3 days. For more information about lifecycle configuration, see [PutBucketLifecycleConfiguration](API_PutBucketLifecycleConfiguration.md "API_PutBucketLifecycleConfiguration.md") and [Object Lifecycle Management](https://docs.aws.amazon.com/AmazonS3/latest/dev/object-lifecycle-mgmt.html "https://docs.aws.amazon.com/AmazonS3/latest/dev/object-lifecycle-mgmt.html") in
 *Amazon S3 User Guide*.



Responses

A successful action returns either the `200 OK` or `202 Accepted` status
 code. 



* If the object is not previously restored, then Amazon S3 returns `202 Accepted` in
 the response.
* If the object is previously restored, Amazon S3 returns `200 OK` in the response.


* Special errors:




	+ *Code: RestoreAlreadyInProgress*
	+ *Cause: Object restore is already in progress.*
	+ *HTTP Status Code: 409 Conflict*
	+ *SOAP Fault Code Prefix: Client*
* + *Code: GlacierExpeditedRetrievalNotAvailable*
	+ *Cause: expedited retrievals are currently not available. Try again later.
	 (Returned if there is insufficient capacity to process the Expedited request. This error
	 applies only to Expedited retrievals and not to S3 Standard or Bulk
	 retrievals.)*
	+ *HTTP Status Code: 503*
	+ *SOAP Fault Code Prefix: N/A*


The following operations are related to `RestoreObject`:


* [PutBucketLifecycleConfiguration](API_PutBucketLifecycleConfiguration.md "API_PutBucketLifecycleConfiguration.md")
* [GetBucketNotificationConfiguration](API_GetBucketNotificationConfiguration.md "API_GetBucketNotificationConfiguration.md")
###### Important

You must URL encode any signed header values that contain spaces. For example, if your header value is `my file.txt`, containing two spaces after `my`, you must URL encode this value to `my%20%20file.txt`.


## Request Syntax



```
POST /{Key+}?restore&versionId=`VersionId` HTTP/1.1
Host: `Bucket`.s3.amazonaws.com
x-amz-request-payer: `RequestPayer`
x-amz-sdk-checksum-algorithm: `ChecksumAlgorithm`
x-amz-expected-bucket-owner: `ExpectedBucketOwner`
<?xml version="1.0" encoding="UTF-8"?>
<[RestoreRequest](#AmazonS3-RestoreObject-request-RestoreRequest "#AmazonS3-RestoreObject-request-RestoreRequest") xmlns="http://s3.amazonaws.com/doc/2006-03-01/">
   <[Days](#AmazonS3-RestoreObject-request-Days "#AmazonS3-RestoreObject-request-Days")>`integer`</[Days](#AmazonS3-RestoreObject-request-Days "#AmazonS3-RestoreObject-request-Days")>
   <[GlacierJobParameters](#AmazonS3-RestoreObject-request-GlacierJobParameters "#AmazonS3-RestoreObject-request-GlacierJobParameters")>
      <[Tier](API_GlacierJobParameters.md#AmazonS3-Type-GlacierJobParameters-Tier "API_GlacierJobParameters.md#AmazonS3-Type-GlacierJobParameters-Tier")>`string`</[Tier](API_GlacierJobParameters.md#AmazonS3-Type-GlacierJobParameters-Tier "API_GlacierJobParameters.md#AmazonS3-Type-GlacierJobParameters-Tier")>
   </[GlacierJobParameters](#AmazonS3-RestoreObject-request-GlacierJobParameters "#AmazonS3-RestoreObject-request-GlacierJobParameters")>
   <[Type](#AmazonS3-RestoreObject-request-Type "#AmazonS3-RestoreObject-request-Type")>`string`</[Type](#AmazonS3-RestoreObject-request-Type "#AmazonS3-RestoreObject-request-Type")>
   <[Tier](#AmazonS3-RestoreObject-request-Tier "#AmazonS3-RestoreObject-request-Tier")>`string`</[Tier](#AmazonS3-RestoreObject-request-Tier "#AmazonS3-RestoreObject-request-Tier")>
   <[Description](#AmazonS3-RestoreObject-request-Description "#AmazonS3-RestoreObject-request-Description")>`string`</[Description](#AmazonS3-RestoreObject-request-Description "#AmazonS3-RestoreObject-request-Description")>
   <[SelectParameters](#AmazonS3-RestoreObject-request-SelectParameters "#AmazonS3-RestoreObject-request-SelectParameters")>
      <[Expression](API_SelectParameters.md#AmazonS3-Type-SelectParameters-Expression "API_SelectParameters.md#AmazonS3-Type-SelectParameters-Expression")>`string`</[Expression](API_SelectParameters.md#AmazonS3-Type-SelectParameters-Expression "API_SelectParameters.md#AmazonS3-Type-SelectParameters-Expression")>
      <[ExpressionType](API_SelectParameters.md#AmazonS3-Type-SelectParameters-ExpressionType "API_SelectParameters.md#AmazonS3-Type-SelectParameters-ExpressionType")>`string`</[ExpressionType](API_SelectParameters.md#AmazonS3-Type-SelectParameters-ExpressionType "API_SelectParameters.md#AmazonS3-Type-SelectParameters-ExpressionType")>
      <[InputSerialization](API_SelectParameters.md#AmazonS3-Type-SelectParameters-InputSerialization "API_SelectParameters.md#AmazonS3-Type-SelectParameters-InputSerialization")>
         <[CompressionType](API_InputSerialization.md#AmazonS3-Type-InputSerialization-CompressionType "API_InputSerialization.md#AmazonS3-Type-InputSerialization-CompressionType")>`string`</[CompressionType](API_InputSerialization.md#AmazonS3-Type-InputSerialization-CompressionType "API_InputSerialization.md#AmazonS3-Type-InputSerialization-CompressionType")>
         <[CSV](API_InputSerialization.md#AmazonS3-Type-InputSerialization-CSV "API_InputSerialization.md#AmazonS3-Type-InputSerialization-CSV")>
            <[AllowQuotedRecordDelimiter](API_CSVInput.md#AmazonS3-Type-CSVInput-AllowQuotedRecordDelimiter "API_CSVInput.md#AmazonS3-Type-CSVInput-AllowQuotedRecordDelimiter")>`boolean`</[AllowQuotedRecordDelimiter](API_CSVInput.md#AmazonS3-Type-CSVInput-AllowQuotedRecordDelimiter "API_CSVInput.md#AmazonS3-Type-CSVInput-AllowQuotedRecordDelimiter")>
            <[Comments](API_CSVInput.md#AmazonS3-Type-CSVInput-Comments "API_CSVInput.md#AmazonS3-Type-CSVInput-Comments")>`string`</[Comments](API_CSVInput.md#AmazonS3-Type-CSVInput-Comments "API_CSVInput.md#AmazonS3-Type-CSVInput-Comments")>
            <[FieldDelimiter](API_CSVInput.md#AmazonS3-Type-CSVInput-FieldDelimiter "API_CSVInput.md#AmazonS3-Type-CSVInput-FieldDelimiter")>`string`</[FieldDelimiter](API_CSVInput.md#AmazonS3-Type-CSVInput-FieldDelimiter "API_CSVInput.md#AmazonS3-Type-CSVInput-FieldDelimiter")>
            <[FileHeaderInfo](API_CSVInput.md#AmazonS3-Type-CSVInput-FileHeaderInfo "API_CSVInput.md#AmazonS3-Type-CSVInput-FileHeaderInfo")>`string`</[FileHeaderInfo](API_CSVInput.md#AmazonS3-Type-CSVInput-FileHeaderInfo "API_CSVInput.md#AmazonS3-Type-CSVInput-FileHeaderInfo")>
            <[QuoteCharacter](API_CSVInput.md#AmazonS3-Type-CSVInput-QuoteCharacter "API_CSVInput.md#AmazonS3-Type-CSVInput-QuoteCharacter")>`string`</[QuoteCharacter](API_CSVInput.md#AmazonS3-Type-CSVInput-QuoteCharacter "API_CSVInput.md#AmazonS3-Type-CSVInput-QuoteCharacter")>
            <[QuoteEscapeCharacter](API_CSVInput.md#AmazonS3-Type-CSVInput-QuoteEscapeCharacter "API_CSVInput.md#AmazonS3-Type-CSVInput-QuoteEscapeCharacter")>`string`</[QuoteEscapeCharacter](API_CSVInput.md#AmazonS3-Type-CSVInput-QuoteEscapeCharacter "API_CSVInput.md#AmazonS3-Type-CSVInput-QuoteEscapeCharacter")>
            <[RecordDelimiter](API_CSVInput.md#AmazonS3-Type-CSVInput-RecordDelimiter "API_CSVInput.md#AmazonS3-Type-CSVInput-RecordDelimiter")>`string`</[RecordDelimiter](API_CSVInput.md#AmazonS3-Type-CSVInput-RecordDelimiter "API_CSVInput.md#AmazonS3-Type-CSVInput-RecordDelimiter")>
         </[CSV](API_InputSerialization.md#AmazonS3-Type-InputSerialization-CSV "API_InputSerialization.md#AmazonS3-Type-InputSerialization-CSV")>
         <[JSON](API_InputSerialization.md#AmazonS3-Type-InputSerialization-JSON "API_InputSerialization.md#AmazonS3-Type-InputSerialization-JSON")>
            <[Type](API_JSONInput.md#AmazonS3-Type-JSONInput-Type "API_JSONInput.md#AmazonS3-Type-JSONInput-Type")>`string`</[Type](API_JSONInput.md#AmazonS3-Type-JSONInput-Type "API_JSONInput.md#AmazonS3-Type-JSONInput-Type")>
         </[JSON](API_InputSerialization.md#AmazonS3-Type-InputSerialization-JSON "API_InputSerialization.md#AmazonS3-Type-InputSerialization-JSON")>
         <[Parquet](API_InputSerialization.md#AmazonS3-Type-InputSerialization-Parquet "API_InputSerialization.md#AmazonS3-Type-InputSerialization-Parquet")>
         </[Parquet](API_InputSerialization.md#AmazonS3-Type-InputSerialization-Parquet "API_InputSerialization.md#AmazonS3-Type-InputSerialization-Parquet")>
      </[InputSerialization](API_SelectParameters.md#AmazonS3-Type-SelectParameters-InputSerialization "API_SelectParameters.md#AmazonS3-Type-SelectParameters-InputSerialization")>
      <[OutputSerialization](API_SelectParameters.md#AmazonS3-Type-SelectParameters-OutputSerialization "API_SelectParameters.md#AmazonS3-Type-SelectParameters-OutputSerialization")>
         <[CSV](API_OutputSerialization.md#AmazonS3-Type-OutputSerialization-CSV "API_OutputSerialization.md#AmazonS3-Type-OutputSerialization-CSV")>
            <[FieldDelimiter](API_CSVOutput.md#AmazonS3-Type-CSVOutput-FieldDelimiter "API_CSVOutput.md#AmazonS3-Type-CSVOutput-FieldDelimiter")>`string`</[FieldDelimiter](API_CSVOutput.md#AmazonS3-Type-CSVOutput-FieldDelimiter "API_CSVOutput.md#AmazonS3-Type-CSVOutput-FieldDelimiter")>
            <[QuoteCharacter](API_CSVOutput.md#AmazonS3-Type-CSVOutput-QuoteCharacter "API_CSVOutput.md#AmazonS3-Type-CSVOutput-QuoteCharacter")>`string`</[QuoteCharacter](API_CSVOutput.md#AmazonS3-Type-CSVOutput-QuoteCharacter "API_CSVOutput.md#AmazonS3-Type-CSVOutput-QuoteCharacter")>
            <[QuoteEscapeCharacter](API_CSVOutput.md#AmazonS3-Type-CSVOutput-QuoteEscapeCharacter "API_CSVOutput.md#AmazonS3-Type-CSVOutput-QuoteEscapeCharacter")>`string`</[QuoteEscapeCharacter](API_CSVOutput.md#AmazonS3-Type-CSVOutput-QuoteEscapeCharacter "API_CSVOutput.md#AmazonS3-Type-CSVOutput-QuoteEscapeCharacter")>
            <[QuoteFields](API_CSVOutput.md#AmazonS3-Type-CSVOutput-QuoteFields "API_CSVOutput.md#AmazonS3-Type-CSVOutput-QuoteFields")>`string`</[QuoteFields](API_CSVOutput.md#AmazonS3-Type-CSVOutput-QuoteFields "API_CSVOutput.md#AmazonS3-Type-CSVOutput-QuoteFields")>
            <[RecordDelimiter](API_CSVOutput.md#AmazonS3-Type-CSVOutput-RecordDelimiter "API_CSVOutput.md#AmazonS3-Type-CSVOutput-RecordDelimiter")>`string`</[RecordDelimiter](API_CSVOutput.md#AmazonS3-Type-CSVOutput-RecordDelimiter "API_CSVOutput.md#AmazonS3-Type-CSVOutput-RecordDelimiter")>
         </[CSV](API_OutputSerialization.md#AmazonS3-Type-OutputSerialization-CSV "API_OutputSerialization.md#AmazonS3-Type-OutputSerialization-CSV")>
         <[JSON](API_OutputSerialization.md#AmazonS3-Type-OutputSerialization-JSON "API_OutputSerialization.md#AmazonS3-Type-OutputSerialization-JSON")>
            <[RecordDelimiter](API_JSONOutput.md#AmazonS3-Type-JSONOutput-RecordDelimiter "API_JSONOutput.md#AmazonS3-Type-JSONOutput-RecordDelimiter")>`string`</[RecordDelimiter](API_JSONOutput.md#AmazonS3-Type-JSONOutput-RecordDelimiter "API_JSONOutput.md#AmazonS3-Type-JSONOutput-RecordDelimiter")>
         </[JSON](API_OutputSerialization.md#AmazonS3-Type-OutputSerialization-JSON "API_OutputSerialization.md#AmazonS3-Type-OutputSerialization-JSON")>
      </[OutputSerialization](API_SelectParameters.md#AmazonS3-Type-SelectParameters-OutputSerialization "API_SelectParameters.md#AmazonS3-Type-SelectParameters-OutputSerialization")>
   </[SelectParameters](#AmazonS3-RestoreObject-request-SelectParameters "#AmazonS3-RestoreObject-request-SelectParameters")>
   <[OutputLocation](#AmazonS3-RestoreObject-request-OutputLocation "#AmazonS3-RestoreObject-request-OutputLocation")>
      <[S3](API_OutputLocation.md#AmazonS3-Type-OutputLocation-S3 "API_OutputLocation.md#AmazonS3-Type-OutputLocation-S3")>
         <[AccessControlList](API_S3Location.md#AmazonS3-Type-S3Location-AccessControlList "API_S3Location.md#AmazonS3-Type-S3Location-AccessControlList")>
            <Grant>
               <[Grantee](API_Grant.md#AmazonS3-Type-Grant-Grantee "API_Grant.md#AmazonS3-Type-Grant-Grantee")>
                  <[DisplayName](API_Grantee.md#AmazonS3-Type-Grantee-DisplayName "API_Grantee.md#AmazonS3-Type-Grantee-DisplayName")>`string`</[DisplayName](API_Grantee.md#AmazonS3-Type-Grantee-DisplayName "API_Grantee.md#AmazonS3-Type-Grantee-DisplayName")>
                  <[EmailAddress](API_Grantee.md#AmazonS3-Type-Grantee-EmailAddress "API_Grantee.md#AmazonS3-Type-Grantee-EmailAddress")>`string`</[EmailAddress](API_Grantee.md#AmazonS3-Type-Grantee-EmailAddress "API_Grantee.md#AmazonS3-Type-Grantee-EmailAddress")>
                  <[ID](API_Grantee.md#AmazonS3-Type-Grantee-ID "API_Grantee.md#AmazonS3-Type-Grantee-ID")>`string`</[ID](API_Grantee.md#AmazonS3-Type-Grantee-ID "API_Grantee.md#AmazonS3-Type-Grantee-ID")>
                  <[xsi:type](API_Grantee.md#AmazonS3-Type-Grantee-Type "API_Grantee.md#AmazonS3-Type-Grantee-Type")>`string`</[xsi:type](API_Grantee.md#AmazonS3-Type-Grantee-Type "API_Grantee.md#AmazonS3-Type-Grantee-Type")>
                  <[URI](API_Grantee.md#AmazonS3-Type-Grantee-URI "API_Grantee.md#AmazonS3-Type-Grantee-URI")>`string`</[URI](API_Grantee.md#AmazonS3-Type-Grantee-URI "API_Grantee.md#AmazonS3-Type-Grantee-URI")>
               </[Grantee](API_Grant.md#AmazonS3-Type-Grant-Grantee "API_Grant.md#AmazonS3-Type-Grant-Grantee")>
               <[Permission](API_Grant.md#AmazonS3-Type-Grant-Permission "API_Grant.md#AmazonS3-Type-Grant-Permission")>`string`</[Permission](API_Grant.md#AmazonS3-Type-Grant-Permission "API_Grant.md#AmazonS3-Type-Grant-Permission")>
            </Grant>
         </[AccessControlList](API_S3Location.md#AmazonS3-Type-S3Location-AccessControlList "API_S3Location.md#AmazonS3-Type-S3Location-AccessControlList")>
         <[BucketName](API_S3Location.md#AmazonS3-Type-S3Location-BucketName "API_S3Location.md#AmazonS3-Type-S3Location-BucketName")>`string`</[BucketName](API_S3Location.md#AmazonS3-Type-S3Location-BucketName "API_S3Location.md#AmazonS3-Type-S3Location-BucketName")>
         <[CannedACL](API_S3Location.md#AmazonS3-Type-S3Location-CannedACL "API_S3Location.md#AmazonS3-Type-S3Location-CannedACL")>`string`</[CannedACL](API_S3Location.md#AmazonS3-Type-S3Location-CannedACL "API_S3Location.md#AmazonS3-Type-S3Location-CannedACL")>
         <[Encryption](API_S3Location.md#AmazonS3-Type-S3Location-Encryption "API_S3Location.md#AmazonS3-Type-S3Location-Encryption")>
            <[EncryptionType](API_Encryption.md#AmazonS3-Type-Encryption-EncryptionType "API_Encryption.md#AmazonS3-Type-Encryption-EncryptionType")>`string`</[EncryptionType](API_Encryption.md#AmazonS3-Type-Encryption-EncryptionType "API_Encryption.md#AmazonS3-Type-Encryption-EncryptionType")>
            <[KMSContext](API_Encryption.md#AmazonS3-Type-Encryption-KMSContext "API_Encryption.md#AmazonS3-Type-Encryption-KMSContext")>`string`</[KMSContext](API_Encryption.md#AmazonS3-Type-Encryption-KMSContext "API_Encryption.md#AmazonS3-Type-Encryption-KMSContext")>
            <[KMSKeyId](API_Encryption.md#AmazonS3-Type-Encryption-KMSKeyId "API_Encryption.md#AmazonS3-Type-Encryption-KMSKeyId")>`string`</[KMSKeyId](API_Encryption.md#AmazonS3-Type-Encryption-KMSKeyId "API_Encryption.md#AmazonS3-Type-Encryption-KMSKeyId")>
         </[Encryption](API_S3Location.md#AmazonS3-Type-S3Location-Encryption "API_S3Location.md#AmazonS3-Type-S3Location-Encryption")>
         <[Prefix](API_S3Location.md#AmazonS3-Type-S3Location-Prefix "API_S3Location.md#AmazonS3-Type-S3Location-Prefix")>`string`</[Prefix](API_S3Location.md#AmazonS3-Type-S3Location-Prefix "API_S3Location.md#AmazonS3-Type-S3Location-Prefix")>
         <[StorageClass](API_S3Location.md#AmazonS3-Type-S3Location-StorageClass "API_S3Location.md#AmazonS3-Type-S3Location-StorageClass")>`string`</[StorageClass](API_S3Location.md#AmazonS3-Type-S3Location-StorageClass "API_S3Location.md#AmazonS3-Type-S3Location-StorageClass")>
         <[Tagging](API_S3Location.md#AmazonS3-Type-S3Location-Tagging "API_S3Location.md#AmazonS3-Type-S3Location-Tagging")>
            <[TagSet](API_Tagging.md#AmazonS3-Type-Tagging-TagSet "API_Tagging.md#AmazonS3-Type-Tagging-TagSet")>
               <Tag>
                  <[Key](API_Tag.md#AmazonS3-Type-Tag-Key "API_Tag.md#AmazonS3-Type-Tag-Key")>`string`</[Key](API_Tag.md#AmazonS3-Type-Tag-Key "API_Tag.md#AmazonS3-Type-Tag-Key")>
                  <[Value](API_Tag.md#AmazonS3-Type-Tag-Value "API_Tag.md#AmazonS3-Type-Tag-Value")>`string`</[Value](API_Tag.md#AmazonS3-Type-Tag-Value "API_Tag.md#AmazonS3-Type-Tag-Value")>
               </Tag>
            </[TagSet](API_Tagging.md#AmazonS3-Type-Tagging-TagSet "API_Tagging.md#AmazonS3-Type-Tagging-TagSet")>
         </[Tagging](API_S3Location.md#AmazonS3-Type-S3Location-Tagging "API_S3Location.md#AmazonS3-Type-S3Location-Tagging")>
         <[UserMetadata](API_S3Location.md#AmazonS3-Type-S3Location-UserMetadata "API_S3Location.md#AmazonS3-Type-S3Location-UserMetadata")>
            <MetadataEntry>
               <[Name](API_MetadataEntry.md#AmazonS3-Type-MetadataEntry-Name "API_MetadataEntry.md#AmazonS3-Type-MetadataEntry-Name")>`string`</[Name](API_MetadataEntry.md#AmazonS3-Type-MetadataEntry-Name "API_MetadataEntry.md#AmazonS3-Type-MetadataEntry-Name")>
               <[Value](API_MetadataEntry.md#AmazonS3-Type-MetadataEntry-Value "API_MetadataEntry.md#AmazonS3-Type-MetadataEntry-Value")>`string`</[Value](API_MetadataEntry.md#AmazonS3-Type-MetadataEntry-Value "API_MetadataEntry.md#AmazonS3-Type-MetadataEntry-Value")>
            </MetadataEntry>
         </[UserMetadata](API_S3Location.md#AmazonS3-Type-S3Location-UserMetadata "API_S3Location.md#AmazonS3-Type-S3Location-UserMetadata")>
      </[S3](API_OutputLocation.md#AmazonS3-Type-OutputLocation-S3 "API_OutputLocation.md#AmazonS3-Type-OutputLocation-S3")>
   </[OutputLocation](#AmazonS3-RestoreObject-request-OutputLocation "#AmazonS3-RestoreObject-request-OutputLocation")>
</[RestoreRequest](#AmazonS3-RestoreObject-request-RestoreRequest "#AmazonS3-RestoreObject-request-RestoreRequest")>
```

## URI Request Parameters


The request uses the following URI parameters.





**[Bucket](#API_RestoreObject_RequestSyntax "#API_RestoreObject_RequestSyntax")**


The bucket name containing the object to restore. 



**Access points** - When you use this action with an access point for general purpose buckets, you must provide the alias of the access point in place of the bucket name or specify the access point ARN. When you use this action with an access point for directory buckets, you must provide the access point name in place of the bucket name. When using the access point ARN, you must direct requests to the access point hostname. The access point hostname takes the form *AccessPointName*-*AccountId*.s3-accesspoint.*Region*.amazonaws.com. When using this action with an access point through the AWS SDKs, you provide the access point ARN in place of the bucket name. For more information about access point ARNs, see [Using access points](../userguide/using-access-points.md "../userguide/using-access-points.md") in the *Amazon S3 User Guide*.



**S3 on Outposts** - When you use this action with S3 on Outposts, you must direct requests to the S3 on Outposts hostname. The S3 on Outposts hostname takes the 
 form `*AccessPointName*-*AccountId*.*outpostID*.s3-outposts.*Region*.amazonaws.com`. When you use this action with S3 on Outposts, the destination bucket must be the Outposts access point ARN or the access point alias. For more information about S3 on Outposts, see [What is S3 on Outposts?](../userguide/S3onOutposts.md "../userguide/S3onOutposts.md") in the *Amazon S3 User Guide*.


Required: Yes




**[Key](#API_RestoreObject_RequestSyntax "#API_RestoreObject_RequestSyntax")**


Object key for which the action was initiated.


Length Constraints: Minimum length of 1.


Required: Yes




**[versionId](#API_RestoreObject_RequestSyntax "#API_RestoreObject_RequestSyntax")**


VersionId used to reference a specific version of the object.




**[x-amz-expected-bucket-owner](#API_RestoreObject_RequestSyntax "#API_RestoreObject_RequestSyntax")**


The account ID of the expected bucket owner. If the account ID that you provide does not match the actual owner of the bucket, the request fails with the HTTP status code `403 Forbidden` (access denied).




**[x-amz-request-payer](#API_RestoreObject_RequestSyntax "#API_RestoreObject_RequestSyntax")**


Confirms that the requester knows that they will be charged for the request. Bucket owners need not
 specify this parameter in their requests. If either the source or destination S3 bucket has Requester
 Pays enabled, the requester will pay for corresponding charges to copy the object. For information about
 downloading objects from Requester Pays buckets, see [Downloading Objects in Requester Pays
 Buckets](https://docs.aws.amazon.com/AmazonS3/latest/dev/ObjectsinRequesterPaysBuckets.html "https://docs.aws.amazon.com/AmazonS3/latest/dev/ObjectsinRequesterPaysBuckets.html") in the *Amazon S3 User Guide*.


###### Note

This functionality is not supported for directory buckets.


Valid Values: `requester`





**[x-amz-sdk-checksum-algorithm](#API_RestoreObject_RequestSyntax "#API_RestoreObject_RequestSyntax")**


Indicates the algorithm used to create the checksum for the object when you use the SDK. This header will not provide any
 additional functionality if you don't use the SDK. When you send this header, there must be a corresponding `x-amz-checksum` or
 `x-amz-trailer` header sent. Otherwise, Amazon S3 fails the request with the HTTP status code `400 Bad Request`. For more
 information, see [Checking object integrity](../userguide/checking-object-integrity.md "../userguide/checking-object-integrity.md") in
 the *Amazon S3 User Guide*.


If you provide an individual checksum, Amazon S3 ignores any provided `ChecksumAlgorithm`
 parameter.


Valid Values: `CRC32 | CRC32C | SHA1 | SHA256 | CRC64NVME`





## Request Body


The request accepts the following data in XML format.





**[RestoreRequest](#API_RestoreObject_RequestSyntax "#API_RestoreObject_RequestSyntax")**


Root level tag for the RestoreRequest parameters.


Required: Yes




**[Days](#API_RestoreObject_RequestSyntax "#API_RestoreObject_RequestSyntax")**


Lifetime of the active copy in days. Do not use with restores that specify
 `OutputLocation`.


The Days element is required for regular restores, and must not be provided for select
 requests.


Type: Integer


Required: No




**[Description](#API_RestoreObject_RequestSyntax "#API_RestoreObject_RequestSyntax")**


The optional description for the job.


Type: String


Required: No




**[GlacierJobParameters](#API_RestoreObject_RequestSyntax "#API_RestoreObject_RequestSyntax")**


S3 Glacier related parameters pertaining to this job. Do not use with restores that specify
 `OutputLocation`.


Type: [GlacierJobParameters](API_GlacierJobParameters.md "API_GlacierJobParameters.md") data type


Required: No




**[OutputLocation](#API_RestoreObject_RequestSyntax "#API_RestoreObject_RequestSyntax")**


Describes the location where the restore job's output is stored.


Type: [OutputLocation](API_OutputLocation.md "API_OutputLocation.md") data type


Required: No




**[SelectParameters](#API_RestoreObject_RequestSyntax "#API_RestoreObject_RequestSyntax")**


###### Important

Amazon S3 Select is no longer available to new customers. Existing customers of Amazon S3 Select can
 continue to use the feature as usual. [Learn more](http://aws.amazon.com/blogs/storage/how-to-optimize-querying-your-data-in-amazon-s3/ "http://aws.amazon.com/blogs/storage/how-to-optimize-querying-your-data-in-amazon-s3/")



Describes the parameters for Select job types.


Type: [SelectParameters](API_SelectParameters.md "API_SelectParameters.md") data type


Required: No




**[Tier](#API_RestoreObject_RequestSyntax "#API_RestoreObject_RequestSyntax")**


Retrieval tier at which the restore will be processed.


Type: String


Valid Values: `Standard | Bulk | Expedited`



Required: No




**[Type](#API_RestoreObject_RequestSyntax "#API_RestoreObject_RequestSyntax")**


###### Important

Amazon S3 Select is no longer available to new customers. Existing customers of Amazon S3 Select can
 continue to use the feature as usual. [Learn more](http://aws.amazon.com/blogs/storage/how-to-optimize-querying-your-data-in-amazon-s3/ "http://aws.amazon.com/blogs/storage/how-to-optimize-querying-your-data-in-amazon-s3/")



Type of restore request.


Type: String


Valid Values: `SELECT`



Required: No




## Response Syntax



```
HTTP/1.1 200
x-amz-request-charged: `RequestCharged`
x-amz-restore-output-path: `RestoreOutputPath`

```

## Response Elements


If the action is successful, the service sends back an HTTP 200 response.


The response returns the following HTTP headers.





**[x-amz-request-charged](#API_RestoreObject_ResponseSyntax "#API_RestoreObject_ResponseSyntax")**


If present, indicates that the requester was successfully charged for the request. For more
 information, see [Using Requester Pays buckets for storage transfers and usage](../userguide/RequesterPaysBuckets.md "../userguide/RequesterPaysBuckets.md") in the *Amazon Simple
 Storage Service user guide*.


###### Note

This functionality is not supported for directory buckets.


Valid Values: `requester`





**[x-amz-restore-output-path](#API_RestoreObject_ResponseSyntax "#API_RestoreObject_ResponseSyntax")**


Indicates the path in the provided S3 output location where Select results will be restored
 to.




## Errors





**ObjectAlreadyInActiveTierError** 


This action is not allowed against this storage tier.


HTTP Status Code: 403




## Examples


### Example: Restore an object for 2 days using the expedited retrieval option


The following restore request restores a copy of the `photo1.jpg` object from
 S3 Glacier for a period of two days using the expedited retrieval option.



```

POST /photo1.jpg?restore HTTP/1.1
Host: examplebucket.dummy value
Date: Mon, 22 Oct 2012 01:49:52 GMT
Authorization: authorization string
Content-Length: content length
<RestoreRequest>
  <Days>2</Days>
  <GlacierJobParameters>
    <Tier>Standard</Tier>
  </GlacierJobParameters>
</RestoreRequest>
         
```

### Sample response


If the `examplebucket` does not have a restored copy of the object, Amazon S3 returns the
 following `202 Accepted` response. 


###### Note

If a copy of the object is already restored, Amazon S3 returns a `200 OK` response, and
 updates only the restored copy's expiry time.



```

HTTP/1.1 202 Accepted
x-amz-id-2: GFihv3y6+kE7KG11GEkQhU7/2/cHR3Yb2fCb2S04nxI423Dqwg2XiQ0B/UZlzYQvPiBlZNRcovw=
x-amz-request-id: 9F341CD3C4BA79E0
Date: Sat, 20 Oct 2012 23:54:05 GMT
Content-Length: 0
Server: AmazonS3
         
```

## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface](https://docs.aws.amazon.com/goto/cli2/s3-2006-03-01/RestoreObject "https://docs.aws.amazon.com/goto/cli2/s3-2006-03-01/RestoreObject")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/s3-2006-03-01/RestoreObject "https://docs.aws.amazon.com/goto/DotNetSDKV3/s3-2006-03-01/RestoreObject")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/RestoreObject "https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/RestoreObject")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/s3-2006-03-01/RestoreObject "https://docs.aws.amazon.com/goto/SdkForGoV2/s3-2006-03-01/RestoreObject")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/RestoreObject "https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/RestoreObject")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3-2006-03-01/RestoreObject "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3-2006-03-01/RestoreObject")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/s3-2006-03-01/RestoreObject "https://docs.aws.amazon.com/goto/SdkForKotlin/s3-2006-03-01/RestoreObject")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/s3-2006-03-01/RestoreObject "https://docs.aws.amazon.com/goto/SdkForPHPV3/s3-2006-03-01/RestoreObject")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/s3-2006-03-01/RestoreObject "https://docs.aws.amazon.com/goto/boto3/s3-2006-03-01/RestoreObject")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/RestoreObject "https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/RestoreObject")
