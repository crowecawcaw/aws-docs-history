

 **Help improve this page** 

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Review release notes for Kubernetes versions on extended support
<a name="kubernetes-versions-extended"></a>

Amazon EKS supports Kubernetes versions longer than they are supported upstream, with standard support for Kubernetes minor versions for 14 months from the time they are released in Amazon EKS, and extended support for Kubernetes minor versions for an additional 12 months of support (26 total months per version).

This topic gives important changes to be aware of for each Kubernetes version in extended support. When upgrading, carefully review the changes that have occurred between the old and new versions for your cluster.

**Note**  
If you roll back from a version under standard support to a version under extended support, extended support charges resume for that cluster.

## Kubernetes 1.33
<a name="kubernetes-1-33"></a>

Kubernetes `1.33` is now available in Amazon EKS. For more information about Kubernetes `1.33`, see the [official release announcement](https://kubernetes.io/blog/2025/04/23/kubernetes-v1-33-release/).

**Important**  
The Dynamic Resource Allocation *beta* Kubernetes API is enabled.  
This beta API improves the experience of scheduling and monitoring workloads that require resources such as GPUs.
The beta API is defined by the Kubernetes community, and might change in future versions of Kubernetes.
Carefully review [Feature stages](https://kubernetes.io/docs/reference/command-line-tools-reference/feature-gates/#feature-stages) in the Kubernetes documentation to understand the implications of using beta APIs.
 AWS is not releasing an EKS-optimized Amazon Linux 2 AMI for Kubernetes 1.33.  
 AWS encourages you to migrate to Amazon Linux 2023. Learn how to [Upgrade from Amazon Linux 2 to Amazon Linux 2023](al2023.md).
For more information, see [Amazon Linux 2 AMI deprecation](#al2-ami-deprecation).
+  **In-Place Pod Resource Resize (Beta):** Kubernetes 1.33 promotes in-place resource resize to beta. This allows dynamic updates to CPU and memory resources for existing Pods without restarts, enabling vertical scaling of stateful workloads with zero downtime.
+  **Sidecar Containers Now Stable:** Sidecar containers have graduated to stable. They are implemented as special init containers with `restartPolicy: Always` that start before application containers, run throughout the Pod lifecycle, and support probes for operational state signaling.
  + For more information, see [Sidecar Containers](https://kubernetes.io/docs/concepts/workloads/pods/sidecar-containers/) in the *Kubernetes Documentation*.
+  **Endpoints API Deprecation:** The Endpoints API is now officially deprecated and will return warnings when accessed—migrate workloads and scripts to use the EndpointSlices API instead, which supports modern features like dual-stack networking and handles multiple EndpointSlices per Service.
  + For more information, see [Kubernetes v1.33: Continuing the transition from Endpoints to EndpointSlice](https://kubernetes.io/blog/2025/04/24/endpoints-deprecation/) on the *Kubernetes Blog*.
+  **Elastic Fabric Adapter Support:** The default security group for Amazon EKS clusters now supports Elastic Fabric Adapter (EFA) traffic. The default security group has a new outbound rule that allows EFA traffic with the destination of the same security group. This allows EFA traffic within the cluster.
  + For more information, see [Elastic Fabric Adapter for AI/ML and HPC workloads on Amazon EC2](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/efa.html) in the Amazon Elastic Compute Cloud User Guide.

For the complete Kubernetes `1.33` changelog, see https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md

## Kubernetes 1.32
<a name="kubernetes-1-32"></a>

Kubernetes `1.32` is now available in Amazon EKS. For more information about Kubernetes `1.32`, see the [official release announcement](https://kubernetes.io/blog/2024/12/11/kubernetes-v1-32-release/).

**Important**  
The `flowcontrol.apiserver.k8s.io/v1beta3` API version of FlowSchema and PriorityLevelConfiguration has been removed in version `1.32`. If you are using these APIs, you must update your configurations to use the latest supported version before upgrading.
ServiceAccount `metadata.annotations[kubernetes.io/enforce-mountable-secrets]` has been deprecated in version `1.32` and will be removed in a future Kubernetes minor version release. It is recommended to use separate namespaces to isolate access to mounted secrets.
Kubernetes version `1.32` is the last version for which Amazon EKS will release Amazon Linux 2 (AL2) AMIs. From version `1.33` onwards, Amazon EKS will continue to release Amazon Linux 2023 (AL2023) and Bottlerocket based AMIs.
+ The Memory Manager feature has graduated to Generally Available (GA) status in Kubernetes version `1.32`. This enhancement provides more efficient and predictable memory allocation for containerized applications, particularly beneficial for workloads with specific memory requirements.
+ PersistentVolumeClaims (PVCs) created by StatefulSets now include automatic cleanup functionality. When PVCs are no longer needed, they will be automatically deleted while maintaining data persistence during StatefulSet updates and node maintenance operations. This feature simplifies storage management and helps prevent orphaned PVCs in your cluster.
+ Custom Resource Field Selector functionality has been introduced, allowing developers to add field selectors to custom resources. This feature provides the same filtering capabilities available for built-in Kubernetes objects to custom resources, enabling more precise and efficient resource filtering and promoting better API design practices.

For the complete Kubernetes `1.32` changelog, see https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md

### Anonymous authentication changes
<a name="_anonymous_authentication_changes"></a>

Starting with Amazon EKS `1.32`, anonymous authentication is restricted to the following API server health check endpoints:
+  `/healthz` 
+  `/livez` 
+  `/readyz` 

Requests to any other endpoint using the `system:unauthenticated` user will receive a `401 Unauthorized` HTTP response. This security enhancement helps prevent unintended cluster access that could occur due to misconfigured RBAC policies.

**Note**  
The `public-info-viewer` RBAC role continues to apply for the health check endpoints listed above.

### Amazon Linux 2 AMI deprecation
<a name="al2-ami-deprecation"></a>

Kubernetes version `1.32` is the last version for which Amazon EKS released AL2 AMIs. From version `1.33` onwards, Amazon EKS will continue to release AL2023 and Bottlerocket based AMIs. For more information, see [Guide to EKS AL2 & AL2-Accelerated AMIs transition features](eks-ami-deprecation-faqs.md).

## Kubernetes 1.31
<a name="kubernetes-1-31"></a>

Kubernetes `1.31` is now available in Amazon EKS. For more information about Kubernetes `1.31`, see the [official release announcement](https://kubernetes.io/blog/2024/08/13/kubernetes-v1-31-release/).

**Important**  
The kubelet flag `--keep-terminated-pod-volumes` deprecated since 2017 has been removed as part of the version `1.31` release. This change impacts how terminated pod volumes are handled by the kubelet. If you are using this flag in your node configurations, you must update your bootstrap scripts and launch templates to remove it before upgrading.
+ The beta `VolumeAttributesClass` feature gate and API resource is enabled in Amazon EKS version `1.31`. This feature allows cluster operators to modify mutable properties of Persistent Volumes (PVs) managed by compatible CSI Drivers, including the Amazon EBS CSI Driver. To leverage this feature, ensure that your CSI Driver supports the `VolumeAttributesClass` feature (for the Amazon EBS CSI Driver, upgrade to version `1.35.0` or later to automatically enable the feature). You will be able to create `VolumeAttributesClass` objects to define the desired volume attributes, such as volume type and throughput, and associate them with your Persistent Volume Claims (PVCs). See the [official Kubernetes documentation](https://kubernetes.io/docs/concepts/storage/volume-attributes-classes/) as well as the documentation of your CSI driver for more information.
  + For more information about the Amazon EBS CSI Driver, see [Use Kubernetes volume storage with Amazon EBS](ebs-csi.md).
+ Kubernetes support for [AppArmor](https://apparmor.net/) has graduated to stable and is now generally available for public use. This feature allows you to protect your containers with AppArmor by setting the `appArmorProfile.type` field in the container’s `securityContext`. Prior to Kubernetes version `1.30`, AppArmor was controlled by annotations. Starting with version `1.30`, it is controlled using fields. To leverage this feature, we recommend migrating away from annotations and using the `appArmorProfile.type` field to ensure that your workloads are compatible.
+ The PersistentVolume last phase transition time feature has graduated to stable and is now generally available for public use in Kubernetes version `1.31`. This feature introduces a new field, `.status.lastTransitionTime`, in the PersistentVolumeStatus, which provides a timestamp of when a PersistentVolume last transitioned to a different phase. This enhancement allows for better tracking and management of PersistentVolumes, particularly in scenarios where understanding the lifecycle of volumes is important.

For the complete Kubernetes `1.31` changelog, see https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md