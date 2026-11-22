

# Get started with SageMaker AI Data Preparation

Synthetic data generation, data quality evaluation, data transformation, and auto-labeling jobs use the same setup. Complete it once, and then go to the page for the capability that fits your situation. Human-in-the-loop annotation also needs a labeling space, which its page describes.

## Set up and prerequisites
<a name="ai-data-preparation-setup"></a>

Before you run a job, you need the following:
+ The Amazon SageMaker Python SDK, installed in your environment.
+ An execution role that the service can assume to run jobs.
+ A default Amazon S3 bucket for job output, in a supported AWS Region. For more information about supported Regions, see [Regions and limits for SageMaker AI Data Preparation](ai-data-preparation-regions-limits.md).
+ (Recommended) The core AI and ML skill from the Agent Toolkit for AWS, to run jobs through a coding assistant. To install it, see the [Agent Toolkit for AWS User Guide](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/).

### Install the SDK
<a name="ai-data-preparation-setup-install"></a>

SageMaker AI Data Preparation requires version 3.30.0 or later of the Amazon SageMaker Python SDK (`sagemaker` on PyPI), which requires Python 3.10 or later. Jobs are also submitted through `botocore`, which must be recent enough to include the data preparation APIs. To install or upgrade both, run the following command in the Python environment that you run jobs from:

```bash
python -m pip install -U 'sagemaker>=3.30.0,<4.0' boto3
```

To check the installed version, run the following command:

```bash
python -c "from importlib.metadata import version; print(version('sagemaker'))"
```

### Configure your environment
<a name="ai-data-preparation-setup-config"></a>

Jobs read their execution role and default Amazon S3 bucket from the SDK configuration file, so you don't pass them in every job. On Linux, including Studio, create `~/.config/sagemaker/config.yaml` with the following content:

```yaml
SageMaker:
  PythonSDK:
    Modules:
      DataPreparer:
        GlobalDefaults:
          RoleArn: arn:aws:iam::{{111122223333}}:role/{{SageMakerExecutionRole}}
      Session:
        DefaultS3Bucket: {{amzn-s3-demo-bucket}}
```

In this file, set the following values:
+ `RoleArn` – The ARN of the execution role. If you don't set it, the SDK uses `SageMaker.TrainingJob.RoleArn` from the same file, and then the IAM role of your current credentials, such as the Studio or notebook execution role.
+ `DefaultS3Bucket` – The bucket that jobs write output to when a job doesn't name an output location. The bucket must be in the same Region as your jobs. If you don't set it, the SDK uses `sagemaker-{{region}}-{{account-id}}`, and creates that bucket if it doesn't exist.

On Linux, the SDK also reads an administrator file at `/etc/xdg/sagemaker/config.yaml`. To use a different file, set the `SAGEMAKER_USER_CONFIG_OVERRIDE` environment variable, or `SAGEMAKER_ADMIN_CONFIG_OVERRIDE` for the administrator file, to its path. `Session()` loads the configuration automatically.

### Required permissions
<a name="ai-data-preparation-setup-iam"></a>

Jobs run by assuming the execution role in your account. The role needs a trust policy that lets the service assume it. It also needs a permissions policy that lets the job read your data, write its output, and register the output as a dataset. A gap in either policy can fail the job.

