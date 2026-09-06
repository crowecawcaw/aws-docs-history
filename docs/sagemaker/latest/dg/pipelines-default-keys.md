

# Default cache key attributes by pipeline step type
<a name="pipelines-default-keys"></a>

When deciding whether to reuse a previous pipeline step or rerun the step, Pipelines checks to see if certain attributes have changed. If the set of attributes is different from all previous runs within the timeout period, the step runs again. These attributes include input artifacts, app or algorithm specification, and environment variables. The following list shows each pipeline step type and the attributes that, if changed, initiate a rerun of the step. For more information about which Python SDK parameters are used to create the following attributes, see [ Caching Configuration](https://sagemaker.readthedocs.io/en/stable/api/sagemaker_mlops.html#caching-configuration) in the Amazon SageMaker Python SDK documentation.

## [Processing step](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateProcessingJob.html)
<a name="collapsible-caching-section-1"></a>
+ AppSpecification
+ Environment
+ ProcessingInputs. This attribute contains information about the preprocessing script.

  

## [Training step](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateTrainingJob.html)
<a name="collapsible-caching-section-2"></a>
+ AlgorithmSpecification
+ CheckpointConfig
+ DebugHookConfig
+ DebugRuleConfigurations
+ Environment
+ HyperParameters
+ InputDataConfig. This attribute contains information about the training script.

  

## [Tuning step](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateHyperParameterTuningJob.html)
<a name="collapsible-caching-section-3"></a>
+ HyperParameterTuningJobConfig
+ TrainingJobDefinition. This attribute is composed of multiple child attributes, not all of which cause the step to rerun. The child attributes that could incur a rerun (if changed) are:
  + AlgorithmSpecification
  + HyperParameterRanges
  + InputDataConfig
  + StaticHyperParameters
  + TuningObjective
+ TrainingJobDefinitions

  

## [AutoML step](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_AutoMLJobConfig.html)
<a name="collapsible-caching-section-4"></a>
+ AutoMLJobConfig. This attribute is composed of multiple child attributes, not all of which cause the step to rerun. The child attributes that could incur a rerun (if changed) are:
  + CompletionCriteria
  + CandidateGenerationConfig
  + DataSplitConfig
  + Mode
+ AutoMLJobObjective
+ InputDataConfig
+ ProblemType

  

## [Transform step](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateTransformJob.html)
<a name="collapsible-caching-section-5"></a>
+ DataProcessing
+ Environment
+ ModelName
+ TransformInput

  

## [ClarifyCheck step](build-and-manage-steps-types.md#step-type-clarify-check)
<a name="collapsible-caching-section-6"></a>
+ ClarifyCheckConfig
+ CheckJobConfig
+ SkipCheck
+ RegisterNewBaseline
+ ModelPackageGroupName
+ SuppliedBaselineConstraints

  

## [QualityCheck step](build-and-manage-steps-types.md#step-type-quality-check)
<a name="collapsible-caching-section-7"></a>
+ QualityCheckConfig
+ CheckJobConfig
+ SkipCheck
+ RegisterNewBaseline
+ ModelPackageGroupName
+ SuppliedBaselineConstraints
+ SuppliedBaselineStatistics

  

## [EMR Step](https://docs.aws.amazon.com/sagemaker/latest/dg/build-and-manage-steps.html#step-type-emr)
<a name="collapsible-caching-section-8"></a>
+ ClusterId
+ StepConfig

  