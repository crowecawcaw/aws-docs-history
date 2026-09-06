

# PipeTargetLambdaFunctionParameters
<a name="API_PipeTargetLambdaFunctionParameters"></a>

The parameters for using a Lambda function as a target.

## Contents
<a name="API_PipeTargetLambdaFunctionParameters_Contents"></a>

 ** InvocationType **   <a name="eventbridge-Type-PipeTargetLambdaFunctionParameters-InvocationType"></a>
Specify whether to invoke the function synchronously or asynchronously.  
+  `REQUEST_RESPONSE` (default) - Invoke synchronously. This corresponds to the `RequestResponse` option in the `InvocationType` parameter for the Lambda [Invoke](https://docs.aws.amazon.com/lambda/latest/dg/API_Invoke.html#API_Invoke_RequestSyntax) API.
+  `FIRE_AND_FORGET` - Invoke asynchronously. This corresponds to the `Event` option in the `InvocationType` parameter for the Lambda [Invoke](https://docs.aws.amazon.com/lambda/latest/dg/API_Invoke.html#API_Invoke_RequestSyntax) API.
For more information, see [Invocation types](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-pipes.html#pipes-invocation) in the *Amazon EventBridge User Guide*.  
Type: String  
Valid Values: `REQUEST_RESPONSE | FIRE_AND_FORGET`   
Required: No

## See Also
<a name="API_PipeTargetLambdaFunctionParameters_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pipes-2015-10-07/PipeTargetLambdaFunctionParameters) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pipes-2015-10-07/PipeTargetLambdaFunctionParameters) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pipes-2015-10-07/PipeTargetLambdaFunctionParameters) 