

# Shared file storage with Amazon Elastic File System
<a name="storage-efs"></a>

With Amazon Elastic File System (Amazon EFS), you can mount a shared, elastic, POSIX-compliant file system across many pods at the same time. Amazon EFS is the ROSA option for ReadWriteMany (RWX) workloads, such as content management systems, shared application data, and machine learning training data that is read by many pods.

Unlike Amazon EBS, the Amazon EFS CSI driver is **not installed by default**. You must install the Amazon EFS CSI Driver Operator and create the required AWS Identity and Access Management (IAM) resources before you can use it.

## Characteristics
<a name="storage-efs-characteristics"></a>
+  **Storage type** – Shared file storage.
+  **Access modes** – ReadWriteMany (RWX), ReadWriteOnce (RWO), and ReadOnlyMany (ROX).
+  **Availability Zone scope** – Amazon EFS is a Regional file system that is reachable from multiple Availability Zones. An Amazon EFS file system is not affected by the failure of a single node or Availability Zone.
+  **Provisioning** – Supports both static and dynamic provisioning. Dynamic provisioning uses Amazon EFS access points.

## Enabling Amazon EFS
<a name="storage-efs-install"></a>

To use Amazon EFS on ROSA, you install the Amazon EFS CSI Driver Operator that is provided for Red Hat OpenShift. The Operator is available from OperatorHub in the OpenShift web console and is installed manually. After the Operator is installed, you create a storage class that references the Amazon EFS CSI driver.

**Use only the Red Hat OpenShift EFS CSI driver**  
Only the Red Hat OpenShift Amazon EFS CSI driver and Operator are supported on ROSA. The upstream community Amazon EFS CSI driver is not supported.

## Permissions and setup
<a name="storage-efs-permissions"></a>

Because ROSA uses AWS STS, you must create an IAM role and policy for the Amazon EFS CSI driver and associate it with the cluster’s OIDC provider so that the driver can call Amazon EFS APIs. This is an additional step compared to Amazon EBS, whose role is created automatically. For more information about the OIDC credential model, see [AWS STS and storage-driver permissions](storage-csi-concepts.md#storage-sts-permissions).

The IAM configuration steps are the same for ROSA with HCP and ROSA classic. In both architectures, worker nodes run in your AWS account and authenticate to AWS resources through the cluster’s OIDC issuer.

Setting up Amazon EFS also involves configuring the Amazon EFS file system policy, allowing NFS traffic in worker node security groups, and creating a storage class. For the detailed steps, see the Red Hat documentation for using the Amazon EFS CSI driver with ROSA.

## Access points and file ownership
<a name="storage-efs-access-points"></a>

When you use dynamic provisioning, the Amazon EFS CSI driver creates an Amazon EFS access point for each volume. Be aware of the following behavior:
+  Amazon EFS evaluates the user ID and group ID of the access point. It then replaces the file user and group IDs with those of the access point. As a result, ROSA cannot use `fsGroup` to control file group ownership on Amazon EFS volumes; the `fsGroup` setting is silently ignored.
+ Any pod that can access a mounted access point can access any file on that volume.

Take these characteristics into account when you design multi-tenant workloads on Amazon EFS.

## Encryption
<a name="storage-efs-encryption"></a>

 Amazon EFS supports encryption of data at rest using AWS KMS and encryption of data in transit using TLS.

### Encryption at rest
<a name="storage-efs-encryption-at-rest"></a>

 Amazon EFS at-rest encryption is configured on the file system itself, not through storage class parameters. The Amazon EFS CSI driver does not dynamically provision Amazon EFS file systems. You must pre-provision the file system in AWS with at-rest encryption enabled. You then reference the pre-provisioned file system in your PersistentVolume by setting the file system ID as the `volumeHandle`.

### Encryption in transit
<a name="storage-efs-encryption-in-transit"></a>

In-transit encryption is not enabled by default. To enable it, add `tls` to the `mountOptions` array in your PersistentVolume or StorageClass definition. When `tls` is set, the Amazon EFS CSI driver mounts the file system over TLS.

### Key management
<a name="storage-efs-key-management"></a>

Specify the AWS KMS key when you provision the Amazon EFS file system.