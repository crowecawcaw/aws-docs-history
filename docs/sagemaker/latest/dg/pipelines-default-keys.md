# Default cache key attributes by pipeline step

type

When deciding whether to reuse a previous pipeline step or rerun the step, Pipelines checks to
see if certain attributes have changed. If the set of attributes is different from all
previous runs within the timeout period, the step runs again. These attributes include input
artifacts, app or algorithm specification, and environment variables. The following list shows
each pipeline step type and the attributes that, if changed, initiate a rerun of the step. For
more information about which Python SDK parameters are used to create the following
attributes, see [Caching Configuration](https://sagemaker.readthedocs.io/en/stable/amazon_sagemaker_model_building_pipeline.html#caching-configuration "https://sagemaker.readthedocs.io/en/stable/amazon_sagemaker_model_building_pipeline.html#caching-configuration") in the Amazon SageMaker Python SDK documentation.

- AppSpecification
- Environment
- ProcessingInputs. This attribute contains information about the preprocessing script.

- AlgorithmSpecification
- CheckpointConfig
- DebugHookConfig
- DebugRuleConfigurations
- Environment
- HyperParameters
- InputDataConfig. This attribute contains information about the training script.

- HyperParameterTuningJobConfig
- TrainingJobDefinition. This attribute is composed of multiple child attributes, not
  all of which cause the step to rerun. The child attributes that could incur a rerun (if
  changed) are:
  - AlgorithmSpecification
  - HyperParameterRanges
  - InputDataConfig
  - StaticHyperParameters
  - TuningObjective

- TrainingJobDefinitions

- AutoMLJobConfig. This attribute is composed of multiple child attributes, not
  all of which cause the step to rerun. The child attributes that could incur a rerun (if
  changed) are:
  - CompletionCriteria
  - CandidateGenerationConfig
  - DataSplitConfig
  - Mode

- AutoMLJobObjective
- InputDataConfig
- ProblemType

- DataProcessing
- Environment
- ModelName
- TransformInput

- ClarifyCheckConfig
- CheckJobConfig
- SkipCheck
- RegisterNewBaseline
- ModelPackageGroupName
- SuppliedBaselineConstraints

- QualityCheckConfig
- CheckJobConfig
- SkipCheck
- RegisterNewBaseline
- ModelPackageGroupName
- SuppliedBaselineConstraints
- SuppliedBaselineStatistics

- ClusterId
- StepConfig
