# PutStorageLensConfiguration

###### Note

This operation is not supported by directory buckets.

Puts an Amazon S3 Storage Lens configuration. For more information about S3 Storage Lens, see [Working with
 Amazon S3 Storage Lens](https://docs.aws.amazon.com/AmazonS3/latest/dev/storage_lens.html "https://docs.aws.amazon.com/AmazonS3/latest/dev/storage_lens.html") in the *Amazon S3 User Guide*. For a complete list of S3 Storage Lens metrics, see [S3 Storage Lens metrics glossary](../userguide/storage_lens_metrics_glossary.md "../userguide/storage_lens_metrics_glossary.md") in the *Amazon S3 User Guide*.

###### Note

To use this action, you must have permission to perform the
 `s3:PutStorageLensConfiguration` action. For more information, see [Setting permissions to use Amazon S3 Storage Lens](https://docs.aws.amazon.com/AmazonS3/latest/dev/storage_lens_iam_permissions.html "https://docs.aws.amazon.com/AmazonS3/latest/dev/storage_lens_iam_permissions.html") in the
 *Amazon S3 User Guide*.

###### Important

You must URL encode any signed header values that contain spaces. For example, if your header value is `my file.txt`, containing two spaces after `my`, you must URL encode this value to `my%20%20file.txt`.


## Request Syntax



```
PUT /v20180820/storagelens/`storagelensid` HTTP/1.1
Host: s3-control.amazonaws.com
x-amz-account-id: `AccountId`
<?xml version="1.0" encoding="UTF-8"?>
<[PutStorageLensConfigurationRequest](#AmazonS3-control_PutStorageLensConfiguration-request-PutStorageLensConfigurationRequest "#AmazonS3-control_PutStorageLensConfiguration-request-PutStorageLensConfigurationRequest") xmlns="http://awss3control.amazonaws.com/doc/2018-08-20/">
   <[StorageLensConfiguration](#AmazonS3-control_PutStorageLensConfiguration-request-StorageLensConfiguration "#AmazonS3-control_PutStorageLensConfiguration-request-StorageLensConfiguration")>
      <[AccountLevel](API_control_StorageLensConfiguration.md#AmazonS3-Type-control_StorageLensConfiguration-AccountLevel "API_control_StorageLensConfiguration.md#AmazonS3-Type-control_StorageLensConfiguration-AccountLevel")>
         <[ActivityMetrics](API_control_AccountLevel.md#AmazonS3-Type-control_AccountLevel-ActivityMetrics "API_control_AccountLevel.md#AmazonS3-Type-control_AccountLevel-ActivityMetrics")>
            <[IsEnabled](API_control_ActivityMetrics.md#AmazonS3-Type-control_ActivityMetrics-IsEnabled "API_control_ActivityMetrics.md#AmazonS3-Type-control_ActivityMetrics-IsEnabled")>`boolean`</[IsEnabled](API_control_ActivityMetrics.md#AmazonS3-Type-control_ActivityMetrics-IsEnabled "API_control_ActivityMetrics.md#AmazonS3-Type-control_ActivityMetrics-IsEnabled")>
         </[ActivityMetrics](API_control_AccountLevel.md#AmazonS3-Type-control_AccountLevel-ActivityMetrics "API_control_AccountLevel.md#AmazonS3-Type-control_AccountLevel-ActivityMetrics")>
         <[AdvancedCostOptimizationMetrics](API_control_AccountLevel.md#AmazonS3-Type-control_AccountLevel-AdvancedCostOptimizationMetrics "API_control_AccountLevel.md#AmazonS3-Type-control_AccountLevel-AdvancedCostOptimizationMetrics")>
            <[IsEnabled](API_control_AdvancedCostOptimizationMetrics.md#AmazonS3-Type-control_AdvancedCostOptimizationMetrics-IsEnabled "API_control_AdvancedCostOptimizationMetrics.md#AmazonS3-Type-control_AdvancedCostOptimizationMetrics-IsEnabled")>`boolean`</[IsEnabled](API_control_AdvancedCostOptimizationMetrics.md#AmazonS3-Type-control_AdvancedCostOptimizationMetrics-IsEnabled "API_control_AdvancedCostOptimizationMetrics.md#AmazonS3-Type-control_AdvancedCostOptimizationMetrics-IsEnabled")>
         </[AdvancedCostOptimizationMetrics](API_control_AccountLevel.md#AmazonS3-Type-control_AccountLevel-AdvancedCostOptimizationMetrics "API_control_AccountLevel.md#AmazonS3-Type-control_AccountLevel-AdvancedCostOptimizationMetrics")>
         <[AdvancedDataProtectionMetrics](API_control_AccountLevel.md#AmazonS3-Type-control_AccountLevel-AdvancedDataProtectionMetrics "API_control_AccountLevel.md#AmazonS3-Type-control_AccountLevel-AdvancedDataProtectionMetrics")>
            <[IsEnabled](API_control_AdvancedDataProtectionMetrics.md#AmazonS3-Type-control_AdvancedDataProtectionMetrics-IsEnabled "API_control_AdvancedDataProtectionMetrics.md#AmazonS3-Type-control_AdvancedDataProtectionMetrics-IsEnabled")>`boolean`</[IsEnabled](API_control_AdvancedDataProtectionMetrics.md#AmazonS3-Type-control_AdvancedDataProtectionMetrics-IsEnabled "API_control_AdvancedDataProtectionMetrics.md#AmazonS3-Type-control_AdvancedDataProtectionMetrics-IsEnabled")>
         </[AdvancedDataProtectionMetrics](API_control_AccountLevel.md#AmazonS3-Type-control_AccountLevel-AdvancedDataProtectionMetrics "API_control_AccountLevel.md#AmazonS3-Type-control_AccountLevel-AdvancedDataProtectionMetrics")>
         <[BucketLevel](API_control_AccountLevel.md#AmazonS3-Type-control_AccountLevel-BucketLevel "API_control_AccountLevel.md#AmazonS3-Type-control_AccountLevel-BucketLevel")>
            <[ActivityMetrics](API_control_BucketLevel.md#AmazonS3-Type-control_BucketLevel-ActivityMetrics "API_control_BucketLevel.md#AmazonS3-Type-control_BucketLevel-ActivityMetrics")>
               <[IsEnabled](API_control_ActivityMetrics.md#AmazonS3-Type-control_ActivityMetrics-IsEnabled "API_control_ActivityMetrics.md#AmazonS3-Type-control_ActivityMetrics-IsEnabled")>`boolean`</[IsEnabled](API_control_ActivityMetrics.md#AmazonS3-Type-control_ActivityMetrics-IsEnabled "API_control_ActivityMetrics.md#AmazonS3-Type-control_ActivityMetrics-IsEnabled")>
            </[ActivityMetrics](API_control_BucketLevel.md#AmazonS3-Type-control_BucketLevel-ActivityMetrics "API_control_BucketLevel.md#AmazonS3-Type-control_BucketLevel-ActivityMetrics")>
            <[AdvancedCostOptimizationMetrics](API_control_BucketLevel.md#AmazonS3-Type-control_BucketLevel-AdvancedCostOptimizationMetrics "API_control_BucketLevel.md#AmazonS3-Type-control_BucketLevel-AdvancedCostOptimizationMetrics")>
               <[IsEnabled](API_control_AdvancedCostOptimizationMetrics.md#AmazonS3-Type-control_AdvancedCostOptimizationMetrics-IsEnabled "API_control_AdvancedCostOptimizationMetrics.md#AmazonS3-Type-control_AdvancedCostOptimizationMetrics-IsEnabled")>`boolean`</[IsEnabled](API_control_AdvancedCostOptimizationMetrics.md#AmazonS3-Type-control_AdvancedCostOptimizationMetrics-IsEnabled "API_control_AdvancedCostOptimizationMetrics.md#AmazonS3-Type-control_AdvancedCostOptimizationMetrics-IsEnabled")>
            </[AdvancedCostOptimizationMetrics](API_control_BucketLevel.md#AmazonS3-Type-control_BucketLevel-AdvancedCostOptimizationMetrics "API_control_BucketLevel.md#AmazonS3-Type-control_BucketLevel-AdvancedCostOptimizationMetrics")>
            <[AdvancedDataProtectionMetrics](API_control_BucketLevel.md#AmazonS3-Type-control_BucketLevel-AdvancedDataProtectionMetrics "API_control_BucketLevel.md#AmazonS3-Type-control_BucketLevel-AdvancedDataProtectionMetrics")>
               <[IsEnabled](API_control_AdvancedDataProtectionMetrics.md#AmazonS3-Type-control_AdvancedDataProtectionMetrics-IsEnabled "API_control_AdvancedDataProtectionMetrics.md#AmazonS3-Type-control_AdvancedDataProtectionMetrics-IsEnabled")>`boolean`</[IsEnabled](API_control_AdvancedDataProtectionMetrics.md#AmazonS3-Type-control_AdvancedDataProtectionMetrics-IsEnabled "API_control_AdvancedDataProtectionMetrics.md#AmazonS3-Type-control_AdvancedDataProtectionMetrics-IsEnabled")>
            </[AdvancedDataProtectionMetrics](API_control_BucketLevel.md#AmazonS3-Type-control_BucketLevel-AdvancedDataProtectionMetrics "API_control_BucketLevel.md#AmazonS3-Type-control_BucketLevel-AdvancedDataProtectionMetrics")>
            <[DetailedStatusCodesMetrics](API_control_BucketLevel.md#AmazonS3-Type-control_BucketLevel-DetailedStatusCodesMetrics "API_control_BucketLevel.md#AmazonS3-Type-control_BucketLevel-DetailedStatusCodesMetrics")>
               <[IsEnabled](API_control_DetailedStatusCodesMetrics.md#AmazonS3-Type-control_DetailedStatusCodesMetrics-IsEnabled "API_control_DetailedStatusCodesMetrics.md#AmazonS3-Type-control_DetailedStatusCodesMetrics-IsEnabled")>`boolean`</[IsEnabled](API_control_DetailedStatusCodesMetrics.md#AmazonS3-Type-control_DetailedStatusCodesMetrics-IsEnabled "API_control_DetailedStatusCodesMetrics.md#AmazonS3-Type-control_DetailedStatusCodesMetrics-IsEnabled")>
            </[DetailedStatusCodesMetrics](API_control_BucketLevel.md#AmazonS3-Type-control_BucketLevel-DetailedStatusCodesMetrics "API_control_BucketLevel.md#AmazonS3-Type-control_BucketLevel-DetailedStatusCodesMetrics")>
            <[PrefixLevel](API_control_BucketLevel.md#AmazonS3-Type-control_BucketLevel-PrefixLevel "API_control_BucketLevel.md#AmazonS3-Type-control_BucketLevel-PrefixLevel")>
               <[StorageMetrics](API_control_PrefixLevel.md#AmazonS3-Type-control_PrefixLevel-StorageMetrics "API_control_PrefixLevel.md#AmazonS3-Type-control_PrefixLevel-StorageMetrics")>
                  <[IsEnabled](API_control_PrefixLevelStorageMetrics.md#AmazonS3-Type-control_PrefixLevelStorageMetrics-IsEnabled "API_control_PrefixLevelStorageMetrics.md#AmazonS3-Type-control_PrefixLevelStorageMetrics-IsEnabled")>`boolean`</[IsEnabled](API_control_PrefixLevelStorageMetrics.md#AmazonS3-Type-control_PrefixLevelStorageMetrics-IsEnabled "API_control_PrefixLevelStorageMetrics.md#AmazonS3-Type-control_PrefixLevelStorageMetrics-IsEnabled")>
                  <[SelectionCriteria](API_control_PrefixLevelStorageMetrics.md#AmazonS3-Type-control_PrefixLevelStorageMetrics-SelectionCriteria "API_control_PrefixLevelStorageMetrics.md#AmazonS3-Type-control_PrefixLevelStorageMetrics-SelectionCriteria")>
                     <[Delimiter](API_control_SelectionCriteria.md#AmazonS3-Type-control_SelectionCriteria-Delimiter "API_control_SelectionCriteria.md#AmazonS3-Type-control_SelectionCriteria-Delimiter")>`string`</[Delimiter](API_control_SelectionCriteria.md#AmazonS3-Type-control_SelectionCriteria-Delimiter "API_control_SelectionCriteria.md#AmazonS3-Type-control_SelectionCriteria-Delimiter")>
                     <[MaxDepth](API_control_SelectionCriteria.md#AmazonS3-Type-control_SelectionCriteria-MaxDepth "API_control_SelectionCriteria.md#AmazonS3-Type-control_SelectionCriteria-MaxDepth")>`integer`</[MaxDepth](API_control_SelectionCriteria.md#AmazonS3-Type-control_SelectionCriteria-MaxDepth "API_control_SelectionCriteria.md#AmazonS3-Type-control_SelectionCriteria-MaxDepth")>
                     <[MinStorageBytesPercentage](API_control_SelectionCriteria.md#AmazonS3-Type-control_SelectionCriteria-MinStorageBytesPercentage "API_control_SelectionCriteria.md#AmazonS3-Type-control_SelectionCriteria-MinStorageBytesPercentage")>`double`</[MinStorageBytesPercentage](API_control_SelectionCriteria.md#AmazonS3-Type-control_SelectionCriteria-MinStorageBytesPercentage "API_control_SelectionCriteria.md#AmazonS3-Type-control_SelectionCriteria-MinStorageBytesPercentage")>
                  </[SelectionCriteria](API_control_PrefixLevelStorageMetrics.md#AmazonS3-Type-control_PrefixLevelStorageMetrics-SelectionCriteria "API_control_PrefixLevelStorageMetrics.md#AmazonS3-Type-control_PrefixLevelStorageMetrics-SelectionCriteria")>
               </[StorageMetrics](API_control_PrefixLevel.md#AmazonS3-Type-control_PrefixLevel-StorageMetrics "API_control_PrefixLevel.md#AmazonS3-Type-control_PrefixLevel-StorageMetrics")>
            </[PrefixLevel](API_control_BucketLevel.md#AmazonS3-Type-control_BucketLevel-PrefixLevel "API_control_BucketLevel.md#AmazonS3-Type-control_BucketLevel-PrefixLevel")>
         </[BucketLevel](API_control_AccountLevel.md#AmazonS3-Type-control_AccountLevel-BucketLevel "API_control_AccountLevel.md#AmazonS3-Type-control_AccountLevel-BucketLevel")>
         <[DetailedStatusCodesMetrics](API_control_AccountLevel.md#AmazonS3-Type-control_AccountLevel-DetailedStatusCodesMetrics "API_control_AccountLevel.md#AmazonS3-Type-control_AccountLevel-DetailedStatusCodesMetrics")>
            <[IsEnabled](API_control_DetailedStatusCodesMetrics.md#AmazonS3-Type-control_DetailedStatusCodesMetrics-IsEnabled "API_control_DetailedStatusCodesMetrics.md#AmazonS3-Type-control_DetailedStatusCodesMetrics-IsEnabled")>`boolean`</[IsEnabled](API_control_DetailedStatusCodesMetrics.md#AmazonS3-Type-control_DetailedStatusCodesMetrics-IsEnabled "API_control_DetailedStatusCodesMetrics.md#AmazonS3-Type-control_DetailedStatusCodesMetrics-IsEnabled")>
         </[DetailedStatusCodesMetrics](API_control_AccountLevel.md#AmazonS3-Type-control_AccountLevel-DetailedStatusCodesMetrics "API_control_AccountLevel.md#AmazonS3-Type-control_AccountLevel-DetailedStatusCodesMetrics")>
         <[StorageLensGroupLevel](API_control_AccountLevel.md#AmazonS3-Type-control_AccountLevel-StorageLensGroupLevel "API_control_AccountLevel.md#AmazonS3-Type-control_AccountLevel-StorageLensGroupLevel")>
            <[SelectionCriteria](API_control_StorageLensGroupLevel.md#AmazonS3-Type-control_StorageLensGroupLevel-SelectionCriteria "API_control_StorageLensGroupLevel.md#AmazonS3-Type-control_StorageLensGroupLevel-SelectionCriteria")>
               <[Exclude](API_control_StorageLensGroupLevelSelectionCriteria.md#AmazonS3-Type-control_StorageLensGroupLevelSelectionCriteria-Exclude "API_control_StorageLensGroupLevelSelectionCriteria.md#AmazonS3-Type-control_StorageLensGroupLevelSelectionCriteria-Exclude")>
                  <Arn>`string`</Arn>
               </[Exclude](API_control_StorageLensGroupLevelSelectionCriteria.md#AmazonS3-Type-control_StorageLensGroupLevelSelectionCriteria-Exclude "API_control_StorageLensGroupLevelSelectionCriteria.md#AmazonS3-Type-control_StorageLensGroupLevelSelectionCriteria-Exclude")>
               <[Include](API_control_StorageLensGroupLevelSelectionCriteria.md#AmazonS3-Type-control_StorageLensGroupLevelSelectionCriteria-Include "API_control_StorageLensGroupLevelSelectionCriteria.md#AmazonS3-Type-control_StorageLensGroupLevelSelectionCriteria-Include")>
                  <Arn>`string`</Arn>
               </[Include](API_control_StorageLensGroupLevelSelectionCriteria.md#AmazonS3-Type-control_StorageLensGroupLevelSelectionCriteria-Include "API_control_StorageLensGroupLevelSelectionCriteria.md#AmazonS3-Type-control_StorageLensGroupLevelSelectionCriteria-Include")>
            </[SelectionCriteria](API_control_StorageLensGroupLevel.md#AmazonS3-Type-control_StorageLensGroupLevel-SelectionCriteria "API_control_StorageLensGroupLevel.md#AmazonS3-Type-control_StorageLensGroupLevel-SelectionCriteria")>
         </[StorageLensGroupLevel](API_control_AccountLevel.md#AmazonS3-Type-control_AccountLevel-StorageLensGroupLevel "API_control_AccountLevel.md#AmazonS3-Type-control_AccountLevel-StorageLensGroupLevel")>
      </[AccountLevel](API_control_StorageLensConfiguration.md#AmazonS3-Type-control_StorageLensConfiguration-AccountLevel "API_control_StorageLensConfiguration.md#AmazonS3-Type-control_StorageLensConfiguration-AccountLevel")>
      <[AwsOrg](API_control_StorageLensConfiguration.md#AmazonS3-Type-control_StorageLensConfiguration-AwsOrg "API_control_StorageLensConfiguration.md#AmazonS3-Type-control_StorageLensConfiguration-AwsOrg")>
         <[Arn](API_control_StorageLensAwsOrg.md#AmazonS3-Type-control_StorageLensAwsOrg-Arn "API_control_StorageLensAwsOrg.md#AmazonS3-Type-control_StorageLensAwsOrg-Arn")>`string`</[Arn](API_control_StorageLensAwsOrg.md#AmazonS3-Type-control_StorageLensAwsOrg-Arn "API_control_StorageLensAwsOrg.md#AmazonS3-Type-control_StorageLensAwsOrg-Arn")>
      </[AwsOrg](API_control_StorageLensConfiguration.md#AmazonS3-Type-control_StorageLensConfiguration-AwsOrg "API_control_StorageLensConfiguration.md#AmazonS3-Type-control_StorageLensConfiguration-AwsOrg")>
      <[DataExport](API_control_StorageLensConfiguration.md#AmazonS3-Type-control_StorageLensConfiguration-DataExport "API_control_StorageLensConfiguration.md#AmazonS3-Type-control_StorageLensConfiguration-DataExport")>
         <[CloudWatchMetrics](API_control_StorageLensDataExport.md#AmazonS3-Type-control_StorageLensDataExport-CloudWatchMetrics "API_control_StorageLensDataExport.md#AmazonS3-Type-control_StorageLensDataExport-CloudWatchMetrics")>
            <[IsEnabled](API_control_CloudWatchMetrics.md#AmazonS3-Type-control_CloudWatchMetrics-IsEnabled "API_control_CloudWatchMetrics.md#AmazonS3-Type-control_CloudWatchMetrics-IsEnabled")>`boolean`</[IsEnabled](API_control_CloudWatchMetrics.md#AmazonS3-Type-control_CloudWatchMetrics-IsEnabled "API_control_CloudWatchMetrics.md#AmazonS3-Type-control_CloudWatchMetrics-IsEnabled")>
         </[CloudWatchMetrics](API_control_StorageLensDataExport.md#AmazonS3-Type-control_StorageLensDataExport-CloudWatchMetrics "API_control_StorageLensDataExport.md#AmazonS3-Type-control_StorageLensDataExport-CloudWatchMetrics")>
         <[S3BucketDestination](API_control_StorageLensDataExport.md#AmazonS3-Type-control_StorageLensDataExport-S3BucketDestination "API_control_StorageLensDataExport.md#AmazonS3-Type-control_StorageLensDataExport-S3BucketDestination")>
            <[AccountId](API_control_S3BucketDestination.md#AmazonS3-Type-control_S3BucketDestination-AccountId "API_control_S3BucketDestination.md#AmazonS3-Type-control_S3BucketDestination-AccountId")>`string`</[AccountId](API_control_S3BucketDestination.md#AmazonS3-Type-control_S3BucketDestination-AccountId "API_control_S3BucketDestination.md#AmazonS3-Type-control_S3BucketDestination-AccountId")>
            <[Arn](API_control_S3BucketDestination.md#AmazonS3-Type-control_S3BucketDestination-Arn "API_control_S3BucketDestination.md#AmazonS3-Type-control_S3BucketDestination-Arn")>`string`</[Arn](API_control_S3BucketDestination.md#AmazonS3-Type-control_S3BucketDestination-Arn "API_control_S3BucketDestination.md#AmazonS3-Type-control_S3BucketDestination-Arn")>
            <[Encryption](API_control_S3BucketDestination.md#AmazonS3-Type-control_S3BucketDestination-Encryption "API_control_S3BucketDestination.md#AmazonS3-Type-control_S3BucketDestination-Encryption")>
               <[SSE-KMS](API_control_StorageLensDataExportEncryption.md#AmazonS3-Type-control_StorageLensDataExportEncryption-SSEKMS "API_control_StorageLensDataExportEncryption.md#AmazonS3-Type-control_StorageLensDataExportEncryption-SSEKMS")>
                  <[KeyId](API_control_SSEKMS.md#AmazonS3-Type-control_SSEKMS-KeyId "API_control_SSEKMS.md#AmazonS3-Type-control_SSEKMS-KeyId")>`string`</[KeyId](API_control_SSEKMS.md#AmazonS3-Type-control_SSEKMS-KeyId "API_control_SSEKMS.md#AmazonS3-Type-control_SSEKMS-KeyId")>
               </[SSE-KMS](API_control_StorageLensDataExportEncryption.md#AmazonS3-Type-control_StorageLensDataExportEncryption-SSEKMS "API_control_StorageLensDataExportEncryption.md#AmazonS3-Type-control_StorageLensDataExportEncryption-SSEKMS")>
               <[SSE-S3](API_control_StorageLensDataExportEncryption.md#AmazonS3-Type-control_StorageLensDataExportEncryption-SSES3 "API_control_StorageLensDataExportEncryption.md#AmazonS3-Type-control_StorageLensDataExportEncryption-SSES3")>
               </[SSE-S3](API_control_StorageLensDataExportEncryption.md#AmazonS3-Type-control_StorageLensDataExportEncryption-SSES3 "API_control_StorageLensDataExportEncryption.md#AmazonS3-Type-control_StorageLensDataExportEncryption-SSES3")>
            </[Encryption](API_control_S3BucketDestination.md#AmazonS3-Type-control_S3BucketDestination-Encryption "API_control_S3BucketDestination.md#AmazonS3-Type-control_S3BucketDestination-Encryption")>
            <[Format](API_control_S3BucketDestination.md#AmazonS3-Type-control_S3BucketDestination-Format "API_control_S3BucketDestination.md#AmazonS3-Type-control_S3BucketDestination-Format")>`string`</[Format](API_control_S3BucketDestination.md#AmazonS3-Type-control_S3BucketDestination-Format "API_control_S3BucketDestination.md#AmazonS3-Type-control_S3BucketDestination-Format")>
            <[OutputSchemaVersion](API_control_S3BucketDestination.md#AmazonS3-Type-control_S3BucketDestination-OutputSchemaVersion "API_control_S3BucketDestination.md#AmazonS3-Type-control_S3BucketDestination-OutputSchemaVersion")>`string`</[OutputSchemaVersion](API_control_S3BucketDestination.md#AmazonS3-Type-control_S3BucketDestination-OutputSchemaVersion "API_control_S3BucketDestination.md#AmazonS3-Type-control_S3BucketDestination-OutputSchemaVersion")>
            <[Prefix](API_control_S3BucketDestination.md#AmazonS3-Type-control_S3BucketDestination-Prefix "API_control_S3BucketDestination.md#AmazonS3-Type-control_S3BucketDestination-Prefix")>`string`</[Prefix](API_control_S3BucketDestination.md#AmazonS3-Type-control_S3BucketDestination-Prefix "API_control_S3BucketDestination.md#AmazonS3-Type-control_S3BucketDestination-Prefix")>
         </[S3BucketDestination](API_control_StorageLensDataExport.md#AmazonS3-Type-control_StorageLensDataExport-S3BucketDestination "API_control_StorageLensDataExport.md#AmazonS3-Type-control_StorageLensDataExport-S3BucketDestination")>
      </[DataExport](API_control_StorageLensConfiguration.md#AmazonS3-Type-control_StorageLensConfiguration-DataExport "API_control_StorageLensConfiguration.md#AmazonS3-Type-control_StorageLensConfiguration-DataExport")>
      <[Exclude](API_control_StorageLensConfiguration.md#AmazonS3-Type-control_StorageLensConfiguration-Exclude "API_control_StorageLensConfiguration.md#AmazonS3-Type-control_StorageLensConfiguration-Exclude")>
         <[Buckets](API_control_Exclude.md#AmazonS3-Type-control_Exclude-Buckets "API_control_Exclude.md#AmazonS3-Type-control_Exclude-Buckets")>
            <Arn>`string`</Arn>
         </[Buckets](API_control_Exclude.md#AmazonS3-Type-control_Exclude-Buckets "API_control_Exclude.md#AmazonS3-Type-control_Exclude-Buckets")>
         <[Regions](API_control_Exclude.md#AmazonS3-Type-control_Exclude-Regions "API_control_Exclude.md#AmazonS3-Type-control_Exclude-Regions")>
            <Region>`string`</Region>
         </[Regions](API_control_Exclude.md#AmazonS3-Type-control_Exclude-Regions "API_control_Exclude.md#AmazonS3-Type-control_Exclude-Regions")>
      </[Exclude](API_control_StorageLensConfiguration.md#AmazonS3-Type-control_StorageLensConfiguration-Exclude "API_control_StorageLensConfiguration.md#AmazonS3-Type-control_StorageLensConfiguration-Exclude")>
      <[Id](API_control_StorageLensConfiguration.md#AmazonS3-Type-control_StorageLensConfiguration-Id "API_control_StorageLensConfiguration.md#AmazonS3-Type-control_StorageLensConfiguration-Id")>`string`</[Id](API_control_StorageLensConfiguration.md#AmazonS3-Type-control_StorageLensConfiguration-Id "API_control_StorageLensConfiguration.md#AmazonS3-Type-control_StorageLensConfiguration-Id")>
      <[Include](API_control_StorageLensConfiguration.md#AmazonS3-Type-control_StorageLensConfiguration-Include "API_control_StorageLensConfiguration.md#AmazonS3-Type-control_StorageLensConfiguration-Include")>
         <[Buckets](API_control_Include.md#AmazonS3-Type-control_Include-Buckets "API_control_Include.md#AmazonS3-Type-control_Include-Buckets")>
            <Arn>`string`</Arn>
         </[Buckets](API_control_Include.md#AmazonS3-Type-control_Include-Buckets "API_control_Include.md#AmazonS3-Type-control_Include-Buckets")>
         <[Regions](API_control_Include.md#AmazonS3-Type-control_Include-Regions "API_control_Include.md#AmazonS3-Type-control_Include-Regions")>
            <Region>`string`</Region>
         </[Regions](API_control_Include.md#AmazonS3-Type-control_Include-Regions "API_control_Include.md#AmazonS3-Type-control_Include-Regions")>
      </[Include](API_control_StorageLensConfiguration.md#AmazonS3-Type-control_StorageLensConfiguration-Include "API_control_StorageLensConfiguration.md#AmazonS3-Type-control_StorageLensConfiguration-Include")>
      <[IsEnabled](API_control_StorageLensConfiguration.md#AmazonS3-Type-control_StorageLensConfiguration-IsEnabled "API_control_StorageLensConfiguration.md#AmazonS3-Type-control_StorageLensConfiguration-IsEnabled")>`boolean`</[IsEnabled](API_control_StorageLensConfiguration.md#AmazonS3-Type-control_StorageLensConfiguration-IsEnabled "API_control_StorageLensConfiguration.md#AmazonS3-Type-control_StorageLensConfiguration-IsEnabled")>
      <[StorageLensArn](API_control_StorageLensConfiguration.md#AmazonS3-Type-control_StorageLensConfiguration-StorageLensArn "API_control_StorageLensConfiguration.md#AmazonS3-Type-control_StorageLensConfiguration-StorageLensArn")>`string`</[StorageLensArn](API_control_StorageLensConfiguration.md#AmazonS3-Type-control_StorageLensConfiguration-StorageLensArn "API_control_StorageLensConfiguration.md#AmazonS3-Type-control_StorageLensConfiguration-StorageLensArn")>
   </[StorageLensConfiguration](#AmazonS3-control_PutStorageLensConfiguration-request-StorageLensConfiguration "#AmazonS3-control_PutStorageLensConfiguration-request-StorageLensConfiguration")>
   <[Tags](#AmazonS3-control_PutStorageLensConfiguration-request-Tags "#AmazonS3-control_PutStorageLensConfiguration-request-Tags")>
      <Tag>
         <[Key](API_control_StorageLensTag.md#AmazonS3-Type-control_StorageLensTag-Key "API_control_StorageLensTag.md#AmazonS3-Type-control_StorageLensTag-Key")>`string`</[Key](API_control_StorageLensTag.md#AmazonS3-Type-control_StorageLensTag-Key "API_control_StorageLensTag.md#AmazonS3-Type-control_StorageLensTag-Key")>
         <[Value](API_control_StorageLensTag.md#AmazonS3-Type-control_StorageLensTag-Value "API_control_StorageLensTag.md#AmazonS3-Type-control_StorageLensTag-Value")>`string`</[Value](API_control_StorageLensTag.md#AmazonS3-Type-control_StorageLensTag-Value "API_control_StorageLensTag.md#AmazonS3-Type-control_StorageLensTag-Value")>
      </Tag>
   </[Tags](#AmazonS3-control_PutStorageLensConfiguration-request-Tags "#AmazonS3-control_PutStorageLensConfiguration-request-Tags")>
</[PutStorageLensConfigurationRequest](#AmazonS3-control_PutStorageLensConfiguration-request-PutStorageLensConfigurationRequest "#AmazonS3-control_PutStorageLensConfiguration-request-PutStorageLensConfigurationRequest")>
```

## URI Request Parameters


The request uses the following URI parameters.





**[storagelensid](#API_control_PutStorageLensConfiguration_RequestSyntax "#API_control_PutStorageLensConfiguration_RequestSyntax")**


The ID of the S3 Storage Lens configuration.


Length Constraints: Minimum length of 1. Maximum length of 64.


Pattern: `[a-zA-Z0-9\-\_\.]+`



Required: Yes




**[x-amz-account-id](#API_control_PutStorageLensConfiguration_RequestSyntax "#API_control_PutStorageLensConfiguration_RequestSyntax")**


The account ID of the requester.


Length Constraints: Maximum length of 64.


Pattern: `^\d{12}$`



Required: Yes




## Request Body


The request accepts the following data in XML format.





**[PutStorageLensConfigurationRequest](#API_control_PutStorageLensConfiguration_RequestSyntax "#API_control_PutStorageLensConfiguration_RequestSyntax")**


Root level tag for the PutStorageLensConfigurationRequest parameters.


Required: Yes




**[StorageLensConfiguration](#API_control_PutStorageLensConfiguration_RequestSyntax "#API_control_PutStorageLensConfiguration_RequestSyntax")**


The S3 Storage Lens configuration.


Type: [StorageLensConfiguration](API_control_StorageLensConfiguration.md "API_control_StorageLensConfiguration.md") data type


Required: Yes




**[Tags](#API_control_PutStorageLensConfiguration_RequestSyntax "#API_control_PutStorageLensConfiguration_RequestSyntax")**


The tag set of the S3 Storage Lens configuration.


###### Note

You can set up to a maximum of 50 tags.


Type: Array of [StorageLensTag](API_control_StorageLensTag.md "API_control_StorageLensTag.md") data types


Required: No




## Response Syntax



```
HTTP/1.1 200

```

## Response Elements


If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.


## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface](https://docs.aws.amazon.com/goto/cli2/s3control-2018-08-20/PutStorageLensConfiguration "https://docs.aws.amazon.com/goto/cli2/s3control-2018-08-20/PutStorageLensConfiguration")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/s3control-2018-08-20/PutStorageLensConfiguration "https://docs.aws.amazon.com/goto/DotNetSDKV3/s3control-2018-08-20/PutStorageLensConfiguration")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/PutStorageLensConfiguration "https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/PutStorageLensConfiguration")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/s3control-2018-08-20/PutStorageLensConfiguration "https://docs.aws.amazon.com/goto/SdkForGoV2/s3control-2018-08-20/PutStorageLensConfiguration")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/PutStorageLensConfiguration "https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/PutStorageLensConfiguration")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3control-2018-08-20/PutStorageLensConfiguration "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3control-2018-08-20/PutStorageLensConfiguration")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/s3control-2018-08-20/PutStorageLensConfiguration "https://docs.aws.amazon.com/goto/SdkForKotlin/s3control-2018-08-20/PutStorageLensConfiguration")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/s3control-2018-08-20/PutStorageLensConfiguration "https://docs.aws.amazon.com/goto/SdkForPHPV3/s3control-2018-08-20/PutStorageLensConfiguration")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/s3control-2018-08-20/PutStorageLensConfiguration "https://docs.aws.amazon.com/goto/boto3/s3control-2018-08-20/PutStorageLensConfiguration")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/PutStorageLensConfiguration "https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/PutStorageLensConfiguration")
