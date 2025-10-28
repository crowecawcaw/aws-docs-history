**Help improve this page**

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Use data storage with Amazon FSx for OpenZFS

Amazon FSx for OpenZFS is a fully managed file storage service that makes it easy to move data to AWS from on-premises ZFS or other Linux-based file servers. You can do this without changing your application code or how you manage data. It offers highly reliable, scalable, efficient, and feature-rich file storage built on the open-source OpenZFS file system. It combines these capabilities with the agility, scalability, and simplicity of a fully managed AWS service. For more information, see the [Amazon FSx for OpenZFS User Guide](../../../fsx/latest/OpenZFSGuide/what-is-fsx.md "../../../fsx/latest/OpenZFSGuide/what-is-fsx.md").

The FSx for OpenZFS Container Storage Interface (CSI) driver provides a CSI interface that allows Amazon EKS clusters to manage the life cycle of FSx for OpenZFS volumes. Note that the Amazon FSx for OpenZFS CSI driver is not compatible with Amazon EKS Hybrid Nodes. To deploy the FSx for OpenZFS CSI driver to your Amazon EKS cluster, see [aws-fsx-openzfs-csi-driver](https://github.com/kubernetes-sigs/aws-fsx-openzfs-csi-driver "https://github.com/kubernetes-sigs/aws-fsx-openzfs-csi-driver") on GitHub.
