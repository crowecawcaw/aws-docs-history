

# Deploy models from local NVMe storage using kubectl
<a name="sagemaker-hyperpod-model-deployment-deploy-nvme"></a>

This topic shows you how to deploy inference endpoints on Amazon SageMaker HyperPod that load model weights from a node's local NVMe storage instead of pulling them over the network from Amazon S3 or Amazon FSx. Reading weights locally eliminates the network hop during pod startup, which reduces inference pod cold-start time and is useful for autoscaling events, scale-from-zero workloads, and latency-sensitive failovers. For workloads where cold-start latency is not a concern, use `modelSourceType: s3` or `fsx` and skip this topic.

Local NVMe is node-local and ephemeral: data on NVMe is lost when a node is replaced, for example during a spot interruption, hardware failure, or AMI refresh. The approaches in this topic handle this differently — some require you to pre-populate every node, others fall back to Amazon S3 automatically when the model is not cached locally. Local NVMe instance storage is typically found in P, G, and Trn instance families. See [Amazon EC2 instance store specifications](https://docs.aws.amazon.com/ec2/latest/instancetypes/ac.html#ac_instance-store) to validate availability for your instance type.

You can choose from the following approaches based on your storage requirements:


**NVMe deployment approaches**  

| \# | Approach | Description | 
| --- | --- | --- | 
| 1 | Kubernetes volume (no fallback) | Use when model weights exist on NVMe on every node. Simplest setup with no Amazon S3, Amazon FSx, PV/PVC, or initContainers required. | 
| 2 | Kubernetes volume with fallback | Use when the model might not exist on NVMe on every node. You provide a custom initContainer that checks NVMe first and downloads from Amazon S3 using IRSA credentials if the model is missing. | 
| 3 | Amazon S3 with prefetch and fallback | Use when you want to stage model weights to RAM for pod startup. You provide a custom initContainer that checks NVMe first and falls back to copying from the operator-provisioned Amazon S3 mount if the model is not cached locally. | 

## Prerequisites
<a name="sagemaker-hyperpod-model-deployment-deploy-nvme-prereqs"></a>

Before you begin, verify that you've:
+ Set up inference capabilities on your Amazon SageMaker HyperPod clusters. For more information, see [Setting up your HyperPod clusters for model deployment](sagemaker-hyperpod-model-deployment-setup.md).
+ Installed [kubectl](https://kubernetes.io/docs/reference/kubectl/) utility and configured [jq](https://jqlang.org/) in your terminal.
+ Pre-populated model weights on the local NVMe storage of your target nodes (see [Preload model weights to NVMe](#sagemaker-hyperpod-model-deployment-deploy-nvme-preload) for instructions).

## Choose your deployment approach
<a name="sagemaker-hyperpod-model-deployment-deploy-nvme-choose"></a>

Use the following decision flow to determine which approach is right for your use case.

```
                  ┌────────────────────────────┐
                  │ Want to use a volume of    │
                  │ your choice, e.g. NVMe?    │
                  └─────┬──────────────┬───────┘
                   YES  │              │ NO
                        ▼              ▼
        ┌──────────────────────┐   Use S3/FSx/HF
        │ Are you sure EVERY   │   as-is (no volume
        │ node has the model   │   override needed)
        │ on NVMe?             │
        └─────┬──────────┬─────┘
         YES  │          │ NO
              ▼          ▼
  ┌─────────────────┐  ┌───────────────────────────────┐
  │ Approach 1      │  │ Do you need the operator to   │
  │                 │  │ create S3/FSx PVCs as a       │
  │ Use k8sVolume   │  │ fallback when the model is    │
  │ field in CRD to │  │ missing on a node?            │
  │ read from NVMe  │  └──────┬────────────────┬───────┘
  │ directly.       │    YES  │                │ NO
  └─────────────────┘         ▼                ▼
                  ┌──────────────────┐  ┌──────────────────────┐
                  │ Approach 3       │  │ Approach 2           │
                  │                  │  │                      │
                  │ Use S3 with      │  │ Use k8sVolume with a │
                  │ prefetch enabled.│  │ custom initContainer │
                  │ Custom           │  │ you create that      │
                  │ initContainer    │  │ checks NVMe first    │
                  │ checks NVMe      │  │ and downloads from   │
                  │ first, falls     │  │ S3 via IRSA if the   │
                  │ back to S3, and  │  │ model is missing.    │
                  │ copies to RAM.   │  └──────────────────────┘
                  └──────────────────┘
```

## Deploy using a Kubernetes volume (no fallback)
<a name="sagemaker-hyperpod-model-deployment-deploy-nvme-volume"></a>

Use this approach when you have model weights on NVMe on every node and want the simplest setup — no Amazon S3 or Amazon FSx configuration, no PV/PVC, and no initContainers.

When you set `modelSourceType: kubernetesVolume`, the operator skips PV/PVC creation entirely. No CSI driver, Amazon S3 fuse mount, or Amazon FSx mount is used. The customer-provided `model-weights` volume is used directly in the pod spec, and the worker reads model data from NVMe at `/opt/ml/model`.

**Important**  
When using `modelSourceType: kubernetesVolume`, the operator derives the expected volume name from `modelVolumeMount.name` in your worker configuration. `kubernetes.volumes` must contain a volume with that same name. The operator validates this and rejects the deployment with a `KubernetesVolumeValidationFailed` condition if no matching volume is found. In the following examples, both use `model-weights`.

1. Create the `InferenceEndpointConfig` YAML file. Replace the placeholder values with your actual resource identifiers.

   ```
   cat <<EOF> deploy_nvme_k8s_volume.yaml
   apiVersion: inference.sagemaker.aws.amazon.com/v1
   kind: InferenceEndpointConfig
   metadata:
     name: nvme-k8s-volume
     namespace: default
   spec:
     endpointName: nvme-k8s-volume
     modelName: Qwen2.5-VL-7B-Instruct
     invocationEndpoint: v1/chat/completions
     replicas: 1
     modelSourceConfig:
       modelSourceType: kubernetesVolume
     kubernetes:
       volumes:
         - name: model-weights
           hostPath:
             path: /opt/dlami/nvme/<YOUR_MODEL>
             type: Directory
     loadBalancer:
       healthCheckPath: /health
     worker:
       image: lmcache/vllm-openai:latest
       args:
         - /opt/ml/model
         - --max-model-len
         - "15000"
         - --tensor-parallel-size
         - "1"
       modelInvocationPort:
         containerPort: 8000
         name: http
       modelVolumeMount:
         name: model-weights
         mountPath: /opt/ml/model
       resources:
         limits:
           nvidia.com/gpu: "1"
         requests:
           cpu: "6"
           memory: 30Gi
           nvidia.com/gpu: "1"
       environmentVariables:
         - name: PYTHONHASHSEED
           value: "123"
         - name: VLLM_REQUEST_TIMEOUT
           value: "600"
   EOF
   ```
**Note**  
To configure KV caching and intelligent routing for improved performance, see [Configure KV caching and intelligent routing](sagemaker-hyperpod-model-deployment-caching-routing.md#sagemaker-hyperpod-model-deployment-deploy-ftm-cache-route).

1. Deploy the `InferenceEndpointConfig`.

   ```
   kubectl apply -f deploy_nvme_k8s_volume.yaml
   ```

1. Verify the deployment status.

   ```
   kubectl describe InferenceEndpointConfig nvme-k8s-volume -n default
   ```

## Deploy using a Kubernetes volume with fallback
<a name="sagemaker-hyperpod-model-deployment-deploy-nvme-fallback"></a>

Use this approach when the model might or might not be on NVMe on a given node. A `hostPath` volume only works on nodes where the data exists — pods scheduled on other nodes would mount an empty or nonexistent path, causing the model server to fail.

In this approach, you set `modelSourceType: kubernetesVolume` and provide a custom `initContainer` that checks NVMe first and downloads from Amazon S3 using IRSA credentials if the model is missing.

### Set up IRSA
<a name="sagemaker-hyperpod-model-deployment-deploy-nvme-fallback-irsa"></a>

Before deploying, configure IAM Roles for Service Accounts (IRSA) to give your pods credentials for downloading from Amazon S3.

1. Get the OIDC provider ID for your cluster.

   ```
   aws eks describe-cluster --name <CLUSTER_NAME> --region <REGION> \
     --query "cluster.identity.oidc.issuer" --output text
   ```

1. Create an IAM trust policy. Save the following as `trust-policy.json`, replacing the placeholder values.

   ```
   {
     "Version": "2012-10-17",		 	 	 
     "Statement": [{
       "Effect": "Allow",
       "Principal": {
         "Federated": "arn:aws:iam::<ACCOUNT_ID>:oidc-provider/oidc.eks.<REGION>.amazonaws.com/id/<OIDC_ID>"
       },
       "Action": "sts:AssumeRoleWithWebIdentity",
       "Condition": {
         "StringEquals": {
           "oidc.eks.<REGION>.amazonaws.com/id/<OIDC_ID>:sub": "system:serviceaccount:<NAMESPACE>:<SA_NAME>",
           "oidc.eks.<REGION>.amazonaws.com/id/<OIDC_ID>:aud": "sts.amazonaws.com"
         }
       }
     }]
   }
   ```
**Warning**  
Always scope the trust policy to a specific namespace and ServiceAccount name. Never use wildcards in the subject condition (for example, `system:serviceaccount:*:*`), as this would allow any ServiceAccount in any namespace to assume the role.

1. Create the IAM role and attach a scoped Amazon S3 read policy for your model bucket.

   ```
   aws iam create-role --role-name <ROLE_NAME> \
     --assume-role-policy-document file://trust-policy.json
   
   aws iam put-role-policy --role-name <ROLE_NAME> \
     --policy-name S3ModelReadAccess \
     --policy-document '{
       "Version": "2012-10-17",		 	 	 
       "Statement": [{
         "Effect": "Allow",
         "Action": ["s3:GetObject", "s3:ListBucket"],
         "Resource": [
           "arn:aws:s3:::<YOUR_BUCKET>",
           "arn:aws:s3:::<YOUR_BUCKET>/<YOUR_MODEL_PREFIX>/*"
         ]
       }]
     }'
   ```

1. Create the Kubernetes service account with the IRSA annotation.

   ```
   kubectl create sa <SA_NAME> -n <NAMESPACE>
   kubectl annotate sa <SA_NAME> -n <NAMESPACE> \
     eks.amazonaws.com/role-arn=arn:aws:iam::<ACCOUNT_ID>:role/<ROLE_NAME>
   ```

### Deploy the model
<a name="sagemaker-hyperpod-model-deployment-deploy-nvme-fallback-deploy"></a>

1. Create the `InferenceEndpointConfig` YAML file. Replace the placeholder values with your actual resource identifiers.

   ```
   cat <<EOF> deploy_nvme_k8s_volume_fallback.yaml
   apiVersion: inference.sagemaker.aws.amazon.com/v1
   kind: InferenceEndpointConfig
   metadata:
     name: nvme-k8s-volume-fallback
     namespace: default
   spec:
     endpointName: nvme-k8s-volume-fallback
     modelName: Qwen2.5-VL-7B-Instruct
     invocationEndpoint: v1/chat/completions
     replicas: 1
     modelSourceConfig:
       modelSourceType: kubernetesVolume
     kubernetes:
       serviceAccountName: <YOUR_SERVICE_ACCOUNT>
       initContainers:
         - name: smart-loader
           image: public.ecr.aws/aws-cli/aws-cli:latest
           command: ["/bin/bash", "-c"]
           args:
             - |
               if [ "$(ls -A /model)" ]; then
                 echo "NVMe hit — model already present ($(du -sh /model | cut -f1))"
               else
                 echo "NVMe miss — downloading from S3"
                 aws s3 sync s3://<YOUR_BUCKET>/<YOUR_MODEL>/ /model/
               fi
           volumeMounts:
             - name: model-weights
               mountPath: /model
       volumes:
         - name: model-weights
           hostPath:
             path: /opt/dlami/nvme/<YOUR_MODEL>
             type: DirectoryOrCreate
     loadBalancer:
       healthCheckPath: /health
     worker:
       image: lmcache/vllm-openai:latest
       args:
         - /opt/ml/model
         - --max-model-len
         - "15000"
         - --tensor-parallel-size
         - "1"
       modelInvocationPort:
         containerPort: 8000
         name: http
       modelVolumeMount:
         name: model-weights
         mountPath: /opt/ml/model
       resources:
         limits:
           nvidia.com/gpu: "1"
         requests:
           cpu: "6"
           memory: 30Gi
           nvidia.com/gpu: "1"
       environmentVariables:
         - name: PYTHONHASHSEED
           value: "123"
   EOF
   ```
**Note**  
To configure KV caching and intelligent routing for improved performance, see [Configure KV caching and intelligent routing](sagemaker-hyperpod-model-deployment-caching-routing.md#sagemaker-hyperpod-model-deployment-deploy-ftm-cache-route).

1. Deploy the `InferenceEndpointConfig`.

   ```
   kubectl apply -f deploy_nvme_k8s_volume_fallback.yaml
   ```

1. Verify the deployment status.

   ```
   kubectl describe InferenceEndpointConfig nvme-k8s-volume-fallback -n default
   ```

## Deploy using Amazon S3 with prefetch and NVMe fallback
<a name="sagemaker-hyperpod-model-deployment-deploy-nvme-s3-prefetch"></a>

Use this approach when you want inference performance by staging model weights to RAM, with automatic fallback to Amazon S3 if the model isn't cached locally on NVMe.

When you set `modelSourceType: s3` with `prefetchEnabled: true`, the operator creates two volumes automatically:
+ A volume named after your `modelVolumeMount.name` (typically `model-weights`) — an Amazon S3 CSI fuse mount containing your model
+ `model-weights-copy` — a RAM-backed `emptyDir` where the worker reads from

You add a custom `nvme-cache` volume pointing to the node's local NVMe storage, and a custom `initContainer` that:
+ If the model exists on NVMe — copies from NVMe to RAM (`model-weights-copy`), skipping the network entirely.
+ If the model is missing — falls back to copying from the Amazon S3 mount (`model-weights`) to RAM (`model-weights-copy`). Optionally copies to NVMe so subsequent pod startups on the same node use the fast local path.

**Important**  
Do not override `model-weights` in `kubernetes.volumes` when using this approach. The operator creates `model-weights` pointing to the Amazon S3 CSI volume. Overriding it removes the operator-provisioned volume that your initContainer needs for fallback. Use a separate volume name (for example, `nvme-cache`) for your NVMe hostPath.

**Important**  
Do not include `model-weights-copy` in `kubernetes.volumes`. It is a reserved name created automatically by the operator. Your initContainer can reference it in `volumeMounts` but must not declare it as a volume.

1. Create the `InferenceEndpointConfig` YAML file. Replace the placeholder values with your actual resource identifiers.

   ```
   cat <<EOF> deploy_nvme_s3_prefetch_fallback.yaml
   apiVersion: inference.sagemaker.aws.amazon.com/v1
   kind: InferenceEndpointConfig
   metadata:
     name: nvme-s3-prefetch-fallback
     namespace: default
   spec:
     endpointName: nvme-s3-prefetch-fallback
     modelName: Qwen2.5-VL-7B-Instruct
     invocationEndpoint: v1/chat/completions
     replicas: 1
     modelSourceConfig:
       modelSourceType: s3
       s3Storage:
         bucketName: <YOUR_BUCKET>
         region: <YOUR_REGION>
       prefetchEnabled: true
     kubernetes:
       serviceAccountName: <YOUR_SERVICE_ACCOUNT>
       initContainers:
         - name: smart-loader
           image: public.ecr.aws/aws-cli/aws-cli:latest
           command: ["/bin/bash", "-c"]
           args:
             - |
               # Check NVMe first, fall back to S3 mount, then copy to RAM
               if [ "$(ls -A /nvme)" ]; then
                 echo "NVMe hit ($(du -sh /nvme | cut -f1))"
                 echo "Copying model from NVMe to RAM..."
                 cp -r /nvme/* /model/
               else
                 echo "NVMe miss — copying from S3 mount to NVMe, then NVMe to RAM"
                 cp -r /s3-model/* /nvme/
                 cp -r /nvme/* /model/
               fi
               echo "Done. $(du -sh /model | cut -f1) in RAM."
           volumeMounts:
             - name: model-weights
               mountPath: /s3-model
             - name: nvme-cache
               mountPath: /nvme
             - name: model-weights-copy
               mountPath: /model
       volumes:
         - name: nvme-cache
           hostPath:
             path: /opt/dlami/nvme/<YOUR_MODEL>
             type: DirectoryOrCreate
     loadBalancer:
       healthCheckPath: /health
     worker:
       image: lmcache/vllm-openai:latest
       args:
         - /opt/ml/model
         - --max-model-len
         - "15000"
         - --tensor-parallel-size
         - "1"
       modelInvocationPort:
         containerPort: 8000
         name: http
       modelVolumeMount:
         name: model-weights
         mountPath: /opt/ml/model
       resources:
         limits:
           nvidia.com/gpu: "1"
         requests:
           cpu: "6"
           memory: 30Gi
           nvidia.com/gpu: "1"
       environmentVariables:
         - name: PYTHONHASHSEED
           value: "123"
         - name: VLLM_REQUEST_TIMEOUT
           value: "600"
   EOF
   ```
**Note**  
To configure KV caching and intelligent routing for improved performance, see [Configure KV caching and intelligent routing](sagemaker-hyperpod-model-deployment-caching-routing.md#sagemaker-hyperpod-model-deployment-deploy-ftm-cache-route).

1. Deploy the `InferenceEndpointConfig`.

   ```
   kubectl apply -f deploy_nvme_s3_prefetch_fallback.yaml
   ```

1. Verify the deployment status.

   ```
   kubectl describe InferenceEndpointConfig nvme-s3-prefetch-fallback -n default
   ```

## Understanding model-weights and model-weights-copy with prefetch
<a name="sagemaker-hyperpod-model-deployment-deploy-nvme-prefetch-volumes"></a>

When using prefetch, the operator creates two model-related volumes:
+ A volume named after your `modelVolumeMount.name` (typically `model-weights`) — an Amazon S3 CSI fuse mount containing your model
+ `model-weights-copy` — a RAM-backed emptyDir where the worker actually reads from

In your `InferenceEndpointConfig`, you define:

```
modelVolumeMount:
    name: model-weights
    mountPath: /opt/ml/model
```

While you reference `model-weights`, when `prefetchEnabled: true`, it is actually `model-weights-copy` that gets mounted at `/opt/ml/model` in the worker container. When using a custom initContainer, ensure that you copy the data into the volume called `model-weights-copy` — that is where the worker expects to find it.

When `prefetchEnabled: false`, there is only one volume (named after your `modelVolumeMount.name`) and it is mounted directly at `/opt/ml/model`.

## Configure a custom service account
<a name="sagemaker-hyperpod-model-deployment-deploy-nvme-sa"></a>

You can assign a custom Kubernetes ServiceAccount to your inference endpoint pods using the `spec.kubernetes.serviceAccountName` field in the `InferenceEndpointConfig`. This is useful for providing AWS credentials via IRSA (IAM Roles for Service Accounts) to your worker containers or init containers — for example, to download model weights from Amazon S3 in a fallback scenario.

**Important**  
Custom service account support is disabled by default and must be explicitly enabled by a cluster administrator before use. See [Enable custom service accounts](#sagemaker-hyperpod-model-deployment-deploy-nvme-sa-enable) for instructions.

If you do not specify a ServiceAccount, the namespace's default ServiceAccount is used.

### Enable custom service accounts
<a name="sagemaker-hyperpod-model-deployment-deploy-nvme-sa-enable"></a>

Custom service account support is disabled by default. A cluster administrator must enable it in the operator's Helm configuration before users can reference custom ServiceAccounts in their `InferenceEndpointConfig`.
+ Update the operator Helm values to enable the feature. If you deployed the operator via Helm, upgrade with the flag:

  ```
  helm upgrade hyperpod-inference-operator <CHART_PATH> \
    --set enableCustomServiceAccounts=true \
    --reuse-values
  ```
+ If you deployed the operator as an Amazon EKS add-on, update the add-on configuration to include `enableCustomServiceAccounts: true` in the advanced configuration settings.
+ Verify the operator pod has the environment variable set:

  ```
  kubectl get deployment hyperpod-inference-controller-manager \
    -n hyperpod-inference-system \
    -o jsonpath='{.spec.template.spec.containers[0].env}' | jq '.[] | select(.name=="ENABLE_CUSTOM_SERVICE_ACCOUNTS")'
  ```

  You should see:

  ```
  {
    "name": "ENABLE_CUSTOM_SERVICE_ACCOUNTS",
    "value": "true"
  }
  ```

**Important**  
If this feature is not enabled, any `InferenceEndpointConfig` that specifies `kubernetes.serviceAccountName` is rejected with a `DeploymentFailed` status and the message: `kubernetes.serviceAccountName is not enabled. Requires addon configuration (enableCustomServiceAccounts: true)`.

### Label the service account
<a name="sagemaker-hyperpod-model-deployment-deploy-nvme-sa-label"></a>

Before you can reference a custom ServiceAccount, a cluster administrator must label it as user-assignable:

```
kubectl label serviceaccount <your-service-account> \
  sagemaker.amazonaws.com/user-assignable=true \
  -n <namespace>
```

Only ServiceAccounts with this label can be referenced by inference endpoints. This is a security control to prevent unauthorized privilege escalation.

### Specify the service account in your configuration
<a name="sagemaker-hyperpod-model-deployment-deploy-nvme-sa-spec"></a>

Add the `serviceAccountName` field under `spec.kubernetes` in your `InferenceEndpointConfig`:

```
apiVersion: inference.sagemaker.aws.amazon.com/v1
kind: InferenceEndpointConfig
metadata:
  name: my-inference-endpoint
  namespace: my-namespace
spec:
  kubernetes:
    serviceAccountName: my-inference-sa
  # ... rest of your config
```

### Validation rules
<a name="sagemaker-hyperpod-model-deployment-deploy-nvme-sa-validation"></a>

The operator validates the `serviceAccountName` field on both create and update operations. Your deployment will be rejected with a `DeploymentFailed` status if any of the following conditions are met:
+ The ServiceAccount does not exist in the namespace — `serviceAccountName "X" not found in namespace "Y"`
+ The ServiceAccount is missing the required label — `serviceAccountName "X" is not labeled as user-assignable (requires label sagemaker.amazonaws.com/user-assignable=true)`
+ The ServiceAccount is the operator's system ServiceAccount — `serviceAccountName must not reference the operator's service account`

**Note**  
All containers in the inference pod (worker, init containers, and sidecars) inherit the permissions of the specified ServiceAccount. If the ServiceAccount is annotated with `eks.amazonaws.com/role-arn`, the pod receives temporary AWS credentials for that IAM role. Cluster administrators should only label ServiceAccounts as user-assignable after reviewing the associated RBAC roles and IAM permissions.

**Note**  
If a ServiceAccount is deleted while an `InferenceEndpointConfig` is already running, existing pods continue to run with their current credentials until they are restarted. However, new pod creation (for example, during scaling or rescheduling) will fail because the ServiceAccount no longer exists. The operator validates the ServiceAccount when the deployment is first created and when the IEC spec is updated — it does not continuously monitor the ServiceAccount. Updating the IEC spec after the SA is deleted will result in a `DeploymentFailed` status.

### Security best practices for custom service accounts
<a name="sagemaker-hyperpod-model-deployment-deploy-nvme-sa-security"></a>

When you use a custom ServiceAccount with inference endpoints, the HyperPod inference operator creates Deployments on your behalf. All containers in the inference pod — including the worker, init containers, and sidecars — inherit the permissions of the specified ServiceAccount. Follow these best practices to secure your cluster.

**Lock down RBAC permissions**
+ Create a dedicated ServiceAccount for each inference workload. Do not reuse ServiceAccounts across unrelated workloads.
+ Bind only the minimum RBAC permissions required. For example, if your init container only needs to read from Amazon S3, the ServiceAccount should not have permissions to list or modify Kubernetes resources.

  ```
  # Example: minimal Role for an inference workload that only needs S3 access via IRSA
  # No Kubernetes API permissions needed — IRSA provides AWS credentials directly
  apiVersion: v1
  kind: ServiceAccount
  metadata:
    name: my-inference-sa
    namespace: my-namespace
    labels:
      sagemaker.amazonaws.com/user-assignable: "true"
    annotations:
      eks.amazonaws.com/role-arn: arn:aws:iam::<ACCOUNT_ID>:role/<SCOPED_ROLE_NAME>
  ```
+ Avoid granting cluster-wide permissions (ClusterRoleBindings) to ServiceAccounts used by inference pods.

**Scope IRSA IAM roles**
+ When annotating a ServiceAccount with `eks.amazonaws.com/role-arn`, ensure the IAM role follows least-privilege principles.
+ Scope Amazon S3 permissions to the specific bucket and prefix containing your model weights.

  ```
  {
    "Version": "2012-10-17",		 	 	 
    "Statement": [{
      "Effect": "Allow",
      "Action": ["s3:GetObject", "s3:ListBucket"],
      "Resource": [
        "arn:aws:s3:::<YOUR_BUCKET>",
        "arn:aws:s3:::<YOUR_BUCKET>/<YOUR_MODEL_PREFIX>/*"
      ]
    }]
  }
  ```
+ Do not use broad managed policies such as `AmazonS3FullAccess` in production. Use `AmazonS3ReadOnlyAccess` or a custom policy scoped to your model bucket.

**Protect the user-assignable label**
+ Only cluster administrators should add or remove the `sagemaker.amazonaws.com/user-assignable=true` label. Use Kubernetes RBAC to restrict who can modify ServiceAccount labels in your namespace.
+ Review the RBAC roles and IAM permissions associated with a ServiceAccount before labeling it as user-assignable.
+ Periodically audit which ServiceAccounts carry the `user-assignable` label.

  ```
  kubectl get serviceaccounts -n <NAMESPACE> -l sagemaker.amazonaws.com/user-assignable=true
  ```
+ Ensure non-admin roles do not include `patch`, `update`, or `create` verbs on ServiceAccount resources. The operator validates the `user-assignable` label at deployment time, but does not prevent unauthorized users from adding the label to a ServiceAccount. Restricting who can modify ServiceAccounts via RBAC is the primary control for protecting this label. Non-admin users should only have `get` and `list` access:

  ```
  # Example: RBAC Role for non-admin users — read-only access to ServiceAccounts
  apiVersion: rbac.authorization.k8s.io/v1
  kind: Role
  metadata:
    name: sa-read-only
    namespace: <NAMESPACE>
  rules:
    - apiGroups: [""]
      resources: ["serviceaccounts"]
      verbs: ["get", "list"]
  ```

**Important**  
The HyperPod inference operator acts as an intermediary that creates Deployments on behalf of users. Unlike standard Kubernetes workloads where the caller directly creates pods, the operator assigns the specified ServiceAccount to pods it creates. This means that any permissions granted to a user-assignable ServiceAccount are effectively available to anyone who can create an `InferenceEndpointConfig` in that namespace. Ensure that namespace-level RBAC controls who can create and update `InferenceEndpointConfig` resources.

## Preload model weights to NVMe
<a name="sagemaker-hyperpod-model-deployment-deploy-nvme-preload"></a>

If you need to pre-populate NVMe on specific nodes before deploying, you can use a one-off pod to sync from Amazon S3.

**Note**  
This approach targets a specific node via `nodeName` and does not work with autoscaling. For autoscaling scenarios, use the Kubernetes volume with fallback or Amazon S3 with prefetch approaches, which handle missing models automatically via initContainer fallback logic.

1. Create the preload pod YAML file. Replace the placeholder values with your actual resource identifiers.

   ```
   cat <<EOF> nvme-s3-copy.yaml
   apiVersion: v1
   kind: Pod
   metadata:
     name: nvme-s3-copy
     namespace: default
   spec:
     nodeName: <TARGET_NODE>
     restartPolicy: Never
     containers:
       - name: s3-copy
         image: public.ecr.aws/aws-cli/aws-cli:latest
         command: ["/bin/bash", "-c"]
         args:
           - |
             echo "=== Starting S3 sync to NVMe ==="
             aws s3 sync s3://<YOUR_BUCKET>/<YOUR_MODEL>/ /nvme/<YOUR_MODEL>/ --region <YOUR_REGION>
             echo "=== Sync complete ==="
             ls -la /nvme/<YOUR_MODEL>/
             du -sh /nvme/<YOUR_MODEL>/
             echo "=== Done ==="
         volumeMounts:
           - name: nvme-storage
             mountPath: /nvme
     serviceAccountName: default
     volumes:
       - name: nvme-storage
         hostPath:
           path: /opt/dlami/nvme
           type: Directory
   EOF
   ```

1. Apply the pod and monitor the sync progress.

   ```
   kubectl apply -f nvme-s3-copy.yaml
   kubectl get pod nvme-s3-copy -w
   kubectl logs nvme-s3-copy -f
   ```

1. Clean up the pod after the sync completes.

   ```
   kubectl delete pod nvme-s3-copy
   ```

## Reserved volume names
<a name="sagemaker-hyperpod-model-deployment-deploy-nvme-reserved-volumes"></a>

The operator manages several internal volumes that cannot be overridden via `kubernetes.volumes`. Using any of these names results in a `KubernetesVolumeValidationFailed` condition.


**Reserved volume names**  

| \# | Name | Purpose | 
| --- | --- | --- | 
| 1 | shm | Shared memory (/dev/shm) for inter-process communication | 
| 2 | model-weights-copy | RAM-backed emptyDir used when prefetchEnabled: true | 
| 3 | parallel-copy-configmap | ConfigMap for parallel copy script (prefetch) | 
| 4 | lmcache-config | LMCache configuration volume | 
| 5 | gated-model-downloader-configmap | ConfigMap for gated model download script | 

## Things to remember
<a name="sagemaker-hyperpod-model-deployment-deploy-nvme-things-to-remember"></a>
+ **Do not use reserved volume names.** The operator manages several internal volumes (see [Reserved volume names](#sagemaker-hyperpod-model-deployment-deploy-nvme-reserved-volumes)). Using any of these names in `kubernetes.volumes` results in a `KubernetesVolumeValidationFailed` condition.
+ **Volume names must match.** The operator derives the volume name from `modelVolumeMount.name`. When using `modelSourceType: kubernetesVolume`, `kubernetes.volumes` must contain a volume with that same name.
+ **Mount volumes to the correct location in your initContainer.** Ensure that any volume you create is mounted to the correct path in your initContainer.
+ **No custom service account is needed for S3/FSx.** If you are unable to create custom service accounts or prefer not to, you can use `modelSourceType: s3` or `fsx`. The operator provisions S3/FSx volumes automatically. You can still add custom `initContainers` and override volumes on top of the operator-managed storage.
+ **IRSA credentials are injected into all containers.** When you set `kubernetes.serviceAccountName` to a service account with an IRSA annotation, Amazon EKS injects AWS credentials (`aws-iam-token` volume, `AWS_ROLE_ARN`, `AWS_WEB_IDENTITY_TOKEN_FILE`) into all containers, including your custom initContainers.
+ **Do not set `modelLocation` when using `kubernetesVolume`.** The volume path is controlled by `kubernetes.volumes`. Setting `modelLocation` when `modelSourceType` is `kubernetesVolume` results in a validation error.
+ **Understand how `model-weights` vs `model-weights-copy` works with prefetch.** When `prefetchEnabled: true`, the operator creates two model-related volumes:
  + `model-weights` — the source volume (from Amazon S3/Amazon FSx PVC or your override)
  + `model-weights-copy` — a RAM-backed emptyDir where the worker actually reads from
+ While you reference `model-weights` in your config, when `prefetchEnabled: true`, it is actually `model-weights-copy` that gets mounted at `/opt/ml/model` in the worker container. When using a custom initContainer, ensure that you copy the data into the volume called `model-weights-copy` — that is where the worker expects to find it. When `prefetchEnabled: false`, there is only one volume (named after your `modelVolumeMount.name`) and it is mounted directly at `/opt/ml/model`.

## Troubleshooting
<a name="sagemaker-hyperpod-model-deployment-deploy-nvme-troubleshooting"></a>

Use these debugging commands if your deployment isn't working as expected.
+ Check the `InferenceEndpointConfig` status to see the high-level deployment state and any configuration issues.

  ```
  kubectl describe InferenceEndpointConfig <ENDPOINT_NAME> -n <NAMESPACE>
  ```
+ Check the Kubernetes deployment status.

  ```
  kubectl describe deployment <ENDPOINT_NAME> -n <NAMESPACE>
  ```
+ Check the status of all Kubernetes objects in your namespace.

  ```
  kubectl get pods,svc,deployment,InferenceEndpointConfig,sagemakerendpointregistration -n <NAMESPACE>
  ```
+ Check initContainer logs if the model loading step fails.

  ```
  kubectl logs <POD_NAME> -c smart-loader -n <NAMESPACE>
  ```
+ If the deployment fails with "not found in namespace", verify the ServiceAccount exists:

  ```
  kubectl get serviceaccount <name> -n <namespace>
  ```
+ If the deployment fails with "not labeled as user-assignable", ask your cluster administrator to add the required label:

  ```
  kubectl label serviceaccount <name> sagemaker.amazonaws.com/user-assignable=true -n <namespace>
  ```
+ If the deployment fails with "must not reference the operator's service account", create a separate ServiceAccount for your workload. You cannot use the HyperPod inference operator's own ServiceAccount.