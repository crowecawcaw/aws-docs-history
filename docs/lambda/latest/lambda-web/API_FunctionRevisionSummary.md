

# FunctionRevisionSummary
<a name="API_FunctionRevisionSummary"></a>

A summary of a web function revision.

## Contents
<a name="API_FunctionRevisionSummary_Contents"></a>

 ** createdAt **   <a name="lambdaweb-Type-FunctionRevisionSummary-createdAt"></a>
The date and time the revision was created.  
Type: Timestamp  
Required: Yes

 ** revisionArn **   <a name="lambdaweb-Type-FunctionRevisionSummary-revisionArn"></a>
The Amazon Resource Name (ARN) of the revision.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Required: Yes

 ** revisionId **   <a name="lambdaweb-Type-FunctionRevisionSummary-revisionId"></a>
The identifier of the revision.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 256.  
Required: Yes

 ** state **   <a name="lambdaweb-Type-FunctionRevisionSummary-state"></a>
The current state of the revision.  
Type: String  
Valid Values: `Pending | Active | Failed`   
Required: Yes

 ** stateReason **   <a name="lambdaweb-Type-FunctionRevisionSummary-stateReason"></a>
The reason for the current state of the revision.  
Type: String  
Required: Yes

 ** description **   <a name="lambdaweb-Type-FunctionRevisionSummary-description"></a>
A description of the revision.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 256.  
Required: No

## See Also
<a name="API_FunctionRevisionSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lambda-web-2025-03-07/FunctionRevisionSummary) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lambda-web-2025-03-07/FunctionRevisionSummary) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lambda-web-2025-03-07/FunctionRevisionSummary) 