# Monitoring Progress Across Iterations

You can track metrics via MLflow.

## Create an MLflow app

**Using Studio UI:** If you create a training job
through the Studio UI, a default MLflow app is created automatically and selected by
default under Advanced Options.

**Using CLI:** If you use the CLI, you must create an
MLflow app and pass it as an input to the training job API request.

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

## Access the MLflow app

**Using CLI:** Create a pre-signed URL to access the
MLflow app UI:

```
aws sagemaker create-presigned-mlflow-app-url \
  --arn $mlflow_app_arn \
  --region $region \
  --output text
```

**Using Studio UI:** The Studio UI displays key
metrics stored in MLflow and provides a link to the MLflow app UI.

## Key metrics to track

Monitor these metrics across iterations to assess improvement and track the job progress:

**For SFT**

- Training loss curves
- Number of samples consumed and time to process samples
- Performance accuracy on held-out test sets
- Format compliance (e.g., valid JSON output rate)
- Perplexity on domain-specific evaluation data

**For RFT**

- Average reward scores over training
- Reward distribution (percentage of high-reward responses)
- Validation reward trends (watch for over-fitting)
- Task-specific success rates (e.g., code execution pass rate, math problem
  accuracy)

**General**

- Benchmark performance deltas between iterations
- Human evaluation scores on representative samples
- Production metrics (if deploying iteratively)

## Determining when to stop

Stop iterating when:

- **Performance plateaus**: Additional training
  no longer meaningfully improves target metrics
- **Technique switching helps**: If one
  technique plateaus, try switching (e.g., SFT → RFT → SFT) to break through
  performance ceilings
- **Target metrics achieved**: Your success
  criteria are met
- **Regression detected**: New iterations
  degrade performance (see rollback procedures below)

For detailed evaluation procedures, refer to the **Evaluation** section.
