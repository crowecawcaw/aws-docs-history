

# Model evaluation
<a name="model-customize-mtrl-evaluation"></a>

 Evaluation runs your agent against a prompt set and reports reward, pass@k, and trajectory metrics. Use it to compare a fine-tuned model against its base or benchmark a candidate before deployment. 

 **Note:** Evaluation jobs use `JobCategory: AgentRFTEvaluation` (not `AgentRFT` as used in training). Use this category on `CreateJob` and `DescribeJob` calls for eval jobs. 

## Preparing evaluation data
<a name="model-customize-mtrl-evaluation-preparing-data"></a>

 Evaluation datasets use the same format and schema as training datasets. See [Prompt dataset format](model-customize-mtrl-assets.md#model-customize-mtrl-assets-prompt-dataset-format). The guidance below is eval-specific. 

1. **Hold out evaluation data from training datasets.** Never evaluate on training prompts as scores will overstate performance. Reserve a portion of the data for a held-out set, or maintain a separate eval dataset. Keep the same eval set across iterations so results are comparable.

1. **Match the training prompt format.** The agent must parse eval prompts the same way it parsed training prompts. If you used encoding or encryption during training, use the identical structure here. Generating both from the same code path avoids drift.

1. **Cover the behaviors you care about.** Exercise each tool and tool combination your agent uses. Include prompts that previously caused failures so regressions surface.

1. **Protect sensitive content the same way as in training** as the service passes prompts through without inspection.

## Launching an evaluation job
<a name="model-customize-mtrl-evaluation-launching"></a>

After training completes, evaluate your model using one of the following methods.

### SageMaker AI Studio
<a name="model-customize-mtrl-evaluation-launching-studio"></a>
+ Navigate to your custom model's details page (**Models** > **My Models** > select your MTRL model).
+ Choose **Evaluate** to open the evaluation configuration page.
+ Select **Multi-Turn RL** as the evaluation type.
+ Configure your agent environment — select your Bedrock AgentCore runtime or provide your Lambda forwarder ARN.
+ Provide your evaluation dataset (S3 URI or registered dataset containing held-out evaluation prompts).
+ Choose **Submit** to start the evaluation job.

### SageMaker AI Python SDK
<a name="model-customize-mtrl-evaluation-launching-sdk"></a>

The `MultiTurnRLEvaluator` provides a high-level interface for launching evaluation jobs. When you pass a completed trainer, the evaluator automatically resolves the model package ARN, agent configuration, and agent qualifier.

**Evaluate a fine-tuned model**

```
from sagemaker.train.evaluate import MultiTurnRLEvaluator
from sagemaker.train.multi_turn_rl_trainer import MultiTurnRLTrainer

# Attach to a completed training job
trainer = MultiTurnRLTrainer.attach(job_name="my-mtrl-job-20260512082005")

# Minimal evaluator — everything else inferred from trainer
evaluator = MultiTurnRLEvaluator(
    model=trainer,
    dataset="s3://my-bucket/eval-prompts.parquet",
    s3_output_path="s3://my-bucket/eval-output/",
)

execution = evaluator.evaluate()
print(f"Evaluation started: {execution.arn}")

# Wait for completion
execution.wait()
print(f"Status: {execution.status.overall_status}")
print(f"S3 Output: {execution.s3_output_path}")
print(f"MLflow: {execution.mlflow_url}")
```

**Evaluate a base model (no training)**

When evaluating a base model directly, `agent_config` is required since there is no trainer to inherit from:

```
from sagemaker.train.evaluate import MultiTurnRLEvaluator

# With Bedrock AgentCore
evaluator_base = MultiTurnRLEvaluator(
    model="openai-reasoning-gpt-oss-20b",
    dataset="s3://my-bucket/eval-prompts.parquet",
    agent_config="arn:aws:bedrock-agentcore:us-west-2:123456789012:runtime/my-agent",
    s3_output_path="s3://my-bucket/eval-output/base/",
    mlflow_resource_arn="arn:aws:sagemaker:us-west-2:123456789012:mlflow-tracking-server/my-mlflow",
    role="arn:aws:iam::123456789012:role/SageMakerRole",
    accept_eula=True,
)

execution = evaluator_base.evaluate()
execution.wait()
```

**Side-by-side comparison (base vs fine-tuned)**

A single `evaluate()` call that evaluates both the base model and the fine-tuned model in one pipeline:

```
comparison_evaluator = MultiTurnRLEvaluator(
    model=trainer,
    dataset="s3://my-bucket/eval-prompts.parquet",
    s3_output_path="s3://my-bucket/eval-output/comparison/",
    evaluate_base_model=True,
)

execution = comparison_evaluator.evaluate()
execution.wait()
print(f"Status: {execution.status.overall_status}")
```

**Monitor and retrieve results**

```
# Refresh status
execution.refresh()
print(f"Status: {execution.status.overall_status}")

# Step-level detail
for step in execution.status.step_details:
    print(f"  {step.name}: {step.status}")
    if step.job_arn:
        print(f"    Job ARN: {step.job_arn}")

# MLflow URL
print(f"MLflow: {execution.mlflow_url}")
```

### AWS CLI and boto3
<a name="model-customize-mtrl-evaluation-launching-agentcore"></a>

You can also create evaluation jobs directly using the `CreateJob` API.

**Create an evaluation job (Bedrock AgentCore)**

 To create an evaluation job, call the `CreateJob` API with `JobCategory` set to `AgentRFTEvaluation`. Agent setup and configuration follows the same process as training jobs. 

**Using AWS CLI**

```
aws sagemaker create-job \
  --job-category AgentRFTEvaluation \
  --job-name "my-agent-rft-eval-job" \
  --role-arn "arn:aws:iam::123456789012:role/SageMakerFineTuningJobRole" \
  --job-config-schema-version "1.0.0" \
  --job-config-document '{
    "AgentConfig": {
      "BedrockAgentCoreConfig": {
        "AgentRuntimeArn": "arn:aws:bedrock-agentcore:us-west-2:123456789012:runtime/my-agent"
      }
    },
    "InputDataConfig": [{
      "ChannelName": "evaluation",
      "DataSource": {
        "S3DataSource": {
          "S3DataType": "S3Prefix",
          "S3Uri": "s3://your-bucket-name/eval-prompts/"
        }
      }
    }],
    "OutputDataConfig": {
      "S3OutputPath": "s3://your-bucket-name/eval-output/",
      "MlflowConfig": {
        "MlflowResourceArn": "arn:aws:sagemaker:us-west-2:123456789012:mlflow-app/my-rft-mlflow-app"
      }
    },
    "EvaluationConfig": {
      "BaseModelArn": "arn:aws:sagemaker:us-west-2:aws:hub-content/SageMakerPublicHub/Model/openai-reasoning-gpt-oss-20b",
      "AcceptEula": true,
      "HyperParameters": {"batch": { "eval_group_size": 1 }, "eval_metrics_config": { "pass_k_values": [1, 2, 4, 8, 16, 32], "success_threshold": 1 }}
    }
  }' \
  --region us-west-2
```

**Using SageMaker AI Python SDK (boto3)**

```
import json
import boto3

sm = boto3.client("sagemaker")

response = sm.create_job(
    JobName="my-agent-rft-eval-job",
    RoleArn="arn:aws:iam::123456789012:role/SageMakerFineTuningJobRole",
    JobCategory="AgentRFTEvaluation",
    JobConfigSchemaVersion="1.0.0",
    JobConfigDocument=json.dumps({
        "AgentConfig": {
            "BedrockAgentCoreConfig": {
                "AgentRuntimeArn": "arn:aws:bedrock-agentcore:us-west-2:123456789012:runtime/my-agent"
            }
        },
        "InputDataConfig": [{
            "ChannelName": "evaluation",
            "DataSource": {
                "S3DataSource": {
                    "S3DataType": "S3Prefix",
                    "S3Uri": "s3://your-bucket-name/eval-prompts/"
                }
            }
        }],
        "OutputDataConfig": {
            "S3OutputPath": "s3://your-bucket-name/eval-output/",
            "MlflowConfig": {
                "MlflowResourceArn": "arn:aws:sagemaker:us-west-2:123456789012:mlflow-app/my-rft-mlflow-app"
            }
        },
        "EvaluationConfig": {
            "BaseModelArn": "arn:aws:sagemaker:us-west-2:aws:hub-content/SageMakerPublicHub/Model/openai-reasoning-gpt-oss-20b",
            "AcceptEula": True,
            "HyperParameters": {"batch": { "eval_group_size": 1 }, "eval_metrics_config": { "pass_k_values": [1, 2, 4, 8, 16, 32], "success_threshold": 1 }}
        }
    })
)

print(f"Eval Job ARN: {response['JobArn']}")
```

**Evaluating a fine-tuned model**

 To evaluate a model produced by a training job, include `ModelPackageConfig` with the `InputModelPackageArn`: 

```
import json
import boto3

sm = boto3.client("sagemaker")

response = sm.create_job(
    JobName="my-agent-rft-eval-finetuned",
    RoleArn="arn:aws:iam::123456789012:role/SageMakerFineTuningJobRole",
    JobCategory="AgentRFTEvaluation",
    JobConfigSchemaVersion="1.0.0",
    JobConfigDocument=json.dumps({
        "AgentConfig": {...},
        "InputDataConfig": [...],
        "OutputDataConfig": {...},
        "ModelPackageConfig": {
            "InputModelPackageArn": "arn:aws:sagemaker:us-west-2:123456789012:model-package/my-final-models/1"
        },
        "EvaluationConfig": {...}
    })
)

print(f"Eval Job ARN: {response['JobArn']}")
```

**Create an evaluation job (Custom Agent with Lambda Forwarder)**

 Use the same approach as Bedrock AgentCore evaluation but specify `CustomAgentLambdaConfig` in the `AgentConfig`: 

```
"AgentConfig": {
    "CustomAgentLambdaConfig": {
        "LambdaArn": "arn:aws:lambda:us-west-2:account-id:function:rft-agent-forwarder"
    }
}
```

## Evaluation hyperparameters
<a name="model-customize-mtrl-evaluation-hyperparameters"></a>


| Category | Parameter | Type | Default | Description | 
| --- | --- | --- | --- | --- | 
| batch | eval\_group\_size | integer | 1 | Rollouts per prompt. Note: To compute pass@k, set eval\_group\_size >= k. | 
| eval\_metrics\_config | pass\_k\_values | array | [1, 2, 4, 8, 16, 32] | List of k values for computing pass@k and pass^k metrics. pass@k = probability that at least 1 of k sampled rollouts succeeds. pass^k = probability that all k rollouts succeed. | 
| eval\_metrics\_config | success\_threshold | float | 1 | A rollout is "successful" when reward >= success\_threshold. Note this applies for pass@k, pass^k, succeeded/failed count metrics. | 
| eval\_sampling\_params | temperature | float | 0 | Sampling temperature for evaluation rollouts. Note: it is recommended to increase this value beyond 0 for pass@k and pass^k metrics to avoid deterministic behavior. | 
| eval\_sampling\_params | sampling\_top\_p | float | 1 | Nucleus sampling cutoff for evaluation rollouts. | 
| eval\_sampling\_params | sampling\_max\_tokens | integer | 4096 | Maximum tokens the model can generate per turn during evaluation rollouts. | 
| rollout | timeout | float | 600 | Time (seconds) after which an evaluation rollout is treated as failed and may be retried. | 
| rollout | max\_concurrency | int | 96 | Maximum number of evaluation rollouts that can execute in parallel. | 
| rollout | max\_retries | int | 3 | Number of retry attempts for failed evaluation rollouts before marking them as permanently failed. | 

## Monitoring evaluation
<a name="model-customize-mtrl-evaluation-monitoring"></a>

```
aws sagemaker describe-job \
  --job-name "my-agent-rft-eval-job" \
  --job-category AgentRFTEvaluation \
  --region us-west-2
```

## Interpreting evaluation results
<a name="model-customize-mtrl-evaluation-results"></a>

 Open your MLflow App to view logged metrics, reward distributions, and trajectory visualizations for the evaluation run. See below for explanation on what each of the metrics means. 

### Reward metrics (`eval/reward/`)
<a name="model-customize-mtrl-evaluation-results-reward"></a>


| Metric | Description | 
| --- | --- | 
| eval/reward/mean | Average reward score across all rollouts. | 
| eval/reward/min | Minimum reward score across all rollouts. | 
| eval/reward/max | Maximum reward score across all rollouts. | 
| eval/reward/std | Standard deviation of reward scores across all rollouts. | 
| eval/reward/zero\_frac | Fraction of rollouts that scored exactly 0 (complete failures). | 
| eval/reward/pass\_at\_1 | Probability that at least 1 out of 1 sample per prompt succeeds. This is the primary success metric. | 
| eval/reward/pass\_power\_1 | Pass rate with power weighting. | 
| eval/reward/succeeded\_rollouts | Total number of rollouts that achieved a positive reward. | 
| eval/reward/failed\_rollouts | Total number of rollouts that scored 0. | 
| eval/reward/num\_prompts | Number of distinct prompts evaluated. | 
| eval/reward/rollouts\_per\_prompt | Number of attempts (samples) generated per prompt. | 
| eval/reward/success\_threshold | The reward value required to count a rollout as "successful". | 
| eval/reward/mean\_within\_groups | Average reward per prompt group (requires setting rollouts\_per\_prompt > 1). | 
| eval/reward/std\_within\_groups | Standard deviation of reward within each prompt group. | 
| eval/reward/min\_within\_groups | Minimum reward within each prompt group. | 
| eval/reward/max\_within\_groups | Maximum reward within each prompt group. | 

### Token metrics (`eval/tokens/`)
<a name="model-customize-mtrl-evaluation-results-token"></a>


| Metric | Description | 
| --- | --- | 
| eval/tokens/prompt\_mean | Average prompt length in tokens (includes system prompt, tool descriptions, and multi-turn context). | 
| eval/tokens/response\_mean | Average model response length in tokens per turn. | 
| eval/tokens/response\_min | Shortest model response in tokens. | 
| eval/tokens/response\_max | Longest model response in tokens. | 
| eval/tokens/response\_std | Standard deviation of response lengths. High variance may indicate inconsistent agent behavior. | 

### Turn metrics (`eval/turns/`)
<a name="model-customize-mtrl-evaluation-results-turn"></a>


| Metric | Description | 
| --- | --- | 
| eval/turns/mean | Average number of turns per rollout. High values may indicate the agent is looping or retrying excessively. | 
| eval/turns/min | Fewest turns in any rollout. | 
| eval/turns/max | Most turns in any rollout. Very high values suggest the agent got stuck without solving the task. | 

### Log probability metrics (`eval/logprob/`)
<a name="model-customize-mtrl-evaluation-results-logprob"></a>


| Metric | Description | 
| --- | --- | 
| eval/logprob/nz\_mean | Mean log-probability of non-zero (non-padding) tokens. Values close to 0 indicate high model confidence. | 
| eval/logprob/nz\_min | Lowest log-probability token (least confident prediction). | 
| eval/logprob/nz\_max | Highest log-probability token (most confident prediction). | 
| eval/logprob/nz\_std | Standard deviation of non-zero log-probabilities. Low values mean consistently high confidence. | 
| eval/logprob/zero\_frac | Fraction of tokens with exactly zero log-probability (probability 1.0), typically padding or forced tokens. | 
| eval/logprob/zero\_count | Total count of zero-logprob tokens. | 
| eval/logprob/zero\_per\_group | Average zero-logprob tokens per prompt group. | 

### Timing metrics (`timing_s/`)
<a name="model-customize-mtrl-evaluation-results-timing"></a>


| Metric | Description | 
| --- | --- | 
| timing\_s/eval | Total wall-clock time for the evaluation in seconds. Divide by eval/reward/num\_prompts for average time per prompt. | 

### How to diagnose common patterns
<a name="model-customize-mtrl-evaluation-results-diagnose"></a>


| Pattern | Likely cause | 
| --- | --- | 
| pass\_at\_1 = 0, high turns/mean | Agent is looping without solving tasks. Check tool usage and action patterns in trajectories. | 
| pass\_at\_1 = 0, low tokens/response\_mean | Agent producing very short (possibly empty or malformed) responses. Check prompt format and model compatibility. | 
| High turns/max with low turns/min | Agent is showing inconsistent behavior across prompts. Some tasks may be much harder or the agent may be failing on specific tool interactions. | 
| High confidence (logprob/nz\_mean close to 0) but low reward | Model is confidently producing wrong outputs. It may need more training data diversity or reward signal refinement. | 
| zero\_frac = 1.0 in reward | Complete failure. Verify agent deployment, tool connectivity, and that the evaluation dataset format is correct. | 

 For raw results, review the artifacts written to the `S3OutputPath` specified in `OutputDataConfig`. 

## Limits & quotas for evaluation
<a name="model-customize-mtrl-evaluation-limits"></a>

 Use AWS service quotas to request a limit increase on the maximum number of concurrent evaluation jobs. 


| Quota | Default | 
| --- | --- | 
| rft-evaluation-job maximum concurrent jobs | 1 | 