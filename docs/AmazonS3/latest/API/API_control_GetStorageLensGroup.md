# GetStorageLensGroup


Retrieves the Storage Lens group configuration details.

To use this operation, you must have the permission to perform the
 `s3:GetStorageLensGroup` action. For more information about the required Storage Lens
 Groups permissions, see [Setting account permissions to use S3 Storage Lens groups](../userguide/storage_lens_iam_permissions.md#storage_lens_groups_permissions "../userguide/storage_lens_iam_permissions.md#storage_lens_groups_permissions").

For information about Storage Lens groups errors, see [List of Amazon S3 Storage
 Lens error codes](ErrorResponses.md#S3LensErrorCodeList "ErrorResponses.md#S3LensErrorCodeList").

###### Important

You must URL encode any signed header values that contain spaces. For example, if your header value is `my file.txt`, containing two spaces after `my`, you must URL encode this value to `my%20%20file.txt`.


## Request Syntax



```
GET /v20180820/storagelensgroup/`name` HTTP/1.1
Host: s3-control.amazonaws.com
x-amz-account-id: `AccountId`

```

## URI Request Parameters


The request uses the following URI parameters.





**[name](#API_control_GetStorageLensGroup_RequestSyntax "#API_control_GetStorageLensGroup_RequestSyntax")**



The name of the Storage Lens group that you're trying to retrieve the configuration details for.



Length Constraints: Minimum length of 1. Maximum length of 64.


Pattern: `[a-zA-Z0-9\-\_]+`



Required: Yes




**[x-amz-account-id](#API_control_GetStorageLensGroup_RequestSyntax "#API_control_GetStorageLensGroup_RequestSyntax")**



The AWS account ID associated with the Storage Lens group that you're trying to retrieve the details for.



Length Constraints: Maximum length of 64.


Pattern: `^\d{12}$`



Required: Yes




## Request Body


The request does not have a request body.


## Response Syntax



```
HTTP/1.1 200
<?xml version="1.0" encoding="UTF-8"?>
<[StorageLensGroup](#AmazonS3-control_GetStorageLensGroup-response-StorageLensGroup "#AmazonS3-control_GetStorageLensGroup-response-StorageLensGroup")>
   <[Name](#AmazonS3-control_GetStorageLensGroup-response-Name "#AmazonS3-control_GetStorageLensGroup-response-Name")>***string***</[Name](#AmazonS3-control_GetStorageLensGroup-response-Name "#AmazonS3-control_GetStorageLensGroup-response-Name")>
   <[Filter](#AmazonS3-control_GetStorageLensGroup-response-Filter "#AmazonS3-control_GetStorageLensGroup-response-Filter")>
      <[And](API_control_StorageLensGroupFilter.md#AmazonS3-Type-control_StorageLensGroupFilter-And "API_control_StorageLensGroupFilter.md#AmazonS3-Type-control_StorageLensGroupFilter-And")>
         <[MatchAnyPrefix](API_control_StorageLensGroupAndOperator.md#AmazonS3-Type-control_StorageLensGroupAndOperator-MatchAnyPrefix "API_control_StorageLensGroupAndOperator.md#AmazonS3-Type-control_StorageLensGroupAndOperator-MatchAnyPrefix")>
            <Prefix>***string***</Prefix>
         </[MatchAnyPrefix](API_control_StorageLensGroupAndOperator.md#AmazonS3-Type-control_StorageLensGroupAndOperator-MatchAnyPrefix "API_control_StorageLensGroupAndOperator.md#AmazonS3-Type-control_StorageLensGroupAndOperator-MatchAnyPrefix")>
         <[MatchAnySuffix](API_control_StorageLensGroupAndOperator.md#AmazonS3-Type-control_StorageLensGroupAndOperator-MatchAnySuffix "API_control_StorageLensGroupAndOperator.md#AmazonS3-Type-control_StorageLensGroupAndOperator-MatchAnySuffix")>
            <Suffix>***string***</Suffix>
         </[MatchAnySuffix](API_control_StorageLensGroupAndOperator.md#AmazonS3-Type-control_StorageLensGroupAndOperator-MatchAnySuffix "API_control_StorageLensGroupAndOperator.md#AmazonS3-Type-control_StorageLensGroupAndOperator-MatchAnySuffix")>
         <[MatchAnyTag](API_control_StorageLensGroupAndOperator.md#AmazonS3-Type-control_StorageLensGroupAndOperator-MatchAnyTag "API_control_StorageLensGroupAndOperator.md#AmazonS3-Type-control_StorageLensGroupAndOperator-MatchAnyTag")>
            <Tag>
               <[Key](API_control_S3Tag.md#AmazonS3-Type-control_S3Tag-Key "API_control_S3Tag.md#AmazonS3-Type-control_S3Tag-Key")>***string***</[Key](API_control_S3Tag.md#AmazonS3-Type-control_S3Tag-Key "API_control_S3Tag.md#AmazonS3-Type-control_S3Tag-Key")>
               <[Value](API_control_S3Tag.md#AmazonS3-Type-control_S3Tag-Value "API_control_S3Tag.md#AmazonS3-Type-control_S3Tag-Value")>***string***</[Value](API_control_S3Tag.md#AmazonS3-Type-control_S3Tag-Value "API_control_S3Tag.md#AmazonS3-Type-control_S3Tag-Value")>
            </Tag>
         </[MatchAnyTag](API_control_StorageLensGroupAndOperator.md#AmazonS3-Type-control_StorageLensGroupAndOperator-MatchAnyTag "API_control_StorageLensGroupAndOperator.md#AmazonS3-Type-control_StorageLensGroupAndOperator-MatchAnyTag")>
         <[MatchObjectAge](API_control_StorageLensGroupAndOperator.md#AmazonS3-Type-control_StorageLensGroupAndOperator-MatchObjectAge "API_control_StorageLensGroupAndOperator.md#AmazonS3-Type-control_StorageLensGroupAndOperator-MatchObjectAge")>
            <[DaysGreaterThan](API_control_MatchObjectAge.md#AmazonS3-Type-control_MatchObjectAge-DaysGreaterThan "API_control_MatchObjectAge.md#AmazonS3-Type-control_MatchObjectAge-DaysGreaterThan")>***integer***</[DaysGreaterThan](API_control_MatchObjectAge.md#AmazonS3-Type-control_MatchObjectAge-DaysGreaterThan "API_control_MatchObjectAge.md#AmazonS3-Type-control_MatchObjectAge-DaysGreaterThan")>
            <[DaysLessThan](API_control_MatchObjectAge.md#AmazonS3-Type-control_MatchObjectAge-DaysLessThan "API_control_MatchObjectAge.md#AmazonS3-Type-control_MatchObjectAge-DaysLessThan")>***integer***</[DaysLessThan](API_control_MatchObjectAge.md#AmazonS3-Type-control_MatchObjectAge-DaysLessThan "API_control_MatchObjectAge.md#AmazonS3-Type-control_MatchObjectAge-DaysLessThan")>
         </[MatchObjectAge](API_control_StorageLensGroupAndOperator.md#AmazonS3-Type-control_StorageLensGroupAndOperator-MatchObjectAge "API_control_StorageLensGroupAndOperator.md#AmazonS3-Type-control_StorageLensGroupAndOperator-MatchObjectAge")>
         <[MatchObjectSize](API_control_StorageLensGroupAndOperator.md#AmazonS3-Type-control_StorageLensGroupAndOperator-MatchObjectSize "API_control_StorageLensGroupAndOperator.md#AmazonS3-Type-control_StorageLensGroupAndOperator-MatchObjectSize")>
            <[BytesGreaterThan](API_control_MatchObjectSize.md#AmazonS3-Type-control_MatchObjectSize-BytesGreaterThan "API_control_MatchObjectSize.md#AmazonS3-Type-control_MatchObjectSize-BytesGreaterThan")>***long***</[BytesGreaterThan](API_control_MatchObjectSize.md#AmazonS3-Type-control_MatchObjectSize-BytesGreaterThan "API_control_MatchObjectSize.md#AmazonS3-Type-control_MatchObjectSize-BytesGreaterThan")>
            <[BytesLessThan](API_control_MatchObjectSize.md#AmazonS3-Type-control_MatchObjectSize-BytesLessThan "API_control_MatchObjectSize.md#AmazonS3-Type-control_MatchObjectSize-BytesLessThan")>***long***</[BytesLessThan](API_control_MatchObjectSize.md#AmazonS3-Type-control_MatchObjectSize-BytesLessThan "API_control_MatchObjectSize.md#AmazonS3-Type-control_MatchObjectSize-BytesLessThan")>
         </[MatchObjectSize](API_control_StorageLensGroupAndOperator.md#AmazonS3-Type-control_StorageLensGroupAndOperator-MatchObjectSize "API_control_StorageLensGroupAndOperator.md#AmazonS3-Type-control_StorageLensGroupAndOperator-MatchObjectSize")>
      </[And](API_control_StorageLensGroupFilter.md#AmazonS3-Type-control_StorageLensGroupFilter-And "API_control_StorageLensGroupFilter.md#AmazonS3-Type-control_StorageLensGroupFilter-And")>
      <[MatchAnyPrefix](API_control_StorageLensGroupFilter.md#AmazonS3-Type-control_StorageLensGroupFilter-MatchAnyPrefix "API_control_StorageLensGroupFilter.md#AmazonS3-Type-control_StorageLensGroupFilter-MatchAnyPrefix")>
         <Prefix>***string***</Prefix>
      </[MatchAnyPrefix](API_control_StorageLensGroupFilter.md#AmazonS3-Type-control_StorageLensGroupFilter-MatchAnyPrefix "API_control_StorageLensGroupFilter.md#AmazonS3-Type-control_StorageLensGroupFilter-MatchAnyPrefix")>
      <[MatchAnySuffix](API_control_StorageLensGroupFilter.md#AmazonS3-Type-control_StorageLensGroupFilter-MatchAnySuffix "API_control_StorageLensGroupFilter.md#AmazonS3-Type-control_StorageLensGroupFilter-MatchAnySuffix")>
         <Suffix>***string***</Suffix>
      </[MatchAnySuffix](API_control_StorageLensGroupFilter.md#AmazonS3-Type-control_StorageLensGroupFilter-MatchAnySuffix "API_control_StorageLensGroupFilter.md#AmazonS3-Type-control_StorageLensGroupFilter-MatchAnySuffix")>
      <[MatchAnyTag](API_control_StorageLensGroupFilter.md#AmazonS3-Type-control_StorageLensGroupFilter-MatchAnyTag "API_control_StorageLensGroupFilter.md#AmazonS3-Type-control_StorageLensGroupFilter-MatchAnyTag")>
         <Tag>
            <[Key](API_control_S3Tag.md#AmazonS3-Type-control_S3Tag-Key "API_control_S3Tag.md#AmazonS3-Type-control_S3Tag-Key")>***string***</[Key](API_control_S3Tag.md#AmazonS3-Type-control_S3Tag-Key "API_control_S3Tag.md#AmazonS3-Type-control_S3Tag-Key")>
            <[Value](API_control_S3Tag.md#AmazonS3-Type-control_S3Tag-Value "API_control_S3Tag.md#AmazonS3-Type-control_S3Tag-Value")>***string***</[Value](API_control_S3Tag.md#AmazonS3-Type-control_S3Tag-Value "API_control_S3Tag.md#AmazonS3-Type-control_S3Tag-Value")>
         </Tag>
      </[MatchAnyTag](API_control_StorageLensGroupFilter.md#AmazonS3-Type-control_StorageLensGroupFilter-MatchAnyTag "API_control_StorageLensGroupFilter.md#AmazonS3-Type-control_StorageLensGroupFilter-MatchAnyTag")>
      <[MatchObjectAge](API_control_StorageLensGroupFilter.md#AmazonS3-Type-control_StorageLensGroupFilter-MatchObjectAge "API_control_StorageLensGroupFilter.md#AmazonS3-Type-control_StorageLensGroupFilter-MatchObjectAge")>
         <[DaysGreaterThan](API_control_MatchObjectAge.md#AmazonS3-Type-control_MatchObjectAge-DaysGreaterThan "API_control_MatchObjectAge.md#AmazonS3-Type-control_MatchObjectAge-DaysGreaterThan")>***integer***</[DaysGreaterThan](API_control_MatchObjectAge.md#AmazonS3-Type-control_MatchObjectAge-DaysGreaterThan "API_control_MatchObjectAge.md#AmazonS3-Type-control_MatchObjectAge-DaysGreaterThan")>
         <[DaysLessThan](API_control_MatchObjectAge.md#AmazonS3-Type-control_MatchObjectAge-DaysLessThan "API_control_MatchObjectAge.md#AmazonS3-Type-control_MatchObjectAge-DaysLessThan")>***integer***</[DaysLessThan](API_control_MatchObjectAge.md#AmazonS3-Type-control_MatchObjectAge-DaysLessThan "API_control_MatchObjectAge.md#AmazonS3-Type-control_MatchObjectAge-DaysLessThan")>
      </[MatchObjectAge](API_control_StorageLensGroupFilter.md#AmazonS3-Type-control_StorageLensGroupFilter-MatchObjectAge "API_control_StorageLensGroupFilter.md#AmazonS3-Type-control_StorageLensGroupFilter-MatchObjectAge")>
      <[MatchObjectSize](API_control_StorageLensGroupFilter.md#AmazonS3-Type-control_StorageLensGroupFilter-MatchObjectSize "API_control_StorageLensGroupFilter.md#AmazonS3-Type-control_StorageLensGroupFilter-MatchObjectSize")>
         <[BytesGreaterThan](API_control_MatchObjectSize.md#AmazonS3-Type-control_MatchObjectSize-BytesGreaterThan "API_control_MatchObjectSize.md#AmazonS3-Type-control_MatchObjectSize-BytesGreaterThan")>***long***</[BytesGreaterThan](API_control_MatchObjectSize.md#AmazonS3-Type-control_MatchObjectSize-BytesGreaterThan "API_control_MatchObjectSize.md#AmazonS3-Type-control_MatchObjectSize-BytesGreaterThan")>
         <[BytesLessThan](API_control_MatchObjectSize.md#AmazonS3-Type-control_MatchObjectSize-BytesLessThan "API_control_MatchObjectSize.md#AmazonS3-Type-control_MatchObjectSize-BytesLessThan")>***long***</[BytesLessThan](API_control_MatchObjectSize.md#AmazonS3-Type-control_MatchObjectSize-BytesLessThan "API_control_MatchObjectSize.md#AmazonS3-Type-control_MatchObjectSize-BytesLessThan")>
      </[MatchObjectSize](API_control_StorageLensGroupFilter.md#AmazonS3-Type-control_StorageLensGroupFilter-MatchObjectSize "API_control_StorageLensGroupFilter.md#AmazonS3-Type-control_StorageLensGroupFilter-MatchObjectSize")>
      <[Or](API_control_StorageLensGroupFilter.md#AmazonS3-Type-control_StorageLensGroupFilter-Or "API_control_StorageLensGroupFilter.md#AmazonS3-Type-control_StorageLensGroupFilter-Or")>
         <[MatchAnyPrefix](API_control_StorageLensGroupOrOperator.md#AmazonS3-Type-control_StorageLensGroupOrOperator-MatchAnyPrefix "API_control_StorageLensGroupOrOperator.md#AmazonS3-Type-control_StorageLensGroupOrOperator-MatchAnyPrefix")>
            <Prefix>***string***</Prefix>
         </[MatchAnyPrefix](API_control_StorageLensGroupOrOperator.md#AmazonS3-Type-control_StorageLensGroupOrOperator-MatchAnyPrefix "API_control_StorageLensGroupOrOperator.md#AmazonS3-Type-control_StorageLensGroupOrOperator-MatchAnyPrefix")>
         <[MatchAnySuffix](API_control_StorageLensGroupOrOperator.md#AmazonS3-Type-control_StorageLensGroupOrOperator-MatchAnySuffix "API_control_StorageLensGroupOrOperator.md#AmazonS3-Type-control_StorageLensGroupOrOperator-MatchAnySuffix")>
            <Suffix>***string***</Suffix>
         </[MatchAnySuffix](API_control_StorageLensGroupOrOperator.md#AmazonS3-Type-control_StorageLensGroupOrOperator-MatchAnySuffix "API_control_StorageLensGroupOrOperator.md#AmazonS3-Type-control_StorageLensGroupOrOperator-MatchAnySuffix")>
         <[MatchAnyTag](API_control_StorageLensGroupOrOperator.md#AmazonS3-Type-control_StorageLensGroupOrOperator-MatchAnyTag "API_control_StorageLensGroupOrOperator.md#AmazonS3-Type-control_StorageLensGroupOrOperator-MatchAnyTag")>
            <Tag>
               <[Key](API_control_S3Tag.md#AmazonS3-Type-control_S3Tag-Key "API_control_S3Tag.md#AmazonS3-Type-control_S3Tag-Key")>***string***</[Key](API_control_S3Tag.md#AmazonS3-Type-control_S3Tag-Key "API_control_S3Tag.md#AmazonS3-Type-control_S3Tag-Key")>
               <[Value](API_control_S3Tag.md#AmazonS3-Type-control_S3Tag-Value "API_control_S3Tag.md#AmazonS3-Type-control_S3Tag-Value")>***string***</[Value](API_control_S3Tag.md#AmazonS3-Type-control_S3Tag-Value "API_control_S3Tag.md#AmazonS3-Type-control_S3Tag-Value")>
            </Tag>
         </[MatchAnyTag](API_control_StorageLensGroupOrOperator.md#AmazonS3-Type-control_StorageLensGroupOrOperator-MatchAnyTag "API_control_StorageLensGroupOrOperator.md#AmazonS3-Type-control_StorageLensGroupOrOperator-MatchAnyTag")>
         <[MatchObjectAge](API_control_StorageLensGroupOrOperator.md#AmazonS3-Type-control_StorageLensGroupOrOperator-MatchObjectAge "API_control_StorageLensGroupOrOperator.md#AmazonS3-Type-control_StorageLensGroupOrOperator-MatchObjectAge")>
            <[DaysGreaterThan](API_control_MatchObjectAge.md#AmazonS3-Type-control_MatchObjectAge-DaysGreaterThan "API_control_MatchObjectAge.md#AmazonS3-Type-control_MatchObjectAge-DaysGreaterThan")>***integer***</[DaysGreaterThan](API_control_MatchObjectAge.md#AmazonS3-Type-control_MatchObjectAge-DaysGreaterThan "API_control_MatchObjectAge.md#AmazonS3-Type-control_MatchObjectAge-DaysGreaterThan")>
            <[DaysLessThan](API_control_MatchObjectAge.md#AmazonS3-Type-control_MatchObjectAge-DaysLessThan "API_control_MatchObjectAge.md#AmazonS3-Type-control_MatchObjectAge-DaysLessThan")>***integer***</[DaysLessThan](API_control_MatchObjectAge.md#AmazonS3-Type-control_MatchObjectAge-DaysLessThan "API_control_MatchObjectAge.md#AmazonS3-Type-control_MatchObjectAge-DaysLessThan")>
         </[MatchObjectAge](API_control_StorageLensGroupOrOperator.md#AmazonS3-Type-control_StorageLensGroupOrOperator-MatchObjectAge "API_control_StorageLensGroupOrOperator.md#AmazonS3-Type-control_StorageLensGroupOrOperator-MatchObjectAge")>
         <[MatchObjectSize](API_control_StorageLensGroupOrOperator.md#AmazonS3-Type-control_StorageLensGroupOrOperator-MatchObjectSize "API_control_StorageLensGroupOrOperator.md#AmazonS3-Type-control_StorageLensGroupOrOperator-MatchObjectSize")>
            <[BytesGreaterThan](API_control_MatchObjectSize.md#AmazonS3-Type-control_MatchObjectSize-BytesGreaterThan "API_control_MatchObjectSize.md#AmazonS3-Type-control_MatchObjectSize-BytesGreaterThan")>***long***</[BytesGreaterThan](API_control_MatchObjectSize.md#AmazonS3-Type-control_MatchObjectSize-BytesGreaterThan "API_control_MatchObjectSize.md#AmazonS3-Type-control_MatchObjectSize-BytesGreaterThan")>
            <[BytesLessThan](API_control_MatchObjectSize.md#AmazonS3-Type-control_MatchObjectSize-BytesLessThan "API_control_MatchObjectSize.md#AmazonS3-Type-control_MatchObjectSize-BytesLessThan")>***long***</[BytesLessThan](API_control_MatchObjectSize.md#AmazonS3-Type-control_MatchObjectSize-BytesLessThan "API_control_MatchObjectSize.md#AmazonS3-Type-control_MatchObjectSize-BytesLessThan")>
         </[MatchObjectSize](API_control_StorageLensGroupOrOperator.md#AmazonS3-Type-control_StorageLensGroupOrOperator-MatchObjectSize "API_control_StorageLensGroupOrOperator.md#AmazonS3-Type-control_StorageLensGroupOrOperator-MatchObjectSize")>
      </[Or](API_control_StorageLensGroupFilter.md#AmazonS3-Type-control_StorageLensGroupFilter-Or "API_control_StorageLensGroupFilter.md#AmazonS3-Type-control_StorageLensGroupFilter-Or")>
   </[Filter](#AmazonS3-control_GetStorageLensGroup-response-Filter "#AmazonS3-control_GetStorageLensGroup-response-Filter")>
   <[StorageLensGroupArn](#AmazonS3-control_GetStorageLensGroup-response-StorageLensGroupArn "#AmazonS3-control_GetStorageLensGroup-response-StorageLensGroupArn")>***string***</[StorageLensGroupArn](#AmazonS3-control_GetStorageLensGroup-response-StorageLensGroupArn "#AmazonS3-control_GetStorageLensGroup-response-StorageLensGroupArn")>
</[StorageLensGroup](#AmazonS3-control_GetStorageLensGroup-response-StorageLensGroup "#AmazonS3-control_GetStorageLensGroup-response-StorageLensGroup")>
```

## Response Elements


If the action is successful, the service sends back an HTTP 200 response.


The following data is returned in XML format by the service.





**[StorageLensGroup](#API_control_GetStorageLensGroup_ResponseSyntax "#API_control_GetStorageLensGroup_ResponseSyntax")**


Root level tag for the StorageLensGroup parameters.


Required: Yes




**[Filter](#API_control_GetStorageLensGroup_ResponseSyntax "#API_control_GetStorageLensGroup_ResponseSyntax")**


Sets the criteria for the Storage Lens group data that is displayed. For multiple filter
 conditions, the `AND` or `OR` logical operator is used.


Type: [StorageLensGroupFilter](API_control_StorageLensGroupFilter.md "API_control_StorageLensGroupFilter.md") data type




**[Name](#API_control_GetStorageLensGroup_ResponseSyntax "#API_control_GetStorageLensGroup_ResponseSyntax")**


 Contains the name of the Storage Lens group. 


Type: String


Length Constraints: Minimum length of 1. Maximum length of 64.


Pattern: `[a-zA-Z0-9\-\_]+`





**[StorageLensGroupArn](#API_control_GetStorageLensGroup_ResponseSyntax "#API_control_GetStorageLensGroup_ResponseSyntax")**


 Contains the Amazon Resource Name (ARN) of the Storage Lens group. This property is
 read-only. 


Type: String


Length Constraints: Minimum length of 4. Maximum length of 1024.


Pattern: `arn:[a-z\-]+:s3:[a-z0-9\-]+:\d{12}:storage\-lens\-group\/.*`





## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface](https://docs.aws.amazon.com/goto/cli2/s3control-2018-08-20/GetStorageLensGroup "https://docs.aws.amazon.com/goto/cli2/s3control-2018-08-20/GetStorageLensGroup")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/s3control-2018-08-20/GetStorageLensGroup "https://docs.aws.amazon.com/goto/DotNetSDKV3/s3control-2018-08-20/GetStorageLensGroup")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/GetStorageLensGroup "https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/GetStorageLensGroup")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/s3control-2018-08-20/GetStorageLensGroup "https://docs.aws.amazon.com/goto/SdkForGoV2/s3control-2018-08-20/GetStorageLensGroup")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/GetStorageLensGroup "https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/GetStorageLensGroup")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3control-2018-08-20/GetStorageLensGroup "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3control-2018-08-20/GetStorageLensGroup")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/s3control-2018-08-20/GetStorageLensGroup "https://docs.aws.amazon.com/goto/SdkForKotlin/s3control-2018-08-20/GetStorageLensGroup")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/s3control-2018-08-20/GetStorageLensGroup "https://docs.aws.amazon.com/goto/SdkForPHPV3/s3control-2018-08-20/GetStorageLensGroup")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/s3control-2018-08-20/GetStorageLensGroup "https://docs.aws.amazon.com/goto/boto3/s3control-2018-08-20/GetStorageLensGroup")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/GetStorageLensGroup "https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/GetStorageLensGroup")
