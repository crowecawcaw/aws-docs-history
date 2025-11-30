# Task Submission with MIG

###### Topics

- [Using Kubernetes YAML](#sagemaker-hyperpod-eks-gpu-partitioning-task-submission-kubectl "#sagemaker-hyperpod-eks-gpu-partitioning-task-submission-kubectl")
- [Using HyperPod CLI](#sagemaker-hyperpod-eks-gpu-partitioning-task-submission-cli "#sagemaker-hyperpod-eks-gpu-partitioning-task-submission-cli")
- [Model Deployment with MIG](#sagemaker-hyperpod-eks-gpu-partitioning-task-submission-deployment "#sagemaker-hyperpod-eks-gpu-partitioning-task-submission-deployment")
- [Using HyperPod CLI](#sagemaker-hyperpod-eks-gpu-partitioning-task-submission-hyperpod-cli "#sagemaker-hyperpod-eks-gpu-partitioning-task-submission-hyperpod-cli")

## Using Kubernetes YAML

```
apiVersion: batch/v1
kind: Job
metadata:
  name: mig-job
  namespace: default
spec:
  template:
    spec:
      containers:
      - name: pytorch
        image: pytorch/pytorch:latest
        resources:
          requests:
            nvidia.com/mig-1g.5gb: 1
            cpu: "100m"
            memory: "128Mi"
          limits:
            nvidia.com/mig-1g.5gb: 1
      restartPolicy: Never
```

## Using HyperPod CLI

Use the HyperPod CLI to deploy JumpStart models with MIG support. The following example demonstrates the new CLI parameters for GPU partitioning:

```
# Deploy JumpStart model with MIG
hyp create hyp-jumpstart-endpoint \
  --model-id deepseek-llm-r1-distill-qwen-1-5b \
  --instance-type ml.p5.48xlarge \
  --accelerator-partition-type mig-2g.10gb \
  --accelerator-partition-validation True \
  --endpoint-name `my-endpoint` \
  --tls-certificate-output-s3-uri s3://`certificate-bucket`/ \
  --namespace default
```

## Model Deployment with MIG

HyperPod Inference allows deploying the models on MIG profiles via Studio Classic, `kubectl` and HyperPod CLI. To deploy JumpStart Models on `kubectl`, CRDs have fields called `spec.server.acceleratorPartitionType` to deploy the model to the desired MIG profile. We run validations to ensure models can be deployed on the MIG profile selected in the CRD. In case you want to disable the MIG validation checks, use `spec.server.validations.acceleratorPartitionValidation` to `False`.

### JumpStart Models

```
apiVersion: inference.sagemaker.aws.amazon.com/v1
kind: JumpStartModel
metadata:
  name: deepseek-model
  namespace: default
spec:
  sageMakerEndpoint:
    name: deepseek-endpoint
  model:
    modelHubName: SageMakerPublicHub
    modelId: deepseek-llm-r1-distill-qwen-1-5b
  server:
    acceleratorPartitionType: mig-7g.40gb
    instanceType: ml.p4d.24xlarge
```

### Deploy model from Amazon S3 using InferenceEndpointConfig

InferenceEndpointConfig allows you to deploy custom model from Amazon S3. To deploy a model on MIG, in `spec.worker.resources` mention MIG profile in `requests` and `limits`. Refer to a simple deployment below:

```
apiVersion: inference.sagemaker.aws.amazon.com/v1
kind: InferenceEndpointConfig
metadata:
  name: custom-model
  namespace: default
spec:
  replicas: 1
  modelName: my-model
  endpointName: my-endpoint
  instanceType: ml.p4d.24xlarge
  modelSourceConfig:
    modelSourceType: s3
    s3Storage:
      bucketName: `my-model-bucket`
      region: `us-east-2`
    modelLocation: `model-path`
  worker:
    resources:
      requests:
        nvidia.com/mig-3g.20gb: 1
        cpu: "5600m"
        memory: "10Gi"
      limits:
        nvidia.com/mig-3g.20gb: 1
```

### Deploy model from FSx for Lustre using InferenceEndpointConfig

InferenceEndpointConfig allows you to deploy custom model from FSx for Lustre. To deploy a model on MIG, in `spec.worker.resources` mention MIG profile in `requests` and `limits`. Refer to a simple deployment below:

```
apiVersion: inference.sagemaker.aws.amazon.com/v1
kind: InferenceEndpointConfig
metadata:
  name: custom-model
  namespace: default
spec:
  replicas: 1
  modelName: my-model
  endpointName: my-endpoint
  instanceType: ml.p4d.24xlarge
  modelSourceConfig:
    modelSourceType: fsx
    fsxStorage:
      fileSystemId: `fs-xxxxx`
    modelLocation: `location-on-fsx`
  worker:
    resources:
      requests:
        nvidia.com/mig-3g.20gb: 1
        cpu: "5600m"
        memory: "10Gi"
      limits:
        nvidia.com/mig-3g.20gb: 1
```

### Using Studio Classic UI

#### Deploying JumpStart Models with MIG

1. Open **Studio Classic** and navigate to **JumpStart**
2. Browse or search for your desired model (e.g., "DeepSeek", "Llama", etc.)
3. Click on the model card and select **Deploy**
4. In the deployment configuration:
   - Choose **HyperPod** as the deployment target
   - Select your MIG-enabled cluster from the dropdown
   - Under **Instance configuration**:
     - Select instance type (e.g., `ml.p4d.24xlarge`)
     - Choose **GPU Partition Type** from available options
     - Configure **Instance count** and **Auto-scaling** settings

5. Review and click **Deploy**
6. Monitor deployment progress in the **Endpoints** section

#### Model Configuration Options

**Endpoint Settings:**

- **Endpoint name** - Unique identifier for your deployment
- **Variant name** - Configuration variant (default: AllTraffic)
- **Instance type** - Must support GPU partition (p series)
- **MIG profile** - GPU partition
- **Initial instance count** - Number of instances to deploy
- **Auto-scaling** - Enable for dynamic scaling based on traffic

**Advanced Configuration:**

- **Model data location** - Amazon S3 path for custom models
- **Container image** - Custom inference container (optional)
- **Environment variables** - Model-specific configurations
- **Amazon VPC configuration** - Network isolation settings

#### Monitoring Deployed Models

1. Navigate to **Studio Classic** > **Deployments** > **Endpoints**
2. Select your MIG-enabled endpoint
3. View metrics including:
   - **MIG utilization** - Per GPU partition usage
   - **Memory consumption** - Per GPU partition
   - **Inference latency** - Request processing time
   - **Throughput** - Requests per second

4. Set up **Amazon CloudWatch alarms** for automated monitoring
5. Configure **auto-scaling policies** based on MIG utilization

## Using HyperPod CLI

### JumpStart Deployment

The HyperPod CLI JumpStart command includes two new fields for MIG support:

- `--accelerator-partition-type` - Specifies the MIG configuration (e.g., mig-4g.20gb)
- `--accelerator-partition-validation` - Validates compatibility between models and MIG profile (default: true)

```
hyp create hyp-jumpstart-endpoint \
  --version 1.1 \
  --model-id deepseek-llm-r1-distill-qwen-1-5b \
  --instance-type ml.p4d.24xlarge \
  --endpoint-name js-test \
  --accelerator-partition-type "mig-4g.20gb" \
  --accelerator-partition-validation true \
  --tls-certificate-output-s3-uri `s3://my-bucket/certs/`
```

### Custom Endpoint Deployment

For deploying via custom endpoint, use the existing fields `--resources-requests` and `--resources-limits` to enable MIG profile functionality:

```
hyp create hyp-custom-endpoint \
  --namespace default \
  --metadata-name deepseek15b-mig-10-14-v2 \
  --endpoint-name deepseek15b-mig-endpoint \
  --instance-type ml.p4d.24xlarge \
  --model-name deepseek15b-mig \
  --model-source-type s3 \
  --model-location deep-seek-15b \
  --prefetch-enabled true \
  --tls-certificate-output-s3-uri s3://`sagemaker-bucket` \
  --image-uri lmcache/vllm-openai:v0.3.7 \
  --container-port 8080 \
  --model-volume-mount-path /opt/ml/model \
  --model-volume-mount-name model-weights \
  --s3-bucket-name `model-storage-123456789` \
  --s3-region us-east-2 \
  --invocation-endpoint invocations \
  --resources-requests '{"cpu":"5600m","memory":"10Gi","nvidia.com/mig-3g.20gb":"1"}' \
  --resources-limits '{"nvidia.com/mig-3g.20gb":"1"}' \
  --env '{
    "OPTION_ROLLING_BATCH":"vllm",
    "SERVING_CHUNKED_READ_TIMEOUT":"480",
    "DJL_OFFLINE":"true",
    "NUM_SHARD":"1",
    "SAGEMAKER_PROGRAM":"inference.py",
    "SAGEMAKER_SUBMIT_DIRECTORY":"/opt/ml/model/code",
    "MODEL_CACHE_ROOT":"/opt/ml/model",
    "SAGEMAKER_MODEL_SERVER_WORKERS":"1",
    "SAGEMAKER_MODEL_SERVER_TIMEOUT":"3600",
    "OPTION_TRUST_REMOTE_CODE":"true",
    "OPTION_ENABLE_REASONING":"true",
    "OPTION_REASONING_PARSER":"deepseek_r1",
    "SAGEMAKER_CONTAINER_LOG_LEVEL":"20",
    "SAGEMAKER_ENV":"1"
  }'
```
