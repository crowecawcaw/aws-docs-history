

# Amazon SageMaker HyperPod Inference release notes
<a name="sagemaker-hyperpod-inference-release-notes"></a>

This topic covers release notes that track updates, fixes, and new features for Amazon SageMaker HyperPod Inference. SageMaker HyperPod Inference enables you to deploy and scale machine learning models on your HyperPod clusters with enterprise-grade reliability. For general Amazon SageMaker HyperPod platform releases, updates, and improvements, see [Amazon SageMaker HyperPod release notes](sagemaker-hyperpod-release-notes.md).

For information about SageMaker HyperPod Inference capabilities and deployment options, see [Deploying models on Amazon SageMaker HyperPod](sagemaker-hyperpod-model-deployment.md).

## SageMaker HyperPod Inference release notes: v3.4
<a name="sagemaker-hyperpod-inference-release-notes-20260821"></a>

**Release Date:** August 21, 2026

**Summary**

Amazon SageMaker HyperPod Inference Operator v3.4 makes the resource requests and limits of the managed sidecar containers configurable through the CRD. You can now size the reverse proxy, metrics collector, and data capture uploader containers to match your workload instead of relying on fixed defaults.

Amazon SageMaker HyperPod Inference Operator v3.4 is available in all AWS Regions where SageMaker HyperPod is supported.

**New Features**
+ **Configurable Container Resources** – Set resource requests and limits for the operator-managed sidecar containers. Use the new `metricsSidecarResources`, `metricsCollectorResources`, and `s3UploaderResources` fields on your `InferenceEndpointConfig` or `JumpStartModel`. These fields let you raise the reverse proxy memory for high-concurrency deployments, tune the metrics collector, and size the data capture uploader. When a field is set, the operator applies your values instead of the built-in defaults and preserves them across reconciliation. Each field fully replaces that container's resource block, so specify complete requests and limits.

### Upgrade to v3.4
<a name="sagemaker-hyperpod-inference-v3-4-upgrade"></a>

**Helm upgrade:**

If you already have the Inference Operator installed by using Helm, use the following commands to upgrade:

```
helm get values -n kube-system hyperpod-inference-operator \
> current-values.yaml

cd sagemaker-hyperpod-cli/helm_chart/HyperPodHelmChart/\
charts/inference-operator

helm upgrade hyperpod-inference-operator . -n kube-system \
  -f current-values.yaml --set image.tag=v3.4

# Verification
kubectl get deployment hyperpod-inference-operator-controller-manager \
  -n hyperpod-inference-system \
  -o jsonpath='{.spec.template.spec.containers[0].image}'
```

**EKS Add-on upgrade:**

If you installed the Inference Operator as an EKS Add-on, upgrade to the latest version:

```
CLUSTER=EKS_CLUSTER_NAME
REGION=REGION

aws eks update-addon \
  --cluster-name $CLUSTER \
  --addon-name amazon-sagemaker-hyperpod-inference \
  --addon-version v1.5.0-eksbuild.1 \
  --resolve-conflicts OVERWRITE \
  --region $REGION
```

## SageMaker HyperPod Inference release notes: v3.3
<a name="sagemaker-hyperpod-inference-release-notes-20260804"></a>

**Release Date:** August 4, 2026

**Summary**

Amazon SageMaker HyperPod Inference Operator v3.3 introduces host-local model caching. This reduces cold-start latency when you scale out an inference deployment. This release also makes the Application Load Balancer idle timeout configurable for each deployment.

Amazon SageMaker HyperPod Inference Operator v3.3 is available in all AWS Regions where SageMaker HyperPod is supported.

**New Features**
+ **Model Weights and Image Caching** – Cache model weights on node-local NVMe storage and pre-pull the inference server container image onto target nodes. Pods added during scale-out do not download weights from Amazon S3 or Amazon FSx. They do not wait for a cold image pull. Enable either mechanism independently or both together by using `modelCacheConfig` in your CRD. This feature requires an instance type with local NVMe storage. See [Model weights caching and image caching](sagemaker-hyperpod-model-deployment-model-caching.md).
+ **Configurable ALB Idle Timeout** – Control how long the Application Load Balancer keeps an idle connection open by using `loadBalancer.idleTimeoutSeconds` on your `InferenceEndpointConfig` or `JumpStartModel`. Valid values are 1–4000 seconds, and the default is 60 seconds. Increase this value for deployments whose requests take longer than the default to return a response.