The trust policy must trust the SageMaker AI service principal, `sagemaker.amazonaws.com`:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "Service": "sagemaker.amazonaws.com"
      },
      "Action": ["sts:AssumeRole", "sts:SetSourceIdentity"]
    }
  ]
}
```

The following permissions policy grants what jobs need. Replace the bucket, Region, account ID, and hub name with your own:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": ["s3:GetObject", "s3:PutObject"],
      "Resource": "arn:aws:s3:::{{amzn-s3-demo-bucket}}/*"
    },
    {
      "Effect": "Allow",
      "Action": ["s3:ListBucket", "s3:GetBucketLocation"],
      "Resource": "arn:aws:s3:::{{amzn-s3-demo-bucket}}"
    },
    {
      "Effect": "Allow",
      "Action": "sagemaker:ImportHubContent",
      "Resource": [
        "arn:aws:sagemaker:{{us-east-1}}:{{111122223333}}:hub/{{my-hub}}",
        "arn:aws:sagemaker:{{us-east-1}}:{{111122223333}}:hub-content/{{my-hub}}/DataSet/*"
      ]
    },
    {
      "Effect": "Allow",
      "Action": ["bedrock:InvokeModel", "bedrock:InvokeModelWithResponseStream"],
      "Resource": "*"
    }
  ]
}
```

Each grant is for the following:

`s3:GetObject`, `s3:PutObject`, and `s3:ListBucket`  
Read input data and write job output. The object actions apply to the bucket ARN with the `/*` suffix.

`s3:GetBucketLocation`  
Find the Region of the bucket. Without it, a job can run and then fail when it validates its output.

`sagemaker:ImportHubContent`  
Register the output as a dataset in your hub. The action is `ImportHubContent`, not `CreateHubContent`, and it needs both the hub ARN and the `hub-content/{{hub-name}}/DataSet/*` ARN. For a job that transforms an existing dataset, this is the hub that holds the input dataset. Without this grant, the job still writes the output records to Amazon S3, but it can't register them as a dataset.

`bedrock:InvokeModel` and `bedrock:InvokeModelWithResponseStream`  
Invoke Amazon Bedrock models. Synthetic data generation and data quality evaluation jobs always invoke a model. Data transformation jobs need these permissions only when they use an operator that invokes a model.

Human-in-the-loop annotation uses its own permissions for the labeling space. For more information about those permissions, see [Human-in-the-loop annotation](ai-data-preparation-hil.md).

### Discover configurable fields
<a name="ai-data-preparation-setup-discovery"></a>

Each job is configured with a `DatasetJobConfig`. To list every field that a job type accepts, run `print_schema()` with its job category. The schema comes from the service, so it lists the fields that the service currently accepts:

```python
from sagemaker.ai_registry import DatasetJobConfig, JobCategory

DatasetJobConfig.print_schema(JobCategory.SYNTHETIC_DATA_GENERATION)
DatasetJobConfig.print_schema(JobCategory.DATA_QUALITY_EVALUATION)
DatasetJobConfig.print_schema(JobCategory.DATA_TRANSFORMATION)
```

To start from a configuration with the required fields marked, use `from_template()`. Required top-level fields that you still need to set show as `<SET_ME>`:

```python
config = DatasetJobConfig.from_template(JobCategory.SYNTHETIC_DATA_GENERATION)
print(config)
```

## Choose where to start
<a name="ai-data-preparation-start-choose"></a>

Start with the capability that matches your situation. Each page describes the inputs that the capability needs, including any specification that you write for it.


| Your situation | Start with | 
| --- | --- | 
| You have no data, or not enough, for the model that you want to train, evaluate, or test. | [Synthetic data generation](ai-data-preparation-sdg.md) | 
| You have a dataset and want to know whether its quality is good enough to use. | [Data quality evaluation](ai-data-preparation-dq.md) | 
| You want to remove duplicates, filter or redact records, split or merge datasets, or convert records to another format. | [Data transformation](ai-data-preparation-dt.md) | 
| Your records don't have labels yet. | [Auto-labeling](ai-data-preparation-autolabel.md) | 
| You want people to review or correct labels. | [Human-in-the-loop annotation](ai-data-preparation-hil.md) | 

The capabilities connect through datasets. A job that produces data registers it as a dataset in your hub and returns its ARN. You pass that ARN as the input to the next job. For example, you can generate records with synthetic data generation, check them with data quality evaluation, and then split them into training and test sets with data transformation. For more information about datasets, see [Datasets and hub content](ai-data-preparation.md#ai-data-preparation-concepts-datasets).