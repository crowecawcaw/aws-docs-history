

# HybridUpdateInfoEntry
<a name="API_HybridUpdateInfoEntry"></a>

Contains detailed information about a specific update activity for a hybrid directory component.

## Contents
<a name="API_HybridUpdateInfoEntry_Contents"></a>

 ** AssessmentId **   <a name="DirectoryService-Type-HybridUpdateInfoEntry-AssessmentId"></a>
The identifier of the assessment performed to validate this update configuration.  
Type: String  
Pattern: `^da-[0-9a-f]{18}$`   
Required: No

 ** InitiatedBy **   <a name="DirectoryService-Type-HybridUpdateInfoEntry-InitiatedBy"></a>
Specifies if the update was initiated by the customer or AWS.  
Type: String  
Required: No

 ** LastUpdatedDateTime **   <a name="DirectoryService-Type-HybridUpdateInfoEntry-LastUpdatedDateTime"></a>
The date and time when the update activity status was last updated.  
Type: Timestamp  
Required: No

 ** NewValue **   <a name="DirectoryService-Type-HybridUpdateInfoEntry-NewValue"></a>
The new configuration values being applied in this update.  
Type: [HybridUpdateValue](API_HybridUpdateValue.md) object  
Required: No

 ** PreviousValue **   <a name="DirectoryService-Type-HybridUpdateInfoEntry-PreviousValue"></a>
The previous configuration values before this update was applied.  
Type: [HybridUpdateValue](API_HybridUpdateValue.md) object  
Required: No

 ** StartTime **   <a name="DirectoryService-Type-HybridUpdateInfoEntry-StartTime"></a>
The date and time when the update activity was initiated.  
Type: Timestamp  
Required: No

 ** Status **   <a name="DirectoryService-Type-HybridUpdateInfoEntry-Status"></a>
The current status of the update activity. Valid values include `UPDATED`, `UPDATING`, and `UPDATE_FAILED`.  
Type: String  
Valid Values: `Updated | Updating | UpdateFailed`   
Required: No

 ** StatusReason **   <a name="DirectoryService-Type-HybridUpdateInfoEntry-StatusReason"></a>
A human-readable description of the update status, including any error details or progress information.  
Type: String  
Required: No

## See Also
<a name="API_HybridUpdateInfoEntry_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ds-2015-04-16/HybridUpdateInfoEntry) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ds-2015-04-16/HybridUpdateInfoEntry) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ds-2015-04-16/HybridUpdateInfoEntry) 