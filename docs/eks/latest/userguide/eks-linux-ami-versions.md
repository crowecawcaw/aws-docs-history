**Help improve this page**

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Retrieve Amazon Linux AMI version information

Amazon EKS optimized Amazon Linux AMIs are versioned by Kubernetes version and the release date of the AMI in the following format:

```
 k8s_major_version.k8s_minor_version.k8s_patch_version-release_date
```

Each AMI release includes various versions of [kubelet](https://kubernetes.io/docs/reference/command-line-tools-reference/kubelet/ "https://kubernetes.io/docs/reference/command-line-tools-reference/kubelet/"), the Linux kernel, and [containerd](https://containerd.io/ "https://containerd.io/"). The accelerated AMIs also include various versions of the NVIDIA driver. You can find this version information in the [Changelog](https://github.com/awslabs/amazon-eks-ami/blob/main/CHANGELOG.md "https://github.com/awslabs/amazon-eks-ami/blob/main/CHANGELOG.md") on GitHub.
