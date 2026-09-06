

 **Help improve this page** 

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Set up Amazon EKS cluster for AI/ML workloads
<a name="ml-cluster-setup"></a>

**Tip**  
 [Register](https://events.eksworkshop.com/workshops/genai/) for upcoming Amazon EKS AI/ML workshops.

This section guides you through creating an Amazon EKS cluster ready to run inference workloads, including the compute with GPUs, monitoring stack, and Amazon S3 storage for model weights, along with the necessary AWS IAM permissions.

## Architecture overview
<a name="_architecture_overview"></a>

The setup creates the following infrastructure:
+  **EKS cluster with GPU-enabled nodes** — A Karpenter-managed NodePool that dynamically provisions G-family GPU instances using Spot capacity with On-Demand fallback.
+  **Monitoring stack** — Prometheus scrapes cluster, node, and GPU metrics and remote-writes them to Amazon Managed Service for Prometheus (AMP). Grafana provides dashboards for visualization. The NVIDIA DCGM Exporter adds GPU-specific metrics including utilization, memory, temperature, power draw, NVLink bandwidth, and tensor activity.
+  **Model weights S3 bucket** — An Amazon S3 bucket for storing model weights, with an EKS Pod Identity association that grants workload pods read/write access.

## Cluster compute options
<a name="_cluster_compute_options"></a>

The guide provides two paths for setting up your cluster. Choose one and follow it consistently through all steps.
+  **EKS Auto Mode** — A single command provisions an EKS cluster with EKS Auto Mode enabled. All of the required components are provided out-of-the-box including Karpenter-based auto-scaling, the EKS node monitoring agent, fast container pulls with SOCI, and the NVIDIA device plugin.
+  **Self-managed Karpenter** — You install and configure each component explicitly: Karpenter via `eksctl`, automatic node repair through its feature gate, the EKS node monitoring agent as an EKS add-on, and the NVIDIA device plugin via Helm. You also create a custom `EC2NodeClass` that uses the EKS-optimized NVIDIA AL2023 AMIs and configures SOCI.

## What you’ll set up
<a name="_what_youll_set_up"></a>


| Step | Description | 
| --- | --- | 
|  **Create cluster**  | Provision the EKS control plane and cluster-level components needed for GPU workloads. | 
|  **Create dynamically provisioned GPU nodes**  | Define a dynamic GPU NodePool that provisions G-family GPU instances as workloads are scheduled. | 
|  **Test with a sample pod**  | Validate the setup end-to-end by running an `nvidia-smi` pod that triggers Karpenter to provision a GPU-enabled node. | 
|  **Add reserved capacity (optional)**  | Attach an On-Demand Capacity Reservation (ODCR) to your NodeClass for reserved-first with Spot/On-Demand fallback. | 
|  **Install monitoring**  | Deploy kube-prometheus-stack (Prometheus \+ Grafana) with remote-write to AMP, plus the NVIDIA DCGM Exporter for GPU metrics. | 
|  **Create model weights bucket**  | Create an S3 bucket and configure EKS Pod Identity so workload pods can read and write model weights. | 

## Get started
<a name="_get_started"></a>

For step-by-step instructions using the AWS CLI, see [Set up Amazon EKS cluster for AI/ML workloads using CLIs](ml-cluster-setup-cli.md). For step-by-step instructions using Terraform, see [Set up Amazon EKS cluster for AI/ML workloads using Terraform](ml-cluster-setup-tf.md).