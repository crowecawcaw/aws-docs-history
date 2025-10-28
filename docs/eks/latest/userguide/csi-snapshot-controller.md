**Help improve this page**

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Enable snapshot functionality for CSI volumes

Snapshot functionality allows for point-in-time copies of your data. For this capability to work in Kubernetes, you need both a CSI driver with snapshot support (such as the Amazon EBS CSI driver) and a CSI snapshot controller. The snapshot controller is available either as an Amazon EKS managed add-on or as a self-managed installation.

Here are some things to consider when using the CSI snapshot controller.

- The snapshot controller must be installed alongside a CSI driver with snapshot functionality. For installation instructions of the Amazon EBS CSI driver, see [Use Kubernetes volume storage with Amazon EBS](ebs-csi.md "ebs-csi.md").
- Kubernetes doesn’t support snapshots of volumes being served via CSI migration, such as Amazon EBS volumes using a `StorageClass` with provisioner `kubernetes.io/aws-ebs`. Volumes must be created with a `StorageClass` that references the CSI driver provisioner, `ebs.csi.aws.com`.
- Amazon EKS Auto Mode does not include the snapshot controller. The storage capability of EKS Auto Mode is compatible with the snapshot controller.
  We recommend that you install the CSI snapshot controller through the Amazon EKS managed add-on. This add-on includes the custom resource definitions (CRDs) that are needed to create and manage snapshots on Amazon EKS. To add an Amazon EKS add-on to your cluster, see [Create an Amazon EKS add-on](creating-an-add-on.md "creating-an-add-on.md"). For more information about add-ons, see [Amazon EKS add-ons](eks-add-ons.md "eks-add-ons.md").

Alternatively, if you want a self-managed installation of the CSI snapshot controller, see [Usage](https://github.com/kubernetes-csi/external-snapshotter/blob/master/README.md#usage "https://github.com/kubernetes-csi/external-snapshotter/blob/master/README.md#usage") in the upstream Kubernetes `external-snapshotter` on GitHub.
