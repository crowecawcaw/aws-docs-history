# GetBucketLogging

###### Important

End of support notice: Beginning November 21, 2025, Amazon S3 will stop returning `DisplayName`. Update your applications to use canonical IDs (unique identifier for 
 AWS accounts), AWS account ID (12 digit identifier) or IAM ARNs (full resource naming) as a direct replacement of `DisplayName`.


Between July 15, 2025 and November 21, 2025, you will begin to see an increasing rate of missing `DisplayName` in the Owner object.

This change affects the following AWS Regions: US East (N. Virginia) Region, US West (N. California) Region, US West (Oregon) Region, Asia Pacific (Singapore) Region, Asia Pacific (Sydney) Region, 
 Asia Pacific (Tokyo) Region, Europe (Ireland) Region, and South America (São Paulo) Region.

###### Note

This operation is not supported for directory buckets.

Returns the logging status of a bucket and the permissions users have to view and modify that
 status.

The following operations are related to `GetBucketLogging`:


* [CreateBucket](API_CreateBucket.md "API_CreateBucket.md")
* [PutBucketLogging](API_PutBucketLogging.md "API_PutBucketLogging.md")
###### Important

You must URL encode any signed header values that contain spaces. For example, if your header value is `my file.txt`, containing two spaces after `my`, you must URL encode this value to `my%20%20file.txt`.


## Request Syntax



```
GET /?logging HTTP/1.1
Host: `Bucket`.s3.amazonaws.com
x-amz-expected-bucket-owner: `ExpectedBucketOwner`

```

## URI Request Parameters


The request uses the following URI parameters.





