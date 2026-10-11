

# Multi-protocol storage with Amazon FSx for NetApp ONTAP
<a name="storage-fsx-ontap"></a>

With Amazon FSx for NetApp ONTAP, you can provision high-performance file and block storage built on the NetApp ONTAP file system. On ROSA, you provision FSx for ONTAP storage through **NetApp Trident** (also known as Astra Trident), the open-source CSI driver from NetApp for Kubernetes.

Use FSx for ONTAP when you need high-performance shared storage, or both NFS file volumes and iSCSI block volumes from the same file system. It also suits enterprise workloads such as databases and business applications that expect ONTAP data-management features.

**NetApp Trident is not an AWS or Red Hat service**  
NetApp Trident is a NetApp product. It is not an AWS or Red Hat service or add-on. You install, configure, and operate Trident yourself, and NetApp supports the Trident driver.

## Characteristics
<a name="storage-fsx-ontap-characteristics"></a>
+  **Storage type** – Multi-protocol file and block storage. Trident can back ROSA persistent volume claims with FSx for ONTAP NFS or iSCSI volumes.
+  **Access modes** – NFS volumes support ReadWriteMany (RWX) and ReadWriteOnce (RWO). iSCSI block volumes support ReadWriteMany (RWX) and ReadWriteOnce (RWO).
+  **Availability Zone scope** – FSx for ONTAP supports Single-AZ and Multi-AZ deployments. Multi-AZ file systems provide high availability with transparent failover for file protocols and multipath failover for iSCSI.
+  **Multi-protocol access** – Trident can provision both NFS file volumes and iSCSI block volumes from the same FSx for ONTAP file system.

## Installing Trident
<a name="storage-fsx-ontap-install"></a>

You deploy Trident with the Trident Operator, using either a Helm chart (Helm v3) or the `tridentctl` command-line tool. You install and operate Trident yourself. Trident uses a calendar-based version scheme (for example, 26.06). NetApp typically supports the two to three most recent minor versions. For the specific release that is compatible with your ROSA and Red Hat OpenShift version, see [Requirements](https://docs.netapp.com/us-en/trident/trident-get-started/requirements.html) in the NetApp Trident documentation.

Because ROSA uses AWS STS, Trident needs an IAM role for FSx API access. This role must be wired to the cluster’s OIDC provider, similar to the Amazon EFS CSI driver.

For deployment and IAM setup instructions, see [Initial Setup](https://docs.netapp.com/us-en/netapp-solutions-containers/openshift/os-rosa-solution-overview.html#initial-setup) in NetApp’s ROSA solution guide.

**Exclude EBS devices from multipath when running iSCSI**  
If you run FSx for ONTAP iSCSI volumes alongside the Amazon EBS CSI driver on the same nodes, exclude Amazon EBS devices in the node `multipath.conf` configuration. This prevents multipath from managing Amazon EBS volumes. The NetApp deployment guide includes a prepared `multipath.conf`.

## Encryption
<a name="storage-fsx-ontap-encryption"></a>

FSx for ONTAP provides encryption at rest and in transit.

### Encryption at rest
<a name="storage-fsx-ontap-encryption-at-rest"></a>

FSx for ONTAP automatically encrypts all data at rest and all backups using an AES-256 block cipher and AWS KMS.

### Encryption in transit
<a name="storage-fsx-ontap-encryption-in-transit"></a>

FSx for ONTAP supports in-transit encryption for its file and block protocols.

### Key management
<a name="storage-fsx-ontap-key-management"></a>

You choose one of two key options:
+  ** AWS managed key** – The default option. AWS manages the key at no additional cost.
+  **Customer managed key** – Provide your own symmetric AWS KMS key for greater control. With a customer managed key, you can define cross-account key policies and fine-grained key grants, and enable automatic annual key rotation managed by AWS KMS.

**FSx for ONTAP requires symmetric KMS keys**  
FSx for ONTAP accepts only symmetric AWS KMS encryption keys. Asymmetric keys are not supported.

## Support model
<a name="storage-fsx-ontap-support"></a>

Responsibility for FSx for ONTAP with Trident is shared between AWS and NetApp:
+  ** AWS ** supports the FSx for ONTAP backend, including the file system, storage virtual machine, volumes, logical interfaces, and the ONTAP data path.
+  **NetApp** supports the Trident CSI driver code and configuration.