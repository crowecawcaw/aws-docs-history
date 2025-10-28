# Deploy

models from JumpStart using kubectl

The following steps show you how to deploy a JumpStart model to a
HyperPod cluster using kubectl.

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

1. Select your Region.

```
export REGION=<region>
```

2. View all SageMaker public hub models and HyperPod clusters.
3. Select a `JumpstartModel` from JumpstartPublic Hub.
   JumpstartPublic hub has a large number of models available so you can
   use `NextToken` to iteratively list all available models in
   the public hub.

```
aws sagemaker list-hub-contents --hub-name SageMakerPublicHub --hub-content-type Model --query '{Models: HubContentSummaries[].{ModelId:HubContentName,Version:HubContentVersion}, NextToken: NextToken}' --output json
```

```
export MODEL_ID="deepseek-llm-r1-distill-qwen-1-5b"
export MODEL_VERSION="2.0.4"
```

4. Configure the model ID and cluster name you’ve selected into the
   variables below.

###### Note

Check with your cluster admin to ensure permissions are granted
for this role or user. You can run `!aws sts
 get-caller-identity --query "Arn"` to check which role or
user you are using in your terminal.

```
aws sagemaker list-clusters --output table

# Select the cluster name where you want to deploy the model.
export HYPERPOD_CLUSTER_NAME="<insert cluster name here>"

# Select the instance that is relevant for your model deployment and exists within the selected cluster.
# List availble instances in your HyperPod cluster
aws sagemaker describe-cluster --cluster-name=$HYPERPOD_CLUSTER_NAME --query "InstanceGroups[].{InstanceType:InstanceType,Count:CurrentCount}" --output table

# List supported instance types for the selected model
aws sagemaker describe-hub-content --hub-name SageMakerPublicHub --hub-content-type Model --hub-content-name "$MODEL_ID" --output json | jq -r '.HubContentDocument | fromjson | {Default: .DefaultInferenceInstanceType, Supported: .SupportedInferenceInstanceTypes}'


# Select and instance type from the cluster that is compatible with the model.
# Make sure that the selected instance is either default or supported instance type for the jumpstart model
export INSTANCE_TYPE="<Instance_type_In_cluster"
```

5. Confirm with the cluster admin which namespace you are permitted to
   use. The admin should have created a `hyperpod-inference`
   service account in your namespace.

```
export CLUSTER_NAMESPACE="default"
```

6. Set a name for endpoint and custom object to be create.

```
export SAGEMAKER_ENDPOINT_NAME="deepsek-qwen-1-5b-test"
```

7. The following is an example for a
   `deepseek-llm-r1-distill-qwen-1-5b` model deployment from
   Jumpstart. Create a similar deployment yaml file based on the model
   selected iin the above step.

```
cat << EOF > jumpstart_model.yaml
---
apiVersion: inference.sagemaker.aws.amazon.com/v1alpha1
kind: JumpStartModel
metadata:
  name: $SAGEMAKER_ENDPOINT_NAME
  namespace: $CLUSTER_NAMESPACE
spec:
  sageMakerEndpoint:
    name: $SAGEMAKER_ENDPOINT_NAME
  model:
    modelHubName: SageMakerPublicHub
    modelId: $MODEL_ID
    modelVersion: $MODEL_VERSION
  server:
    instanceType: $INSTANCE_TYPE
  metrics:
    enabled: true
  environmentVariables:
    - name: SAMPLE_ENV_VAR
      value: "sample_value"
  maxDeployTimeInSeconds: 1800
  autoScalingSpec:
    cloudWatchTrigger:
      name: "SageMaker-Invocations"
      namespace: "AWS/SageMaker"
      useCachedMetrics: false
      metricName: "Invocations"
      targetValue: 10
      minValue: 0.0
      metricCollectionPeriod: 30
      metricStat: "Sum"
      metricType: "Average"
      dimensions:
        - name: "EndpointName"
          value: "$SAGEMAKER_ENDPOINT_NAME"
        - name: "VariantName"
          value: "AllTraffic"
EOF
```

## Deploy your model

###### Update your kubernetes configuration and deploy your model

1. Configure kubectl to connect to the HyperPod cluster
   orchestrated by Amazon EKS.

```
export EKS_CLUSTER_NAME=$(aws --region $REGION sagemaker describe-cluster --cluster-name $HYPERPOD_CLUSTER_NAME \
  --query 'Orchestrator.Eks.ClusterArn' --output text | \
  cut -d'/' -f2)
aws eks update-kubeconfig --name $EKS_CLUSTER_NAME --region $REGION
```

2. Deploy your JumpStart model.

```
kubectl apply -f jumpstart_model.yaml
```

###### Monitor the status of your model deployment

1. Verify that the model is successfully deployed.

```
kubectl describe JumpStartModel $SAGEMAKER_ENDPOINT_NAME -n $CLUSTER_NAMESPACE
```

2. Verify that the endpoint is successfully created.

```
aws sagemaker describe-endpoint --endpoint-name=$SAGEMAKER_ENDPOINT_NAME --output table
```

3. Invoke your model endpoint. You can programmatically retrieve example
   payloads from the `JumpStartModel` object.

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

Delete your JumpStart model deployment once you no longer need it.

```
kubectl delete JumpStartModel $SAGEMAKER_ENDPOINT_NAME -n $CLUSTER_NAMESPACE
```

###### Troubleshooting

Use these debugging commands if your deployment isn't working as
expected.

1. Check the status of Kubernetes deployment. This command inspects the
   underlying Kubernetes deployment object that manages the pods running
   your model. Use this to troubleshoot pod scheduling, resource
   allocation, and container startup issues.

```
kubectl describe deployment $SAGEMAKER_ENDPOINT_NAME -n $CLUSTER_NAMESPACE
```

2. Check the status of your JumpStart model resource. This command
   examines the custom `JumpStartModel` resource that manages
   the high-level model configuration and deployment lifecycle. Use this to
   troubleshoot model-specific issues like configuration errors or SageMaker AI
   endpoint creation problems.

```
kubectl describe JumpStartModel $SAGEMAKER_ENDPOINT_NAME -n $CLUSTER_NAMESPACE
```

3. Check the status of all Kubernetes objects. This command provides a
   comprehensive overview of all related Kubernetes resources in your
   namespace. Use this for a quick health check to see the overall state of
   pods, services, deployments, and custom resources associated with your
   model deployment.

```
kubectl get pods,svc,deployment,JumpStartModel,sagemakerendpointregistration -n $CLUSTER_NAMESPACE
```
