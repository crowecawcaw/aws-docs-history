

 **Help improve this page** 

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Resources to get started with AI/ML on Amazon EKS
<a name="ml-resources"></a>

To jump into Machine Learning on EKS, start by choosing from these prescriptive patterns to quickly get an EKS cluster and ML software and hardware ready to begin running ML workloads.

## Workshops
<a name="aiml-workshops"></a>

### [Generative AI on Amazon EKS Workshop](https://genai.eksworkshop.com/)
<a name="_generative_ai_on_amazon_eks_workshop"></a>

Learn how to get started with Large Language Model (LLM) applications and inference on Amazon EKS. Discover how to deploy and manage production-grade LLM workloads. Through hands-on labs, you’ll explore how to leverage Amazon EKS along with AWS services and open-source tools to create robust LLM solutions. The workshop environment provides all the necessary infrastructure and tools, allowing you to focus on learning and implementation.

### [Generative AI on Amazon EKS using Neuron](https://catalog.us-east-1.prod.workshops.aws/workshops/e21aadbd-23cb-4207-bd09-625e6de08a6c/en-US)
<a name="_generative_ai_on_amazon_eks_using_neuron"></a>

Learn how to get started with Large Language Model (LLM) applications and inference on Amazon EKS. Discover how to deploy and manage production-grade LLM workloads, implement advanced RAG patterns with vector databases, and build data-backed LLM applications using open-source frameworks. Through hands-on labs, you’ll explore how to leverage Amazon EKS along with AWS services and open-source tools to create robust LLM solutions. The workshop environment provides all the necessary infrastructure and tools, allowing you to focus on learning and implementation.

## [Best Practices](https://docs.aws.amazon.com/eks/latest/best-practices/aiml.html)
<a name="aiml-best-practices"></a>

The AI/ML focused topics in the Amazon EKS Best Practices guide provide detailed recommendations across the following areas to optimize your AI/ML workloads on Amazon EKS.

### [AI/ML Compute and Autoscaling](https://docs.aws.amazon.com/eks/latest/best-practices/aiml-compute.html)
<a name="_aiml_compute_and_autoscaling"></a>

This section outlines best practices for optimizing AI/ML compute and autoscaling in Amazon EKS, focusing on GPU resource management, node resiliency, and application scaling. It provides strategies such as scheduling workloads with well-known labels and node affinity, using ML Capacity Blocks or On-Demand Capacity Reservations, and implementing node health checks with tools like EKS Node Monitoring Agent.

### [AI/ML Networking](https://docs.aws.amazon.com/eks/latest/best-practices/aiml-networking.html)
<a name="_aiml_networking"></a>

This section outlines best practices for optimizing AI/ML networking in Amazon EKS to enhance performance and scalability, including strategies like selecting instances with higher network bandwidth or Elastic Fabric Adapter (EFA) for distributed training, installing tools like MPI and NCCL, and enabling prefix delegation to increase IP addresses and improve pod launch times.

### [AI/ML Security](https://docs.aws.amazon.com/eks/latest/best-practices/aiml-security.html)
<a name="_aiml_security"></a>

This section focuses on securing data storage and ensuring compliance for AI/ML workloads on Amazon EKS, including practices such as using Amazon S3 with AWS Key Management Service (KMS) for server-side encryption (SSE-KMS), configuring buckets with regional KMS keys and S3 Bucket Keys to reduce costs, granting IAM permissions for KMS actions like decryption to EKS pods, and auditing with AWS CloudTrail logs.

### [AI/ML Storage](https://docs.aws.amazon.com/eks/latest/best-practices/aiml-storage.html)
<a name="_aiml_storage"></a>

This section provides best practices for optimizing storage in AI/ML workloads on Amazon EKS, including practices like deploying models using CSI drivers to mount services like S3, FSx for Lustre, or EFS as Persistent Volumes, selecting storage based on workload needs (e.g., FSx for Lustre for distributed training with options like Scratch-SSD or Persistent-SSD), and enabling features like data compression and striping.

### [AI/ML Observability](https://docs.aws.amazon.com/eks/latest/best-practices/aiml-observability.html)
<a name="_aiml_observability"></a>

This section focuses on monitoring and optimizing GPU utilization for AI/ML workloads on Amazon EKS to improve efficiency and reduce costs, including strategies such as targeting high GPU usage with tools like CloudWatch Container Insights and NVIDIA’s DCGM-Exporter integrated with Prometheus and Grafana, and metrics we recommend analyzing for your AI/ML workloads.

### [AI/ML Performance](https://docs.aws.amazon.com/eks/latest/best-practices/aiml-performance.html)
<a name="_aiml_performance"></a>

This section focuses on enhancing application scaling and performance for AI/ML workloads on Amazon EKS through container image management and startup optimization, including practices such as using small lightweight base images or AWS Deep Learning Containers with multi-stage builds, preloading images via EBS snapshots or pre-pulling into runtime cache using DaemonSets or Deployments.

## Reference Architectures
<a name="aiml-reference-architectures"></a>

Explore these GitHub repositories for reference architectures, sample code, and utilities to implement distributed training and inference for AI/ML workloads on Amazon EKS and other AWS services.

