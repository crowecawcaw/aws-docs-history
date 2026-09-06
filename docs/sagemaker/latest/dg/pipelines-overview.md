

# Pipelines overview
<a name="pipelines-overview"></a>

An Amazon SageMaker AI pipeline is a series of interconnected steps in directed acyclic graph (DAG) that are defined using the drag-and-drop UI or [Pipelines SDK](https://sagemaker.readthedocs.io/en/stable/api/sagemaker_mlops.html). You can also build your pipeline using the [pipeline definition JSON schema](https://aws-sagemaker-mlops.github.io/sagemaker-model-building-pipeline-definition-JSON-schema/). This DAG JSON definition gives information on the requirements and relationships between each step of your pipeline. The structure of a pipeline's DAG is determined by the data dependencies between steps. These data dependencies are created when the properties of a step's output are passed as the input to another step. The following image is an example of a pipeline DAG:

![An example pipeline directed acyclic graph (DAG).](http://docs.aws.amazon.com/sagemaker/latest/dg/images/pipeline-full.png)


**The example DAG includes the following steps:**

1. `AbaloneProcess`, an instance of the [Processing](https://docs.aws.amazon.com/sagemaker/latest/dg/build-and-manage-steps.html#step-type-processing) step, runs a preprocessing script on the data used for training. For example, the script could fill in missing values, normalize numerical data, or split data into the train, validation, and test datasets.

1. `AbaloneTrain`, an instance of the [Training](https://docs.aws.amazon.com/sagemaker/latest/dg/build-and-manage-steps.html#step-type-training) step, configures hyperparameters and trains a model from the preprocessed input data.

1. `AbaloneEval`, another instance of the [Processing](https://docs.aws.amazon.com/sagemaker/latest/dg/build-and-manage-steps.html#step-type-processing) step, evaluates the model for accuracy. This step shows an example of a data dependency—this step uses the test dataset output of the `AbaloneProcess`.

1. `AbaloneMSECond` is an instance of a [Condition](https://docs.aws.amazon.com/sagemaker/latest/dg/build-and-manage-steps.html#step-type-condition) step which, in this example, checks to make sure the mean-square-error result of model evaluation is below a certain limit. If the model does not meet the criteria, the pipeline run stops.

1. The pipeline run proceeds with the following steps:

   1. `AbaloneRegisterModel`, where SageMaker AI calls a [RegisterModel](https://docs.aws.amazon.com/sagemaker/latest/dg/build-and-manage-steps.html#step-type-register-model) step to register the model as a versioned model package group into the Amazon SageMaker Model Registry.

   1. `AbaloneCreateModel`, where SageMaker AI calls a [CreateModel](https://docs.aws.amazon.com/sagemaker/latest/dg/build-and-manage-steps.html#step-type-create-model) step to create the model in preparation for batch transform. In `AbaloneTransform`, SageMaker AI calls a [Transform](https://docs.aws.amazon.com/sagemaker/latest/dg/build-and-manage-steps.html#step-type-transform) step to generate model predictions on a dataset you specify.

The following topics describe fundamental Pipelines concepts. For a tutorial describing the implementation of these concepts, see [Pipelines actions](pipelines-build.md).

**Topics**
+ [Pipeline Structure and Execution](build-and-manage-pipeline.md)
+ [IAM Access Management](build-and-manage-access.md)
+ [Set up cross-account support for Pipelines](build-and-manage-xaccount.md)
+ [Pipeline parameters](build-and-manage-parameters.md)
+ [Pipelines steps](build-and-manage-steps.md)
+ [Lift-and-shift Python code with the @step decorator](pipelines-step-decorator.md)
+ [Pass Data Between Steps](build-and-manage-propertyfile.md)
+ [Caching pipeline steps](pipelines-caching.md)
+ [Retry Policy for Pipeline Steps](pipelines-retry-policy.md)
+ [Selective execution of pipeline steps](pipelines-selective-ex.md)
+ [Baseline calculation, drift detection and lifecycle with ClarifyCheck and QualityCheck steps in Amazon SageMaker Pipelines](pipelines-quality-clarify-baseline-lifecycle.md)
+ [Schedule Pipeline Runs](pipeline-eventbridge.md)
+ [Amazon SageMaker Experiments Integration](pipelines-experiments.md)
+ [Run pipelines using local mode](pipelines-local-mode.md)
+ [Troubleshooting Amazon SageMaker Pipelines](pipelines-troubleshooting.md)