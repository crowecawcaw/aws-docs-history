

# AWS Glue for Ray end of support
<a name="awsglue-ray-jobs-availability-change"></a>

**Important**  
AWS Glue for Ray is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [AWS Glue for Ray end of support](https://docs.aws.amazon.com/glue/latest/dg/awsglue-ray-jobs-availability-change.html).

After careful consideration, we decided to close AWS Glue for Ray to new customers starting April 30, 2026. If you would like to use AWS Glue for Ray, sign up prior to that date. Existing customers can continue to use the service as normal.

AWS continues to invest in security and availability improvements for AWS Glue for Ray. Note that we do not plan to introduce new features to AWS Glue for Ray, except for security and availability enhancements.

As an alternative to AWS Glue for Ray, we recommend using Amazon Elastic Kubernetes Service. Amazon Elastic Kubernetes Service is a fully managed, certified Kubernetes conformant service that simplifies the process of building, securing, operating, and maintaining Kubernetes clusters on AWS. It is a highly customizable option that relies on open-source KubeRay Operator to deploy and manage Ray clusters on Kubernetes, offering improved resource utilization, simplified infrastructure management, and full support for Ray features.

## Migrating a Ray job to Amazon Elastic Kubernetes Service
<a name="awsglue-ray-jobs-availability-change-migration"></a>

This section provides steps for migrating from AWS Glue for Ray to Ray on Amazon Elastic Kubernetes Service. These steps are helpful for two migration scenarios:
+ **Standard Migration (x86/amd64)**: For these use cases, the migration strategy uses OpenSource Ray container for basic implementations and executes scripts directly on the base container.
+ **ARM64 Migration**: For these use cases, the migration strategy supports custom container builds for ARM64-specific dependencies and architecture requirements.

### Prerequisites for migration
<a name="awsglue-ray-jobs-availability-change-prerequisites"></a>

Install the following CLI tools: **aws**, **kubectl**, **eksctl**, **helm**, Python 3.9\+. These CLI tools are required to provision and manage your Ray on EKS environment. **eksctl** simplifies creating and managing EKS clusters. **kubectl** is the standard Kubernetes CLI for deploying and troubleshooting workloads on your cluster. **helm** is used to install and manage KubeRay (the operator that runs Ray on Kubernetes). Python 3.9\+ is required for Ray itself and to run job submission scripts locally.

#### Install eksctl
<a name="awsglue-ray-jobs-availability-change-install-eksctl"></a>

Follow the instructions on [Installation options for Eksctl](https://docs.aws.amazon.com/eks/latest/eksctl/installation.html) or use the instructions below for installation.

For macOS:

```
brew tap weaveworks/tap
brew install weaveworks/tap/eksctl
```

For Linux:

```
curl --silent --location "https://github.com/weaveworks/eksctl/releases/latest/download/eksctl_$(uname -s)_amd64.tar.gz" | tar xz -C /tmp

# Move the extracted binary to /usr/local/bin
sudo mv /tmp/eksctl /usr/local/bin

# Test the installation
eksctl version
```

#### Install kubectl
<a name="awsglue-ray-jobs-availability-change-install-kubectl"></a>

Follow the instructions on [Set up kubectl and eksctl](https://docs.aws.amazon.com/eks/latest/userguide/install-kubectl.html) or use the instructions below for installation.

For macOS:

```
brew install kubectl
```

For Linux:

```
curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"
chmod +x kubectl
sudo mv kubectl /usr/local/bin/
```

#### Install helm
<a name="awsglue-ray-jobs-availability-change-install-helm"></a>

Follow the instructions on [Installing Helm](https://helm.sh/docs/intro/install/) or use the instructions below for installation.

For macOS:

```
brew install helm
```

For Linux:

```
curl https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3 | bash
```

### Step 1. Build or choose a Docker Image for Ray
<a name="awsglue-ray-jobs-availability-change-step1"></a>

**Option 1: Use the official Ray image (no build required)**

This option uses the official Ray Docker image on [Docker Hub](https://hub.docker.com/u/rayproject), for example `rayproject/ray:2.4.0-py39`, which is maintained by the Ray project.

**Note**  
This image is amd64-only. Use this if your dependencies are compatible with amd64 and you don't require ARM-specific builds.

**Option 2: Build and publish your own arm64 Ray 2.4.0 image**

This option is useful when using Graviton (ARM) nodes, consistent with what AWS Glue for Ray uses internally. You can create a custom image pinned to the same dependency versions as AWS Glue for Ray, to reduce compatibility mismatches.

Create a Dockerfile locally:

```
# Build an ARM64 image
FROM --platform=linux/arm64 python:3.9-slim-bullseye
# Handy tools: wget for KubeRay probes; CA certs; keep image small
RUN apt-get update && apt-get install -y --no-install-recommends \
    wget ca-certificates \
    && rm -rf /var/lib/apt/lists/*

# Keep pip/setuptools modern enough for wheels resolution
RUN python -m pip install -U "pip<24" "setuptools<70" wheel

# ---- Install Ray 2.4.0 (ARM64 / Py3.9) and Glue-like dependencies ----
# 1) Download the exact Ray 2.4.0 wheel for aarch64 (no network at runtime)
RUN python -m pip download --only-binary=:all: --no-deps --dest /tmp/wheels ray==2.4.0

# 2) Core libs used in Glue (pin to Glue-era versions)
#    + the dashboard & jobs API dependencies compatible with Ray 2.4.0.
#    (Pins matter: newer major versions break 2.4.0's dashboard.)
RUN python -m pip install --no-cache-dir \
    /tmp/wheels/ray-2.4.0-*.whl \
    "pyarrow==11.0.0" \
    "pandas==1.5.3" \
    "boto3==1.26.133" \
    "botocore==1.29.133" \
    "numpy==1.24.3" \
    "fsspec==2023.4.0" \
    "protobuf<4" \
    # --- dashboard / jobs server deps ---
    "aiohttp==3.8.5" \
    "aiohttp-cors==0.7.0" \
    "yarl<1.10" "multidict<7.0" "frozenlist<1.4" "aiosignal<1.4" "async_timeout<5" \
    "pydantic<2" \
    "opencensus<0.12" \
    "prometheus_client<0.17" \
    # --- needed if using py_modules ---
    "smart_open[s3]==6.4.0"

# Optional: prove Ray & arch at container start
ENV PYTHONUNBUFFERED=1
WORKDIR /app

# KubeRay overrides the start command; this is just a harmless default
CMD ["python","-c","import ray,platform; print('Ray', ray.__version__, 'on', platform.machine())"]
```

```
# Set environment variables
export AWS_REGION=us-east-1
export AWS_ACCOUNT=$(aws sts get-caller-identity --query Account --output text)
export REPO=ray-2-4-arm64
export IMAGE=${AWS_ACCOUNT}.dkr.ecr.${AWS_REGION}.amazonaws.com/${REPO}:v1

# Create repository and login
aws ecr create-repository --repository-name $REPO >/dev/null 2>&1 || true
aws ecr get-login-password --region $AWS_REGION \
  | docker login --username AWS --password-stdin ${AWS_ACCOUNT}.dkr.ecr.${AWS_REGION}.amazonaws.com

# Enable Buildx (for cross-builds on non-ARM hosts)
docker buildx create --name multi --driver docker-container --use 2>/dev/null || true

# Build & push ARM64 image
docker buildx build \
  --platform linux/arm64 \
  -t "$IMAGE" \
  . --push

# Verify the image architecture remotely
aws ecr batch-get-image \
  --repository-name $REPO \
  --image-ids imageTag=v1 \
  --accepted-media-types application/vnd.docker.distribution.manifest.v2+json \
  | jq -r '.images[0].imageManifest' \
  | jq -r 'fromjson.config.digest'
```

Once done, reference this ARM64 image in the RayCluster spec with `nodeSelector: { kubernetes.io/arch: arm64 }`.

```
spec:
  rayVersion: "2.4.0"
  headGroupSpec:
    template:
      spec:
        containers:
        - name: ray-head
          image: <your ECR image>
```

### Step 2. Convert AWS Glue for Ray Job Configuration to Ray on Amazon Elastic Kubernetes Service
<a name="awsglue-ray-jobs-availability-change-step2"></a>

AWS Glue for Ray jobs support a set of job arguments that configure workers, dependencies, memory, and logging. When migrating to Amazon Elastic Kubernetes Service with KubeRay, these arguments need to be translated into RayCluster spec fields or Ray Job runtime environment settings.

#### Job Argument Mapping
<a name="awsglue-ray-jobs-availability-change-job-argument-mapping"></a>


**Mapping AWS Glue for Ray Arguments to Ray on EKS Equivalents**  

| AWS Glue for Ray argument | What it does in AWS Glue for Ray | Ray on Amazon Elastic Kubernetes Service equivalent | 
| --- | --- | --- | 
| --min-workers | Minimum workers the job must allocate. | workerGroupSpecs[].minReplicas in your RayCluster | 
| --working-dir | Distributes a zip (S3 URI) to all nodes. | Use Ray runtime env: working\_dir if you're submitting from local files; py\_modules for S3 zips to point at the S3 artifact | 
| --s3-py-modules | Adds Python wheels/dists from S3. | Use Ray runtime env: py\_modules: ["s3://.../xxx.whl", ...] | 
| --pip-install | Installs extra PyPI packages for the job. | Ray runtime env: pip: ["pkg==ver", ...] (Ray Job CLI --runtime-env-json or RayJob runtimeEnvYAML). | 
| --object\_store\_memory\_head | % of memory for head node's Plasma store. | headGroupSpec[].rayStartParams.object-store-memory in your RayCluster. Note this should be in bytes. AWS Glue uses percentage, while Ray uses bytes. | 
| --object\_store\_memory\_worker | % of memory for worker nodes' Plasma store. | Same as above but set in each worker group's rayStartParams.object-store-memory (bytes). | 
| --object\_spilling\_config | Configure Ray object spilling. | headGroupSpec[].rayStartParams.object-spilling-config | 
| --logging\_configuration | AWS Glue-managed logs (CloudWatch, S3). | Check pod stdout/stderr: use kubectl -n ray logs <pod-name> --follow. Check logs from Ray Dashboard (port-forward to :8265), you can also see task and job logs there. | 

#### Job Configuration Mapping
<a name="awsglue-ray-jobs-availability-change-job-config-mapping"></a>


**Mapping AWS Glue for Ray Job Configurations to Ray on EKS Equivalents**  

| Configuration | What it does in AWS Glue for Ray | Ray on EKS equivalent | 
| --- | --- | --- | 
| Worker type | Set the type of predefined worker that is allowed when a job runs. Default to Z 2X (8vCPU, 64 GB RAM). | Nodegroup instance type in EKS (e.g., r7g.2xlarge ≈ 8 vCPU / 64 GB for ARM, r7a.2xlarge for x86). | 
| Maximum number of workers | The number of workers you want AWS Glue to allocate to this job. | Set workerGroupSpecs[].maxReplicas to the same number of what you used in AWS Glue. This is the upper bound for autoscaling. Similarly set minReplicas as lower bound. You can start with replicas: 0, minReplicas: 0. | 

### Step 3. Setup Amazon Elastic Kubernetes Service
<a name="awsglue-ray-jobs-availability-change-step3"></a>

You can either create a new Amazon Elastic Kubernetes Service cluster or reuse an existing Amazon Elastic Kubernetes Service cluster. If using an existing cluster, skip the create cluster commands and jump to Add a node group, IRSA, and install KubeRay.

#### Create an Amazon Elastic Kubernetes Service cluster
<a name="awsglue-ray-jobs-availability-change-create-cluster"></a>

**Note**  
If you have an existing Amazon Elastic Kubernetes Service cluster, skip the commands to create a new cluster and just add a node group.

```
# Environment Variables
export AWS_REGION=us-east-1
export CLUSTER=ray-eks
export NS=ray # namespace for your Ray jobs (you can reuse another if you like)

# Create a cluster (OIDC is required for IRSA)
eksctl create cluster \
  --name $CLUSTER \
  --region $AWS_REGION \
  --with-oidc \
  --managed
```

#### Add a node group
<a name="awsglue-ray-jobs-availability-change-add-nodegroup"></a>

```
# ARM/Graviton (matches Glue's typical runtime):
eksctl create nodegroup \
  --cluster $CLUSTER \
  --region $AWS_REGION \
  --name arm64-ng \
  --node-type m7g.large \
  --nodes 2 --nodes-min 1 --nodes-max 5 \
  --managed \
  --node-labels "workload=ray"

# x86/amd64 (use if your image is amd64-only):
eksctl create nodegroup \
  --cluster $CLUSTER \
  --region $AWS_REGION \
  --name amd64-ng \
  --node-type m5.large \
  --nodes 2 --nodes-min 1 --nodes-max 5 \
  --managed \
  --node-labels "workload=ray"
```

**Note**  
If you are using an existing Amazon Elastic Kubernetes Service cluster, then use `--with-oidc` to enable OIDC when adding a node group.

#### Create namespace \+ IAM role for Service Accounts (IRSA) for S3
<a name="awsglue-ray-jobs-availability-change-irsa"></a>

A Kubernetes namespace is a logical grouping for resources (pods, services, roles, etc.). You can create or reuse an existing namespace. You will also need to create an IAM policy for S3 which mirrors your AWS Glue job's access. Use the same custom permissions your AWS Glue job role had (typically S3 read/write to specific buckets). To grant permissions to Amazon Elastic Kubernetes Service similar to the AWSGlueServiceRole, create a Service Account (IRSA) bound to this IAM policy. Refer to [IAM Roles for Service Accounts](https://docs.aws.amazon.com/eks/latest/eksctl/iamserviceaccounts.html) for instructions to setup this service account.

```
# Create (or reuse) namespace
kubectl create namespace $NS || true
```

```
{
  "Version": "2012-10-17",		 	 	 
  "Statement": [{
    "Effect": "Allow",
    "Action": ["s3:PutObject", "s3:GetObject", "s3:ListBucket"],
    "Resource": [
      "arn:aws:s3:::YOUR-BUCKET",
      "arn:aws:s3:::YOUR-BUCKET/*"
    ]
  }]
}
```

```
# Create the IAM policy and wire IRSA:
aws iam create-policy \
  --policy-name RayS3Policy \
  --policy-document file://example.json || true

# Create a service account (IRSA) bound to that policy.
eksctl create iamserviceaccount \
  --cluster $CLUSTER \
  --region $AWS_REGION \
  --namespace $NS \
  --name ray-s3-access \
  --attach-policy-arn arn:aws:iam::${AWS_ACCOUNT}:policy/RayS3Policy \
  --approve \
  --override-existing-serviceaccounts
```

#### Install KubeRay operator (controller that runs Ray on K8s)
<a name="awsglue-ray-jobs-availability-change-install-kuberay"></a>

```
helm repo add kuberay https://ray-project.github.io/kuberay-helm/
helm repo update
helm upgrade --install kuberay-operator kuberay/kuberay-operator \
  --namespace kuberay-system \
  --create-namespace

# Validate the operator pod Running
kubectl -n kuberay-system get pods
```

### Step 4. Spin up a Ray cluster
<a name="awsglue-ray-jobs-availability-change-step4"></a>

Create a YAML file to define ray cluster. Below is a sample configuration (raycluster.yaml):

```
apiVersion: ray.io/v1
kind: RayCluster
metadata:
  name: glue-like
  namespace: ray
spec:
  rayVersion: "2.4.0"
  headGroupSpec:
    template:
      spec:
        nodeSelector:
          kubernetes.io/arch: amd64
        serviceAccountName: ray-s3-access
        containers:
        - name: ray-head
          image: rayproject/ray:2.4.0-py39
          imagePullPolicy: Always
          resources:
            requests: { cpu: "1", memory: "2Gi" }
            limits:   { cpu: "1", memory: "2Gi" }
  workerGroupSpecs:
  - groupName: workers
    replicas: 0 # start with just a head (like small Glue dev job) and turn number of replicas later
    minReplicas: 0
    maxReplicas: 5
    template:
      spec:
        nodeSelector:
          kubernetes.io/arch: amd64
        serviceAccountName: ray-s3-access
        containers:
        - name: ray-worker
          image: rayproject/ray:2.4.0-py39
          imagePullPolicy: Always
          resources:
            requests: { cpu: "1", memory: "2Gi" }
            limits:   { cpu: "1", memory: "2Gi" }
```

#### Deploy the Ray cluster on Amazon Elastic Kubernetes Service cluster
<a name="awsglue-ray-jobs-availability-change-deploy-cluster"></a>

```
kubectl apply -n $NS -f raycluster.yaml

# Validate that the head pod turns to READY/ RUNNING state
kubectl -n $NS get pods -l ray.io/cluster=glue-like -w
```

If there is a need to modify the deployed yaml, delete the cluster first and then re-apply the updated yaml:

```
kubectl -n $NS delete raycluster glue-like
kubectl -n $NS apply -f raycluster.yaml
```

#### Accessing the Ray Dashboard
<a name="awsglue-ray-jobs-availability-change-ray-dashboard"></a>

You can access the Ray dashboard by enabling port-forwarding using kubectl:

```
# Get service
SVC=$(kubectl -n $NS get svc -l ray.io/cluster=glue-like,ray.io/node-type=head -o jsonpath='{.items[0].metadata.name}')

# Make the Ray dashboard accessible at http://localhost:8265 on your local machine.
kubectl -n $NS port-forward svc/$SVC 8265:8265
```

### Step 5. Submit Ray Job
<a name="awsglue-ray-jobs-availability-change-step5"></a>

To submit a Ray job, use the Ray jobs CLI. The CLI version can be newer than the cluster, it is backward compatible. As a pre-requisite, store your job script locally in a file, e.g. `job.py`.

```
python3 -m venv ~/raycli && source ~/raycli/bin/activate
pip install "ray[default]==2.49.2"

# Submit your ray job by supplying all python dependencies that was added to your Glue job
ray job submit --address http://127.0.0.1:8265 --working-dir . \
  --runtime-env-json '{
    "pip": ["boto3==1.28.*","pyarrow==12.*","pandas==2.0.*"]
  }' \
  -- python job.py
```

The job can be monitored on the Ray dashboard.