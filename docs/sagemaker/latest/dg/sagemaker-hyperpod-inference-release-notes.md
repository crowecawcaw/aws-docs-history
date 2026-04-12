# Amazon SageMaker HyperPod Inference release notes

This topic covers release notes that track updates, fixes, and new features for
Amazon SageMaker HyperPod Inference. SageMaker HyperPod Inference enables you to deploy and scale machine
learning models on your HyperPod clusters with enterprise-grade reliability. For general
Amazon SageMaker HyperPod platform releases, updates, and improvements, see [Amazon SageMaker HyperPod release notes](sagemaker-hyperpod-release-notes.md "sagemaker-hyperpod-release-notes.md").

For information about SageMaker HyperPod Inference capabilities and deployment options, see
[Deploying models on Amazon SageMaker HyperPod](sagemaker-hyperpod-model-deployment.md "sagemaker-hyperpod-model-deployment.md").

## SageMaker HyperPod Inference release notes: v3.1

**Release Date:** April 3, 2026

**Summary**

Inference Operator v3.1 introduces custom Kubernetes pod configuration, custom
certificate support, and per-pod request limits.

**Key Features**

- **Custom Kubernetes Pod Configuration** – Added
  a new `kubernetes` field to the `InferenceEndpointConfig`
  CRD that allows users to customize inference pod configurations:
  - **Custom init containers** – Run
    user-defined init containers before the inference server starts (for example,
    cache warming, GDS setup). Init containers are injected after the
    operator's prefetch container.
  - **Custom volumes** – Add additional
    volumes (`emptyDir`, `hostPath`,
    `configMap`, etc.) to the pod spec, which can be referenced
    by init containers via `volumeMounts`.
  - **Custom scheduler name** – Specify a
    custom Kubernetes scheduler for pod placement.

- **Custom Certificates** – Use your own ACM
  certificates for inference endpoints instead of operator-generated self-signed
  certificates, configured via `customCertificateConfig`. Supports
  publicly trusted ACM certificates, AWS Private CA certificates, and
  certificates imported from external CAs. The operator monitors certificate
  health and supports automatic renewal detection.
- **Request Limits** – Control request handling
  per pod via the new `RequestLimits` configuration under
  `Worker`, with the following configurable fields:
  - `maxConcurrentRequests` – Maximum concurrent in-flight
    requests per pod.
  - `maxQueueSize` – Requests to queue when the concurrency
    limit is reached before rejecting.
  - `overflowStatusCode` – HTTP status code returned when
    limits are exceeded (default: 429).

For detailed information including prerequisites and upgrade instructions, see the
sections below.

### Prerequisites

To use the Custom Certificates feature, add the following permissions to your
Inference Operator execution role:

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

If you already have the Inference Operator installed via Helm, use the following
commands to upgrade:

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

**Release Date:** February 23, 2026

**Summary**

Inference Operator 3.0 introduces EKS Add-on integration for simplified lifecycle
management, Node Affinity support for granular scheduling control, and improved resource
tagging. Existing Helm-based installations can be migrated to the EKS Add-on using the
provided migration script. Update your Inference Operator execution role with new tagging
permissions before upgrading.

**Key Features**

- **EKS Add-on Integration** – Enterprise-grade
  lifecycle management with simplified installation experience
- **Node Affinity** – Granular scheduling control
  for excluding spot instances, preferring availability zones, or targeting nodes
  with custom labels

For detailed information including prerequisites, upgrade instructions, and migration
guidance, see the sections below.

### Prerequisites

Before upgrading the Helm version to 3.0, customers should add additional tagging
permissions to their Inference operator execution role. As part of improving resource
tagging and security, the Inference Operator now tags ALB, S3, and ACM resources. This
enhancement requires additional permissions in the Inference Operator execution role.
Add the following permissions to your Inference Operator execution role:

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

If Inference operator is installed through Helm before 3.0 version, we recommend
migrating to EKS Add-on to get timely updates on the new features that will be released
for Inference Operator. This script migrates the SageMaker HyperPod Inference Operator from
Helm-based installation to EKS Add-on installation.

**Overview:** The script takes a cluster name and region
as parameters, retrieves the existing Helm installation configuration, and migrates to
EKS Add-on deployment. It creates new IAM roles for the Inference Operator, ALB
Controller, and KEDA Operator.

Before migrating the Inference Operator, the script ensures required dependencies
(S3 CSI driver, FSx CSI driver, cert-manager, and metrics-server) exist. If they don't
exist, it deploys them as Add-on.

