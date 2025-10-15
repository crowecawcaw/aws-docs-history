# CreateStorageLensGroup

 Creates a new S3 Storage Lens group and associates it with the specified AWS account ID. An
 S3 Storage Lens group is a custom grouping of objects based on prefix, suffix, object tags,
 object size, object age, or a combination of these filters. For each Storage Lens group
 that you’ve created, you can also optionally add AWS resource tags. For more information
 about S3 Storage Lens groups, see [Working with S3 Storage Lens
 groups](../userguide/storage-lens-groups-overview.md "../userguide/storage-lens-groups-overview.md").

To use this operation, you must have the permission to perform the
 `s3:CreateStorageLensGroup` action. If you’re trying to create a Storage Lens
 group with AWS resource tags, you must also have permission to perform the
 `s3:TagResource` action. For more information about the required Storage Lens
 Groups permissions, see [Setting account permissions to use S3 Storage Lens groups](../userguide/storage_lens_iam_permissions.md#storage_lens_groups_permissions "../userguide/storage_lens_iam_permissions.md#storage_lens_groups_permissions").

For information about Storage Lens groups errors, see [List of Amazon S3 Storage
 Lens error codes](ErrorResponses.md#S3LensErrorCodeList "ErrorResponses.md#S3LensErrorCodeList").

###### Important

You must URL encode any signed header values that contain spaces. For example, if your header value is `my file.txt`, containing two spaces after `my`, you must URL encode this value to `my%20%20file.txt`.


## Request Syntax



```
POST /v20180820/storagelensgroup HTTP/1.1
Host: s3-control.amazonaws.com
x-amz-account-id: `AccountId`
<?xml version="1.0" encoding="UTF-8"?>
<[CreateStorageLensGroupRequest](#AmazonS3-control_CreateStorageLensGroup-request-CreateStorageLensGroupRequest "#AmazonS3-control_CreateStorageLensGroup-request-CreateStorageLensGroupRequest") xmlns="http://awss3control.amazonaws.com/doc/2018-08-20/">
   <[StorageLensGroup](#AmazonS3-control_CreateStorageLensGroup-request-StorageLensGroup "#AmazonS3-control_CreateStorageLensGroup-request-StorageLensGroup")>
      <[Filter](API_control_StorageLensGroup.md#AmazonS3-Type-control_StorageLensGroup-Filter "API_control_StorageLensGroup.md#AmazonS3-Type-control_StorageLensGroup-Filter")>
         <[And](API_control_StorageLensGroupFilter.md#AmazonS3-Type-control_StorageLensGroupFilter-And "API_control_StorageLensGroupFilter.md#AmazonS3-Type-control_StorageLensGroupFilter-And")>
            <[MatchAnyPrefix](API_control_StorageLensGroupAndOperator.md#AmazonS3-Type-control_StorageLensGroupAndOperator-MatchAnyPrefix "API_control_StorageLensGroupAndOperator.md#AmazonS3-Type-control_StorageLensGroupAndOperator-MatchAnyPrefix")>
               <Prefix>`string`</Prefix>
            </[MatchAnyPrefix](API_control_StorageLensGroupAndOperator.md#AmazonS3-Type-control_StorageLensGroupAndOperator-MatchAnyPrefix "API_control_StorageLensGroupAndOperator.md#AmazonS3-Type-control_StorageLensGroupAndOperator-MatchAnyPrefix")>
            <[MatchAnySuffix](API_control_StorageLensGroupAndOperator.md#AmazonS3-Type-control_StorageLensGroupAndOperator-MatchAnySuffix "API_control_StorageLensGroupAndOperator.md#AmazonS3-Type-control_StorageLensGroupAndOperator-MatchAnySuffix")>
               <Suffix>`string`</Suffix>
            </[MatchAnySuffix](API_control_StorageLensGroupAndOperator.md#AmazonS3-Type-control_StorageLensGroupAndOperator-MatchAnySuffix "API_control_StorageLensGroupAndOperator.md#AmazonS3-Type-control_StorageLensGroupAndOperator-MatchAnySuffix")>
            <[MatchAnyTag](API_control_StorageLensGroupAndOperator.md#AmazonS3-Type-control_StorageLensGroupAndOperator-MatchAnyTag "API_control_StorageLensGroupAndOperator.md#AmazonS3-Type-control_StorageLensGroupAndOperator-MatchAnyTag")>
               <Tag>
                  <[Key](API_control_S3Tag.md#AmazonS3-Type-control_S3Tag-Key "API_control_S3Tag.md#AmazonS3-Type-control_S3Tag-Key")>`string`</[Key](API_control_S3Tag.md#AmazonS3-Type-control_S3Tag-Key "API_control_S3Tag.md#AmazonS3-Type-control_S3Tag-Key")>
                  <[Value](API_control_S3Tag.md#AmazonS3-Type-control_S3Tag-Value "API_control_S3Tag.md#AmazonS3-Type-control_S3Tag-Value")>`string`</[Value](API_control_S3Tag.md#AmazonS3-Type-control_S3Tag-Value "API_control_S3Tag.md#AmazonS3-Type-control_S3Tag-Value")>
               </Tag>
            </[MatchAnyTag](API_control_StorageLensGroupAndOperator.md#AmazonS3-Type-control_StorageLensGroupAndOperator-MatchAnyTag "API_control_StorageLensGroupAndOperator.md#AmazonS3-Type-control_StorageLensGroupAndOperator-MatchAnyTag")>
            <[MatchObjectAge](API_control_StorageLensGroupAndOperator.md#AmazonS3-Type-control_StorageLensGroupAndOperator-MatchObjectAge "API_control_StorageLensGroupAndOperator.md#AmazonS3-Type-control_StorageLensGroupAndOperator-MatchObjectAge")>
               <[DaysGreaterThan](API_control_MatchObjectAge.md#AmazonS3-Type-control_MatchObjectAge-DaysGreaterThan "API_control_MatchObjectAge.md#AmazonS3-Type-control_MatchObjectAge-DaysGreaterThan")>`integer`</[DaysGreaterThan](API_control_MatchObjectAge.md#AmazonS3-Type-control_MatchObjectAge-DaysGreaterThan "API_control_MatchObjectAge.md#AmazonS3-Type-control_MatchObjectAge-DaysGreaterThan")>
               <[DaysLessThan](API_control_MatchObjectAge.md#AmazonS3-Type-control_MatchObjectAge-DaysLessThan "API_control_MatchObjectAge.md#AmazonS3-Type-control_MatchObjectAge-DaysLessThan")>`integer`</[DaysLessThan](API_control_MatchObjectAge.md#AmazonS3-Type-control_MatchObjectAge-DaysLessThan "API_control_MatchObjectAge.md#AmazonS3-Type-control_MatchObjectAge-DaysLessThan")>
            </[MatchObjectAge](API_control_StorageLensGroupAndOperator.md#AmazonS3-Type-control_StorageLensGroupAndOperator-MatchObjectAge "API_control_StorageLensGroupAndOperator.md#AmazonS3-Type-control_StorageLensGroupAndOperator-MatchObjectAge")>
            <[MatchObjectSize](API_control_StorageLensGroupAndOperator.md#AmazonS3-Type-control_StorageLensGroupAndOperator-MatchObjectSize "API_control_StorageLensGroupAndOperator.md#AmazonS3-Type-control_StorageLensGroupAndOperator-MatchObjectSize")>
               <[BytesGreaterThan](API_control_MatchObjectSize.md#AmazonS3-Type-control_MatchObjectSize-BytesGreaterThan "API_control_MatchObjectSize.md#AmazonS3-Type-control_MatchObjectSize-BytesGreaterThan")>`long`</[BytesGreaterThan](API_control_MatchObjectSize.md#AmazonS3-Type-control_MatchObjectSize-BytesGreaterThan "API_control_MatchObjectSize.md#AmazonS3-Type-control_MatchObjectSize-BytesGreaterThan")>
               <[BytesLessThan](API_control_MatchObjectSize.md#AmazonS3-Type-control_MatchObjectSize-BytesLessThan "API_control_MatchObjectSize.md#AmazonS3-Type-control_MatchObjectSize-BytesLessThan")>`long`</[BytesLessThan](API_control_MatchObjectSize.md#AmazonS3-Type-control_MatchObjectSize-BytesLessThan "API_control_MatchObjectSize.md#AmazonS3-Type-control_MatchObjectSize-BytesLessThan")>
            </[MatchObjectSize](API_control_StorageLensGroupAndOperator.md#AmazonS3-Type-control_StorageLensGroupAndOperator-MatchObjectSize "API_control_StorageLensGroupAndOperator.md#AmazonS3-Type-control_StorageLensGroupAndOperator-MatchObjectSize")>
         </[And](API_control_StorageLensGroupFilter.md#AmazonS3-Type-control_StorageLensGroupFilter-And "API_control_StorageLensGroupFilter.md#AmazonS3-Type-control_StorageLensGroupFilter-And")>
         <[MatchAnyPrefix](API_control_StorageLensGroupFilter.md#AmazonS3-Type-control_StorageLensGroupFilter-MatchAnyPrefix "API_control_StorageLensGroupFilter.md#AmazonS3-Type-control_StorageLensGroupFilter-MatchAnyPrefix")>
            <Prefix>`string`</Prefix>
         </[MatchAnyPrefix](API_control_StorageLensGroupFilter.md#AmazonS3-Type-control_StorageLensGroupFilter-MatchAnyPrefix "API_control_StorageLensGroupFilter.md#AmazonS3-Type-control_StorageLensGroupFilter-MatchAnyPrefix")>
         <[MatchAnySuffix](API_control_StorageLensGroupFilter.md#AmazonS3-Type-control_StorageLensGroupFilter-MatchAnySuffix "API_control_StorageLensGroupFilter.md#AmazonS3-Type-control_StorageLensGroupFilter-MatchAnySuffix")>
            <Suffix>`string`</Suffix>
         </[MatchAnySuffix](API_control_StorageLensGroupFilter.md#AmazonS3-Type-control_StorageLensGroupFilter-MatchAnySuffix "API_control_StorageLensGroupFilter.md#AmazonS3-Type-control_StorageLensGroupFilter-MatchAnySuffix")>
         <[MatchAnyTag](API_control_StorageLensGroupFilter.md#AmazonS3-Type-control_StorageLensGroupFilter-MatchAnyTag "API_control_StorageLensGroupFilter.md#AmazonS3-Type-control_StorageLensGroupFilter-MatchAnyTag")>
            <Tag>
               <[Key](API_control_S3Tag.md#AmazonS3-Type-control_S3Tag-Key "API_control_S3Tag.md#AmazonS3-Type-control_S3Tag-Key")>`string`</[Key](API_control_S3Tag.md#AmazonS3-Type-control_S3Tag-Key "API_control_S3Tag.md#AmazonS3-Type-control_S3Tag-Key")>
               <[Value](API_control_S3Tag.md#AmazonS3-Type-control_S3Tag-Value "API_control_S3Tag.md#AmazonS3-Type-control_S3Tag-Value")>`string`</[Value](API_control_S3Tag.md#AmazonS3-Type-control_S3Tag-Value "API_control_S3Tag.md#AmazonS3-Type-control_S3Tag-Value")>
            </Tag>
         </[MatchAnyTag](API_control_StorageLensGroupFilter.md#AmazonS3-Type-control_StorageLensGroupFilter-MatchAnyTag "API_control_StorageLensGroupFilter.md#AmazonS3-Type-control_StorageLensGroupFilter-MatchAnyTag")>
         <[MatchObjectAge](API_control_StorageLensGroupFilter.md#AmazonS3-Type-control_StorageLensGroupFilter-MatchObjectAge "API_control_StorageLensGroupFilter.md#AmazonS3-Type-control_StorageLensGroupFilter-MatchObjectAge")>
            <[DaysGreaterThan](API_control_MatchObjectAge.md#AmazonS3-Type-control_MatchObjectAge-DaysGreaterThan "API_control_MatchObjectAge.md#AmazonS3-Type-control_MatchObjectAge-DaysGreaterThan")>`integer`</[DaysGreaterThan](API_control_MatchObjectAge.md#AmazonS3-Type-control_MatchObjectAge-DaysGreaterThan "API_control_MatchObjectAge.md#AmazonS3-Type-control_MatchObjectAge-DaysGreaterThan")>
            <[DaysLessThan](API_control_MatchObjectAge.md#AmazonS3-Type-control_MatchObjectAge-DaysLessThan "API_control_MatchObjectAge.md#AmazonS3-Type-control_MatchObjectAge-DaysLessThan")>`integer`</[DaysLessThan](API_control_MatchObjectAge.md#AmazonS3-Type-control_MatchObjectAge-DaysLessThan "API_control_MatchObjectAge.md#AmazonS3-Type-control_MatchObjectAge-DaysLessThan")>
         </[MatchObjectAge](API_control_StorageLensGroupFilter.md#AmazonS3-Type-control_StorageLensGroupFilter-MatchObjectAge "API_control_StorageLensGroupFilter.md#AmazonS3-Type-control_StorageLensGroupFilter-MatchObjectAge")>
         <[MatchObjectSize](API_control_StorageLensGroupFilter.md#AmazonS3-Type-control_StorageLensGroupFilter-MatchObjectSize "API_control_StorageLensGroupFilter.md#AmazonS3-Type-control_StorageLensGroupFilter-MatchObjectSize")>
            <[BytesGreaterThan](API_control_MatchObjectSize.md#AmazonS3-Type-control_MatchObjectSize-BytesGreaterThan "API_control_MatchObjectSize.md#AmazonS3-Type-control_MatchObjectSize-BytesGreaterThan")>`long`</[BytesGreaterThan](API_control_MatchObjectSize.md#AmazonS3-Type-control_MatchObjectSize-BytesGreaterThan "API_control_MatchObjectSize.md#AmazonS3-Type-control_MatchObjectSize-BytesGreaterThan")>
            <[BytesLessThan](API_control_MatchObjectSize.md#AmazonS3-Type-control_MatchObjectSize-BytesLessThan "API_control_MatchObjectSize.md#AmazonS3-Type-control_MatchObjectSize-BytesLessThan")>`long`</[BytesLessThan](API_control_MatchObjectSize.md#AmazonS3-Type-control_MatchObjectSize-BytesLessThan "API_control_MatchObjectSize.md#AmazonS3-Type-control_MatchObjectSize-BytesLessThan")>
         </[MatchObjectSize](API_control_StorageLensGroupFilter.md#AmazonS3-Type-control_StorageLensGroupFilter-MatchObjectSize "API_control_StorageLensGroupFilter.md#AmazonS3-Type-control_StorageLensGroupFilter-MatchObjectSize")>
         <[Or](API_control_StorageLensGroupFilter.md#AmazonS3-Type-control_StorageLensGroupFilter-Or "API_control_StorageLensGroupFilter.md#AmazonS3-Type-control_StorageLensGroupFilter-Or")>
            <[MatchAnyPrefix](API_control_StorageLensGroupOrOperator.md#AmazonS3-Type-control_StorageLensGroupOrOperator-MatchAnyPrefix "API_control_StorageLensGroupOrOperator.md#AmazonS3-Type-control_StorageLensGroupOrOperator-MatchAnyPrefix")>
               <Prefix>`string`</Prefix>
            </[MatchAnyPrefix](API_control_StorageLensGroupOrOperator.md#AmazonS3-Type-control_StorageLensGroupOrOperator-MatchAnyPrefix "API_control_StorageLensGroupOrOperator.md#AmazonS3-Type-control_StorageLensGroupOrOperator-MatchAnyPrefix")>
            <[MatchAnySuffix](API_control_StorageLensGroupOrOperator.md#AmazonS3-Type-control_StorageLensGroupOrOperator-MatchAnySuffix "API_control_StorageLensGroupOrOperator.md#AmazonS3-Type-control_StorageLensGroupOrOperator-MatchAnySuffix")>
               <Suffix>`string`</Suffix>
            </[MatchAnySuffix](API_control_StorageLensGroupOrOperator.md#AmazonS3-Type-control_StorageLensGroupOrOperator-MatchAnySuffix "API_control_StorageLensGroupOrOperator.md#AmazonS3-Type-control_StorageLensGroupOrOperator-MatchAnySuffix")>
            <[MatchAnyTag](API_control_StorageLensGroupOrOperator.md#AmazonS3-Type-control_StorageLensGroupOrOperator-MatchAnyTag "API_control_StorageLensGroupOrOperator.md#AmazonS3-Type-control_StorageLensGroupOrOperator-MatchAnyTag")>
               <Tag>
                  <[Key](API_control_S3Tag.md#AmazonS3-Type-control_S3Tag-Key "API_control_S3Tag.md#AmazonS3-Type-control_S3Tag-Key")>`string`</[Key](API_control_S3Tag.md#AmazonS3-Type-control_S3Tag-Key "API_control_S3Tag.md#AmazonS3-Type-control_S3Tag-Key")>
                  <[Value](API_control_S3Tag.md#AmazonS3-Type-control_S3Tag-Value "API_control_S3Tag.md#AmazonS3-Type-control_S3Tag-Value")>`string`</[Value](API_control_S3Tag.md#AmazonS3-Type-control_S3Tag-Value "API_control_S3Tag.md#AmazonS3-Type-control_S3Tag-Value")>
               </Tag>
            </[MatchAnyTag](API_control_StorageLensGroupOrOperator.md#AmazonS3-Type-control_StorageLensGroupOrOperator-MatchAnyTag "API_control_StorageLensGroupOrOperator.md#AmazonS3-Type-control_StorageLensGroupOrOperator-MatchAnyTag")>
            <[MatchObjectAge](API_control_StorageLensGroupOrOperator.md#AmazonS3-Type-control_StorageLensGroupOrOperator-MatchObjectAge "API_control_StorageLensGroupOrOperator.md#AmazonS3-Type-control_StorageLensGroupOrOperator-MatchObjectAge")>
               <[DaysGreaterThan](API_control_MatchObjectAge.md#AmazonS3-Type-control_MatchObjectAge-DaysGreaterThan "API_control_MatchObjectAge.md#AmazonS3-Type-control_MatchObjectAge-DaysGreaterThan")>`integer`</[DaysGreaterThan](API_control_MatchObjectAge.md#AmazonS3-Type-control_MatchObjectAge-DaysGreaterThan "API_control_MatchObjectAge.md#AmazonS3-Type-control_MatchObjectAge-DaysGreaterThan")>
               <[DaysLessThan](API_control_MatchObjectAge.md#AmazonS3-Type-control_MatchObjectAge-DaysLessThan "API_control_MatchObjectAge.md#AmazonS3-Type-control_MatchObjectAge-DaysLessThan")>`integer`</[DaysLessThan](API_control_MatchObjectAge.md#AmazonS3-Type-control_MatchObjectAge-DaysLessThan "API_control_MatchObjectAge.md#AmazonS3-Type-control_MatchObjectAge-DaysLessThan")>
            </[MatchObjectAge](API_control_StorageLensGroupOrOperator.md#AmazonS3-Type-control_StorageLensGroupOrOperator-MatchObjectAge "API_control_StorageLensGroupOrOperator.md#AmazonS3-Type-control_StorageLensGroupOrOperator-MatchObjectAge")>
            <[MatchObjectSize](API_control_StorageLensGroupOrOperator.md#AmazonS3-Type-control_StorageLensGroupOrOperator-MatchObjectSize "API_control_StorageLensGroupOrOperator.md#AmazonS3-Type-control_StorageLensGroupOrOperator-MatchObjectSize")>
               <[BytesGreaterThan](API_control_MatchObjectSize.md#AmazonS3-Type-control_MatchObjectSize-BytesGreaterThan "API_control_MatchObjectSize.md#AmazonS3-Type-control_MatchObjectSize-BytesGreaterThan")>`long`</[BytesGreaterThan](API_control_MatchObjectSize.md#AmazonS3-Type-control_MatchObjectSize-BytesGreaterThan "API_control_MatchObjectSize.md#AmazonS3-Type-control_MatchObjectSize-BytesGreaterThan")>
               <[BytesLessThan](API_control_MatchObjectSize.md#AmazonS3-Type-control_MatchObjectSize-BytesLessThan "API_control_MatchObjectSize.md#AmazonS3-Type-control_MatchObjectSize-BytesLessThan")>`long`</[BytesLessThan](API_control_MatchObjectSize.md#AmazonS3-Type-control_MatchObjectSize-BytesLessThan "API_control_MatchObjectSize.md#AmazonS3-Type-control_MatchObjectSize-BytesLessThan")>
            </[MatchObjectSize](API_control_StorageLensGroupOrOperator.md#AmazonS3-Type-control_StorageLensGroupOrOperator-MatchObjectSize "API_control_StorageLensGroupOrOperator.md#AmazonS3-Type-control_StorageLensGroupOrOperator-MatchObjectSize")>
         </[Or](API_control_StorageLensGroupFilter.md#AmazonS3-Type-control_StorageLensGroupFilter-Or "API_control_StorageLensGroupFilter.md#AmazonS3-Type-control_StorageLensGroupFilter-Or")>
      </[Filter](API_control_StorageLensGroup.md#AmazonS3-Type-control_StorageLensGroup-Filter "API_control_StorageLensGroup.md#AmazonS3-Type-control_StorageLensGroup-Filter")>
      <[Name](API_control_StorageLensGroup.md#AmazonS3-Type-control_StorageLensGroup-Name "API_control_StorageLensGroup.md#AmazonS3-Type-control_StorageLensGroup-Name")>`string`</[Name](API_control_StorageLensGroup.md#AmazonS3-Type-control_StorageLensGroup-Name "API_control_StorageLensGroup.md#AmazonS3-Type-control_StorageLensGroup-Name")>
      <[StorageLensGroupArn](API_control_StorageLensGroup.md#AmazonS3-Type-control_StorageLensGroup-StorageLensGroupArn "API_control_StorageLensGroup.md#AmazonS3-Type-control_StorageLensGroup-StorageLensGroupArn")>`string`</[StorageLensGroupArn](API_control_StorageLensGroup.md#AmazonS3-Type-control_StorageLensGroup-StorageLensGroupArn "API_control_StorageLensGroup.md#AmazonS3-Type-control_StorageLensGroup-StorageLensGroupArn")>
   </[StorageLensGroup](#AmazonS3-control_CreateStorageLensGroup-request-StorageLensGroup "#AmazonS3-control_CreateStorageLensGroup-request-StorageLensGroup")>
   <[Tags](#AmazonS3-control_CreateStorageLensGroup-request-Tags "#AmazonS3-control_CreateStorageLensGroup-request-Tags")>
      <Tag>
         <[Key](API_control_Tag.md#AmazonS3-Type-control_Tag-Key "API_control_Tag.md#AmazonS3-Type-control_Tag-Key")>`string`</[Key](API_control_Tag.md#AmazonS3-Type-control_Tag-Key "API_control_Tag.md#AmazonS3-Type-control_Tag-Key")>
         <[Value](API_control_Tag.md#AmazonS3-Type-control_Tag-Value "API_control_Tag.md#AmazonS3-Type-control_Tag-Value")>`string`</[Value](API_control_Tag.md#AmazonS3-Type-control_Tag-Value "API_control_Tag.md#AmazonS3-Type-control_Tag-Value")>
      </Tag>
   </[Tags](#AmazonS3-control_CreateStorageLensGroup-request-Tags "#AmazonS3-control_CreateStorageLensGroup-request-Tags")>
</[CreateStorageLensGroupRequest](#AmazonS3-control_CreateStorageLensGroup-request-CreateStorageLensGroupRequest "#AmazonS3-control_CreateStorageLensGroup-request-CreateStorageLensGroupRequest")>
```

## URI Request Parameters


The request uses the following URI parameters.





**[x-amz-account-id](#API_control_CreateStorageLensGroup_RequestSyntax "#API_control_CreateStorageLensGroup_RequestSyntax")**



The AWS account ID that the Storage Lens group is created from and associated with.



Length Constraints: Maximum length of 64.


Pattern: `^\d{12}$`



Required: Yes




## Request Body


The request accepts the following data in XML format.





**[CreateStorageLensGroupRequest](#API_control_CreateStorageLensGroup_RequestSyntax "#API_control_CreateStorageLensGroup_RequestSyntax")**


Root level tag for the CreateStorageLensGroupRequest parameters.


Required: Yes




**[StorageLensGroup](#API_control_CreateStorageLensGroup_RequestSyntax "#API_control_CreateStorageLensGroup_RequestSyntax")**



The Storage Lens group configuration.



Type: [StorageLensGroup](API_control_StorageLensGroup.md "API_control_StorageLensGroup.md") data type


Required: Yes




**[Tags](#API_control_CreateStorageLensGroup_RequestSyntax "#API_control_CreateStorageLensGroup_RequestSyntax")**



The AWS resource tags that you're adding to your Storage Lens group. This parameter is optional.



Type: Array of [Tag](API_control_Tag.md "API_control_Tag.md") data types


Array Members: Minimum number of 0 items. Maximum number of 50 items.


Required: No




## Response Syntax



```
HTTP/1.1 204

```

## Response Elements


If the action is successful, the service sends back an HTTP 204 response with an empty HTTP body.


## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface](https://docs.aws.amazon.com/goto/cli2/s3control-2018-08-20/CreateStorageLensGroup "https://docs.aws.amazon.com/goto/cli2/s3control-2018-08-20/CreateStorageLensGroup")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/s3control-2018-08-20/CreateStorageLensGroup "https://docs.aws.amazon.com/goto/DotNetSDKV3/s3control-2018-08-20/CreateStorageLensGroup")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/CreateStorageLensGroup "https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/CreateStorageLensGroup")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/s3control-2018-08-20/CreateStorageLensGroup "https://docs.aws.amazon.com/goto/SdkForGoV2/s3control-2018-08-20/CreateStorageLensGroup")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/CreateStorageLensGroup "https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/CreateStorageLensGroup")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3control-2018-08-20/CreateStorageLensGroup "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3control-2018-08-20/CreateStorageLensGroup")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/s3control-2018-08-20/CreateStorageLensGroup "https://docs.aws.amazon.com/goto/SdkForKotlin/s3control-2018-08-20/CreateStorageLensGroup")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/s3control-2018-08-20/CreateStorageLensGroup "https://docs.aws.amazon.com/goto/SdkForPHPV3/s3control-2018-08-20/CreateStorageLensGroup")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/s3control-2018-08-20/CreateStorageLensGroup "https://docs.aws.amazon.com/goto/boto3/s3control-2018-08-20/CreateStorageLensGroup")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/CreateStorageLensGroup "https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/CreateStorageLensGroup")
