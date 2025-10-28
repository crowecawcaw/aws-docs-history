# PipeTargetParameters

The parameters required to set up a target for your pipe.

For more information about pipe target parameters, including how to use dynamic path parameters, see [Target parameters](../userguide/eb-pipes-event-target.md "../userguide/eb-pipes-event-target.md") in the _Amazon EventBridge User Guide_.

## Contents

**BatchJobParameters**

The parameters for using an AWS Batch job as a target.

Type: [PipeTargetBatchJobParameters](API_PipeTargetBatchJobParameters.md "API_PipeTargetBatchJobParameters.md") object

Required: No

**CloudWatchLogsParameters**

The parameters for using an CloudWatch Logs log stream as a target.

Type: [PipeTargetCloudWatchLogsParameters](API_PipeTargetCloudWatchLogsParameters.md "API_PipeTargetCloudWatchLogsParameters.md") object

Required: No

**EcsTaskParameters**

The parameters for using an Amazon ECS task as a target.

Type: [PipeTargetEcsTaskParameters](API_PipeTargetEcsTaskParameters.md "API_PipeTargetEcsTaskParameters.md") object

Required: No

**EventBridgeEventBusParameters**

The parameters for using an EventBridge event bus as a target.

Type: [PipeTargetEventBridgeEventBusParameters](API_PipeTargetEventBridgeEventBusParameters.md "API_PipeTargetEventBridgeEventBusParameters.md") object

Required: No

**HttpParameters**

These are custom parameter to be used when the target is an API Gateway REST APIs or
EventBridge ApiDestinations.

Type: [PipeTargetHttpParameters](API_PipeTargetHttpParameters.md "API_PipeTargetHttpParameters.md") object

Required: No

**InputTemplate**

Valid JSON text passed to the target. In this case, nothing from the event itself is
passed to the target. For more information, see [The JavaScript Object Notation (JSON)
Data Interchange Format](http://www.rfc-editor.org/rfc/rfc7159.txt "http://www.rfc-editor.org/rfc/rfc7159.txt").

To remove an input template, specify an empty string.

Type: String

Length Constraints: Minimum length of 0. Maximum length of 8192.

Required: No

**KinesisStreamParameters**

The parameters for using a Kinesis stream as a target.

Type: [PipeTargetKinesisStreamParameters](API_PipeTargetKinesisStreamParameters.md "API_PipeTargetKinesisStreamParameters.md") object

Required: No

**LambdaFunctionParameters**

The parameters for using a Lambda function as a target.

Type: [PipeTargetLambdaFunctionParameters](API_PipeTargetLambdaFunctionParameters.md "API_PipeTargetLambdaFunctionParameters.md") object

Required: No

**RedshiftDataParameters**

These are custom parameters to be used when the target is a Amazon Redshift cluster to invoke the
Amazon Redshift Data API BatchExecuteStatement.

Type: [PipeTargetRedshiftDataParameters](API_PipeTargetRedshiftDataParameters.md "API_PipeTargetRedshiftDataParameters.md") object

Required: No

**SageMakerPipelineParameters**

The parameters for using a SageMaker AI pipeline as a target.

Type: [PipeTargetSageMakerPipelineParameters](API_PipeTargetSageMakerPipelineParameters.md "API_PipeTargetSageMakerPipelineParameters.md") object

Required: No

**SqsQueueParameters**

The parameters for using a Amazon SQS stream as a target.

Type: [PipeTargetSqsQueueParameters](API_PipeTargetSqsQueueParameters.md "API_PipeTargetSqsQueueParameters.md") object

Required: No

**StepFunctionStateMachineParameters**

The parameters for using a Step Functions state machine as a target.

Type: [PipeTargetStateMachineParameters](API_PipeTargetStateMachineParameters.md "API_PipeTargetStateMachineParameters.md") object

Required: No

**TimestreamParameters**

The parameters for using a Timestream for LiveAnalytics table as a
target.

Type: [PipeTargetTimestreamParameters](API_PipeTargetTimestreamParameters.md "API_PipeTargetTimestreamParameters.md") object

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/pipes-2015-10-07/PipeTargetParameters.md "../../../goto/SdkForCpp/pipes-2015-10-07/PipeTargetParameters.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/pipes-2015-10-07/PipeTargetParameters.md "../../../goto/SdkForJavaV2/pipes-2015-10-07/PipeTargetParameters.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/pipes-2015-10-07/PipeTargetParameters.md "../../../goto/SdkForRubyV3/pipes-2015-10-07/PipeTargetParameters.md")