**Bug Fixes**
+ **Missing Routing Service** – Fixed an issue where an interrupted initial reconcile could leave a deployment without the Kubernetes routing Service. This Service backs the deployment's Ingress and load balancer. Endpoints returned HTTP 503 responses while all health signals reported healthy. The operator now re-creates the routing Service when it is missing.
+ **Intelligent Routing Endpoint Registration** – Fixed an issue where intelligent routing deployments used an unprefixed name for the Ingress path lookup. The lookup failed on every reconciliation, which prevented SageMaker AI endpoint registration from completing.
+ **KV Cache Configuration** – Fixed an issue where the operator did not honor `enableL1Cache` or `enableL2Cache` set to `false` in `kvCacheSpec`.

### Upgrade to v3.3
<a name="sagemaker-hyperpod-inference-v3-3-upgrade"></a>

**Helm upgrade:**

If you already have the Inference Operator installed by using Helm, use the following commands to upgrade:

```
helm get values -n kube-system hyperpod-inference-operator \
> current-values.yaml

cd sagemaker-hyperpod-cli/helm_chart/HyperPodHelmChart/\
charts/inference-operator

helm upgrade hyperpod-inference-operator . -n kube-system \
  -f current-values.yaml --set image.tag=v3.3

# Verification
kubectl get deployment hyperpod-inference-operator-controller-manager \
  -n hyperpod-inference-system \
  -o jsonpath='{.spec.template.spec.containers[0].image}'
```

**EKS Add-on upgrade:**

If you installed the Inference Operator as an EKS Add-on, upgrade to the latest version:

```
CLUSTER=EKS_CLUSTER_NAME
REGION=REGION

aws eks update-addon \
  --cluster-name $CLUSTER \
  --addon-name amazon-sagemaker-hyperpod-inference \
  --addon-version v1.4.0-eksbuild.1 \
  --resolve-conflicts OVERWRITE \
  --region $REGION
```

## SageMaker HyperPod Inference release notes: v3.2
<a name="sagemaker-hyperpod-inference-release-notes-20260612"></a>

**Release Date:** June 12, 2026

**Summary**

Inference Operator v3.2 enables customers to deploy long-context LLMs (such as Llama 3.3 70B) with predictable per-token latency under concurrent load. The release introduces Disaggregated Prefill and Decode (DPD), which separates the compute-bound prefill phase and the memory-bandwidth-bound decode phase onto distinct GPU pools and transfers KV cache between them over EFA with GPU-Direct RDMA. DPD reduces tail per-token latency, increases throughput, and lets you scale prefill and decode capacity independently. Besides DPD we include other bug fixes in this release.

**Key Features**

**Disaggregated Prefill and Decode (DPD)**
+ Added a new `pdSpec` field to the `InferenceEndpointConfig` CRD that enables disaggregated inference. When `pdSpec` is set, the operator provisions separate prefiller and decoder pods, wires them together via the DPD router, and transfers KV cache between them using LMCache over NIXL and EFA with GPU-Direct RDMA. Example configurable fields include (more config can check user guide):
  + `routingThreshold` – Token-length threshold above which requests use the disaggregated path. Below the threshold, requests bypass the prefiller and go directly to the decoder.
  + `prefillSpec.args` and `decodingSpec.args` – Per-role vLLM flags merged into `worker.args` at startup.
  + `prefillSpec.replicas` and `decodingSpec.replicas` – Scale prefill and decode capacity independently to match your workload's input and output length distribution.
