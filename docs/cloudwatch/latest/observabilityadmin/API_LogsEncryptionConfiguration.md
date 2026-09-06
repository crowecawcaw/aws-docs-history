

# LogsEncryptionConfiguration
<a name="API_LogsEncryptionConfiguration"></a>

Configuration for encrypting centralized destination log groups. By default, this configuration applies only to destination log groups whose corresponding source log groups are encrypted using customer managed KMS keys. To encrypt all destination log groups created by the rule, set `EncryptionScope` to `NEW_DESTINATION_LOG_GROUPS`.

## Contents
<a name="API_LogsEncryptionConfiguration_Contents"></a>

 ** EncryptionStrategy **   <a name="cwoa-Type-LogsEncryptionConfiguration-EncryptionStrategy"></a>
Configuration that determines the encryption strategy of the destination log groups. CUSTOMER\_MANAGED uses the configured KmsKeyArn to encrypt newly created destination log groups.  
Type: String  
Valid Values: `CUSTOMER_MANAGED | AWS_OWNED`   
Required: Yes

 ** EncryptionConflictResolutionStrategy **   <a name="cwoa-Type-LogsEncryptionConfiguration-EncryptionConflictResolutionStrategy"></a>
Conflict resolution strategy for centralization if the encryption strategy is set to CUSTOMER\_MANAGED and the destination log group is encrypted with an AWS\_OWNED KMS Key. ALLOW lets centralization go through while SKIP prevents centralization into the destination log group.  
Type: String  
Valid Values: `ALLOW | SKIP`   
Required: No

 ** EncryptionScope **   <a name="cwoa-Type-LogsEncryptionConfiguration-EncryptionScope"></a>
Determines which newly created destination log groups are encrypted with the configured `KmsKeyArn` when `EncryptionStrategy` is `CUSTOMER_MANAGED`.  
If you set this to `ENCRYPTED_SOURCE_ONLY` (the default), only destination log groups whose source log group is encrypted with a customer managed KMS key use the configured `KmsKeyArn`. Destination log groups derived from AWS owned encrypted source log groups remain AWS owned encrypted.  
If you set this to `NEW_DESTINATION_LOG_GROUPS`, every new destination log group created by this rule uses the configured `KmsKeyArn`, regardless of the source log group's encryption posture.  
This field is not valid when `EncryptionStrategy` is `AWS_OWNED`.  
Type: String  
Valid Values: `ENCRYPTED_SOURCE_ONLY | NEW_DESTINATION_LOG_GROUPS`   
Required: No

 ** KmsKeyArn **   <a name="cwoa-Type-LogsEncryptionConfiguration-KmsKeyArn"></a>
KMS Key ARN belonging to the primary destination account and region, to encrypt newly created central log groups in the primary destination.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 1011.  
Pattern: `arn:aws([a-z0-9\-]+)?:([a-zA-Z0-9\-]+):([a-z0-9\-]+)?:([0-9]{12})?:(.+)`   
Required: No

## See Also
<a name="API_LogsEncryptionConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/observabilityadmin-2018-05-10/LogsEncryptionConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/observabilityadmin-2018-05-10/LogsEncryptionConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/observabilityadmin-2018-05-10/LogsEncryptionConfiguration) 