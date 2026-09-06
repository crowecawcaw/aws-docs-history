

# PipeTargetParameters
<a name="API_PipeTargetParameters"></a>

The parameters required to set up a target for your pipe.

For more information about pipe target parameters, including how to use dynamic path parameters, see [Target parameters](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-pipes-event-target.html) in the *Amazon EventBridge User Guide*.

## Contents
<a name="API_PipeTargetParameters_Contents"></a>

 ** BatchJobParameters **   <a name="eventbridge-Type-PipeTargetParameters-BatchJobParameters"></a>
The parameters for using an AWS Batch job as a target.  
Type: [PipeTargetBatchJobParameters](API_PipeTargetBatchJobParameters.md) object  
Required: No

 ** CloudWatchLogsParameters **   <a name="eventbridge-Type-PipeTargetParameters-CloudWatchLogsParameters"></a>
The parameters for using an CloudWatch Logs log stream as a target.  
Type: [PipeTargetCloudWatchLogsParameters](API_PipeTargetCloudWatchLogsParameters.md) object  
Required: No

 ** EcsTaskParameters **   <a name="eventbridge-Type-PipeTargetParameters-EcsTaskParameters"></a>
The parameters for using an Amazon ECS task as a target.  
Type: [PipeTargetEcsTaskParameters](API_PipeTargetEcsTaskParameters.md) object  
Required: No

 ** EventBridgeEventBusParameters **   <a name="eventbridge-Type-PipeTargetParameters-EventBridgeEventBusParameters"></a>
The parameters for using an EventBridge event bus as a target.  
Type: [PipeTargetEventBridgeEventBusParameters](API_PipeTargetEventBridgeEventBusParameters.md) object  
Required: No

 ** HttpParameters **   <a name="eventbridge-Type-PipeTargetParameters-HttpParameters"></a>
These are custom parameter to be used when the target is an API Gateway REST APIs or EventBridge ApiDestinations.  
Type: [PipeTargetHttpParameters](API_PipeTargetHttpParameters.md) object  
Required: No

 ** InputTemplate **   <a name="eventbridge-Type-PipeTargetParameters-InputTemplate"></a>
Valid JSON text passed to the target. In this case, nothing from the event itself is passed to the target. For more information, see [The JavaScript Object Notation (JSON) Data Interchange Format](http://www.rfc-editor.org/rfc/rfc7159.txt).  
To remove an input template, specify an empty string.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 8192.  
Required: No

 ** KinesisStreamParameters **   <a name="eventbridge-Type-PipeTargetParameters-KinesisStreamParameters"></a>
The parameters for using a Kinesis stream as a target.  
Type: [PipeTargetKinesisStreamParameters](API_PipeTargetKinesisStreamParameters.md) object  
Required: No

 ** LambdaFunctionParameters **   <a name="eventbridge-Type-PipeTargetParameters-LambdaFunctionParameters"></a>
The parameters for using a Lambda function as a target.  
Type: [PipeTargetLambdaFunctionParameters](API_PipeTargetLambdaFunctionParameters.md) object  
Required: No

 ** RedshiftDataParameters **   <a name="eventbridge-Type-PipeTargetParameters-RedshiftDataParameters"></a>
These are custom parameters to be used when the target is a Amazon Redshift cluster to invoke the Amazon Redshift Data API BatchExecuteStatement.  
Type: [PipeTargetRedshiftDataParameters](API_PipeTargetRedshiftDataParameters.md) object  
Required: No

 ** SageMakerPipelineParameters **   <a name="eventbridge-Type-PipeTargetParameters-SageMakerPipelineParameters"></a>
The parameters for using a SageMaker AI pipeline as a target.  
Type: [PipeTargetSageMakerPipelineParameters](API_PipeTargetSageMakerPipelineParameters.md) object  
Required: No

 ** SqsQueueParameters **   <a name="eventbridge-Type-PipeTargetParameters-SqsQueueParameters"></a>
The parameters for using a Amazon SQS stream as a target.  
Type: [PipeTargetSqsQueueParameters](API_PipeTargetSqsQueueParameters.md) object  
Required: No

 ** StepFunctionStateMachineParameters **   <a name="eventbridge-Type-PipeTargetParameters-StepFunctionStateMachineParameters"></a>
The parameters for using a Step Functions state machine as a target.  
Type: [PipeTargetStateMachineParameters](API_PipeTargetStateMachineParameters.md) object  
Required: No

 ** TimestreamParameters **   <a name="eventbridge-Type-PipeTargetParameters-TimestreamParameters"></a>
The parameters for using a Timestream for LiveAnalytics table as a target.  
Type: [PipeTargetTimestreamParameters](API_PipeTargetTimestreamParameters.md) object  
Required: No

## See Also
<a name="API_PipeTargetParameters_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pipes-2015-10-07/PipeTargetParameters) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pipes-2015-10-07/PipeTargetParameters) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pipes-2015-10-07/PipeTargetParameters) 