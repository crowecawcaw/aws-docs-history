

# FunctionSummary
<a name="API_FunctionSummary"></a>

A summary of a web function.

## Contents
<a name="API_FunctionSummary_Contents"></a>

 ** createdAt **   <a name="lambdaweb-Type-FunctionSummary-createdAt"></a>
The date and time the web function was created.  
Type: Timestamp  
Required: Yes

 ** functionArn **   <a name="lambdaweb-Type-FunctionSummary-functionArn"></a>
The Amazon Resource Name (ARN) of the web function.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Required: Yes

 ** functionName **   <a name="lambdaweb-Type-FunctionSummary-functionName"></a>
The name of the web function.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 256.  
Required: Yes

 ** state **   <a name="lambdaweb-Type-FunctionSummary-state"></a>
The current state of the web function.  
Type: String  
Valid Values: `Pending | Active | Failed | Deleting`   
Required: Yes

 ** stateReason **   <a name="lambdaweb-Type-FunctionSummary-stateReason"></a>
The reason for the current state of the web function.  
Type: String  
Required: Yes

 ** updatedAt **   <a name="lambdaweb-Type-FunctionSummary-updatedAt"></a>
The date and time the web function was last updated.  
Type: Timestamp  
Required: Yes

## See Also
<a name="API_FunctionSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lambda-web-2025-03-07/FunctionSummary) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lambda-web-2025-03-07/FunctionSummary) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lambda-web-2025-03-07/FunctionSummary) 