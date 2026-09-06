

 **Help improve this page** 

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Manage NVIDIA GPUs on Amazon EKS
<a name="device-management-nvidia"></a>

NVIDIA GPUs are widely used for machine learning training, inference, and high-performance computing workloads. Amazon EKS supports two mechanisms for managing NVIDIA GPU devices in your EKS clusters: the *NVIDIA DRA driver for GPUs* and the *NVIDIA Kubernetes device plugin*.

We recommend using DRA drivers for new deployments with Kubernetes versions 1.34 and later when using [static capacity provisioning](https://karpenter.sh/docs/concepts/nodepools/#static-nodepool) in Karpenter, EKS managed node groups, or self-managed nodes. DRA is not currently supported with EKS Auto Mode. The NVIDIA DRA driver enables flexible GPU allocation and GPU sharing between containers.

For the availability of DRA features in EKS, see the [Release notes for Kubernetes versions](kubernetes-versions-standard.md) for EKS. For more information on using the NVIDIA DRA driver and device plugin with EKS, see [Use the NVIDIA DRA driver or device plugin on Amazon EKS](device-management-nvidia-dra-device-plugin.md).

## GPU sharing (MIG & time-slicing)
<a name="eks-nvidia-gpu-sharing"></a>

 **Multi-instance GPU (MIG)** 

Multi-Instance GPU (MIG) is a hardware feature on NVIDIA GPUs that partitions a single physical GPU into multiple isolated instances. The maximum number of instances depends on the GPU. Data center GPUs such as the A100, H100, H200, and B200 support up to seven instances, while the Blackwell-based `g7` and `g7e` GPUs support fewer. Each instance has dedicated memory, compute units, and memory bandwidth, so a workload that runs on one instance cannot affect a workload on another. Unlike time-slicing, which shares a GPU through software time-multiplexing without isolation, MIG provides hardware-level memory and fault isolation between Pods.

MIG is best suited to multi-tenant inference, workloads that require predictable quality of service, and environments with compliance requirements for hardware-isolated tenancy. It is available on NVIDIA Ampere (A100), Hopper (H100 and H200), and Blackwell GPUs. On AWS, these are the P-family instance types and the Blackwell-based `g7` and `g7e` instance types.

For more information and steps for using MIG with NVIDIA GPUs and EKS, see [Use multi-instance GPUs (MIG) with NVIDIA GPUs on Amazon EKS](device-management-nvidia-mig.md).

 **Time-slicing** 

Time-slicing lets multiple Pods share a single physical NVIDIA GPU by configuring the NVIDIA device plugin or DRA driver to advertise more than one schedulable slot per GPU. The Kubernetes scheduler places multiple Pods on the same GPU, and the GPU’s CUDA scheduler time-multiplexes the workloads.

Time-slicing is the simplest GPU-sharing strategy. It uses software only, requires no special hardware, and works on every NVIDIA GPU instance type on AWS. Time-slicing does not offer memory or compute isolation between Pods that share a GPU. It is best for workloads with low GPU utilization, such as inference services that idle between requests or development environments where several users share a GPU. For workloads that require hardware-level memory and compute isolation, use MIG instead.

For more information and steps for using time-slicing with NVIDIA GPUs and EKS, see [Use time-slicing with NVIDIA GPUs on Amazon EKS](device-management-nvidia-time-slicing.md).

## Topics
<a name="_topics"></a>
+  [Use the NVIDIA DRA driver or device plugin on Amazon EKS](device-management-nvidia-dra-device-plugin.md) 
+  [Use multi-instance GPUs (MIG) with NVIDIA GPUs on Amazon EKS](device-management-nvidia-mig.md) 
+  [Use time-slicing with NVIDIA GPUs on Amazon EKS](device-management-nvidia-time-slicing.md) 