# PutBucketLogging

###### Important

End of support notice: As of October 1, 2025, Amazon S3 has discontinued support for Email Grantee Access Control Lists (ACLs). If you attempt to use an Email Grantee ACL in a request after October 1, 2025, 
 the request will receive an `HTTP 405` (Method Not Allowed) error.

This change affects the following AWS Regions: US East (N. Virginia), US West (N. California), US West (Oregon), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Tokyo), Europe (Ireland), and South America (São Paulo).

###### Note

This operation is not supported for directory buckets.

Set the logging parameters for a bucket and to specify permissions for who can view and modify the
 logging parameters. All logs are saved to buckets in the same AWS Region as the source bucket. To set
 the logging status of a bucket, you must be the bucket owner.

The bucket owner is automatically granted FULL\_CONTROL to all logs. You use the `Grantee`
 request element to grant access to other people. The `Permissions` request element specifies
 the kind of access the grantee has to the logs.

###### Important

If the target bucket for log delivery uses the bucket owner enforced setting for S3 Object
 Ownership, you can't use the `Grantee` request element to grant access to others.
 Permissions can only be granted using policies. For more information, see [Permissions for server access log delivery](../userguide/enable-server-access-logging.md#grant-log-delivery-permissions-general "../userguide/enable-server-access-logging.md#grant-log-delivery-permissions-general") in the
 *Amazon S3 User Guide*.



Grantee Values

You can specify the person (grantee) to whom you're assigning access rights (by using request
 elements) in the following ways. For examples of how to specify these grantee values in JSON
 format, see the AWS CLI example in  [Enabling Amazon S3 server
 access logging](../userguide/enable-server-access-logging.md "../userguide/enable-server-access-logging.md") in the *Amazon S3 User Guide*.



* By the person's ID:



`<Grantee xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
 xsi:type="CanonicalUser"><ID><>ID<></ID><DisplayName><>GranteesEmail<></DisplayName>
 </Grantee>`




`DisplayName` is optional and ignored in the request.
* By Email address:



 `<Grantee xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
 xsi:type="AmazonCustomerByEmail"><EmailAddress><>Grantees@email.com<></EmailAddress></Grantee>`



The grantee is resolved to the `CanonicalUser` and, in a response to a
 `GETObjectAcl` request, appears as the CanonicalUser.
* By URI:



`<Grantee xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
 xsi:type="Group"><URI><>http://acs.amazonaws.com/groups/global/AuthenticatedUsers<></URI></Grantee>`


To enable logging, you use `LoggingEnabled` and its children request elements. To disable
 logging, you use an empty `BucketLoggingStatus` request element:


`<BucketLoggingStatus xmlns="http://doc.s3.amazonaws.com/2006-03-01" />`


For more information about server access logging, see [Server Access Logging](../userguide/ServerLogs.md "../userguide/ServerLogs.md") in the
 *Amazon S3 User Guide*. 

For more information about creating a bucket, see [CreateBucket](API_CreateBucket.md "API_CreateBucket.md"). For more information about
 returning the logging status of a bucket, see [GetBucketLogging](API_GetBucketLogging.md "API_GetBucketLogging.md").

The following operations are related to `PutBucketLogging`:


* [PutObject](API_PutObject.md "API_PutObject.md")
* [DeleteBucket](API_DeleteBucket.md "API_DeleteBucket.md")
* [CreateBucket](API_CreateBucket.md "API_CreateBucket.md")
* [GetBucketLogging](API_GetBucketLogging.md "API_GetBucketLogging.md")
###### Important

You must URL encode any signed header values that contain spaces. For example, if your header value is `my file.txt`, containing two spaces after `my`, you must URL encode this value to `my%20%20file.txt`.


## Request Syntax



