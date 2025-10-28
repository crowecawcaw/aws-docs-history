# PipeTargetStateMachineParameters

The parameters for using a Step Functions state machine as a target.

## Contents

**InvocationType**

Specify whether to invoke the Step Functions state machine synchronously or
asynchronously.

- `REQUEST_RESPONSE` (default) - Invoke synchronously. For more
  information, see [StartSyncExecution](../../../step-functions/latest/apireference/API_StartSyncExecution.md "../../../step-functions/latest/apireference/API_StartSyncExecution.md") in the _AWS Step Functions API
  Reference_.

###### Note

`REQUEST_RESPONSE` is not supported for `STANDARD` state
machine workflows.

- `FIRE_AND_FORGET` - Invoke asynchronously. For more information, see
  [StartExecution](../../../step-functions/latest/apireference/API_StartExecution.md "../../../step-functions/latest/apireference/API_StartExecution.md") in the _AWS Step Functions API
  Reference_.

For more information, see [Invocation
types](../userguide/eb-pipes.md#pipes-invocation "../userguide/eb-pipes.md#pipes-invocation") in the _Amazon EventBridge User Guide_.

Type: String

Valid Values: `REQUEST_RESPONSE | FIRE_AND_FORGET`

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/pipes-2015-10-07/PipeTargetStateMachineParameters.md "../../../goto/SdkForCpp/pipes-2015-10-07/PipeTargetStateMachineParameters.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/pipes-2015-10-07/PipeTargetStateMachineParameters.md "../../../goto/SdkForJavaV2/pipes-2015-10-07/PipeTargetStateMachineParameters.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/pipes-2015-10-07/PipeTargetStateMachineParameters.md "../../../goto/SdkForRubyV3/pipes-2015-10-07/PipeTargetStateMachineParameters.md")
