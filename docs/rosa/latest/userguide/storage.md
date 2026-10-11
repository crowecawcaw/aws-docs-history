

# Storage in ROSA
<a name="storage"></a>

 Red Hat OpenShift Service on AWS clusters store persistent data on AWS storage services through the Kubernetes persistent volume framework and the Container Storage Interface (CSI). This section describes the storage options that are available for your workloads, when to use each one, and how they behave on ROSA.

The following storage backends are available:
+  ** Amazon Elastic Block Store (Amazon EBS)** – block storage for single-node, read-write-once workloads. Your cluster includes the Amazon EBS CSI driver and uses Amazon EBS storage by default. For more information, see [Block storage with Amazon Elastic Block Store](storage-ebs.md).
+  ** Amazon Elastic File System (Amazon EFS)** – shared, elastic file storage for read-write-many workloads across multiple pods and Availability Zones. You install and configure the Amazon EFS CSI driver before use. For more information, see [Shared file storage with Amazon Elastic File System](storage-efs.md).
+  **Amazon FSx for NetApp ONTAP (FSx for ONTAP)** – high-performance, multi-protocol shared file and block storage, provisioned through the NetApp Trident CSI driver. NetApp provides and supports Trident. You install and configure it. For more information, see [Multi-protocol storage with Amazon FSx for NetApp ONTAP](storage-fsx-ontap.md).

Before you choose a storage backend, review [How storage works in ROSA](storage-csi-concepts.md) to understand how ROSA provisions storage and how AWS STS affects the permissions that each storage driver requires.

**Topics**
+ [How storage works](storage-csi-concepts.md)
+ [Amazon EBS](storage-ebs.md)
+ [Amazon EFS](storage-efs.md)
+ [FSx for ONTAP](storage-fsx-ontap.md)