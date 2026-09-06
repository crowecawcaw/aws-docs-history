

# API Reference guide for Autopilot
<a name="autopilot-reference"></a>

This section provides a subset of the HTTP service REST APIs for creating and managing Amazon SageMaker Autopilot resources (AutoML jobs) programmatically.

If your language of choice is Python, you can refer to [AWS SDK for Python (Boto3)](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html) or the [AutoMLV2 object](https://sagemaker.readthedocs.io/en/stable/api/sagemaker_train.html) of the Amazon SageMaker Python SDK directly.

## AutoML API Actions
<a name="autopilot-api-actions"></a>

This list details the operations available in the Reference API to manage AutoML jobs programmatically.
+ [`CreateAutoMLJob`](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateAutoMLJob.html)
+ [`CreateAutoMLJobV2`](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateAutoMLJobV2.html)
+ [`DescribeAutoMLJob`](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DescribeAutoMLJob.html)
+ [`DescribeAutoMLJobV2`](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DescribeAutoMLJobV2.html)
+ [`ListAutoMLJobs`](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ListAutoMLJobs.html)
+ [`ListCandidatesForAutoMLJob`](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ListCandidatesForAutoMLJob.html)
+ [`StopAutoMLJob`](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_StopAutoMLJob.html)

**Note**  
[CreateAutoMLJobV2](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateAutoMLJobV2.html) and [DescribeAutoMLJobV2](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DescribeAutoMLJobV2.html) are new versions of [CreateAutoMLJob](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateAutoMLJob.html) and [DescribeAutoMLJob](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DescribeAutoMLJob.html) which offer backward compatibility.  
We recommend using the `CreateAutoMLJobV2`. `CreateAutoMLJobV2` can manage tabular problem types identical to those of its previous version `CreateAutoMLJob`, as well as non-tabular problem types such as image or text classification, or time-series forecasting.  
Find guidelines about how to migrate a `CreateAutoMLJob` to `CreateAutoMLJobV2` in [Migrate a CreateAutoMLJob to CreateAutoMLJobV2](https://docs.aws.amazon.com/sagemaker/latest/dg/autopilot-automate-model-development-create-experiment.html#autopilot-create-experiment-api-migrate-v1-v2).

## AutoML API Data Types
<a name="autopilot-api-data-types"></a>

This list details the API AutoML objects used by the actions above as inbound requests or outbound responses.
+ [`AutoMLAlgorithmConfig`](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_AutoMLAlgorithmConfig.html)
+ [`AutoMLCandidate`](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_AutoMLCandidate.html)
+ [`AutoMLCandidateGenerationConfig`](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_AutoMLCandidateGenerationConfig.html)
+ [`AutoMLCandidateStep`](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_AutoMLCandidateStep.html)
+ [`AutoMLChannel`](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_AutoMLChannel.html)
+ [`AutoMLContainerDefinition`](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_AutoMLContainerDefinition.html)
+ [`AutoMLDataSource`](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_AutoMLDataSource.html)
+ [`AutoMLDataSplitConfig`](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_AutoMLDataSplitConfig.html)
+ [`AutoMLInferenceContainerDefinitions`](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_AutoMLInferenceContainerDefinitions.html)
+ [`AutoMLJobArtifacts`](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_AutoMLJobArtifacts.html)
+ [`AutoMLJobChannel`](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_AutoMLJobChannel.html)
+ [`AutoMLJobCompletionCriteria`](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_AutoMLJobCompletionCriteria.html)
+ [`AutoMLJobInputDataConfig`](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_AutoMLJobInputDataConfig.html)
+ [`AutoMLJobConfig`](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_AutoMLJobConfig.html)
+ [`AutoMLJobObjective`](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_AutoMLJobObjective.html)
+ [`AutoMLJobStepMetadata`](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_AutoMLJobStepMetadata.html)
+ [`AutoMLJobSummary`](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_AutoMLJobSummary.html)
+ [`AutoMLOutputDataConfig`](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_AutoMLOutputDataConfig.html)
+ [`AutoMLProblemTypeConfig`](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_AutoMLProblemTypeConfig.html)
+ [`AutoMLJobCompletionCriteria`](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_AutoMLJobCompletionCriteria.html)
+ [`AutoMLJobSummary`](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_AutoMLJobSummary.html)
+ [`AutoMLOutputDataConfig`](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_AutoMLOutputDataConfig.html)
+ [`AutoMLPartialFailureReason`](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_AutoMLPartialFailureReason.html) 
+ [`AutoMLProblemTypeConfig`](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_AutoMLProblemTypeConfig.html)
+ [`AutoMLProblemTypeResolvedAttributes`](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_AutoMLProblemTypeResolvedAttributes.html)
+ [`AutoMLResolvedAttributes`](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_AutoMLResolvedAttributes.html)
+ [`AutoMLSecurityConfig`](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_AutoMLSecurityConfig.html)
+ [`AutoMLS3DataSource`](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_AutoMLS3DataSource.html)
+ [`CandidateArtifactLocations`](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CandidateArtifactLocations.html) 
+ [`CandidateGenerationConfig`](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CandidateGenerationConfig.html)
+ [`CandidateProperties`](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CandidateProperties.html) 
+ [`FinalAutoMLJobObjectiveMetric`](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_FinalAutoMLJobObjectiveMetric.html) 
+ [`HolidayConfigAttributes`](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_HolidayConfigAttributes.html) 
+ [`ImageClassificationJobConfig`](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ImageClassificationJobConfig.html)
+ [`MetricDatum`](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_MetricDatum.html) 
+ [`ModelDeployConfig`](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ModelDeployConfig.html) 
+ [`ModelDeployResult`](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ModelDeployResult.html) 
+ [`ResolvedAttributes`](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ResolvedAttributes.html)
+ [`TabularJobConfig`](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_TabularJobConfig.html)
+ [`TabularResolvedAttributes`](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_TabularResolvedAttributes.html)
+ [`TextGenerationJobConfig`](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_TextGenerationJobConfig.html)
+ [`TextGenerationResolvedAttribute`](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_TextGenerationResolvedAttribute.html)
+ [`TimeSeriesConfig`](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_TimeSeriesConfig.html)
+ [`TimeSeriesForecastingJobConfig`](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_TimeSeriesForecastingJobConfig.html)
+ [`TimeSeriesTransformations`](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_TimeSeriesTransformations.html)
+ [`TuningJobCompletionCriteria`](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_TuningJobCompletionCriteria.html)