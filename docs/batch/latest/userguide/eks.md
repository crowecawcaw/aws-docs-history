

# Amazon EKS compute environments
<a name="eks"></a>

[Getting started with AWS Batch on Amazon EKS](getting-started-eks.md) provides a short guide to creating EKS compute environments. This section provides more details on Amazon EKS compute environments.

![Architecture diagram showing AWS Batch submitting jobs to Amazon ECS and Amazon EKS clusters.](http://docs.aws.amazon.com/batch/latest/userguide/images/batch-on-eks.png)


AWS Batch simplifies your batch workloads on Amazon EKS clusters by providing managed batch capabilities. This includes queuing, dependency tracking, managed job retries and priorities, pod management, and node scaling. AWS Batch can handle multiple Availability Zones and multiple Amazon EC2 instance types and sizes. AWS Batch integrates several of the Amazon EC2 Spot best practices to run your workloads in a fault-tolerant manner, allowing for fewer interruptions. You can use AWS Batch to run a handful of overnight jobs or millions of mission-critical jobs with confidence.

![AWS Batch architecture showing job submission, EKS cluster with managed node groups, and EC2 Spot instances.](http://docs.aws.amazon.com/batch/latest/userguide/images/batch-on-eks-detail.png)


AWS Batch is a managed service that orchestrates batch workloads in your Kubernetes clusters that are managed by Amazon Elastic Kubernetes Service (Amazon EKS). AWS Batch conducts this orchestration external to your clusters using an "overlay" model. Since AWS Batch is a managed service, there are no Kubernetes components (for example, Operators or Custom Resources) to install or manage in your cluster. AWS Batch only needs your cluster to be configured with Role-Based Access Controls (RBAC) that allow AWS Batch to communicate with the Kubernetes API server. AWS Batch calls Kubernetes APIs to create, monitor, and delete Kubernetes pods and nodes.

AWS Batch has built-in scaling logic to scale Kubernetes nodes based on job queue load with optimizations in terms of job capacity allocations. When the job queue is empty, AWS Batch scales down the nodes to the minimum capacity that you set, which by default is zero. AWS Batch manages the full lifecycle of these nodes, and decorates the nodes with labels and taints. This way, other Kubernetes workloads aren't placed on the nodes managed by AWS Batch. The exception to this are `DaemonSets`, which can target AWS Batch nodes to provide monitoring and other functionality required for proper execution of the jobs. Additionally, AWS Batch doesn't run jobs, specifically pods, on nodes in your cluster that it doesn't manage. This way, you can use separate scaling logic and services for other applications on the cluster.

To submit jobs to AWS Batch, you interact directly with the AWS Batch API. AWS Batch translates jobs into `podspecs` and then creates the requests to place pods on nodes managed by AWS Batch in your Amazon EKS cluster. You can use tools such as `kubectl` to view running pods and nodes. When a pod has completed its execution, AWS Batch deletes the pod it created to maintain a lower load on the Kubernetes system.

You can get started by connecting a valid Amazon EKS cluster with AWS Batch. Then attach an AWS Batch job queue to it, and register an Amazon EKS job definition using `podspec` equivalent attributes. Last, submit jobs using the [SubmitJob](https://docs.aws.amazon.com/batch/latest/APIReference/API_SubmitJob.html) API operation referencing to the job definition. For more information, see [Getting started with AWS Batch on Amazon EKS](getting-started-eks.md).

AWS Batch on Amazon EKS supports Amazon EC2 instances (On-Demand and Spot) as compute resources. To use Fargate with AWS Batch, use an Amazon ECS compute environment instead. For more information, see [Fargate compute environments](fargate.md).

## Amazon EKS
<a name="compute-environments-eks"></a>

**Topics**
+ [Amazon EKS](#compute-environments-eks)
+ [Amazon EKS default AMI](eks-ce-ami-selection.md)
+ [Mixed AMI environments](mixed-ami-environments.md)
+ [Supported Kubernetes versions](supported_kubernetes_version.md)
+ [Update the Kubernetes version of the compute environment](updating-k8s-version-ce.md)
+ [Shared responsibility of the Kubernetes nodes](eks-ce-shared-responsibility.md)
+ [Run a DaemonSet on AWS Batch managed nodes](daemonset-on-batch-eks-nodes.md)
+ [Customize Amazon EKS launch templates](eks-launch-templates.md)
+ [How to upgrade from EKS AL2 to EKS AL2023](eks-migration-2023.md)