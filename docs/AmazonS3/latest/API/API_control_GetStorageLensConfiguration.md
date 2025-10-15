# GetStorageLensConfiguration

###### Note

This operation is not supported by directory buckets.

Gets the Amazon S3 Storage Lens configuration. For more information, see [Assessing your storage
 activity and usage with Amazon S3 Storage Lens](https://docs.aws.amazon.com/AmazonS3/latest/dev/storage_lens.html "https://docs.aws.amazon.com/AmazonS3/latest/dev/storage_lens.html")  in the
 *Amazon S3 User Guide*. For a complete list of S3 Storage Lens metrics, see [S3 Storage Lens metrics glossary](../userguide/storage_lens_metrics_glossary.md "../userguide/storage_lens_metrics_glossary.md") in the *Amazon S3 User Guide*.

###### Note

To use this action, you must have permission to perform the
 `s3:GetStorageLensConfiguration` action. For more information, see [Setting permissions to use Amazon S3 Storage Lens](https://docs.aws.amazon.com/AmazonS3/latest/dev/storage_lens_iam_permissions.html "https://docs.aws.amazon.com/AmazonS3/latest/dev/storage_lens_iam_permissions.html") in the
 *Amazon S3 User Guide*.

###### Important

You must URL encode any signed header values that contain spaces. For example, if your header value is `my file.txt`, containing two spaces after `my`, you must URL encode this value to `my%20%20file.txt`.


## Request Syntax



```
GET /v20180820/storagelens/`storagelensid` HTTP/1.1
Host: s3-control.amazonaws.com
x-amz-account-id: `AccountId`

```

## URI Request Parameters


The request uses the following URI parameters.





**[storagelensid](#API_control_GetStorageLensConfiguration_RequestSyntax "#API_control_GetStorageLensConfiguration_RequestSyntax")**


The ID of the Amazon S3 Storage Lens configuration.


Length Constraints: Minimum length of 1. Maximum length of 64.


Pattern: `[a-zA-Z0-9\-\_\.]+`



Required: Yes




**[x-amz-account-id](#API_control_GetStorageLensConfiguration_RequestSyntax "#API_control_GetStorageLensConfiguration_RequestSyntax")**


The account ID of the requester.


Length Constraints: Maximum length of 64.


Pattern: `^\d{12}$`



Required: Yes




## Request Body


The request does not have a request body.


## Response Syntax



```
HTTP/1.1 200
<?xml version="1.0" encoding="UTF-8"?>
<[StorageLensConfiguration](#AmazonS3-control_GetStorageLensConfiguration-response-StorageLensConfiguration "#AmazonS3-control_GetStorageLensConfiguration-response-StorageLensConfiguration")>
   <[Id](#AmazonS3-control_GetStorageLensConfiguration-response-Id "#AmazonS3-control_GetStorageLensConfiguration-response-Id")>***string***</[Id](#AmazonS3-control_GetStorageLensConfiguration-response-Id "#AmazonS3-control_GetStorageLensConfiguration-response-Id")>
   <[AccountLevel](#AmazonS3-control_GetStorageLensConfiguration-response-AccountLevel "#AmazonS3-control_GetStorageLensConfiguration-response-AccountLevel")>
      <[ActivityMetrics](API_control_AccountLevel.md#AmazonS3-Type-control_AccountLevel-ActivityMetrics "API_control_AccountLevel.md#AmazonS3-Type-control_AccountLevel-ActivityMetrics")>
         <[IsEnabled](API_control_ActivityMetrics.md#AmazonS3-Type-control_ActivityMetrics-IsEnabled "API_control_ActivityMetrics.md#AmazonS3-Type-control_ActivityMetrics-IsEnabled")>***boolean***</[IsEnabled](API_control_ActivityMetrics.md#AmazonS3-Type-control_ActivityMetrics-IsEnabled "API_control_ActivityMetrics.md#AmazonS3-Type-control_ActivityMetrics-IsEnabled")>
      </[ActivityMetrics](API_control_AccountLevel.md#AmazonS3-Type-control_AccountLevel-ActivityMetrics "API_control_AccountLevel.md#AmazonS3-Type-control_AccountLevel-ActivityMetrics")>
      <[AdvancedCostOptimizationMetrics](API_control_AccountLevel.md#AmazonS3-Type-control_AccountLevel-AdvancedCostOptimizationMetrics "API_control_AccountLevel.md#AmazonS3-Type-control_AccountLevel-AdvancedCostOptimizationMetrics")>
         <[IsEnabled](API_control_AdvancedCostOptimizationMetrics.md#AmazonS3-Type-control_AdvancedCostOptimizationMetrics-IsEnabled "API_control_AdvancedCostOptimizationMetrics.md#AmazonS3-Type-control_AdvancedCostOptimizationMetrics-IsEnabled")>***boolean***</[IsEnabled](API_control_AdvancedCostOptimizationMetrics.md#AmazonS3-Type-control_AdvancedCostOptimizationMetrics-IsEnabled "API_control_AdvancedCostOptimizationMetrics.md#AmazonS3-Type-control_AdvancedCostOptimizationMetrics-IsEnabled")>
      </[AdvancedCostOptimizationMetrics](API_control_AccountLevel.md#AmazonS3-Type-control_AccountLevel-AdvancedCostOptimizationMetrics "API_control_AccountLevel.md#AmazonS3-Type-control_AccountLevel-AdvancedCostOptimizationMetrics")>
      <[AdvancedDataProtectionMetrics](API_control_AccountLevel.md#AmazonS3-Type-control_AccountLevel-AdvancedDataProtectionMetrics "API_control_AccountLevel.md#AmazonS3-Type-control_AccountLevel-AdvancedDataProtectionMetrics")>
         <[IsEnabled](API_control_AdvancedDataProtectionMetrics.md#AmazonS3-Type-control_AdvancedDataProtectionMetrics-IsEnabled "API_control_AdvancedDataProtectionMetrics.md#AmazonS3-Type-control_AdvancedDataProtectionMetrics-IsEnabled")>***boolean***</[IsEnabled](API_control_AdvancedDataProtectionMetrics.md#AmazonS3-Type-control_AdvancedDataProtectionMetrics-IsEnabled "API_control_AdvancedDataProtectionMetrics.md#AmazonS3-Type-control_AdvancedDataProtectionMetrics-IsEnabled")>
      </[AdvancedDataProtectionMetrics](API_control_AccountLevel.md#AmazonS3-Type-control_AccountLevel-AdvancedDataProtectionMetrics "API_control_AccountLevel.md#AmazonS3-Type-control_AccountLevel-AdvancedDataProtectionMetrics")>
      <[BucketLevel](API_control_AccountLevel.md#AmazonS3-Type-control_AccountLevel-BucketLevel "API_control_AccountLevel.md#AmazonS3-Type-control_AccountLevel-BucketLevel")>
         <[ActivityMetrics](API_control_BucketLevel.md#AmazonS3-Type-control_BucketLevel-ActivityMetrics "API_control_BucketLevel.md#AmazonS3-Type-control_BucketLevel-ActivityMetrics")>
            <[IsEnabled](API_control_ActivityMetrics.md#AmazonS3-Type-control_ActivityMetrics-IsEnabled "API_control_ActivityMetrics.md#AmazonS3-Type-control_ActivityMetrics-IsEnabled")>***boolean***</[IsEnabled](API_control_ActivityMetrics.md#AmazonS3-Type-control_ActivityMetrics-IsEnabled "API_control_ActivityMetrics.md#AmazonS3-Type-control_ActivityMetrics-IsEnabled")>
         </[ActivityMetrics](API_control_BucketLevel.md#AmazonS3-Type-control_BucketLevel-ActivityMetrics "API_control_BucketLevel.md#AmazonS3-Type-control_BucketLevel-ActivityMetrics")>
         <[AdvancedCostOptimizationMetrics](API_control_BucketLevel.md#AmazonS3-Type-control_BucketLevel-AdvancedCostOptimizationMetrics "API_control_BucketLevel.md#AmazonS3-Type-control_BucketLevel-AdvancedCostOptimizationMetrics")>
            <[IsEnabled](API_control_AdvancedCostOptimizationMetrics.md#AmazonS3-Type-control_AdvancedCostOptimizationMetrics-IsEnabled "API_control_AdvancedCostOptimizationMetrics.md#AmazonS3-Type-control_AdvancedCostOptimizationMetrics-IsEnabled")>***boolean***</[IsEnabled](API_control_AdvancedCostOptimizationMetrics.md#AmazonS3-Type-control_AdvancedCostOptimizationMetrics-IsEnabled "API_control_AdvancedCostOptimizationMetrics.md#AmazonS3-Type-control_AdvancedCostOptimizationMetrics-IsEnabled")>
         </[AdvancedCostOptimizationMetrics](API_control_BucketLevel.md#AmazonS3-Type-control_BucketLevel-AdvancedCostOptimizationMetrics "API_control_BucketLevel.md#AmazonS3-Type-control_BucketLevel-AdvancedCostOptimizationMetrics")>
         <[AdvancedDataProtectionMetrics](API_control_BucketLevel.md#AmazonS3-Type-control_BucketLevel-AdvancedDataProtectionMetrics "API_control_BucketLevel.md#AmazonS3-Type-control_BucketLevel-AdvancedDataProtectionMetrics")>
            <[IsEnabled](API_control_AdvancedDataProtectionMetrics.md#AmazonS3-Type-control_AdvancedDataProtectionMetrics-IsEnabled "API_control_AdvancedDataProtectionMetrics.md#AmazonS3-Type-control_AdvancedDataProtectionMetrics-IsEnabled")>***boolean***</[IsEnabled](API_control_AdvancedDataProtectionMetrics.md#AmazonS3-Type-control_AdvancedDataProtectionMetrics-IsEnabled "API_control_AdvancedDataProtectionMetrics.md#AmazonS3-Type-control_AdvancedDataProtectionMetrics-IsEnabled")>
         </[AdvancedDataProtectionMetrics](API_control_BucketLevel.md#AmazonS3-Type-control_BucketLevel-AdvancedDataProtectionMetrics "API_control_BucketLevel.md#AmazonS3-Type-control_BucketLevel-AdvancedDataProtectionMetrics")>
         <[DetailedStatusCodesMetrics](API_control_BucketLevel.md#AmazonS3-Type-control_BucketLevel-DetailedStatusCodesMetrics "API_control_BucketLevel.md#AmazonS3-Type-control_BucketLevel-DetailedStatusCodesMetrics")>
            <[IsEnabled](API_control_DetailedStatusCodesMetrics.md#AmazonS3-Type-control_DetailedStatusCodesMetrics-IsEnabled "API_control_DetailedStatusCodesMetrics.md#AmazonS3-Type-control_DetailedStatusCodesMetrics-IsEnabled")>***boolean***</[IsEnabled](API_control_DetailedStatusCodesMetrics.md#AmazonS3-Type-control_DetailedStatusCodesMetrics-IsEnabled "API_control_DetailedStatusCodesMetrics.md#AmazonS3-Type-control_DetailedStatusCodesMetrics-IsEnabled")>
         </[DetailedStatusCodesMetrics](API_control_BucketLevel.md#AmazonS3-Type-control_BucketLevel-DetailedStatusCodesMetrics "API_control_BucketLevel.md#AmazonS3-Type-control_BucketLevel-DetailedStatusCodesMetrics")>
         <[PrefixLevel](API_control_BucketLevel.md#AmazonS3-Type-control_BucketLevel-PrefixLevel "API_control_BucketLevel.md#AmazonS3-Type-control_BucketLevel-PrefixLevel")>
            <[StorageMetrics](API_control_PrefixLevel.md#AmazonS3-Type-control_PrefixLevel-StorageMetrics "API_control_PrefixLevel.md#AmazonS3-Type-control_PrefixLevel-StorageMetrics")>
               <[IsEnabled](API_control_PrefixLevelStorageMetrics.md#AmazonS3-Type-control_PrefixLevelStorageMetrics-IsEnabled "API_control_PrefixLevelStorageMetrics.md#AmazonS3-Type-control_PrefixLevelStorageMetrics-IsEnabled")>***boolean***</[IsEnabled](API_control_PrefixLevelStorageMetrics.md#AmazonS3-Type-control_PrefixLevelStorageMetrics-IsEnabled "API_control_PrefixLevelStorageMetrics.md#AmazonS3-Type-control_PrefixLevelStorageMetrics-IsEnabled")>
               <[SelectionCriteria](API_control_PrefixLevelStorageMetrics.md#AmazonS3-Type-control_PrefixLevelStorageMetrics-SelectionCriteria "API_control_PrefixLevelStorageMetrics.md#AmazonS3-Type-control_PrefixLevelStorageMetrics-SelectionCriteria")>
                  <[Delimiter](API_control_SelectionCriteria.md#AmazonS3-Type-control_SelectionCriteria-Delimiter "API_control_SelectionCriteria.md#AmazonS3-Type-control_SelectionCriteria-Delimiter")>***string***</[Delimiter](API_control_SelectionCriteria.md#AmazonS3-Type-control_SelectionCriteria-Delimiter "API_control_SelectionCriteria.md#AmazonS3-Type-control_SelectionCriteria-Delimiter")>
                  <[MaxDepth](API_control_SelectionCriteria.md#AmazonS3-Type-control_SelectionCriteria-MaxDepth "API_control_SelectionCriteria.md#AmazonS3-Type-control_SelectionCriteria-MaxDepth")>***integer***</[MaxDepth](API_control_SelectionCriteria.md#AmazonS3-Type-control_SelectionCriteria-MaxDepth "API_control_SelectionCriteria.md#AmazonS3-Type-control_SelectionCriteria-MaxDepth")>
                  <[MinStorageBytesPercentage](API_control_SelectionCriteria.md#AmazonS3-Type-control_SelectionCriteria-MinStorageBytesPercentage "API_control_SelectionCriteria.md#AmazonS3-Type-control_SelectionCriteria-MinStorageBytesPercentage")>***double***</[MinStorageBytesPercentage](API_control_SelectionCriteria.md#AmazonS3-Type-control_SelectionCriteria-MinStorageBytesPercentage "API_control_SelectionCriteria.md#AmazonS3-Type-control_SelectionCriteria-MinStorageBytesPercentage")>
               </[SelectionCriteria](API_control_PrefixLevelStorageMetrics.md#AmazonS3-Type-control_PrefixLevelStorageMetrics-SelectionCriteria "API_control_PrefixLevelStorageMetrics.md#AmazonS3-Type-control_PrefixLevelStorageMetrics-SelectionCriteria")>
            </[StorageMetrics](API_control_PrefixLevel.md#AmazonS3-Type-control_PrefixLevel-StorageMetrics "API_control_PrefixLevel.md#AmazonS3-Type-control_PrefixLevel-StorageMetrics")>
         </[PrefixLevel](API_control_BucketLevel.md#AmazonS3-Type-control_BucketLevel-PrefixLevel "API_control_BucketLevel.md#AmazonS3-Type-control_BucketLevel-PrefixLevel")>
      </[BucketLevel](API_control_AccountLevel.md#AmazonS3-Type-control_AccountLevel-BucketLevel "API_control_AccountLevel.md#AmazonS3-Type-control_AccountLevel-BucketLevel")>
      <[DetailedStatusCodesMetrics](API_control_AccountLevel.md#AmazonS3-Type-control_AccountLevel-DetailedStatusCodesMetrics "API_control_AccountLevel.md#AmazonS3-Type-control_AccountLevel-DetailedStatusCodesMetrics")>
         <[IsEnabled](API_control_DetailedStatusCodesMetrics.md#AmazonS3-Type-control_DetailedStatusCodesMetrics-IsEnabled "API_control_DetailedStatusCodesMetrics.md#AmazonS3-Type-control_DetailedStatusCodesMetrics-IsEnabled")>***boolean***</[IsEnabled](API_control_DetailedStatusCodesMetrics.md#AmazonS3-Type-control_DetailedStatusCodesMetrics-IsEnabled "API_control_DetailedStatusCodesMetrics.md#AmazonS3-Type-control_DetailedStatusCodesMetrics-IsEnabled")>
      </[DetailedStatusCodesMetrics](API_control_AccountLevel.md#AmazonS3-Type-control_AccountLevel-DetailedStatusCodesMetrics "API_control_AccountLevel.md#AmazonS3-Type-control_AccountLevel-DetailedStatusCodesMetrics")>
      <[StorageLensGroupLevel](API_control_AccountLevel.md#AmazonS3-Type-control_AccountLevel-StorageLensGroupLevel "API_control_AccountLevel.md#AmazonS3-Type-control_AccountLevel-StorageLensGroupLevel")>
         <[SelectionCriteria](API_control_StorageLensGroupLevel.md#AmazonS3-Type-control_StorageLensGroupLevel-SelectionCriteria "API_control_StorageLensGroupLevel.md#AmazonS3-Type-control_StorageLensGroupLevel-SelectionCriteria")>
            <[Exclude](API_control_StorageLensGroupLevelSelectionCriteria.md#AmazonS3-Type-control_StorageLensGroupLevelSelectionCriteria-Exclude "API_control_StorageLensGroupLevelSelectionCriteria.md#AmazonS3-Type-control_StorageLensGroupLevelSelectionCriteria-Exclude")>
               <Arn>***string***</Arn>
            </[Exclude](API_control_StorageLensGroupLevelSelectionCriteria.md#AmazonS3-Type-control_StorageLensGroupLevelSelectionCriteria-Exclude "API_control_StorageLensGroupLevelSelectionCriteria.md#AmazonS3-Type-control_StorageLensGroupLevelSelectionCriteria-Exclude")>
            <[Include](API_control_StorageLensGroupLevelSelectionCriteria.md#AmazonS3-Type-control_StorageLensGroupLevelSelectionCriteria-Include "API_control_StorageLensGroupLevelSelectionCriteria.md#AmazonS3-Type-control_StorageLensGroupLevelSelectionCriteria-Include")>
               <Arn>***string***</Arn>
            </[Include](API_control_StorageLensGroupLevelSelectionCriteria.md#AmazonS3-Type-control_StorageLensGroupLevelSelectionCriteria-Include "API_control_StorageLensGroupLevelSelectionCriteria.md#AmazonS3-Type-control_StorageLensGroupLevelSelectionCriteria-Include")>
         </[SelectionCriteria](API_control_StorageLensGroupLevel.md#AmazonS3-Type-control_StorageLensGroupLevel-SelectionCriteria "API_control_StorageLensGroupLevel.md#AmazonS3-Type-control_StorageLensGroupLevel-SelectionCriteria")>
      </[StorageLensGroupLevel](API_control_AccountLevel.md#AmazonS3-Type-control_AccountLevel-StorageLensGroupLevel "API_control_AccountLevel.md#AmazonS3-Type-control_AccountLevel-StorageLensGroupLevel")>
   </[AccountLevel](#AmazonS3-control_GetStorageLensConfiguration-response-AccountLevel "#AmazonS3-control_GetStorageLensConfiguration-response-AccountLevel")>
   <[Include](#AmazonS3-control_GetStorageLensConfiguration-response-Include "#AmazonS3-control_GetStorageLensConfiguration-response-Include")>
      <[Buckets](API_control_Include.md#AmazonS3-Type-control_Include-Buckets "API_control_Include.md#AmazonS3-Type-control_Include-Buckets")>
         <Arn>***string***</Arn>
      </[Buckets](API_control_Include.md#AmazonS3-Type-control_Include-Buckets "API_control_Include.md#AmazonS3-Type-control_Include-Buckets")>
      <[Regions](API_control_Include.md#AmazonS3-Type-control_Include-Regions "API_control_Include.md#AmazonS3-Type-control_Include-Regions")>
         <Region>***string***</Region>
      </[Regions](API_control_Include.md#AmazonS3-Type-control_Include-Regions "API_control_Include.md#AmazonS3-Type-control_Include-Regions")>
   </[Include](#AmazonS3-control_GetStorageLensConfiguration-response-Include "#AmazonS3-control_GetStorageLensConfiguration-response-Include")>
   <[Exclude](#AmazonS3-control_GetStorageLensConfiguration-response-Exclude "#AmazonS3-control_GetStorageLensConfiguration-response-Exclude")>
      <[Buckets](API_control_Exclude.md#AmazonS3-Type-control_Exclude-Buckets "API_control_Exclude.md#AmazonS3-Type-control_Exclude-Buckets")>
         <Arn>***string***</Arn>
      </[Buckets](API_control_Exclude.md#AmazonS3-Type-control_Exclude-Buckets "API_control_Exclude.md#AmazonS3-Type-control_Exclude-Buckets")>
      <[Regions](API_control_Exclude.md#AmazonS3-Type-control_Exclude-Regions "API_control_Exclude.md#AmazonS3-Type-control_Exclude-Regions")>
         <Region>***string***</Region>
      </[Regions](API_control_Exclude.md#AmazonS3-Type-control_Exclude-Regions "API_control_Exclude.md#AmazonS3-Type-control_Exclude-Regions")>
   </[Exclude](#AmazonS3-control_GetStorageLensConfiguration-response-Exclude "#AmazonS3-control_GetStorageLensConfiguration-response-Exclude")>
   <[DataExport](#AmazonS3-control_GetStorageLensConfiguration-response-DataExport "#AmazonS3-control_GetStorageLensConfiguration-response-DataExport")>
      <[CloudWatchMetrics](API_control_StorageLensDataExport.md#AmazonS3-Type-control_StorageLensDataExport-CloudWatchMetrics "API_control_StorageLensDataExport.md#AmazonS3-Type-control_StorageLensDataExport-CloudWatchMetrics")>
         <[IsEnabled](API_control_CloudWatchMetrics.md#AmazonS3-Type-control_CloudWatchMetrics-IsEnabled "API_control_CloudWatchMetrics.md#AmazonS3-Type-control_CloudWatchMetrics-IsEnabled")>***boolean***</[IsEnabled](API_control_CloudWatchMetrics.md#AmazonS3-Type-control_CloudWatchMetrics-IsEnabled "API_control_CloudWatchMetrics.md#AmazonS3-Type-control_CloudWatchMetrics-IsEnabled")>
      </[CloudWatchMetrics](API_control_StorageLensDataExport.md#AmazonS3-Type-control_StorageLensDataExport-CloudWatchMetrics "API_control_StorageLensDataExport.md#AmazonS3-Type-control_StorageLensDataExport-CloudWatchMetrics")>
      <[S3BucketDestination](API_control_StorageLensDataExport.md#AmazonS3-Type-control_StorageLensDataExport-S3BucketDestination "API_control_StorageLensDataExport.md#AmazonS3-Type-control_StorageLensDataExport-S3BucketDestination")>
         <[AccountId](API_control_S3BucketDestination.md#AmazonS3-Type-control_S3BucketDestination-AccountId "API_control_S3BucketDestination.md#AmazonS3-Type-control_S3BucketDestination-AccountId")>***string***</[AccountId](API_control_S3BucketDestination.md#AmazonS3-Type-control_S3BucketDestination-AccountId "API_control_S3BucketDestination.md#AmazonS3-Type-control_S3BucketDestination-AccountId")>
         <[Arn](API_control_S3BucketDestination.md#AmazonS3-Type-control_S3BucketDestination-Arn "API_control_S3BucketDestination.md#AmazonS3-Type-control_S3BucketDestination-Arn")>***string***</[Arn](API_control_S3BucketDestination.md#AmazonS3-Type-control_S3BucketDestination-Arn "API_control_S3BucketDestination.md#AmazonS3-Type-control_S3BucketDestination-Arn")>
         <[Encryption](API_control_S3BucketDestination.md#AmazonS3-Type-control_S3BucketDestination-Encryption "API_control_S3BucketDestination.md#AmazonS3-Type-control_S3BucketDestination-Encryption")>
            <[SSE-KMS](API_control_StorageLensDataExportEncryption.md#AmazonS3-Type-control_StorageLensDataExportEncryption-SSEKMS "API_control_StorageLensDataExportEncryption.md#AmazonS3-Type-control_StorageLensDataExportEncryption-SSEKMS")>
               <[KeyId](API_control_SSEKMS.md#AmazonS3-Type-control_SSEKMS-KeyId "API_control_SSEKMS.md#AmazonS3-Type-control_SSEKMS-KeyId")>***string***</[KeyId](API_control_SSEKMS.md#AmazonS3-Type-control_SSEKMS-KeyId "API_control_SSEKMS.md#AmazonS3-Type-control_SSEKMS-KeyId")>
            </[SSE-KMS](API_control_StorageLensDataExportEncryption.md#AmazonS3-Type-control_StorageLensDataExportEncryption-SSEKMS "API_control_StorageLensDataExportEncryption.md#AmazonS3-Type-control_StorageLensDataExportEncryption-SSEKMS")>
            <[SSE-S3](API_control_StorageLensDataExportEncryption.md#AmazonS3-Type-control_StorageLensDataExportEncryption-SSES3 "API_control_StorageLensDataExportEncryption.md#AmazonS3-Type-control_StorageLensDataExportEncryption-SSES3")>
            </[SSE-S3](API_control_StorageLensDataExportEncryption.md#AmazonS3-Type-control_StorageLensDataExportEncryption-SSES3 "API_control_StorageLensDataExportEncryption.md#AmazonS3-Type-control_StorageLensDataExportEncryption-SSES3")>
         </[Encryption](API_control_S3BucketDestination.md#AmazonS3-Type-control_S3BucketDestination-Encryption "API_control_S3BucketDestination.md#AmazonS3-Type-control_S3BucketDestination-Encryption")>
         <[Format](API_control_S3BucketDestination.md#AmazonS3-Type-control_S3BucketDestination-Format "API_control_S3BucketDestination.md#AmazonS3-Type-control_S3BucketDestination-Format")>***string***</[Format](API_control_S3BucketDestination.md#AmazonS3-Type-control_S3BucketDestination-Format "API_control_S3BucketDestination.md#AmazonS3-Type-control_S3BucketDestination-Format")>
         <[OutputSchemaVersion](API_control_S3BucketDestination.md#AmazonS3-Type-control_S3BucketDestination-OutputSchemaVersion "API_control_S3BucketDestination.md#AmazonS3-Type-control_S3BucketDestination-OutputSchemaVersion")>***string***</[OutputSchemaVersion](API_control_S3BucketDestination.md#AmazonS3-Type-control_S3BucketDestination-OutputSchemaVersion "API_control_S3BucketDestination.md#AmazonS3-Type-control_S3BucketDestination-OutputSchemaVersion")>
         <[Prefix](API_control_S3BucketDestination.md#AmazonS3-Type-control_S3BucketDestination-Prefix "API_control_S3BucketDestination.md#AmazonS3-Type-control_S3BucketDestination-Prefix")>***string***</[Prefix](API_control_S3BucketDestination.md#AmazonS3-Type-control_S3BucketDestination-Prefix "API_control_S3BucketDestination.md#AmazonS3-Type-control_S3BucketDestination-Prefix")>
      </[S3BucketDestination](API_control_StorageLensDataExport.md#AmazonS3-Type-control_StorageLensDataExport-S3BucketDestination "API_control_StorageLensDataExport.md#AmazonS3-Type-control_StorageLensDataExport-S3BucketDestination")>
   </[DataExport](#AmazonS3-control_GetStorageLensConfiguration-response-DataExport "#AmazonS3-control_GetStorageLensConfiguration-response-DataExport")>
   <[IsEnabled](#AmazonS3-control_GetStorageLensConfiguration-response-IsEnabled "#AmazonS3-control_GetStorageLensConfiguration-response-IsEnabled")>***boolean***</[IsEnabled](#AmazonS3-control_GetStorageLensConfiguration-response-IsEnabled "#AmazonS3-control_GetStorageLensConfiguration-response-IsEnabled")>
   <[AwsOrg](#AmazonS3-control_GetStorageLensConfiguration-response-AwsOrg "#AmazonS3-control_GetStorageLensConfiguration-response-AwsOrg")>
      <[Arn](API_control_StorageLensAwsOrg.md#AmazonS3-Type-control_StorageLensAwsOrg-Arn "API_control_StorageLensAwsOrg.md#AmazonS3-Type-control_StorageLensAwsOrg-Arn")>***string***</[Arn](API_control_StorageLensAwsOrg.md#AmazonS3-Type-control_StorageLensAwsOrg-Arn "API_control_StorageLensAwsOrg.md#AmazonS3-Type-control_StorageLensAwsOrg-Arn")>
   </[AwsOrg](#AmazonS3-control_GetStorageLensConfiguration-response-AwsOrg "#AmazonS3-control_GetStorageLensConfiguration-response-AwsOrg")>
   <[StorageLensArn](#AmazonS3-control_GetStorageLensConfiguration-response-StorageLensArn "#AmazonS3-control_GetStorageLensConfiguration-response-StorageLensArn")>***string***</[StorageLensArn](#AmazonS3-control_GetStorageLensConfiguration-response-StorageLensArn "#AmazonS3-control_GetStorageLensConfiguration-response-StorageLensArn")>
</[StorageLensConfiguration](#AmazonS3-control_GetStorageLensConfiguration-response-StorageLensConfiguration "#AmazonS3-control_GetStorageLensConfiguration-response-StorageLensConfiguration")>
```

## Response Elements


If the action is successful, the service sends back an HTTP 200 response.


The following data is returned in XML format by the service.





**[StorageLensConfiguration](#API_control_GetStorageLensConfiguration_ResponseSyntax "#API_control_GetStorageLensConfiguration_ResponseSyntax")**


Root level tag for the StorageLensConfiguration parameters.


Required: Yes




**[AccountLevel](#API_control_GetStorageLensConfiguration_ResponseSyntax "#API_control_GetStorageLensConfiguration_ResponseSyntax")**


A container for all the account-level configurations of your S3 Storage Lens
 configuration.


Type: [AccountLevel](API_control_AccountLevel.md "API_control_AccountLevel.md") data type




**[AwsOrg](#API_control_GetStorageLensConfiguration_ResponseSyntax "#API_control_GetStorageLensConfiguration_ResponseSyntax")**


A container for the AWS organization for this S3 Storage Lens configuration.


Type: [StorageLensAwsOrg](API_control_StorageLensAwsOrg.md "API_control_StorageLensAwsOrg.md") data type




**[DataExport](#API_control_GetStorageLensConfiguration_ResponseSyntax "#API_control_GetStorageLensConfiguration_ResponseSyntax")**


A container to specify the properties of your S3 Storage Lens metrics export including, the
 destination, schema and format.


Type: [StorageLensDataExport](API_control_StorageLensDataExport.md "API_control_StorageLensDataExport.md") data type




**[Exclude](#API_control_GetStorageLensConfiguration_ResponseSyntax "#API_control_GetStorageLensConfiguration_ResponseSyntax")**


A container for what is excluded in this configuration. This container can only be valid
 if there is no `Include` container submitted, and it's not empty. 


Type: [Exclude](API_control_Exclude.md "API_control_Exclude.md") data type




**[Id](#API_control_GetStorageLensConfiguration_ResponseSyntax "#API_control_GetStorageLensConfiguration_ResponseSyntax")**


A container for the Amazon S3 Storage Lens configuration ID.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 64.


Pattern: `[a-zA-Z0-9\-\_\.]+`





**[Include](#API_control_GetStorageLensConfiguration_ResponseSyntax "#API_control_GetStorageLensConfiguration_ResponseSyntax")**


A container for what is included in this configuration. This container can only be valid
 if there is no `Exclude` container submitted, and it's not empty. 


Type: [Include](API_control_Include.md "API_control_Include.md") data type




**[IsEnabled](#API_control_GetStorageLensConfiguration_ResponseSyntax "#API_control_GetStorageLensConfiguration_ResponseSyntax")**


A container for whether the S3 Storage Lens configuration is enabled.


Type: Boolean




**[StorageLensArn](#API_control_GetStorageLensConfiguration_ResponseSyntax "#API_control_GetStorageLensConfiguration_ResponseSyntax")**


The Amazon Resource Name (ARN) of the S3 Storage Lens configuration. This property is read-only
 and follows the following format: `arn:aws:s3:*us-east-1*:*example-account-id*:storage-lens/*your-dashboard-name*`



Type: String


Length Constraints: Minimum length of 1. Maximum length of 1024.


Pattern: `arn:[a-z\-]+:s3:[a-z0-9\-]+:\d{12}:storage\-lens\/.*`





## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface](https://docs.aws.amazon.com/goto/cli2/s3control-2018-08-20/GetStorageLensConfiguration "https://docs.aws.amazon.com/goto/cli2/s3control-2018-08-20/GetStorageLensConfiguration")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/s3control-2018-08-20/GetStorageLensConfiguration "https://docs.aws.amazon.com/goto/DotNetSDKV3/s3control-2018-08-20/GetStorageLensConfiguration")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/GetStorageLensConfiguration "https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/GetStorageLensConfiguration")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/s3control-2018-08-20/GetStorageLensConfiguration "https://docs.aws.amazon.com/goto/SdkForGoV2/s3control-2018-08-20/GetStorageLensConfiguration")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/GetStorageLensConfiguration "https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/GetStorageLensConfiguration")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3control-2018-08-20/GetStorageLensConfiguration "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3control-2018-08-20/GetStorageLensConfiguration")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/s3control-2018-08-20/GetStorageLensConfiguration "https://docs.aws.amazon.com/goto/SdkForKotlin/s3control-2018-08-20/GetStorageLensConfiguration")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/s3control-2018-08-20/GetStorageLensConfiguration "https://docs.aws.amazon.com/goto/SdkForPHPV3/s3control-2018-08-20/GetStorageLensConfiguration")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/s3control-2018-08-20/GetStorageLensConfiguration "https://docs.aws.amazon.com/goto/boto3/s3control-2018-08-20/GetStorageLensConfiguration")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/GetStorageLensConfiguration "https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/GetStorageLensConfiguration")
