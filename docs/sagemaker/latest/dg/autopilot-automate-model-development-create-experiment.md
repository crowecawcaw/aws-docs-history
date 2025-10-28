# Create Regression or

Classification Jobs for Tabular Data Using the AutoML API

You can create an Autopilot regression or classification job for tabular data programmatically
by calling the [`CreateAutoMLJobV2`](../APIReference/API_CreateAutoMLJobV2.md "../APIReference/API_CreateAutoMLJobV2.md") API action in any language supported by Autopilot or the
AWS CLI. The following is a collection of mandatory and optional input request parameters for the
`CreateAutoMLJobV2` API action. You can find the alternative information for the
previous version of this action, `CreateAutoMLJob`. However, we recommend using
`CreateAutoMLJobV2`.

For information on how this API action translates into a function in the language of your
choice, see the [See Also](../APIReference/API_CreateAutoMLJobV2.md#API_CreateAutoMLJobV2_SeeAlso "../APIReference/API_CreateAutoMLJobV2.md#API_CreateAutoMLJobV2_SeeAlso") section of `CreateAutoMLJobV2` and choose an SDK. As an example, for Python users, see the full request syntax of `create_auto_ml_job_v2` in AWS SDK for Python (Boto3).

###### Note

[CreateAutoMLJobV2](../APIReference/API_CreateAutoMLJobV2.md "../APIReference/API_CreateAutoMLJobV2.md")
and [DescribeAutoMLJobV2](../APIReference/API_DescribeAutoMLJobV2.md "../APIReference/API_DescribeAutoMLJobV2.md") are new versions of [CreateAutoMLJob](../APIReference/API_CreateAutoMLJob.md "../APIReference/API_CreateAutoMLJob.md") and
[DescribeAutoMLJob](../APIReference/API_DescribeAutoMLJob.md "../APIReference/API_DescribeAutoMLJob.md") which offer backward compatibility.

We recommend using the `CreateAutoMLJobV2`. `CreateAutoMLJobV2` can
manage tabular problem types identical to those of its previous version
`CreateAutoMLJob`, as well as non-tabular problem types such as image or text
classification, or time-series forecasting.

At a minimum, all experiments on tabular data require the specification of the experiment
name, providing locations for the input and output data, and specifying which target data to
predict. Optionally, you can also specify the type of problem that you want to solve
(regression, classification, multiclass classification), choose your modeling strategy
(_stacked ensembles_ or _hyperparameters optimization_), select the list of algorithms used by the Autopilot
job to train the data, and more.

After the experiment runs, you can compare trials and delve into the details of the
pre-processing steps, algorithms, and hyperparameter ranges of each model. You also have the
option to download their [explainability](autopilot-explainability.md "autopilot-explainability.md") and [performance](autopilot-model-insights.md "autopilot-model-insights.md") reports. Use the provided [notebooks](autopilot-automate-model-development-notebook-output.md "autopilot-automate-model-development-notebook-output.md") to see the results of the automated data exploration or the candidate model
definitions.

Find guidelines on how to migrate a `CreateAutoMLJob` to
`CreateAutoMLJobV2` in [Migrate a CreateAutoMLJob to
CreateAutoMLJobV2](#autopilot-create-experiment-api-migrate-v1-v2 "#autopilot-create-experiment-api-migrate-v1-v2").

## Required parameters

CreateAutoMLJobV2
When calling `CreateAutoMLJobV2` to create an Autopilot experiment for tabular data,
you must provide the following values:

- An `AutoMLJobName` to specify the name of your job.
- At least one `AutoMLJobChannel` in `AutoMLJobInputDataConfig` to specify your data source.
- Both an `AutoMLJobObjective` metric and your chosen type of supervised
  learning problem (binary classification, multiclass classification, regression) in
  `AutoMLProblemTypeConfig`, or none at all. For tabular data, you must
  choose `TabularJobConfig` as the type of `AutoMLProblemTypeConfig`. You set the supervised learning problem
  in the `ProblemType` attribute of `TabularJobConfig`.
- An `OutputDataConfig` to specify the Amazon S3 output path to store the
  artifacts of your AutoML job.
- A `RoleArn` to specify the ARN of the role used to access your
  data.

CreateAutoMLJob
When calling `CreateAutoMLJob` to create an AutoML experiment, you must provide the
following four values:

- An `AutoMLJobName` to specify the name of your job.
- At least one `AutoMLChannel` in `InputDataConfig` to specify your data source.
- An `OutputDataConfig` to specify the Amazon S3 output path to store the
  artifacts of your AutoML job.
- A `RoleArn` to specify the ARN of the role used to access your
  data.

All other parameters are optional.

## Optional parameters

The following sections provide details of some optional parameters that you can pass to
your `CreateAutoMLJobV2` API action when using tabular data. You can find the
alternative information for the previous version of this action, `CreateAutoMLJob`.
However, we recommend using `CreateAutoMLJobV2`.

For tabular data, the set of algorithms run on your data to train your model
candidates is dependent on your modeling strategy (`ENSEMBLING` or
`HYPERPARAMETER_TUNING`). The following details how to set this training
mode.

If you keep blank (or `null`), the `Mode` is inferred based on
the size of your dataset.

For information on Autopilot's _stacked ensembles_ and
_hyperparameters optimization_ training methods, see
[Training modes and algorithm
support](autopilot-model-support-validation.md "autopilot-model-support-validation.md")

CreateAutoMLJobV2
For tabular data, you must choose `TabularJobConfig` as the type of `AutoMLProblemTypeConfig`.

You can set the [training
method](autopilot-model-support-validation.md "autopilot-model-support-validation.md") of an AutoML job V2 with the `TabularJobConfig.Mode` parameter.

CreateAutoMLJob
You can set the [training
method](autopilot-model-support-validation.md "autopilot-model-support-validation.md") of an AutoML job with the `AutoMLJobConfig.Mode` parameter.

#### Features selection

Autopilot provides automatic data-preprocessing steps including feature selection and
feature extraction. However, you can manually provide the features to be used in
training with the `FeatureSpecificatioS3Uri` attribute.

Selected features should be contained within a JSON file in the following
format:

```
{ "FeatureAttributeNames":["col1", "col2", ...] }
```

The values listed in `["col1", "col2", ...]` are case sensitive. They
should be a list of strings containing unique values that are subsets of the column
names in the input data.

###### Note

The list of columns provided as features cannot include the target column.

CreateAutoMLJobV2
For tabular data, you must choose `TabularJobConfig` as the type of `AutoMLProblemTypeConfig`.

You can set the URL to your selected features with the `TabularJobConfig.FeatureSpecificationS3Uri` parameter.

CreateAutoMLJob
You can set the `FeatureSpecificatioS3Uri` attribute of [AutoMLCandidateGenerationConfig](../APIReference/API_AutoMLCandidateGenerationConfig.md "../APIReference/API_AutoMLCandidateGenerationConfig.md") within the [CreateAutoMLJob](../APIReference/API_CreateAutoMLJob.md "../APIReference/API_CreateAutoMLJob.md") API with the following format:

```
{
    "AutoMLJobConfig": {
        "CandidateGenerationConfig": {
            "FeatureSpecificationS3Uri":"string"
            },
       }
  }
```

#### Algorithms selection

By default, your Autopilot job runs a pre-defined list of algorithms on your dataset to
train model candidates. The list of algorithms depends on the training mode
(`ENSEMBLING` or `HYPERPARAMETER_TUNING`) used by the
job.

You can provide a subset of the default selection of algorithms.

CreateAutoMLJobV2
For tabular data, you must choose `TabularJobConfig` as the type of `AutoMLProblemTypeConfig`.

You can specify an array of selected `AutoMLAlgorithms` in the
`AlgorithmsConfig` attribute of [CandidateGenerationConfig](../APIReference/API_CandidateGenerationConfig.md "../APIReference/API_CandidateGenerationConfig.md").

The following is an example of an `AlgorithmsConfig` attribute
listing exactly three algorithms ("xgboost", "fastai", "catboost") in its
`AutoMLAlgorithms` field for the ensembling training mode.

```
{
   "AutoMLProblemTypeConfig": {
        "TabularJobConfig": {
          "Mode": "ENSEMBLING",
          "CandidateGenerationConfig": {
            "AlgorithmsConfig":[
               {"AutoMLAlgorithms":["xgboost", "fastai", "catboost"]}
            ]
         },
       },
     },
  }
```

CreateAutoMLJob
You can specify an array of selected `AutoMLAlgorithms` in the
`AlgorithmsConfig` attribute of [AutoMLCandidateGenerationConfig](../APIReference/API_AutoMLCandidateGenerationConfig.md "../APIReference/API_AutoMLCandidateGenerationConfig.md").

The following is an example of an `AlgorithmsConfig` attribute
listing exactly three algorithms ("xgboost", "fastai", "catboost") in its
`AutoMLAlgorithms` field for the ensembling training mode.

```
{
   "AutoMLJobConfig": {
        "CandidateGenerationConfig": {
            "AlgorithmsConfig":[
               {"AutoMLAlgorithms":["xgboost", "fastai", "catboost"]}
            ]
         },
     "Mode": "ENSEMBLING"
  }
```

For the list of available algorithms per training `Mode`, see [`AutoMLAlgorithms`](../APIReference/API_AutoMLAlgorithmConfig.md#sagemaker-Type-AutoMLAlgorithmConfig-AutoMLAlgorithms "../APIReference/API_AutoMLAlgorithmConfig.md#sagemaker-Type-AutoMLAlgorithmConfig-AutoMLAlgorithms"). For details on each algorithm, see [Training modes and algorithm
support](autopilot-model-support-validation.md "autopilot-model-support-validation.md").

You can provide your own validation dataset and custom data split ratio, or let Autopilot
split the dataset automatically.

CreateAutoMLJobV2
Each [`AutoMLJobChannel`](../APIReference/API_AutoMLJobChannel.md "../APIReference/API_AutoMLJobChannel.md") object (see the required parameter [AutoMLJobInputDataConfig](../../../sagemaker-api/src/AWSSageMakerAPIDoc/build/server-root/sagemaker/latest/APIReference/API_CreateAutoMLJobV2.md#sagemaker-CreateAutoMLJobV2-request-AutoMLJobInputDataConfig "../../../sagemaker-api/src/AWSSageMakerAPIDoc/build/server-root/sagemaker/latest/APIReference/API_CreateAutoMLJobV2.md#sagemaker-CreateAutoMLJobV2-request-AutoMLJobInputDataConfig")) has a `ChannelType`, which can be
set to either `training` or `validation` values that specify
how the data is to be used when building a machine learning model. At least one data
source must be provided and a maximum of two data sources is allowed: one for
training data and one for validation data.

How you split the data into training and validation datasets depends on
whether you have one or two data sources.

- If you only have **one data source**, the
  `ChannelType` is set to `training` by default and must
  have this value.
  - If the `ValidationFraction` value in [`AutoMLDataSplitConfig`](../APIReference/API_AutoMLDataSplitConfig.md "../APIReference/API_AutoMLDataSplitConfig.md") is not set, 0.2 (20%) of the
    data from this source is used for validation by default.
  - If the `ValidationFraction` is set to a value between 0 and
    1, the dataset is split based on the value specified, where the value
    specifies the fraction of the dataset used for validation.

- If you have **two data sources**, the
  `ChannelType` of one of the `AutoMLJobChannel` objects
  must be set to `training`, the default value. The
  `ChannelType` of the other data source must be set to
  `validation`. The two data sources must have the same format,
  either CSV or Parquet, and the same schema. You must not set the value for the
  `ValidationFraction` in this case because all of the data from each
  source is used for either training or validation. Setting this value causes an
  error.

CreateAutoMLJob
Each [`AutoMLChannel`](../APIReference/API_AutoMLChannel.md "../APIReference/API_AutoMLChannel.md") object (see the required parameter [InputDataConfig](../APIReference/API_CreateAutoMLJob.md#sagemaker-CreateAutoMLJob-request-InputDataConfig "../APIReference/API_CreateAutoMLJob.md#sagemaker-CreateAutoMLJob-request-InputDataConfig")) has a `ChannelType`, which can be set to
either `training` or `validation` values that specify how the
data is to be used when building a machine learning model. At least one data source
must be provided and a maximum of two data sources is allowed: one for training data
and one for validation data.

How you split the data into training and validation datasets depends on
whether you have one or two data sources.

- If you only have **one data source**, the
  `ChannelType` is set to `training` by default and must
  have this value.
  - If the `ValidationFraction` value in [`AutoMLDataSplitConfig`](../APIReference/API_AutoMLDataSplitConfig.md "../APIReference/API_AutoMLDataSplitConfig.md") is not set, 0.2 (20%) of the
    data from this source is used for validation by default.
  - If the `ValidationFraction` is set to a value between 0 and
    1, the dataset is split based on the value specified, where the value
    specifies the fraction of the dataset used for validation.

- If you have **two data sources**, the
  `ChannelType` of one of the `AutoMLChannel` objects must
  be set to `training`, the default value. The `ChannelType`
  of the other data source must be set to `validation`. The two data
  sources must have the same format, either CSV or Parquet, and the same schema.
  You must not set the value for the `ValidationFraction` in this case
  because all of the data from each source is used for either training or
  validation. Setting this value causes an error.

For information on split and cross-validation in Autopilot see [Cross-validation in Autopilot](autopilot-metrics-validation.md#autopilot-cross-validation "autopilot-metrics-validation.md#autopilot-cross-validation").

CreateAutoMLJobV2
For tabular data, you must choose `TabularJobConfig` as the type of `AutoMLProblemTypeConfig`.

You can further specify the type of supervised learning problem (binary
classification, multiclass classification, regression) available for the model
candidates of your AutoML job V2 with the `TabularJobConfig.ProblemType` parameter.

CreateAutoMLJob
You can set the [type of problem](autopilot-datasets-problem-types.md#autopilot-problem-types "autopilot-datasets-problem-types.md#autopilot-problem-types") on an AutoML job with the `CreateAutoPilot.ProblemType` parameter. This limits the kind of
preprocessing and algorithms that Autopilot tries. After the job is finished, if you
had set the `CreateAutoPilot.ProblemType`, then the `ResolvedAttribute.ProblemType` matches the
`ProblemType` you set. If you keep it blank (or `null`), the
`ProblemType` is inferred on your behalf.

###### Note

In some cases, Autopilot is unable to infer the `ProblemType` with high
enough confidence, in which case you must provide the value for the job to
succeed.

You can add a sample weights column to your tabular dataset and then pass it to your
AutoML job to request dataset rows to be weighted during training and evaluation.

Support for sample weights is available in [ensembling mode](autopilot-model-support-validation.md#autopilot-training-mode "autopilot-model-support-validation.md#autopilot-training-mode") only. Your weights should be numeric and non-negative. Data
points with invalid or no weight value are excluded. For more information on the available
objective metrics, see [Autopilot weighted metrics](autopilot-metrics-validation.md#autopilot-weighted-metrics "autopilot-metrics-validation.md#autopilot-weighted-metrics").

CreateAutoMLJobV2
For tabular data, you must choose `TabularJobConfig` as the type of `AutoMLProblemTypeConfig`.

To set sample weights when creating an experiment (see [CreateAutoMLJobV2](../APIReference/API_CreateAutoMLJobV2.md "../APIReference/API_CreateAutoMLJobV2.md")), you can pass the name of your sample weights column
in the `SampleWeightAttributeName` attribute of the
`TabularJobConfig` object. This ensures that your objective metric uses
the weights for the training, evaluation, and selection of model candidates.

CreateAutoMLJob
To set sample weights when creating an experiment (see [CreateAutoMLJob](../APIReference/API_CreateAutoMLJob.md "../APIReference/API_CreateAutoMLJob.md")), you can pass the name of your sample weights column in
the `SampleWeightAttributeName` attribute of the [AutoMLChannel](../APIReference/API_AutoMLChannel.md "../APIReference/API_AutoMLChannel.md") object. This ensures that your objective metric uses the
weights for the training, evaluation, and selection of model candidates.

You can configure your AutoML job V2 to automatically initiate a remote job on Amazon EMR
Serverless when additional compute resources are needed to process large datasets. By
seamlessly transitioning to EMR Serverless when required, the AutoML job can handle
datasets that would otherwise exceed the initially provisioned resources, without any
manual intervention from you. EMR Serverless is available for the tabular and time
series problem types. We recommend setting up this option for tabular datasets larger than
5 GB.

To allow your AutoML job V2 to automatically transition to EMR Serverless for large
dataset, you need to provide an `EmrServerlessComputeConfig` object, which
includes an `ExecutionRoleARN` field, to the `AutoMLComputeConfig`
of the AutoML job V2 input request.

The `ExecutionRoleARN` is the ARN of the IAM role granting the AutoML job
V2 the necessary permissions to run EMR Serverless jobs.

This role should have the following trust relationship:

JSON

```
`{
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
}`

```

And grant the permissions to:

- Create, list, and update EMR Serverless applications.
- Start, list, get, or cancel job runs on an EMR Serverless application.
- Tag EMR Serverless resources.
- Pass an IAM role to the EMR Serverless service for execution.

By granting the `iam:PassRole` permission, the AutoML job V2 can
temporarily assume the `EMRServerlessRuntimeRole-*` role and pass it to the
EMR Serverless service. These are the IAM roles used by the EMR Serverless job
execution environments to access other AWS services and resources needed during
runtime, such as Amazon S3 for data access, CloudWatch for logging, access to the AWS Glue Data
Catalog or other services based on your workload requirements.

See [Job runtime
roles for Amazon EMR Serverless](../../../emr/latest/EMR-Serverless-UserGuide/security-iam-runtime-role.md "../../../emr/latest/EMR-Serverless-UserGuide/security-iam-runtime-role.md") for details on this role
permissions.
The IAM policy defined in the provided JSON document grants those
permissions:

```
{
    "Version": "2012-10-17",
    "Statement": [{
+            "Sid": "EMRServerlessCreateApplicationOperation",
+            "Effect": "Allow",
+            "Action": "emr-serverless:CreateApplication",
+            "Resource": "arn:aws:emr-serverless:*:*:/*",
+            "Condition": {
+                "StringEquals": {
+                    "aws:RequestTag/sagemaker:is-canvas-resource": "True",
+                    "aws:ResourceAccount": "${aws:PrincipalAccount}"
+                }
+            }
+        },
+        {
+            "Sid": "EMRServerlessListApplicationOperation",
+            "Effect": "Allow",
+            "Action": "emr-serverless:ListApplications",
+            "Resource": "arn:aws:emr-serverless:*:*:/*",
+            "Condition": {
+                "StringEquals": {
+                    "aws:ResourceAccount": "${aws:PrincipalAccount}"
+                }
+            }
+        },
+        {
+            "Sid": "EMRServerlessApplicationOperations",
+            "Effect": "Allow",
+            "Action": [
+                "emr-serverless:UpdateApplication",
+                "emr-serverless:GetApplication"
+            ],
+            "Resource": "arn:aws:emr-serverless:*:*:/applications/*",
+            "Condition": {
+                "StringEquals": {
+                    "aws:ResourceTag/sagemaker:is-canvas-resource": "True",
+                    "aws:ResourceAccount": "${aws:PrincipalAccount}"
+                }
+            }
+        },
+        {
+            "Sid": "EMRServerlessStartJobRunOperation",
+            "Effect": "Allow",
+            "Action": "emr-serverless:StartJobRun",
+            "Resource": "arn:aws:emr-serverless:*:*:/applications/*",
+            "Condition": {
+                "StringEquals": {
+                    "aws:RequestTag/sagemaker:is-canvas-resource": "True",
+                    "aws:ResourceAccount": "${aws:PrincipalAccount}"
+                }
+            }
+        },
+        {
+            "Sid": "EMRServerlessListJobRunOperation",
+            "Effect": "Allow",
+            "Action": "emr-serverless:ListJobRuns",
+            "Resource": "arn:aws:emr-serverless:*:*:/applications/*",
+            "Condition": {
+                "StringEquals": {
+                    "aws:ResourceTag/sagemaker:is-canvas-resource": "True",
+                    "aws:ResourceAccount": "${aws:PrincipalAccount}"
+                }
+            }
+        },
+        {
+            "Sid": "EMRServerlessJobRunOperations",
+            "Effect": "Allow",
+            "Action": [
+                "emr-serverless:GetJobRun",
+                "emr-serverless:CancelJobRun"
+            ],
+            "Resource": "arn:aws:emr-serverless:*:*:/applications/*/jobruns/*",
+            "Condition": {
+                "StringEquals": {
+                    "aws:ResourceTag/sagemaker:is-canvas-resource": "True",
+                    "aws:ResourceAccount": "${aws:PrincipalAccount}"
+                }
+            }
+        },
+        {
+            "Sid": "EMRServerlessTagResourceOperation",
+            "Effect": "Allow",
+            "Action": "emr-serverless:TagResource",
+            "Resource": "arn:aws:emr-serverless:*:*:/*",
+            "Condition": {
+                "StringEquals": {
+                    "aws:RequestTag/sagemaker:is-canvas-resource": "True",
+                    "aws:ResourceAccount": "${aws:PrincipalAccount}"
+                }
+            }
+        },
+        {
+            "Sid": "IAMPassOperationForEMRServerless",
+            "Effect": "Allow",
+            "Action": "iam:PassRole",
+            "Resource": "arn:aws:iam::*:role/EMRServerlessRuntimeRole-*",
+            "Condition": {
+                "StringEquals": {
+                    "iam:PassedToService": "emr-serverless.amazonaws.com",
+                    "aws:ResourceAccount": "${aws:PrincipalAccount}"
+                }
+            }
         }
    ]
}
```

## Migrate a CreateAutoMLJob to

CreateAutoMLJobV2

We recommend users of `CreateAutoMLJob` to migrate to
`CreateAutoMLJobV2`.

This section explains the differences in the input parameters between [CreateAutoMLJob](../../../sagemaker-api/src/AWSSageMakerAPIDoc/build/server-root/sagemaker/latest/APIReference/API_CreateAutoMLJob.md#API_CreateAutoMLJob_RequestSyntax "../../../sagemaker-api/src/AWSSageMakerAPIDoc/build/server-root/sagemaker/latest/APIReference/API_CreateAutoMLJob.md#API_CreateAutoMLJob_RequestSyntax") and [CreateAutoMLJobV2](../APIReference/API_CreateAutoMLJobV2.md#API_CreateAutoMLJobV2_RequestSyntax "../APIReference/API_CreateAutoMLJobV2.md#API_CreateAutoMLJobV2_RequestSyntax") by highlighting the changes in the position, name, or structure
of the objects and attributes of the input request between the two versions.

- **Request attributes that did not change between
  versions.**

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

- **Request attributes that changed position and structure between
  versions.**

The following attributes changed position: `DataSplitConfig`,
`Security Config`, `CompletionCriteria`, `Mode`,
`FeatureSpecificationS3Uri`, `SampleWeightAttributeName`,
`TargetAttributeName`.

CreateAutoMLJob

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

CreateAutoMLJobV2

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

- **The following attributes changed position and structure
  between versions.**

The following JSON illustrates how [AutoMLJobConfig.CandidateGenerationConfig](../APIReference/API_AutoMLJobConfig.md#sagemaker-Type-AutoMLJobConfig-CandidateGenerationConfig "../APIReference/API_AutoMLJobConfig.md#sagemaker-Type-AutoMLJobConfig-CandidateGenerationConfig") of type [AutoMLCandidateGenerationConfig](../APIReference/API_AutoMLCandidateGenerationConfig.md "../APIReference/API_AutoMLCandidateGenerationConfig.md") moved to [AutoMLProblemTypeConfig.TabularJobConfig.CandidateGenerationConfig](../APIReference/API_CreateAutoMLJobV2.md#API_CreateAutoMLJobV2_RequestSyntax "../APIReference/API_CreateAutoMLJobV2.md#API_CreateAutoMLJobV2_RequestSyntax") of type
[CandidateGenerationConfig](../APIReference/API_CandidateGenerationConfig.md "../APIReference/API_CandidateGenerationConfig.md") in V2.

CreateAutoMLJob

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

CreateAutoMLJobV2

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

- **Request attributes that changed name and
  structure.**

The following JSON illustrates how [InputDataConfig](../APIReference/API_CreateAutoMLJob.md#sagemaker-CreateAutoMLJob-request-InputDataConfig "../APIReference/API_CreateAutoMLJob.md#sagemaker-CreateAutoMLJob-request-InputDataConfig") (An array of [AutoMLChannel](../APIReference/API_AutoMLChannel.md "../APIReference/API_AutoMLChannel.md"))
changed to [AutoMLJobInputDataConfig](../APIReference/API_CreateAutoMLJobV2.md#sagemaker-CreateAutoMLJobV2-request-AutoMLJobInputDataConfig "../APIReference/API_CreateAutoMLJobV2.md#sagemaker-CreateAutoMLJobV2-request-AutoMLJobInputDataConfig") (An array of [AutoMLJobChannel](../APIReference/API_AutoMLJobChannel.md "../APIReference/API_AutoMLJobChannel.md"))
in V2. Note that the attributes `SampleWeightAttributeName` and
`TargetAttributeName` move out of `InputDataConfig` and into
`AutoMLProblemTypeConfig`.

CreateAutoMLJob

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

CreateAutoMLJobV2

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