+ **Prerequisite**
  + To deploy DPD endpoints, your cluster nodes must support EFA with RDMA read and write, and be located within the same Availability Zone for high-bandwidth node-to-node communication.
  + Recommended instance families: `ml.p5.48xlarge`, `ml.p5e.48xlarge`, `ml.p5en.48xlarge`, `ml.p6-b200.48xlarge`, `ml.p6-b300.48xlarge`.

**Bug Fixes**
+ **Operator scheduling on x86 nodes** – The operator deployment now uses `nodeAffinity` to schedule onto amd64 Linux nodes only.
+ We include other minor and security fixes.

### Upgrade to v3.2
<a name="sagemaker-hyperpod-inference-v3-2-upgrade"></a>

**Helm upgrade:**

If you already have the Inference Operator installed via Helm, use the following commands to upgrade:

```
helm get values -n kube-system hyperpod-inference-operator \
> current-values.yaml

cd sagemaker-hyperpod-cli/helm_chart/HyperPodHelmChart/\
charts/inference-operator

helm upgrade hyperpod-inference-operator . -n kube-system \
  -f current-values.yaml --set image.tag=v3.2

# Verification
kubectl get deployment hyperpod-inference-operator-controller-manager \
  -n hyperpod-inference-system \
  -o jsonpath='{.spec.template.spec.containers[0].image}'
```

**EKS Add-on upgrade:**

If you installed the Inference Operator as an EKS Add-on, upgrade to the latest version:

```
CLUSTER=EKS_CLUSTER_NAME
REGION=REGION

aws eks update-addon \
  --cluster-name $CLUSTER \
  --addon-name amazon-sagemaker-hyperpod-inference \
  --addon-version v1.3.0-eksbuild.1 \
  --resolve-conflicts OVERWRITE \
  --region $REGION
```

## SageMaker HyperPod Inference release notes: v3.1.2
<a name="sagemaker-hyperpod-inference-release-notes-20260506"></a>

**Release Date:** May 6, 2026

**Summary**

Inference Operator v3.1.2 introduces inference data capture for logging endpoint traffic, HuggingFace Hub integration for direct model deployment, Route 53 DNS management for custom domains, local NVMe model deployment for reduced cold-start latency, and custom service accounts with IRSA support.

**New Features**
+ **Inference Data Capture** – Record inputs and outputs at three capture points: SageMaker AI endpoint, load balancer (ALB access logs), and model pod. Enable any combination via `dataCapture` in your CRD. See [Data capture for inference on HyperPod](sagemaker-hyperpod-model-deployment-data-capture.md).
+ **HuggingFace Model Source** – Deploy models directly from HuggingFace Hub without pre-staging to S3 or FSx. Supports gated models via `tokenSecretRef`, revision pinning via `commitSHA`, and token isolation. Compatible with vLLM, TGI, and SGLang runtimes. See [Deploy models from Amazon S3, Amazon FSx, or Hugging Face Hub using kubectl](sagemaker-hyperpod-model-deployment-deploy-ftm.md).
+ **Route 53 DNS Management** – Automatically create and manage DNS records for custom domains via `dnsConfig`. See [Custom certificates and Route 53 DNS management for HyperPod Inference](sagemaker-hyperpod-model-deployment-custom-certs.md).
+ **Local NVMe Model Deployment** – Load model weights from node-local NVMe storage via `modelSourceType: kubernetesVolume` to reduce cold-start latency. Supports fallback to S3. See [Deploy models from local NVMe storage using kubectl](sagemaker-hyperpod-model-deployment-deploy-nvme.md).
+ **Custom Service Accounts** – Assign custom ServiceAccounts with IRSA support to inference pods via `spec.kubernetes.serviceAccountName`.

**Bug Fixes**
+ **Tag Propagation** – User-defined tags on `InferenceEndpointConfig` now propagate correctly to the `SageMakerEndpointRegistration` CRD and downstream SageMaker AI resources. Previously, tags were not passed during endpoint registration creation or updates.
+ **Autoscaling Replica Preservation** – Fixed an issue where updating an `InferenceEndpointConfig` or `JumpStartModel` CR would reset the replica count to the spec value, overriding the current HPA/KEDA-managed replica count. The operator now preserves the active replica count during CR updates.
+ **Autoscaling CRD Validation** – Fixed `prometheusTrigger.serverAddress` validation regex that incorrectly required a trailing path segment, causing 404 errors when KEDA appended `/api/v1/query` to the AMP workspace URL.
+ **Certificate Rotation** – Fixed custom certificate rotation not propagating to ALB after operator pod restart.

