

# RevisionError
<a name="API_RevisionError"></a>

A single error encountered while creating or reading a web function revision. The error describes the affected attribute, an error code, and a human-readable message. This structure is present only when the revision has errors.

## Contents
<a name="API_RevisionError_Contents"></a>

 ** attribute **   <a name="lambdaweb-Type-RevisionError-attribute"></a>
The name of the revision attribute that the error applies to.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 64.  
Required: Yes

 ** errorCode **   <a name="lambdaweb-Type-RevisionError-errorCode"></a>
A short, machine-readable code that identifies the error.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 64.  
Required: Yes

 ** errorMessage **   <a name="lambdaweb-Type-RevisionError-errorMessage"></a>
A human-readable message describing the error.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Required: Yes

## See Also
<a name="API_RevisionError_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lambda-web-2025-03-07/RevisionError) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lambda-web-2025-03-07/RevisionError) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lambda-web-2025-03-07/RevisionError) 