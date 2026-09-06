

# Trust
<a name="API_Trust"></a>

Describes a trust relationship between an AWS Managed Microsoft AD directory and an external domain.

## Contents
<a name="API_Trust_Contents"></a>

 ** CreatedDateTime **   <a name="DirectoryService-Type-Trust-CreatedDateTime"></a>
The date and time that the trust relationship was created.  
Type: Timestamp  
Required: No

 ** DirectoryId **   <a name="DirectoryService-Type-Trust-DirectoryId"></a>
The Directory ID of the AWS directory involved in the trust relationship.  
Type: String  
Pattern: `^d-[0-9a-f]{10}$`   
Required: No

 ** LastUpdatedDateTime **   <a name="DirectoryService-Type-Trust-LastUpdatedDateTime"></a>
The date and time that the trust relationship was last updated.  
Type: Timestamp  
Required: No

 ** RemoteDomainName **   <a name="DirectoryService-Type-Trust-RemoteDomainName"></a>
The Fully Qualified Domain Name (FQDN) of the external domain involved in the trust relationship.  
Type: String  
Length Constraints: Maximum length of 1024.  
Pattern: `^([a-zA-Z0-9]+[\\.-])+([a-zA-Z0-9])+[.]?$`   
Required: No

 ** SelectiveAuth **   <a name="DirectoryService-Type-Trust-SelectiveAuth"></a>
Current state of selective authentication for the trust.  
Type: String  
Valid Values: `Enabled | Disabled`   
Required: No

 ** StateLastUpdatedDateTime **   <a name="DirectoryService-Type-Trust-StateLastUpdatedDateTime"></a>
The date and time that the TrustState was last updated.  
Type: Timestamp  
Required: No

 ** TrustDirection **   <a name="DirectoryService-Type-Trust-TrustDirection"></a>
The trust relationship direction.  
Type: String  
Valid Values: `One-Way: Outgoing | One-Way: Incoming | Two-Way`   
Required: No

 ** TrustId **   <a name="DirectoryService-Type-Trust-TrustId"></a>
The unique ID of the trust relationship.  
Type: String  
Pattern: `^t-[0-9a-f]{10}$`   
Required: No

 ** TrustState **   <a name="DirectoryService-Type-Trust-TrustState"></a>
The trust relationship state.  
Type: String  
Valid Values: `Creating | Created | Verifying | VerifyFailed | Verified | Updating | UpdateFailed | Updated | Deleting | Deleted | Failed`   
Required: No

 ** TrustStateReason **   <a name="DirectoryService-Type-Trust-TrustStateReason"></a>
The reason for the TrustState.  
Type: String  
Required: No

 ** TrustType **   <a name="DirectoryService-Type-Trust-TrustType"></a>
The trust relationship type. `Forest` is the default.  
Type: String  
Valid Values: `Forest | External`   
Required: No

## See Also
<a name="API_Trust_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ds-2015-04-16/Trust) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ds-2015-04-16/Trust) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ds-2015-04-16/Trust) 