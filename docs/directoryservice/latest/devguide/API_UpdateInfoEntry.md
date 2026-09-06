

# UpdateInfoEntry
<a name="API_UpdateInfoEntry"></a>

An entry of update information related to a requested update type.

## Contents
<a name="API_UpdateInfoEntry_Contents"></a>

 ** InitiatedBy **   <a name="DirectoryService-Type-UpdateInfoEntry-InitiatedBy"></a>
 This specifies if the update was initiated by the customer or by the service team.   
Type: String  
Required: No

 ** LastUpdatedDateTime **   <a name="DirectoryService-Type-UpdateInfoEntry-LastUpdatedDateTime"></a>
 The last updated date and time of a particular directory setting.   
Type: Timestamp  
Required: No

 ** NewValue **   <a name="DirectoryService-Type-UpdateInfoEntry-NewValue"></a>
 The new value of the target setting.   
Type: [UpdateValue](API_UpdateValue.md) object  
Required: No

 ** PreviousValue **   <a name="DirectoryService-Type-UpdateInfoEntry-PreviousValue"></a>
 The old value of the target setting.   
Type: [UpdateValue](API_UpdateValue.md) object  
Required: No

 ** Region **   <a name="DirectoryService-Type-UpdateInfoEntry-Region"></a>
 The name of the Region.   
Type: String  
Length Constraints: Minimum length of 8. Maximum length of 32.  
Required: No

 ** StartTime **   <a name="DirectoryService-Type-UpdateInfoEntry-StartTime"></a>
 The start time of the `UpdateDirectorySetup` for the particular type.   
Type: Timestamp  
Required: No

 ** Status **   <a name="DirectoryService-Type-UpdateInfoEntry-Status"></a>
 The status of the update performed on the directory.   
Type: String  
Valid Values: `Updated | Updating | UpdateFailed`   
Required: No

 ** StatusReason **   <a name="DirectoryService-Type-UpdateInfoEntry-StatusReason"></a>
 The reason for the current status of the update type activity.   
Type: String  
Required: No

## See Also
<a name="API_UpdateInfoEntry_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ds-2015-04-16/UpdateInfoEntry) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ds-2015-04-16/UpdateInfoEntry) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ds-2015-04-16/UpdateInfoEntry) 