

# Training job submission
<a name="model-customize-mtrl-job"></a>

## Launching Training Jobs
<a name="model-customize-mtrl-job-launching"></a>

After your agent is deployed and your dataset is in S3, create a training job using one of the following methods.

### SageMaker AI Studio
<a name="model-customize-mtrl-job-studio-ui"></a>
+ Navigate to Models in the navigation pane and select JumpStart Base Models.
+ Select a model that supports multi-turn RL (see the supported models table) and choose Customize model, then Customize with UI.
+ Select Multi-Turn Reinforcement Learning as the customization technique.
+ Configure your agent environment — select your Bedrock AgentCore runtime or provide your Lambda forwarder ARN.
+ Provide your training dataset as an S3 URI or registered dataset.
+ Adjust hyperparameters as needed.
+ Review your configuration and choose Submit.

### SageMaker AI Python SDK
<a name="model-customize-mtrl-job-sdk"></a>

**Discover supported models**

```
from sagemaker.train.multi_turn_rl_trainer import MultiTurnRLTrainer

supported_models = MultiTurnRLTrainer.list_supported_models()
print(f"Supported MTRL models ({len(supported_models)}):")
for m in supported_models:
    print(f"  - {m}")
```

**Set up your agent environment**

Option 1: Bedrock AgentCore runtime

```
# List available runtimes
runtimes = MultiTurnRLTrainer.list_bedrock_agentcore_runtimes()
for rt in runtimes:
    print(f"  - {rt['name']} ({rt['status']}) → {rt['arn']}")
```

Option 2: Custom Lambda agent

```
from sagemaker.train.agent_lambda import AgentLambda

# Create from inline code
adapter = AgentLambda.create(
    source='''
import json
def handler(event, context):
    prompt = event.get("prompt", "")
    return {"statusCode": 200, "body": json.dumps({"status": "ok", "agentResponse": prompt})}
''',
    role="arn:aws:iam::123456789012:role/AgentLambdaRole",
)

# Create from a local file
adapter = AgentLambda.create(
    source="~/my_agent_handler.py",
    role="arn:aws:iam::123456789012:role/AgentLambdaRole",
)

# Create from S3
adapter = AgentLambda.create(
    source="s3://my-bucket/agent_handler.py",
    role="arn:aws:iam::123456789012:role/AgentLambdaRole",
)

# Wrap an existing Lambda
adapter = AgentLambda.get("arn:aws:lambda:us-west-2:123456789012:function:my-agent")
```

**Register your dataset (optional)**

```
from sagemaker.ai_registry.dataset import DataSet

dataset = DataSet.create(
    name="my-mtrl-dataset",
    source="s3://my-bucket/prompts/training_prompts.parquet"
)
print(f"Dataset ARN: {dataset.arn}")
```

**Create Restricted Model Package Group for Nova (optional)**

If you are choosing Nova model (`nova-textgeneration-lite-v2`), then optionally create Restricted Model Package Group prior to submitting a training job (next step). If you skip this step, the SDK automatically creates one for you.

Restricted Model Package Group (RMPG) is a Model Package Group with ManagedStorageType: Restricted. It's required for closed-source models like Nova where the model weights are managed by AWS and not directly accessible to the customer.

The RFT job schema requires two separate Restricted MPGs:
+ Output MPG — stores the final fine-tuned model package
+ Intermediate Checkpoint MPG — reserved for intermediate training checkpoints (must differ from the Output MPG)

```
from sagemaker.core.resources import Job, ModelPackageGroup
from sagemaker.core.shapes import ManagedConfiguration

model_name = "nova-textgeneration-lite-v2"

# Restricted configuration
managed_config = ManagedConfiguration(managed_storage_type="Restricted")

# Output Model package group
output_mpg_name = f"{model_name}-mtrl-output-mpg"
create_kwargs = {
    "model_package_group_name": output_mpg_name,
    "region": "us-east-1",
    "managed_configuration": managed_config
}
output_mpg = ModelPackageGroup.create(**create_kwargs)

# Intermediate Model package group
intermediate_mpg_name = f"{model_name}-mtrl-inter-mpg"
create_kwargs = {
    "model_package_group_name": intermediate_mpg_name,
    "region": "us-east-1",
    "managed_configuration": managed_config
}
intermediate_mpg = ModelPackageGroup.create(**create_kwargs)
```

