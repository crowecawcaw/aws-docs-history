**Help improve this page**

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Create nodes with optimized Amazon Linux AMIs

The Amazon EKS-optimized Amazon Linux AMIs are built on top of Amazon Linux 2 (AL2) and Amazon Linux 2023 (AL2023). They are configured to serve as the base images for Amazon EKS nodes. The AMIs are configured to work with Amazon EKS and they include the following components:

- `kubelet`
- AWS IAM Authenticator
- `containerd`

###### Note

- You can track security or privacy events for Amazon Linux at the [Amazon Linux security center](https://alas.aws.amazon.com/ "https://alas.aws.amazon.com/") by choosing the tab for your desired version. You can also subscribe to the applicable RSS feed. Security and privacy events include an overview of the issue, what packages are affected, and how to update your instances to correct the issue.
- Before deploying an accelerated or Arm AMI, review the information in [Amazon EKS-optimized accelerated Amazon Linux AMIs](#gpu-ami "#gpu-ami") and [Amazon EKS-optimized Arm Amazon Linux AMIs](#arm-ami "#arm-ami").
- Amazon EC2 `P2` instances aren’t supported on Amazon EKS because they require `NVIDIA` driver version 470 or earlier.
- Any newly created managed node groups in clusters on version `1.30` or newer will automatically default to using AL2023 as the node operating system. Previously, new node groups would default to AL2. You can continue to use AL2 by choosing it as the AMI type when creating a new node group.
- Amazon EKS will no longer publish EKS-optimized Amazon Linux 2 (AL2) AMIs after November 26th, 2025. Additionally, Kubernetes version `1.32` is the last version for which Amazon EKS will release AL2 AMIs. From version `1.33` onwards, Amazon EKS will continue to release AL2023 and Bottlerocket based AMIs.

## Amazon EKS-optimized accelerated Amazon Linux AMIs

The Amazon EKS-optimized accelerated Amazon Linux AMIs are built on top of the standard Amazon EKS-optimized Amazon Linux AMIs. They are configured to serve as optional images for Amazon EKS nodes to support GPU, [Inferentia](https://aws.amazon.com/machine-learning/inferentia/ "https://aws.amazon.com/machine-learning/inferentia/"), and [Trainium](https://aws.amazon.com/machine-learning/trainium/ "https://aws.amazon.com/machine-learning/trainium/") based workloads.

For more information, see [Use EKS-optimized accelerated AMIs for GPU instances](ml-eks-optimized-ami.md "ml-eks-optimized-ami.md").

## Amazon EKS-optimized Arm Amazon Linux AMIs

Arm instances deliver significant cost savings for scale-out and Arm-based applications such as web servers, containerized microservices, caching fleets, and distributed data stores. When adding Arm nodes to your cluster, review the following considerations.

- If your cluster was deployed before August 17, 2020, you must do a one-time upgrade of critical cluster add-on manifests. This is so that Kubernetes can pull the correct image for each hardware architecture in use in your cluster. For more information about updating cluster add-ons, see [Step 1: Prepare for upgrade](update-cluster.md#update-existing-cluster "update-cluster.md#update-existing-cluster"). If you deployed your cluster on or after August 17, 2020, then your CoreDNS, `kube-proxy`, and Amazon VPC CNI plugin for Kubernetes add-ons are already multi-architecture capable.
- Applications deployed to Arm nodes must be compiled for Arm.
- If you have DaemonSets that are deployed in an existing cluster, or you want to deploy them to a new cluster that you also want to deploy Arm nodes in, then verify that your DaemonSet can run on all hardware architectures in your cluster.
- You can run Arm node groups and x86 node groups in the same cluster. If you do, consider deploying multi-architecture container images to a container repository such as Amazon Elastic Container Registry and then adding node selectors to your manifests so that Kubernetes knows what hardware architecture a Pod can be deployed to. For more information, see [Pushing a multi-architecture image](../../../AmazonECR/latest/userguide/docker-push-multi-architecture-image.md "../../../AmazonECR/latest/userguide/docker-push-multi-architecture-image.md") in the _Amazon ECR User Guide_ and the [Introducing multi-architecture container images for Amazon ECR](https://aws.amazon.com/blogs/containers/introducing-multi-architecture-container-images-for-amazon-ecr "https://aws.amazon.com/blogs/containers/introducing-multi-architecture-container-images-for-amazon-ecr") blog post.

## More information

For more information about using Amazon EKS-optimized Amazon Linux AMIs, see the following sections:

- To use Amazon Linux with managed node groups, see [Simplify node lifecycle with managed node groups](managed-node-groups.md "managed-node-groups.md").
- To launch self-managed Amazon Linux nodes, see [Retrieve recommended Amazon Linux AMI IDs](retrieve-ami-id.md "retrieve-ami-id.md").
- For version information, see [Retrieve Amazon Linux AMI version information](eks-linux-ami-versions.md "eks-linux-ami-versions.md").
- To retrieve the latest IDs of the Amazon EKS-optimized Amazon Linux AMIs, see [Retrieve recommended Amazon Linux AMI IDs](retrieve-ami-id.md "retrieve-ami-id.md").
- For open-source scripts that are used to build the Amazon EKS-optimized AMIs, see [Build a custom Amazon Linux AMI](eks-ami-build-scripts.md "eks-ami-build-scripts.md").
