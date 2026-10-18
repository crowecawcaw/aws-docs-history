

 **Help improve this page** 

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Set up Amazon EKS cluster for AI/ML workloads
<a name="ml-cluster-setup"></a>

**Tip**  
 [Register](https://events.eksworkshop.com/workshops/genai/) for upcoming Amazon EKS AI/ML workshops.

This section sets up the supporting infrastructure that AI/ML training and inference workloads need on Amazon EKS. This includes the EKS cluster itself, load balancing for in-cluster endpoints, a monitoring stack, Amazon S3 storage for model weights, and the AWS IAM permissions that connect them.

You provision GPU compute afterward, in [Create a GPU NodePool for AI/ML inference](ml-inference-gpu-nodepool.md). Setting up this infrastructure first means that monitoring and storage are already in place when GPU nodes join the cluster, so the GPU components start reporting metrics as soon as the nodes are ready.

## Architecture overview
<a name="_architecture_overview"></a>

The setup creates the following infrastructure:
+  **EKS cluster** — An EKS cluster with the cluster-level components that GPU workloads depend on, including EKS Auto Mode or Karpenter for node auto-scaling and the NVIDIA device plugin.
+  **Load balancing** — An `alb` `IngressClass` backed by an AWS Application Load Balancer, which fronts traffic for Grafana and, later, the inference endpoint.
+  **Monitoring stack** — Prometheus scrapes cluster, node, and GPU metrics and remote-writes them to Amazon Managed Service for Prometheus (AMP). Grafana provides dashboards for visualization. The NVIDIA DCGM Exporter adds GPU-specific metrics including utilization, memory, temperature, power draw, NVLink bandwidth, and tensor activity.
+  **Model weights S3 bucket** — An Amazon S3 bucket for storing model weights, with an EKS Pod Identity association that grants workload pods read/write access.

## Cluster compute options
<a name="_cluster_compute_options"></a>

The guide provides two paths for setting up your cluster, which differ in how much of the node lifecycle you manage yourself. Choose one and follow it consistently through all steps, including the GPU NodePool you create later.
+  **EKS Auto Mode** — A single command provisions an EKS cluster with EKS Auto Mode enabled. All of the required components are provided out-of-the-box including Karpenter-based auto-scaling, the EKS node monitoring agent, fast container pulls with SOCI, and the NVIDIA device plugin.
+  **Self-managed Karpenter** — You install and configure each component explicitly: Karpenter by using `eksctl`, automatic node repair through its feature gate, the EKS node monitoring agent as an EKS add-on, and the NVIDIA device plugin by using Helm. You also create a custom `EC2NodeClass` that uses the EKS-optimized NVIDIA AL2023 AMIs and configures SOCI.

## What you’ll set up
<a name="_what_youll_set_up"></a>


| Step | Description | 
| --- | --- | 
|  **Create cluster**  | Provision the EKS control plane and cluster-level components needed for GPU workloads. | 
|  **Set up load balancing**  | Deploy an Application Load Balancer (ALB) to front traffic for Grafana and the inference endpoint. | 
|  **Install monitoring**  | Deploy kube-prometheus-stack (Prometheus \+ Grafana) with remote-write to AMP, plus the NVIDIA DCGM Exporter for GPU metrics. | 
|  **Create model weights bucket**  | Create an S3 bucket and configure EKS Pod Identity so workload pods can read and write model weights. | 

Once you finish setting up your cluster, the next step is GPU compute. For instructions on creating the GPU NodePool that dynamically provisions GPU instances, see [Create a GPU NodePool for AI/ML inference](ml-inference-gpu-nodepool.md).

## Get started
<a name="_get_started"></a>
+ For step-by-step instructions using the AWS CLI, see [Set up Amazon EKS cluster for AI/ML workloads using CLIs](ml-cluster-setup-cli.md).
+ For step-by-step instructions using Terraform, see [Set up Amazon EKS cluster for AI/ML workloads using Terraform](ml-cluster-setup-tf.md).