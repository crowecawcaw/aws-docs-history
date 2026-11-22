

# SetupArtifact

A setup artifact, which is one file in the requested format.

## Contents
<a name="API_SetupArtifact_Contents"></a>

 ** Content **   <a name="cwoa-Type-SetupArtifact-Content"></a>
The content of the artifact.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 262144.  
Required: Yes

 ** FileName **   <a name="cwoa-Type-SetupArtifact-FileName"></a>
The suggested file name, for example `main.bicep`.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 1024.  
Required: Yes

 ** Format **   <a name="cwoa-Type-SetupArtifact-Format"></a>
The format of the artifact.  
Type: String  
Valid Values: `BICEP`   
Required: Yes

 ** ContentType **   <a name="cwoa-Type-SetupArtifact-ContentType"></a>
The content type of the artifact, for example `text/plain`.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 127.  
Required: No

## See Also
<a name="API_SetupArtifact_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/observabilityadmin-2018-05-10/SetupArtifact) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/observabilityadmin-2018-05-10/SetupArtifact) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/observabilityadmin-2018-05-10/SetupArtifact) 