

# API reference
<a name="training-sessions-api"></a>

The training session APIs expose two groups of API operations: control-plane operations that manage the session lifecycle, and runtime operations that run training and sampling against an active session. For complete request and response syntax, see the reference pages linked below.

## Control plane (session management)
<a name="training-sessions-api-control-plane"></a>

Control-plane operations are part of the SageMaker AI API. Use them to create, inspect, stop, and delete training sessions.
+ [CreateTrainingSession](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateTrainingSession.html)
+ [DescribeTrainingSession](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DescribeTrainingSession.html)
+ [ListTrainingSessions](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ListTrainingSessions.html)
+ [StopTrainingSession](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_StopTrainingSession.html)
+ [DeleteTrainingSession](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DeleteTrainingSession.html)

## Runtime API (training and sampling operations)
<a name="training-sessions-api-runtime"></a>

Runtime operations are part of the SageMaker AI Training Session Runtime API, a separate service endpoint from the SageMaker AI control plane. You call them against an active session to submit training steps and to generate samples from the in-training model. For the full reference, see the [*SageMaker AI Training Session Runtime API Reference*](https://docs.aws.amazon.com/sagemakertrainingsession/latest/APIReference/Welcome.html).

**Training operations**
+ [ExecuteTrainingOperation](https://docs.aws.amazon.com/sagemakertrainingsession/latest/APIReference/API_ExecuteTrainingOperation.html)
+ [GetTrainingOperationResult](https://docs.aws.amazon.com/sagemakertrainingsession/latest/APIReference/API_GetTrainingOperationResult.html)

**Sampling operations**
+ [ExecuteSamplingOperation](https://docs.aws.amazon.com/sagemakertrainingsession/latest/APIReference/API_ExecuteSamplingOperation.html)
+ [GetSamplingOperationResult](https://docs.aws.amazon.com/sagemakertrainingsession/latest/APIReference/API_GetSamplingOperationResult.html)
+ [SampleTrainingSession](https://docs.aws.amazon.com/sagemakertrainingsession/latest/APIReference/API_SampleTrainingSession.html)
+ [SampleTrainingSessionWithResponseStream](https://docs.aws.amazon.com/sagemakertrainingsession/latest/APIReference/API_SampleTrainingSessionWithResponseStream.html)

Sampling also supports an OpenAI-compatible chat completions endpoint, so you can point existing OpenAI client code at an active training session.