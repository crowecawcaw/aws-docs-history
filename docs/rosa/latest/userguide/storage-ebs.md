

# Block storage with Amazon Elastic Block Store
<a name="storage-ebs"></a>

 Amazon Elastic Block Store (Amazon EBS) provides block storage volumes for use with your ROSA workloads. Amazon EBS is the default storage backend for ROSA. Your cluster includes the Amazon EBS CSI driver and the Amazon EBS CSI Driver Operator. Unless you configure another backend, Amazon EBS provisions all persistent volumes.

Use Amazon EBS for single-pod, read-write workloads that need low-latency block storage, such as databases and other stateful applications that do not share a file system across pods.

## Characteristics
<a name="storage-ebs-characteristics"></a>
+  **Storage type** – Block storage. Each volume attaches to a single node.
+  **Access mode** – ReadWriteOnce (RWO). An Amazon EBS volume cannot be written to by multiple nodes at the same time.
+  **Availability Zone scope** – An Amazon EBS volume exists in a single Availability Zone and can be attached only to a node in that same Availability Zone. If the node fails, the volume is not automatically available to a node in another Availability Zone.
+  **Dynamic provisioning** – Supported, including volume snapshots.

**Availability Zone constraint for EBS volumes**  
An Amazon EBS volume is bound to a single Availability Zone and cannot move between zones while attached. Use the `Recreate` deployment strategy for workloads that depend on Amazon EBS volumes. Set `volumeBindingMode: WaitForFirstConsumer` on the storage class. This ensures that the volume is provisioned in the same Availability Zone as the pod that consumes it.

## Volume types
<a name="storage-ebs-volume-types"></a>

The Amazon EBS CSI driver (`ebs.csi.aws.com`) supports many Amazon EBS volume types, including `gp3`, `gp2`, `io1`, `io2`, `st1`, and `sc1`. You set the volume type with the `type` parameter in a storage class.

 ROSA ships two storage classes that use the General Purpose SSD types:
+  `gp3-csi` provisions `gp3` volumes and is the cluster default.
+  `gp2-csi` provisions `gp2` volumes.

To use other volume types—for example, `io1` for high-IOPS workloads or `st1` for throughput-optimized HDD—create a custom storage class that specifies the volume type in the `parameters.type` field. We recommend `gp3` over `gp2` for most workloads.

Common storage class parameters for the Amazon EBS CSI driver include `type`, `iops`, `throughput`, `encrypted`, and `kmsKeyId`. Setting `allowVolumeExpansion: true` on a storage class enables online volume resizing.

## Default storage class
<a name="storage-ebs-default-class"></a>

Newly created ROSA clusters (version 4.10 and later) are configured with a default `gp3-csi` storage class backed by the Amazon EBS CSI driver. When a PVC does not name a storage class, ROSA uses `gp3-csi` to provision the volume. A `gp2-csi` class is also available for workloads that require the `gp2` volume type.

Modern ROSA clusters use only CSI-backed storage classes. The legacy in-tree AWS EBS volume plugin and its associated storage classes have been removed from the underlying OpenShift platform. Do not reference legacy in-tree class names—such as `gp2` or `gp3` without the `-csi` suffix—in storage class configurations.

## Encryption
<a name="storage-ebs-encryption"></a>

 Amazon EBS encryption protects persistent volume data at rest and in transit.

### Encryption at rest
<a name="storage-ebs-encryption-at-rest"></a>

With the default `gp3-csi` storage class, your persistent volumes are encrypted at rest using the AWS managed `aws/ebs` AWS KMS key. Volumes provisioned from other storage classes are encrypted only when the class sets `encrypted: "true"`.

### Encryption in transit
<a name="storage-ebs-encryption-in-transit"></a>

For encrypted Amazon EBS volumes, Amazon EBS encryption protects data in transit between the Amazon EC2 instance and its attached volume. Encryption operations run on the Amazon EC2 host.

### Key management
<a name="storage-ebs-key-management"></a>

When you create a cluster, you can choose to encrypt Amazon EBS volumes with the default AWS KMS key or with a customer managed, symmetric AWS KMS key. A customer managed key must be in the same AWS Region as the cluster. To use a customer managed key for volumes provisioned from a custom storage class, specify the key with `kmsKeyId`.

For more information about AWS KMS keys and encryption on ROSA, see [Protecting data using encryption](data-protection-encryption.md).

## Permissions
<a name="storage-ebs-permissions"></a>

The Amazon EBS CSI Driver Operator receives its permissions from the AWS managed policy `ROSAAmazonEBSCSIDriverOperatorPolicy`. The operator’s IAM role is created automatically when you create the cluster, so no additional IAM configuration is required to use Amazon EBS storage. For more information about how AWS STS affects storage-driver permissions, see [AWS STS and storage-driver permissions](storage-csi-concepts.md#storage-sts-permissions).