**Help improve this page**

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Best Practices Cluster Setup Guide for Real-Time Inference on Amazon EKS

## Introduction

This guide offers a hands-on walkthrough for setting up an Amazon Elastic Kubernetes Service (EKS) cluster optimized for real-time online inference workloads, incorporating best practices curated by AWS experts throughout. It uses an opinionated EKS Quickstart Architecture—a curated set of drivers, instance types, and configurations aligned with AWS best practices for models, accelerators, and scaling. This approach helps you bypass the task of selecting cluster settings, allowing you to get a functional, pre-configured cluster up and running quickly. Along the way, we’ll deploy sample workloads to validate your setup, explain key architectural concepts (such as decoupling CPU-bound tasks from GPU-intensive computations), address common questions (e.g., why choose Bottlerocket AMI over AL2023?), and outline next steps to extend your cluster’s capabilities.

Designed specifically for Machine Learning (ML) and Artificial Intelligence (AI) engineers, platform administrators, operators, and data/AI specialists who are new to the AWS and EKS ecosystem, this guide assumes familiarity with Kubernetes but no prior EKS experience. It is designed to help you understand the steps and processes needed to get real-time online inference workloads up and running. The guide shows you the essentials of creating a single-node inference cluster, including provisioning GPU resources, integrating storage for model artifacts, enabling secure AWS service access, and exposing inference endpoints. Throughout, it emphasizes low-latency, resilient design for user-facing applications like fraud detection, real-time chatbots, and sentiment analysis in customer feedback systems.

In this guide, we focus exclusively on setting up a foundational, prescriptive starting point using G5 EC2 instances. If you’re seeking AWS Inferentia-specific cluster configurations or end-to-end workflows, see [Use AWS Inferentia instances with Amazon EKS for Machine Learning](inferentia-support.md "inferentia-support.md") or our workshops in [Resources to get started with AI/ML on Amazon EKS](ml-resources.md "ml-resources.md").

## Before you begin

Before you start, make sure you have performed the following tasks:

- [Setup your environment for Amazon EKS](setting-up.md "setting-up.md")
- [Install the latest version of eksctl](https://eksctl.io/installation/ "https://eksctl.io/installation/")
- [Install Helm](https://helm.sh/docs/intro/install/ "https://helm.sh/docs/intro/install/")
- [(Optional) Install Docker](https://docs.docker.com/get-started/ "https://docs.docker.com/get-started/")
- [(Optional) Install the NGC CLI](https://org.ngc.nvidia.com/setup/installers/cli "https://org.ngc.nvidia.com/setup/installers/cli")

## Architecture

Real-time online inference refers to the process of using a trained machine learning model to generate predictions or outputs on incoming data streams with minimal latency. For example, it enables real-time fraud detection, classification of images, or the generation of knowledge graphs in response to user inputs. The architecture of a real-time online inference system delivers low-latency machine learning predictions in user-facing applications by decoupling CPU-bound web traffic handling from GPU-intensive AI computations. This process typically lives within a larger application ecosystem, and often includes backend, frontend, vector, and model services, with a focus on specialized components to enable independent scaling, parallel development, and resilience against failures. Isolating inference tasks on dedicated GPU hardware and leveraging interfaces like APIs and WebSockets ensures high concurrency, fast processing of models like transformers, and user interactions through the frontend. Note that although vector databases and Retrieval Augmented Generation (RAG) pipelines often play a big part in real-time inference systems, these components are not covered in this guide. At a minimum, a typical architecture often includes:

- **Frontend Service**: Serves as the user-facing interface, handling client-side logic, rendering dynamic content, and facilitating real-time interactions, it communicates with the backend service to initiate inference requests and display results, often initiating requests to the backend service which uses WebSockets for streaming updates or APIs for structured data exchange. This service typically does not require a dedicated load balancer, as it can be hosted on content delivery networks (CDNs) like AWS CloudFront for static assets or served directly from web servers, with scaling handled via auto-scaling groups if needed for dynamic content.
- **Backend Service**: Acts as the application’s orchestrator, managing business logic such as user authentication, data validation, and service coordination (e.g., via APIs for RESTful endpoints or WebSockets for persistent connections). It communicates with the inference service, scales independently on multi-core CPUs and RAM to handle high web traffic without relying on GPUs, and often requires a load balancer (such as AWS Application Load Balancer or Network Load Balancer) to distribute incoming requests across multiple instances, especially in high-concurrency scenarios. An ingress controller can further manage external access and routing rules for enhanced security and traffic shaping.
- **Inference Service**: Serves as the core for AI computations, running on GPUs with sufficient VRAM (e.g., 8-12 GB for models like DistilBERT) to perform vector embeddings, knowledge extraction, and model inference (e.g., exposed through APIs for batch requests or WebSockets for real-time streaming) using custom or open-source models. This isolation prevents dependency conflicts, allows model updates without downtime, and enables horizontal scaling with load balancing for multiple concurrent requests. To expose the model service effectively, it typically sits behind a load balancer to distribute GPU-bound workloads across replicated instances, while an ingress resource or controller (such as ALB Ingress Controller in AWS) handles external routing, SSL termination, and path-based forwarding to ensure secure and efficient access without overwhelming individual GPUs.

## Solution Overview

Real-time online inference systems require a high-performance, resilient architecture that can deliver ultra-low latency while handling unpredictable, high volume traffic bursts. This solution overview explains how the following AWS components work together in the Amazon EKS cluster we will create to ensure our cluster is able to host and manage machine learning models that provide immediate predictions on live data with minimal delay for end-users.

- [Amazon G5 EC2 Instances](https://aws.amazon.com/ec2/instance-types/g5/ "https://aws.amazon.com/ec2/instance-types/g5/") — For GPU-intensive inference tasks, we are using g5.xlarge and g5.2xlarge G5 EC2 instance types, which feature a single (1) NVIDIA A10G GPU with 24GB of memory (e.g., 8 billion parameters at FP16). Based on the NVIDIA Ampere Architecture, these GPUs are powered by NVIDIA A10G Tensor Core GPUs and 2nd generation AMD EPYC processors, support 4-8 vCPUs, up to 10 Gbps network bandwidth, and 250-450 GB of local NVMe SSD storage, ensuring fast data movement and compute power for complex models, making them ideal for low-latency, high-throughput inference tasks. Choosing an EC2 instance type is application-specific, depends on your model (e.g., image, video, text model), and your latency and throughput requirements. For instance, if using an image and or video model, you may want to use [P5 EC2 instances](https://aws.amazon.com/ec2/instance-types/p5/ "https://aws.amazon.com/ec2/instance-types/p5/") for optimal, real-time latency. We recommend starting out with [G5 EC2 instances](https://aws.amazon.com/ec2/instance-types/g5/ "https://aws.amazon.com/ec2/instance-types/g5/") as it provides a good starting point for getting up and running quickly, then evaluating whether it’s the right fit for your workloads through performance benchmark testing. For more advanced cases, consider [G6 EC2 instances](https://aws.amazon.com/ec2/instance-types/g6/ "https://aws.amazon.com/ec2/instance-types/g6/").
- [Amazon EC2 M7g Instances](https://aws.amazon.com/ec2/instance-types/m7g/ "https://aws.amazon.com/ec2/instance-types/m7g/") — For CPU-intensive tasks like data preprocessing, API request handling, hosting the Karpenter controller, add-ons, and other system components, we are using the m5.xlarge M7g EC2 instance type. M7g instances are ARM-based instance which features 4 vCPUs, 16 GB of memory, up to 12.5 Gbps network bandwidth, and is powered by AWS Graviton3 processors. Choosing an EC2 instance type is application-specific and depends on your workload’s compute, memory, and scalability requirements. For compute-optimized workloads, you might consider [C7g EC2 instances](https://aws.amazon.com/ec2/instance-types/c7g/ "https://aws.amazon.com/ec2/instance-types/c7g/"), which also use Graviton3 processors but are optimized for higher compute performance than M7g instances for certain use cases. Alternatively, newer [C8g EC2 instances](https://aws.amazon.com/ec2/instance-types/c8g/ "https://aws.amazon.com/ec2/instance-types/c8g/") (where available) provide up to 30% better compute performance than C7g instances. We recommend starting out with M7g EC2 instances for their cost efficiency and compatibility with a wide range of workloads (e.g., application servers, microservices, gaming servers, mid-size data stores), then evaluating whether it’s the right fit for your workloads through performance benchmark testing.
- [Amazon S3 Mountpoint CSI Driver](s3-csi.md "s3-csi.md") — For workloads on single-GPU instances where multiple pods share a GPU (e.g., multiple pods scheduled on the same node to utilize its GPU resources), we are using the Mountpoint S3 CSI Driver to optimize memory usage—essential for tasks like large-model inference in cost-sensitive, low-complexity setups. It exposes Amazon S3 buckets as a POSIX-like file system available to the Kubernetes cluster, which allows inference pods to read model artifacts (e.g., model weights) directly into memory without having to download them first, and input datasets using standard file operations. Additionally, S3 has virtually unlimited storage capacity and accelerates data-intensive inference workloads. Choosing a storage CSI driver is application-specific, and depends on your workload’s throughput and latency requirements. Though the [FSx for OpenZFS CSI Driver](fsx-openzfs-csi.md "fsx-openzfs-csi.md") offers sub-millisecond latency for random I/O or fully POSIX-compliant shared persistent volumes across nodes, we recommend starting out with the Mountpoint S3 CSI Driver due to its scalability, lower costs for large datasets, and built-in integration with S3-managed object storage for read-heavy inference patterns (e.g., streaming model inputs), then evaluating whether it’s the right fit for your workloads through performance benchmark testing.
- [EKS Pod Identity Agent](pod-identities.md "pod-identities.md") — To enable access to AWS services, we are using the EKS Pod Identity Agent, which uses a single service principal and facilitates pod-level IAM role associations within the Amazon EKS cluster. EKS Pod Identity offers a streamlined alternative to the traditional [IAM Roles for Service Accounts (IRSA)](iam-roles-for-service-accounts.md "iam-roles-for-service-accounts.md") approach by utilizing a single service principal (pods.eks.amazonaws.com) instead of relying on individual OIDC providers for each cluster, which makes it easier to assign permissions. Additionally, it enables roles to be reused across multiple clusters and it supports advanced features like [IAM role session tags](pod-id-abac.md "pod-id-abac.md") and [Target IAM roles](pod-id-assign-target-role.md "pod-id-assign-target-role.md").
- [EKS Node Monitoring Agent](node-health.md "node-health.md") — To ensure continuous availability and reliability of inference services, we are using the EKS Node Monitoring Agent with Auto Repair, which automatically detects and replaces unhealthy nodes, minimizing downtime. It continuously monitors nodes for hardware, kernel, networking, and storage issues using enhanced health checks (e.g., KernelReady, NetworkingReady). For GPU nodes, it detects accelerator-specific failures, initiating graceful remediation by cordoning unhealthy nodes, waiting 10 minutes for transient GPU issues to resolve, and replacing nodes after 30 minutes for persistent failures.
- [Bottlerocket AMI](eks-optimized-ami-bottlerocket.md "eks-optimized-ami-bottlerocket.md") — To provide a security-hardened foundation for our EKS cluster, we are using the Bottlerocket AMI, which includes only the essential components required to run containers and offers minimal boot times for fast scaling. Choosing a node AMI is application-specific and depends on your workload’s customization, security, and scalability requirements. Though the [AL2023 AMI](eks-optimized-ami.md "eks-optimized-ami.md") provides greater flexibility for host-level installations and customizations (e.g., specifying a dedicated cache directory in a PV/PVC without any additional node configurations), we recommend starting out with the Bottlerocket AMI for its smaller footprint and built-in optimization for containerized workloads (e.g., microservices, inference servers, scalable APIs), then evaluating whether it’s the right fit for your workloads through performance benchmark testing.
- [AWS Load Balancer Controller (LBC)](lbc-helm.md "lbc-helm.md") — To expose real-time inference endpoints, we are using the AWS Load Balancer Controller, which automatically provisions and manages Application Load Balancers (ALBs) for HTTP/HTTPS traffic and Network Load Balancers (NLBs) for TCP/UDP traffic based on Kubernetes Ingress and Service resources, enabling the integration of inference models with external clients. Additionally, it supports features like path-based routing to distribute inference requests across multiple pods or nodes, ensuring scalability during traffic spikes and minimizing latency through AWS-native optimizations like connection multiplexing and health checks.

## 1. Create your EKS cluster

In this step, we create a cluster with CPU nodes and a managed node group using an AWS CloudFormation-powered eksctl [ClusterConfig](https://eksctl.io/usage/creating-and-managing-clusters/ "https://eksctl.io/usage/creating-and-managing-clusters/") template. Initializing the cluster with only CPU nodes allows us to use Karpenter exclusively to manage CPU-intensive and GPU nodes for optimized resource allocation using Karpenter NodePools which we create in later steps. To support our real-time inference workloads, we provision the cluster with the EKS Bottlerocket AMI, EKS Node Monitoring Agent, EKS Pod Identity Agent, Mountpoint S3 CSI Driver, AWS Load Balancer Controller (LBC), and [kube-proxy](managing-kube-proxy.md "managing-kube-proxy.md"), [vpc-cni](managing-vpc-cni.md "managing-vpc-cni.md"), and [coredns](managing-coredns.md "managing-coredns.md") drivers. The m7g.xlarge instances will be used for CPU system tasks, including hosting the Karpenter controller, add-ons, and other system components.

By default, `eksctl` will create a dedicated VPC for the cluster with a CIDR block of `192.168.0.0/16`. The VPC includes three public subnets and three private subnets, each distributed across three different Availability Zones (or two AZs in the `us-east-1` region) which is the ideal method for deploying Kubernetes workloads. The template also deploys an internet gateway, providing internet access to the public subnets through default routes in their route tables and a single NAT gateway in one of the public subnets, with default routes in the private subnets' route tables directing outbound traffic through the NAT gateway for internet access. To learn more about this setup, see [Deploy Nodes to Private Subnets](../best-practices/subnets.md#_deploy_nodes_to_private_subnets "../best-practices/subnets.md#_deploy_nodes_to_private_subnets").

### Check your credentials

Check whether your AWS CLI credentials are valid and can authenticate with AWS services:

```
aws sts get-caller-identity
```

If successful, the CLI will return details about your AWS identity (UserId, Account, and Arn).

### Check instance availability

G5 instance types are not available in all regions. Check your nearest region. For example:

```
aws ec2 describe-instance-types --instance-types g5.xlarge g5.2xlarge --region us-east-1
```

If successful, the G5 instance type is available in the region you specified.

The Bottlerocket AMI is not available in all regions. Check by retrieving a Bottlerocket AMI ID for your nearest region. For example:

```
aws ssm get-parameter --name /aws/service/bottlerocket/aws-k8s-1.33/arm64/latest/image_id \
    --region us-east-1 --query "Parameter.Value" --output text
```

If successful, the Bottlerocket AMI is available in the region you specified.

### Prepare your environment

First, set the following environment variables in a new terminal window. **Note**: Be sure to substitute the sample placeholders with your unique values, including cluster name, your desired region, [Karpenter release version](https://github.com/kubernetes-sigs/karpenter/releases "https://github.com/kubernetes-sigs/karpenter/releases"), and [Kubernetes version](kubernetes-versions.md "kubernetes-versions.md").

###### Tip

Some variables (such as `${AWS_REGION}` and `${K8S_VERSION}`) are defined early in the block and then referenced in later commands for consistency and to avoid repetition. Make sure to run the commands in sequence so that these values are properly exported and available for use in subsequent definitions.

```
export TEMPOUT="$(mktemp)"
export K8S_VERSION=1.33
export KARPENTER_VERSION="1.5.0"
export AWS_REGION="us-east-1"
export EKS_CLUSTER_NAME="eks-rt-inference-${AWS_REGION}"
export S3_BUCKET_NAME="eks-rt-inference-models-${AWS_REGION}-$(date +%s)"
export NVIDIA_BOTTLEROCKET_AMI="$(aws ssm get-parameter --name /aws/service/bottlerocket/aws-k8s-${K8S_VERSION}-nvidia/x86_64/latest/image_id --query Parameter.Value --output text)"
export STANDARD_BOTTLEROCKET_AMI="$(aws ssm get-parameter --name /aws/service/bottlerocket/aws-k8s-${K8S_VERSION}/arm64/latest/image_id --query Parameter.Value --output text)"
export AWS_ACCOUNT_ID="$(aws sts get-caller-identity --query Account --output text)"
export ALIAS_VERSION="$(aws ssm get-parameter --name "/aws/service/eks/optimized-ami/${K8S_VERSION}/amazon-linux-2023/x86_64/standard/recommended/image_id" --query Parameter.Value | xargs aws ec2 describe-images --query 'Images[0].Name' --image-ids | sed -r 's/^.*(v[[:digit:]]+).*$/\1/')"
```

### Create required roles and policies

Karpenter needs specific IAM roles and policies (e.g., Karpenter controller IAM role, instance profile, and policies) to manage EC2 instances as Kubernetes worker nodes. It uses these roles to perform actions like launching and terminating EC2 instances, tagging resources, and interacting with other AWS services. Create the Karpenter roles and policies using the Karpenter’s [cloudformation.yaml](https://raw.githubusercontent.com/aws/karpenter-provider-aws/v1.5.0/website/content/en/preview/getting-started/getting-started-with-karpenter/cloudformation.yaml "https://raw.githubusercontent.com/aws/karpenter-provider-aws/v1.5.0/website/content/en/preview/getting-started/getting-started-with-karpenter/cloudformation.yaml"):

```
curl -fsSL https://raw.githubusercontent.com/aws/karpenter-provider-aws/v${KARPENTER_VERSION}/website/content/en/preview/getting-started/getting-started-with-karpenter/cloudformation.yaml > "${TEMPOUT}" \
&& aws cloudformation deploy \
  --stack-name "Karpenter-${EKS_CLUSTER_NAME}" \
  --template-file "${TEMPOUT}" \
  --capabilities CAPABILITY_NAMED_IAM \
  --parameter-overrides "ClusterName=${EKS_CLUSTER_NAME}"
```

The AWS LBC needs permission to provision and manage AWS load balancers, such as creating ALBs for Ingress resources or NLBs for services of type `LoadBalancer`. We’ll specify this permissions policy during cluster creation. During cluster creation, we will create the service account with eksctl in the ClusterConfig. Create the LBC IAM policy:

```
aws iam create-policy \
  --policy-name AWSLoadBalancerControllerIAMPolicy \
  --policy-document "$(curl -fsSL https://raw.githubusercontent.com/kubernetes-sigs/aws-load-balancer-controller/v2.14.1/docs/install/iam_policy.json)"
```

When the Mountpoint S3 CSI Driver is installed, its DaemonSet pods are configured to use a service account for execution. The Mountpoint for Mountpoint S3 CSI driver needs permission to interact with the Amazon S3 bucket you create later in this guide. We’ll specify this permissions policy during cluster creation. During cluster creation, we will create the service account with eksctl in the ClusterConfig. Create the S3 IAM policy:

```
aws iam create-policy \
    --policy-name S3CSIDriverPolicy \
    --policy-document "{\"Version\": \"2012-10-17\", \"Statement\": [{\"Effect\": \"Allow\", \"Action\": [\"s3:GetObject\", \"s3:PutObject\", \"s3:AbortMultipartUpload\", \"s3:DeleteObject\", \"s3:ListBucket\"], \"Resource\": [\"arn:aws:s3:::${S3_BUCKET_NAME}\", \"arn:aws:s3:::${S3_BUCKET_NAME}/*\"]}]}"
```

**Note**: if a role already exists with this name, give the role a different name. The role we create in this step is specific to your cluster and your S3 bucket.

### Create the cluster

In this template, eksctl automatically creates a Kubernetes service account for EKS Pod Identity, Node Monitoring Agent, CoreDNS, Kubeproxy, the VPC CNI Plugin. As of today, the Mountpoint S3 CSI Driver is not available for EKS Pod Identity, so we create an IAM Roles for Service Account (IRSA) and an [OIDC endpoint](enable-iam-roles-for-service-accounts.md "enable-iam-roles-for-service-accounts.md"). In addition, we create a service account for the AWS Load Balancer Controller (LBC). For access to Bottlerocket nodes, eksctl automatically attaches AmazonSSMManagedInstanceCore for Bottlerocket to allow secure shell sessions via SSM.

In the same terminal where you set your environment variables, run the following command block to create the cluster:

```
eksctl create cluster -f - <<EOF
---
apiVersion: eksctl.io/v1alpha5
kind: ClusterConfig
metadata:
  name: ${EKS_CLUSTER_NAME}
  region: ${AWS_REGION}
  version: "${K8S_VERSION}"
  tags:
    karpenter.sh/discovery: ${EKS_CLUSTER_NAME}
    # Add more tags if needed for billing
iam:
  # Creates an OIDC endpoint and IRSA service account for the Mountpoint S3 CSI Driver
  # Uses the S3 CSI Driver policy for permissions
  withOIDC: true
  podIdentityAssociations:
  # Creates the pod identity association and service account
  # Uses the Karpenter controller IAM policy for permissions
  - namespace: "kube-system"
    serviceAccountName: karpenter
    roleName: ${EKS_CLUSTER_NAME}-karpenter
    permissionPolicyARNs:
    - arn:aws:iam::${AWS_ACCOUNT_ID}:policy/KarpenterControllerPolicy-${EKS_CLUSTER_NAME}
  # Creates the pod identity association and service account
  # Uses the {aws} LBC policy for permissions
  - namespace: kube-system
    serviceAccountName: aws-load-balancer-controller
    createServiceAccount: true
    roleName: AmazonEKSLoadBalancerControllerRole
    permissionPolicyARNs:
    - arn:aws:iam::${AWS_ACCOUNT_ID}:policy/AWSLoadBalancerControllerIAMPolicy
iamIdentityMappings:
- arn: "arn:aws:iam::${AWS_ACCOUNT_ID}:role/KarpenterNodeRole-${EKS_CLUSTER_NAME}"
  username: system:node:{{EC2PrivateDNSName}}
  groups:
  - system:bootstrappers
  - system:nodes
managedNodeGroups:
  # Creates 2 CPU nodes for lightweight system tasks
  - name: ${EKS_CLUSTER_NAME}-m7-cpu
    instanceType: m7g.xlarge
    amiFamily: Bottlerocket
    desiredCapacity: 2
    minSize: 1
    maxSize: 10
    labels:
      role: cpu-worker
# Enable automatic Pod Identity associations for VPC CNI Driver, coreDNS, kube-proxy
addonsConfig:
  autoApplyPodIdentityAssociations: true
addons:
  # Installs the S3 CSI Driver addon and creates IAM role
  # Uses the S3 CSI Driver policy for IRSA permissions
  - name: aws-mountpoint-s3-csi-driver
    attachPolicyARNs:
      - "arn:aws:iam::${AWS_ACCOUNT_ID}:policy/S3CSIDriverPolicy"
  - name: eks-pod-identity-agent
  - name: eks-node-monitoring-agent
  - name: coredns
  - name: kube-proxy
  - name: vpc-cni
EOF
```

This process takes several minutes to complete. If you’d like to monitor the status, see the [AWS CloudFormation](https://console.aws.amazon.com/cloudformation "https://console.aws.amazon.com/cloudformation") console.

## 2. Verify Cluster Node and Pod Health

Let’s perform a few health checks to ensure the cluster is ready. When the previous command completes, view the instance types and verify that your CPU system nodes have reached the `Ready` state with the following command:

```
kubectl get nodes -L node.kubernetes.io/instance-type
```

The expected output should look like this:

```
NAME                             STATUS   ROLES    AGE     VERSION               INSTANCE-TYPE
ip-192-168-35-103.ec2.internal   Ready    <none>   12m     v1.33.0-eks-802817d   m7g.xlarge
ip-192-168-7-15.ec2.internal     Ready    <none>   12m     v1.33.0-eks-802817d   m7g.xlarge
```

Verify all the Pod Identity associations and how they map a role to a service account in a namespace in the cluster with the following command:

```
eksctl get podidentityassociation --cluster ${EKS_CLUSTER_NAME} --region ${AWS_REGION}
```

The output should show the IAM roles for Karpenter ("karpenter") and the AWS LBC ("aws-load-balancer-controller").

Verify the DaemonSets are available:

```
kubectl get daemonsets -n kube-system
```

The expected output should look like this:

```
NAME                           DESIRED CURRENT READY UP-TO-DATE AVAILABLE NODE SELECTOR          AGE
aws-node                       3       3       3     3          3         <none>                 12m
dcgm-server                    0       0       0     0          0         kubernetes.io/os=linux 12m
eks-node-monitoring-agent      3       3       3     3          3         kubernetes.io/os=linux 12m
eks-pod-identity-agent         3       3       3     3          3         <none>                 12m
kube-proxy                     3       3       3     3          3         <none>                 12m
s3-csi-node                    2       2       2     2          2         kubernetes.io/os=linux 12m
```

Verify all addons are installed on the cluster:

```
eksctl get addons --cluster ${EKS_CLUSTER_NAME} --region ${AWS_REGION}
```

The expected output should look like this:

```
NAME                           VERSION              STATUS    ISSUES    IAMROLE                                           UPDATE AVAILABLE    CONFIGURATION VALUES    POD IDENTITY ASSOCIATION ROLES
aws-mountpoint-s3-csi-driver   v1.15.0-eksbuild.1   ACTIVE    0    arn:aws:iam::143095308808:role/eksctl-eks-rt-inference-us-east-1-addon-aws-m-Role1-RAUjk4sJnc0L
coredns                        v1.12.1-eksbuild.2   ACTIVE    0
eks-node-monitoring-agent      v1.3.0-eksbuild.2    ACTIVE    0
eks-pod-identity-agent         v1.3.7-eksbuild.2    ACTIVE    0
kube-proxy                     v1.33.0-eksbuild.2   ACTIVE    0
metrics-server                 v0.7.2-eksbuild.3    ACTIVE    0
vpc-cni                        v1.19.5-eksbuild.1   ACTIVE    0
```

## 3. Install Karpenter

Install the Karpenter controller on your CPU worker nodes (`cpu-worker`) to optimize costs and conserve GPU resources. We’ll be installing it in the "kube-system" namespace and specifying the "karpenter" service account we defined during cluster creation. Additionally, this command configures the cluster name and a Spot Instance interruption queue for CPU nodes. Karpenter will use IRSA to assume this IAM role.

```
# Logout of helm registry before pulling from public ECR
helm registry logout public.ecr.aws

# Install Karpenter
helm upgrade --install karpenter oci://public.ecr.aws/karpenter/karpenter --version "${KARPENTER_VERSION}" --namespace "kube-system" --create-namespace  \
  --set "settings.clusterName=${EKS_CLUSTER_NAME}" \
  --set "settings.interruptionQueue=${EKS_CLUSTER_NAME}" \
  --set controller.resources.requests.cpu=1 \
  --set controller.resources.requests.memory=1Gi \
  --set controller.resources.limits.cpu=1 \
  --set controller.resources.limits.memory=1Gi \
  --set serviceAccount.annotations."eks\.amazonaws\.com/role-arn"="arn:aws:iam::${AWS_ACCOUNT_ID}:role/${EKS_CLUSTER_NAME}-karpenter" \
  --wait
```

The expected output should look like this:

```
Release "karpenter" does not exist. Installing it now.
Pulled: public.ecr.aws/karpenter/karpenter:1.5.0
Digest: sha256:9a155c7831fbff070669e58500f68d7ccdcf3f7c808dcb4c21d3885aa20c0a1c
NAME: karpenter
LAST DEPLOYED: Thu Jun 19 09:57:06 2025
NAMESPACE: kube-system
STATUS: deployed
REVISION: 1
TEST SUITE: None
```

Verify that Karpenter is running:

```
kubectl get pods -n kube-system -l app.kubernetes.io/name=karpenter
```

The expected output should look like this:

```
NAME                       READY   STATUS    RESTARTS   AGE
karpenter-555895dc-865bc   1/1     Running   0          5m58s
karpenter-555895dc-j7tk9   1/1     Running   0          5m58s
```

## 4. Setup Karpenter NodePools

In this step, we configure mutually exclusive CPU and GPU [Karpenter NodePools](https://karpenter.sh/docs/concepts/nodepools/ "https://karpenter.sh/docs/concepts/nodepools/"). The `limits` field in the NodePool spec constrains the maximum total resources (e.g., CPU, memory, GPUs) that each NodePool can consume across all provisioned nodes, preventing additional node provisioning if these limits are exceeded. While NodePools support broad instance categories (e.g., `c`, `g`), specifying specific [instance types](https://karpenter.sh/docs/concepts/nodepools/#instance-types "https://karpenter.sh/docs/concepts/nodepools/#instance-types"), [capacity types](https://karpenter.sh/docs/concepts/nodepools/#capacity-type "https://karpenter.sh/docs/concepts/nodepools/#capacity-type"), and resource [limits](https://karpenter.sh/docs/concepts/nodepools/#speclimits "https://karpenter.sh/docs/concepts/nodepools/#speclimits") help you more easily estimate costs for your on-demand workloads. In these NodePools, we use a diverse set of instance types within the G5 instance family. This allows Karpenter to automatically select the most appropriate instance type based on pod resource requests, optimizing resource utilization while respecting the NodePool’s total limits. To learn more, see [Creating NodePools](../best-practices/karpenter.md#_creating_nodepools "../best-practices/karpenter.md#_creating_nodepools").

### Setup the GPU NodePool

In this NodePool, we set resource limits to manage the provisioning of nodes with GPU capabilities. These limits are designed to cap the total resources across all nodes in the pool, allowing for up to 10 instances in total. Each instance can be either g5.xlarge (4 vCPUs, 16 GiB memory, 1 GPU) or g5.2xlarge (8 vCPUs, 32 GiB memory, 1 GPU), as long as the total vCPUs do not exceed 80, total memory does not exceed 320GiB, and total GPUs do not exceed 10. For example, the pool can provision 10 g5.2xlarge instances (80 vCPUs, 320 GiB, 10 GPUs), or 10 g5.xlarge instances (40 vCPUs, 160 GiB, 10 GPUs), or a mix such as 5 g5.xlarge and 5 g5.2xlarge (60 vCPUs, 240 GiB, 10 GPUs), ensuring flexibility based on workload demands while respecting resource constraints.

Additionally, we specify the ID of the Nvidia variant of the Bottlerocket AMI. Finally, we set a [disruption policy](https://karpenter.sh/docs/concepts/disruption/#nodepool-disruption-budgets "https://karpenter.sh/docs/concepts/disruption/#nodepool-disruption-budgets") to remove empty nodes after 30 minutes (`consolidateAfter: 30m`) and set a maximum node lifetime of 30 days (`expireAfter: 720h`) to optimize costs and maintain node health for GPU-intensive tasks. To learn more, see [Disable Karpenter Consolidation for interruption sensitive workloads](../best-practices/aiml-compute.md#_disable_karpenter_consolidation_for_interruption_sensitive_workloads "../best-practices/aiml-compute.md#_disable_karpenter_consolidation_for_interruption_sensitive_workloads"), and [Use ttlSecondsAfterFinished to Auto Clean-Up Kubernetes Jobs](../best-practices/aiml-compute.md#_use_ttlsecondsafterfinished_to_auto_clean_up_kubernetes_jobs "../best-practices/aiml-compute.md#_use_ttlsecondsafterfinished_to_auto_clean_up_kubernetes_jobs").

```
cat <<EOF | envsubst | kubectl apply -f -
apiVersion: karpenter.sh/v1
kind: NodePool
metadata:
  name: gpu-a10g-inference-g5
spec:
  template:
    metadata:
      labels:
        role: gpu-worker
        gpu-type: nvidia-a10g
    spec:
      requirements:
        - key: node.kubernetes.io/instance-type
          operator: In
          values: ["g5.xlarge", "g5.2xlarge"]
        - key: "karpenter.sh/capacity-type"
          operator: In
          values: ["on-demand"]
      taints:
        - key: nvidia.com/gpu
          value: "true"
          effect: NoSchedule
      nodeClassRef:
        name: gpu-a10g-inference-ec2
        group: karpenter.k8s.aws
        kind: EC2NodeClass
      expireAfter: 720h
  limits:
    cpu: "80"
    memory: "320Gi"
    nvidia.com/gpu: "10"
  disruption:
    consolidationPolicy: WhenEmpty
    consolidateAfter: 30m
---
apiVersion: karpenter.k8s.aws/v1
kind: EC2NodeClass
metadata:
  name: gpu-a10g-inference-ec2
spec:
  amiFamily: Bottlerocket
  amiSelectorTerms:
    - id: ${NVIDIA_BOTTLEROCKET_AMI}
  role: "KarpenterNodeRole-${EKS_CLUSTER_NAME}"
  subnetSelectorTerms:
    - tags:
        karpenter.sh/discovery: "${EKS_CLUSTER_NAME}"
  securityGroupSelectorTerms:
    - tags:
        karpenter.sh/discovery: "${EKS_CLUSTER_NAME}"
  tags:
    nvidia.com/gpu: "true"
EOF
```

The expected output should look like this:

```
nodepool.karpenter.sh/gpu-a10g-inference-g5 created
ec2nodeclass.karpenter.k8s.aws/gpu-a10g-inference-ec2 created
```

Verify the NodePool is created and healthy:

```
kubectl get nodepool gpu-a10g-inference-g5 -o yaml
```

Look for `status.conditions` like `ValidationSucceeded: True`, `NodeClassReady: True`, and `Ready: True` to confirm the NodePool is healthy.

### Setup the CPU NodePool

In this NodePool, we set limits to support approximately 50 instances, aligning with a moderate CPU workload (e.g., 100-200 pods) and typical AWS vCPU quotas (e.g., 128-1152). The limits are calculated assuming the NodePool should scale up to 50 m7.xlarge instances: CPU (4 vCPUs per instance × 50 instances = 200 vCPUs) and memory (16 GiB per instance × 50 instances = 800 GiB). These limits are designed to cap the total resources across all nodes in the pool, allowing for up to 50 m7g.xlarge instances (each with 4 vCPUs and 16 GiB memory), as long as the total vCPUs do not exceed 200 and total memory does not exceed 800GiB.

Additionally, we specify the ID of the standard variant of the Bottlerocket AMI. Finally, we set a [disruption policy](https://karpenter.sh/docs/concepts/disruption/#nodepool-disruption-budgets "https://karpenter.sh/docs/concepts/disruption/#nodepool-disruption-budgets") to remove empty nodes after 60 minutes (`consolidateAfter: 60m`) and set a maximum node lifetime of 30 days (`expireAfter: 720h`) to optimize costs and maintain node health for GPU-intensive tasks. To learn more, see [Disable Karpenter Consolidation for interruption sensitive workloads](../best-practices/aiml-compute.md#_disable_karpenter_consolidation_for_interruption_sensitive_workloads "../best-practices/aiml-compute.md#_disable_karpenter_consolidation_for_interruption_sensitive_workloads"), and [Use ttlSecondsAfterFinished to Auto Clean-Up Kubernetes Jobs](../best-practices/aiml-compute.md#_use_ttlsecondsafterfinished_to_auto_clean_up_kubernetes_jobs "../best-practices/aiml-compute.md#_use_ttlsecondsafterfinished_to_auto_clean_up_kubernetes_jobs").

```
cat <<EOF | envsubst | kubectl apply -f -
apiVersion: karpenter.sh/v1
kind: NodePool
metadata:
  name: cpu-inference-m7gxlarge
spec:
  template:
    metadata:
      labels:
        role: cpu-worker
    spec:
      requirements:
        - key: node.kubernetes.io/instance-type
          operator: In
          values: ["m7g.xlarge"]
        - key: karpenter.sh/capacity-type
          operator: In
          values: ["on-demand"]
      taints:
        - key: role
          value: cpu-intensive
          effect: NoSchedule
      nodeClassRef:
        name: cpu-inference-m7gxlarge-ec2
        group: karpenter.k8s.aws
        kind: EC2NodeClass
      expireAfter: 720h
  limits:
    cpu: "200"
    memory: "800Gi"
  disruption:
    consolidationPolicy: WhenEmpty
    consolidateAfter: 60m
---
apiVersion: karpenter.k8s.aws/v1
kind: EC2NodeClass
metadata:
  name: cpu-inference-m7gxlarge-ec2
spec:
  amiFamily: Bottlerocket
  amiSelectorTerms:
    - id: ${STANDARD_BOTTLEROCKET_AMI}
  role: "KarpenterNodeRole-${EKS_CLUSTER_NAME}"
  subnetSelectorTerms:
    - tags:
        karpenter.sh/discovery: "${EKS_CLUSTER_NAME}"
  securityGroupSelectorTerms:
    - tags:
        karpenter.sh/discovery: "${EKS_CLUSTER_NAME}"
EOF
```

The expected output should look like this:

```
nodepool.karpenter.sh/cpu-inference-m7gxlarge created
ec2nodeclass.karpenter.k8s.aws/cpu-inference-m7gxlarge-ec2 created
```

Verify the NodePool is created and healthy:

```
kubectl get nodepool cpu-inference-m7gxlarge -o yaml
```

Look for `status.conditions` like `ValidationSucceeded: True`, `NodeClassReady: True`, and `Ready: True` to confirm the NodePool is healthy.

## 5. Deploy a GPU Pod to Expose a GPU

You need the Nvidia Device Plugin to enable Kubernetes to expose GPU devices to the Kubernetes cluster. Typically, you would need to deploy the plugin as a DaemonSet; however, the Bottlerocket AMI pre-installs the plugin as part of the AMI. That means when using Bottlerocket AMIs, there is no need to deploy the Nvidia device plugin DaemonSet. To learn more, see [Kubernetes Device Plugin to expose GPUs](../best-practices/aiml-compute.md#_use_kubernetes_device_plugin_for_exposing_gpus "../best-practices/aiml-compute.md#_use_kubernetes_device_plugin_for_exposing_gpus").

### Deploy a sample pod

Karpenter acts dynamically: it provisions GPU nodes when a workload (pod) requests GPU resources. To verify that pods are able to request and use GPUs, deploy a pod that requests the `nvidia.com/gpu` resource in its limits (e.g., `nvidia.com/gpu: 1`). To learn more about these labels, see [Schedule workloads with GPU requirements using Well-Known labels](../best-practices/aiml-compute.md#_schedule_workloads_with_gpu_requirements_using_well_known_labels "../best-practices/aiml-compute.md#_schedule_workloads_with_gpu_requirements_using_well_known_labels").

```
cat <<EOF | envsubst | kubectl apply -f -
apiVersion: v1
kind: Pod
metadata:
  name: gpu-nvidia-smi
spec:
  restartPolicy: OnFailure
  tolerations:
  - key: "nvidia.com/gpu"
    operator: "Exists"
    effect: "NoSchedule"
  nodeSelector:
    role: gpu-worker  # Matches GPU NodePool's label
  containers:
  - name: cuda-container
    image: nvidia/cuda:12.9.1-base-ubuntu20.04
    command: ["nvidia-smi"]
    resources:
      limits:
        nvidia.com/gpu: 1
      requests:
        nvidia.com/gpu: 1
EOF
```

The expected output should look like this:

```
pod/gpu-ndivia-smi created
```

Give it a minute then check if the Pod has a "Pending," "ContainerCreating," "Running," then a "Completed" status:

```
kubectl get pod gpu-nvidia-smi -w
```

Verify the node for the pod belongs to the GPU NodePool:

```
kubectl get node $(kubectl get pod gpu-nvidia-smi -o jsonpath='{.spec.nodeName}') -o custom-columns="Name:.metadata.name,Nodepool:.metadata.labels.karpenter\.sh/nodepool"
```

The expected output should look like this:

```
Name                             Nodepool
ip-192-168-83-245.ec2.internal   gpu-a10g-inference-g5
```

Check the pod’s logs:

```
kubectl logs gpu-nvidia-smi
```

The expected output should look like this:

```
Thu Jul 17 04:31:33 2025
+---------------------------------------------------------------------------------------+
| NVIDIA-SMI 570.148.08                 Driver Version: 570.148.08         CUDA Version: 12.9 |
|-----------------------------------------+----------------------+----------------------+
| GPU  Name                 Persistence-M | Bus-Id        Disp.A | Volatile Uncorr. ECC |
| Fan  Temp   Perf          Pwr:Usage/Cap |         Memory-Usage | GPU-Util  Compute M. |
|                                         |                      |               MIG M. |
|=========================================+======================+======================|
|   0  NVIDIA A10G                    On  | 00000000:00:1E.0 Off |                    0 |
|  0%   30C    P8               9W / 300W |      0MiB / 23028MiB |      0%      Default |
|                                         |                      |                  N/A |
+---------------------------------------------------------------------------------------+

+---------------------------------------------------------------------------------------+
| Processes:                                                                            |
|  GPU        GI     CI        PID   Type   Process name                  GPU Memory    |
|                     ID        ID                                         Usage        |
|=======================================================================================|
|  No running processes found                                                           |
+---------------------------------------------------------------------------------------+
```

## 6. (Optional) Prepare and Upload Model Artifacts for Deployment

In this step, you’ll deploy a model service for real-time image classification, starting with uploading model weights to an Amazon S3 bucket. For demonstration, we are using the open-source [GPUNet-0](https://catalog.ngc.nvidia.com/orgs/nvidia/teams/dle/models/gpunet_0_pyt_ckpt "https://catalog.ngc.nvidia.com/orgs/nvidia/teams/dle/models/gpunet_0_pyt_ckpt") vision model part of NVIDIA’s [GPUNet](https://catalog.ngc.nvidia.com/orgs/nvidia/teams/dle/resources/gpunet_pyt "https://catalog.ngc.nvidia.com/orgs/nvidia/teams/dle/resources/gpunet_pyt"), which supports low-latency inference on images using NVIDIA GPUs and TensorRT. This model is pretrained on [ImageNet](https://www.image-net.org/ "https://www.image-net.org/"), allows us to classifies objects in photos or video streams on the fly, and is considered a small model with 11.9 million parameters.

### Set up your environment

To download the GPUNet-0 model weights In this step, you need access to NVIDIA’s NGC catalog and [Docker](https://docs.docker.com/get-started/ "https://docs.docker.com/get-started/") installed on your local machine. Follow these steps to set up a free account and configure the NGC CLI:

- [Sign up for a free NGC account](https://ngc.nvidia.com/signup "https://ngc.nvidia.com/signup") and generate an API key from the NGC dashboard (User Icon > Setup > Generate API Key > Generate Personal Key > NGC Catalog).
- [Download and install the NGC CLI](https://org.ngc.nvidia.com/setup/installers/cli "https://org.ngc.nvidia.com/setup/installers/cli") (Linux/macOS/Windows) and configure the CLI using: `ngc config set`. Enter your API key when prompted; set org to `nvidia` and hit Enter to accept defaults for others. If successful, you should see something like: `Successfully saved NGC configuration to /Users/your-username/.ngc/config`.

### Verify service account permissions

Before we start, check the Kubernetes service account permissions:

```
kubectl get serviceaccount s3-csi-driver-sa -n kube-system -o yaml
```

During cluster creation, we attached the S3CSIDriverPolicy to an IAM role and annotated the service account ("s3-csi-driver-sa"). The Mountpoint S3 CSI driver pods inherits the IAM role’s permissions when interacting with S3. The expected output should look like this:

```
apiVersion: v1
kind: ServiceAccount
metadata:
  annotations:
    eks.amazonaws.com/role-arn: arn:aws:iam::143095308808:role/eksctl-eks-rt-inference-us-east-1-addon-aws-m-Role1-fpXXjRYdKN8r
  creationTimestamp: "2025-07-17T03:55:29Z"
  labels:
    app.kubernetes.io/component: csi-driver
    app.kubernetes.io/instance: aws-mountpoint-s3-csi-driver
    app.kubernetes.io/managed-by: EKS
    app.kubernetes.io/name: aws-mountpoint-s3-csi-driver
  name: s3-csi-driver-sa
  namespace: kube-system
  resourceVersion: "2278"
  uid: 50b36272-6716-4c68-bdc3-c4054df1177c
```

### Add a toleration

The S3 CSI Driver runs as a DaemonSet on all nodes. Pods use the CSI driver on those nodes to mount S3 volumes. To allow it to schedule on our GPU nodes which have taints, add a toleration to the DaemonSet:

```
kubectl patch daemonset s3-csi-node -n kube-system --type='json' -p='[{"op": "add", "path": "/spec/template/spec/tolerations/-", "value": {"key": "nvidia.com/gpu", "operator": "Exists", "effect": "NoSchedule"}}]'
```

The expected output should look like this:

```
daemonset.apps/s3-csi-node patched
```

### Upload model weights to S3

In this step, you’ll create an Amazon S3 bucket, download the GPUNet-0 model weights from NVIDIA GPU Cloud (NGC), and upload them to the bucket. These weights will be accessed by our application at runtime for inference.

Create your Amazon S3 bucket:

```
aws s3 mb s3://${S3_BUCKET_NAME} --region ${AWS_REGION}
```

Enable [S3 Versioning](../../../AmazonS3/latest/userguide/Versioning.md "../../../AmazonS3/latest/userguide/Versioning.md") for the bucket, to prevent accidental deletions and overwrites from causing immediate and permanent data loss:

```
aws s3api put-bucket-versioning --bucket ${S3_BUCKET_NAME} --versioning-configuration Status=Enabled
```

Apply a lifecycle rule to the bucket to remove overwritten or deleted object versions 14 days after they become non-current, remove expired delete markers, and remove incomplete multi-part uploads after 7 days. To learn more, see [Examples of S3 Lifecycle configurations](../../../AmazonS3/latest/userguide/lifecycle-configuration-examples.md "../../../AmazonS3/latest/userguide/lifecycle-configuration-examples.md").

```
aws s3api put-bucket-lifecycle-configuration --bucket $S3_BUCKET_NAME --lifecycle-configuration '{"Rules":[{"ID":"LifecycleRule","Status":"Enabled","Filter":{},"Expiration":{"ExpiredObjectDeleteMarker":true},"NoncurrentVersionExpiration":{"NoncurrentDays":14},"AbortIncompleteMultipartUpload":{"DaysAfterInitiation":7}}]}'
```

Download the GPUNet-0 model weights from NGC. For example, on macOS:

```
ngc registry model download-version nvidia/dle/gpunet_0_pyt_ckpt:21.12.0_amp --dest ~/downloads
```

###### Note

You may need to adjust this download command for your operating system. For this command to work on a Linux system, you likely need to create the directory as part of the command (e.g., `mkdir ~/downloads`).

The expected output should look like this:

```
{
  "download_end": "2025-07-18 08:22:39",
  "download_start": "2025-07-18 08:22:33",
  "download_time": "6s",
  "files_downloaded": 1,
  "local_path": "/Users/your-username/downloads/gpunet_0_pyt_ckpt_v21.12.0_amp",
  "size_downloaded": "181.85 MB",
  "status": "Completed",
  "transfer_id": "gpunet_0_pyt_ckpt[version=21.12.0_amp]"
}
```

Rename the checkpoint file to match the expected naming in our application code in later steps (no extraction is needed, as it’s a standard PyTorch \*.pth.tar checkpoint containing the model state dictionary):

```
mv ~/downloads/gpunet_0_pyt_ckpt_v21.12.0_amp/0.65ms.pth.tar gpunet-0.pth
```

Enable the [AWS Common Runtime](https://aws.amazon.com/blogs/storage/improving-amazon-s3-throughput-for-the-aws-cli-and-boto3-with-the-aws-common-runtime/ "https://aws.amazon.com/blogs/storage/improving-amazon-s3-throughput-for-the-aws-cli-and-boto3-with-the-aws-common-runtime/") in the AWS CLI to optimize S3 throughput:

```
aws configure set s3.preferred_transfer_client crt
```

Upload the model weights to your S3 bucket:

```
aws s3 cp gpunet-0.pth s3://${S3_BUCKET_NAME}/gpunet-0.pth
```

The expected output should look like this:

```
upload: ./gpunet-0.pth to s3://eks-rt-inference-models-us-east-1-1752722786/gpunet-0.pth
```

### Create the Model Service

In this step, you’ll set up a FastAPI web application for GPU-accelerated image classification using the GPUNet-0 vision model. The application downloads model weights from Amazon S3 at runtime, fetches the model architecture from NVIDIA’s repository for caching, and downloads ImageNet class labels via HTTP. The application includes image preprocessing transforms and exposes two endpoints: a root GET for status check and a POST `/predict` endpoint that accepts an image URL.

We serve the model using FastAPI with PyTorch, loading weights from Amazon S3 at runtime in a containerized setup for quick prototyping and Kubernetes deployment. For other methods like optimized batching or high-throughput engines, see [Serving ML Models](../best-practices/aiml-performance.md#_serving_ml_models "../best-practices/aiml-performance.md#_serving_ml_models").

#### Create the application

Create a directory for your application files such as `model-testing`, then change directories into it and add the following code to a new file named `app.py`:

```
import os
import torch
import json
import requests
from fastapi import FastAPI, HTTPException
from PIL import Image
from io import BytesIO, StringIO
import torchvision.transforms as transforms
from torch.nn.functional import softmax
import warnings
from contextlib import redirect_stdout, redirect_stderr
import argparse
import boto3
app = FastAPI()

# Suppress specific warnings from the model code (quantization is optional and unused here)
warnings.simplefilter("ignore", UserWarning)

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Load model code from cache (if present)
# Use backed cache directory
torch.hub.set_dir('/cache/torch/hub')

# Allowlist for secure deserialization (handles potential issues in older checkpoints)
torch.serialization.add_safe_globals([argparse.Namespace])
# Load the model architecture only on container startup (changed to pretrained=False)
# Precision (FP32 for full accuracy, could be 'fp16' for speed on Ampere+ GPUs)
with redirect_stdout(StringIO()), redirect_stderr(StringIO()):
    gpunet = torch.hub.load('NVIDIA/DeepLearningExamples:torchhub', 'nvidia_gpunet', pretrained=False, model_type='GPUNet-0', model_math='fp32')

# Download weights from S3 if not present, then load them
model_path = os.getenv('MODEL_PATH', '/cache/torch/hub/checkpoints/gpunet-0.pth')
os.makedirs(os.path.dirname(model_path), exist_ok=True)  # Ensure checkpoints dir exists
if not os.path.exists(model_path):
    s3 = boto3.client('s3')
    s3.download_file(os.getenv('S3_BUCKET_NAME'), 'gpunet-0.pth', model_path)
checkpoint = torch.load(model_path, map_location=device, weights_only=True)
gpunet.load_state_dict(checkpoint['state_dict'])
# Move to GPU/CPU
gpunet.to(device)
gpunet.eval()

# Preprocessing
preprocess = transforms.Compose([
    transforms.Resize(256),
    transforms.CenterCrop(224),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
])

# Load ImageNet labels
labels_url = "https://s3.amazonaws.com/deep-learning-models/image-models/imagenet_class_index.json"
response = requests.get(labels_url)
json_data = json.loads(response.text)
labels = [json_data[str(i)][1].replace('_', ' ') for i in range(1000)]

# Required, FastAPI root
@app.get("/")
async def hello():
    return {"status": "hello"}

# Serve model requests
@app.post("/predict")
async def predict(image_url: str):
    try:
        response = requests.get(image_url)
        response.raise_for_status()
        img = Image.open(BytesIO(response.content)).convert("RGB")
        input_tensor = preprocess(img).unsqueeze(0).to(device)

        with torch.no_grad():
            output = gpunet(input_tensor)

        probs = softmax(output, dim=1)[0]
        top5_idx = probs.topk(5).indices.cpu().numpy()
        top5_probs = probs.topk(5).values.cpu().numpy()

        results = [{ "label": labels[idx], "probability": float(prob) } for idx, prob in zip(top5_idx, top5_probs)]

        return {"predictions": results}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
```

#### Create the Dockerfile

The following Dockerfile creates a container image for our application utilizing the GPUNet model from the [NVIDIA Deep Learning Examples for Tensor Cores](https://github.com/NVIDIA/DeepLearningExamples "https://github.com/NVIDIA/DeepLearningExamples") GitHub repository.

We reduce container image size by using a runtime-only PyTorch base, installing only essential packages with cache cleanup, pre-caching model code, and avoiding "baking" weights in the container image to enable faster pulls and updates. To learn more, see [Reducing Container Image Sizes](../best-practices/aiml-performance.md#_reducing_container_image_sizes "../best-practices/aiml-performance.md#_reducing_container_image_sizes").

In the same directory as `app.py`, create the `Dockerfile`:

```
FROM pytorch/pytorch:2.4.0-cuda12.4-cudnn9-runtime

# Install required system packages required for git cloning
RUN apt-get update && apt-get install -y git && rm -rf /var/lib/apt/lists/*

# Install application dependencies
RUN pip install --no-cache-dir fastapi uvicorn requests pillow boto3 timm==0.5.4

# Pre-cache the GPUNet code from Torch Hub (without weights)
# Clone the repository containing the GPUNet code
RUN mkdir -p /cache/torch/hub && \
    cd /cache/torch/hub && \
    git clone --branch torchhub --depth 1 https://github.com/NVIDIA/DeepLearningExamples NVIDIA_DeepLearningExamples_torchhub

COPY app.py /app/app.py

WORKDIR /app

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "80"]
```

#### Test the application

From the same directory as your `app.py` and `Dockerfile`, build the container image for the inference application, targeting AMD64 architecture:

```
docker build --platform linux/amd64 -t gpunet-inference-app .
```

Set environment variables for your AWS credentials, and optionally an AWS session token. For example:

```
export AWS_REGION="us-east-1"
export AWS_ACCESS_KEY_ID=ABCEXAMPLESCUJFEIELSMUHHAZ
export AWS_SECRET_ACCESS_KEY=123EXAMPLEMZREoQXr8XkiicsOgWDQ5TpUsq0/Z
```

Run the container locally, injecting AWS credentials as environment variables for S3 access. For example:

```
docker run --platform linux/amd64 -p 8080:80 \
  -e S3_BUCKET_NAME=${S3_BUCKET_NAME} \
  -e AWS_ACCESS_KEY_ID=${AWS_ACCESS_KEY_ID} \
  -e AWS_SECRET_ACCESS_KEY=${AWS_SECRET_ACCESS_KEY} \
  -e AWS_DEFAULT_REGION=${AWS_REGION} \
  gpunet-inference-app
```

The expected output should look like this:

```
INFO:     Started server process [1]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:80 (Press CTRL+C to quit)
```

In a new terminal window, test the inference endpoint by sending a sample POST request with a public image URL as a query parameter:

```
curl -X POST "http://localhost:8080/predict?image_url=http://images.cocodataset.org/test-stuff2017/000000024309.jpg"
```

The expected output should be a JSON response with top-5 predictions, similar to this (actual labels and probabilities may vary slightly based on the image and model precision):

```
{"predictions":[{"label":"desk","probability":0.28885871171951294},{"label":"laptop","probability":0.24679335951805115},{"label":"notebook","probability":0.08539070934057236},{"label":"library","probability":0.030645888298749924},{"label":"monitor","probability":0.02989606373012066}]}
```

Quit the application using "Ctrl + C".

### Push the container to Amazon ECR

In this step, we upload the container image for the GPUNet-0 model service to [Amazon Elastic Container Registry (ECR)](../../../AmazonECR/latest/userguide/what-is-ecr.md "../../../AmazonECR/latest/userguide/what-is-ecr.md"), making it available for deployment on Amazon EKS. This process involves creating a new ECR repository to store the image, authenticating with ECR, then tagging and pushing the container image to our registry.

First, navigate back to the directory where you set your environment variables at the beginning of this guide. For example:

```
cd ..
```

Create a repository in Amazon ECR:

```
aws ecr create-repository --repository-name gpunet-inference-app --region ${AWS_REGION}
```

Log into Amazon ECR:

```
aws ecr get-login-password --region ${AWS_REGION} | docker login --username AWS --password-stdin ${AWS_ACCOUNT_ID}.dkr.ecr.${AWS_REGION}.amazonaws.com
```

The expected output should look like this:

```
Login Succeeded
```

Tag the image:

```
docker tag gpunet-inference-app:latest ${AWS_ACCOUNT_ID}.dkr.ecr.${AWS_REGION}.amazonaws.com/gpunet-inference-app:latest
```

Push the image to your Amazon ECR repository:

```
docker push ${AWS_ACCOUNT_ID}.dkr.ecr.${AWS_REGION}.amazonaws.com/gpunet-inference-app:latest
```

This last step takes several minutes to complete.

## 7. (Optional) Expose the Model Service

In this step, you’ll expose your real-time inference model service externally on Amazon EKS using the AWS Load Balancer Controller (LBC). This involves setting up the LBC, mounting model weights from Amazon S3 as a persistent volume using the Mountpoint S3 CSI Driver, deploying a GPU-accelerated application pod, creating a service and ingress to provision an Application Load Balancer (ALB), and testing the endpoint.

First, verify the Pod Identity association for the AWS LBC, confirming that the service account is properly linked to the required IAM role:

```
eksctl get podidentityassociation --cluster ${EKS_CLUSTER_NAME} --namespace kube-system --service-account-name aws-load-balancer-controller
```

The expected output should look like this:

```
ASSOCIATION ARN                                                    NAMESPACE    SERVICE ACCOUNT NAME        IAM ROLE ARN    OWNER ARN
arn:aws:eks:us-east-1:143095308808:podidentityassociation/eks-rt-inference-us-east-1/a-buavluu2wp1jropya    kube-system     aws-load-balancer-controller    arn:aws:iam::143095308808:role/AmazonEKSLoadBalancerControllerRole
```

### Tag your cluster security group

The AWS Load Balancer Controller only supports a single security group with the tag key `karpenter.sh/discovery: "${EKS_CLUSTER_NAME}"` for Karpenter’s security group selection. When creating a cluster with eksctl, the default cluster security group (which has the `"kubernetes.io/cluster/<cluster-name>: owned"` tag) is not automatically tagged with `karpenter.sh/discovery` tags. This tag is essential for Karpenter to discover and attach this security group to the nodes it provisions. Attaching this security group ensures compatibility with the AWS Load Balancer Controller (LBC), allowing it to automatically manage inbound traffic rules for services exposed via Ingress, such as the model service in these steps.

Export the VPC ID for your cluster:

```
CLUSTER_VPC_ID="$(aws eks describe-cluster --name ${EKS_CLUSTER_NAME} --query cluster.resourcesVpcConfig.vpcId --output text)"
```

Export the default security group for your cluster:

```
CLUSTER_SG_ID="$(aws ec2 describe-security-groups --filters Name=vpc-id,Values=$CLUSTER_VPC_ID Name=tag-key,Values=kubernetes.io/cluster/${EKS_CLUSTER_NAME} --query 'SecurityGroups[].[GroupId]' --output text)"
```

Add the `karpenter.sh/discovery` tag to the default cluster security group. This will allow our CPU and GPU EC2NodeClass selectors to use it:

```
aws ec2 create-tags --resources ${CLUSTER_SG_ID} --tags Key=karpenter.sh/discovery,Value=${EKS_CLUSTER_NAME}
```

Verify the tag was added:

```
aws ec2 describe-security-groups --group-ids ${CLUSTER_SG_ID} --query "SecurityGroups[].Tags"
```

Among the results, you should see the following with the tag and your cluster name. For example:

```
{
  "Key": "karpenter.sh/discovery",
  "Value": "eks-rt-inference-us-east-1"
}
```

### Setup the AWS Load Balancer Controller (LBC)

The AWS LBC is essential for managing ingress traffic to AI/ML workloads on Amazon EKS, ensuring access to inference endpoints or data processing pipelines. By integrating with AWS Application Load Balancers (ALB) and Network Load Balancers (NLB), the LBC dynamically routes traffic to containerized applications, such as those running large language models, computer vision models, or real-time inference services. Since we’ve already created the service account and the Pod Identity Association during cluster creation, we set the `serviceAccount.name` to match what’s defined in our cluster config (`aws-load-balancer-controller`).

Add the AWS-owned **eks-charts** Helm chart repository:

```
helm repo add eks https://aws.github.io/eks-charts
```

Refresh your local Helm repositories with the most recent charts:

```
helm repo update eks
```

Deploy the AWS LBC using Helm, specifying the EKS cluster name and referencing the pre-created service account:

```
helm install aws-load-balancer-controller eks/aws-load-balancer-controller \
  -n kube-system \
  --set clusterName=${EKS_CLUSTER_NAME} \
  --set serviceAccount.create=false \
  --set serviceAccount.name=aws-load-balancer-controller
```

The expected output should look like this:

```
NAME: aws-load-balancer-controller
LAST DEPLOYED: Wed Jul 9 15:03:31 2025
NAMESPACE: kube-system
STATUS: deployed
REVISION: 1
TEST SUITE: None
NOTES:
AWS Load Balancer controller installed!
```

### Mount the model in a persistent volume

In this step, you’ll mount model weights from your Amazon S3 bucket using a PersistentVolume (PV) backed by the Mountpoint for Amazon S3 CSI driver. This allows Kubernetes pods to access S3 objects as local files, eliminating resource-intensive downloads to ephemeral pod storage or init containers—ideal for large, multi-gigabyte model weights.

The PV mounts the entire bucket root (no path specified in `volumeAttributes`), supports concurrent read-only access by multiple pods, and exposes files like the model weights (`/models/gpunet-0.pth`) inside the container for inference. This ensures the fallback "download" in our application (`app.py`) does not trigger because the file exists via the mount. By decoupling the model from the container image, this enables shared access and independent model version updates without image rebuilds.

#### Create the PersistentVolume (PV)

Create a PersistentVolume (PV) resource to mount the S3 bucket containing your model weights, enabling read-only access for multiple pods without downloading files at runtime:

```
cat <<EOF | envsubst | kubectl apply -f -
apiVersion: v1
kind: PersistentVolume
metadata:
  name: s3-model-pv
spec:
  capacity:
    storage: 5Gi  # Ignored by the driver; can be any value
  accessModes:
    - ReadOnlyMany  # Read only
  persistentVolumeReclaimPolicy: Retain
  storageClassName: ""  # Required for static provisioning
  claimRef:
    namespace: default  # Adjust if you prefer a different namespace
    name: s3-model-pvc
  mountOptions:
    - allow-other  # Enables multi-user access (useful for non-root pods)
    - region ${AWS_REGION} # Optional, include if your bucket is in a different region than the cluster
  csi:
    driver: s3.csi.aws.com
    volumeHandle: gpunet-model-volume  # Must be unique across all PVs
    volumeAttributes:
      bucketName: ${S3_BUCKET_NAME}
EOF
```

#### Create the PersistentVolumeClaim (PVC)

Create a PersistentVolumeClaim (PVC) to bind to the PV, requesting read-only access to the mounted S3 model data:

```
cat <<EOF | envsubst | kubectl apply -f -
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: s3-model-pvc
spec:
  accessModes:
    - ReadOnlyMany
  storageClassName: ""  # Required for static provisioning
  resources:
    requests:
      storage: 5Gi  # Ignored, match PV capacity
  volumeName: s3-model-pv  # Bind to the PV created above
EOF
```

#### Deploy the application

Deploy the inference application as a Kubernetes Deployment, mounting the S3-backed persistent volume for model access, applying GPU node selectors and tolerations, and setting environment variables for the model path. This Deployment sets the model path (env var of `"/models/gpunet-0.pth"`), so our application (in `app.py`) will use this path by default. With the Deployment’s volume mount at `/models` (read-only), the model download won’t trigger if the file is already present via the PVC.

```
cat <<EOF | envsubst | kubectl apply -f -
apiVersion: apps/v1
kind: Deployment
metadata:
  name: gpunet-inference-app
spec:
  replicas: 1
  selector:
    matchLabels:
      app: gpunet-inference-app
  template:
    metadata:
      labels:
        app: gpunet-inference-app
    spec:
      tolerations:
      - key: "nvidia.com/gpu"
        operator: "Exists"
        effect: "NoSchedule"
      nodeSelector:
        role: gpu-worker
      containers:
      - name: inference
        image: ${AWS_ACCOUNT_ID}.dkr.ecr.${AWS_REGION}.amazonaws.com/gpunet-inference-app:latest
        ports:
        - containerPort: 80
        env:
        - name: MODEL_PATH
          value: "/models/gpunet-0.pth"
        resources:
          limits:
            nvidia.com/gpu: 1
          requests:
            nvidia.com/gpu: 1
        volumeMounts:
        - name: model-volume
          mountPath: /models
          readOnly: true
      volumes:
      - name: model-volume
        persistentVolumeClaim:
          claimName: s3-model-pvc
EOF
```

It will take a few minutes for Karpenter to provision a GPU node if one isn’t already available. Verify that the inference pod is in a "Running" state:

```
kubectl get pods -l app=gpunet-inference-app
```

The expected output should look like this:

```
NAME                               READY   STATUS    RESTARTS   AGE
gpunet-inference-app-5d4b6c7f8-abcde        1/1     Running   0          2m
```

### Expose the Service with Ingress and Load Balancer

Create a ClusterIP Service to expose the inference deployment internally within the EKS cluster, targeting the application’s port:

```
cat <<EOF | envsubst | kubectl apply -f -
apiVersion: v1
kind: Service
metadata:
  name: gpunet-model-service
spec:
  type: ClusterIP
  ports:
  - port: 80
    targetPort: 80
  selector:
    app: gpunet-inference-app
EOF
```

Create an Ingress resource to provision an internet-facing Application Load Balancer (ALB) via the AWS LBC, routing external traffic to the inference service:

```
cat <<EOF | envsubst | kubectl apply -f -
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: gpunet-model-ingress
  annotations:
    alb.ingress.kubernetes.io/scheme: internet-facing
    alb.ingress.kubernetes.io/target-type: ip
spec:
  ingressClassName: alb
  rules:
  - http:
      paths:
      - path: /
        pathType: Prefix
        backend:
          service:
            name: gpunet-model-service
            port:
              number: 80
EOF
```

Give it a few minutes for the Application Load Balancer (ALB) to finish provisioning. Monitor the Ingress resource status to confirm the ALB has been provisioned:

```
kubectl get ingress gpunet-model-ingress
```

The expected output should look like this (with the ADDRESS field populated):

```
NAME                   CLASS   HOSTS   ADDRESS                                         PORTS   AGE
gpunet-model-ingress   alb     *       k8s-default-gpunetmo-183de3f819-516310036.us-east-1.elb.amazonaws.com   80      6m58s
```

Extract and export the ALB hostname from the Ingress status for use in subsequent testing:

```
export ALB_HOSTNAME=$(kubectl get ingress gpunet-model-ingress -o jsonpath='{.status.loadBalancer.ingress[0].hostname}')
```

### Test the Model Service

Validate the exposed inference endpoint by sending a POST request with a sample image URL (e.g., from the COCO dataset), simulating real-time prediction:

```
curl -X POST "http://${ALB_HOSTNAME}/predict?image_url=http://images.cocodataset.org/test-stuff2017/000000024309.jpg"
```

The expected output should be a JSON response with top-5 predictions, similar to this (actual labels and probabilities may vary slightly based on the image and model precision):

```
{"predictions":[{"label":"desk","probability":0.2888975441455841},{"label":"laptop","probability":0.2464350312948227},{"label":"notebook","probability":0.08554483205080032},{"label":"library","probability":0.030612602829933167},{"label":"monitor","probability":0.029896672815084457}]}
```

You can optionally continue testing other images in a new POST request. For example:

```
http://images.cocodataset.org/test-stuff2017/000000024309.jpg
http://images.cocodataset.org/test-stuff2017/000000028117.jpg
http://images.cocodataset.org/test-stuff2017/000000006149.jpg
http://images.cocodataset.org/test-stuff2017/000000004954.jpg
```

## Conclusion

In this guide, you set up an Amazon EKS cluster optimized for GPU-accelerated real-time inference workloads. You provisioned a cluster with [G5 EC2 instances](https://aws.amazon.com/ec2/instance-types/g5/ "https://aws.amazon.com/ec2/instance-types/g5/"), installed the [Mountpoint S3 CSI Driver](s3-csi.md "s3-csi.md"), [EKS Pod Identity Agent](pod-identities.md "pod-identities.md"), [EKS Node Monitoring Agent](node-health.md "node-health.md"), [Bottlerocket AMI](eks-optimized-ami-bottlerocket.md "eks-optimized-ami-bottlerocket.md"), [AWS Load Balancer Controller (LBC)](lbc-helm.md "lbc-helm.md"), and [Karpenter](https://karpenter.sh/ "https://karpenter.sh/") to manage CPU and GPU NodePools. You used the NVIDIA Device Plugin to enable GPU scheduling and configured S3 with a PersistentVolume and PersistentVolumeClaim for model access. You validated the setup by deploying a sample GPU pod, setting up model access for the NVIDIA [GPUNet-0](https://catalog.ngc.nvidia.com/orgs/nvidia/teams/dle/models/gpunet_0_pyt_ckpt "https://catalog.ngc.nvidia.com/orgs/nvidia/teams/dle/models/gpunet_0_pyt_ckpt") model on [Amazon S3](https://aws.amazon.com/s3/ "https://aws.amazon.com/s3/"), enabling pod initialization, and exposing the inference service via Application Load Balancer. To fully utilize your cluster, configure the [EKS Node Monitoring Agent](node-health.md "node-health.md") with auto-repair. Be sure to conduct benchmark tests, including GPU performance, latency, and throughput assessments to optimize response times. To learn more, see [Using Monitoring and Observability Tools for your AI/ML Workloads](../best-practices/aiml-observability.md#_using_monitoring_and_observability_tools_for_your_aiml_workloads "../best-practices/aiml-observability.md#_using_monitoring_and_observability_tools_for_your_aiml_workloads").

## Clean up

To avoid incurring future charges, you need to delete the associated CloudFormation stack manually to delete all resources created during this guide, including the VPC network.

Delete the CloudFormation stack using the `--wait` flag with eksctl:

```
eksctl delete cluster --region ${AWS_REGION} --name ${EKS_CLUSTER_NAME} --wait
```

Upon completion, you should see the following response output:

```
2025-07-29 13:03:55 [✔]  all cluster resources were deleted
```

Delete the Amazon S3 bucket created during this guide using the [Amazon S3 Console](https://console.aws.amazon.com/s3/home "https://console.aws.amazon.com/s3/home").
