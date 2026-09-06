

# Remediating exposures for Azure Storage blob containers
<a name="exposure-azure-storage-blob-container"></a>

AWS Security Hub can generate exposure findings for Azure Storage blob containers.

On the Security Hub console, the Azure Storage blob container involved in an exposure finding and its identifying information are listed in the **Resources** section of the finding details. Programmatically, you can retrieve resource details with the [GetFindingsV2](https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_GetFindingsV2.html) operation of the Security Hub CSPM API.

After identifying the resource involved in an exposure finding, you can delete the resource if you don't need it. Deleting a nonessential resource can reduce your exposure profile and AWS costs. If the resource is essential, follow these recommended remediation steps to help mitigate the risk. The remediation topics are divided based on the type of trait. 

A single exposure finding contains issues identified in multiple remediation topics. Conversely, you can address an exposure finding and bring down its severity level by addressing just one remediation topic. Your approach to risk remediation depends on your organizational requirements and workloads.

**Note**  
 The remediation guidance provided in this topic might require additional consultation in other Microsoft Azure resources. 

**Contents**
+ [Reachability traits for Azure Storage blob containers](#azure-storage-reachability)
  + [The storage account allows anonymous blob access](#storage-account-anonymous-access-allowed)
+ [Misconfiguration traits for Azure Storage blob containers](#azure-storage-misconfiguration)
  + [The storage account does not require HTTPS for transfer operations](#storage-account-allows-insecure-protocols)
  + [The storage account is not encrypted with customer-managed keys](#storage-account-cmk-not-used)
  + [The storage account allows cross-tenant access](#storage-account-cross-tenant-access-allowed)
  + [The storage account has blob soft delete disabled](#storage-account-soft-delete-disabled)
  + [The storage account allows permanent deletion of soft-deleted blobs](#storage-account-permanent-delete-allowed)
  + [The Azure Storage blob container has blob versioning disabled](#versioning-disabled)
  + [The storage container does not have an immutability policy](#storage-container-immutability-disabled)

## Reachability traits for Azure Storage blob containers
<a name="azure-storage-reachability"></a>

Here are reachability traits for Azure Storage blob containers and suggested remediation steps.

### The storage account allows anonymous blob access
<a name="storage-account-anonymous-access-allowed"></a>

 When anonymous read access is enabled, unauthenticated clients can read blob data without authorization. When the storage account permits anonymous (public) blob access and a container's access level allows it, anyone on the public internet can read the data in that container. Following standard security principles, disallow anonymous access at the account level and require every request to be authorized, unless your scenario explicitly depends on public read access. 

**Remediation**  
Take one or more of the following actions to address this exposure:

**Disallow anonymous access for the storage account**  
 Set the storage account's `AllowBlobPublicAccess` property to `false`. Disallowing anonymous access at the account level overrides the access settings of all containers in the account and blocks future anonymous requests. For more information, see [Prevent anonymous read access](https://learn.microsoft.com/en-us/azure/storage/blobs/anonymous-read-access-prevent) in the Microsoft Azure documentation. 

**Set the container access level to private**  
 If individual containers were configured for public access, set each container's anonymous access level to `Private` so that all requests require authorization. Before changing the setting, review any client applications that might depend on anonymous access. For more information, see [Configure anonymous read access](https://learn.microsoft.com/en-us/azure/storage/blobs/anonymous-read-access-configure) in the Microsoft Azure documentation. 

## Misconfiguration traits for Azure Storage blob containers
<a name="azure-storage-misconfiguration"></a>

Here are misconfiguration traits for Azure Storage blob containers and suggested remediation steps.

### The storage account does not require HTTPS for transfer operations
<a name="storage-account-allows-insecure-protocols"></a>

 When a storage account does not require secure transfer, it accepts requests over unencrypted HTTP. Data and credentials sent over HTTP can be intercepted or modified in transit by an attacker on the network path. Following standard security principles, require secure transfer so that the account accepts requests only over HTTPS. 

**Remediation**  
Take one or more of the following actions to address this exposure:

**Require secure transfer**  
 Enable the **Secure transfer required** property on the storage account (the `enableHttpsTrafficOnly` property). When secure transfer is required, any request made over HTTP is rejected. For more information, see [Require secure transfer](https://learn.microsoft.com/en-us/azure/storage/common/storage-require-secure-transfer) in the Microsoft Azure documentation. 

**Enforce a minimum TLS version**  
 Set the storage account's minimum TLS version to 1.2 (the `minimumTlsVersion` property) so that requests that use older, less secure protocol versions are rejected. Confirm that your clients support TLS 1.2 before you enforce this setting. For more information, see [Configure the minimum TLS version for a storage account](https://learn.microsoft.com/en-us/azure/storage/common/transport-layer-security-configure-minimum-version) in the Microsoft Azure documentation. 

### The storage account is not encrypted with customer-managed keys
<a name="storage-account-cmk-not-used"></a>

 By default, Azure Storage encrypts data at rest with Microsoft-managed keys. Customer-managed keys (CMK) give you control over the key that protects your data, including the ability to rotate, revoke, and audit access to the key. If your organization's compliance requirements call for control over encryption keys, the absence of customer-managed keys is a gap. Following data protection best practices, configure the storage account to use customer-managed keys stored in Azure Key Vault or a managed HSM. 

**Remediation: Configure customer-managed keys**  
 Store a key in Azure Key Vault or Azure Key Vault Managed HSM, with soft delete and purge protection enabled. Grant a managed identity the `get`, `wrapkey`, and `unwrapkey` permissions, and then configure the storage account to use that key for encryption. You can switch between customer-managed and Microsoft-managed keys at any time. For more information, see [Customer-managed keys for storage encryption](https://learn.microsoft.com/en-us/azure/storage/common/customer-managed-keys-overview) in the Microsoft Azure documentation. 

### The storage account allows cross-tenant access
<a name="storage-account-cross-tenant-access-allowed"></a>

 Cross-tenant access settings, such as cross-tenant object replication or cross-tenant shared access signature (SAS) delegation, can cause data to leave the Microsoft Entra tenant that owns the storage account. If your workload does not require sharing data across tenants, leaving these settings enabled increases the risk of data leaving your tenant boundary. Following standard security principles, disable cross-tenant access unless it is explicitly required. 

**Remediation: Disable cross-tenant access settings**  
 On the storage account, disable cross-tenant object replication (set `allowCrossTenantReplication` to `false`) and, where supported, restrict cross-tenant SAS delegation. Review your replication and sharing requirements before making the change. For more information, see [Azure Storage account overview](https://learn.microsoft.com/en-us/azure/storage/common/storage-account-overview) in the Microsoft Azure documentation. 

### The storage account has blob soft delete disabled
<a name="storage-account-soft-delete-disabled"></a>

 Blob soft delete protects individual blobs, snapshots, and versions from accidental or malicious deletion and overwrite. It retains the deleted data for a configurable retention period, during which you can restore it. When soft delete is disabled, deleted or overwritten blob data cannot be recovered, which exposes your account to permanent data loss. Following data protection best practices, enable blob soft delete with an appropriate retention period. 

**Remediation: Enable blob soft delete**  
 Enable blob soft delete on the storage account and set a retention period (1 to 365 days) that meets your recovery requirements. For more complete protection, enable container soft delete and blob versioning as well. For more information, see [Soft delete for blobs](https://learn.microsoft.com/en-us/azure/storage/blobs/soft-delete-blob-overview) in the Microsoft Azure documentation. 

### The storage account allows permanent deletion of soft-deleted blobs
<a name="storage-account-permanent-delete-allowed"></a>

 When permanent delete is allowed (the `allowPermanentDelete` property is `true`), soft-deleted blobs and snapshots can be removed before the soft delete retention period expires. This undermines the protection that soft delete provides, because a user or a compromised principal can permanently destroy recoverable data before the retention period expires. Following data protection best practices, do not allow permanent deletion of soft-deleted blobs unless you have a specific, well-understood requirement. 

**Remediation: Disable permanent delete**  
 Set the storage account's `allowPermanentDelete` property to `false` so that soft-deleted blobs and snapshots remain recoverable for the full retention period. For more information, see [Soft delete for blobs](https://learn.microsoft.com/en-us/azure/storage/blobs/soft-delete-blob-overview) in the Microsoft Azure documentation. 

### The Azure Storage blob container has blob versioning disabled
<a name="versioning-disabled"></a>

 Blob versioning automatically maintains previous versions of a blob. When a blob is modified or deleted, the prior state is preserved as a previous version that you can restore. When versioning is disabled, overwrites and deletes cannot be rolled back to an earlier state, which increases the risk of unrecoverable data loss or corruption. Following data protection best practices, enable blob versioning, together with soft delete, for optimal data protection. 

**Remediation: Enable blob versioning**  
 Enable versioning on the storage account's blob service. To control the cost of retaining many versions, use a lifecycle management policy to delete old versions automatically. For more information, see [Blob versioning](https://learn.microsoft.com/en-us/azure/storage/blobs/versioning-overview) in the Microsoft Azure documentation. 

### The storage container does not have an immutability policy
<a name="storage-container-immutability-disabled"></a>

 An immutability policy stores blob data in a WORM (Write Once, Read Many) state. In this state, data cannot be modified or deleted for a specified interval (a time-based retention policy) or until a legal hold is cleared. Without an immutability policy, business-critical or compliance-relevant data in the container can be overwritten or deleted, including by privileged users. Where regulatory or data-integrity requirements apply, configure an immutability policy for the container. 

**Remediation: Configure an immutability policy**  
 Configure a time-based retention policy or a legal hold on the container. Lock the time-based policy when testing is complete so that the data is fully protected in a WORM state. Enable soft delete before applying immutability policies for additional protection. For more information, see [Immutable storage for blob data](https://learn.microsoft.com/en-us/azure/storage/blobs/immutable-storage-overview) in the Microsoft Azure documentation. 