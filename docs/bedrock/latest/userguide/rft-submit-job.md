# Create a reinforcement fine-tuning job

You can create a reinforcement fine-tuning job using the Amazon Bedrock console or API. The RFT job can take several
hours depending on the size of your training data, number of epochs, and complexity of your reward functions.

###### Topics

- [Prerequisites](#rft-prerequisites "#rft-prerequisites")
- [Create your RFT job](#rft-submit-job-how-to "#rft-submit-job-how-to")
- [RFT job workflow](#rft-job-workflow "#rft-job-workflow")
- [Set up inference](#rft-setup-inference "#rft-setup-inference")
- [Monitor your RFT training job](rft-monitor-job.md "rft-monitor-job.md")
- [Evaluate your RFT model](rft-evaluate-model.md "rft-evaluate-model.md")

## Prerequisites

- Create an IAM service role to access the Amazon S3 bucket where you want to store your RFT training
  data and output artifacts. You can create this role automatically using the AWS Management Console or manually.
  For RFT-specific permissions, see [Reinforcement fine-tuning access and security](rft-access-security.md "rft-access-security.md").
- (Optional) Encrypt input and output data, your RFT job, or inference requests made to custom models.
  For more information, see [Encryption of custom models](encryption-custom-job.md "encryption-custom-job.md").

## Create your RFT job

Choose the tab for your preferred method, and then follow the steps:

Console
To submit an RFT job in the console, carry out the following steps:

1. Sign in to the AWS Management Console and open the Amazon Bedrock console at [https://console.aws.amazon.com/bedrock](https://console.aws.amazon.com/bedrock "https://console.aws.amazon.com/bedrock").
2. From the left navigation pane, choose **Custom models** under **Tune**.
3. In the Models table, choose **Create**. Then, choose **Create reinforcement
   fine-tuning job**.
4. In the **Model details** section, choose **Amazon Nova 2 Lite** as your base model.
5. In the **Customization details** section, enter the customization name.
6. In the **Training data** section, choose your data source:
   - **Use stored invocation logs** - Select from your available invocation
     logs stored in Amazon S3
   - **Upload new dataset** - Select the Amazon S3 location of your training
     dataset file or upload a file directly from your device

###### Note

Your training dataset should be in the OpenAI Chat Completions data format. If you provide
invocation logs in the Amazon Bedrock invoke or converse format, Amazon Bedrock automatically converts them to
the Chat Completions format. 7. In the **Reward function** section, set up your reward mechanism:

    * **Model as judge (RLAIF)** - Select a Bedrock hosted base model as judge
     and configure the instructions for evaluation. Use this for subjective tasks like content
     moderation.


    ###### Note

    The console's **Model as judge** option automatically converts your configuration into a Lambda
     function during training.
    * **Custom code (RLVR)** - Create custom reward functions using Python
     code executed through Lambda functions. Use this for objective tasks like code generation.

For more information, see [Setting up reward functions](reward-functions.md "reward-functions.md"). 8. (Optional) In the **Hyperparameters** section, adjust training parameters or use
default values. 9. In the **Output data** section, enter the Amazon S3 location where Bedrock should save
job outputs. 10. In the **Role configuration** section, select:

    * **Choose an existing role** - Select from dropdown list
    * **Create a role** - Enter a name for the service role

11. (Optional) In the **Additional configuration** section, configure:
    - Validation data by pointing to an Amazon S3 bucket
    - KMS encryption settings
    - Job and model tags

12. Choose **Create reinforcement fine-tuning job** to begin the job.

API
Send a CreateModelCustomizationJob request with `customizationType` set to `REINFORCEMENT_FINE_TUNING`.
You must provide the following fields:

**Required fields:**

- `roleArn` - ARN of the service role with RFT permissions
- `baseModelIdentifier` - Model ID or ARN of the foundation model to customize
- `customModelName` - Name for the newly customized model
- `jobName` - Name for the training job
- `customizationType` - Set to `REINFORCEMENT_FINE_TUNING`
- `trainingDataConfig` - Amazon S3 URI of training dataset or invocation log configuration
- `outputDataConfig` - Amazon S3 URI to write output data
- `rftConfig` - Reward function configuration (RLVR or RLAIF) and hyper paramerters configuration

**Example request:**

```
{
    "roleArn": "arn:aws:iam::`123456789012`:role/`BedrockRFTRole`",
    "baseModelIdentifier": "amazon.nova-2.0",
    "customModelName": "`my-rft-model`",
    "jobName": "`my-rft-job`",
    "customizationType": "REINFORCEMENT_FINE_TUNING",
    "trainingDataConfig": {
        "s3Uri": "s3://`my-bucket`/`training-data.jsonl`"
    },
    "customizationConfig": {
        "rftConfig" : {
            "graderConfig": {
                "lambdaGrader": {
                    "lambdaArn": "arn:aws:lambda:`us-east-1`:`123456789012`:function:`function-name`"
                }
            },
            "hyperParameters": {
                "batchSize": 64,
                "epochCount": 2,
                "evalInterval": 10,
                "inferenceMaxTokens": 8192,
                "learningRate": 0.00001,
                "maxPromptLength": 4096,
                "reasoningEffort": "high",
                "trainingSamplePerPrompt": 4
            }
        }
    },
    "outputDataConfig": {
        "s3Uri": "s3://`my-bucket`/`rft-output/`"
    }
}
```

**Python API sample request:**

```
import boto3

bedrock = boto3.client(service_name='bedrock')

# Set parameters
customizationType = "REINFORCEMENT_FINE_TUNING"
baseModelIdentifier = "arn:aws:bedrock:us-east-1::foundation-model/amazon.nova-2-lite-v1:0:256k"
roleArn = "${your-customization-role-arn}"
jobName = "MyFineTuningJob"
customModelName = "MyCustomModel"

customizationConfig = {
    'rftConfig' : {
        'graderConfig': {
            'lambdaGrader': {
                'lambdaArn': 'arn:aws:lambda:us-east-1:123456789012:function:function-name'
            }
        },
        'hyperParameters': {
            'batchSize': 64,
            'epochCount': 2,
            'evalInterval': 10,
            'inferenceMaxTokens': 8192,
            'learningRate':0.00001,
            'maxPromptLength': 4096,
            'reasoningEffort': 'high',
            'trainingSamplePerPrompt':4
        }
    }
}

trainingDataConfig = {"s3Uri": "s3://${training-bucket}/myInputData/train.jsonl"}
outputDataConfig = {"s3Uri": "s3://${output-bucket}/myOutputData"}

# Create job
response_ft = bedrock.create_model_customization_job(
    jobName=jobName,
    customModelName=customModelName,
    roleArn=roleArn,
    baseModelIdentifier=baseModelIdentifier,
    customizationConfig=customizationConfig,
    trainingDataConfig=trainingDataConfig,
    outputDataConfig=outputDataConfig,
    customizationType=customizationType
)

jobArn = response_ft['jobArn']
```

## RFT job workflow

The RFT job follows this automated workflow:

1. **Response Generation** - The actor model generates responses from training prompts
2. **Reward Computation** - Reward functions evaluate prompt-response pairs
3. **Actor Model Training** - Model learns from scored pairs using GRPO

During training, you can monitor progress using real-time graphs with training and validation metrics such as loss, rewards,
reward margin, and accuracy. Once successful, an RFT model is created with a custom model ARN.

## Set up inference

After job completion, you can deploy the resulting RFT model with one click for on-demand inference. You can also use
Provisioned Throughput for mission-critical workloads that require consistent performance. Once inference is set up, use
**Test in Playground** to interactively evaluate and compare responses side-by-side with the base model.

For monitoring your RFT job progress, see [Monitor your RFT training job](rft-monitor-job.md "rft-monitor-job.md").

For evaluating your completed RFT model, see [Evaluate your RFT model](rft-evaluate-model.md "rft-evaluate-model.md").
