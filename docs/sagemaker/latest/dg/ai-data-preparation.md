

# Preparing Data with SageMaker AI Data Preparation

Customizing or evaluating a model starts with data that fits the task. That data is often missing, too small, unlabeled, or of unknown quality. SageMaker AI Data Preparation is a set of data preparation capabilities that close those gaps. Synthetic data generation, data quality evaluation, data transformation, and auto-labeling run as jobs that SageMaker AI manages. Jobs that produce data register it as a dataset in your account, ready for the next step or for model training. Human-in-the-loop annotation runs in a labeling space where people review and correct labels.

## The data preparation journey
<a name="ai-data-preparation-journey"></a>

The capabilities are stages on one path from no data, or raw data, to a dataset that is ready for training. Stages connect through datasets: you pass a dataset to the next stage by its ARN. You can start at any stage and stop when the data is ready. For example, you can generate records, check their quality, and then split them into training and test sets.
+ [Synthetic data generation](ai-data-preparation-sdg.md) – Generate records from a dataset specification when you have no data or not enough.
+ [Data quality evaluation](ai-data-preparation-dq.md) – Score a dataset against quality criteria before you train on it.
+ [Data transformation](ai-data-preparation-dt.md) – Remove duplicates, filter or redact records, split or merge datasets, and convert formats.
+ [Auto-labeling](ai-data-preparation-autolabel.md) – Label records with models, and flag the labels that need human review.
+ [Human-in-the-loop annotation](ai-data-preparation-hil.md) – Have people review and correct labels, in chat or in a Label Studio labeling space.

## Ways to use data preparation capabilities
<a name="ai-data-preparation-ways-to-use"></a>

You can run synthetic data generation, data quality evaluation, data transformation, and auto-labeling in two ways. Both submit the same jobs and produce the same datasets, so you can switch between them, or use both in one project. Human-in-the-loop annotation runs through a coding assistant.

### Amazon SageMaker Python SDK
<a name="ai-data-preparation-ways-sdk"></a>

Use the SDK when you want to script jobs, run them from a notebook or a pipeline, or control each configuration field. The `DataPreparer` class runs the jobs: `generate()` for synthetic data generation and auto-labeling, `evaluate()` for data quality evaluation, and `transform()` for data transformation. You need version 3.30.0 or later. To install it and configure your environment, see [Get started with SageMaker AI Data Preparation](ai-data-preparation-getting-started.md).

### Coding assistant with the AI and ML skill
<a name="ai-data-preparation-ways-skills"></a>

Use a coding assistant when you want to describe what you need in plain language and be guided through it. The assistant is directed by the core AI and ML skill (`aws-ai-ml`) in the Agent Toolkit for AWS. It drafts specifications with you. It checks your environment and offers to upgrade the SDK when a step needs a newer version. It asks for your approval before it runs a job or creates resources. It also saves job runs as a notebook or script that you can rerun. To install the skill, see the [Agent Toolkit for AWS User Guide](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/). You still need the execution role and default Amazon S3 bucket described in [Set up and prerequisites](ai-data-preparation-getting-started.md#ai-data-preparation-setup).

## Key concepts
<a name="ai-data-preparation-concepts"></a>

Every capability shares the following concepts.

### Datasets and hub content
<a name="ai-data-preparation-concepts-datasets"></a>

A job's output is a **dataset**. SageMaker AI writes the records to Amazon S3 and registers them as hub content of type `DataSet` in a hub in your account. In the SDK, a completed job returns a `DataSet` object. Its `arn` identifies the dataset when you pass it to another job, and its `source` is the Amazon S3 location of the records. A dataset ARN has the following format:

```
arn:aws:sagemaker:{{region}}:{{account-id}}:hub-content/{{hub-name}}/DataSet/{{dataset-name}}/{{version}}
```

Jobs that start from an existing dataset take its ARN as input. Data transformation publishes its output in the same hub as the input, usually as a new version of the input dataset. Data quality evaluation scores the dataset that you give it and writes the results to Amazon S3, rather than registering a new dataset. To use data that you already have, upload it to Amazon S3 and register it as a dataset with `DataSet.create()`. If you name a format other than `Custom` in `dataset_file_format`, also pass `validation_role_arn`, the IAM role that SageMaker AI uses to validate the records against that format. `Custom` skips format validation and needs no role. For the properties that SageMaker AI records for a dataset, see [DataSet properties](hub-content-document-dataset-properties.md). For more information about registering data, see [Inputs](ai-data-preparation-dt.md#ai-data-preparation-dt-inputs) in [Data transformation](ai-data-preparation-dt.md).

### Job configuration and schema discovery
<a name="ai-data-preparation-concepts-jobconfig"></a>

You configure a job with a `DatasetJobConfig` and a `JobCategory`, such as `SYNTHETIC_DATA_GENERATION`. The fields come from a schema that the SDK gets from the service. Values that you don't set come from your SDK configuration file, such as the execution role and default Amazon S3 bucket, and the service applies its own defaults to the fields that remain unset.

Before it submits a job, the SDK checks that required fields are present and that values have the right types and structure. The service checks value limits, such as patterns, lengths, and numeric ranges. When a value is outside a limit, the job fails, and its `FailureReason` explains why. To list the fields for a job type, see [Discover configurable fields](ai-data-preparation-getting-started.md#ai-data-preparation-setup-discovery).