```
PUT /?logging HTTP/1.1
Host: `Bucket`.s3.amazonaws.com
Content-MD5: `ContentMD5`
x-amz-sdk-checksum-algorithm: `ChecksumAlgorithm`
x-amz-expected-bucket-owner: `ExpectedBucketOwner`
<?xml version="1.0" encoding="UTF-8"?>
<[BucketLoggingStatus](#AmazonS3-PutBucketLogging-request-BucketLoggingStatus "#AmazonS3-PutBucketLogging-request-BucketLoggingStatus") xmlns="http://s3.amazonaws.com/doc/2006-03-01/">
   <[LoggingEnabled](#AmazonS3-PutBucketLogging-request-LoggingEnabled "#AmazonS3-PutBucketLogging-request-LoggingEnabled")>
      <[TargetBucket](API_LoggingEnabled.md#AmazonS3-Type-LoggingEnabled-TargetBucket "API_LoggingEnabled.md#AmazonS3-Type-LoggingEnabled-TargetBucket")>`string`</[TargetBucket](API_LoggingEnabled.md#AmazonS3-Type-LoggingEnabled-TargetBucket "API_LoggingEnabled.md#AmazonS3-Type-LoggingEnabled-TargetBucket")>
      <[TargetGrants](API_LoggingEnabled.md#AmazonS3-Type-LoggingEnabled-TargetGrants "API_LoggingEnabled.md#AmazonS3-Type-LoggingEnabled-TargetGrants")>
         <Grant>
            <[Grantee](API_TargetGrant.md#AmazonS3-Type-TargetGrant-Grantee "API_TargetGrant.md#AmazonS3-Type-TargetGrant-Grantee")>
               <[DisplayName](API_Grantee.md#AmazonS3-Type-Grantee-DisplayName "API_Grantee.md#AmazonS3-Type-Grantee-DisplayName")>`string`</[DisplayName](API_Grantee.md#AmazonS3-Type-Grantee-DisplayName "API_Grantee.md#AmazonS3-Type-Grantee-DisplayName")>
               <[EmailAddress](API_Grantee.md#AmazonS3-Type-Grantee-EmailAddress "API_Grantee.md#AmazonS3-Type-Grantee-EmailAddress")>`string`</[EmailAddress](API_Grantee.md#AmazonS3-Type-Grantee-EmailAddress "API_Grantee.md#AmazonS3-Type-Grantee-EmailAddress")>
               <[ID](API_Grantee.md#AmazonS3-Type-Grantee-ID "API_Grantee.md#AmazonS3-Type-Grantee-ID")>`string`</[ID](API_Grantee.md#AmazonS3-Type-Grantee-ID "API_Grantee.md#AmazonS3-Type-Grantee-ID")>
               <[xsi:type](API_Grantee.md#AmazonS3-Type-Grantee-Type "API_Grantee.md#AmazonS3-Type-Grantee-Type")>`string`</[xsi:type](API_Grantee.md#AmazonS3-Type-Grantee-Type "API_Grantee.md#AmazonS3-Type-Grantee-Type")>
               <[URI](API_Grantee.md#AmazonS3-Type-Grantee-URI "API_Grantee.md#AmazonS3-Type-Grantee-URI")>`string`</[URI](API_Grantee.md#AmazonS3-Type-Grantee-URI "API_Grantee.md#AmazonS3-Type-Grantee-URI")>
            </[Grantee](API_TargetGrant.md#AmazonS3-Type-TargetGrant-Grantee "API_TargetGrant.md#AmazonS3-Type-TargetGrant-Grantee")>
            <[Permission](API_TargetGrant.md#AmazonS3-Type-TargetGrant-Permission "API_TargetGrant.md#AmazonS3-Type-TargetGrant-Permission")>`string`</[Permission](API_TargetGrant.md#AmazonS3-Type-TargetGrant-Permission "API_TargetGrant.md#AmazonS3-Type-TargetGrant-Permission")>
         </Grant>
      </[TargetGrants](API_LoggingEnabled.md#AmazonS3-Type-LoggingEnabled-TargetGrants "API_LoggingEnabled.md#AmazonS3-Type-LoggingEnabled-TargetGrants")>
      <[TargetObjectKeyFormat](API_LoggingEnabled.md#AmazonS3-Type-LoggingEnabled-TargetObjectKeyFormat "API_LoggingEnabled.md#AmazonS3-Type-LoggingEnabled-TargetObjectKeyFormat")>
         <[PartitionedPrefix](API_TargetObjectKeyFormat.md#AmazonS3-Type-TargetObjectKeyFormat-PartitionedPrefix "API_TargetObjectKeyFormat.md#AmazonS3-Type-TargetObjectKeyFormat-PartitionedPrefix")>
            <[PartitionDateSource](API_PartitionedPrefix.md#AmazonS3-Type-PartitionedPrefix-PartitionDateSource "API_PartitionedPrefix.md#AmazonS3-Type-PartitionedPrefix-PartitionDateSource")>`string`</[PartitionDateSource](API_PartitionedPrefix.md#AmazonS3-Type-PartitionedPrefix-PartitionDateSource "API_PartitionedPrefix.md#AmazonS3-Type-PartitionedPrefix-PartitionDateSource")>
         </[PartitionedPrefix](API_TargetObjectKeyFormat.md#AmazonS3-Type-TargetObjectKeyFormat-PartitionedPrefix "API_TargetObjectKeyFormat.md#AmazonS3-Type-TargetObjectKeyFormat-PartitionedPrefix")>
         <[SimplePrefix](API_TargetObjectKeyFormat.md#AmazonS3-Type-TargetObjectKeyFormat-SimplePrefix "API_TargetObjectKeyFormat.md#AmazonS3-Type-TargetObjectKeyFormat-SimplePrefix")>
         </[SimplePrefix](API_TargetObjectKeyFormat.md#AmazonS3-Type-TargetObjectKeyFormat-SimplePrefix "API_TargetObjectKeyFormat.md#AmazonS3-Type-TargetObjectKeyFormat-SimplePrefix")>
      </[TargetObjectKeyFormat](API_LoggingEnabled.md#AmazonS3-Type-LoggingEnabled-TargetObjectKeyFormat "API_LoggingEnabled.md#AmazonS3-Type-LoggingEnabled-TargetObjectKeyFormat")>
      <[TargetPrefix](API_LoggingEnabled.md#AmazonS3-Type-LoggingEnabled-TargetPrefix "API_LoggingEnabled.md#AmazonS3-Type-LoggingEnabled-TargetPrefix")>`string`</[TargetPrefix](API_LoggingEnabled.md#AmazonS3-Type-LoggingEnabled-TargetPrefix "API_LoggingEnabled.md#AmazonS3-Type-LoggingEnabled-TargetPrefix")>
   </[LoggingEnabled](#AmazonS3-PutBucketLogging-request-LoggingEnabled "#AmazonS3-PutBucketLogging-request-LoggingEnabled")>
</[BucketLoggingStatus](#AmazonS3-PutBucketLogging-request-BucketLoggingStatus "#AmazonS3-PutBucketLogging-request-BucketLoggingStatus")>
```

