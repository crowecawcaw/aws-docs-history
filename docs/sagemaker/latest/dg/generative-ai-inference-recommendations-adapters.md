

# Get recommendations for models with LoRA adapters
<a name="generative-ai-inference-recommendations-adapters"></a>

Low-Rank Adaptation (LoRA) is a parameter-efficient fine-tuning technique that trains a small set of adapter weights on top of a frozen base model. You can serve many adapters that share a single base model on one endpoint. This is more cost-effective than deploying a separate copy of the model for each fine-tuned variant.

When you add adapters to a recommendation job, SageMaker AI sizes and benchmarks a *multi-adapter* deployment. This deployment is a single base model with one [Inference components](realtime-endpoints-deploy-models.md#inference-components) per adapter on the same endpoint. The recommendations account for the additional memory that the adapters require, so SageMaker AI validates the returned configurations against the base model and the adapters together.

## Prerequisites
<a name="generative-ai-inference-recommendations-adapters-prereqs"></a>

In addition to the [Prerequisites](generative-ai-inference-recommendations-get-started.md#generative-ai-inference-recommendations-get-started-prereqs) for a recommendation job, you need the following to include adapters:
+ 1–10 LoRA adapters, each trained against the base model that you specify in `ModelSource`.
+ Each adapter in PEFT format. The adapter location must contain an `adapter_config.json` file with a positive rank (`r`), and the adapter weight files (`.safetensors` or `.bin`).
+ All adapters provided in a single form: either in Amazon S3, or as registered SageMaker AI model packages. You can't mix the two forms in one job.

SageMaker AI reads your adapters with the IAM execution role that you pass in `RoleArn`. The role must be able to read (`s3:GetObject` and `s3:ListBucket`) the Amazon S3 location of each adapter. These are the same permissions that it uses for your base model artifacts. If you provide adapters as model packages, the role also needs `sagemaker:DescribeModelPackage` on each package so that SageMaker AI can resolve the Amazon S3 location of the adapter.

## Requirements and restrictions
<a name="generative-ai-inference-recommendations-adapters-restrictions"></a>

The following requirements and restrictions apply when you add adapters to a recommendation job:
+ **One source form per job.** `AdapterSource` is a union. Set exactly one of `S3Uris` or `ModelPackageArns`. SageMaker AI rejects a job that sets both fields or neither field.
+ **Adapter rank.** No adapter's rank can exceed 512, the largest LoRA rank that the vLLM serving engine supports. For more information, see the note in [Add adapters to a recommendation job](#generative-ai-inference-recommendations-adapters-input).

## Add adapters to a recommendation job
<a name="generative-ai-inference-recommendations-adapters-input"></a>

To include adapters, add the optional `AdapterSource` object to your `CreateAIRecommendationJob` request. `AdapterSource` is a union: set exactly one of the following fields, each a list of 1–10 adapter entries:

`S3Uris`  
A list of `{"AdapterId": ..., "S3Uri": ...}` entries. Use this form for adapters that you produced with your own or an open-source PEFT pipeline. Each `S3Uri` is the Amazon S3 prefix that holds the adapter's `adapter_config.json` and weight files.

`ModelPackageArns`  
A list of `{"AdapterId": ..., "ModelPackageArn": ...}` entries. Use this form for adapters that are already registered as SageMaker AI model packages, such as adapters produced by a SageMaker AI fine-tuning workflow. SageMaker AI reads the adapter artifact location from each model package.

The `AdapterId` is a name that you assign to each adapter. It must meet the following requirements:
+ Must be unique within the request.
+ Must be no more than 63 characters.
+ Must match the pattern `^[a-zA-Z0-9](-*[a-zA-Z0-9])*$`: it starts and ends with an alphanumeric character, allows hyphens only between alphanumeric characters, and doesn't use underscores.

SageMaker AI uses the `AdapterId` as the inference component name for that adapter. This name is also the routing handle that you use to send requests to the adapter when you invoke the deployed endpoint.

**Python (boto3) — adapters in Amazon S3**

```
try:
    response = client.create_ai_recommendation_job(
        AIRecommendationJobName="my-lora-recommendation-job",
        ModelSource={
            "S3": {
                "S3Uri": "s3://amzn-s3-demo-bucket/models/my-base-model/",
            }
        },
        OutputConfig={
            "S3OutputLocation": "s3://amzn-s3-demo-bucket/recommendations/"
        },
        AdapterSource={
            "S3Uris": [
                {"AdapterId": "sql", "S3Uri": "s3://amzn-s3-demo-bucket/adapters/sql/"},
                {"AdapterId": "chat", "S3Uri": "s3://amzn-s3-demo-bucket/adapters/chat/"},
            ]
        },
        PerformanceTarget={
            "Constraints": [
                {"Metric": "throughput"}
            ]
        },
        AIWorkloadConfigIdentifier="my-recommendation-workload",
        RoleArn="arn:aws:iam::111122223333:role/ExampleRole",
    )
    print(response["AIRecommendationJobArn"])
except client.exceptions.ResourceInUse as error:
    print(f"A job with this name already exists: {error}")
except Exception as error:
    print(f"Error creating recommendation job: {error}")
    raise
```

**Python (boto3) — adapters as model packages**

```
try:
    response = client.create_ai_recommendation_job(
        AIRecommendationJobName="my-lora-recommendation-job",
        ModelSource={
            "S3": {
                "S3Uri": "s3://amzn-s3-demo-bucket/models/my-base-model/",
            }
        },
        OutputConfig={
            "S3OutputLocation": "s3://amzn-s3-demo-bucket/recommendations/"
        },
        AdapterSource={
            "ModelPackageArns": [
                {
                    "AdapterId": "sql",
                    "ModelPackageArn": "arn:aws:sagemaker:us-west-2:111122223333:model-package/my-sql-adapter/1",
                }
            ]
        },
        PerformanceTarget={
            "Constraints": [
                {"Metric": "throughput"}
            ]
        },
        AIWorkloadConfigIdentifier="my-recommendation-workload",
        RoleArn="arn:aws:iam::111122223333:role/ExampleRole",
    )
    print(response["AIRecommendationJobArn"])
except client.exceptions.ResourceInUse as error:
    print(f"A job with this name already exists: {error}")
except Exception as error:
    print(f"Error creating recommendation job: {error}")
    raise
```

**AWS CLI**

```
aws sagemaker create-ai-recommendation-job \
  --ai-recommendation-job-name "my-lora-recommendation-job" \
  --model-source '{"S3": {"S3Uri": "s3://amzn-s3-demo-bucket/models/my-base-model/"}}' \
  --output-config '{"S3OutputLocation": "s3://amzn-s3-demo-bucket/recommendations/"}' \
  --adapter-source '{
    "S3Uris": [
      {"AdapterId": "sql", "S3Uri": "s3://amzn-s3-demo-bucket/adapters/sql/"},
      {"AdapterId": "chat", "S3Uri": "s3://amzn-s3-demo-bucket/adapters/chat/"}
    ]
  }' \
  --performance-target '{"Constraints": [{"Metric": "throughput"}]}' \
  --ai-workload-config-identifier "my-recommendation-workload" \
  --role-arn "arn:aws:iam::111122223333:role/ExampleRole" \
  --region us-west-2
```

**Note**  
No adapter's rank (`r` in `adapter_config.json`) can exceed 512, the largest LoRA rank that the vLLM serving engine supports. SageMaker AI serves all of your adapters at a single rank, and rounds that rank up to the nearest rank that vLLM supports: 1, 8, 16, 32, 64, 128, 256, 320, or 512. For example, SageMaker AI serves adapters with ranks of 4 and 12 at rank 16. If the largest rank across your adapters exceeds 512, the job fails with a validation error. Retrain the affected adapters with a smaller rank, or omit them from `AdapterSource`.

## Interpret the recommendations
<a name="generative-ai-inference-recommendations-adapters-output"></a>

When the job completes, call `DescribeAIRecommendationJob`. In addition to the fields described in [Step 3: Review recommendations](generative-ai-inference-recommendations-get-started.md#generative-ai-inference-recommendations-get-started-results), the response includes adapter-specific information.

`AdapterSource`  
The top-level response echoes the `AdapterSource` that you supplied, in the same form (`S3Uris` or `ModelPackageArns`).

`AdapterDetails`  
Each recommendation in the `Recommendations` array carries an `AdapterDetails` object that lists every adapter in *both* forms: `S3Uris` and `ModelPackageArns`, keyed by `AdapterId`. If you supplied adapters only as Amazon S3 URIs, SageMaker AI registers a model package for each adapter on your behalf and returns its ARN here. This gives you a registered, versioned artifact to deploy with.

The `DeploymentConfiguration` in each recommendation describes the multi-adapter, inference-component-based topology (the base model plus one inference component per adapter). `ExpectedPerformance` reports the benchmarked metrics for that configuration.

The following example shows the adapter-related fields of a `DescribeAIRecommendationJob` response for a job created with Amazon S3 adapters.

```
{
    "AIRecommendationJobName": "my-lora-recommendation-job",
    "AIRecommendationJobStatus": "Completed",
    "AdapterSource": {
        "S3Uris": [
            {"AdapterId": "sql", "S3Uri": "s3://amzn-s3-demo-bucket/adapters/sql/"},
            {"AdapterId": "chat", "S3Uri": "s3://amzn-s3-demo-bucket/adapters/chat/"}
        ]
    },
    "Recommendations": [
        {
            "AdapterDetails": {
                "S3Uris": [
                    {"AdapterId": "sql", "S3Uri": "s3://amzn-s3-demo-bucket/adapters/sql/"},
                    {"AdapterId": "chat", "S3Uri": "s3://amzn-s3-demo-bucket/adapters/chat/"}
                ],
                "ModelPackageArns": [
                    {"AdapterId": "sql", "ModelPackageArn": "arn:aws:sagemaker:us-west-2:111122223333:model-package/my-lora-recommendation-job-adapters/1"},
                    {"AdapterId": "chat", "ModelPackageArn": "arn:aws:sagemaker:us-west-2:111122223333:model-package/my-lora-recommendation-job-adapters/2"}
                ]
            },
            "DeploymentConfiguration": {
                "InstanceType": "ml.g6e.12xlarge",
                "InstanceCount": 1,
                "CopyCountPerInstance": 2,
                "MinCpuMemoryRequiredInMb": 12288,
                "EnvironmentVariables": {
                    "SAGEMAKER_SHM_SIZE_MB": "2048"
                }
            },
            "ExpectedPerformance": [
                {"Metric": "throughput", "Stat": "average", "Value": "512.0", "Unit": "tokens/second"}
            ]
        }
    ]
}
```

To benchmark a deployed multi-adapter endpoint, or to compare adapters against one another, target the inference component for each adapter in your benchmark job. For more information, see [Benchmark multi-LoRA endpoints](generative-ai-inference-recommendations-benchmark.md#generative-ai-inference-recommendations-benchmark-multi-lora).