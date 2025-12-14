# ADVPERF02-BP02 Consider containerization for scalability, low latency, and cost optimization

Adopt containerization as a strategy to operate at scale with low
latency and cost optimization. Evaluate the various options of
running container workloads on AWS.

## Implementation guidance

Consider containerization, which helps improve application
performance and helps scaling needs for adtech workloads, due to
the following benefits:

- **Faster startup times:**
  Containers share the host OS kernel and start only the
  necessary processes, so they can start almost instantly
  compared to a full virtual machine (VM) startup. This makes
  scaling up and down faster.
- **Lower resource usage:**
  Containers require fewer resources than VMs, as there is no
  guest OS overhead. More efficient resource usage leads to cost optimization and the ability to run more container instances per host.
- **Portability across
  environments:** Container images can run on any
  infrastructure due to standardized runtime without need to
  re-optimize for different environments.
- **Scaling and availability:**
  Container orchestrators (for example, Amazon EKS) help to
  scale containerized apps, provide high availability, and
  improve performance under heavy loads.
- **Isolation:** Containers
  isolate processes and resources per application, reducing
  noisy neighbor issues on multi-tenant hosts for more
  predictable performance.
- **Utilization:** Higher
  density of containers per host allows full utilization of
  available resources, especially with auto scaling.
- **Microservices:**
  Decomposing monoliths into containerized microservices
  reduces interdependencies and allows independent scaling.

## Key AWS services

- [Amazon Elastic Compute Cloud (EC2)](https://aws.amazon.com/ec2/ "https://aws.amazon.com/ec2/")
- [Amazon Elastic Kubernetes Service (EKS)](https://aws.amazon.com/eks/ "https://aws.amazon.com/eks/")
- [Amazon Elastic Container Service (ECS)](https://aws.amazon.com/ecs/ "https://aws.amazon.com/ecs/")

## Resources

- [Leveraging Amazon EKS managed node group with placement group for low latency critical applications](https://aws.amazon.com/blogs/containers/leveraging-amazon-eks-managed-node-group-with-placement-group-for-low-latency-critical-applications/ "https://aws.amazon.com/blogs/containers/leveraging-amazon-eks-managed-node-group-with-placement-group-for-low-latency-critical-applications/")
- [Amazon ECS vs Amazon EKS: making sense of AWS container services](https://aws.amazon.com/blogs/containers/amazon-ecs-vs-amazon-eks-making-sense-of-aws-container-services/ "https://aws.amazon.com/blogs/containers/amazon-ecs-vs-amazon-eks-making-sense-of-aws-container-services/")
- [Under
  the hood: Lazy Loading Container Images with Seekable OCI and AWS Fargate](https://aws.amazon.com/blogs/containers/under-the-hood-lazy-loading-container-images-with-seekable-oci-and-aws-fargate/ "https://aws.amazon.com/blogs/containers/under-the-hood-lazy-loading-container-images-with-seekable-oci-and-aws-fargate/")
- [Optimizing
  your Kubernetes compute costs with Karpenter consolidation](https://aws.amazon.com/blogs/containers/optimizing-your-kubernetes-compute-costs-with-karpenter-consolidation/ "https://aws.amazon.com/blogs/containers/optimizing-your-kubernetes-compute-costs-with-karpenter-consolidation/")
