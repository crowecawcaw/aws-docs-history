# Deploy custom

fine-tuned models from Amazon S3 and Amazon FSx using kubectl

The following steps show you how to deploy models stored on Amazon S3 or Amazon FSx to a
Amazon SageMaker HyperPod cluster using kubectl.

The following instructions contain code cells and commands designed to run in a
terminal. Ensure you have configured your environment with AWS credentials before
executing these commands.

## Prerequisites

Before you begin, verify that you've:

- Set up inference capabilities on your Amazon SageMaker HyperPod clusters. For
  more information, see [Setting up your
  HyperPod clusters for model deployment](sagemaker-hyperpod-model-deployment-setup.md "sagemaker-hyperpod-model-deployment-setup.md").
- Installed [kubectl](https://kubernetes.io/docs/reference/kubectl/ "https://kubernetes.io/docs/reference/kubectl/") utility and configured [jq](https://jqlang.org/ "https://jqlang.org/") in your terminal.

## Setup and

configuration

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



    ```
    cat <<EOF> deploy_fsx_cluster_inference.yaml
    ---
    apiVersion: inference.sagemaker.aws.amazon.com/v1alpha1
    kind: InferenceEndpointConfig
    metadata:
      name: $SAGEMAKER_ENDPOINT_NAME
      namespace: $CLUSTER_NAMESPACE
    spec:
      endpointName: $SAGEMAKER_ENDPOINT_NAME
      instanceType: $INSTANCE_TYPE
      invocationEndpoint: invocations
      modelName: deepseek15b
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
          requests:
            cpu: 30000m
            memory: 100Gi
            nvidia.com/gpu: 1
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
          requests:
            nvidia.com/gpu: 1
            cpu: 25600m
            memory: 102Gi
        image: 763104351884.dkr.ecr.us-east-2.amazonaws.com/djl-inference:0.32.0-lmi14.0.0-cu124
        modelInvocationPort:
          containerPort: 8080
          name: http
        modelVolumeMount:
          name: model-weights
          mountPath: /opt/ml/model
        environmentVariables:
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
    EOF
    ```

## Deploy your

model from Amazon S3 or Amazon FSx

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

## Verify the

status of your deployment

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

## Manage your

deployment

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