**[Bucket](#API_GetBucketLogging_RequestSyntax "#API_GetBucketLogging_RequestSyntax")**


The bucket name for which to get the logging information.


Required: Yes




**[x-amz-expected-bucket-owner](#API_GetBucketLogging_RequestSyntax "#API_GetBucketLogging_RequestSyntax")**


The account ID of the expected bucket owner. If the account ID that you provide does not match the actual owner of the bucket, the request fails with the HTTP status code `403 Forbidden` (access denied).




## Request Body


The request does not have a request body.


## Response Syntax



```
HTTP/1.1 200
<?xml version="1.0" encoding="UTF-8"?>
<[BucketLoggingStatus](#AmazonS3-GetBucketLogging-response-GetBucketLoggingOutput "#AmazonS3-GetBucketLogging-response-GetBucketLoggingOutput")>
   <[LoggingEnabled](#AmazonS3-GetBucketLogging-response-LoggingEnabled "#AmazonS3-GetBucketLogging-response-LoggingEnabled")>
      <[TargetBucket](API_LoggingEnabled.md#AmazonS3-Type-LoggingEnabled-TargetBucket "API_LoggingEnabled.md#AmazonS3-Type-LoggingEnabled-TargetBucket")>***string***</[TargetBucket](API_LoggingEnabled.md#AmazonS3-Type-LoggingEnabled-TargetBucket "API_LoggingEnabled.md#AmazonS3-Type-LoggingEnabled-TargetBucket")>
      <[TargetGrants](API_LoggingEnabled.md#AmazonS3-Type-LoggingEnabled-TargetGrants "API_LoggingEnabled.md#AmazonS3-Type-LoggingEnabled-TargetGrants")>
         <Grant>
            <[Grantee](API_TargetGrant.md#AmazonS3-Type-TargetGrant-Grantee "API_TargetGrant.md#AmazonS3-Type-TargetGrant-Grantee")>
               <[DisplayName](API_Grantee.md#AmazonS3-Type-Grantee-DisplayName "API_Grantee.md#AmazonS3-Type-Grantee-DisplayName")>***string***</[DisplayName](API_Grantee.md#AmazonS3-Type-Grantee-DisplayName "API_Grantee.md#AmazonS3-Type-Grantee-DisplayName")>
               <[EmailAddress](API_Grantee.md#AmazonS3-Type-Grantee-EmailAddress "API_Grantee.md#AmazonS3-Type-Grantee-EmailAddress")>***string***</[EmailAddress](API_Grantee.md#AmazonS3-Type-Grantee-EmailAddress "API_Grantee.md#AmazonS3-Type-Grantee-EmailAddress")>
               <[ID](API_Grantee.md#AmazonS3-Type-Grantee-ID "API_Grantee.md#AmazonS3-Type-Grantee-ID")>***string***</[ID](API_Grantee.md#AmazonS3-Type-Grantee-ID "API_Grantee.md#AmazonS3-Type-Grantee-ID")>
               <[xsi:type](API_Grantee.md#AmazonS3-Type-Grantee-Type "API_Grantee.md#AmazonS3-Type-Grantee-Type")>***string***</[xsi:type](API_Grantee.md#AmazonS3-Type-Grantee-Type "API_Grantee.md#AmazonS3-Type-Grantee-Type")>
               <[URI](API_Grantee.md#AmazonS3-Type-Grantee-URI "API_Grantee.md#AmazonS3-Type-Grantee-URI")>***string***</[URI](API_Grantee.md#AmazonS3-Type-Grantee-URI "API_Grantee.md#AmazonS3-Type-Grantee-URI")>
            </[Grantee](API_TargetGrant.md#AmazonS3-Type-TargetGrant-Grantee "API_TargetGrant.md#AmazonS3-Type-TargetGrant-Grantee")>
            <[Permission](API_TargetGrant.md#AmazonS3-Type-TargetGrant-Permission "API_TargetGrant.md#AmazonS3-Type-TargetGrant-Permission")>***string***</[Permission](API_TargetGrant.md#AmazonS3-Type-TargetGrant-Permission "API_TargetGrant.md#AmazonS3-Type-TargetGrant-Permission")>
         </Grant>
      </[TargetGrants](API_LoggingEnabled.md#AmazonS3-Type-LoggingEnabled-TargetGrants "API_LoggingEnabled.md#AmazonS3-Type-LoggingEnabled-TargetGrants")>
      <[TargetObjectKeyFormat](API_LoggingEnabled.md#AmazonS3-Type-LoggingEnabled-TargetObjectKeyFormat "API_LoggingEnabled.md#AmazonS3-Type-LoggingEnabled-TargetObjectKeyFormat")>
         <[PartitionedPrefix](API_TargetObjectKeyFormat.md#AmazonS3-Type-TargetObjectKeyFormat-PartitionedPrefix "API_TargetObjectKeyFormat.md#AmazonS3-Type-TargetObjectKeyFormat-PartitionedPrefix")>
            <[PartitionDateSource](API_PartitionedPrefix.md#AmazonS3-Type-PartitionedPrefix-PartitionDateSource "API_PartitionedPrefix.md#AmazonS3-Type-PartitionedPrefix-PartitionDateSource")>***string***</[PartitionDateSource](API_PartitionedPrefix.md#AmazonS3-Type-PartitionedPrefix-PartitionDateSource "API_PartitionedPrefix.md#AmazonS3-Type-PartitionedPrefix-PartitionDateSource")>
         </[PartitionedPrefix](API_TargetObjectKeyFormat.md#AmazonS3-Type-TargetObjectKeyFormat-PartitionedPrefix "API_TargetObjectKeyFormat.md#AmazonS3-Type-TargetObjectKeyFormat-PartitionedPrefix")>
         <[SimplePrefix](API_TargetObjectKeyFormat.md#AmazonS3-Type-TargetObjectKeyFormat-SimplePrefix "API_TargetObjectKeyFormat.md#AmazonS3-Type-TargetObjectKeyFormat-SimplePrefix")>
         </[SimplePrefix](API_TargetObjectKeyFormat.md#AmazonS3-Type-TargetObjectKeyFormat-SimplePrefix "API_TargetObjectKeyFormat.md#AmazonS3-Type-TargetObjectKeyFormat-SimplePrefix")>
      </[TargetObjectKeyFormat](API_LoggingEnabled.md#AmazonS3-Type-LoggingEnabled-TargetObjectKeyFormat "API_LoggingEnabled.md#AmazonS3-Type-LoggingEnabled-TargetObjectKeyFormat")>
      <[TargetPrefix](API_LoggingEnabled.md#AmazonS3-Type-LoggingEnabled-TargetPrefix "API_LoggingEnabled.md#AmazonS3-Type-LoggingEnabled-TargetPrefix")>***string***</[TargetPrefix](API_LoggingEnabled.md#AmazonS3-Type-LoggingEnabled-TargetPrefix "API_LoggingEnabled.md#AmazonS3-Type-LoggingEnabled-TargetPrefix")>
   </[LoggingEnabled](#AmazonS3-GetBucketLogging-response-LoggingEnabled "#AmazonS3-GetBucketLogging-response-LoggingEnabled")>
</[BucketLoggingStatus](#AmazonS3-GetBucketLogging-response-GetBucketLoggingOutput "#AmazonS3-GetBucketLogging-response-GetBucketLoggingOutput")>
```

## Response Elements


If the action is successful, the service sends back an HTTP 200 response.


The following data is returned in XML format by the service.





**[BucketLoggingStatus](#API_GetBucketLogging_ResponseSyntax "#API_GetBucketLogging_ResponseSyntax")**


Root level tag for the BucketLoggingStatus parameters.


Required: Yes




**[LoggingEnabled](#API_GetBucketLogging_ResponseSyntax "#API_GetBucketLogging_ResponseSyntax")**


Describes where logs are stored and the prefix that Amazon S3 assigns to all log object keys for a
 bucket. For more information, see [PUT Bucket logging](RESTBucketPUTlogging.md "RESTBucketPUTlogging.md") in the
 *Amazon S3 API Reference*.


Type: [LoggingEnabled](API_LoggingEnabled.md "API_LoggingEnabled.md") data type




## Examples


### Sample Request


The following request returns the logging status for `amzn-s3-demo-bucket`.



```

            GET ?logging HTTP/1.1
            Host: amzn-s3-demo-bucket.s3.<Region>.amazonaws.com
            Date: Wed, 25 Nov 2009 12:00:00 GMT
            Authorization: authorization string
         
```

### Sample Response: Showing an enabled logging status


This example illustrates one usage of GetBucketLogging.



```

            HTTP/1.1 200 OK
            Date: Wed, 25 Nov 2009 12:00:00 GMT
            Connection: close
            Server: AmazonS3

            <?xml version="1.0" encoding="UTF-8"?>
            <BucketLoggingStatus xmlns="http://doc.s3.amazonaws.com/2006-03-01">
             <LoggingEnabled>
              <TargetBucket>amzn-s3-demo-bucket</TargetBucket>
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

### Sample Response: Showing a disabled logging status


This example illustrates one usage of GetBucketLogging.



```

         HTTP/1.1 200 OK
         Date: Wed, 25 Nov 2009 12:00:00 GMT
         Connection: close
         Server: AmazonS3

         <?xml version="1.0" encoding="UTF-8"?>
         <BucketLoggingStatus xmlns="http://doc.s3.amazonaws.com/2006-03-01" />
         
```

## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface](https://docs.aws.amazon.com/goto/cli2/s3-2006-03-01/GetBucketLogging "https://docs.aws.amazon.com/goto/cli2/s3-2006-03-01/GetBucketLogging")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/s3-2006-03-01/GetBucketLogging "https://docs.aws.amazon.com/goto/DotNetSDKV3/s3-2006-03-01/GetBucketLogging")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/GetBucketLogging "https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/GetBucketLogging")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/s3-2006-03-01/GetBucketLogging "https://docs.aws.amazon.com/goto/SdkForGoV2/s3-2006-03-01/GetBucketLogging")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/GetBucketLogging "https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/GetBucketLogging")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3-2006-03-01/GetBucketLogging "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3-2006-03-01/GetBucketLogging")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/s3-2006-03-01/GetBucketLogging "https://docs.aws.amazon.com/goto/SdkForKotlin/s3-2006-03-01/GetBucketLogging")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/s3-2006-03-01/GetBucketLogging "https://docs.aws.amazon.com/goto/SdkForPHPV3/s3-2006-03-01/GetBucketLogging")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/s3-2006-03-01/GetBucketLogging "https://docs.aws.amazon.com/goto/boto3/s3-2006-03-01/GetBucketLogging")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/GetBucketLogging "https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/GetBucketLogging")
