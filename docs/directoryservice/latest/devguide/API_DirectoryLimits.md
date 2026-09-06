

# DirectoryLimits
<a name="API_DirectoryLimits"></a>

Contains directory limit information for a Region.

## Contents
<a name="API_DirectoryLimits_Contents"></a>

 ** CloudOnlyDirectoriesCurrentCount **   <a name="DirectoryService-Type-DirectoryLimits-CloudOnlyDirectoriesCurrentCount"></a>
The current number of cloud directories in the Region.  
Type: Integer  
Valid Range: Minimum value of 0.  
Required: No

 ** CloudOnlyDirectoriesLimit **   <a name="DirectoryService-Type-DirectoryLimits-CloudOnlyDirectoriesLimit"></a>
The maximum number of cloud directories allowed in the Region.  
Type: Integer  
Valid Range: Minimum value of 0.  
Required: No

 ** CloudOnlyDirectoriesLimitReached **   <a name="DirectoryService-Type-DirectoryLimits-CloudOnlyDirectoriesLimitReached"></a>
Indicates if the cloud directory limit has been reached.  
Type: Boolean  
Required: No

 ** CloudOnlyMicrosoftADCurrentCount **   <a name="DirectoryService-Type-DirectoryLimits-CloudOnlyMicrosoftADCurrentCount"></a>
The current number of AWS Managed Microsoft AD directories in the region.  
Type: Integer  
Valid Range: Minimum value of 0.  
Required: No

 ** CloudOnlyMicrosoftADLimit **   <a name="DirectoryService-Type-DirectoryLimits-CloudOnlyMicrosoftADLimit"></a>
The maximum number of AWS Managed Microsoft AD directories allowed in the region.  
Type: Integer  
Valid Range: Minimum value of 0.  
Required: No

 ** CloudOnlyMicrosoftADLimitReached **   <a name="DirectoryService-Type-DirectoryLimits-CloudOnlyMicrosoftADLimitReached"></a>
Indicates if the AWS Managed Microsoft AD directory limit has been reached.  
Type: Boolean  
Required: No

 ** ConnectedDirectoriesCurrentCount **   <a name="DirectoryService-Type-DirectoryLimits-ConnectedDirectoriesCurrentCount"></a>
The current number of connected directories in the Region.  
Type: Integer  
Valid Range: Minimum value of 0.  
Required: No

 ** ConnectedDirectoriesLimit **   <a name="DirectoryService-Type-DirectoryLimits-ConnectedDirectoriesLimit"></a>
The maximum number of connected directories allowed in the Region.  
Type: Integer  
Valid Range: Minimum value of 0.  
Required: No

 ** ConnectedDirectoriesLimitReached **   <a name="DirectoryService-Type-DirectoryLimits-ConnectedDirectoriesLimitReached"></a>
Indicates if the connected directory limit has been reached.  
Type: Boolean  
Required: No

## See Also
<a name="API_DirectoryLimits_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ds-2015-04-16/DirectoryLimits) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ds-2015-04-16/DirectoryLimits) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ds-2015-04-16/DirectoryLimits) 