Once the Model package group is created, pass the groups in the next step when submitting a training job.

**Submit a training job with Bedrock AgentCore**

```
from sagemaker.train.multi_turn_rl_trainer import MultiTurnRLTrainer

trainer = MultiTurnRLTrainer(
    model="openai-reasoning-gpt-oss-20b",
    agent_env="arn:aws:bedrock-agentcore:us-west-2:123456789012:runtime/my-agent-runtime",
    training_dataset="s3://my-bucket/prompts/prompts.parquet",
    mlflow_app_arn="arn:aws:sagemaker:us-west-2:123456789012:mlflow-app/mlflow-app-id",
    s3_output_path="s3://my-bucket/output/",
    role="arn:aws:iam::123456789012:role/SageMakerRole",
    accept_eula=True,
)

# View and adjust hyperparameters
trainer.hyperparameters.get_info()
trainer.hyperparameters.max_epochs = 1
trainer.hyperparameters.global_batch_size = 32
trainer.hyperparameters.max_steps = 12

job = trainer.train(wait=True)
print(f"Job: {job.job_name}")
print(f"Status: {job.job_status}")
print(f"Output Model Package: {job.output_model_package_arn}")
```

**Submit a training job with a custom Lambda agent**

```
trainer = MultiTurnRLTrainer(
    model="openai-reasoning-gpt-oss-20b",
    agent_env=adapter,  # AgentLambda object or Lambda ARN string
    training_dataset="s3://my-bucket/prompts/prompts.parquet",
    mlflow_app_arn="arn:aws:sagemaker:us-west-2:123456789012:mlflow-app/mlflow-app-id",
    s3_output_path="s3://my-bucket/output/",
    role="arn:aws:iam::123456789012:role/SageMakerRole",
    accept_eula=True,
)

trainer.hyperparameters.max_epochs = 1
trainer.hyperparameters.global_batch_size = 32
trainer.hyperparameters.max_steps = 12

job = trainer.train(wait=True)
print(f"Job: {job.job_name}")
print(f"Status: {job.job_status}")
print(f"Output Model Package: {job.output_model_package_arn}")
```

**Submit a training job with Restricted Model package group for Nova**

Refer to the step above (Create Restricted Model Package Group for Nova) on how to create a Restricted Model Package group.

```
from sagemaker.train.multi_turn_rl_trainer import MultiTurnRLTrainer

trainer = MultiTurnRLTrainer(
    model="nova-textgeneration-lite-v2",
    agent_env="arn:aws:bedrock-agentcore:us-west-2:123456789012:runtime/my-agent-runtime",
    training_dataset="s3://my-bucket/prompts/prompts.parquet",
    mlflow_app_arn="arn:aws:sagemaker:us-west-2:123456789012:mlflow-app/mlflow-app-id",
    s3_output_path="s3://my-bucket/output/",
    role="arn:aws:iam::123456789012:role/SageMakerRole",
    accept_eula=True,
    output_model_package_group=output_mpg,
    intermediate_checkpoint_model_package_group=intermediate_mpg
)

# View and adjust hyperparameters
trainer.hyperparameters.get_info()
trainer.hyperparameters.max_epochs = 1
trainer.hyperparameters.global_batch_size = 32
trainer.hyperparameters.max_steps = 12

job = trainer.train(wait=True)
print(f"Job: {job.job_name}")
print(f"Status: {job.job_status}")
print(f"Output Model Package: {job.output_model_package_arn}")
```

### AWS CLI
<a name="model-customize-mtrl-job-cli"></a>

Create a training job using the `CreateJob` API. You specify the agent configuration, training data location, base model, and output settings in the `JobConfigDocument`.

To retrieve the full JobConfigDocument schema:

```
aws sagemaker list-job-schema-versions --job-category AgentRFT
aws sagemaker describe-job-schema-version --job-category AgentRFT --version "1.0.0"
```

**Create job with Bedrock AgentCore**

```
aws sagemaker create-job \
  --job-category AgentRFT \
  --job-name "my-agent-rft-job" \
  --role-arn "arn:aws:iam::123456789012:role/SageMakerFineTuningJobRole" \
  --job-config-schema-version "1.0.0" \
  --job-config-document '{
    "AgentConfig": {
      "BedrockAgentCoreConfig": {
        "AgentRuntimeArn": "arn:aws:bedrock-agentcore:us-west-2:123456789012:runtime/my-agent"
      }
    },
    "InputDataConfig": [...],
    "OutputDataConfig": {...},
    "ModelPackageConfig": {...},
    "TrainingConfig": {...}
  }' \
  --region us-west-2
```

