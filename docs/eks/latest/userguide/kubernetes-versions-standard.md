

 **Help improve this page** 

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Review release notes for Kubernetes versions on standard support
<a name="kubernetes-versions-standard"></a>

**Tip**  
 [Register](https://aws-experience.com/emea/smb/events/series/get-hands-on-with-amazon-eks?trk=4a9b4147-2490-4c63-bc9f-f8a84b122c8c&sc_channel=el) for upcoming Amazon EKS workshops.

This topic gives important changes to be aware of for each Kubernetes version in standard support. When upgrading, carefully review the changes that have occurred between the old and new versions for your cluster.

## Kubernetes 1.36
<a name="kubernetes-1-36"></a>

Kubernetes `1.36` is now available in Amazon EKS. For more information about Kubernetes `1.36`, see the [official release announcement](https://kubernetes.io/blog/2026/04/22/kubernetes-v1-36-release/).

**Important**  
gitRepo Volume Removal: The `gitRepo` volume type is permanently disabled in Kubernetes 1.36 and cannot be re-enabled. The Kubernetes API still accepts Pods with `gitRepo` volumes, but the kubelet will refuse to run them and return an error.  
Action required: Migrate to [init containers](https://kubernetes.io/docs/concepts/workloads/pods/init-containers/) or [git-sync](https://github.com/kubernetes/git-sync) sidecar containers before upgrading to 1.36. For more information, see [KEP-5040](https://github.com/kubernetes/enhancements/issues/5040).
SELinux Volume Labeling Changes (GA): Faster SELinux volume labeling now defaults to all volumes in Kubernetes 1.36, using `mount -o context` instead of recursive file relabeling. Sharing a volume between privileged and unprivileged Pods on the same node may cause issues. Future Kubernetes releases may introduce additional breaking changes related to this feature.  
Action required: Customers running SELinux-enforcing systems should audit clusters and ensure the `seLinuxChangePolicy` field and SELinux volume labels are correctly set on Pods before upgrading. For more information, see [SELinux Volume Label Changes goes GA (and likely implications in v1.37)](https://kubernetes.io/blog/2026/04/22/breaking-changes-in-selinux-volume-labeling/).
Strict IP/CIDR Validation Enabled by Default: The `StrictIPCIDRValidation` feature gate is now enabled by default for built-in API kinds. API fields no longer accept IP or CIDR values with extraneous leading zeros (e.g., `010.000.000.005` instead of `10.0.0.5`) or CIDR values with ambiguous semantics (e.g., `192.168.0.5/24` instead of `192.168.0.0/24`). Existing stored objects are preserved via validation ratcheting, but new creates and updates will be rejected. This does not apply to custom resource kinds.  
Action required: Review manifests, Helm charts, and automation for IP addresses containing leading zeros or non-canonical CIDR notation. Update them to use canonical formats before upgrading. For more information, see [KEP-4858](https://github.com/kubernetes/enhancements/issues/4858).
+  **User Namespaces (Stable):** User Namespaces provides defense-in-depth by mapping a container’s root user to a non-privileged user on the host, ensuring that a container breakout grants no administrative power over the node.
  + For more information, see [User Namespaces in Kubernetes are finally GA](https://kubernetes.io/blog/2026/04/23/kubernetes-v1-36-userns-ga/) on the *Kubernetes Blog*.
+  **Resource Health Status (Beta):** Reports per-device health in Pod status, allowing operators to determine whether a crash loop is due to an Unhealthy or Unknown device status rather than application issues. Works with both Device Plugins and Dynamic Resource Allocation.
  + For more information, see [KEP-4680](https://github.com/kubernetes/enhancements/issues/4680).
+  **Dynamic Resource Allocation Features (Beta):** Several DRA features are now enabled by default: Partitionable Devices and Consumable Capacity for more granular sharing of hardware like GPUs, and Device Binding Conditions for thorough device readiness checks before scheduling.
  + For more information, see [Kubernetes v1.36: More Drivers, New Features, and the Next Era of DRA](https://kubernetes.io/blog/2026/05/07/kubernetes-v1-36-dra-136-updates/) on the *Kubernetes Blog*.
+  **Deprecation Notice — Service externalIPs:** The `externalIPs` field in Service `.spec` is deprecated in Kubernetes 1.36. You will see deprecation warnings when creating or updating Services that use this field. Full removal is planned for Kubernetes 1.43. Customers who use `externalIPs` should migrate to LoadBalancer Services, NodePort, or [Gateway API](https://gateway-api.sigs.k8s.io/). For more information, see [KEP-5707](https://github.com/kubernetes/enhancements/issues/5707).

For the complete Kubernetes `1.36` changelog, see https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.36.md

## Kubernetes 1.35
<a name="kubernetes-1-35"></a>

Kubernetes `1.35` is now available in Amazon EKS. For more information about Kubernetes `1.35`, see the [official release announcement](https://kubernetes.io/blog/2025/12/17/kubernetes-v1-35-release/).

**Important**  
Cgroup v1 Support Removed: Kubernetes 1.35 deprecates cgroup v1 support, meaning the kubelet will refuse to start by default on nodes using cgroup v1.  
AL2023: AL2023 uses cgroup v2 by default and aligns with Kubernetes upstream behavior.  
Action required: Customers who manually configured AL2023 to use cgroup v1 must either [migrate to cgroups v2](https://kubernetes.io/docs/concepts/architecture/cgroups/) or manually set `failCgroupV1: false` in kubelet configuration.
Bottlerocket: Bottlerocket 1.35 uses cgroup v2 by default, however sets `failCgroupV1: false` in the kubelet configuration, maintaining backward compatibility.
Fargate: Fargate continues to use cgroup v1.
Containerd 1.x End of Support: Kubernetes 1.35 is the last release supporting containerd 1.x. You must switch to containerd 2.0 or later before upgrading to the next Kubernetes version.
In March 2026, the upstream Kubernetes project will retire Ingress NGINX, a critical infrastructure component for many Kubernetes environments.  
Action required: EKS customers should evaluate whether they rely on Ingress NGINX and begin planning migration to alternatives such as Gateway API or third-party Ingress controllers, as there will be no further releases for bug fixes, security patches, or updates after retirement. Existing deployments will continue to work, but remaining with Ingress NGINX after retirement leaves your environment vulnerable to security risks, as none of the available alternatives are direct drop-in replacements and will require planning and engineering time. For more information about this Kubernetes announcement, see the official statement from the Kubernetes Steering and Security Response Committees [Ingress NGINX retirement](https://kubernetes.io/blog/2026/01/29/ingress-nginx-statement/).
+  **In-Place Pod Resource Updates (Stable):** In-Place Pod Resource Updates allows users to adjust CPU and memory resources without restarting Pods or containers. Previously, such modifications required recreating Pods, which could disrupt workloads, particularly for stateful or batch applications. The new in-place functionality allows for smoother, non-disruptive vertical scaling, improves efficiency, and can also simplify development.
  + For more information, see [Kubernetes 1.35: In-Place Pod Resize Graduates to Stable](https://kubernetes.io/blog/2025/12/19/kubernetes-v1-35-in-place-pod-resize-ga/) on the *Kubernetes Blog*.
+  **PreferSameNode Traffic Distribution (Stable):** The `trafficDistribution` field for Services has been updated to provide more explicit control over traffic routing. A new option, `PreferSameNode`, has been introduced to allow services to strictly prioritize endpoints on the local node when available, falling back to remote endpoints otherwise. This change makes the API more explicit about preferring traffic within the current node.
+  **StatefulSet MaxUnavailable (Beta):** This feature enables parallel Pod updates by setting `maxUnavailable` (e.g., 3 or 10%), allowing stateful applications like database clusters to update up to 60% faster than sequential one-at-a-time updates, significantly reducing maintenance windows.
+  **Windows Server 2025 Support:** EKS 1.35 adds support for [Windows Server 2025](https://docs.aws.amazon.com/eks/latest/userguide/eks-optimized-windows-ami.html).
+  **Kubelet Flag Removal:** The `--pod-infra-container-image` flag has been removed from kubelet. Custom AMI users must remove this flag from kubelet configuration before upgrading to 1.35.
+  **Deprecation Notice - IPVS Mode:** IPVS mode in kube-proxy is deprecated and will be removed in Kubernetes 1.36.

For the complete Kubernetes `1.35` changelog, see https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md

## Kubernetes 1.34
<a name="kubernetes-1-34"></a>

Kubernetes `1.34` is now available in Amazon EKS. For more information about Kubernetes `1.34`, see the [official release announcement](https://kubernetes.io/blog/2025/08/27/kubernetes-v1-34-release/).

**Important**  
Containerd updated to 2.1 in Version 1.34 for launch.  
If you experience any issues after upgrade, check the [containerd 2.1 release notes](https://github.com/containerd/containerd/releases/tag/v2.1.0).
 AWS is not releasing an EKS-optimized Amazon Linux 2 AMI for Kubernetes 1.34.  
 AWS encourages you to migrate to Amazon Linux 2023. Learn how to [Upgrade from Amazon Linux 2 to Amazon Linux 2023](al2023.md).
For more information, see [Amazon Linux 2 AMI deprecation](kubernetes-versions-extended.md#al2-ami-deprecation).
AppArmor is deprecated in Kubernetes 1.34.  
We recommend migrating to alternative container security solutions like [seccomp](https://kubernetes.io/docs/tutorials/security/seccomp/) or [Pod Security Standards](https://kubernetes.io/docs/concepts/security/pod-security-standards/).
VolumeAttributesClass (VAC) graduates to GA in Kubernetes 1.34, migrating from the beta API (`storage.k8s.io/v1beta1`) to the stable API (`storage.k8s.io/v1`).  
If you use the EBS CSI driver with AWS-managed sidecar containers (from [CSI Components](https://gallery.ecr.aws/csi-components) on the ECR Gallery), volume modification will continue to work seamlessly on EKS 1.31-1.33 clusters. AWS will patch the sidecars to support beta VAC APIs until the end of EKS 1.33 standard support (July 29, 2026).
If you self-manage your CSI sidecar containers, you may need to pin to older sidecar versions on pre-1.34 clusters to maintain VAC functionality.
To use GA VolumeAttributesClass features (such as modification rollback), upgrade to EKS 1.34 or later.
External JWT Signer for Service Account Tokens is promoted to Beta. When using external signers, the --service-account-extend-token-expiration flag is no longer fully respected. The API server enforces the minimum expiration between the desired extension (1 year) and the external signer’s limit (24 hours).  
We recommend using [bound service account tokens](https://kubernetes.io/docs/reference/access-authn-authz/service-accounts-admin/#bound-service-account-tokens), which are automatically mounted and rotated by Kubernetes.
+  **Dynamic Resource Allocation (DRA) Core APIs (GA):** Dynamic Resource Allocation has graduated to stable, enabling efficient management of specialized hardware like GPUs through standardized allocation interfaces - simplifying resource management for hardware accelerators and improving utilization of specialized resources.
+  **Projected ServiceAccount Tokens for Kubelet (Beta):** This enhancement improves security by using short-lived credentials for container image pulls instead of long-lived secrets - reducing the risk of credential exposure and strengthening the overall security posture of your clusters.
+  **Pod-level Resource Requests and Limits (Beta):** This feature simplifies resource management by allowing shared resource pools for multi-container pods - enabling more efficient resource allocation and utilization for complex applications with multiple containers.
+  **Mutable CSI Node Allocatable Count (Beta):** The `MutableCSINodeAllocatableCount` feature gate is enabled by default in EKS 1.34, making the CSINode max attachable volume count attribute mutable and introducing a mechanism to update it dynamically based on user configuration at the CSI driver level. These updates can be triggered either by periodic intervals or by failure detection, enhancing the reliability of stateful pod scheduling by addressing mismatches between reported and actual attachment capacity on nodes.
  + For more information, see [Kubernetes v1.34: Mutable CSI Node Allocatable Count](https://kubernetes.io/blog/2025/09/11/kubernetes-v1-34-mutable-csi-node-allocatable-count/) on the *Kubernetes Blog*.
+  **Deprecation Notice - cgroup driver configuration:** Manual cgroup driver configuration is being deprecated in favor of automatic detection.
  +  **Customer impact:** If you currently set the `--cgroup-driver` flag manually in your kubelet configuration, you should prepare to remove this configuration.
  +  **Required action:** Plan to update node bootstrap scripts and custom AMI configurations to remove manual cgroup driver settings before the feature is removed in a future Kubernetes release.
  + For more information, see the [cgroup driver documentation](https://kubernetes.io/docs/tasks/administer-cluster/kubeadm/configure-cgroup-driver/).

For the complete Kubernetes `1.34` changelog, see https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md