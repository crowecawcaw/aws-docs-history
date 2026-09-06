

AWS Migration Hub is no longer open to new customers as of November 7, 2025. For capabilities similar to AWS Migration Hub, explore [AWS Transform](https://aws.amazon.com/transform).

# SourceResource
<a name="API_SourceResource"></a>

A source resource can be a source server, a migration wave, an application, or any other resource that you track.

## Contents
<a name="API_SourceResource_Contents"></a>

 ** Name **   <a name="migrationhub-Type-SourceResource-Name"></a>
This is the name that you want to use to identify the resource. If the resource is an AWS resource, we recommend that you set this parameter to the ARN of the resource.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 1600.  
Required: Yes

 ** Description **   <a name="migrationhub-Type-SourceResource-Description"></a>
A description that can be free-form text to record additional detail about the resource for clarity or later reference.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 500.  
Pattern: `^.{0,500}$`   
Required: No

 ** StatusDetail **   <a name="migrationhub-Type-SourceResource-StatusDetail"></a>
A free-form description of the status of the resource.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 2500.  
Pattern: `^.{0,2500}$`   
Required: No

## See Also
<a name="API_SourceResource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/AWSMigrationHub-2017-05-31/SourceResource) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/AWSMigrationHub-2017-05-31/SourceResource) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/AWSMigrationHub-2017-05-31/SourceResource) 