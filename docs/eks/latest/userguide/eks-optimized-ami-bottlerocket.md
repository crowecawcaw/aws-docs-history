**Help improve this page**

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Create nodes with optimized Bottlerocket AMIs

[Bottlerocket](https://aws.amazon.com/bottlerocket/ "https://aws.amazon.com/bottlerocket/") is an open source Linux distribution that’s sponsored and supported by AWS. Bottlerocket is purpose-built for hosting container workloads. With Bottlerocket, you can improve the availability of containerized deployments and reduce operational costs by automating updates to your container infrastructure. Bottlerocket includes only the essential software to run containers, which improves resource usage, reduces security threats, and lowers management overhead. The Bottlerocket AMI includes `containerd`, `kubelet`, and AWS IAM Authenticator. In addition to managed node groups and self-managed nodes, Bottlerocket is also supported by [Karpenter](https://karpenter.sh/ "https://karpenter.sh/").

## Advantages

Using Bottlerocket with your Amazon EKS cluster has the following advantages:

- **Higher uptime with lower operational cost and lower management complexity** – Bottlerocket has a smaller resource footprint, shorter boot times, and is less vulnerable to security threats than other Linux distributions. Bottlerocket’s smaller footprint helps to reduce costs by using less storage, compute, and networking resources.
- **Improved security from automatic OS updates** – Updates to Bottlerocket are applied as a single unit which can be rolled back, if necessary. This removes the risk of corrupted or failed updates that can leave the system in an unusable state. With Bottlerocket, security updates can be automatically applied as soon as they’re available in a minimally disruptive manner and be rolled back if failures occur.
- **Premium support** – AWS provided builds of Bottlerocket on Amazon EC2 is covered under the same AWS Support plans that also cover AWS services such as Amazon EC2, Amazon EKS, and Amazon ECR.

## Considerations

Consider the following when using Bottlerocket for your AMI type:

- Bottlerocket supports Amazon EC2 instances with `x86_64` and `arm64` processors.
- Bottlerocket supports Amazon EC2 instances with GPUs. For more information, see [Use EKS-optimized accelerated AMIs for GPU instances](ml-eks-optimized-ami.md "ml-eks-optimized-ami.md").
- Bottlerocket images don’t include an SSH server or a shell. You can employ out-of-band access methods to allow SSH. These approaches enable the admin container and to pass some bootstrapping configuration steps with user data. For more information, refer to the following sections in [Bottlerocket OS](https://github.com/bottlerocket-os/bottlerocket/blob/develop/README.md "https://github.com/bottlerocket-os/bottlerocket/blob/develop/README.md") on GitHub:
  - [Exploration](https://github.com/bottlerocket-os/bottlerocket/blob/develop/README.md#exploration "https://github.com/bottlerocket-os/bottlerocket/blob/develop/README.md#exploration")
  - [Admin container](https://github.com/bottlerocket-os/bottlerocket/blob/develop/README.md#admin-container "https://github.com/bottlerocket-os/bottlerocket/blob/develop/README.md#admin-container")
  - [Kubernetes settings](https://github.com/bottlerocket-os/bottlerocket/blob/develop/README.md#kubernetes-settings "https://github.com/bottlerocket-os/bottlerocket/blob/develop/README.md#kubernetes-settings")

- Bottlerocket uses different container types:
  - By default, a [control container](https://github.com/bottlerocket-os/bottlerocket-control-container "https://github.com/bottlerocket-os/bottlerocket-control-container") is enabled. This container runs the [AWS Systems Manager agent](https://github.com/aws/amazon-ssm-agent "https://github.com/aws/amazon-ssm-agent") that you can use to run commands or start shell sessions on Amazon EC2 Bottlerocket instances. For more information, see [Setting up Session Manager](../../../systems-manager/latest/userguide/session-manager-getting-started.md "../../../systems-manager/latest/userguide/session-manager-getting-started.md") in the _AWS Systems Manager User Guide_.
  - If an SSH key is given when creating the node group, an admin container is enabled. We recommend using the admin container only for development and testing scenarios. We don’t recommend using it for production environments. For more information, see [Admin container](https://github.com/bottlerocket-os/bottlerocket/blob/develop/README.md#admin-container "https://github.com/bottlerocket-os/bottlerocket/blob/develop/README.md#admin-container") on GitHub.

## More information

For more information about using Amazon EKS optimized Bottlerocket AMIs, see the following sections:

- For details about Bottlerocket, see the [Bottlerocket Documentation](https://bottlerocket.dev/en/ "https://bottlerocket.dev/en/").
- For version information resources, see [Retrieve Bottlerocket AMI version information](eks-ami-versions-bottlerocket.md "eks-ami-versions-bottlerocket.md").
- To use Bottlerocket with managed node groups, see [Simplify node lifecycle with managed node groups](managed-node-groups.md "managed-node-groups.md").
- To launch self-managed Bottlerocket nodes, see [Create self-managed Bottlerocket nodes](launch-node-bottlerocket.md "launch-node-bottlerocket.md").
- To retrieve the latest IDs of the Amazon EKS optimized Bottlerocket AMIs, see [Retrieve recommended Bottlerocket AMI IDs](retrieve-ami-id-bottlerocket.md "retrieve-ami-id-bottlerocket.md").
- For details on compliance support, see [Meet compliance requirements with Bottlerocket](bottlerocket-compliance-support.md "bottlerocket-compliance-support.md").
