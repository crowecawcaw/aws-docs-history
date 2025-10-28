# Train a PyTorch model

This topic walks you through the process of training a PyTorch model using HyperPod.

In this scenario, let's train a PyTorch model using the `hyp-pytorch-job` template, which simplifies job creation by exposing commonly used parameters.
The model artifacts will be stored in an S3 bucket for later use in inference. However, this is optional, and you can choose your preferred storage location.

## Create a training job

You can train the model using either the CLI or Python SDK.

### Using the CLI

Create a training job with the following command:

```
hyp create hyp-pytorch-job \
    --version 1.0 \
    --job-name test-pytorch-job \
    --image pytorch/pytorch:latest \
    --command '["python", "train.py"]' \
    --args '["--epochs", "10", "--batch-size", "32"]' \
    --environment '{"PYTORCH_CUDA_ALLOC_CONF": "max_split_size_mb:32"}' \
    --pull-policy "IfNotPresent" \
    --instance-type ml.p4d.24xlarge \
    --tasks-per-node 8 \
    --label-selector '{"accelerator": "nvidia", "network": "efa"}' \
    --deep-health-check-passed-nodes-only true \
    --scheduler-type "kueue" \
    --queue-name "training-queue" \
    --priority "high" \
    --max-retry 3 \
    --volumes '["data-vol", "model-vol", "checkpoint-vol"]' \
    --persistent-volume-claims '["shared-data-pvc", "model-registry-pvc"]' \
    --output-s3-uri s3://my-bucket/model-artifacts
```

**Key required parameters explained**:

- `--job-name`: Unique identifier for your training job
- `--image`: Docker image containing your training environment

This command starts a training job named `test-pytorch-job`. The `--output-s3-uri` specifies where the trained model artifacts will be stored,
for example, `s3://my-bucket/model-artifacts`. Note this location, as you’ll need it for deploying the custom model.

### Using the Python SDK

For programmatic control, use the SDK. Create a Python script to launch the same training job.

```

from sagemaker.hyperpod import HyperPodPytorchJob
from sagemaker.hyperpod.job
import ReplicaSpec, Template, Spec, Container, Resources, RunPolicy, Metadata

# Define job specifications
nproc_per_node = "1"  # Number of processes per node
replica_specs =
[
    ReplicaSpec
    (
        name = "pod",  # Replica name
        template = Template
        (
            spec = Spec
            (
                containers =
                [
                    Container
                    (
                        # Container name
                        name="container-name",

                        # Training image
                        image="448049793756.dkr.ecr.us-west-2.amazonaws.com/ptjob:mnist",

                        # Always pull image
                        image_pull_policy="Always",
                        resources=Resources\
                        (
                            # No GPUs requested
                            requests={"nvidia.com/gpu": "0"},
                            # No GPU limit
                            limits={"nvidia.com/gpu": "0"},
                        ),
                        # Command to run
                        command=["python", "train.py"],
                        # Script arguments
                        args=["--epochs", "10", "--batch-size", "32"],
                    )
                ]
            )
        ),
    )
]
# Keep pods after completion
run_policy = RunPolicy(clean_pod_policy="None")

# Create and start the PyTorch job
pytorch_job = HyperPodPytorchJob
(
    # Job name
    metadata = Metadata(name="demo"),
    # Processes per node
    nproc_per_node = nproc_per_node,
    # Replica specifications
    replica_specs = replica_specs,
    # Run policy
    run_policy = run_policy,
    # S3 location for artifacts
    output_s3_uri="s3://my-bucket/model-artifacts"
)
# Launch the job
pytorch_job.create()


```

## Monitor your training job

Monitor your job's progress with these commands:

### Using the CLI

```
# Check job status
hyp list hyp-pytorch-job

# Get detailed information
hyp describe hyp-pytorch-job --job-name test-pytorch-job

# View logs
hyp get-logs hyp-pytorch-job \
    --pod-name test-pytorch-job-pod-0 \
    --job-name test-pytorch-job
```

**Note**: Training time varies based on model complexity and instance type. Monitor the logs to track progress.

These commands help you verify the job’s status and troubleshoot issues. Once the job completes successfully, the model artifacts are saved to
`s3://my-bucket/model-artifacts`.

### Using the Python SDK

Add the following code to your Python script:

```
print("List all pods created for this job:")
print(pytorch_job.list_pods())

print("Check the logs from pod0:")
print(pytorch_job.get_logs_from_pod(pod_name="demo-pod-0"))

print("List all HyperPodPytorchJobs:")
print(HyperPodPytorchJob.list())

print("Describe job:")
print(HyperPodPytorchJob.get(name="demo").model_dump())

pytorch_job.refresh()
print(pytorch_job.status.model_dump())
```

## Next steps

After training, the model artifacts are stored in the S3 bucket you specified (`s3://my-bucket/model-artifacts`). You can use these artifacts to deploy a model.
Currently, you must manually manage the transition from training to inference. This involves:

- **Locating artifacts**: Check the S3 bucket (`s3://my-bucket/model-artifacts`) to confirm the trained model files are present.
- **Recording the path**: Note the exact S3 path (e.g., `s3://my-bucket/model-artifacts/test-pytorch-job/model.tar.gz`) for use in the inference setup.
- **Referencing in deployment**: Provide this S3 path when configuring the custom endpoint to ensure the correct model is loaded.
