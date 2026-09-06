

# RegionDescription
<a name="API_RegionDescription"></a>

The replicated Region information for a directory.

## Contents
<a name="API_RegionDescription_Contents"></a>

 ** DesiredNumberOfDomainControllers **   <a name="DirectoryService-Type-RegionDescription-DesiredNumberOfDomainControllers"></a>
The desired number of domain controllers in the specified Region for the specified directory.  
Type: Integer  
Valid Range: Minimum value of 2.  
Required: No

 ** DirectoryId **   <a name="DirectoryService-Type-RegionDescription-DirectoryId"></a>
The identifier of the directory.  
Type: String  
Pattern: `^d-[0-9a-f]{10}$`   
Required: No

 ** LastUpdatedDateTime **   <a name="DirectoryService-Type-RegionDescription-LastUpdatedDateTime"></a>
The date and time that the Region description was last updated.  
Type: Timestamp  
Required: No

 ** LaunchTime **   <a name="DirectoryService-Type-RegionDescription-LaunchTime"></a>
Specifies when the Region replication began.  
Type: Timestamp  
Required: No

 ** RegionName **   <a name="DirectoryService-Type-RegionDescription-RegionName"></a>
The name of the Region. For example, `us-east-1`.  
Type: String  
Length Constraints: Minimum length of 8. Maximum length of 32.  
Required: No

 ** RegionType **   <a name="DirectoryService-Type-RegionDescription-RegionType"></a>
Specifies whether the Region is the primary Region or an additional Region.  
Type: String  
Valid Values: `Primary | Additional`   
Required: No

 ** Status **   <a name="DirectoryService-Type-RegionDescription-Status"></a>
The status of the replication process for the specified Region.  
Type: String  
Valid Values: `Requested | Creating | Created | Active | Inoperable | Impaired | Restoring | RestoreFailed | Deleting | Deleted | Failed | Updating`   
Required: No

 ** StatusLastUpdatedDateTime **   <a name="DirectoryService-Type-RegionDescription-StatusLastUpdatedDateTime"></a>
The date and time that the Region status was last updated.  
Type: Timestamp  
Required: No

 ** VpcSettings **   <a name="DirectoryService-Type-RegionDescription-VpcSettings"></a>
Contains VPC information for the [CreateDirectory](API_CreateDirectory.md), [CreateMicrosoftAD](API_CreateMicrosoftAD.md), or [CreateHybridAD](API_CreateHybridAD.md) operation.  
Type: [DirectoryVpcSettings](API_DirectoryVpcSettings.md) object  
Required: No

## See Also
<a name="API_RegionDescription_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ds-2015-04-16/RegionDescription) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ds-2015-04-16/RegionDescription) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ds-2015-04-16/RegionDescription) 