## URI Request Parameters


The request uses the following URI parameters.





**[Bucket](#API_PutBucketLogging_RequestSyntax "#API_PutBucketLogging_RequestSyntax")**


The name of the bucket for which to set the logging parameters.


Required: Yes




**[Content-MD5](#API_PutBucketLogging_RequestSyntax "#API_PutBucketLogging_RequestSyntax")**


The MD5 hash of the `PutBucketLogging` request body.


For requests made using the AWS Command Line Interface (CLI) or AWS SDKs, this field is calculated automatically.




**[x-amz-expected-bucket-owner](#API_PutBucketLogging_RequestSyntax "#API_PutBucketLogging_RequestSyntax")**


The account ID of the expected bucket owner. If the account ID that you provide does not match the actual owner of the bucket, the request fails with the HTTP status code `403 Forbidden` (access denied).




**[x-amz-sdk-checksum-algorithm](#API_PutBucketLogging_RequestSyntax "#API_PutBucketLogging_RequestSyntax")**


Indicates the algorithm used to create the checksum for the request when you use the SDK. This header will not provide any
 additional functionality if you don't use the SDK. When you send this header, there must be a corresponding `x-amz-checksum` or
 `x-amz-trailer` header sent. Otherwise, Amazon S3 fails the request with the HTTP status code `400 Bad Request`. For more
 information, see [Checking object integrity](../userguide/checking-object-integrity.md "../userguide/checking-object-integrity.md") in
 the *Amazon S3 User Guide*.


If you provide an individual checksum, Amazon S3 ignores any provided `ChecksumAlgorithm`
 parameter.


Valid Values: `CRC32 | CRC32C | SHA1 | SHA256 | CRC64NVME`





## Request Body


The request accepts the following data in XML format.





**[BucketLoggingStatus](#API_PutBucketLogging_RequestSyntax "#API_PutBucketLogging_RequestSyntax")**


Root level tag for the BucketLoggingStatus parameters.


Required: Yes




**[LoggingEnabled](#API_PutBucketLogging_RequestSyntax "#API_PutBucketLogging_RequestSyntax")**


Describes where logs are stored and the prefix that Amazon S3 assigns to all log object keys for a
 bucket. For more information, see [PUT Bucket logging](RESTBucketPUTlogging.md "RESTBucketPUTlogging.md") in the
 *Amazon S3 API Reference*.


Type: [LoggingEnabled](API_LoggingEnabled.md "API_LoggingEnabled.md") data type


Required: No




## Response Syntax



```
HTTP/1.1 200

```

## Response Elements


If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.


## Examples


### Sample Request


This request enables logging and gives the grantee of the bucket READ access to the logs.


Buckets that use the bucket owner enforced setting for Object Ownership to disable ACLs don't
 support target grants. For more information, see [Permissions for server access log delivery](../userguide/enable-server-access-logging.md#grant-log-delivery-permissions-general "../userguide/enable-server-access-logging.md#grant-log-delivery-permissions-general") in the
 *Amazon S3 User Guide*.



```

PUT ?logging HTTP/1.1
Host: quotes.s3.<Region>.amazonaws.com
Content-Length: 214
Date: Wed, 25 Nov 2009 12:00:00 GMT
Authorization: authorization string

<?xml version="1.0" encoding="UTF-8"?>
<BucketLoggingStatus xmlns="http://doc.s3.amazonaws.com/2006-03-01">
  <LoggingEnabled>
    <TargetBucket>mybucketlogs</TargetBucket>
    <TargetPrefix>mybucket-access_log-/</TargetPrefix>
    <TargetGrants>
      <Grant>
        <Grantee xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
          xsi:type="AmazonCustomerByEmail">
          <EmailAddress>user@company.com</EmailAddress>
        </Grantee>
        <Permission>READ</Permission>
      </Grant>
    </TargetGrants>
  </LoggingEnabled>
</BucketLoggingStatus>
         
```

### Sample Response


This example illustrates one usage of PutBucketLogging.



```

HTTP/1.1 200 OK
x-amz-id-2: YgIPIfBiKa2bj0KMg95r/0zo3emzU4dzsD4rcKCHQUAdQkf3ShJTOOpXUueF6QKo
x-amz-request-id: 236A8905248E5A01
Date: Wed, 01 Mar  2006 12:00:00 GMT
         
```

### Sample Request: Disabling logging


This request disables logging on the bucket `quotes`.



```

PUT ?logging HTTP/1.1
Host: quotes.s3.<Region>.amazonaws.com
Content-Length: 214
Date: Wed, 25 Nov 2009 12:00:00 GMT
Authorization: authorization string

<?xml version="1.0" encoding="UTF-8"?>
<BucketLoggingStatus xmlns="http://doc.s3.amazonaws.com/2006-03-01" />
         
```

### Sample Response


This example illustrates one usage of PutBucketLogging.



```

HTTP/1.1 200 OK
x-amz-id-2: YgIPIfBiKa2bj0KMg95r/0zo3emzU4dzsD4rcKCHQUAdQkf3ShJTOOpXUueF6QKo
x-amz-request-id: 236A8905248E5A01
Date: Wed, 01 Mar  2006 12:00:00 GMT
         
```

## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface](https://docs.aws.amazon.com/goto/cli2/s3-2006-03-01/PutBucketLogging "https://docs.aws.amazon.com/goto/cli2/s3-2006-03-01/PutBucketLogging")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/s3-2006-03-01/PutBucketLogging "https://docs.aws.amazon.com/goto/DotNetSDKV3/s3-2006-03-01/PutBucketLogging")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/PutBucketLogging "https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/PutBucketLogging")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/s3-2006-03-01/PutBucketLogging "https://docs.aws.amazon.com/goto/SdkForGoV2/s3-2006-03-01/PutBucketLogging")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/PutBucketLogging "https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/PutBucketLogging")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3-2006-03-01/PutBucketLogging "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3-2006-03-01/PutBucketLogging")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/s3-2006-03-01/PutBucketLogging "https://docs.aws.amazon.com/goto/SdkForKotlin/s3-2006-03-01/PutBucketLogging")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/s3-2006-03-01/PutBucketLogging "https://docs.aws.amazon.com/goto/SdkForPHPV3/s3-2006-03-01/PutBucketLogging")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/s3-2006-03-01/PutBucketLogging "https://docs.aws.amazon.com/goto/boto3/s3-2006-03-01/PutBucketLogging")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/PutBucketLogging "https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/PutBucketLogging")
