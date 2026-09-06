

# RegionsInfo
<a name="API_RegionsInfo"></a>

Provides information about the Regions that are configured for multi-Region replication.

## Contents
<a name="API_RegionsInfo_Contents"></a>

 ** AdditionalRegions **   <a name="DirectoryService-Type-RegionsInfo-AdditionalRegions"></a>
Lists the Regions where the directory has been replicated, excluding the primary Region.  
Type: Array of strings  
Length Constraints: Minimum length of 8. Maximum length of 32.  
Required: No

 ** PrimaryRegion **   <a name="DirectoryService-Type-RegionsInfo-PrimaryRegion"></a>
The Region where the AWS Managed Microsoft AD directory was originally created.  
Type: String  
Length Constraints: Minimum length of 8. Maximum length of 32.  
Required: No

## See Also
<a name="API_RegionsInfo_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ds-2015-04-16/RegionsInfo) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ds-2015-04-16/RegionsInfo) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ds-2015-04-16/RegionsInfo) 