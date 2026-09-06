

# SchemaExtensionInfo
<a name="API_SchemaExtensionInfo"></a>

Information about a schema extension.

## Contents
<a name="API_SchemaExtensionInfo_Contents"></a>

 ** Description **   <a name="DirectoryService-Type-SchemaExtensionInfo-Description"></a>
A description of the schema extension.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 128.  
Pattern: `^([a-zA-Z0-9_])[\\a-zA-Z0-9_@#%*+=:?./!\s-]*$`   
Required: No

 ** DirectoryId **   <a name="DirectoryService-Type-SchemaExtensionInfo-DirectoryId"></a>
The identifier of the directory to which the schema extension is applied.  
Type: String  
Pattern: `^d-[0-9a-f]{10}$`   
Required: No

 ** EndDateTime **   <a name="DirectoryService-Type-SchemaExtensionInfo-EndDateTime"></a>
The date and time that the schema extension was completed.  
Type: Timestamp  
Required: No

 ** SchemaExtensionId **   <a name="DirectoryService-Type-SchemaExtensionInfo-SchemaExtensionId"></a>
The identifier of the schema extension.  
Type: String  
Pattern: `^e-[0-9a-f]{10}$`   
Required: No

 ** SchemaExtensionStatus **   <a name="DirectoryService-Type-SchemaExtensionInfo-SchemaExtensionStatus"></a>
The current status of the schema extension.  
Type: String  
Valid Values: `Initializing | CreatingSnapshot | UpdatingSchema | Replicating | CancelInProgress | RollbackInProgress | Cancelled | Failed | Completed`   
Required: No

 ** SchemaExtensionStatusReason **   <a name="DirectoryService-Type-SchemaExtensionInfo-SchemaExtensionStatusReason"></a>
The reason for the `SchemaExtensionStatus`.  
Type: String  
Required: No

 ** StartDateTime **   <a name="DirectoryService-Type-SchemaExtensionInfo-StartDateTime"></a>
The date and time that the schema extension started being applied to the directory.  
Type: Timestamp  
Required: No

## See Also
<a name="API_SchemaExtensionInfo_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ds-2015-04-16/SchemaExtensionInfo) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ds-2015-04-16/SchemaExtensionInfo) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ds-2015-04-16/SchemaExtensionInfo) 