**Create job with custom Lambda agent**

```
aws sagemaker create-job \
  --job-category AgentRFT \
  --job-name "my-custom-agent-rft-job" \
  --role-arn "arn:aws:iam::account-id:role/SageMakerFineTuningJobRole" \
  --job-config-schema-version "1.0.0" \
  --job-config-document '{
    "AgentConfig": {
      "CustomAgentLambdaConfig": {
        "LambdaArn": "arn:aws:lambda:us-west-2:account-id:function:rft-agent-forwarder"
      }
    },
    "InputDataConfig": [...],
    "OutputDataConfig": {...},
    "ModelPackageConfig": {...},
    "TrainingConfig": {...}
  }' \
  --region us-west-2
```

### boto3
<a name="model-customize-mtrl-job-boto3"></a>

**Create job with Bedrock AgentCore**

```
import json
import boto3

sm = boto3.client("sagemaker")

response = sm.create_job(
    JobName="my-agent-rft-job",
    RoleArn="arn:aws:iam::123456789012:role/SageMakerFineTuningJobRole",
    JobCategory="AgentRFT",
    JobConfigSchemaVersion="1.0.0",
    JobConfigDocument=json.dumps({
        "AgentConfig": {
            "BedrockAgentCoreConfig": {
                "AgentRuntimeArn": "arn:aws:bedrock-agentcore:us-west-2:123456789012:runtime/my-agent"
            }
        },
        "InputDataConfig": [...],
        "OutputDataConfig": {...},
        "ModelPackageConfig": {...},
        "TrainingConfig": {...}
    })
)

print(f"Job ARN: {response['JobArn']}")
```

**Create job with custom Lambda agent**

```
import json
import boto3

sm = boto3.client("sagemaker")

response = sm.create_job(
    JobName="my-custom-agent-rft-job",
    RoleArn="arn:aws:iam::account-id:role/SageMakerFineTuningJobRole",
    JobCategory="AgentRFT",
    JobConfigSchemaVersion="1.0.0",
    JobConfigDocument=json.dumps({
        "AgentConfig": {
            "CustomAgentLambdaConfig": {
                "LambdaArn": "arn:aws:lambda:us-west-2:account-id:function:rft-agent-forwarder"
            }
        },
        "InputDataConfig": [...],
        "OutputDataConfig": {...},
        "ModelPackageConfig": {...},
        "TrainingConfig": {...}
    })
)

print(f"Job ARN: {response['JobArn']}")
```

## Monitoring Training
<a name="model-customize-mtrl-job-monitoring"></a>

### Monitor your Training Job
<a name="model-customize-mtrl-job-monitor-status"></a>

Use the `DescribeJob` API to check your job's current status at any time. The job status transitions through `InProgress`, and then to `Completed`, `Failed` or `Stopped`.

```
aws sagemaker describe-job \
  --job-name "my-agent-rft-job" \
  --job-category AgentRFT \
  --region us-west-2
```

Use the SDK:

```
# Run without blocking
job = trainer.train(wait=False)
job.wait(poll=5, timeout=3000, max_log_lines=10)
# Check status
job.refresh()
print(f"Status: {job.job_status}")
print(f"Secondary Status: {job.secondary_status}")
print(f"Output Model Package: {job.output_model_package_arn}")
print(f"MLflow Details: {job.mlflow_details}")
print(f"Billable Tokens: {job.billable_token_usage}")
# Open MLflow tracking URL
job.get_mlflow_url()
# Stop a running job
job.stop()
# Attach to an existing job from a different session
existing_job = MultiTurnRLTrainer.attach(job_name="my-existing-job-name")
print(f"Status: {existing_job.job_status}")
print(f"Output Model: {existing_job.output_model_package_arn}")
# List all completed jobs
from sagemaker.train.agent_rft_job import AgentRFTJob
for j in AgentRFTJob.get_all(status_equals="Completed"):
    print(f"{j.job_name}: {j.job_status}")
```

### Monitor Training in MLflow
<a name="model-customize-mtrl-job-monitor-mlflow"></a>

SageMaker AI automatically integrates with managed MLflow to track your training job's progress, metrics, and artifacts. To enable MLflow tracking, include an `MlflowConfig` in your job's `OutputDataConfig`:

