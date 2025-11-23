**Help improve this page**

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Manage `kube-proxy` in Amazon EKS clusters

###### Tip

With Amazon EKS Auto Mode, you don’t need to install or upgrade networking add-ons. Auto Mode includes pod networking and load balancing capabilities.

For more information, see [Automate cluster infrastructure with EKS Auto Mode](automode.md "automode.md").

We recommend adding the Amazon EKS type of the add-on to your cluster instead of using the self-managed type of the add-on. If you’re not familiar with the difference between the types, see [Amazon EKS add-ons](eks-add-ons.md "eks-add-ons.md"). For more information about adding an Amazon EKS add-on to your cluster, see [Create an Amazon EKS add-on](creating-an-add-on.md "creating-an-add-on.md"). If you’re unable to use the Amazon EKS add-on, we encourage you to submit an issue about why you can’t to the [Containers roadmap GitHub repository](https://github.com/aws/containers-roadmap/issues "https://github.com/aws/containers-roadmap/issues").

The `kube-proxy` add-on is deployed on each Amazon EC2 node in your Amazon EKS cluster. It maintains network rules on your nodes and enables network communication to your Pods. The add-on isn’t deployed to Fargate nodes in your cluster. For more information, see [kube-proxy](https://kubernetes.io/docs/reference/command-line-tools-reference/kube-proxy/ "https://kubernetes.io/docs/reference/command-line-tools-reference/kube-proxy/") in the Kubernetes documentation.

## Install as Amazon EKS Add-on

## `kube-proxy` versions

The following table lists the latest version of the Amazon EKS add-on type for each Kubernetes version.

| Kubernetes version | `kube-proxy` version |
| ------------------ | -------------------- |
| 1.34               | v1.34.1-eksbuild.2   |
| 1.33               | v1.33.5-eksbuild.2   |
| 1.32               | v1.32.9-eksbuild.2   |
| 1.31               | v1.31.13-eksbuild.2  |
| 1.30               | v1.30.14-eksbuild.8  |
| 1.29               | v1.29.15-eksbuild.16 |
| 1.28               | v1.28.15-eksbuild.31 |

###### Note

An earlier version of the documentation was incorrect. `kube-proxy` versions `v1.28.5`, `v1.27.9`, and `v1.26.12` aren’t available.

If you’re self-managing this add-on, the versions in the table might not be the same as the available self-managed versions.

## `kube-proxy` container image

The `kube-proxy` container image is based on a [minimal base image](https://gallery.ecr.aws/eks-distro-build-tooling/eks-distro-minimal-base-iptables "https://gallery.ecr.aws/eks-distro-build-tooling/eks-distro-minimal-base-iptables") maintained by Amazon EKS Distro, which contains minimal packages and doesn’t have shells. For more information, see [Amazon EKS Distro](https://distro.eks.amazonaws.com/ "https://distro.eks.amazonaws.com/").

The following table lists the latest available self-managed `kube-proxy` container image version for each Amazon EKS cluster version.

| Version | kube-proxy                   |
| ------- | ---------------------------- |
| 1.34    | v1.34.1-eksbuild.2           |
| 1.33    | v1.33.5-minimal-eksbuild.2   |
| 1.32    | v1.32.9-minimal-eksbuild.2   |
| 1.31    | v1.31.13-minimal-eksbuild.2  |
| 1.30    | v1.30.14-minimal-eksbuild.8  |
| 1.29    | v1.29.15-minimal-eksbuild.16 |
| 1.28    | v1.28.15-minimal-eksbuild.31 |

When you [update an Amazon EKS add-on type](updating-an-add-on.md "updating-an-add-on.md"), you specify a valid Amazon EKS add-on version, which might not be a version listed in this table. This is because [Amazon EKS add-on](workloads-add-ons-available-eks.md#add-ons-kube-proxy "workloads-add-ons-available-eks.md#add-ons-kube-proxy") versions don’t always match container image versions specified when updating the self-managed type of this add-on. When you update the self-managed type of this add-on, you specify a valid container image version listed in this table.