### [AWSome Distributed Training](https://github.com/aws-samples/awsome-distributed-training)
<a name="_awsome_distributed_training"></a>

This repository offers a collection of best practices, reference architectures, model training examples, and utilities for training large models on AWS. It supports distributed training with Amazon EKS, including CloudFormation templates for EKS clusters, custom AMI and container builds, test cases for frameworks like PyTorch (DDP/FSDP, MegatronLM, NeMo) and JAX, and tools for validation, observability, and performance monitoring such as EFA Prometheus exporter and Nvidia Nsight Systems.

### [AWSome Inference](https://github.com/aws-samples/awsome-inference)
<a name="_awsome_inference"></a>

This repository provides reference architectures and test cases for optimizing inference solutions on AWS, with a focus on Amazon EKS and accelerated EC2 instances. It includes infrastructure setups for VPC and EKS clusters, projects for frameworks like NVIDIA NIMs, TensorRT-LLM, Triton Inference Server, and RayService, with examples for models such as Llama3-8B and Llama 3.1 405B. Features multi-node deployments using K8s LeaderWorkerSet, EKS autoscaling, Multi-Instance GPUs (MIG), and real-life use cases like an audio bot for ASR, inference, and TTS.

## Tutorials
<a name="aiml-tutorials"></a>

If you are interested in setting up Machine Learning platforms and frameworks in EKS, explore the tutorials described in this section. These tutorials cover everything from patterns for making the best use of GPU processors to choosing modeling tools to building frameworks for specialized industries.

### Build generative AI platforms on EKS
<a name="_build_generative_ai_platforms_on_eks"></a>
+  [Deploy Generative AI Models on Amazon EKS](https://aws.amazon.com/blogs/containers/deploy-generative-ai-models-on-amazon-eks/) 
+  [Building multi-tenant JupyterHub Platforms on Amazon EKS](https://aws.amazon.com/blogs/containers/building-multi-tenant-jupyterhub-platforms-on-amazon-eks/) 

### Run specialized generative AI frameworks on EKS
<a name="_run_specialized_generative_ai_frameworks_on_eks"></a>
+  [Accelerate your generative AI distributed training workloads with the NVIDIA NeMo Framework on Amazon EKS](https://aws.amazon.com/blogs/machine-learning/accelerate-your-generative-ai-distributed-training-workloads-with-the-nvidia-nemo-framework-on-amazon-eks/) 
+  [Running TorchServe on Amazon Elastic Kubernetes Service](https://aws.amazon.com/blogs/opensource/running-torchserve-on-amazon-elastic-kubernetes-service/) 

### Maximize NVIDIA GPU performance for ML on EKS
<a name="_maximize_nvidia_gpu_performance_for_ml_on_eks"></a>
+ Implement GPU sharing to efficiently use NVIDIA GPUs for your EKS clusters:

   [GPU sharing on Amazon EKS with NVIDIA time-slicing and accelerated EC2 instances](https://aws.amazon.com/blogs/containers/gpu-sharing-on-amazon-eks-with-nvidia-time-slicing-and-accelerated-ec2-instances/) 
+ Use Multi-Instance GPUs (MIGs) and NIM microservices to run more pods per GPU on your EKS clusters:

   [Maximizing GPU utilization with NVIDIA’s Multi-Instance GPU (MIG) on Amazon EKS: Running more pods per GPU for enhanced performance](https://aws.amazon.com/blogs/containers/maximizing-gpu-utilization-with-nvidias-multi-instance-gpu-mig-on-amazon-eks-running-more-pods-per-gpu-for-enhanced-performance/) 
+  [Build and deploy a scalable machine learning system on Kubernetes with Kubeflow on AWS](https://aws.amazon.com/blogs/machine-learning/build-and-deploy-a-scalable-machine-learning-system-on-kubernetes-with-kubeflow-on-aws/) 

### Run video encoding workloads on EKS
<a name="_run_video_encoding_workloads_on_eks"></a>
+  [Delivering video content with fractional GPUs in containers on Amazon EKS](https://aws.amazon.com/blogs/containers/delivering-video-content-with-fractional-gpus-in-containers-on-amazon-eks/) 

### Accelerate image loading for inference workloads
<a name="_accelerate_image_loading_for_inference_workloads"></a>
+  [How H2O.ai optimized and secured their AI/ML infrastructure with Karpenter and Bottlerocket](https://aws.amazon.com/blogs/containers/how-h2o-ai-optimized-and-secured-their-ai-ml-infrastructure-with-karpenter-and-bottlerocket/) 

### Monitoring ML workloads
<a name="_monitoring_ml_workloads"></a>
+  [Monitoring GPU workloads on Amazon EKS using AWS managed open-source services](https://aws.amazon.com/blogs/mt/monitoring-gpu-workloads-on-amazon-eks-using-aws-managed-open-source-services/) 
+  [Enable pod-based GPU metrics in Amazon CloudWatch](https://aws.amazon.com/blogs/machine-learning/enable-pod-based-gpu-metrics-in-amazon-cloudwatch/) 