### Upgrade to v3.1.2
<a name="sagemaker-hyperpod-inference-v3-1-2-upgrade"></a>

**Helm upgrade:**

If you already have the Inference Operator installed via Helm, use the following commands to upgrade:

```
helm get values -n kube-system hyperpod-inference-operator \
> current-values.yaml

cd sagemaker-hyperpod-cli/helm_chart/HyperPodHelmChart/\
charts/inference-operator

helm upgrade hyperpod-inference-operator . -n kube-system \
  -f current-values.yaml --set image.tag=v3.1
    
# Verification
kubectl get deployment hyperpod-inference-operator-controller-manager \
  -n hyperpod-inference-system \
  -o jsonpath='{.spec.template.spec.containers[0].image}'
```

**EKS Add-on upgrade:**

If you installed the Inference Operator as an EKS Add-on, upgrade to the latest version.

First, check if `hyperpodClusterArn` is already in your add-on configuration:

```
CLUSTER=EKS_CLUSTER_NAME
REGION=REGION

aws eks describe-addon \
  --cluster-name $CLUSTER \
  --addon-name amazon-sagemaker-hyperpod-inference \
  --region $REGION \
  --query 'addon.configurationValues' --output text | jq .
```

If `hyperpodClusterArn` is present in the output, run the following command to upgrade:

```
aws eks update-addon \
  --cluster-name $CLUSTER \
  --addon-name amazon-sagemaker-hyperpod-inference \
  --addon-version v1.2.0-eksbuild.1 \
  --resolve-conflicts OVERWRITE \
  --region $REGION
```

If `hyperpodClusterArn` is not present, fetch the current configuration, add it, and upgrade:

```
HP_ARN=HYPERPOD_CLUSTER_ARN

CURRENT_CONFIG=$(aws eks describe-addon \
  --cluster-name $CLUSTER \
  --addon-name amazon-sagemaker-hyperpod-inference \
  --region $REGION \
  --query 'addon.configurationValues' --output text)

# Add hyperpodClusterArn to the configuration
NEW_CONFIG=$(echo "$CURRENT_CONFIG" | jq --arg arn "$HP_ARN" \
  '. + {hyperpodClusterArn: $arn}')

aws eks update-addon \
  --cluster-name $CLUSTER \
  --addon-name amazon-sagemaker-hyperpod-inference \
  --addon-version v1.2.0-eksbuild.1 \
  --configuration-values "$NEW_CONFIG" \
  --resolve-conflicts OVERWRITE \
  --region $REGION
```

Wait for the add-on to become active before deploying models.

## SageMaker HyperPod Inference release notes: v3.1
<a name="sagemaker-hyperpod-inference-release-notes-20260403"></a>

**Release Date:** April 3, 2026

**Summary**

Inference Operator v3.1 introduces custom Kubernetes pod configuration, custom certificate support, and per-pod request limits.

**Key Features**
+ **Custom Kubernetes Pod Configuration** – Added a new `kubernetes` field to the `InferenceEndpointConfig` CRD that allows users to customize inference pod configurations:
  + **Custom init containers** – Run user-defined init containers before the inference server starts (for example, cache warming, GDS setup). Init containers are injected after the operator's prefetch container.
  + **Custom volumes** – Add additional volumes (`emptyDir`, `hostPath`, `configMap`, etc.) to the pod spec, which can be referenced by init containers via `volumeMounts`.
  + **Custom scheduler name** – Specify a custom Kubernetes scheduler for pod placement.
