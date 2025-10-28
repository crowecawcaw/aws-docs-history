# PipeTargetLambdaFunctionParameters

The parameters for using a Lambda function as a target.

## Contents

**InvocationType**

Specify whether to invoke the function synchronously or asynchronously.

- `REQUEST_RESPONSE` (default) - Invoke synchronously. This corresponds
  to the `RequestResponse` option in the `InvocationType`
  parameter for the Lambda
  [Invoke](../../../lambda/latest/dg/API_Invoke.md#API_Invoke_RequestSyntax "../../../lambda/latest/dg/API_Invoke.md#API_Invoke_RequestSyntax")
  API.
- `FIRE_AND_FORGET` - Invoke asynchronously. This corresponds to the
  `Event` option in the `InvocationType` parameter for the
  Lambda
  [Invoke](../../../lambda/latest/dg/API_Invoke.md#API_Invoke_RequestSyntax "../../../lambda/latest/dg/API_Invoke.md#API_Invoke_RequestSyntax")
  API.

For more information, see [Invocation
types](../userguide/eb-pipes.md#pipes-invocation "../userguide/eb-pipes.md#pipes-invocation") in the _Amazon EventBridge User Guide_.

Type: String

Valid Values: `REQUEST_RESPONSE | FIRE_AND_FORGET`

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/pipes-2015-10-07/PipeTargetLambdaFunctionParameters.md "../../../goto/SdkForCpp/pipes-2015-10-07/PipeTargetLambdaFunctionParameters.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/pipes-2015-10-07/PipeTargetLambdaFunctionParameters.md "../../../goto/SdkForJavaV2/pipes-2015-10-07/PipeTargetLambdaFunctionParameters.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/pipes-2015-10-07/PipeTargetLambdaFunctionParameters.md "../../../goto/SdkForRubyV3/pipes-2015-10-07/PipeTargetLambdaFunctionParameters.md")
