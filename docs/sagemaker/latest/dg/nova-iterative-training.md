# Iterative Training

## Overview

Iterative training is the process of repeatedly fine-tuning a model through multiple training cycles across different training methods — train, evaluate, analyze errors, adjust data/objectives/hyperparameters — with each round starting from the previous checkpoint. This approach allows you to systematically target model failure modes, incorporate curated examples addressing specific weaknesses, and adapt to changing requirements over time.

**Benefits over single-pass training:**

- **Targeted improvement**: Address specific failure patterns discovered through evaluation
- **Adaptive refinement**: Respond to distribution shifts or evolving product requirements
- **Risk mitigation**: Validate improvements incrementally rather than committing to a single long training run
- **Data efficiency**: Focus data collection efforts on areas where the model underperforms
- **Curriculum Training**: Multiple round of training with increasingly higher quality data

## How it works

### Checkpoint location and access

After each training job completes, a manifest file is generated in the output location specified by the `output_path` parameter in your training configuration.

**To access your checkpoint**

- Navigate to your specified `output_path` in S3
- Download and extract the `output.tar.gz` file
- Open the `manifest.json` file inside
- Locate the `checkpoint_s3_bucket` parameter, which contains the S3 URI of your trained model

**Example manifest.json structure**

```
{
  "checkpoint_s3_bucket": "s3://customer-escrow-<account-number>-smtj-<unique-identifier>/<job-name>/stepID",
  ...
}
```

### Understanding escrow buckets

Since Amazon Nova weights are proprietary, trained model checkpoints are stored in **escrow S3 buckets** within AWS-managed accounts rather than being copied to your account. These escrow buckets:

- Contain your customized model weights securely
- Can be referenced by other AWS services (Inference, Evaluation, and subsequent training jobs)
- Are accessible only to your AWS account via IAM permissions
- Incur standard S3 storage charges in your account (see Cost considerations)

You can use the escrow bucket path as the `model_name_or_path` in your next training run to continue iterative training.

### Using checkpoints for iterative training

Configure your next training job to use the previous checkpoint as the base model:

```
run:
  name: "my-iterative-training-job"
  model_type: amazon.nova-2-lite-v1:0:256k
  model_name_or_path: "s3://customer-escrow-<account-number>-smtj-<unique-identifier>/<previous-job-name>"
  data_s3_path: s3://<bucket>/<data-file>.jsonl
  replicas: 4
```

## When to use iterative training

### Ideal use cases

Use iterative training when you have:

- **Feedback loops** – Ability to collect real-world failure cases and systematically address them
- **Dynamic environments** – Evolving documentation, APIs, or support topics requiring periodic model updates
- **Robust evaluation** – Strong benchmarks and evaluation frameworks (see examples below) to measure improvements confidently
- **ML operations capability** – Resources to manage multiple training cycles and version control

**Examples of robust evaluation frameworks**

- Automated benchmark suites with pass/fail thresholds
- Human evaluation protocols with inter-rater reliability metrics
- Red-team testing scenarios covering edge cases and adversarial inputs
- A/B testing infrastructure to measure production impact

### Common patterns

**SFT → RFT Pipeline**: A frequently used iterative pattern involves:

- **SFT first** – Teach the model how to solve problems through demonstration examples
- **RFT second** – Optimize performance across the broader problem space using reward signals

This sequence is essential when models perform poorly initially—RFT on near-zero accuracy models will not improve performance without first establishing basic problem-solving capabilities through SFT.

### When not to use iterative training

Avoid iterative training for:

- **Stable, well-defined tasks** – Stationary data with consistent requirements already achieving near-ceiling performance
- **Simple classification problems** – Narrow tasks where single-pass training suffices
- **Resource constraints** – Lacking dedicated ML operations capabilities to manage multiple training cycles
- **Marginal gains** – When overhead doesn't justify minimal performance improvements

## Example workflow: SFT → RFT

This example demonstrates a common iterative training pattern for reasoning models.

### Step 1: Initial SFT training

Configure and launch your SFT training job with your dataset:

```
run:
  name: "initial-sft-training"
  model_type: amazon.nova-2-lite-v1:0:256k
  model_name_or_path: "nova-lite-2/prod"
  data_s3_path: s3://<bucket>/sft-training-data.jsonl
  validation_data_s3_path: s3://<bucket>/sft-validation-data.jsonl
```

**Rationale**: SFT provides additional demonstrations that shape model outputs into your desired format and voice, establishing foundational capabilities.

**After training completes**

- Note the `output_path` configured in your training job
- Download `output.tar.gz` from that location
- Extract and locate `manifest.json`
- Copy the `checkpoint_s3_bucket` value

### Step 2: RFT training on SFT checkpoint

Create a new RFT training job using the SFT checkpoint:

```
run:
  name: "rft-on-sft-checkpoint"
  model_type: amazon.nova-2-lite-v1:0:256k
  model_name_or_path: "s3://customer-escrow-<account-number>-smtj-<unique-identifier>/<initial-sft-training>"
  data_s3_path: s3://<bucket>/rft-training-data.jsonl
  reward_lambda_arn: <your-reward-function-arn>
```

**Rationale**: RFT training builds on the SFT foundation, allowing the model to develop more complex reasoning patterns optimized by your reward function.

### Step 3: Evaluate and iterate

Run evaluation on the RFT checkpoint to assess performance:

```
run:
  name: "evaluate-rft-checkpoint"
  model_type: amazon.nova-2-lite-v1:0:256k
  model_name_or_path: "s3://customer-escrow-<account-number>-smtj-<unique-identifier>/<rft-on-sft-checkpoint>"
  data_s3_path: s3://<bucket>/evaluation-data.jsonl
```

If target metrics are not satisfied, continue iterating with adjusted data or hyperparameters.

###### Important

The training technique (LoRA vs. Full Rank) must remain consistent across all iterations:

- If you use SFT with **LoRA**, you must use RFT with **LoRA**
- If you use SFT with **Full Rank**, you must use RFT with **Full Rank**
- You cannot switch between LoRA and Full Rank mid-pipeline

###### Important

If a KMS key is used for encryption in the Amazon-owned output S3 bucket, that same KMS key must be used for all future iterations.

## Monitoring progress across iterations

You can track metrics via MLFlow.

### Create an MLflow app

**Using Studio UI**: If you create a training job through the Studio UI, a default MLflow app is created automatically and selected by default under Advanced Options.

**Using CLI**: If you use the CLI, you must create an MLflow app and pass it as an input to the training job API request.

```
mlflow_app_name="<enter your MLflow app name>"
role_arn="<enter your role ARN>"
bucket_name="<enter your bucket name>"
region="<enter your region>"

mlflow_app_arn=$(aws sagemaker create-mlflow-app \
  --name $mlflow_app_name \
  --artifact-store-uri "s3://$bucket_name" \
  --role-arn $role_arn \
  --region $region)
```

### Access the MLflow app

**Using CLI**: Create a presigned URL to access the MLflow app UI:

```
aws sagemaker create-presigned-mlflow-app-url \
  --arn $mlflow_app_arn \
  --region $region \
  --output text
```

**Using Studio UI**: The Studio UI displays key metrics stored in MLflow and provides a link to the MLflow app UI.

### Key metrics to track

Monitor these metrics across iterations to assess improvement and track the job progress:

**For SFT**

- Training loss curves
- Number of samples consumed and time to process samples
- Performance accuracy on held-out test sets
- Format compliance (for example, valid JSON output rate)
- Perplexity on domain-specific evaluation data

**For RFT**

- Average reward scores over training
- Reward distribution (percentage of high-reward responses)
- Validation reward trends (watch for overfitting)
- Task-specific success rates (for example, code execution pass rate, math problem accuracy)

**General**

- Benchmark performance deltas between iterations
- Human evaluation scores on representative samples
- Production metrics (if deploying iteratively)

### Determining when to stop

Stop iterating when:

- **Performance plateaus** – Additional training no longer meaningfully improves target metrics
- **Technique switching helps** – If one technique plateaus, try switching (for example, SFT → RFT → SFT) to break through performance ceilings
- **Target metrics achieved** – Your success criteria are met
- **Regression detected** – New iterations degrade performance (see rollback procedures below)

For detailed evaluation procedures, refer to the **Evaluation** section.

## Best practices

### Start small and scale gradually

Begin with minimal datasets and single training epochs to validate your approach before scaling up. This builds confidence and helps identify issues early.

### Establish clear success metrics

Define quantitative and qualitative indicators before starting:

**Example success metrics by use case**

- **Question answering** – Exact match accuracy, F1 score, human preference ratings
- **Code generation** – Unit test pass rate, compilation success, execution time
- **Reasoning tasks** – Step accuracy, final answer correctness, reward scores
- **Content generation** – Coherence scores, factual accuracy, style adherence

### Implement automated evaluation

Set up automated evaluation pipelines to track performance after each round, enabling rapid iteration and objective comparison.

### Maintain rigorous version control

Document for each iteration:

- Dataset versions and modifications
- Model checkpoint locations
- Hyperparameter changes
- Performance metrics and deltas
- Qualitative observations

This builds institutional knowledge and enables debugging.

### Focus on data quality over quantity

Analyze failure cases from previous rounds and add targeted, high-quality examples rather than simply increasing dataset size.

### Plan iteration budget

Plan for **3-5 iterations** as a typical range:

- **1-2 iterations** – Often sufficient for simple improvements or final polishing
- **3-5 iterations** – Appropriate for complex tasks requiring multiple refinement cycles
- **5+ iterations** – May indicate diminishing returns or need for different approaches

Adjust based on computational budget and performance improvement rates.

### Implement rollback capabilities

If an iteration introduces regressions:

- **Identify the regression** – Compare evaluation metrics across checkpoints
- **Return to previous checkpoint** – Use the earlier checkpoint's S3 path as your `model_name_or_path`
- **Adjust training approach** – Modify data, hyperparameters, or technique before retrying
- **Document the failure** – Record what caused regression to avoid repeating

**Example rollback**

```
run:
  name: "rollback-to-iteration-2"
  model_type: amazon.nova-2-lite-v1:0:256k
  # Use iteration 2 checkpoint instead of failed iteration 3
  model_name_or_path: "s3://customer-escrow-<account-number>-smtj-<unique-identifier>/<iteration-2-job-name>"
```

## Cost considerations

### Checkpoint storage

- **Location** – Checkpoints stored in escrow buckets incur standard S3 storage charges billed to your AWS account
- **Retention** – Checkpoints are retained indefinitely unless explicitly deleted
- **Management** – Implement lifecycle policies to archive or delete old checkpoints you no longer need

**Cost optimization tips**

- Delete intermediate checkpoints after validating newer iterations
- Archive checkpoints to S3 Glacier for long-term retention at lower cost
- Set retention policies based on your compliance and experimentation needs

## Limitations

### Model family consistency

When iteratively training, you must use the **same model type** throughout all iterations.

**Initial training**

```
run:
  model_type: amazon.nova-2-lite-v1:0:256k
  model_name_or_path: "nova-lite-2/prod"
```

**Subsequent iterations must use the same model_type**

```
run:
  model_type: amazon.nova-2-lite-v1:0:256k  # Must match original
  model_name_or_path: "s3://customer-escrow-<account-number>-smtj-<unique-identifier>/<job-name>"
```

### Training technique consistency

The training technique must remain consistent across iterations:

- **LoRA-trained models** can only be iteratively trained with LoRA
- **Full-Rank-trained models** can only be iteratively trained with Full-Rank

**How LoRA adapters work in iterative training**

- Each LoRA training iteration produces new adapter weights
- New adapters replace (not stack with) previous adapters
- The base model remains frozen; only adapters are updated

### Technique compatibility matrix

| Initial training | Can iterate with                 |
| ---------------- | -------------------------------- |
| SFT (Full-Rank)  | SFT (Full-Rank), RFT (Full-Rank) |
| SFT (LoRA)       | SFT (LoRA), RFT (LoRA)           |
| RFT (Full-Rank)  | RFT (Full-Rank)                  |
| RFT (LoRA)       | RFT (LoRA)                       |

**Verifying compatibility before starting a job**

- Check your previous training recipe to identify the model type and training technique (LoRA vs. Full-Rank)
- Ensure your new recipe matches both the model type and technique
- Review the manifest.json to confirm the checkpoint path is correct

## Troubleshooting

### Error: "Incompatible model training techniques detected"

**Cause**: The training technique (LoRA vs. Full-Rank) doesn't match the checkpoint's technique.

**Resolution**: Ensure your recipe uses the same training technique as the original model:

- If the checkpoint was trained with LoRA, use LoRA in your new recipe
- If the checkpoint was trained with Full-Rank, use Full-Rank in your new recipe

### Error: "Base model for the job extracted from model_name_or_path does not match model_type"

**Cause**: The model type specified in `model_type` doesn't match the actual model in the checkpoint.

**Resolution**: Verify that:

- The `model_type` in your recipe matches the original model type
- The checkpoint S3 path in `model_name_or_path` is correct
- You're using the path from the correct manifest.json file

**Example of correct configuration**

```
run:
  model_type: amazon.nova-2-lite-v1:0:256k  # Must match checkpoint's model
  model_name_or_path: "s3://customer-escrow-<account-number>-smtj-<unique-identifier>/<job-name>"
```

### Error: "Model configuration not found"

**Cause**: The S3 path in `model_name_or_path` is invalid or inaccessible.

**Resolution**:

- Verify the S3 path is correctly copied from the manifest.json file
- Ensure your IAM role has permissions to access the escrow bucket
- Confirm the previous training job completed successfully
- Check for typos in the path

### Performance regression after iteration

**Symptoms**: Evaluation metrics decline after a new training iteration.

**Resolution**:

- **Rollback** – Use the previous checkpoint as your base model
- **Analyze** – Review training logs and data quality for the failed iteration
- **Adjust** – Modify hyperparameters (reduce learning rate), improve data quality, or reduce training epochs
- **Retry** – Launch a new iteration with adjustments
