

# Deploy models with Managed NVIDIA Dynamo on HyperPod

NVIDIA Dynamo is an open-source inference framework that runs on top of engines such as vLLM, SGLang, and TensorRT-LLM and coordinates them across GPUs and nodes. It's built for large language models that are too big or too costly to run efficiently on a single worker. It helps you use GPUs more efficiently, reduce time to first token by reusing cached context, and serve models larger than one instance. For more information, see the [NVIDIA Dynamo documentation](https://docs.nvidia.com/dynamo/) on the NVIDIA website.

Amazon SageMaker HyperPod Inference now supports NVIDIA Dynamo as a serving runtime for large-model inference. When you add a `dynamoSpec` to an `InferenceEndpointConfig`, the inference operator translates it into a `DynamoGraphDeployment` (DGD), the Dynamo custom resource that defines the frontend and workers. The Dynamo operator then runs the DGD. The inference operator continues to manage model storage, endpoint registration, TLS, and status. Dynamo provides two serving modes:
+ **Aggregated serving**: Each worker runs both prefill and decode. A worker can span multiple nodes when the model is too large for one node.
+ **Disaggregated serving**: Prefill and decode run in separate worker pools that you size and scale independently. The key-value (KV) cache moves from prefill workers to decode workers over the [NVIDIA Inference Xfer Library (NIXL)](https://github.com/ai-dynamo/nixl) (on the GitHub website).

A Dynamo frontend exposes an OpenAI-compatible HTTP API and routes each request to a worker. You choose how the frontend picks a worker with the `routingMode` setting: `kv-aware` (default) routes each request to the worker with the best KV cache overlap for it, `round-robin` cycles through workers, and `random` picks a worker at random.

## What HyperPod manages
<a name="sagemaker-hyperpod-model-deployment-dynamo-managed"></a>

You choose the model, the serving mode, and how many nodes each worker uses. HyperPod manages the rest:
+ **Installation and upgrades**: The HyperPod inference add-on installs the Dynamo operator, Grove, and the KAI scheduler together, and upgrades them together. For more information, see [Grove](https://github.com/ai-dynamo/grove) and [KAI Scheduler](https://github.com/NVIDIA/KAI-Scheduler) on the GitHub website. You don't install or upgrade Helm charts yourself.
+ **Runtime images**: AWS Deep Learning Containers provides Dynamo runtime images for vLLM, SGLang, and TensorRT-LLM, including Elastic Fabric Adapter (EFA) images for multi-node workers.
+ **Deployment**: With `dynamoSpec`, the inference operator generates the `DynamoGraphDeployment` and sets the EFA and KV transfer settings from the instance type.
+ **Endpoint and scaling**: The inference operator creates the load balancer and TLS certificate, optionally registers a SageMaker AI endpoint, and autoscales workers with Kubernetes Event-driven Autoscaling (KEDA). For more information, see [Autoscaling policies for your HyperPod inference model deployment](sagemaker-hyperpod-model-deployment-autoscaling.md).
+ **Infrastructure**: HyperPod monitors node health and replaces faulty nodes.

If you create a `DynamoGraphDeployment` directly, the add-on still installs and upgrades Dynamo, but you set up the endpoint and scaling yourself.

## Steps to deploy a model
<a name="sagemaker-hyperpod-model-deployment-dynamo-steps"></a>

To deploy a model with Dynamo, complete these steps in order:

1. [Step 1: Complete the prerequisites](#sagemaker-hyperpod-model-deployment-dynamo-prereqs)

1. [Step 2: Choose a deployment approach](#sagemaker-hyperpod-model-deployment-dynamo-approach)

1. [Step 3: Install or upgrade the add-on with Dynamo](#sagemaker-hyperpod-model-deployment-dynamo-addon)

1. [Step 4: Deploy a model](#sagemaker-hyperpod-model-deployment-dynamo-deploy)

1. [Step 5: Verify your deployment](#sagemaker-hyperpod-model-deployment-dynamo-verify)

## Step 1: Complete the prerequisites
<a name="sagemaker-hyperpod-model-deployment-dynamo-prereqs"></a>

Before you deploy a model with Dynamo, make sure that you have the following:
+ An Amazon SageMaker HyperPod cluster orchestrated by Amazon EKS. To create one, see [Create an EKS-orchestrated SageMaker HyperPod cluster](sagemaker-hyperpod-quickstart.md#sagemaker-hyperpod-quickstart-eks).
+ GPU instances for your workers. Multi-node workers require instance types with EFA devices. For how KV transfer works on each instance type with disaggregated serving, see [KV transfer path by instance type](#sagemaker-hyperpod-model-deployment-dynamo-kv).
+ A Dynamo runtime image for your `modelServer` from the same release as the Dynamo platform that the add-on installs (1.6.2). AWS Deep Learning Containers provides these images in the [Amazon ECR Public Gallery](https://gallery.ecr.aws/deep-learning-containers/dynamo). Use the EFA image when any worker runs on an instance type with EFA devices, which is required for multi-node workers. `worker.image` sets one image for the frontend and every worker, so if prefill and decode run on different instance types, use the EFA image when either role uses EFA.

  The following table lists the standard and EFA runtime images for each model server.


<table>
<thead>
  <tr><th><code>modelServer</code></th><th>Standard image</th><th>EFA image</th></tr>
</thead>
<tbody>
  <tr><td><code>vllm</code></td><td><code>public.ecr.aws/deep-learning-containers/dynamo:1.6.2-vllm-runtime-v1</code></td><td><code>public.ecr.aws/deep-learning-containers/dynamo:1.6.2-efa-vllm-runtime-v1</code></td></tr>
  <tr><td><code>sglang</code></td><td><code>public.ecr.aws/deep-learning-containers/dynamo:1.6.2-sglang-runtime-v1</code></td><td><code>public.ecr.aws/deep-learning-containers/dynamo:1.6.2-efa-sglang-runtime-v1</code></td></tr>
  <tr><td><code>trtllm</code></td><td><code>public.ecr.aws/deep-learning-containers/dynamo:1.6.2-trtllm-runtime-v1</code></td><td><code>public.ecr.aws/deep-learning-containers/dynamo:1.6.2-efa-trtllm-runtime-v1</code></td></tr>
</tbody>
</table>


  You can also use the NVIDIA GPU Cloud (NGC) images from the same release, such as `nvcr.io/nvidia/ai-dynamo/vllm-runtime:1.6.2` and `nvcr.io/nvidia/ai-dynamo/vllm-runtime:1.6.2-efa`.

**Step 1 is complete when:** `kubectl get nodes -L node.kubernetes.io/instance-type` lists nodes of the GPU instance type that you plan to use.

## Step 2: Choose a deployment approach
<a name="sagemaker-hyperpod-model-deployment-dynamo-approach"></a>

You can deploy a model with Dynamo in two ways:
+ **`InferenceEndpointConfig` with `dynamoSpec`**: An `InferenceEndpointConfig` is the HyperPod inference resource that describes a model endpoint. Add a `dynamoSpec` block to serve the model with Dynamo. The inference operator generates the Dynamo resources and manages the endpoint for you. Use this approach for most deployments.
+ **`DynamoGraphDeployment` (DGD)**: A DGD is the NVIDIA Dynamo resource that describes the full serving graph: the frontend and every worker. You write it and apply it yourself. The add-on's Dynamo operator runs it, but the inference operator doesn't manage it. Use this approach if you already have DGD manifests, or if you need settings that `dynamoSpec` doesn't currently support.

The following table compares what each deployment approach manages.


| Capability | `InferenceEndpointConfig` with `dynamoSpec` | `DynamoGraphDeployment` | 
| --- | --- | --- | 
| Model download, endpoint registration, load balancer, and TLS | Managed | You set these up | 
| Autoscaling | Managed | You set these up | 
| EFA and KV transfer settings | Set from the instance type | You configure them | 

Engine arguments, per-role instance types, `nodeAffinity`, and probes are configurable with `dynamoSpec`. For settings that `dynamoSpec` ignores, see [Compatibility and limitations](#sagemaker-hyperpod-model-deployment-dynamo-limitations).

**Note**  
You can't add or remove `dynamoSpec` on an existing `InferenceEndpointConfig`. To make this change, delete and recreate the resource.

**Step 2 is complete when:** you've chosen either an `InferenceEndpointConfig` with `dynamoSpec` or a `DynamoGraphDeployment`.

## Step 3: Install or upgrade the add-on with Dynamo
<a name="sagemaker-hyperpod-model-deployment-dynamo-addon"></a>

Dynamo is installed through the Amazon SageMaker HyperPod inference add-on (`amazon-sagemaker-hyperpod-inference`). Add-on version v3.0.0-eksbuild.1 installs the Dynamo operator 1.6.2 together with Grove and the KAI scheduler.

When you install the add-on from the SageMaker AI console, Dynamo is installed by default. When you install or update the add-on with the AWS CLI, Dynamo is installed only if you set `"dynamo": { "enabled": true }` in the add-on configuration values. Before you enable it, review [Security considerations](#sagemaker-hyperpod-model-deployment-dynamo-security). Dynamo endpoints rely on network policy to restrict traffic to their pods, and the Dynamo operator runs with cluster-wide permissions.

**To check whether Dynamo is installed**

```
aws eks describe-addon \
    --cluster-name $EKS_CLUSTER_NAME \
    --addon-name amazon-sagemaker-hyperpod-inference \
    --region $REGION \
    --query "addon.{Version:addonVersion,Status:status,Config:configurationValues}"
```

Dynamo is installed when the status is `ACTIVE`, the version is v3.0.0-eksbuild.1 or later, and the configuration values include `"dynamo": { "enabled": true }`. If so, continue to [Step 4: Deploy a model](#sagemaker-hyperpod-model-deployment-dynamo-deploy).

If the cluster doesn't have the add-on, install it as described in [Setting up your HyperPod clusters for model deployment](sagemaker-hyperpod-model-deployment-setup.md), and include `"dynamo": { "enabled": true }` in the configuration values.

**To enable Dynamo or upgrade the add-on**

1. Save the current add-on configuration values to a file. `--resolve-conflicts OVERWRITE` replaces the existing configuration with the values that you pass, so start from your current values.

   ```
   aws eks describe-addon \
       --cluster-name $EKS_CLUSTER_NAME \
       --addon-name amazon-sagemaker-hyperpod-inference \
       --region $REGION \
       --query addon.configurationValues \
       --output text > addon-config.json
   ```

1. Add the `dynamo` setting to `addon-config.json` and keep your existing values:

   ```
   {
     "executionRoleArn": "arn:aws:iam::{{ACCOUNT_ID}}:role/{{ROLE_NAME}}",
     "tlsCertificateS3Bucket": "{{BUCKET_NAME}}",
     "inferenceOperator": { "enabled": true },
     "dynamo": { "enabled": true }
   }
   ```

1. Find the latest add-on version for your cluster. Replace {{KUBERNETES\_VERSION}} with your cluster's Kubernetes version, which `aws eks describe-cluster --name $EKS_CLUSTER_NAME --query cluster.version` returns.

   ```
   aws eks describe-addon-versions \
       --addon-name amazon-sagemaker-hyperpod-inference \
       --kubernetes-version {{KUBERNETES_VERSION}} \
       --query "addons[0].addonVersions[].addonVersion" \
       --region $REGION
   ```

1. Update the add-on. Replace {{ADDON\_VERSION}} with the version from the previous step.

   ```
   aws eks update-addon \
       --cluster-name $EKS_CLUSTER_NAME \
       --addon-name amazon-sagemaker-hyperpod-inference \
       --addon-version {{ADDON_VERSION}} \
       --configuration-values file://addon-config.json \
       --resolve-conflicts OVERWRITE \
       --region $REGION
   ```

The inference operator reports the `DynamoOperatorNotInstalled` failure reason until the Dynamo operator is available. To upgrade later, run this procedure again with a newer add-on version. The add-on upgrades the Dynamo operator, Grove and the KAI scheduler together.

**To remove Dynamo or the add-on**, delete your Dynamo endpoints and DGDs first. To remove only Dynamo, follow the procedure above with `"dynamo": { "enabled": false }`. To remove the add-on, run the following command.

```
aws eks delete-addon \
    --cluster-name $EKS_CLUSTER_NAME \
    --addon-name amazon-sagemaker-hyperpod-inference \
    --region $REGION
```

**Step 3 is complete when:** the add-on status is `ACTIVE` on version v3.0.0-eksbuild.1 or later, its configuration values include `"dynamo": { "enabled": true }`, and the following command returns both resource definitions.

```
kubectl get crd inferenceendpointconfigs.inference.sagemaker.aws.amazon.com \
    dynamographdeployments.nvidia.com
```

## Step 4: Deploy a model
<a name="sagemaker-hyperpod-model-deployment-dynamo-deploy"></a>

This step deploys with an `InferenceEndpointConfig`. To deploy a DGD instead, see [Deploy a DynamoGraphDeployment](#sagemaker-hyperpod-model-deployment-dynamo-dgd) at the end of this step.

`dynamoSpec` is an optional `InferenceEndpointConfig` field that deploys your model with Dynamo. It sets the inference engine (`modelServer`: `vllm`, `sglang`, or `trtllm`), the request router (`frontend`), and the serving mode: specify exactly one of `aggregation` or `disaggregation`. All other `InferenceEndpointConfig` fields work as they do for other endpoints. The inference operator sets each worker's GPU count from `tensorParallelism`, `dataParallelism`, and any pipeline-parallel size in `args`, so don't set `nvidia.com/gpu` in `worker.resources`.

### Aggregated serving
<a name="sagemaker-hyperpod-model-deployment-dynamo-aggregated"></a>

The following example deploys one aggregated worker from a Hugging Face model. Replace {{ENDPOINT\_NAME}}, {{HUGGING\_FACE\_MODEL\_ID}}, and {{SECRET\_NAME}} with your own values.

```
apiVersion: inference.sagemaker.aws.amazon.com/v1
kind: InferenceEndpointConfig
metadata:
  name: {{ENDPOINT_NAME}}
  namespace: default
spec:
  modelName: {{ENDPOINT_NAME}}
  endpointName: {{ENDPOINT_NAME}}
  instanceType: ml.p5.48xlarge
  invocationEndpoint: v1/chat/completions
  modelSourceConfig:
    modelSourceType: huggingface
    huggingFaceModel:
      modelId: {{HUGGING_FACE_MODEL_ID}}
      tokenSecretRef:
        name: {{SECRET_NAME}}
        key: token
  dynamoSpec:
    modelServer: vllm
    aggregation:
      tensorParallelism: 8
  worker:
    image: public.ecr.aws/deep-learning-containers/dynamo:1.6.2-efa-vllm-runtime-v1
    modelInvocationPort:
      containerPort: 8000
    modelVolumeMount:
      name: model-weights
    resources: {}
  autoScalingSpec:
    minReplicaCount: 1
    maxReplicaCount: 4
    cloudWatchTrigger:
      name: invocations
      namespace: AWS/SageMaker
      metricName: Invocations
      dimensions:
      - name: EndpointName
        value: {{ENDPOINT_NAME}}
      metricStat: Sum
      targetValue: 100
```

Save the manifest to a file, for example `endpoint.yaml`, and apply it:

```
kubectl apply -f endpoint.yaml
```

The `autoScalingSpec` block is optional. It scales the number of workers with the SageMaker AI endpoint's `Invocations` metric, so the example sets `endpointName`. You can also scale on a Prometheus query with `prometheusTrigger`, or combine several triggers with `cloudWatchTriggerList` and `prometheusTriggerList`. `minReplicaCount` must be 1 or greater.

You can also load the model from Amazon S3 (`modelSourceType: s3`), Amazon FSx (`modelSourceType: fsx`), or a Kubernetes volume (`modelSourceType: kubernetesVolume`).

To run more than one aggregated worker, set `spec.replicas`. Each replica is a full copy of the model.

The inference operator also creates a frontend pod for each endpoint. The frontend needs no GPUs, and Kubernetes schedules it on any node with capacity, including CPU nodes. You don't set an instance type for it. To serve a model that doesn't fit on one node, see [Multi-node serving](#sagemaker-hyperpod-model-deployment-dynamo-multinode).

### Disaggregated serving
<a name="sagemaker-hyperpod-model-deployment-dynamo-disaggregated"></a>

The following example runs one prefill worker and one decode worker. Each role has its own replica count and parallelism, so you can size the roles independently.

```
  dynamoSpec:
    modelServer: vllm
    frontend:
      routingMode: kv-aware
    disaggregation:
      prefill:
        replicas: 1
        tensorParallelism: 4
      decode:
        replicas: 1
        tensorParallelism: 4
```

**Note**  
Each role must have enough GPUs on its instance type to hold the full model at its configured tensor parallelism. In this example, each role needs an instance type with at least 4 GPUs. A prefill role and a decode role are placed on separate pods. Use `instanceType` under a role to place it on a different instance type from the endpoint default.

Replace the `dynamoSpec` block in the aggregated example with this one, and remove the endpoint-level `autoScalingSpec`. To autoscale a disaggregated endpoint, set `autoScalingSpec` under `prefill` and `decode` instead.

Save the manifest to a file, for example `endpoint.yaml`, and apply it:

```
kubectl apply -f endpoint.yaml
```

### Multi-node serving
<a name="sagemaker-hyperpod-model-deployment-dynamo-multinode"></a>

The following example runs one aggregated worker that spans two `ml.p5.48xlarge` nodes (8 GPUs each) with a total tensor parallelism of 16. Dynamo gang-schedules the nodes of a worker together, so either every node of the worker is placed or none are. Replace the placeholder values as in the aggregated example.

```
apiVersion: inference.sagemaker.aws.amazon.com/v1
kind: InferenceEndpointConfig
metadata:
  name: {{ENDPOINT_NAME}}
  namespace: default
spec:
  modelName: {{ENDPOINT_NAME}}
  instanceType: ml.p5.48xlarge
  invocationEndpoint: v1/chat/completions
  maxDeployTimeInSeconds: 3600
  modelSourceConfig:
    modelSourceType: huggingface
    huggingFaceModel:
      modelId: {{HUGGING_FACE_MODEL_ID}}
      tokenSecretRef:
        name: {{SECRET_NAME}}
        key: token
  dynamoSpec:
    modelServer: vllm
    aggregation:
      nodesPerReplica: 2
      tensorParallelism: 16
  worker:
    image: public.ecr.aws/deep-learning-containers/dynamo:1.6.2-efa-vllm-runtime-v1
    modelInvocationPort:
      containerPort: 8000
    modelVolumeMount:
      name: model-weights
    resources: {}
```

`tensorParallelism` is the tensor parallelism degree of the worker. To add pipeline parallelism, pass the engine's pipeline-parallel flag in `args`, for example `--pipeline-parallel-size 2` for vLLM. Each worker then uses `tensorParallelism` × pipeline-parallel size GPUs, which must divide evenly across `nodesPerReplica` nodes. In this example, without pipeline parallelism, each of the 2 nodes provides 8 of the 16 GPUs. You can't combine pipeline parallelism with `dataParallelism`.

Multi-node workers require an instance type with EFA devices. The inference operator rejects the configuration for an instance type without them. The operator adds the EFA devices and the settings that cross-node communication needs, so use the EFA runtime image.

If you leave `nodesPerReplica` at 1 and the worker needs more GPUs than one node has (`tensorParallelism` times any pipeline-parallel size), the operator sets `nodesPerReplica` to that GPU count divided by the GPUs per node. Set `nodesPerReplica` explicitly to avoid relying on this.

The same `nodesPerReplica` field applies to the `prefill` and `decode` roles under `disaggregation`.

Multi-node workers aren't supported with HyperPod Task Governance in this release.

Save the manifest to a file, for example `endpoint.yaml`, and apply it:

```
kubectl apply -f endpoint.yaml
```

### Deploy a DynamoGraphDeployment
<a name="sagemaker-hyperpod-model-deployment-dynamo-dgd"></a>

If you chose a DGD in [Step 2: Choose a deployment approach](#sagemaker-hyperpod-model-deployment-dynamo-approach), write the manifest as you would for any Dynamo cluster, and apply it:

```
kubectl apply -f {{DGD_MANIFEST}}.yaml
```
+ Use a Dynamo runtime image from [Step 1: Complete the prerequisites](#sagemaker-hyperpod-model-deployment-dynamo-prereqs) for every component.
+ In each worker, request GPUs. For multi-node workers, also request EFA devices (`vpc.amazonaws.com/efa`).
+ The Dynamo operator creates a frontend Service named `{{DGD_NAME}}-frontend` on port 8000. The inference operator doesn't create a load balancer, TLS certificate, or SageMaker AI endpoint for a DGD, so expose the frontend yourself.
+ Requests use the worker's `--served-model-name` value as the `model` field.
+ Create NetworkPolicies for the DGD's pods. For details, see [Best practices](#sagemaker-hyperpod-model-deployment-dynamo-best-practices).

To check the status, run `kubectl get dynamographdeployment {{DGD_NAME}} -n {{NAMESPACE}}`. The DGD is ready when its `Ready` condition is `True`.

**Step 4 is complete when:** `kubectl apply` succeeds.

## Step 5: Verify your deployment
<a name="sagemaker-hyperpod-model-deployment-dynamo-verify"></a>

The following steps use an `InferenceEndpointConfig`. For a DGD, check its `Ready` condition (see [Deploy a DynamoGraphDeployment](#sagemaker-hyperpod-model-deployment-dynamo-dgd)) and use `{{DGD_NAME}}-frontend` in the test request.

1. Check the endpoint state. The state is `DeploymentComplete` when the Dynamo graph is ready.

   ```
   kubectl get inferenceendpointconfig {{ENDPOINT_NAME}} -n default \
       -o jsonpath='{.status.state}'
   ```

   If the state is `DeploymentFailed`, inspect the reason:

   ```
   kubectl describe inferenceendpointconfig {{ENDPOINT_NAME}} -n default
   ```
   + `DynamoOperatorNotInstalled`: The Dynamo operator isn't available on the cluster. Enable Dynamo in the add-on as described in [Step 3: Install or upgrade the add-on with Dynamo](#sagemaker-hyperpod-model-deployment-dynamo-addon). The inference operator checks again automatically.
   + `DynamoSpecInvalid`: The spec uses an unsupported combination. Update the spec as described in [Compatibility and limitations](#sagemaker-hyperpod-model-deployment-dynamo-limitations).
   + `DynamoDeployTimeout`: The graph didn't become ready within `maxDeployTimeInSeconds`. Large models can take a long time to download, so increase this value if needed.
   + `DynamoPodConfigError`: A container can't be created, for example because of a missing Secret or ConfigMap or a malformed image name. Fix the spec.
   + `DynamoWorkerCrashLoop`: A worker container restarted 3 or more times without becoming ready. The status message includes the last exit reason, such as `OOMKilled`.
   + `DynamoImagePullFailed`: The runtime image couldn't be pulled for 5 minutes. Check the image name and registry access.
   + `DynamoPodsUnschedulable`: A pod stayed unschedulable for 10 minutes, usually because no node has enough free GPUs or EFA devices.
   + `DynamoOperatorNotRunning`: The Dynamo operator didn't process the deployment for 5 minutes, for example because Dynamo was disabled in the add-on after the endpoint was created.

1. Check the Dynamo graph and its pods.

   ```
   kubectl get dynamographdeployment -n default
   kubectl get pods -n default
   ```

1. Send a test request through the frontend service. First, forward the frontend port:

   ```
   kubectl port-forward -n default svc/{{ENDPOINT_NAME}}-frontend 8000:8000
   ```

   In another terminal, send a request:

   ```
   curl http://localhost:8000/v1/chat/completions \
       -H "Content-Type: application/json" \
       -d '{"model": "{{MODEL_NAME}}", "messages": [{"role": "user", "content": "Hello"}]}'
   ```

**Step 5 is complete when:** the endpoint state is `DeploymentComplete`, or for a DGD the `Ready` condition is `True`, and the test request returns a response.

## Supported Regions
<a name="sagemaker-hyperpod-model-deployment-dynamo-regions"></a>

NVIDIA Dynamo on HyperPod Inference is available in the following AWS Regions: US East (N. Virginia), US East (Ohio), US West (N. California), US West (Oregon), South America (São Paulo), Europe (Ireland), Europe (London), Europe (Frankfurt), Europe (Stockholm), Europe (Spain), Asia Pacific (Tokyo), Asia Pacific (Mumbai), Asia Pacific (Hyderabad), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Jakarta), and Asia Pacific (Melbourne).

## Best practices
<a name="sagemaker-hyperpod-model-deployment-dynamo-best-practices"></a>

**Deployment**
+ **Match the runtime image to the Dynamo platform.** Use a runtime image from the same Dynamo release that the add-on installs, for example `public.ecr.aws/deep-learning-containers/dynamo:1.6.2-vllm-runtime-v1`. On EFA-enabled instances, use the EFA runtime image.
+ **Size multi-node workers explicitly.** Set `nodesPerReplica` for every multi-node worker or role. Make sure the worker's GPU count, `tensorParallelism` times any pipeline-parallel size, divides evenly across those nodes.
+ **Allow time for large models to load.** Increase `maxDeployTimeInSeconds` so that the deployment doesn't fail with `DynamoDeployTimeout` while a large model is still downloading or loading.
+ **Run the frontend and platform components on CPU nodes.** The Dynamo frontend and the platform components (the Dynamo operator, Grove, and the KAI scheduler) don't need GPUs and can run on any node. Adding a CPU instance group, such as `ml.c5.4xlarge` or larger, keeps them from using pod and CPU capacity on your GPU nodes.

**Security**
+ **Write your own NetworkPolicies for DGDs.** The inference operator creates NetworkPolicies only for endpoints that use `dynamoSpec`. For a DGD that you create directly, write NetworkPolicies that limit inbound traffic to its pods.
+ **Restrict the serving port to the load balancer, or run Dynamo endpoints in dedicated namespaces.** The frontend has no authentication inside the cluster. Because the policy allows any source on the serving port, any pod in the cluster can call the model directly and bypass the load balancer.
+ **Block pod access to the instance metadata service.** Add an egress policy that at least blocks the Amazon EC2 instance metadata service (IMDS) address, `169.254.169.254/32`, so pods can't read the node's IAM credentials.
+ **Have one namespace per team or trust boundary, and limit who can create pods in it.** The policies select pods by the DGD name label. Anyone who can create pods in the endpoint's namespace can add that label and reach the workers.

## Supported dynamoSpec fields
<a name="sagemaker-hyperpod-model-deployment-dynamo-reference"></a>

The following table lists the `dynamoSpec` fields, their defaults, and what each one does.


| Field | Default | Description | 
| --- | --- | --- | 
| modelServer | vllm | Inference engine that Dynamo wraps. Valid values are vllm, sglang, and trtllm. | 
| frontend.replicas | 1 | Number of frontend replicas. Must be 1 or greater. | 
| frontend.routingMode | kv-aware | How the frontend picks a worker. kv-aware routes to the worker with the best KV cache overlap for the request. round-robin and random ignore cache state. | 
| frontend.args | None | Additional arguments for the frontend process. Not applied to workers. | 
| aggregation.nodesPerReplica | 1 | Number of nodes that form one logical worker. Values greater than 1 create a gang-scheduled multi-node worker. | 
| aggregation.tensorParallelism | 1 | Total tensor parallelism degree for the worker. | 
| aggregation.dataParallelism | 1 | Number of data-parallel engine ranks in one worker. Each worker requests tensorParallelism × dataParallelism GPUs. To shard mixture-of-experts layers across those GPUs, add --enable-expert-parallel to args. Supported with modelServer: vllm on single-node workers only. | 
| aggregation.instanceType | Endpoint instanceType | Overrides the instance type for the worker. Must start with ml.. | 
| aggregation.args | None | Additional engine arguments for the worker. Arguments in worker.args are merged beneath these. To use pipeline parallelism, pass the engine's pipeline-parallel flag here. The operator sizes each worker's GPUs as tensorParallelism × the pipeline-parallel size. | 
| disaggregation.args | None | Engine arguments applied to both roles. Per-role args take precedence. | 
| disaggregation.prefill.replicas, disaggregation.decode.replicas | 1 | Number of workers for the role. Ignored when the role's autoScalingSpec has triggers. | 
| disaggregation.prefill.nodesPerReplica, disaggregation.decode.nodesPerReplica | 1 | Number of nodes that form one worker for the role. Values greater than 1 create a gang-scheduled multi-node worker. | 
| disaggregation.prefill.tensorParallelism, disaggregation.decode.tensorParallelism | 1 | Total tensor parallelism degree for each worker in the role. | 
| disaggregation.prefill.dataParallelism, disaggregation.decode.dataParallelism | 1 | Number of data-parallel engine ranks in each worker of the role. Each worker requests tensorParallelism × dataParallelism GPUs. Supported with modelServer: vllm on single-node workers only. | 
| disaggregation.prefill.instanceType, disaggregation.decode.instanceType | Endpoint instanceType | Overrides the instance type for the role. Must start with ml.. | 
| disaggregation.prefill.args, disaggregation.decode.args | None | Additional engine arguments for the role. Take precedence over disaggregation.args. | 
| disaggregation.prefill.autoScalingSpec, disaggregation.decode.autoScalingSpec | None | Autoscales the role independently of the other role. Takes the same fields as the endpoint-level autoScalingSpec. minReplicaCount must be 1 or greater. Without triggers, replicas sizes the role. | 

Outside `dynamoSpec`, `worker.image` is the Dynamo runtime image for both the frontend and the workers, and `worker.args` are passed to the worker engine. The inference operator ignores `worker.command` because it generates the entrypoint from `dynamoSpec`. If you set `worker.probes`, they replace the default Dynamo probes on every worker container.

## KV transfer path by instance type
<a name="sagemaker-hyperpod-model-deployment-dynamo-kv"></a>

With disaggregated serving, the KV cache moves from prefill workers to decode workers. The path depends on the instance type of each role and on whether the role spans multiple nodes. The following table lists the KV transfer path for each instance type.


| Instance type | GPUs | EFA devices | GPUDirect Remote Direct Memory Access (RDMA) | KV transfer, single-node role | KV transfer, multi-node role | 
| --- | --- | --- | --- | --- | --- | 
| ml.p5.48xlarge, ml.p5e.48xlarge | 8 | 32 | Yes | EFA with GPUDirect RDMA | EFA with GPUDirect RDMA | 
| ml.p5en.48xlarge, ml.p6-b300.48xlarge | 8 | 16 | Yes | EFA with GPUDirect RDMA | EFA with GPUDirect RDMA | 
| ml.p6-b200.48xlarge | 8 | 8 | Yes | EFA with GPUDirect RDMA | EFA with GPUDirect RDMA | 
| ml.p6e-gb200.36xlarge | 4 | 32 | Yes | EFA with GPUDirect RDMA | EFA with GPUDirect RDMA | 
| ml.g7e.12xlarge | 2 | 1 | Yes | TCP | EFA with GPUDirect RDMA | 
| ml.g7e.24xlarge | 4 | 2 | Yes | TCP | EFA with GPUDirect RDMA | 
| ml.g7e.48xlarge | 8 | 4 | Yes | TCP | EFA with GPUDirect RDMA | 
| ml.p4d.24xlarge, ml.p4de.24xlarge | 8 | 4 | No | TCP | EFA through host memory | 
| ml.g6e.48xlarge | 8 | 4 | No | TCP | EFA through host memory | 
| ml.g6e.24xlarge | 4 | 2 | No | TCP | EFA through host memory | 
| ml.g6.12xlarge, ml.g6.24xlarge, ml.g6e.12xlarge | 4 | 1 | No | TCP | EFA through host memory | 
| ml.g6.48xlarge | 8 | 1 | No | TCP | EFA through host memory | 
| ml.g6.8xlarge, ml.g6.16xlarge, ml.g6e.8xlarge, ml.g6e.16xlarge, ml.g7e.8xlarge | 1 | 1 | No | TCP | EFA through host memory | 
| ml.g5.xlarge, ml.g5.2xlarge, ml.g5.4xlarge, ml.g5.8xlarge, ml.g5.16xlarge, ml.g6.xlarge, ml.g6.2xlarge, ml.g6.4xlarge, ml.g6e.xlarge, ml.g6e.2xlarge, ml.g6e.4xlarge, ml.g7e.2xlarge, ml.g7e.4xlarge, ml.p5.4xlarge | 1 | 0 | No | TCP | Not supported | 
| ml.g5.12xlarge, ml.g5.24xlarge | 4 | 0 | No | TCP | Not supported | 
| ml.g5.48xlarge | 8 | 0 | No | TCP | Not supported | 

A single-node role uses EFA only when the instance type supports GPUDirect RDMA and has at least one EFA device per GPU. Multi-node roles require EFA, and the inference operator rejects multi-node workers on instance types without EFA devices.

Prefill and decode always use the same path (either EFA or TCP). If either role can't use EFA, both use TCP. When KV transfer runs over TCP, the endpoint still deploys, and the inference operator sets the `DynamoKVTransferOverTCP` condition with the reason.

The engine also affects the KV transfer path:
+ With `modelServer: vllm`, KV transfer can use EFA.
+ With `trtllm`, KV transfer can use EFA for single-node roles when `cache_transceiver_config.backend` is set to `NIXL`. Multi-node `trtllm` roles use TCP.
+ With `sglang`, KV transfer uses TCP on every instance type.

The inference operator treats instance types that aren't listed in this table as having no EFA devices.

## Compatibility and limitations
<a name="sagemaker-hyperpod-model-deployment-dynamo-limitations"></a>

The inference operator marks an endpoint as `DeploymentFailed` with the reason `DynamoSpecInvalid` when you combine `dynamoSpec` with an unsupported setting:
+ `pdSpec`: To run disaggregated serving with Dynamo, use `dynamoSpec.disaggregation`. `pdSpec` remains available for endpoints that don't use `dynamoSpec`.
+ `intelligentRoutingSpec`: Configure routing with `dynamoSpec.frontend.routingMode` instead.
+ `kvCacheSpec`: To offload KV cache with LMCache, add `--kv-transfer-config` with the `LMCacheConnectorV1` connector to the engine `args`.
+ Scale-to-zero (`spec.replicas` less than 1 with `aggregation`, or `autoScalingSpec.minReplicaCount` less than 1): A Dynamo endpoint needs at least one running worker to serve requests, so set these to 1 or greater.
+ Endpoint-level `autoScalingSpec` with `disaggregation`: To autoscale a disaggregated endpoint, set `autoScalingSpec` under `prefill` and `decode`. Each role then scales on its own. The minimum replica count must be 1 or greater.

`dynamoSpec` doesn't support the following fields yet. If you set them, the endpoint still deploys, but the inference operator doesn't apply them and emits a `DynamoFieldIgnored` warning event:
+ `instanceTypes`: use `instanceType` instead.
+ `worker.command`: the operator generates the entrypoint.
+ `nvidia.com/gpu` in `worker.resources`: set GPUs with `tensorParallelism`.
+ `spec.replicas` other than 1, for disaggregated endpoints: set `prefill.replicas` and `decode.replicas`.
+ `inferenceGateway`, `metrics.modelMetrics`, `worker.workingDir`, `worker.requestLimits`, `worker.resources.claims`, `kubernetes.initContainers`, `kubernetes.schedulerName`, `kubernetes.serviceAccountName`, `kubernetes.podTemplateAnnotations`, `kubernetes.tolerations`, and `kubernetes.volumes` other than the model volume: no replacement is available yet.

`nodeAffinity` is supported. The operator applies it to workers together with `instanceType`, so workers are placed only on nodes that match both.

You can't switch an existing endpoint between `aggregation` and `disaggregation`. Delete and recreate the `InferenceEndpointConfig` instead.

With data capture, `modelPod` capture runs on the frontend pods, because only the frontend sees the original request and response.

## Security considerations
<a name="sagemaker-hyperpod-model-deployment-dynamo-security"></a>

NVIDIA Dynamo is designed to run inside a trusted network boundary. External clients should reach only the frontend, and the internal communication planes shouldn't be reachable from untrusted networks. For more information about NVIDIA's trust model and hardening recommendations, see [Secure Deployment Guidelines](https://docs.nvidia.com/dynamo/latest/security/secure-deployment-guidelines) on the NVIDIA website.

For guidance on restricting host path volumes, see [Restrict host path volumes](sagemaker-hyperpod-model-deployment-deploy-nvme.md#sagemaker-hyperpod-model-deployment-deploy-nvme-hostpath-security). For guidance on protecting captured data, see the best practices in [Data capture for inference on HyperPod](sagemaker-hyperpod-model-deployment-data-capture.md).

### Enable network policy in the Amazon VPC CNI
<a name="sagemaker-hyperpod-model-deployment-dynamo-security-network"></a>

For each Dynamo endpoint, the inference operator creates Kubernetes NetworkPolicies that limit inbound traffic to the endpoint's pods, so workers accept traffic only from pods of the same endpoint. On Amazon EKS, these policies are enforced only when network policy is enabled in the `vpc-cni` add-on. Without it, any pod in the cluster can reach the internal Dynamo ports, which have no authentication. For information about the requirements for enabling network policy, see [Limit pod traffic with Kubernetes network policies](https://docs.aws.amazon.com/eks/latest/userguide/cni-network-policy.html). To enable network policy, run:

```
aws eks update-addon \
    --cluster-name $EKS_CLUSTER_NAME \
    --addon-name vpc-cni \
    --configuration-values '{"enableNetworkPolicy": "true"}' \
    --resolve-conflicts PRESERVE \
    --region $REGION
```

### Pod Security level
<a name="sagemaker-hyperpod-model-deployment-dynamo-security-pss"></a>

Dynamo endpoint pods meet the `baseline` [Pod Security Standard](https://kubernetes.io/docs/concepts/security/pod-security-standards/) (on the Kubernetes website) but not `restricted`, because they don't set `allowPrivilegeEscalation: false`, drop capabilities, run as non-root, or set a seccomp profile. Enforce `baseline` at most on namespaces that host Dynamo endpoints. You can set `warn` or `audit` to `restricted` to see what your own workloads need. Don't enforce `restricted` on `hyperpod-inference-system`, because the add-on's components don't meet it. The operator mounts model weights read-only for models from Amazon S3 and Amazon FSx.

To set the level on a namespace, run the following command. Replace {{NAMESPACE}} with the name of your namespace.

```
kubectl label namespace {{NAMESPACE}} \
    pod-security.kubernetes.io/enforce=baseline \
    pod-security.kubernetes.io/warn=restricted
```