```
"OutputDataConfig": {
    "S3OutputPath": "s3://your-bucket/output/",
    "MlflowConfig": {
        "MlflowResourceArn": "arn:aws:sagemaker:us-west-2:123456789012:mlflow-app/my-rft-mlflow-app"
    }
}
```

**Prerequisites**
+ Create a managed MLflow App in your account. For setup instructions, see MLflow App Setup.
+ Ensure your SageMaker AI execution role has permissions to write to the MLflow App (`sagemaker-mlflow:*` actions).
+ Include the `MlflowResourceArn` in your job configuration.

**What gets logged**


| \# | Category | What's logged | Where in MLflow UI | 
| --- | --- | --- | --- | 
| 1 | Training metrics | Per-step counters, throughput, datum and token accounting, all-clock duration of each phase of a step, trajectory-reward summary rollout batch, and turn-count distribution per trajectory | Metrics tab (time-series charts) | 
| 2 | Trajectory traces | Full multi-turn conversations with tool calls and rewards | Traces tab | 

#### Detailed training metrics reference
<a name="model-customize-mtrl-job-metrics-detail"></a>

The following metrics are logged at each training step.

**Step counters and throughput (`training/`)**


| Metric | Description | 
| --- | --- | 
| training/epoch | Current epoch number | 
| training/global\_step | Global training step counter | 
| training/num\_groups | Trajectory groups in this step | 
| training/num\_trajectories | Total trajectories processed in this step | 
| training/total\_tokens | Tokens summed across all micro-batches in this step | 
| training/num\_datums | Training datums formed from trajectories | 
| training/datums\_per\_trajectory | Average datums emitted per trajectory | 
| training/action\_tokens\_mean | Mean action (response) tokens per trajectory | 
| training/obs\_tokens\_mean | Mean observation (prompt) tokens per trajectory | 
| training/trainable\_token\_positions | Total trainable target positions in this step | 
| training/nontrainable\_token\_positions | Total non-trainable target positions in this step | 
| training/trainable\_token\_ratio | Ratio: trainable / (trainable \+ nontrainable) token positions | 

**Phase durations (`timing_s/`)**


| Metric | Description | 
| --- | --- | 
| timing\_s/step | Total time for the full step | 
| timing\_s/training | Time for forward/backward passes and optimizer step | 
| timing\_s/policy\_update | Time saving updated weights for the sampler | 
| timing\_s/save\_checkpoint | Time saving a checkpoint (only on checkpoint steps) | 
| timing\_s/eval | Time running evaluation (only on eval steps) | 

**Reward distribution (`rollout/reward/`)**


| Metric | Description | 
| --- | --- | 
| rollout/reward/mean | Mean trajectory reward across all groups | 
| rollout/reward/valid\_mean | Mean reward over only the valid (non-zero-advantage) groups; equals mean when no filtering occurred | 
| rollout/reward/std | Standard deviation of trajectory rewards | 
| rollout/reward/min | Minimum trajectory reward | 
| rollout/reward/max | Maximum trajectory reward | 
| rollout/reward/zero\_frac | Fraction of trajectories with total reward exactly 0.0 | 

**Turn counts (`rollout/turns/`)**


| Metric | Description | 
| --- | --- | 
| rollout/turns/mean | Mean turns (transitions) per trajectory | 
| rollout/turns/min | Minimum turns across trajectories | 
| rollout/turns/max | Maximum turns across trajectories | 

**Token lengths (`rollout/tokens/`)**


| Metric | Description | 
| --- | --- | 
| rollout/tokens/prompt\_mean | Mean prompt token count per transition | 
| rollout/tokens/response\_mean | Mean response token count per transition | 
| rollout/tokens/response\_std | Standard deviation of response token counts | 
| rollout/tokens/response\_min | Minimum response tokens | 
| rollout/tokens/response\_max | Maximum response tokens (watch for clustering at sampling\_max\_tokens) | 

**Log-probability health (`rollout/logprob/`)**


| Metric | Description | 
| --- | --- | 
| rollout/logprob/zero\_count | Total zero-logprob tokens | 
| rollout/logprob/zero\_frac | Fraction of all logprobs that are exactly 0.0 | 
| rollout/logprob/zero\_per\_group | Average zero logprobs per trajectory group | 
| rollout/logprob/nz\_mean | Mean of non-zero logprobs | 
| rollout/logprob/nz\_std | Standard deviation of non-zero logprobs | 
| rollout/logprob/nz\_min | Minimum non-zero logprob | 
| rollout/logprob/nz\_max | Maximum non-zero logprob | 

