# Deploy models from Amazon S3, Amazon FSx, or Hugging Face Hub using kubectl

The following steps show you how to deploy models stored on Amazon S3, Amazon FSx, or
Hugging Face Hub to a
Amazon SageMaker HyperPod cluster using kubectl.

The following instructions contain code cells and commands designed to run in a
terminal. Ensure you have configured your environment with AWS credentials before
executing these commands.

## Prerequisites

Before you begin, verify that you've:

- Set up inference capabilities on your Amazon SageMaker HyperPod clusters. For
  more information, see [Setting up your HyperPod clusters for model deployment](sagemaker-hyperpod-model-deployment-setup.md "sagemaker-hyperpod-model-deployment-setup.md").
- Installed [kubectl](https://kubernetes.io/docs/reference/kubectl/ "https://kubernetes.io/docs/reference/kubectl/") utility and configured [jq](https://jqlang.org/ "https://jqlang.org/") in your terminal.

## Setup and configuration

Replace all placeholder values with your actual resource identifiers.

1. Select your Region in your environment.

```
export REGION=<region>
```

2. Initialize your cluster name. This identifies the HyperPod cluster
   where your model will be deployed.

###### Note

Check with your cluster admin to ensure permissions are granted
for this role or user. You can run `!aws sts
 get-caller-identity --query "Arn"` to check which role or
user you are using in your terminal.

```
# Specify your hyperpod cluster name here
HYPERPOD_CLUSTER_NAME="<Hyperpod_cluster_name>"

# NOTE: For sample deployment, we use g5.8xlarge for deepseek-r1 1.5b model which has sufficient memory and GPU
instance_type="ml.g5.8xlarge"
```

3. Initialize your cluster namespace. Your cluster admin should've
   already created a hyperpod-inference service account in your
   namespace.

```
cluster_namespace="<namespace>"
```

4. Create a CRD using one of the following options:

Using Amazon FSx as the model source

    1. Set up a SageMaker endpoint name.



    ```
    export SAGEMAKER_ENDPOINT_NAME="deepseek15b-fsx"
    ```
    2. Configure the Amazon FSx file system ID to be
     used.



    ```
    export FSX_FILE_SYSTEM_ID="fs-1234abcd"
    ```
    3. The following is an example yaml file for creating
     an endpoint with Amazon FSx and a DeepSeek model.


    ###### Note

    For clusters with GPU partitioning enabled, replace `nvidia.com/gpu` with the appropriate MIG resource name such as `nvidia.com/mig-1g.10gb`. For more information, see [Task Submission with MIG](sagemaker-hyperpod-eks-gpu-partitioning-task-submission.md "sagemaker-hyperpod-eks-gpu-partitioning-task-submission.md").



    ```
    cat <<EOF> deploy_fsx_cluster_inference.yaml
    ---
    apiVersion: inference.sagemaker.aws.amazon.com/v1
    kind: InferenceEndpointConfig
    metadata:
      name: lmcache-test
      namespace: inf-update
    spec:
      modelName: Llama-3.1-8B-Instruct
      instanceType: ml.g5.24xlarge
      invocationEndpoint: v1/chat/completions
      replicas: 2
      modelSourceConfig:
        fsxStorage:
          fileSystemId: $FSX_FILE_SYSTEM_ID
        modelLocation: deepseek-1-5b
        modelSourceType: fsx
      worker:
        environmentVariables:
        - name: HF_MODEL_ID
          value: /opt/ml/model
        - name: SAGEMAKER_PROGRAM
          value: inference.py
        - name: SAGEMAKER_SUBMIT_DIRECTORY
          value: /opt/ml/model/code
        - name: MODEL_CACHE_ROOT
          value: /opt/ml/model
        - name: SAGEMAKER_ENV
          value: '1'
        image: 763104351884.dkr.ecr.us-east-2.amazonaws.com/huggingface-pytorch-tgi-inference:2.4.0-tgi2.3.1-gpu-py311-cu124-ubuntu22.04-v2.0
        modelInvocationPort:
          containerPort: 8080
          name: http
        modelVolumeMount:
          mountPath: /opt/ml/model
          name: model-weights
        resources:
          limits:
            nvidia.com/gpu: 1
            # For MIG-enabled instances, use: nvidia.com/mig-1g.10gb: 1
          requests:
            cpu: 30000m
            memory: 100Gi
            nvidia.com/gpu: 1
            # For MIG-enabled instances, use: nvidia.com/mig-1g.10gb: 1
    EOF
    ```

Using Amazon S3 as the model source

    1. Set up a SageMaker endpoint name.



    ```
    export SAGEMAKER_ENDPOINT_NAME="deepseek15b-s3"
    ```
    2. Configure the Amazon S3 bucket location where the model
     is located.



    ```
    export S3_MODEL_LOCATION="deepseek-qwen-1-5b"
    ```
    3. The following is an example yaml file for creating
     an endpoint with Amazon S3 and a DeepSeek model.


    ###### Note

    For clusters with GPU partitioning enabled, replace `nvidia.com/gpu` with the appropriate MIG resource name such as `nvidia.com/mig-1g.10gb`. For more information, see [Task Submission with MIG](sagemaker-hyperpod-eks-gpu-partitioning-task-submission.md "sagemaker-hyperpod-eks-gpu-partitioning-task-submission.md").



    ```
    cat <<EOF> deploy_s3_inference.yaml
    ---
    apiVersion: inference.sagemaker.aws.amazon.com/v1alpha1
    kind: InferenceEndpointConfig
    metadata:
      name: $SAGEMAKER_ENDPOINT_NAME
      namespace: $CLUSTER_NAMESPACE
    spec:
      modelName: deepseek15b
      endpointName: $SAGEMAKER_ENDPOINT_NAME
      instanceType: ml.g5.8xlarge
      invocationEndpoint: invocations
      modelSourceConfig:
        modelSourceType: s3
        s3Storage:
          bucketName: $S3_MODEL_LOCATION
          region: $REGION
        modelLocation: deepseek15b
        prefetchEnabled: true
      worker:
        resources:
          limits:
            nvidia.com/gpu: 1
            # For MIG-enabled instances, use: nvidia.com/mig-1g.10gb: 1
          requests:
            nvidia.com/gpu: 1
            # For MIG-enabled instances, use: nvidia.com/mig-1g.10gb: 1
            cpu: 25600m
            memory: 102Gi
        image: 763104351884.dkr.ecr.us-east-2.amazonaws.com/djl-inference:0.32.0-lmi14.0.0-cu124
        modelInvocationPort:
          containerPort: 8000
          name: http
        modelVolumeMount:
          name: model-weights
          mountPath: /opt/ml/model
        environmentVariables:
          - name: PYTHONHASHSEED
            value: "123"
          - name: OPTION_ROLLING_BATCH
            value: "vllm"
          - name: SERVING_CHUNKED_READ_TIMEOUT
            value: "480"
          - name: DJL_OFFLINE
            value: "true"
          - name: NUM_SHARD
            value: "1"
          - name: SAGEMAKER_PROGRAM
            value: "inference.py"
          - name: SAGEMAKER_SUBMIT_DIRECTORY
            value: "/opt/ml/model/code"
          - name: MODEL_CACHE_ROOT
            value: "/opt/ml/model"
          - name: SAGEMAKER_MODEL_SERVER_WORKERS
            value: "1"
          - name: SAGEMAKER_MODEL_SERVER_TIMEOUT
            value: "3600"
          - name: OPTION_TRUST_REMOTE_CODE
            value: "true"
          - name: OPTION_ENABLE_REASONING
            value: "true"
          - name: OPTION_REASONING_PARSER
            value: "deepseek_r1"
          - name: SAGEMAKER_CONTAINER_LOG_LEVEL
            value: "20"
          - name: SAGEMAKER_ENV
            value: "1"
          - name: MODEL_SERVER_TYPE
            value: "vllm"
          - name: SESSION_KEY
            value: "x-user-id"
    EOF
    ```

Using Amazon S3 as the model source

    1. Set up a SageMaker endpoint name.



    ```
    export SAGEMAKER_ENDPOINT_NAME="deepseek15b-s3"
    ```
    2. Configure the Amazon S3 bucket location where the model
     is located.



    ```
    export S3_MODEL_LOCATION="deepseek-qwen-1-5b"
    ```
    3. The following is an example yaml file for creating
     an endpoint with Amazon S3 and a DeepSeek model.



    ```
    cat <<EOF> deploy_s3_inference.yaml
    ---
    apiVersion: inference.sagemaker.aws.amazon.com/v1
    kind: InferenceEndpointConfig
    metadata:
      name: lmcache-test
      namespace: inf-update
    spec:
      modelName: Llama-3.1-8B-Instruct
      instanceType: ml.g5.24xlarge
      invocationEndpoint: v1/chat/completions
      replicas: 2
      modelSourceConfig:
        modelSourceType: s3
        s3Storage:
          bucketName: bugbash-ada-resources
          region: us-west-2
        modelLocation: models/Llama-3.1-8B-Instruct
        prefetchEnabled: false
      kvCacheSpec:
        enableL1Cache: true
    #    enableL2Cache: true
    #    l2CacheSpec:
    #      l2CacheBackend: redis/sagemaker
    #      l2CacheLocalUrl: redis://redis.redis-system.svc.cluster.local:6379
      intelligentRoutingSpec:
        enabled: true
      tlsConfig:
        tlsCertificateOutputS3Uri: s3://sagemaker-lmcache-fceb9062-tls-6f6ee470
      metrics:
        enabled: true
        modelMetrics:
          port: 8000
      loadBalancer:
        healthCheckPath: /health
      worker:
        resources:
          limits:
            nvidia.com/gpu: "4"
          requests:
            cpu: "6"
            memory: 30Gi
            nvidia.com/gpu: "4"
        image: lmcache/vllm-openai:latest
        args:
          - "/opt/ml/model"
          - "--max-model-len"
          - "20000"
          - "--tensor-parallel-size"
          - "4"
        modelInvocationPort:
          containerPort: 8000
          name: http
        modelVolumeMount:
          name: model-weights
          mountPath: /opt/ml/model
        environmentVariables:
          - name: PYTHONHASHSEED
            value: "123"
          - name: OPTION_ROLLING_BATCH
            value: "vllm"
          - name: SERVING_CHUNKED_READ_TIMEOUT
            value: "480"
          - name: DJL_OFFLINE
            value: "true"
          - name: NUM_SHARD
            value: "1"
          - name: SAGEMAKER_PROGRAM
            value: "inference.py"
          - name: SAGEMAKER_SUBMIT_DIRECTORY
            value: "/opt/ml/model/code"
          - name: MODEL_CACHE_ROOT
            value: "/opt/ml/model"
          - name: SAGEMAKER_MODEL_SERVER_WORKERS
            value: "1"
          - name: SAGEMAKER_MODEL_SERVER_TIMEOUT
            value: "3600"
          - name: OPTION_TRUST_REMOTE_CODE
            value: "true"
          - name: OPTION_ENABLE_REASONING
            value: "true"
          - name: OPTION_REASONING_PARSER
            value: "deepseek_r1"
          - name: SAGEMAKER_CONTAINER_LOG_LEVEL
            value: "20"
          - name: SAGEMAKER_ENV
            value: "1"
          - name: MODEL_SERVER_TYPE
            value: "vllm"
          - name: SESSION_KEY
            value: "x-user-id"
    EOF
    ```

Using Hugging Face Hub as the model source

    1. Create a Kubernetes Secret containing your Hugging Face API token. This token is required for gated models and recommended for all downloads. You can generate a token at [huggingface.co/settings/tokens](https://huggingface.co/settings/tokens "https://huggingface.co/settings/tokens").


    ###### Important

    Deploying models from Hugging Face Hub requires outbound internet access from your cluster nodes to Hugging Face domains including `*.huggingface.co` and `*.hf.co`. Ensure that your VPC networking configuration (NAT gateway, security groups, and network ACLs) allows HTTPS egress to these domains. Without internet access, the model download will fail.


    ###### Note

    For production environments, we recommend using Amazon S3 or Amazon FSx as the model source instead of Hugging Face Hub. With Amazon S3 and Amazon FSx, model artifacts are stored within your AWS account, eliminating the dependency on external internet connectivity and providing more predictable deployment times. Hugging Face Hub is best suited for development, experimentation, and quick prototyping where direct access to the Hugging Face model repository is convenient.



    ```
    kubectl create secret generic hf-token-secret \
      --from-literal=token=hf_YOUR_TOKEN_HERE \
      -n $CLUSTER_NAMESPACE
    ```
    2. Set up a SageMaker endpoint name.



    ```
    export SAGEMAKER_ENDPOINT_NAME="mistral7b-hf"
    ```
    3. The following is an example YAML file for deploying a Mistral 7B model from Hugging Face Hub using vLLM as the inference runtime. With `prefetchEnabled: true`, the operator uses an init container to download the model before the inference container starts.


    ###### Note

    For clusters with GPU partitioning enabled, replace `nvidia.com/gpu` with the appropriate MIG resource name such as `nvidia.com/mig-1g.10gb`. For more information, see [Task Submission with MIG](sagemaker-hyperpod-eks-gpu-partitioning-task-submission.md "sagemaker-hyperpod-eks-gpu-partitioning-task-submission.md").



    ```
    cat <<EOF> deploy_hf_inference.yaml
    ---
    apiVersion: inference.sagemaker.aws.amazon.com/v1
    kind: InferenceEndpointConfig
    metadata:
      name: $SAGEMAKER_ENDPOINT_NAME
      namespace: $CLUSTER_NAMESPACE
    spec:
      modelName: mistral-7b
      modelSourceConfig:
        modelSourceType: huggingface
        prefetchEnabled: true
        huggingFaceModel:
          modelId: "mistralai/Mistral-7B-Instruct-v0.3"
          tokenSecretRef:
            name: hf-token-secret
            key: token
      instanceType: "ml.g5.24xlarge"
      invocationEndpoint: v1/chat/completions
      worker:
        image: "vllm/vllm-openai:v0.10.1"
        modelInvocationPort:
          containerPort: 8000
          name: http
        modelVolumeMount:
          name: model-weights
          mountPath: /opt/ml/model
        resources:
          requests:
            nvidia.com/gpu: "4"
            memory: "96Gi"
            cpu: "16"
          limits:
            nvidia.com/gpu: "4"
            memory: "96Gi"
            cpu: "16"
        args:
          - "--model"
          - "/opt/ml/model"
          - "--port"
          - "8000"
          - "--tensor-parallel-size"
          - "4"
          - "--served-model-name"
          - "mistralai/Mistral-7B-Instruct-v0.3"
        environmentVariables:
          - name: VLLM_REQUEST_TIMEOUT
            value: "600"
    EOF
    ```
    4. The key Hugging Face configuration fields are:




    	* `modelSourceType` (required) — Set to `huggingface`.
    	* `huggingFaceModel.modelId` (required) — The Hugging Face Hub model identifier in `org/model` format (for example, `mistralai/Mistral-7B-Instruct-v0.3`).
    	* `huggingFaceModel.commitSHA` (optional) — A 40-character Git commit SHA to pin a specific model version. If omitted, defaults to the `main` branch.
    	* `huggingFaceModel.tokenSecretRef` (optional) — Reference to a Kubernetes Secret containing your Hugging Face API token. Required for gated models. The token is only used during model download and is not exposed to the inference container.
    	* `prefetchEnabled` (optional) — When `true`, an init container downloads the model before the inference container starts. When `false`, the inference runtime (vLLM, TGI, SGLang) downloads the model natively at startup. Defaults to `false`.

## Configure KV caching and intelligent routing for improved performance

1. Enable KV caching by setting `enableL1Cache` and `enableL2Cache` to `true`.Then, set `l2CacheSpec` to `redis` and update `l2CacheLocalUrl` with the Redis cluster URL.

```
  kvCacheSpec:
    enableL1Cache: true
    enableL2Cache: true
    l2CacheSpec:
      l2CacheBackend: <redis | tieredstorage>
      l2CacheLocalUrl: <redis cluster URL if l2CacheBackend is redis >
```

###### Note

If the redis cluster is not within the same Amazon VPC as the HyperPod cluster, encryption for the data in transit is not guaranteed.

###### Note

Do not need l2CacheLocalUrl if tieredstorage is selected. 2. Enable intelligent routing by setting `enabled` to `true` under `intelligentRoutingSpec`. You can specify which routing strategy to use under `routingStrategy`. If no routing strategy is specified, it defaults to `prefixaware`.

```
intelligentRoutingSpec:
    enabled: true
    routingStrategy: <routing strategy to use>
```

3. Enable router metrics and caching metrics by setting `enabled` to `true` under `metrics`. The `port` value needs to be the same as the `containerPort` value under `modelInvocationPort`.

```
metrics:
    enabled: true
    modelMetrics:
      port: <port value>
    ...
    modelInvocationPort:
      containerPort: <port value>
```

## Deploy your model from Amazon S3, Amazon FSx, or Hugging Face Hub

1. Get the Amazon EKS cluster name from the HyperPod cluster ARN for
   kubectl authentication.

```
export EKS_CLUSTER_NAME=$(aws --region $REGION sagemaker describe-cluster --cluster-name $HYPERPOD_CLUSTER_NAME \
  --query 'Orchestrator.Eks.ClusterArn' --output text | \
  cut -d'/' -f2)
aws eks update-kubeconfig --name $EKS_CLUSTER_NAME --region $REGION
```

2. Deploy your InferenceEndpointConfig model with one of the following
   options:

Deploy with Amazon FSx as a source

```
kubectl apply -f deploy_fsx_luster_inference.yaml
```

Deploy with Amazon S3 as a source

```
kubectl apply -f deploy_s3_inference.yaml
```

Deploy with Hugging Face Hub as a source

```
kubectl apply -f deploy_hf_inference.yaml
```

If the deployment fails, check the InferenceEndpointConfig events for diagnostic information. For common issues such as token errors, network connectivity, and model not found, see [Hugging Face Hub model deployment failures](sagemaker-hyperpod-model-deployment-ts-huggingface.md "sagemaker-hyperpod-model-deployment-ts-huggingface.md").

## Verify the status of your deployment

1. Check if the model successfully deployed.

```
kubectl describe InferenceEndpointConfig $SAGEMAKER_ENDPOINT_NAME -n $CLUSTER_NAMESPACE
```

2. Check that the endpoint is successfully created.

```
kubectl describe SageMakerEndpointRegistration $SAGEMAKER_ENDPOINT_NAME -n $CLUSTER_NAMESPACE
```

3. Test the deployed endpoint to verify it's working correctly. This step
   confirms that your model is successfully deployed and can process
   inference requests.

```
aws sagemaker-runtime invoke-endpoint \
  --endpoint-name $SAGEMAKER_ENDPOINT_NAME \
  --content-type "application/json" \
  --body '{"inputs": "What is AWS SageMaker?"}' \
  --region $REGION \
  --cli-binary-format raw-in-base64-out \
  /dev/stdout
```

## Manage your deployment

When you're finished testing your deployment, use the following commands to
clean up your resources.

###### Note

Verify that you no longer need the deployed model or stored data before
proceeding.

###### Clean up your resources

1. Delete the inference deployment and associated Kubernetes resources.
   This stops the running model containers and removes the SageMaker
   endpoint.

```
kubectl delete inferenceendpointconfig $SAGEMAKER_ENDPOINT_NAME -n $CLUSTER_NAMESPACE
```

2. Verify the cleanup was done successfully.

```
# # Check that Kubernetes resources are removed
kubectl get pods,svc,deployment,InferenceEndpointConfig,sagemakerendpointregistration -n $CLUSTER_NAMESPACE
```

```
# Verify SageMaker endpoint is deleted (should return error or empty)
aws sagemaker describe-endpoint --endpoint-name $SAGEMAKER_ENDPOINT_NAME --region $REGION
```

###### Troubleshooting

Use these debugging commands if your deployment isn't working as
expected.

1. Check the Kubernetes deployment status.

```
kubectl describe deployment $SAGEMAKER_ENDPOINT_NAME -n $CLUSTER_NAMESPACE
```

2. Check the InferenceEndpointConfig status to see the high-level
   deployment state and any configuration issues.

```
kubectl describe InferenceEndpointConfig $SAGEMAKER_ENDPOINT_NAME -n $CLUSTER_NAMESPACE
```

3. Check status of all Kubernetes objects. Get a comprehensive view of
   all related Kubernetes resources in your namespace. This gives you a
   quick overview of what's running and what might be missing.

```
kubectl get pods,svc,deployment,InferenceEndpointConfig,sagemakerendpointregistration -n $CLUSTER_NAMESPACE
```
