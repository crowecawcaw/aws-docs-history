

 **Help improve this page** 

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Amazon EC2 instance store for Kubernetes volume storage
<a name="lis-csi"></a>

The Amazon EC2 Instance Store CSI driver is a Container Storage Interface (CSI) plugin that enables Kubernetes to use EC2 instance store volumes. Instance store volumes provide ephemeral block-level storage that is physically attached to the host computer. The driver manages the lifecycle of these NVMe storage volumes and makes them available as Kubernetes [persistent volumes](https://kubernetes.io/docs/concepts/storage/persistent-volumes/).

The Amazon EC2 Instance Store CSI driver interacts with backend NVMe devices through local Linux operations. No AWS API calls are involved, so no IAM role is required.

## Considerations
<a name="lis-csi-considerations"></a>

**Important**  
The Amazon EC2 Instance Store CSI driver will erase all data on ephemeral disks during installation. If another CSI driver, or volume managing system (such as LVM, raw filesystems, LUKS, etc.) is managing ephemeral disks, back up your data before installing the Amazon EC2 Instance Store CSI driver to avoid data loss.
+ The Amazon EC2 Instance Store CSI driver doesn’t work with EKS Auto Mode.
+ You can’t mount Amazon EC2 instance store volumes to Fargate Pods.
+ The Amazon EC2 Instance Store CSI driver is not available for the following instance types: C1, C3, C4, C5d, C5ad, C6gd, D2, D3, D3en, DL1, E3, Edge1gd, F1, G2, G3, G4ad, G4dn, H1, HSM1, I2, I3, I3.metal, I3en, M1, M2, M3, M4, M5d, M5ad, M5dn, M6gd, P2, P3, P3dn, P4d, P4de, R3, R4, R5d, R5ad, R5dn, R6gd, T1, T2, X1, X1e, X2gd, and Z1d.
+ Support is provided for the latest add-on version and one prior version. Fixes for bugs or vulnerabilities found in the latest version will be backported to the previous release as a new minor version.
+ Instance storage is ephemeral. Data is lost when the node terminates. Implement application-level replication or backups for critical data.
+ Volume expansion is not supported.
+ I/O throttling is enabled by default for all volumes to ensure fair bandwidth sharing across workloads. For more information, see [I/O throttling](#lis-csi-throttling).
+ Newly launched instances have updated NVMe identify command responses compared to older instances of the same type. If your tooling depends on specific NVMe identify values, review your logic for compatibility. For more information, see [NVMe namespace changes on newly launched instances](#lis-csi-nvme-namespace).

## Prerequisites
<a name="lis-csi-prereqs"></a>

Before you begin, make sure you have the following:
+ An existing Amazon EKS cluster. To see all available versions of the add-on, run the following AWS CLI command:

  ```
  aws eks describe-addon-versions --addon-name aws-ec2-local-instance-store-csi-driver
  ```

## Installing the Amazon EC2 Instance Store CSI driver
<a name="managing-lis-csi"></a>

The Amazon EC2 Instance Store CSI driver is available as an Amazon EKS add-on. Installing the driver enables your cluster to use instance store volumes for pod storage.

To install the driver, add the Amazon EC2 Instance Store CSI driver add-on to your cluster. For instructions, see [Creating an Amazon EKS add-on](creating-an-add-on.md). For more information about EKS add-ons, see [Amazon EKS add-ons](eks-add-ons.md).

## Deploying a sample application
<a name="lis-sample-app"></a>

After installing the driver, you can deploy sample applications to verify that instance store volumes work correctly with your cluster. You can deploy a variety of sample apps and modify them as needed.

## I/O throttling
<a name="lis-csi-throttling"></a>

The Amazon EC2 Instance Store CSI driver includes built-in I/O throttling to ensure fair bandwidth sharing across workloads on the same NVMe controller. Throttling is enabled by default for all volumes, preventing any single workload from consuming disproportionate I/O bandwidth at the expense of other workloads on the same node.

### Configuring throttling
<a name="lis-csi-throttling-config"></a>

You can configure throttling at two levels:
+  **StorageClass parameter** – Set the `throttling` parameter to `"true"` (default) or `"false"` in your StorageClass definition.
+  **PVC annotation** – Set the `lis.csi.aws.com/throttling` annotation to `"true"` or `"false"` on individual PersistentVolumeClaims. This overrides the StorageClass setting when present.

The following table shows how the StorageClass parameter and PVC annotation interact:


| PVC Annotation | StorageClass Parameter | Result | 
| --- | --- | --- | 
| Not set | Not set | Throttling enabled (default) | 
| Not set |  `"false"`  | Throttling disabled | 
|  `"false"`  |  `"true"` or not set | Throttling disabled | 
|  `"true"`  |  `"false"`  | Throttling enabled | 

### Creating an unthrottled StorageClass
<a name="lis-csi-throttling-unthrottled-sc"></a>

To disable throttling for all volumes in a StorageClass:

```
apiVersion: storage.k8s.io/v1
kind: StorageClass
metadata:
  name: ec2-instance-store-unthrottled
provisioner: lis.csi.aws.com
parameters:
  throttling: "false"
volumeBindingMode: WaitForFirstConsumer
```

### Disabling throttling for a single PVC
<a name="lis-csi-throttling-disable-pvc"></a>

To disable throttling on an individual PVC while using a throttled StorageClass:

```
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: high-perf-pvc
  annotations:
    lis.csi.aws.com/throttling: "false"
spec:
  accessModes:
    - ReadWriteOnce
  storageClassName: ec2-instance-store-sc
  resources:
    requests:
      storage: 100Gi
```

### Throttling considerations
<a name="lis-csi-throttling-considerations"></a>
+ Throttling is enabled by default to provide predictable performance for all workloads sharing an NVMe controller.
+ Disabling throttling on a volume allows it to consume more I/O bandwidth, which may impact the performance of other throttled volumes on the same controller.
+ Consider isolating unthrottled workloads on dedicated nodes.
+ For RAID-0 volumes that span multiple controllers, throttling is applied to all member partitions.
+ Throttle state persists across node reboots.

## NVMe namespace changes on newly launched instances
<a name="lis-csi-nvme-namespace"></a>

Newly launched EC2 instances with local instance storage have updated NVMe Identify Controller and Identify Namespace command responses. These changes support NVMe namespace management on EC2 local instance storage. Existing running instances are not affected, and values remain stable throughout the lifecycle of any instance.

### Updated field values
<a name="_updated_field_values"></a>

The following fields have changed on newly launched instances compared to older instances of the same type:
+ Bit 3 of OACS: changed from 0 to 1
+ Bit 8 of OAES: changed from 0 to 1
+ NN: changed from 1 to a value <= 256
+ TNVMCAP: changed from 0 to the actual size of the local storage
+ NVMCAP: changed from 0 to the actual size of the local storage
+ NGUID: changed from all zeros to a valid NGUID

All updated values conform to the NVMe specification.

### Scope of changes
<a name="_scope_of_changes"></a>

These changes apply exclusively to EC2 local instance storage. Amazon EBS volumes are not affected. To distinguish between EBS volumes and local instance storage, run the following command:

```
sudo nvme list
```

In the output:
+  `Amazon Elastic Block Store` = EBS volume
+  `Amazon EC2 NVMe Instance Storage` = local instance storage

### Retrieving NVMe identify values
<a name="_retrieving_nvme_identify_values"></a>

To query these values using `nvme-cli`:

```
# Identify Controller
sudo nvme id-ctrl /dev/nvme1

# Identify Namespace
sudo nvme id-ns /dev/nvme1n1
```

### Action required
<a name="_action_required"></a>

No action is required. These changes are backward-compatible and follow the NVMe specification. However, if your application or tooling validates or depends on specific values from NVMe identify commands, review your logic to ensure compatibility with the updated values on newly launched instances.