**Advantage distribution (`rollout/advantage/`)**


| Metric | Description | 
| --- | --- | 
| rollout/advantage/mean | Mean advantage value across all transitions | 
| rollout/advantage/std | Standard deviation of advantages | 
| rollout/advantage/min | Minimum advantage | 
| rollout/advantage/max | Maximum advantage | 
| rollout/advantage/n\_positive | Transitions with positive advantage | 
| rollout/advantage/n\_negative | Transitions with negative advantage | 

**Batch-quality classification (`analysis/`)**


| Metric | Description | 
| --- | --- | 
| analysis/batch\_completion\_ratio | total\_completed / batch\_size — fraction of expected groups that arrived | 
| analysis/batch\_valid\_ratio | valid\_count / batch\_size — non-zero-advantage groups relative to full batch | 
| analysis/zero\_adv\_groups | Groups where all transitions have near-zero advantage | 
| analysis/zero\_adv\_nonzero\_reward | Zero-advantage groups where at least one transition has reward not equal to 0 (all-correct case for binary rewards) | 
| analysis/zero\_adv\_zero\_reward | Zero-advantage groups where all rewards are 0 (all-wrong case) | 
| analysis/reward\_variance\_across\_groups | Variance of per-group mean rewards (high = diverse batch) | 
| analysis/mean\_group\_reward\_spread | Average within-group reward spread max - min | 

**Evaluation reward and pass@k (`val/reward/`)**

Emitted at baseline (step 0), at every `val_every` interval, and at the final step. Includes the same distribution metrics as `rollout/reward` plus group-reward metrics aggregated by prompt.

**Distribution:**


| Metric | Description | 
| --- | --- | 
| val/reward/mean | Mean reward over the eval set | 
| val/reward/std | Reward std dev | 
| val/reward/min | Minimum reward | 
| val/reward/max | Maximum reward | 
| val/reward/zero\_frac | Fraction of zero-reward trajectories | 

**Group-reward (per-prompt aggregation):**


| Metric | Description | 
| --- | --- | 
| val/reward/min\_within\_groups | Average per-prompt minimum reward | 
| val/reward/mean\_within\_groups | Average per-prompt mean reward | 
| val/reward/max\_within\_groups | Average per-prompt maximum reward | 
| val/reward/std\_within\_groups | Average per-prompt reward std (consistency) | 
| val/reward/rollouts\_per\_prompt | Mean rollouts (n) across prompts | 
| val/reward/num\_prompts | Distinct prompts evaluated | 

**Pass@k and success accounting:**


| Metric | Description | 
| --- | --- | 
| val/reward/succeeded\_rollouts | Total rollouts with reward ≥ success\_threshold | 
| val/reward/failed\_rollouts | Total rollouts with reward < success\_threshold | 
| val/reward/success\_threshold | Threshold used (echoed for clarity) | 
| val/reward/pass\_at\_{k} | Probability ≥1 of k samples passes | 
| val/reward/pass\_power\_{k} | Probability all k samples pass (reliability) | 

**Evaluation turn counts (`val/turns/`)**


| Metric | Description | 
| --- | --- | 
| val/turns/mean | Mean turns per eval trajectory | 
| val/turns/min | Minimum turns | 
| val/turns/max | Maximum turns | 

**Evaluation token lengths (`val/tokens/`)**


| Metric | Description | 
| --- | --- | 
| val/tokens/prompt\_mean | Mean prompt tokens per transition | 
| val/tokens/response\_mean | Mean response tokens per transition | 
| val/tokens/response\_std | Standard deviation of response tokens | 
| val/tokens/response\_min | Minimum response tokens | 
| val/tokens/response\_max | Maximum response tokens | 

**Evaluation log-probability health (`val/logprob/`)**


| Metric | Description | 
| --- | --- | 
| val/logprob/zero\_count | Total zero-logprob tokens | 
| val/logprob/zero\_frac | Fraction of zero logprobs | 
| val/logprob/zero\_per\_group | Zero logprobs per group | 
| val/logprob/nz\_mean | Mean of non-zero logprobs | 
| val/logprob/nz\_std | Standard deviation of non-zero logprobs | 
| val/logprob/nz\_min | Minimum non-zero logprob | 
| val/logprob/nz\_max | Maximum non-zero logprob | 

