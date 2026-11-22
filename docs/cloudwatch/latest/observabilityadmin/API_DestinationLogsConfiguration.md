

# DestinationLogsConfiguration

Configuration for centralization destination log groups, including encryption and backup settings.

## Contents
<a name="API_DestinationLogsConfiguration_Contents"></a>

 ** BackupConfiguration **   <a name="cwoa-Type-DestinationLogsConfiguration-BackupConfiguration"></a>
Configuration defining the backup region and an optional KMS key for the backup destination.  
Type: [LogsBackupConfiguration](API_LogsBackupConfiguration.md) object  
Required: No

 ** LogGroupDeletionProtection **   <a name="cwoa-Type-DestinationLogsConfiguration-LogGroupDeletionProtection"></a>
Specifies whether this centralization rule enables deletion protection on the destination log groups that it creates. If you don't specify this setting, the rule doesn't enable deletion protection on the log groups that it creates. If you specify a backup Region in `BackupConfiguration`, the setting also applies to the log groups that the rule creates in the backup Region.  
When you set this to `ENABLED`, the rule enables deletion protection only on log groups that it creates after you enable the setting. It does not add deletion protection to log groups the rule created before you enabled the setting.  
If you remove this setting from the rule or delete the rule, deletion protection stays enabled on log groups that already have it. To delete one of these log groups, first disable deletion protection on the log group in the destination account.  
Type: String  
Valid Values: `ENABLED`   
Required: No

 ** LogGroupNameConfiguration **   <a name="cwoa-Type-DestinationLogsConfiguration-LogGroupNameConfiguration"></a>
Configuration that specifies a naming pattern for destination log groups created during centralization. The pattern supports static text and dynamic variables that are replaced with source attributes when log groups are created.  
Type: [LogGroupNameConfiguration](API_LogGroupNameConfiguration.md) object  
Required: No

 ** LogsEncryptionConfiguration **   <a name="cwoa-Type-DestinationLogsConfiguration-LogsEncryptionConfiguration"></a>
The encryption configuration for centralization destination log groups.  
Type: [LogsEncryptionConfiguration](API_LogsEncryptionConfiguration.md) object  
Required: No

 ** TagPropagationConfiguration **   <a name="cwoa-Type-DestinationLogsConfiguration-TagPropagationConfiguration"></a>
Specifies the tag propagation configuration for this centralization rule. When present, `LogGroupNameConfiguration` must use a `LogGroupNamePattern` that contains `${source.logGroup}`, `${source.accountId}`, and `${source.region}`.  
Type: [TagPropagationConfiguration](API_TagPropagationConfiguration.md) object  
Required: No

## See Also
<a name="API_DestinationLogsConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/observabilityadmin-2018-05-10/DestinationLogsConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/observabilityadmin-2018-05-10/DestinationLogsConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/observabilityadmin-2018-05-10/DestinationLogsConfiguration) 