+ **Custom Certificates** – Use your own ACM certificates for inference endpoints instead of operator-generated self-signed certificates, configured via `customCertificateConfig`. Supports publicly trusted ACM certificates, AWS Private CA certificates, and certificates imported from external CAs. The operator monitors certificate health and supports automatic renewal detection.
+ **Request Limits** – Control request handling per pod via the new `RequestLimits` configuration under `Worker`, with the following configurable fields:
  + `maxConcurrentRequests` – Maximum concurrent in-flight requests per pod.
  + `maxQueueSize` – Requests to queue when the concurrency limit is reached before rejecting.
  + `overflowStatusCode` – HTTP status code returned when limits are exceeded (default: 429).

For detailed information including prerequisites and upgrade instructions, see the sections below.

### Prerequisites
<a name="sagemaker-hyperpod-inference-v3-1-prerequisites"></a>

To use the Custom Certificates feature, add the following permissions to your Inference Operator execution role:

```
{  
    "Sid": "ACMCertificateAccess",  
    "Effect": "Allow",  
    "Action": [  
        "acm:DescribeCertificate",  
        "acm:GetCertificate"  
    ],  
    "Resource": "arn:aws:acm:*:*:certificate/*"  
}
```

### Upgrade to v3.1
<a name="sagemaker-hyperpod-inference-v3-1-upgrade"></a>

If you already have the Inference Operator installed via Helm, use the following commands to upgrade:

```
helm get values -n kube-system hyperpod-inference-operator \
> current-values.yaml

cd sagemaker-hyperpod-cli/helm_chart/HyperPodHelmChart/\
charts/inference-operator

helm upgrade hyperpod-inference-operator . -n kube-system \
  -f current-values.yaml --set image.tag=v3.1
    
# Verification
kubectl get deployment hyperpod-inference-operator-controller-manager \
  -n hyperpod-inference-system \
  -o jsonpath='{.spec.template.spec.containers[0].image}'
```

## SageMaker HyperPod Inference release notes: v3.0
<a name="sagemaker-hyperpod-inference-release-notes-20260223"></a>

**Release Date:** February 23, 2026

**Summary**

Inference Operator 3.0 introduces EKS Add-on integration for simplified lifecycle management, Node Affinity support for granular scheduling control, and improved resource tagging. Existing Helm-based installations can be migrated to the EKS Add-on using the provided migration script. Update your Inference Operator execution role with new tagging permissions before upgrading.

**Key Features**
+ **EKS Add-on Integration** – Enterprise-grade lifecycle management with simplified installation experience
+ **Node Affinity** – Granular scheduling control for excluding spot instances, preferring availability zones, or targeting nodes with custom labels

For detailed information including prerequisites, upgrade instructions, and migration guidance, see the sections below.

### Prerequisites
<a name="sagemaker-hyperpod-inference-v3-0-prerequisites"></a>

Before upgrading the Helm version to 3.0, customers should add additional tagging permissions to their Inference operator execution role. As part of improving resource tagging and security, the Inference Operator now tags ALB, S3, and ACM resources. This enhancement requires additional permissions in the Inference Operator execution role. Add the following permissions to your Inference Operator execution role:

```
{  
    "Sid": "CertificateTagginPermission",  
    "Effect": "Allow",  
    "Action": [  
        "acm:AddTagsToCertificate"  
    ],  
    "Resource": "arn:aws:acm:*:*:certificate/*",  
},  
{  
    "Sid": "S3PutObjectTaggingAccess",  
    "Effect": "Allow",  
    "Action": [  
        "s3:PutObjectTagging"  
    ],  
    "Resource": [  
        "arn:aws:s3:::<TLS_BUCKET>/*" # Replace * with your TLS bucket  
    ]  
}
```

### Upgrade to v3.0
<a name="sagemaker-hyperpod-inference-v3-0-upgrade"></a>

If you already have the Inference Operator installed via Helm, use the following commands to upgrade:

```
helm get values -n kube-system hyperpod-inference-operator \
> current-values.yaml

cd sagemaker-hyperpod-cli/helm_chart/HyperPodHelmChart/\
charts/inference-operator

helm upgrade hyperpod-inference-operator . -n kube-system \
  -f current-values.yaml --set image.tag=v3.0
    
# Verification
kubectl get deployment hyperpod-inference-operator-controller-manager \
  -n hyperpod-inference-system \
  -o jsonpath='{.spec.template.spec.containers[0].image}'
```

### Helm to EKS Add-on Migration
<a name="sagemaker-hyperpod-inference-v3-0-migration"></a>

If Inference operator is installed through Helm before 3.0 version, we recommend migrating to EKS Add-on to get timely updates on the new features that will be released for Inference Operator. This script migrates the SageMaker HyperPod Inference Operator from Helm-based installation to EKS Add-on installation.

**Overview:** The script takes a cluster name and region as parameters, retrieves the existing Helm installation configuration, and migrates to EKS Add-on deployment. It creates new IAM roles for the Inference Operator, ALB Controller, and KEDA Operator.

Before migrating the Inference Operator, the script ensures required dependencies (S3 CSI driver, FSx CSI driver, cert-manager, and metrics-server) exist. If they don't exist, it deploys them as Add-on.

After the Inference Operator Add-on migration completes, the script also migrates S3, FSx, and other dependencies (ALB, KEDA, cert-manager, metrics-server) if they were originally installed via the Inference Operator Helm chart. Use `--skip-dependencies-migration` to skip this step for S3 CSI driver, FSx CSI driver, cert-manager, and metrics-server. Note that ALB and KEDA are installed as part of the Add-on in the same namespace as Inference Operator, and will be migrated as part of the Inference Operator Add-on.

**Important**  
During the migration, do not deploy new models as they will not be deployed until the migration is completed. Once the Inference Operator Add-on is in ACTIVE state, new models can be deployed. Migration time typically takes 15 to 20 minutes, and it can complete within 30 minutes if only a few models are currently deployed.

**Migration Prerequisites:**
+ AWS CLI configured with appropriate credentials
+ kubectl configured with access to your EKS cluster
+ Helm installed
+ Existing Helm installation of hyperpod-inference-operator

**Note**  
Endpoints that are already running will not be interrupted during the migration process. Existing endpoints will continue to serve traffic without disruption throughout the migration.

**Getting the Migration Script:**

```
git clone https://github.com/aws/sagemaker-hyperpod-cli.git
cd sagemaker-hyperpod-cli/helm_chart/HyperPodHelmChart/\
charts/inference-operator/migration
```

**Usage:**

```
./helm_to_addon.sh [OPTIONS] \
  --cluster-name <cluster-name> (Required) \
  --region <region> (Required) \
  --helm-namespace kube-system (Optional) \
  --auto-approve (Optional) \
  --skip-dependencies-migration (Optional) \
  --s3-mountpoint-role-arn <s3-mountpoint-role-arn> (Optional) \
  --fsx-role-arn <fsx-role-arn> (Optional)
```

**Options:**
+ `--cluster-name NAME` – EKS cluster name (required)
+ `--region REGION` – AWS region (required)
+ `--helm-namespace NAMESPACE` – Namespace where Helm chart is installed (default: kube-system) (optional)
+ `--s3-mountpoint-role-arn ARN` – S3 Mountpoint CSI driver IAM role ARN (optional)
+ `--fsx-role-arn ARN` – FSx CSI driver IAM role ARN (optional)
+ `--auto-approve` – Skip confirmation prompts if this flag is enabled. `step-by-step` and `auto-approve` are mutually exclusive, if `--auto-approve` is given, do not specify `--step-by-step` (optional)
+ `--step-by-step` – Pause after each major step for review. This should not be mentioned if `--auto-approve` is already added (optional)
+ `--skip-dependencies-migration` – Skip migration of Helm-installed dependencies to Add-on. For dependencies were NOT installed via the Inference Operator Helm chart, or if you want to manage them separately. (optional)

**Examples:**

Basic migration (migrates dependencies):

```
./helm_to_addon.sh \
  --cluster-name my-cluster \
  --region us-east-1
```

Auto-approve without prompts:

```
./helm_to_addon.sh \
  --cluster-name my-cluster \
  --region us-east-1 \
  --auto-approve
```

Skip dependency migration for FSx, S3 mountpoint, cert manager and Metrics server:

```
./helm_to_addon.sh \
  --cluster-name my-cluster \
  --region us-east-1 \
  --skip-dependencies-migration
```

Provide existing S3 and FSx IAM roles:

```
./helm_to_addon.sh \
  --cluster-name my-cluster \
  --region us-east-1 \
  --s3-mountpoint-role-arn arn:aws:iam::123456789012:role/s3-csi-role \
  --fsx-role-arn arn:aws:iam::123456789012:role/fsx-csi-role
```

**Backup Location:**

Backups are stored in `/tmp/hyperpod-migration-backup-<timestamp>/`

Backups enable safe migration and recovery:
+ **Rollback on Failure** – If migration fails, the script can automatically restore your cluster to its pre-migration state using the backed up configurations
+ **Audit Trail** – Provides a complete record of what existed before migration for troubleshooting and compliance
+ **Configuration Reference** – Allows you to compare pre-migration and post-migration configurations
+ **Manual Recovery** – If needed, you can manually inspect and restore specific resources from the backup directory

**Rollback:**

If migration fails, the script prompts for user confirmation before initiating rollback to restore the previous state.

## SageMaker HyperPod Inference release notes: v2.3
<a name="sagemaker-hyperpod-inference-release-notes-20260203"></a>

**What's new**

This release introduces new optional fields in the Custom Resource Definitions (CRDs) to enhance deployment configuration flexibility.

**Features**
+ **Multi Instance Types**
  + **Enhanced deployment reliability** – Supports multi-instance type configurations with automatic failover to alternative instance types when preferred options lack capacity
  + **Intelligent resource scheduling** – Uses Kubernetes node affinity to prioritize instance types while guaranteeing deployment even when preferred resources are unavailable
  + **Optimized cost and performance** – Maintains your instance type preferences and prevents capacity-related failures during cluster fluctuations

**Bug Fixes**

Changes to the field `invocationEndpoint` in the spec of the `InferenceEndpointConfig` will now take effect:
+ If the `invocationEndpoint` field is patched or updated, dependent resources, such as the `Ingress`, the Load Balancer, `SageMakerEndpointRegistration`, and SageMaker Endpoint, will be updated with normalisation.
+ The value for `invocationEndpoint` provided will be stored as-is in the `InferenceEndpointConfig` spec itself. When this value is used to create a Load Balancer and— if enabled— a SageMaker Endpoint, it will be normalised to have one leading forward slash.
  + `v1/chat/completions` will be normalised to `/v1/chat/completions` for the `Ingress`, AWS Load Balancer, and SageMaker Endpoint. For the `SageMakerEndpointRegistration`, it will be displayed in its spec as `v1/chat/completions`.
  + `///invoke` will be normalised to `/invoke` for the `Ingress`, AWS Load Balancer, and SageMaker Endpoint. For the `SageMakerEndpointRegistration`, it will be displayed in its spec as `invoke`.

**Installing Helm:**

Follow: [https://github.com/aws/sagemaker-hyperpod-cli/tree/main/helm\_chart](https://github.com/aws/sagemaker-hyperpod-cli/tree/main/helm_chart)

If you are focused on only installing the inference operator, after step 1 i.e. `Set Up Your Helm Environment`, do `cd HyperPodHelmChart/charts/inference-operator`. Since you are in the inference operator chart directory itself, in the commands, wherever you see `helm_chart/HyperPodHelmChart`, replace with `.` .

**Upgrade Operator to v2.3 in case already installed:**

```
cd sagemaker-hyperpod-cli/helm_chart/HyperPodHelmChart/\
charts/inference-operator

helm get values -n kube-system hyperpod-inference-operator \
> current-values.yaml

helm upgrade hyperpod-inference-operator . \
  -n kube-system \
  -f current-values.yaml \
  --set image.tag=v2.3
```