**Accessing the MLflow UI**

Access the MLflow UI via a presigned URL:

```
aws sagemaker create-presigned-mlflow-app-url \
  --arn arn:aws:sagemaker:us-west-2:123456789012:mlflow-app/mlflow-app-id \
  --region us-west-2
```

Copy the `AuthorizedUrl` from the output into your browser.

#### Agent trajectories and traces
<a name="model-customize-mtrl-job-trajectories"></a>

During training, SageMaker AI records every interaction between your agent and the policy model as a trajectory — the complete record of one rollout. Each trajectory captures every prompt sent to the model, every response generated, every tool call made, and the final reward. Trajectories are published to your MLflow experiment as structured traces.

**Trace contents**
+ The input prompt from your training dataset
+ Every model inference turn (prompt, response, and token-level data)
+ Tool calls and their results, if your agent uses tools
+ The final reward score
+ Timing information for each turn

**Viewing trajectories in the MLflow UI**

Access the MLflow UI via a presigned URL:

```
aws sagemaker create-presigned-mlflow-app-url \
  --arn arn:aws:sagemaker:us-west-2:123456789012:mlflow-app/mlflow-app-id \
  --region us-west-2
```

Copy the `AuthorizedUrl` from the output into your browser.

Open the MLflow UI using the presigned URL above. Navigate to your experiment's run and select the Traces tab. Each trace represents one completed rollout and shows:
+ The system prompt and user prompt
+ Each assistant response (with thinking/reasoning if applicable)
+ Tool use spans showing which tools were called and their outputs
+ The reward score assigned to the trajectory

**Use trajectories to debug low reward scores**


| Symptom | What to look for | 
| --- | --- | 
| Low reward across most rollouts | Are model responses coherent? Is the prompt format correct? | 
| Tool-related failures | Are tool calls succeeding? Are inputs and outputs well-formed? | 
| Agent looping | Is the agent repeating the same actions without making progress? | 
| Truncated responses | Are responses being cut off by the maxTokens limit? | 

## Get Training Results
<a name="model-customize-mtrl-job-results"></a>

When a training job completes, your trained model weights are stored as a SageMaker AI Model Package. This section explains how to find your results, understand the checkpoint types produced during training, and use them for deployment or continued training.

### How results are stored
<a name="model-customize-mtrl-job-results-storage"></a>

SageMaker AI stores training output as versioned, immutable Model Packages inside Model Package Groups. Multi-turn RL uses two separate groups, which you specify when creating a job:


| Group | Purpose | Contents | 
| --- | --- | --- | 
| Output Model Package Group | Final trained model | HuggingFace-compatible LoRA adapter weights (adapter\_config.json \+ adapter\_model.safetensors) | 
| Intermediate Checkpoint Model Package Group | Resumable training state | LoRA adapter weights \+ optimizer states \+ training step metadata | 

**Configure both groups in your ModelPackageConfig:**

```
"ModelPackageConfig": {
  "OutputModelPackageGroupArn": "arn:aws:sagemaker:us-west-2:123456789012:model-package-group/my-final-models",
  "IntermediateCheckpointModelPackageGroupArn": "arn:aws:sagemaker:us-west-2:123456789012:model-package-group/my-intermediate-checkpoints"
}
```

### Checkpoint types
<a name="model-customize-mtrl-job-results-checkpoint-types"></a>

Training produces two types of checkpoints, saved at every training step:

**Model checkpoint (weights only)**
+ Stored in the Output Model Package Group
+ Contains HuggingFace-compatible LoRA adapter weights in SafeTensors format
+ Use for inference, deployment, or as the starting point for a new training job
+ Created at every step, at job completion, and when a job is stopped

**Resumable checkpoint (full state)**
+ Stored in the Intermediate Checkpoint Model Package Group
+ Contains LoRA adapter weights, optimizer states, and per-GPU training step metadata
+ Use to resume an interrupted job from the exact step it stopped
+ Internal format — not directly usable for inference

### Checkpoint lifecycle
<a name="model-customize-mtrl-job-results-checkpoint-lifecycle"></a>

