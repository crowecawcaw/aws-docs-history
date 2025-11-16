**Help improve this page**

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Use application data storage for your cluster

You can use a range of AWS storage services with Amazon EKS for the storage needs of your applications. Through an AWS-supported breadth of Container Storage Interface (CSI) drivers, you can easily use Amazon EBS, Amazon S3, Amazon EFS, Amazon FSX, and Amazon File Cache for the storage needs of your applications running on Amazon EKS. To manage backups of your Amazon EKS cluster, see [AWS Backup support for Amazon EKS](../../../aws-backup/latest/devguide/working-with-supported-services.md#working-with-eks "../../../aws-backup/latest/devguide/working-with-supported-services.md#working-with-eks").

This chapter covers storage options for Amazon EKS clusters.

###### Topics

- [Use Kubernetes volume storage with Amazon EBS](ebs-csi.md "ebs-csi.md")
- [Use elastic file system storage with Amazon EFS](efs-csi.md "efs-csi.md")
- [Use high-performance app storage with Amazon FSx for Lustre](fsx-csi.md "fsx-csi.md")
- [Use high-performance app storage with FSx for NetApp ONTAP](fsx-ontap.md "fsx-ontap.md")
- [Use data storage with Amazon FSx for OpenZFS](fsx-openzfs-csi.md "fsx-openzfs-csi.md")
- [Minimize latency with Amazon File Cache](file-cache-csi.md "file-cache-csi.md")
- [Access Amazon S3 objects with Mountpoint for Amazon S3 CSI driver](s3-csi.md "s3-csi.md")
- [Enable snapshot functionality for CSI volumes](csi-snapshot-controller.md "csi-snapshot-controller.md")
