# API Reference guide for Autopilot

This section provides a subset of the HTTP service REST APIs for creating and managing
Amazon SageMaker Autopilot resources (AutoML jobs) programmatically.

If your language of choice is Python, you can refer to [AWS SDK for Python (Boto3)](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html "https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html") or the [AutoMLV2 object](https://sagemaker.readthedocs.io/en/stable/api/training/automlv2.html#sagemaker.automl.automlv2.AutoMLV2 "https://sagemaker.readthedocs.io/en/stable/api/training/automlv2.html#sagemaker.automl.automlv2.AutoMLV2") of the Amazon SageMaker Python SDK directly.

## AutoML API Actions

This list details the operations available in the Reference API to manage AutoML jobs
programmatically.

- [`CreateAutoMLJob`](../APIReference/API_CreateAutoMLJob.md "../APIReference/API_CreateAutoMLJob.md")
- [`CreateAutoMLJobV2`](../APIReference/API_CreateAutoMLJobV2.md "../APIReference/API_CreateAutoMLJobV2.md")
- [`DescribeAutoMLJob`](../APIReference/API_DescribeAutoMLJob.md "../APIReference/API_DescribeAutoMLJob.md")
- [`DescribeAutoMLJobV2`](../APIReference/API_DescribeAutoMLJobV2.md "../APIReference/API_DescribeAutoMLJobV2.md")
- [`ListAutoMLJobs`](../APIReference/API_ListAutoMLJobs.md "../APIReference/API_ListAutoMLJobs.md")
- [`ListCandidatesForAutoMLJob`](../APIReference/API_ListCandidatesForAutoMLJob.md "../APIReference/API_ListCandidatesForAutoMLJob.md")
- [`StopAutoMLJob`](../APIReference/API_StopAutoMLJob.md "../APIReference/API_StopAutoMLJob.md")

###### Note

[CreateAutoMLJobV2](../APIReference/API_CreateAutoMLJobV2.md "../APIReference/API_CreateAutoMLJobV2.md")
and [DescribeAutoMLJobV2](../APIReference/API_DescribeAutoMLJobV2.md "../APIReference/API_DescribeAutoMLJobV2.md") are new versions of [CreateAutoMLJob](../APIReference/API_CreateAutoMLJob.md "../APIReference/API_CreateAutoMLJob.md") and
[DescribeAutoMLJob](../APIReference/API_DescribeAutoMLJob.md "../APIReference/API_DescribeAutoMLJob.md") which offer backward compatibility.

We recommend using the `CreateAutoMLJobV2`. `CreateAutoMLJobV2` can
manage tabular problem types identical to those of its previous version
`CreateAutoMLJob`, as well as non-tabular problem types such as image or text
classification, or time-series forecasting.

Find guidelines about how to migrate a `CreateAutoMLJob` to
`CreateAutoMLJobV2` in [Migrate a CreateAutoMLJob to CreateAutoMLJobV2](autopilot-automate-model-development-create-experiment.md#autopilot-create-experiment-api-migrate-v1-v2 "autopilot-automate-model-development-create-experiment.md#autopilot-create-experiment-api-migrate-v1-v2").

## AutoML API Data Types

This list details the API AutoML objects used by the actions above as inbound requests or
outbound responses.

- [`AutoMLAlgorithmConfig`](../APIReference/API_AutoMLAlgorithmConfig.md "../APIReference/API_AutoMLAlgorithmConfig.md")
- [`AutoMLCandidate`](../APIReference/API_AutoMLCandidate.md "../APIReference/API_AutoMLCandidate.md")
- [`AutoMLCandidateGenerationConfig`](../APIReference/API_AutoMLCandidateGenerationConfig.md "../APIReference/API_AutoMLCandidateGenerationConfig.md")
- [`AutoMLCandidateStep`](../APIReference/API_AutoMLCandidateStep.md "../APIReference/API_AutoMLCandidateStep.md")
- [`AutoMLChannel`](../APIReference/API_AutoMLChannel.md "../APIReference/API_AutoMLChannel.md")
- [`AutoMLContainerDefinition`](../APIReference/API_AutoMLContainerDefinition.md "../APIReference/API_AutoMLContainerDefinition.md")
- [`AutoMLDataSource`](../APIReference/API_AutoMLDataSource.md "../APIReference/API_AutoMLDataSource.md")
- [`AutoMLDataSplitConfig`](../APIReference/API_AutoMLDataSplitConfig.md "../APIReference/API_AutoMLDataSplitConfig.md")
- [`AutoMLInferenceContainerDefinitions`](../APIReference/API_AutoMLInferenceContainerDefinitions.md "../APIReference/API_AutoMLInferenceContainerDefinitions.md")
- [`AutoMLJobArtifacts`](../APIReference/API_AutoMLJobArtifacts.md "../APIReference/API_AutoMLJobArtifacts.md")
- [`AutoMLJobChannel`](../APIReference/API_AutoMLJobChannel.md "../APIReference/API_AutoMLJobChannel.md")
- [`AutoMLJobCompletionCriteria`](../APIReference/API_AutoMLJobCompletionCriteria.md "../APIReference/API_AutoMLJobCompletionCriteria.md")
- [`AutoMLJobInputDataConfig`](../APIReference/API_AutoMLJobInputDataConfig.md "../APIReference/API_AutoMLJobInputDataConfig.md")
- [`AutoMLJobConfig`](../APIReference/API_AutoMLJobConfig.md "../APIReference/API_AutoMLJobConfig.md")
- [`AutoMLJobObjective`](../APIReference/API_AutoMLJobObjective.md "../APIReference/API_AutoMLJobObjective.md")
- [`AutoMLJobStepMetadata`](../APIReference/API_AutoMLJobStepMetadata.md "../APIReference/API_AutoMLJobStepMetadata.md")
- [`AutoMLJobSummary`](../APIReference/API_AutoMLJobSummary.md "../APIReference/API_AutoMLJobSummary.md")
- [`AutoMLOutputDataConfig`](../APIReference/API_AutoMLOutputDataConfig.md "../APIReference/API_AutoMLOutputDataConfig.md")
- [`AutoMLProblemTypeConfig`](../APIReference/API_AutoMLProblemTypeConfig.md "../APIReference/API_AutoMLProblemTypeConfig.md")
- [`AutoMLJobCompletionCriteria`](../APIReference/API_AutoMLJobCompletionCriteria.md "../APIReference/API_AutoMLJobCompletionCriteria.md")
- [`AutoMLJobSummary`](../APIReference/API_AutoMLJobSummary.md "../APIReference/API_AutoMLJobSummary.md")
- [`AutoMLOutputDataConfig`](../APIReference/API_AutoMLOutputDataConfig.md "../APIReference/API_AutoMLOutputDataConfig.md")
- [`AutoMLPartialFailureReason`](../APIReference/API_AutoMLPartialFailureReason.md "../APIReference/API_AutoMLPartialFailureReason.md")
- [`AutoMLProblemTypeConfig`](../APIReference/API_AutoMLProblemTypeConfig.md "../APIReference/API_AutoMLProblemTypeConfig.md")
- [`AutoMLProblemTypeResolvedAttributes`](../APIReference/API_AutoMLProblemTypeResolvedAttributes.md "../APIReference/API_AutoMLProblemTypeResolvedAttributes.md")
- [`AutoMLResolvedAttributes`](../APIReference/API_AutoMLResolvedAttributes.md "../APIReference/API_AutoMLResolvedAttributes.md")
- [`AutoMLSecurityConfig`](../APIReference/API_AutoMLSecurityConfig.md "../APIReference/API_AutoMLSecurityConfig.md")
- [`AutoMLS3DataSource`](../APIReference/API_AutoMLS3DataSource.md "../APIReference/API_AutoMLS3DataSource.md")
- [`CandidateArtifactLocations`](../APIReference/API_CandidateArtifactLocations.md "../APIReference/API_CandidateArtifactLocations.md")
- [`CandidateGenerationConfig`](../APIReference/API_CandidateGenerationConfig.md "../APIReference/API_CandidateGenerationConfig.md")
- [`CandidateProperties`](../APIReference/API_CandidateProperties.md "../APIReference/API_CandidateProperties.md")
- [`FinalAutoMLJobObjectiveMetric`](../APIReference/API_FinalAutoMLJobObjectiveMetric.md "../APIReference/API_FinalAutoMLJobObjectiveMetric.md")
- [`HolidayConfigAttributes`](../APIReference/API_HolidayConfigAttributes.md "../APIReference/API_HolidayConfigAttributes.md")
- [`ImageClassificationJobConfig`](../APIReference/API_ImageClassificationJobConfig.md "../APIReference/API_ImageClassificationJobConfig.md")
- [`MetricDatum`](../APIReference/API_MetricDatum.md "../APIReference/API_MetricDatum.md")
- [`ModelDeployConfig`](../APIReference/API_ModelDeployConfig.md "../APIReference/API_ModelDeployConfig.md")
- [`ModelDeployResult`](../APIReference/API_ModelDeployResult.md "../APIReference/API_ModelDeployResult.md")
- [`ResolvedAttributes`](../APIReference/API_ResolvedAttributes.md "../APIReference/API_ResolvedAttributes.md")
- [`TabularJobConfig`](../APIReference/API_TabularJobConfig.md "../APIReference/API_TabularJobConfig.md")
- [`TabularResolvedAttributes`](../APIReference/API_TabularResolvedAttributes.md "../APIReference/API_TabularResolvedAttributes.md")
- [`TextGenerationJobConfig`](../APIReference/API_TextGenerationJobConfig.md "../APIReference/API_TextGenerationJobConfig.md")
- [`TextGenerationResolvedAttribute`](../APIReference/API_TextGenerationResolvedAttribute.md "../APIReference/API_TextGenerationResolvedAttribute.md")
- [`TimeSeriesConfig`](../APIReference/API_TimeSeriesConfig.md "../APIReference/API_TimeSeriesConfig.md")
- [`TimeSeriesForecastingJobConfig`](../APIReference/API_TimeSeriesForecastingJobConfig.md "../APIReference/API_TimeSeriesForecastingJobConfig.md")
- [`TimeSeriesTransformations`](../APIReference/API_TimeSeriesTransformations.md "../APIReference/API_TimeSeriesTransformations.md")
- [`TuningJobCompletionCriteria`](../APIReference/API_TuningJobCompletionCriteria.md "../APIReference/API_TuningJobCompletionCriteria.md")
