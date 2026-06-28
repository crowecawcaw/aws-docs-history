# Restricted Model Packages

## What is a Restricted Model Package?

A Restricted Model Package (RMP) is a SageMaker AI Model Package that wraps
proprietary model artifacts in secure, service-managed storage that is not
directly accessible to customers. RMPs allow you to authorize and control usage
of these models through IAM policies without granting direct access to the
underlying artifacts. Model data cannot be downloaded, exported, or viewed
directly. It can only be used within authorized AWS services. RMPs can only be
created by trusted SageMaker AI platform principals and exist within Model Package Groups
marked with `StorageType: "Restricted"`.

RMPs are produced today by multi-turn reinforcement learning (MTRL) training
on SageMaker Training Jobs Serverless. Once an RMP exists, you can use its ARN to
evaluate the underlying model. Using an RMP as input to a subsequent training
job — for example, to chain MTRL runs into an iterative training workflow — is
planned for Q3 2026.

RMPs differ from standard SageMaker AI Model Packages in that the underlying model
artifacts remain in secure, service-managed storage at all times. Customers
interact with the model through its ARN rather than accessing the checkpoint
files directly in Amazon S3.

## Supported use cases

The following table summarizes which RMP use cases are available today and
which are planned for future releases.

| Use case                                                                                                              | Availability        |
| --------------------------------------------------------------------------------------------------------------------- | ------------------- |
| Training output — receive an RMP as the trained model artifact from an MTRL training job                              | Generally available |
| Evaluation input — reference an RMP as the model under evaluation                                                     | Generally available |
| Training input — use an RMP as the source model for a subsequent training job (for example, iterative MTRL workflows) | Q3 2026             |

## MTRL training output

When you train a model using multi-turn reinforcement learning (MTRL) on SageMaker
Training Jobs Serverless, the training output is delivered as an RMP rather than
an Amazon S3 checkpoint path. The output RMP is automatically created and registered
in the Model Package Group you specify when configuring the runtime manager. You
do not create RMPs directly — they are produced by the platform as training job
outputs.

The `model_package_group_name` parameter is required when
running MTRL on SageMaker Training Jobs Serverless. You must specify an existing
Model Package Group with `StorageType: "Restricted"` where the
output RMP will be registered. Without this parameter, the training job will
fail. Configure the runtime with a `model_package_group_name` to
receive the training output:

```
from amzn_nova_forge.manager.runtime_manager import SMTJServerlessRuntimeManager
from amzn_nova_forge.trainer.forge_trainer import ForgeTrainer
from amzn_nova_forge.model.model_enums import Model, TrainingMethod
from amzn_nova_forge.core import ForgeConfig

# Configure runtime with the output Model Package Group
runtime = SMTJServerlessRuntimeManager(
    model_package_group_name="my-rmp-model-package-group",  # Required for MTRL
    execution_role="arn:aws:iam::123456789012:role/my-role",
    agent_core_arn="arn:aws:bedrock-agentcore:us-east-1:123456789012:runtime/my-agent",  # AgentCore runtime for MTRL execution
)

# Train with MTRL
trainer = ForgeTrainer(
    model=Model.NOVA_LITE_2,
    method=TrainingMethod.RFT_MULTITURN_LORA,
    infra=runtime,
    training_data_s3_path="s3://your-bucket/prompts/train.parquet",
    config=ForgeConfig(output_s3_path="s3://your-bucket/output/"),
)

result = trainer.train(job_name="my-mtrl-job")

# Wait for completion and retrieve the output RMP ARN
result.wait()
print(result.model_artifacts.output_model_arn)
```

After training completes, the resulting model is registered as a new version
in the specified Model Package Group.

## Using an RMP for evaluation

You can evaluate a model stored as an RMP by referencing its ARN. The SageMaker AI
platform resolves the RMP to the underlying model artifacts internally, so your
evaluation workflow does not need to handle the model checkpoint directly.

For details on running evaluations against Amazon Nova models, see [Evaluating your SageMaker AI-trained model](nova-model-evaluation.md "nova-model-evaluation.md").

## Using an RMP as training input (Q3 2026)

Using an RMP as the source model for a training job is planned for Q3 2026
and is not available today. Once supported, you will be able to specify an RMP
ARN as the source model using `ModelPackageConfig.SourceModelPackageArn`.
The SageMaker AI platform will resolve the ARN to the actual model checkpoint
internally, so your training code will receive the model artifacts as if they
were loaded from Amazon S3.

This will enable iterative MTRL training workflows where the output RMP from
one training job can be passed as the source model to a subsequent MTRL job,
allowing each run to build on the output of the previous one without ever
exposing the underlying model checkpoint.
