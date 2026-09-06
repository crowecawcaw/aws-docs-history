

# PipeTargetStateMachineParameters
<a name="API_PipeTargetStateMachineParameters"></a>

The parameters for using a Step Functions state machine as a target.

## Contents
<a name="API_PipeTargetStateMachineParameters_Contents"></a>

 ** InvocationType **   <a name="eventbridge-Type-PipeTargetStateMachineParameters-InvocationType"></a>
Specify whether to invoke the Step Functions state machine synchronously or asynchronously.  
+  `REQUEST_RESPONSE` (default) - Invoke synchronously. For more information, see [StartSyncExecution](https://docs.aws.amazon.com/step-functions/latest/apireference/API_StartSyncExecution.html) in the * AWS Step Functions API Reference*.
**Note**  
 `REQUEST_RESPONSE` is not supported for `STANDARD` state machine workflows.
+  `FIRE_AND_FORGET` - Invoke asynchronously. For more information, see [StartExecution](https://docs.aws.amazon.com/step-functions/latest/apireference/API_StartExecution.html) in the * AWS Step Functions API Reference*.
For more information, see [Invocation types](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-pipes.html#pipes-invocation) in the *Amazon EventBridge User Guide*.  
Type: String  
Valid Values: `REQUEST_RESPONSE | FIRE_AND_FORGET`   
Required: No

## See Also
<a name="API_PipeTargetStateMachineParameters_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pipes-2015-10-07/PipeTargetStateMachineParameters) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pipes-2015-10-07/PipeTargetStateMachineParameters) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pipes-2015-10-07/PipeTargetStateMachineParameters) 