After the Inference Operator Add-on migration completes, the script also migrates
S3, FSx, and other dependencies (ALB, KEDA, cert-manager, metrics-server) if they were
originally installed via the Inference Operator Helm chart. Use
`--skip-dependencies-migration` to skip this step for S3 CSI driver, FSx CSI
driver, cert-manager, and metrics-server. Note that ALB and KEDA are installed as part
of the Add-on in the same namespace as Inference Operator, and will be migrated as part
of the Inference Operator Add-on.

###### Important

During the migration, do not deploy new models as they will not be deployed until
the migration is completed. Once the Inference Operator Add-on is in ACTIVE state,
new models can be deployed. Migration time typically takes 15 to 20 minutes, and it
can complete within 30 minutes if only a few models are currently deployed.

**Migration Prerequisites:**

- AWS CLI configured with appropriate credentials
- kubectl configured with access to your EKS cluster
- Helm installed
- Existing Helm installation of hyperpod-inference-operator

###### Note

Endpoints that are already running will not be interrupted during the migration
process. Existing endpoints will continue to serve traffic without disruption
throughout the migration.

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

- `--cluster-name NAME` – EKS cluster name (required)
- `--region REGION` – AWS region (required)
- `--helm-namespace NAMESPACE` – Namespace where Helm chart is
  installed (default: kube-system) (optional)
- `--s3-mountpoint-role-arn ARN` – S3 Mountpoint CSI driver
  IAM role ARN (optional)
- `--fsx-role-arn ARN` – FSx CSI driver IAM role ARN (optional)
- `--auto-approve` – Skip confirmation prompts if this flag is
  enabled. `step-by-step` and `auto-approve` are mutually exclusive,
  if `--auto-approve` is given, do not specify `--step-by-step`
  (optional)
- `--step-by-step` – Pause after each major step for review.
  This should not be mentioned if `--auto-approve` is already added (optional)
- `--skip-dependencies-migration` – Skip migration of
  Helm-installed dependencies to Add-on. For dependencies were NOT installed via
  the Inference Operator Helm chart, or if you want to manage them separately. (optional)

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

- **Rollback on Failure** – If migration
  fails, the script can automatically restore your cluster to its pre-migration state
  using the backed up configurations
- **Audit Trail** – Provides a complete
  record of what existed before migration for troubleshooting and compliance
- **Configuration Reference** – Allows you
  to compare pre-migration and post-migration configurations
- **Manual Recovery** – If needed, you can
  manually inspect and restore specific resources from the backup directory

**Rollback:**

If migration fails, the script prompts for user confirmation before initiating
rollback to restore the previous state.

## SageMaker HyperPod Inference release notes: v2.3

**What's new**

This release introduces new optional fields in the Custom Resource Definitions (CRDs)
to enhance deployment configuration flexibility.

**Features**

- **Multi Instance Types**
  - **Enhanced deployment reliability** – Supports
    multi-instance type configurations with automatic failover to alternative
    instance types when preferred options lack capacity
  - **Intelligent resource scheduling** – Uses
    Kubernetes node affinity to prioritize instance types while guaranteeing
    deployment even when preferred resources are unavailable
  - **Optimized cost and performance** – Maintains
    your instance type preferences and prevents capacity-related failures during
    cluster fluctuations

**Bug Fixes**

Changes to the field `invocationEndpoint` in the spec of the
`InferenceEndpointConfig` will now take effect:

- If the `invocationEndpoint` field is patched or updated, dependent
  resources, such as the `Ingress`, the Load Balancer,
  `SageMakerEndpointRegistration`, and SageMaker Endpoint, will be
  updated with normalisation.
- The value for `invocationEndpoint` provided will be stored as-is
  in the `InferenceEndpointConfig` spec itself. When this value is used
  to create a Load Balancer and— if enabled— a SageMaker Endpoint, it will be
  normalised to have one leading forward slash.
  - `v1/chat/completions` will be normalised to
    `/v1/chat/completions` for the `Ingress`, AWS Load
    Balancer, and SageMaker Endpoint. For the
    `SageMakerEndpointRegistration`, it will be displayed in its
    spec as `v1/chat/completions`.
  - `///invoke` will be normalised to `/invoke` for
    the `Ingress`, AWS Load Balancer, and SageMaker Endpoint. For
    the `SageMakerEndpointRegistration`, it will be displayed in
    its spec as `invoke`.

**Installing Helm:**

Follow: [https://github.com/aws/sagemaker-hyperpod-cli/tree/main/helm_chart](https://github.com/aws/sagemaker-hyperpod-cli/tree/main/helm_chart "https://github.com/aws/sagemaker-hyperpod-cli/tree/main/helm_chart")

If you are focused on only installing the inference operator, after step 1 i.e.
`Set Up Your Helm Environment`, do
`cd HyperPodHelmChart/charts/inference-operator`. Since you are in the
inference operator chart directory itself, in the commands, wherever you see
`helm_chart/HyperPodHelmChart`, replace with `.` .

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
