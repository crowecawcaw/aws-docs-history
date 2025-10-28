# Running MNP jobs

AWS Batch supports MNP jobs on Amazon Elastic Container Service and Amazon EKS using Amazon EC2. The following provides more
specifics about the instance and container parameters for the feature.

## Instance quotas for MNP on Amazon EKS

- Up to 1000 instances can be used for a single MNP job.
- Up to 5000 instances can join a single Amazon EKS cluster.
- Up to 5 compute environments can be clustered and attached to a job-queue.

For example, you can scale up to 5 clustered compute environments in a job queue and
1000 instances in each compute environment.

In addition to the instance parameters, it’s important to note that you can’t use
Fargate for MNP jobs through either service.

You can use only one instance type in each MNP job. You can change the instance type by
updating the compute environment, or when you define a new compute environment. You can also
specify the instance type, and provide vCPU and memory requirements when creating the
job definition.

## Container quotas for MNP on Amazon EKS

- A multi-node parallel job supports one pod per node.
- Up to 10 containers (or 10 init containers. For more information see [Init
  Containers](https://kubernetes.io/docs/concepts/workloads/pods/init-containers/ "https://kubernetes.io/docs/concepts/workloads/pods/init-containers/") in the _Kubernetes documentation_.) in each pod.
- Up to 5 node ranges in each MNP job.
- Up 10 distinct container images in each node range.

For example, you can run up to a maximum of 10,000 containers in a single MNP job that
contains 5 node ranges and a total of 50 unique images.

## Running MNP jobs in a private Amazon VPC and an

Amazon EKS cluster

MNP jobs can run on any Amazon EKS cluster whether it has public Internet or not. When using
an Amazon EKS cluster with only private network access be sure that AWS Batch can access the Amazon EKS
control plane and the managed Kubernetes API server. You can grant the necessary access through
Amazon Virtual Private Cloud endpoints. For more information, see [Configure an endpoint
service](../../../vpc/latest/privatelink/configure-endpoint-service.md "../../../vpc/latest/privatelink/configure-endpoint-service.md").

Amazon EKS cluster Pods can’t download an image from a public source since the private VPC
doesn’t have Internet access. Your Amazon EKS cluster must pull images from a container registry
that's within your Amazon VPC. You can create an [Amazon Elastic Container Registry (Amazon ECR)](../../../AmazonECR/latest/userguide/Registries.md "../../../AmazonECR/latest/userguide/Registries.md") in your Amazon VPC
and copy container images to it for your nodes access.

You can also create a pull through cache rule with Amazon ECR. Once a pull through cache rule
is created for an external public registry, you can simply pull an image from that external
public registry using your Amazon ECR private registry URI. Then Amazon ECR creates a repository and
caches the image. When a cached image is pulled using the Amazon ECR private registry URI, Amazon ECR
checks the remote registry to see if there is a new version of the image and will update
your private registry up to one time every 24 hours. For more information, see [Creating a pull
through cache rule in Amazon ECR](../../../AmazonECR/latest/userguide/pull-through-cache-creating-rule.md "../../../AmazonECR/latest/userguide/pull-through-cache-creating-rule.md").

## Error notification

If your MNP jobs are blocked, you can receive notifications through the AWS Management Console
and Amazon EventBridge. For example, if an MNP job is stuck at the head of the queue, you can be
notified about the issue along with information about what caused it so that you can take
prompt action to unblock your job queue. Optionally, you can auto-terminate the MNP job if
no action is taken within a distinct amount of time, which can be defined in the job queue
template. For more information, see [Job queue blocked
events](batch-job-queue-blocked-events.md "batch-job-queue-blocked-events.md")