```
Step 1 → Intermediate Checkpoint (resumable)
Step 1 → Intermediate Checkpoint (HF-compatible)
...
Step N-1 → Intermediate Checkpoint (resumable)
Step N-1 → Intermediate Checkpoint (HF-compatible)
...
Step N (final) → Model Checkpoint (HuggingFace LoRA) → Output Model Package Group
```

### Retrieve your trained model
<a name="model-customize-mtrl-job-results-retrieve"></a>

When a job completes successfully, the final model is saved as a Model Package in the Output Model Package Group. The `OutputModelPackageArn` field on the job record contains the ARN.

Check job completion and retrieve the output model ARN:

```
aws sagemaker describe-job \
--job-name "my-agent-rft-job" \
--job-category AgentRFT \
--region us-west-2
```

Look for `OutputModelPackageArn` in the response. Use it to describe the Model Package and get the S3 location of the weights:

```
aws sagemaker describe-model-package \
--model-package-name "arn:aws:sagemaker:us-west-2:123456789012:model-package/my-final-models/5"
```

If a job fails or is stopped before completion, the last intermediate checkpoint is promoted to the Output Model Package Group on a best-effort basis. Check `OutputModelPackageArn` the same way.

To monitor checkpoint creation during training, watch the `ResumableCheckpoint` and `ModelCheckpoint` fields in DescribeJob output.

### Resume an interrupted job
<a name="model-customize-mtrl-job-results-resume"></a>

If a job fails or is stopped mid-training, you can start a new job that picks up from the exact step where it left off. The platform restores the full training state — weights, optimizer momentum, and step counter — from the resumable checkpoint.

Specify a resumable checkpoint from the Intermediate Checkpoint Model Package Group as `InputModelPackageArn`:

```
"ModelPackageConfig": {
  "OutputModelPackageGroupArn": "arn:aws:sagemaker:us-west-2:123456789012:model-package-group/my-final-models",
  "IntermediateCheckpointModelPackageGroupArn": "arn:aws:sagemaker:us-west-2:123456789012:model-package-group/my-intermediate-checkpoints",
  "InputModelPackageArn": "arn:aws:sagemaker:us-west-2:123456789012:model-package/my-intermediate-checkpoints/5"
}
```

The `InputModelPackageArn` must point to a resumable checkpoint (one with `IsCheckpoint=true` in its Model Package metadata). Training resumes from the step after the checkpoint — for example, if the checkpoint was saved at step 4, training continues from step 5.

The following must stay the same between the original job and the resumed job:
+ Base model
+ LoRA configuration (rank and alpha)
+ Hyperparameters (learning rate, batch size, etc.)
+ Dataset

### Continue training on a new job (iterative training)
<a name="model-customize-mtrl-job-results-iterative"></a>

Iterative training lets you build on a previously trained model with a different dataset, different hyperparameters, or a refined reward function. Unlike resuming, this starts a fresh training run — the optimizer resets, the step counter resets to 0, and only the trained LoRA weights carry over.

Specify a model checkpoint from the Output Model Package Group as `InputModelPackageArn`:

```
"ModelPackageConfig": {
  "OutputModelPackageGroupArn": "arn:aws:sagemaker:us-west-2:123456789012:model-package-group/my-final-models",
  "IntermediateCheckpointModelPackageGroupArn": "arn:aws:sagemaker:us-west-2:123456789012:model-package-group/my-intermediate-checkpoints",
  "InputModelPackageArn": "arn:aws:sagemaker:us-west-2:123456789012:model-package/my-final-models/3"
}
```

**What you can change between iterations:**
+ Hyperparameters (learning rate, batch size, max\_steps, group\_size, etc.)
+ Dataset (different prompts or data distribution)
+ Reward function
+ Agent configuration

**What must stay the same:**
+ Base model — the LoRA adapter is tied to the base model architecture

Common patterns for iterative training:
+ **Curriculum learning** — train on easier problems first, then continue on harder ones
+ **Reward refinement** — start with a simple reward function, then iterate with a more nuanced one
+ **Hyperparameter adjustment** — increase batch size or tune learning rate after observing initial training dynamics

### Checkpoint best practices
<a name="model-customize-mtrl-job-results-best-practices"></a>
+ **Monitor checkpoint creation**. Use DescribeJob to track `ResumableCheckpoint` and `ModelCheckpoint` fields during training so you know what's available if you need to resume.
+ **Plan for failures on long jobs.** If a job has many steps, design your workflow to resume from checkpoints rather than restart from scratch.