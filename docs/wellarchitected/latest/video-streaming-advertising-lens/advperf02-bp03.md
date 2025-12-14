# ADVPERF02-BP03 Consider using low latency scaling tools like Karpenter to improve startup and scaling time

Integrate observability metrics to initiate scaling of compute
resources. Use open-source frameworks like Karpenter and KEDA,
which provide for low startup latency scaling.

## Implementation guidance

Karpenter (an open-source Amazon tool) for Kubernetes workloads
can help with low-latency scaling and bursty traffic patterns
for adtech workloads. 

- **Faster node provisioning:**
  Karpenter can provision new nodes in a Kubernetes cluster
  much faster than traditional auto scaling methods, as
  Karpenter integrates directly with AWS APIs and can use
  services like Amazon EC2 Auto Scaling groups for rapid node
  provisioning.
- **Node pre-warming:**
  Although Karpenter does not support prewarmed node pools like Auto Scaling groups, you can use [pod priority](https://aws.amazon.com/blogs/containers/eliminate-kubernetes-node-scaling-lag-with-pod-priority-and-over-provisioning/ "https://aws.amazon.com/blogs/containers/eliminate-kubernetes-node-scaling-lag-with-pod-priority-and-over-provisioning/") to maintain a pool of
  pre-initialized nodes. When new nodes are needed, Karpenter
  can quickly provision them from this pre-warmed pool,
  further reducing the latency associated with node
  provisioning.
- **Horizontal Pod Autoscaling (HPA)
  integration:** Karpenter can be configured to work
  in tandem with the Kubernetes Horizontal Pod Autoscaler
  (HPA). This integration allows Karpenter to provision new
  nodes proactively based on the HPA's scaling decisions,
  which makes resources available before pods start
  experiencing resource constraints.
- **Optimized node selection:**
  Karpenter can provision nodes with the appropriate instance
  types and resource configurations based on the requirements
  of the workloads. This optimization schedules pods on nodes
  with sufficient resources, minimizing the need for
  rescheduling or resource contention, which can introduce
  latency.
- **Parallel node
  provisioning:** Karpenter can provision multiple
  nodes in parallel, allowing it to rapidly scale out the
  cluster when faced with sudden spikes in demand. This
  parallelism helps minimize the overall latency associated
  with scaling operations.

## Key AWS services

- [Amazon Elastic Kubernetes Service (EKS)](https://aws.amazon.com/eks/ "https://aws.amazon.com/eks/")

## Resources

- [Manage
  scale-to-zero scenarios with Karpenter and Serverless](https://aws.amazon.com/blogs/containers/manage-scale-to-zero-scenarios-with-karpenter-and-serverless/ "https://aws.amazon.com/blogs/containers/manage-scale-to-zero-scenarios-with-karpenter-and-serverless/")
- [Proactive autoscaling of Kubernetes workloads with KEDA using metrics ingested into Amazon Managed Service for Prometheus](https://aws.amazon.com/blogs/mt/proactive-autoscaling-kubernetes-workloads-keda-metrics-ingested-into-aws-amp/ "https://aws.amazon.com/blogs/mt/proactive-autoscaling-kubernetes-workloads-keda-metrics-ingested-into-aws-amp/")
- [Scalable and Cost-Effective Event-Driven Workloads with KEDA and
  Karpenter on Amazon EKS](https://aws.amazon.com/blogs/containers/scalable-and-cost-effective-event-driven-workloads-with-keda-and-karpenter-on-amazon-eks/ "https://aws.amazon.com/blogs/containers/scalable-and-cost-effective-event-driven-workloads-with-keda-and-karpenter-on-amazon-eks/")
