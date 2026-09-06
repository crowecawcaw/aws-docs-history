

# Snapshot
<a name="API_Snapshot"></a>

Describes a directory snapshot.

## Contents
<a name="API_Snapshot_Contents"></a>

 ** DirectoryId **   <a name="DirectoryService-Type-Snapshot-DirectoryId"></a>
The directory identifier.  
Type: String  
Pattern: `^d-[0-9a-f]{10}$`   
Required: No

 ** Name **   <a name="DirectoryService-Type-Snapshot-Name"></a>
The descriptive name of the snapshot.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 128.  
Pattern: `^([a-zA-Z0-9_])[\\a-zA-Z0-9_@#%*+=:?./!\s-]*$`   
Required: No

 ** SnapshotId **   <a name="DirectoryService-Type-Snapshot-SnapshotId"></a>
The snapshot identifier.  
Type: String  
Pattern: `^s-[0-9a-f]{10}$`   
Required: No

 ** StartTime **   <a name="DirectoryService-Type-Snapshot-StartTime"></a>
The date and time that the snapshot was taken.  
Type: Timestamp  
Required: No

 ** Status **   <a name="DirectoryService-Type-Snapshot-Status"></a>
The snapshot status.  
Type: String  
Valid Values: `Creating | Completed | Failed`   
Required: No

 ** Type **   <a name="DirectoryService-Type-Snapshot-Type"></a>
The snapshot type.  
Type: String  
Valid Values: `Auto | Manual`   
Required: No

## See Also
<a name="API_Snapshot_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ds-2015-04-16/Snapshot) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ds-2015-04-16/Snapshot) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ds-2015-04-16/Snapshot) 