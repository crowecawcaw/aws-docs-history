

# How storage works in ROSA
<a name="storage-csi-concepts"></a>

With ROSA, you can use the Kubernetes persistent volume framework to give your applications durable storage that outlives individual pods. Storage is consumed through the Container Storage Interface (CSI), a standard that lets ROSA use AWS storage services without building support for each service into the platform.

## Persistent volumes, claims, and storage classes
<a name="storage-csi-objects"></a>

 ROSA applications work with three Kubernetes storage objects:

 **PersistentVolume (PV)**   
A piece of storage in the cluster that is backed by an AWS storage resource, such as an Amazon EBS volume or an Amazon EFS file system. A PV has a lifecycle that is independent of any pod that uses it.

 **PersistentVolumeClaim (PVC)**   
A request for storage made by a workload. A PVC specifies the amount of storage and the access mode that the workload needs. ROSA binds the PVC to a PV that satisfies the request.

 **StorageClass (SC)**   
A template that describes a class of storage, including which CSI driver provisions it and the parameters to use (for example, the Amazon EBS volume type). Storage classes enable *dynamic provisioning*.

You can provision persistent volumes in two ways:
+  **Dynamic provisioning** – When a PVC references a storage class, ROSA automatically provisions a matching PV on demand. This is the most common approach.
+  **Static provisioning** – A cluster administrator creates PVs in advance, and PVCs bind to a matching existing PV.

A PVC binds to a PV only when both the requested capacity and the access mode match. A bound PV serves a single PVC at a time. When you delete a PVC, the reclaim policy of the PV determines what happens to the underlying storage. By default, ROSA deletes dynamically provisioned volumes.

## Access modes
<a name="storage-access-modes"></a>

The access mode of a volume determines how many nodes can mount it and whether they can write to it. The following table shows the access modes and which storage backends support each one.


| Access mode | Description | Supported backends | 
| --- | --- | --- | 
| ReadWriteOnce (RWO) | The volume can be mounted as read-write by a single node. |  Amazon EBS, Amazon EFS, Amazon FSx for NetApp ONTAP | 
| ReadWriteMany (RWX) | The volume can be mounted as read-write by many nodes at the same time. |  Amazon EFS, FSx for ONTAP | 
| ReadOnlyMany (ROX) | The volume can be mounted as read-only by many nodes. |  Amazon EFS  | 

**EBS does not support ReadWriteMany**  
 Amazon EBS volumes cannot be shared for simultaneous writes by multiple nodes. If your workload requires ReadWriteMany (RWX) access, use Amazon EFS or FSx for ONTAP instead.

## Storage drivers installed by default
<a name="storage-default-drivers"></a>

 ROSA installs some CSI drivers for you and requires you to enable others. The following table shows which CSI drivers are installed by default.


| Storage backend | Installed by default | Notes | 
| --- | --- | --- | 
|  Amazon EBS (EBS CSI driver) | Yes | Your cluster includes the Amazon EBS CSI driver and Operator in the `openshift-cluster-csi-drivers` namespace, and uses Amazon EBS to provision persistent volumes by default. | 
|  Amazon EFS (EFS CSI driver) | No | You install the Amazon EFS CSI Driver Operator and create the required AWS Identity and Access Management (IAM) resources before use. | 
| FSx for ONTAP (NetApp Trident) | No | Trident is a NetApp-provided CSI driver that you install and operate. It is not an AWS or Red Hat add-on. | 

Your cluster is built with a prepared Amazon EBS storage class, and uses Amazon EBS by default for both node root volumes and persistent volumes. Under the shared responsibility model, you install and configure any additional storage. To use Amazon EFS or a third-party CSI driver, you install that driver and create its IAM resources.

## AWS STS and storage-driver permissions
<a name="storage-sts-permissions"></a>

 ROSA clusters use AWS Security Token Service (AWS STS). Instead of long-lived credentials, cluster components assume IAM roles through an OpenID Connect (OIDC) identity provider to obtain short-lived credentials. This affects how each storage driver is granted access to AWS APIs:
+ The ** Amazon EBS CSI Driver Operator** receives its permissions from the AWS managed policy `ROSAAmazonEBSCSIDriverOperatorPolicy`, and its IAM role is created automatically when you create the cluster. The Amazon EBS CSI driver is installed by default, and its role is part of the standard ROSA operator roles. As a result, Amazon EBS storage works without any additional IAM setup.
+ The ** Amazon EFS CSI driver** and **NetApp Trident** require you to create an additional IAM role and policy and associate it with the cluster’s OIDC provider before the driver can call AWS APIs.

**IAM policy differences between ROSA HCP and ROSA Classic**  
The IAM model differs between ROSA with HCP and ROSA classic. ROSA with HCP uses AWS managed IAM policies, and ROSA classic uses policies that the service defines and manages. For a comparison of the two architectures, see [Comparing ROSA with HCP and ROSA classic](rosa-architecture-models.md#rosa-architecture-differences).

For more information about encryption of persistent volumes and cluster data, see [Data protection in ROSA](data-protection.md).