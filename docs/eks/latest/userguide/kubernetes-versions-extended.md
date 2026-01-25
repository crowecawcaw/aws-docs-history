**Help improve this page**

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Review release notes for Kubernetes versions on extended support

Amazon EKS supports Kubernetes versions longer than they are supported upstream, with standard support for Kubernetes minor versions for 14 months from the time they are released in Amazon EKS, and extended support for Kubernetes minor versions for an additional 12 months of support (26 total months per version).

This topic gives important changes to be aware of for each Kubernetes version in extended support. When upgrading, carefully review the changes that have occurred between the old and new versions for your cluster.

## Kubernetes 1.31

Kubernetes `1.31` is now available in Amazon EKS. For more information about Kubernetes `1.31`, see the [official release announcement](https://kubernetes.io/blog/2024/08/13/kubernetes-v1-31-release/ "https://kubernetes.io/blog/2024/08/13/kubernetes-v1-31-release/").

###### Important

- The kubelet flag `--keep-terminated-pod-volumes` deprecated since 2017 has been removed as part of the version `1.31` release. This change impacts how terminated pod volumes are handled by the kubelet. If you are using this flag in your node configurations, you must update your bootstrap scripts and launch templates to remove it before upgrading.

- The beta `VolumeAttributesClass` feature gate and API resource is enabled in Amazon EKS version `1.31`. This feature allows cluster operators to modify mutable properties of Persistent Volumes (PVs) managed by compatible CSI Drivers, including the Amazon EBS CSI Driver. To leverage this feature, ensure that your CSI Driver supports the `VolumeAttributesClass` feature (for the Amazon EBS CSI Driver, upgrade to version `1.35.0` or later to automatically enable the feature). You will be able to create `VolumeAttributesClass` objects to define the desired volume attributes, such as volume type and throughput, and associate them with your Persistent Volume Claims (PVCs). See the [official Kubernetes documentation](https://kubernetes.io/docs/concepts/storage/volume-attributes-classes/ "https://kubernetes.io/docs/concepts/storage/volume-attributes-classes/") as well as the documentation of your CSI driver for more information.
  - For more information about the Amazon EBS CSI Driver, see [Use Kubernetes volume storage with Amazon EBS](ebs-csi.md "ebs-csi.md").

- Kubernetes support for [AppArmor](https://apparmor.net/ "https://apparmor.net/") has graduated to stable and is now generally available for public use. This feature allows you to protect your containers with AppArmor by setting the `appArmorProfile.type` field in the container’s `securityContext`. Prior to Kubernetes version `1.30`, AppArmor was controlled by annotations. Starting with version `1.30`, it is controlled using fields. To leverage this feature, we recommend migrating away from annotations and using the `appArmorProfile.type` field to ensure that your workloads are compatible.
- The PersistentVolume last phase transition time feature has graduated to stable and is now generally available for public use in Kubernetes version `1.31`. This feature introduces a new field, `.status.lastTransitionTime`, in the PersistentVolumeStatus, which provides a timestamp of when a PersistentVolume last transitioned to a different phase. This enhancement allows for better tracking and management of PersistentVolumes, particularly in scenarios where understanding the lifecycle of volumes is important.

For the complete Kubernetes `1.31` changelog, see https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md

## Kubernetes 1.30

Kubernetes `1.30` is now available in Amazon EKS. For more information about Kubernetes `1.30`, see the [official release announcement](https://kubernetes.io/blog/2024/04/17/kubernetes-v1-30-release/ "https://kubernetes.io/blog/2024/04/17/kubernetes-v1-30-release/").

- Starting with Amazon EKS version `1.30` or newer, any newly created managed node groups will automatically default to using Amazon Linux 2023 (AL2023) as the node operating system. For more information about specifiying the operating system for a managed node group, see [Create a managed node group for your cluster](create-managed-node-group.md "create-managed-node-group.md").
- With Amazon EKS `1.30`, the `topology.k8s.aws/zone-id` label is added to worker nodes. You can use Availability Zone IDs (AZ IDs) to determine the location of resources in one account relative to the resources in another account. For more information, see [Availability Zone IDs for your AWS resources](../../../ram/latest/userguide/working-with-az-ids.md "../../../ram/latest/userguide/working-with-az-ids.md") in the _AWS RAM User Guide_.
- Starting with `1.30`, Amazon EKS no longer includes the `default` annotation on the `gp2 StorageClass` resource applied to newly created clusters. This has no impact if you are referencing this storage class by name. You must take action if you were relying on having a default `StorageClass` in the cluster. You should reference the `StorageClass` by the name `gp2`. Alternatively, you can deploy the Amazon EBS recommended default storage class by setting the `defaultStorageClass.enabled` parameter to true when installing version `1.31.0` or later of the `aws-ebs-csi-driver add-on`.
- The minimum required IAM policy for the Amazon EKS cluster IAM role has changed. The action `ec2:DescribeAvailabilityZones` is required. For more information, see [Amazon EKS cluster IAM role](cluster-iam-role.md "cluster-iam-role.md").

For the complete Kubernetes `1.30` changelog, see https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.30.md.

## Kubernetes 1.29

Kubernetes `1.29` is now available in Amazon EKS. For more information about Kubernetes `1.29`, see the [official release announcement](https://kubernetes.io/blog/2023/12/13/kubernetes-v1-29-release/ "https://kubernetes.io/blog/2023/12/13/kubernetes-v1-29-release/").

###### Important

- The deprecated `flowcontrol.apiserver.k8s.io/v1beta2` API version of `FlowSchema` and `PriorityLevelConfiguration` are no longer served in Kubernetes version `1.29`. If you have manifests or client software that uses the deprecated beta API group, you should change these before you upgrade to version `1.29`.

- The `.status.kubeProxyVersion` field for node objects is now deprecated, and the Kubernetes project is proposing to remove that field in a future release. The deprecated field is not accurate and has historically been managed by `kubelet` - which does not actually know the `kube-proxy` version, or even whether `kube-proxy` is running. If you’ve been using this field in client software, stop - the information isn’t reliable and the field is now deprecated.
- In Kubernetes `1.29` to reduce potential attack surface, the `LegacyServiceAccountTokenCleanUp` feature labels legacy auto-generated secret-based tokens as invalid if they have not been used for a long time (1 year by default), and automatically removes them if use is not attempted for a long time after being marked as invalid (1 additional year by default). To identify such tokens, a you can run:

```
kubectl get cm kube-apiserver-legacy-service-account-token-tracking -n kube-system
```

For the complete Kubernetes `1.29` changelog, see https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md#changelog-since-v1280.
