

# Create Regression or Classification Jobs for Tabular Data Using the AutoML API
<a name="autopilot-automate-model-development-create-experiment"></a>

You can create an Autopilot regression or classification job for tabular data programmatically by calling the [`CreateAutoMLJobV2`](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateAutoMLJobV2.html) API action in any language supported by Autopilot or the AWS CLI. The following is a collection of mandatory and optional input request parameters for the `CreateAutoMLJobV2` API action. You can find the alternative information for the previous version of this action, `CreateAutoMLJob`. However, we recommend using `CreateAutoMLJobV2`. 

For information on how this API action translates into a function in the language of your choice, see the [ See Also](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateAutoMLJobV2.html#API_CreateAutoMLJobV2_SeeAlso) section of `CreateAutoMLJobV2` and choose an SDK. As an example, for Python users, see the full request syntax of `[create\_auto\_ml\_job\_v2](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.create_auto_ml_job_v2)` in AWS SDK for Python (Boto3).

**Note**  
[CreateAutoMLJobV2](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateAutoMLJobV2.html) and [DescribeAutoMLJobV2](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DescribeAutoMLJobV2.html) are new versions of [CreateAutoMLJob](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateAutoMLJob.html) and [DescribeAutoMLJob](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DescribeAutoMLJob.html) which offer backward compatibility.  
We recommend using the `CreateAutoMLJobV2`. `CreateAutoMLJobV2` can manage tabular problem types identical to those of its previous version `CreateAutoMLJob`, as well as non-tabular problem types such as image or text classification, or time-series forecasting.

At a minimum, all experiments on tabular data require the specification of the experiment name, providing locations for the input and output data, and specifying which target data to predict. Optionally, you can also specify the type of problem that you want to solve (regression, classification, multiclass classification), choose your modeling strategy (*stacked ensembles* or *hyperparameters optimization*), select the list of algorithms used by the Autopilot job to train the data, and more. 

 After the experiment runs, you can compare trials and delve into the details of the pre-processing steps, algorithms, and hyperparameter ranges of each model. You also have the option to download their [explainability](https://docs.aws.amazon.com/sagemaker/latest/dg/autopilot-explainability.html) and [performance](https://docs.aws.amazon.com/sagemaker/latest/dg/autopilot-model-insights.html) reports. Use the provided [ notebooks](https://docs.aws.amazon.com/sagemaker/latest/dg/autopilot-automate-model-development-notebook-output.html ) to see the results of the automated data exploration or the candidate model definitions.

Find guidelines on how to migrate a `CreateAutoMLJob` to `CreateAutoMLJobV2` in [Migrate a CreateAutoMLJob to CreateAutoMLJobV2](#autopilot-create-experiment-api-migrate-v1-v2).

## Required parameters
<a name="autopilot-create-experiment-api-required-params"></a>

------
#### [ CreateAutoMLJobV2 ]

When calling `[CreateAutoMLJobV2](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateAutoMLJobV2.html)` to create an Autopilot experiment for tabular data, you must provide the following values:
+ An `[AutoMLJobName](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateAutoMLJobV2.html#API_CreateAutoMLJobV2_RequestSyntax)` to specify the name of your job.
+ At least one `[AutoMLJobChannel](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_AutoMLJobChannel.html)` in `[AutoMLJobInputDataConfig](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateAutoMLJobV2.html#sagemaker-CreateAutoMLJobV2-request-AutoMLJobInputDataConfig)` to specify your data source.
+ Both an `[AutoMLJobObjective](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateAutoMLJobV2.html#sagemaker-CreateAutoMLJobV2-request-AutoMLJobObjective)` metric and your chosen type of supervised learning problem (binary classification, multiclass classification, regression) in `AutoMLProblemTypeConfig`, or none at all. For tabular data, you must choose `[TabularJobConfig](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_TabularJobConfig.html)` as the type of `[AutoMLProblemTypeConfig](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateAutoMLJobV2.html#sagemaker-CreateAutoMLJobV2-request-AutoMLProblemTypeConfig)`. You set the supervised learning problem in the `ProblemType` attribute of `TabularJobConfig`.
+ An `[OutputDataConfig](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_AutoMLOutputDataConfig.html)` to specify the Amazon S3 output path to store the artifacts of your AutoML job.
+ A `[RoleArn](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateAutoMLJob.html#sagemaker-CreateAutoMLJob-request-RoleArn)` to specify the ARN of the role used to access your data.

------
#### [ CreateAutoMLJob ]

When calling `[CreateAutoMLJob](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateAutoMLJob.html)` to create an AutoML experiment, you must provide the following four values:
+ An `[AutoMLJobName](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateAutoMLJob.html#sagemaker-CreateAutoMLJob-request-AutoMLJobName)` to specify the name of your job.
+ At least one `[AutoMLChannel](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_AutoMLChannel.html)` in `[InputDataConfig](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateAutoMLJob.html#sagemaker-CreateAutoMLJob-request-InputDataConfig)` to specify your data source.
+ An `[OutputDataConfig](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_AutoMLOutputDataConfig.html)` to specify the Amazon S3 output path to store the artifacts of your AutoML job.
+ A `[RoleArn](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateAutoMLJob.html#sagemaker-CreateAutoMLJob-request-RoleArn)` to specify the ARN of the role used to access your data.

------

All other parameters are optional.

## Optional parameters
<a name="autopilot-create-experiment-api-optional-params"></a>

The following sections provide details of some optional parameters that you can pass to your `CreateAutoMLJobV2` API action when using tabular data. You can find the alternative information for the previous version of this action, `CreateAutoMLJob`. However, we recommend using `CreateAutoMLJobV2`.

### How to set the training mode of an AutoML job
<a name="autopilot-set-training-mode"></a>

For tabular data, the set of algorithms run on your data to train your model candidates is dependent on your modeling strategy (`ENSEMBLING` or `HYPERPARAMETER_TUNING`). The following details how to set this training mode.

If you keep blank (or `null`), the `Mode` is inferred based on the size of your dataset.

For information on Autopilot's *stacked ensembles* and *hyperparameters optimization* training methods, see [Training modes and algorithm support](autopilot-model-support-validation.md)

------
#### [ CreateAutoMLJobV2 ]

For tabular data, you must choose `[TabularJobConfig](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_TabularJobConfig.html)` as the type of `[AutoMLProblemTypeConfig](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateAutoMLJobV2.html#sagemaker-CreateAutoMLJobV2-request-AutoMLProblemTypeConfig)`.

You can set the [training method](https://docs.aws.amazon.com/sagemaker/latest/dg/autopilot-model-support-validation.html) of an AutoML job V2 with the `[TabularJobConfig.Mode](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_TabularJobConfig.html)` parameter.

------
#### [ CreateAutoMLJob ]

You can set the [training method](https://docs.aws.amazon.com/sagemaker/latest/dg/autopilot-model-support-validation.html) of an AutoML job with the `[AutoMLJobConfig.Mode](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_AutoMLJobConfig.html#sagemaker-Type-AutoMLJobConfig-Mode)` parameter.

------

### How to select features and algorithms for training an AutoML job
<a name="autopilot-feature-selection"></a>

#### Features selection
<a name="autopilot-automl-job-feature-selection-api"></a>

Autopilot provides automatic data-preprocessing steps including feature selection and feature extraction. However, you can manually provide the features to be used in training with the `FeatureSpecificatioS3Uri` attribute.

Selected features should be contained within a JSON file in the following format:

```
{ "FeatureAttributeNames":["col1", "col2", ...] }
```

The values listed in `["col1", "col2", ...]` are case sensitive. They should be a list of strings containing unique values that are subsets of the column names in the input data.

**Note**  
The list of columns provided as features cannot include the target column.

------
#### [ CreateAutoMLJobV2 ]

For tabular data, you must choose `[TabularJobConfig](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_TabularJobConfig.html)` as the type of `[AutoMLProblemTypeConfig](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateAutoMLJobV2.html#sagemaker-CreateAutoMLJobV2-request-AutoMLProblemTypeConfig)`.

You can set the URL to your selected features with the `[TabularJobConfig.FeatureSpecificationS3Uri](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_TabularJobConfig.html)` parameter.

------
#### [ CreateAutoMLJob ]

You can set the `FeatureSpecificatioS3Uri` attribute of [AutoMLCandidateGenerationConfig](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_AutoMLCandidateGenerationConfig.html) within the [CreateAutoMLJob](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateAutoMLJob.html) API with the following format:

```
{
    "[AutoMLJobConfig](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateAutoMLJob.html#sagemaker-CreateAutoMLJob-request-AutoMLJobConfig)": {
        "[CandidateGenerationConfig](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_AutoMLJobConfig.html#sagemaker-Type-AutoMLJobConfig-CandidateGenerationConfig)": {
            "[FeatureSpecificationS3Uri](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_AutoMLCandidateGenerationConfig.html#sagemaker-Type-AutoMLCandidateGenerationConfig-FeatureSpecificationS3Uri)":"string"
            },
       }
  }
```

------

#### Algorithms selection
<a name="autopilot-automl-job-algorithms-selection-api"></a>

By default, your Autopilot job runs a pre-defined list of algorithms on your dataset to train model candidates. The list of algorithms depends on the training mode (`ENSEMBLING` or `HYPERPARAMETER_TUNING`) used by the job.

You can provide a subset of the default selection of algorithms.

------
#### [ CreateAutoMLJobV2 ]

For tabular data, you must choose `[TabularJobConfig](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_TabularJobConfig.html)` as the type of `[AutoMLProblemTypeConfig](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateAutoMLJobV2.html#sagemaker-CreateAutoMLJobV2-request-AutoMLProblemTypeConfig)`.

You can specify an array of selected `AutoMLAlgorithms` in the `AlgorithmsConfig` attribute of [CandidateGenerationConfig](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CandidateGenerationConfig.html).

The following is an example of an `AlgorithmsConfig` attribute listing exactly three algorithms ("xgboost", "fastai", "catboost") in its `AutoMLAlgorithms` field for the ensembling training mode.

```
{
   "[AutoMLProblemTypeConfig](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateAutoMLJobV2.html#sagemaker-CreateAutoMLJobV2-request-AutoMLProblemTypeConfig)": {
        "[TabularJobConfig](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_TabularJobConfig.html)": {
          "[Mode](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_TabularJobConfig.html)": "ENSEMBLING",
          "[CandidateGenerationConfig](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CandidateGenerationConfig.html)": {
            "[AlgorithmsConfig](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CandidateGenerationConfig.html#sagemaker-Type-CandidateGenerationConfig-AlgorithmsConfig)":[
               {"[AutoMLAlgorithms](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_AutoMLAlgorithmConfig.html)":["xgboost", "fastai", "catboost"]}
            ]
         },
       },
     },
  }
```

------
#### [ CreateAutoMLJob ]

You can specify an array of selected `AutoMLAlgorithms` in the `AlgorithmsConfig` attribute of [AutoMLCandidateGenerationConfig](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_AutoMLCandidateGenerationConfig.html).

The following is an example of an `AlgorithmsConfig` attribute listing exactly three algorithms ("xgboost", "fastai", "catboost") in its `AutoMLAlgorithms` field for the ensembling training mode.

```
{
   "[AutoMLJobConfig](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateAutoMLJob.html#sagemaker-CreateAutoMLJob-request-AutoMLJobConfig)": {
        "[CandidateGenerationConfig](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_AutoMLJobConfig.html#sagemaker-Type-AutoMLJobConfig-CandidateGenerationConfig)": {
            "[AlgorithmsConfig](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_AutoMLCandidateGenerationConfig.html#sagemaker-Type-AutoMLCandidateGenerationConfig-AlgorithmsConfig)":[
               {"[AutoMLAlgorithms](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_AutoMLAlgorithmConfig.html#sagemaker-Type-AutoMLAlgorithmConfig-AutoMLAlgorithms)":["xgboost", "fastai", "catboost"]}
            ]
         },
     "Mode": "ENSEMBLING" 
  }
```

------

For the list of available algorithms per training `Mode`, see [`AutoMLAlgorithms`](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_AutoMLAlgorithmConfig.html#sagemaker-Type-AutoMLAlgorithmConfig-AutoMLAlgorithms). For details on each algorithm, see [Training modes and algorithm support](autopilot-model-support-validation.md).

### How to specify the training and validation datasets of an AutoML job
<a name="autopilot-data-sources-training-or-validation"></a>

You can provide your own validation dataset and custom data split ratio, or let Autopilot split the dataset automatically.

------
#### [ CreateAutoMLJobV2 ]

Each [`AutoMLJobChannel`](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_AutoMLJobChannel.html) object (see the required parameter [AutoMLJobInputDataConfig](https://docs.aws.amazon.com/sagemaker-api/src/AWSSageMakerAPIDoc/build/server-root/sagemaker/latest/APIReference/API_CreateAutoMLJobV2.html#sagemaker-CreateAutoMLJobV2-request-AutoMLJobInputDataConfig)) has a `ChannelType`, which can be set to either `training` or `validation` values that specify how the data is to be used when building a machine learning model. At least one data source must be provided and a maximum of two data sources is allowed: one for training data and one for validation data.

How you split the data into training and validation datasets depends on whether you have one or two data sources.
+ If you only have **one data source**, the `ChannelType` is set to `training` by default and must have this value.
  + If the `ValidationFraction` value in [`AutoMLDataSplitConfig`](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_AutoMLDataSplitConfig.html) is not set, 0.2 (20%) of the data from this source is used for validation by default. 
  + If the `ValidationFraction` is set to a value between 0 and 1, the dataset is split based on the value specified, where the value specifies the fraction of the dataset used for validation.
+ If you have **two data sources**, the `ChannelType` of one of the `AutoMLJobChannel` objects must be set to `training`, the default value. The `ChannelType` of the other data source must be set to `validation`. The two data sources must have the same format, either CSV or Parquet, and the same schema. You must not set the value for the `ValidationFraction` in this case because all of the data from each source is used for either training or validation. Setting this value causes an error.

------
#### [ CreateAutoMLJob ]

Each [`AutoMLChannel`](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_AutoMLChannel.html) object (see the required parameter [InputDataConfig](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateAutoMLJob.html#sagemaker-CreateAutoMLJob-request-InputDataConfig)) has a `ChannelType`, which can be set to either `training` or `validation` values that specify how the data is to be used when building a machine learning model. At least one data source must be provided and a maximum of two data sources is allowed: one for training data and one for validation data.

How you split the data into training and validation datasets depends on whether you have one or two data sources.
+ If you only have **one data source**, the `ChannelType` is set to `training` by default and must have this value.
  + If the `ValidationFraction` value in [`AutoMLDataSplitConfig`](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_AutoMLDataSplitConfig.html) is not set, 0.2 (20%) of the data from this source is used for validation by default. 
  + If the `ValidationFraction` is set to a value between 0 and 1, the dataset is split based on the value specified, where the value specifies the fraction of the dataset used for validation.
+ If you have **two data sources**, the `ChannelType` of one of the `AutoMLChannel` objects must be set to `training`, the default value. The `ChannelType` of the other data source must be set to `validation`. The two data sources must have the same format, either CSV or Parquet, and the same schema. You must not set the value for the `ValidationFraction` in this case because all of the data from each source is used for either training or validation. Setting this value causes an error.

------

For information on split and cross-validation in Autopilot see [Cross-validation in Autopilot](autopilot-metrics-validation.md#autopilot-cross-validation).

### How to set the problem type of an AutoML job
<a name="autopilot-set-problem-type-api"></a>

------
#### [ CreateAutoMLJobV2 ]

For tabular data, you must choose `[TabularJobConfig](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_TabularJobConfig.html)` as the type of `[AutoMLProblemTypeConfig](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateAutoMLJobV2.html#sagemaker-CreateAutoMLJobV2-request-AutoMLProblemTypeConfig)`.

You can further specify the type of supervised learning problem (binary classification, multiclass classification, regression) available for the model candidates of your AutoML job V2 with the `[TabularJobConfig.ProblemType](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_TabularJobConfig.html)` parameter.

------
#### [ CreateAutoMLJob ]

You can set the [type of problem](https://docs.aws.amazon.com/sagemaker/latest/dg/autopilot-datasets-problem-types.html#autopilot-problem-types) on an AutoML job with the `[CreateAutoPilot.ProblemType](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateAutoMLJob.html#sagemaker-CreateAutoMLJob-request-ProblemType)` parameter. This limits the kind of preprocessing and algorithms that Autopilot tries. After the job is finished, if you had set the `[CreateAutoPilot.ProblemType](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateAutoMLJob.html#sagemaker-CreateAutoMLJob-request-ProblemType)`, then the `[ResolvedAttribute.ProblemType](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ResolvedAttributes.html)` matches the `ProblemType` you set. If you keep it blank (or `null`), the `ProblemType` is inferred on your behalf. 

------

**Note**  
In some cases, Autopilot is unable to infer the `ProblemType` with high enough confidence, in which case you must provide the value for the job to succeed.

### How to add sample weights to an AutoML job
<a name="autopilot-add-sample-weights-api"></a>

You can add a sample weights column to your tabular dataset and then pass it to your AutoML job to request dataset rows to be weighted during training and evaluation.

Support for sample weights is available in [ensembling mode](https://docs.aws.amazon.com/sagemaker/latest/dg/autopilot-model-support-validation.html#autopilot-training-mode) only. Your weights should be numeric and non-negative. Data points with invalid or no weight value are excluded. For more information on the available objective metrics, see [Autopilot weighted metrics](autopilot-metrics-validation.md#autopilot-weighted-metrics).

------
#### [ CreateAutoMLJobV2 ]

For tabular data, you must choose `[TabularJobConfig](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_TabularJobConfig.html)` as the type of `[AutoMLProblemTypeConfig](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateAutoMLJobV2.html#sagemaker-CreateAutoMLJobV2-request-AutoMLProblemTypeConfig)`.

To set sample weights when creating an experiment (see [CreateAutoMLJobV2](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateAutoMLJobV2.html)), you can pass the name of your sample weights column in the `SampleWeightAttributeName` attribute of the `TabularJobConfig` object. This ensures that your objective metric uses the weights for the training, evaluation, and selection of model candidates.

------
#### [ CreateAutoMLJob ]

To set sample weights when creating an experiment (see [CreateAutoMLJob](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateAutoMLJob.html)), you can pass the name of your sample weights column in the `SampleWeightAttributeName` attribute of the [AutoMLChannel](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_AutoMLChannel.html) object. This ensures that your objective metric uses the weights for the training, evaluation, and selection of model candidates.

------

### How to configure AutoML to initiate a remote job on EMR Serverless for large datasets
<a name="autopilot-set-emr-serverless-api-tabular"></a>

You can configure your AutoML job V2 to automatically initiate a remote job on Amazon EMR Serverless when additional compute resources are needed to process large datasets. By seamlessly transitioning to EMR Serverless when required, the AutoML job can handle datasets that would otherwise exceed the initially provisioned resources, without any manual intervention from you. EMR Serverless is available for the tabular and time series problem types. We recommend setting up this option for tabular datasets larger than 5 GB.

To allow your AutoML job V2 to automatically transition to EMR Serverless for large dataset, you need to provide an `EmrServerlessComputeConfig` object, which includes an `ExecutionRoleARN` field, to the `AutoMLComputeConfig` of the AutoML job V2 input request.

The `ExecutionRoleARN` is the ARN of the IAM role granting the AutoML job V2 the necessary permissions to run EMR Serverless jobs.

This role should have the following trust relationship:

------
#### [ JSON ]

****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": {
                "Service": "emr-serverless.amazonaws.com"
            },
            "Action": "sts:AssumeRole"
        }
    ]
}
```

------

And grant the permissions to:
+ Create, list, and update EMR Serverless applications.
+ Start, list, get, or cancel job runs on an EMR Serverless application.
+ Tag EMR Serverless resources.
+ Pass an IAM role to the EMR Serverless service for execution.

  By granting the `iam:PassRole` permission, the AutoML job V2 can temporarily assume the `EMRServerlessRuntimeRole-*` role and pass it to the EMR Serverless service. These are the IAM roles used by the EMR Serverless job execution environments to access other AWS services and resources needed during runtime, such as Amazon S3 for data access, CloudWatch for logging, access to the AWS Glue Data Catalog or other services based on your workload requirements.

  See [Job runtime roles for Amazon EMR Serverless](https://docs.aws.amazon.com/emr/latest/EMR-Serverless-UserGuide/security-iam-runtime-role.html) for details on this role permissions.

The IAM policy defined in the provided JSON document grants those permissions:

------
#### [ JSON ]

****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [{
            "Sid": "EMRServerlessCreateApplicationOperation",
            "Effect": "Allow",
            "Action": "emr-serverless:CreateApplication",
            "Resource": "arn:aws:emr-serverless:*:*:/*",
            "Condition": {
                "StringEquals": {
                    "aws:RequestTag/sagemaker:is-canvas-resource": "True",
                    "aws:ResourceAccount": "${aws:PrincipalAccount}"
                }
            }
        },
        {
            "Sid": "EMRServerlessListApplicationOperation",
            "Effect": "Allow",
            "Action": "emr-serverless:ListApplications",
            "Resource": "arn:aws:emr-serverless:*:*:/*",
            "Condition": {
                "StringEquals": {
                    "aws:ResourceAccount": "${aws:PrincipalAccount}"
                }
            }
        },
        {
            "Sid": "EMRServerlessApplicationOperations",
            "Effect": "Allow",
            "Action": [
                "emr-serverless:UpdateApplication",
                "emr-serverless:GetApplication"
            ],
            "Resource": "arn:aws:emr-serverless:*:*:/applications/*",
            "Condition": {
                "StringEquals": {
                    "aws:ResourceTag/sagemaker:is-canvas-resource": "True",
                    "aws:ResourceAccount": "${aws:PrincipalAccount}"
                }
            }
        },
        {
            "Sid": "EMRServerlessStartJobRunOperation",
            "Effect": "Allow",
            "Action": "emr-serverless:StartJobRun",
            "Resource": "arn:aws:emr-serverless:*:*:/applications/*",
            "Condition": {
                "StringEquals": {
                    "aws:RequestTag/sagemaker:is-canvas-resource": "True",
                    "aws:ResourceAccount": "${aws:PrincipalAccount}"
                }
            }
        },
        {
            "Sid": "EMRServerlessListJobRunOperation",
            "Effect": "Allow",
            "Action": "emr-serverless:ListJobRuns",
            "Resource": "arn:aws:emr-serverless:*:*:/applications/*",
            "Condition": {
                "StringEquals": {
                    "aws:ResourceTag/sagemaker:is-canvas-resource": "True",
                    "aws:ResourceAccount": "${aws:PrincipalAccount}"
                }
            }
        },
        {
            "Sid": "EMRServerlessJobRunOperations",
            "Effect": "Allow",
            "Action": [
                "emr-serverless:GetJobRun",
                "emr-serverless:CancelJobRun"
            ],
            "Resource": "arn:aws:emr-serverless:*:*:/applications/*/jobruns/*",
            "Condition": {
                "StringEquals": {
                    "aws:ResourceTag/sagemaker:is-canvas-resource": "True",
                    "aws:ResourceAccount": "${aws:PrincipalAccount}"
                }
            }
        },
        {
            "Sid": "EMRServerlessTagResourceOperation",
            "Effect": "Allow",
            "Action": "emr-serverless:TagResource",
            "Resource": "arn:aws:emr-serverless:*:*:/*",
            "Condition": {
                "StringEquals": {
                    "aws:RequestTag/sagemaker:is-canvas-resource": "True",
                    "aws:ResourceAccount": "${aws:PrincipalAccount}"
                }
            }
        },
        {
            "Sid": "IAMPassOperationForEMRServerless",
            "Effect": "Allow",
            "Action": "iam:PassRole",
            "Resource": "arn:aws:iam::*:role/EMRServerlessRuntimeRole-*",
            "Condition": {
                "StringEquals": {
                    "iam:PassedToService": "emr-serverless.amazonaws.com",
                    "aws:ResourceAccount": "${aws:PrincipalAccount}"
                }
            }
         }
    ]
}
```

------

## Migrate a CreateAutoMLJob to CreateAutoMLJobV2
<a name="autopilot-create-experiment-api-migrate-v1-v2"></a>

We recommend users of `CreateAutoMLJob` to migrate to `CreateAutoMLJobV2`.

This section explains the differences in the input parameters between [CreateAutoMLJob](https://docs.aws.amazon.com/sagemaker-api/src/AWSSageMakerAPIDoc/build/server-root/sagemaker/latest/APIReference/API_CreateAutoMLJob.html#API_CreateAutoMLJob_RequestSyntax) and [CreateAutoMLJobV2](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateAutoMLJobV2.html#API_CreateAutoMLJobV2_RequestSyntax) by highlighting the changes in the position, name, or structure of the objects and attributes of the input request between the two versions.
+ **Request attributes that did not change between versions.**

  ```
  {
     "AutoMLJobName": "string",
     "AutoMLJobObjective": { 
        "MetricName": "string"
     },
     "ModelDeployConfig": { 
        "AutoGenerateEndpointName": boolean,
        "EndpointName": "string"
     },
     "OutputDataConfig": { 
        "KmsKeyId": "string",
        "S3OutputPath": "string"
     },
     "RoleArn": "string",
     "Tags": [ 
        { 
           "Key": "string",
           "Value": "string"
        }
     ]
  }
  ```
+ **Request attributes that changed position and structure between versions.**

  The following attributes changed position: `DataSplitConfig`, `Security Config`, `CompletionCriteria`, `Mode`, `FeatureSpecificationS3Uri`, `SampleWeightAttributeName`, `TargetAttributeName`.

------
#### [ CreateAutoMLJob ]

  ```
  { 
      "AutoMLJobConfig": { 
          "Mode": "string",
          "CompletionCriteria": { 
              "MaxAutoMLJobRuntimeInSeconds": number,
              "MaxCandidates": number,
              "MaxRuntimePerTrainingJobInSeconds": number
          },
          "DataSplitConfig": { 
              "ValidationFraction": number
          },
          "SecurityConfig": { 
              "EnableInterContainerTrafficEncryption": boolean,
              "VolumeKmsKeyId": "string",
              "VpcConfig": { 
              "SecurityGroupIds": [ "string" ],
              "Subnets": [ "string" ]
              }
          },
          "CandidateGenerationConfig": { 
              "FeatureSpecificationS3Uri": "string"
          }
      },
      "GenerateCandidateDefinitionsOnly": boolean,
      "ProblemType": "string"
  }
  ```

------
#### [ CreateAutoMLJobV2 ]

  ```
  {       
      "AutoMLProblemTypeConfig": {
          "TabularJobConfig": {
              "Mode": "string",
              "ProblemType": "string",
              "GenerateCandidateDefinitionsOnly": boolean,
              "CompletionCriteria": { 
                  "MaxAutoMLJobRuntimeInSeconds": number,
                  "MaxCandidates": number,
                  "MaxRuntimePerTrainingJobInSeconds": number
              },
              "FeatureSpecificationS3Uri": "string",
              "SampleWeightAttributeName": "string",
              "TargetAttributeName": "string"
          }
      },
      "DataSplitConfig": { 
          "ValidationFraction": number
      },
      "SecurityConfig": { 
          "EnableInterContainerTrafficEncryption": boolean,
          "VolumeKmsKeyId": "string",
          "VpcConfig": { 
              "SecurityGroupIds": [ "string" ],
              "Subnets": [ "string" ]
          }
      }
  }
  ```

------
+ **The following attributes changed position and structure between versions.**

  The following JSON illustrates how [AutoMLJobConfig.CandidateGenerationConfig](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_AutoMLJobConfig.html#sagemaker-Type-AutoMLJobConfig-CandidateGenerationConfig) of type [AutoMLCandidateGenerationConfig](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_AutoMLCandidateGenerationConfig.html) moved to [AutoMLProblemTypeConfig.TabularJobConfig.CandidateGenerationConfig](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateAutoMLJobV2.html#API_CreateAutoMLJobV2_RequestSyntax) of type [CandidateGenerationConfig](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CandidateGenerationConfig.html) in V2.

------
#### [ CreateAutoMLJob ]

  ```
  {
     "AutoMLJobConfig": { 
        "CandidateGenerationConfig": { 
           "AlgorithmsConfig": [ 
              { 
                 "AutoMLAlgorithms": [ "string" ]
              }
           ],
           "FeatureSpecificationS3Uri": "string"
        }
  }
  ```

------
#### [ CreateAutoMLJobV2 ]

  ```
  {
      "AutoMLProblemTypeConfig": {
          "TabularJobConfig": {
              "CandidateGenerationConfig": { 
                  "AlgorithmsConfig": [ 
                      { 
                      "AutoMLAlgorithms": [ "string" ]
                      }
                  ],
              },
          }
      },
  }
  ```

------
+ **Request attributes that changed name and structure.**

  The following JSON illustrates how [InputDataConfig](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateAutoMLJob.html#sagemaker-CreateAutoMLJob-request-InputDataConfig) (An array of [AutoMLChannel](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_AutoMLChannel.html)) changed to [AutoMLJobInputDataConfig](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateAutoMLJobV2.html#sagemaker-CreateAutoMLJobV2-request-AutoMLJobInputDataConfig) (An array of [AutoMLJobChannel](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_AutoMLJobChannel.html)) in V2. Note that the attributes `SampleWeightAttributeName` and `TargetAttributeName` move out of `InputDataConfig` and into `AutoMLProblemTypeConfig`.

------
#### [ CreateAutoMLJob ]

  ```
  {    
      "InputDataConfig": [ 
          { 
              "ChannelType": "string",
              "CompressionType": "string",
              "ContentType": "string",
              "DataSource": { 
                  "S3DataSource": { 
                      "S3DataType": "string",
                      "S3Uri": "string"
                  }
              },
              "SampleWeightAttributeName": "string",
              "TargetAttributeName": "string"
          }
      ]
  }
  ```

------
#### [ CreateAutoMLJobV2 ]

  ```
  {    
      "AutoMLJobInputDataConfig": [ 
          { 
              "ChannelType": "string",
              "CompressionType": "string",
              "ContentType": "string",
              "DataSource": { 
                  "S3DataSource": { 
                      "S3DataType": "string",
                      "S3Uri": "string"
                  }
              }
          }
      ]
  }
  ```

------