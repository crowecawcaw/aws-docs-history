

# Remediating exposures for GCP Cloud Storage buckets

AWS Security Hub can generate exposure findings for GCP Cloud Storage buckets.

On the Security Hub console, the GCP Cloud Storage bucket involved in an exposure finding and its identifying information are listed in the **Resources** section of the finding details. Programmatically, you can retrieve resource details with the `GetFindingsV2` operation of the Security Hub CSPM API.

After identifying the resource involved in an exposure finding, you can delete the resource if you don't need it. Deleting a nonessential resource can reduce your exposure profile and AWS costs. If the resource is essential, follow these recommended remediation steps to help mitigate the risk. The remediation topics are divided based on the type of trait. 

A single exposure finding contains issues identified in multiple remediation topics. Conversely, you can address an exposure finding and bring down its severity level by addressing just one remediation topic. Your approach to risk remediation depends on your organizational requirements and workloads.

**Note**  
 The remediation guidance provided in this topic might require additional consultation in other Google Cloud resources. 

**Contents**
+ [Reachability traits for GCP Cloud Storage buckets](#gcp-storage-bucket-reachability)
  + [The Cloud Storage bucket is anonymously or publicly accessible](#anonymous-or-public-access-allowed)
  + [The Cloud Storage bucket allows object-level access control lists](#storage-account-anonymous-access-allowed)
+ [Misconfiguration traits for GCP Cloud Storage buckets](#gcp-storage-bucket-misconfiguration)
  + [The Cloud Storage bucket is not encrypted at-rest with customer-managed keys](#sse-kms-not-used)
  + [The Cloud Storage bucket has versioning disabled](#versioning-disabled)
  + [The Cloud Storage bucket has Bucket Lock disabled](#object-lock-disabled)
  + [The Cloud Storage bucket has soft delete disabled](#storage-account-soft-delete-disabled)

## Reachability traits for GCP Cloud Storage buckets
<a name="gcp-storage-bucket-reachability"></a>

Here are reachability traits for GCP Cloud Storage buckets and suggested remediation steps.

### The Cloud Storage bucket is anonymously or publicly accessible
<a name="anonymous-or-public-access-allowed"></a>

 The bucket's Identity and Access Management (IAM) policy grants a role to `allUsers` or `allAuthenticatedUsers`. `allUsers` is anyone on the internet, and `allAuthenticatedUsers` is anyone signed in with a Google Account, including service accounts. Depending on the role, they can read, overwrite, or delete objects in the bucket. Following standard security principles, remove public access from the bucket's IAM policy. 

**Remediation**  
Take one or more of the following actions to address this exposure:

**Remove public principals from the bucket**  
 Remove `allUsers` and `allAuthenticatedUsers` from the bucket's IAM policy. For more information, see [Make data public](https://docs.cloud.google.com/storage/docs/access-control/making-data-public) on the Google Cloud website. 

**Enforce public access prevention**  
 Enforce public access prevention on the bucket so that no one can grant public access. To enforce it across projects, folders, or the organization, use the `storage.publicAccessPrevention` organization policy constraint. Existing public grants stay in the policy, so you must also remove them. Enforcement breaks applications and static websites that depend on public access. For more information, see [Public access prevention](https://docs.cloud.google.com/storage/docs/public-access-prevention) on the Google Cloud website. 

**Use alternative access methods**  
 To share content without public grants, use signed URLs for time-limited access, or use private bucket access to serve the content through Cloud Load Balancing and Cloud CDN. For more information, see [Public access prevention](https://docs.cloud.google.com/storage/docs/public-access-prevention) on the Google Cloud website. 

### The Cloud Storage bucket allows object-level access control lists
<a name="storage-account-anonymous-access-allowed"></a>

 When uniform bucket-level access is off, object-level access control lists (ACLs) can grant access that doesn't appear in the bucket's IAM policy. Because ACLs can grant access to `allUsers`, reviewing only the bucket's IAM policy can miss public objects. Following standard security principles, turn on uniform bucket-level access for your Cloud Storage buckets. 

**Remediation: Turn on uniform bucket-level access**  
 Turn on uniform bucket-level access for the bucket. This disables ACLs, so principals that get access only through ACLs lose it. Before you turn it on, grant that access through IAM instead. After it has been on for 90 days, you can't turn it off. For more information, see [Uniform bucket-level access](https://docs.cloud.google.com/storage/docs/uniform-bucket-level-access) on the Google Cloud website. 

## Misconfiguration traits for GCP Cloud Storage buckets
<a name="gcp-storage-bucket-misconfiguration"></a>

Here are misconfiguration traits for GCP Cloud Storage buckets and suggested remediation steps.

### The Cloud Storage bucket is not encrypted at-rest with customer-managed keys
<a name="sse-kms-not-used"></a>

 The bucket has no default Cloud Key Management Service (Cloud KMS) key, so objects written without a specified key use Google-owned and Google-managed encryption keys. Without a customer-managed key, you can't control or audit key use yourself, and you can't disable the key to revoke access to the data. Following data protection best practices, use customer-managed encryption keys for your Cloud Storage buckets. 

**Remediation: Set a customer-managed key as the default key**  
 Grant the bucket's Cloud Storage service agent the Cloud KMS CryptoKey Encrypter/Decrypter role (`roles/cloudkms.cryptoKeyEncrypterDecrypter`) on a Cloud KMS key in the bucket's location. Then set the key as the bucket's default key. Existing objects keep their current encryption until you rewrite them. For more information, see [Customer-managed encryption keys](https://docs.cloud.google.com/storage/docs/encryption/using-customer-managed-keys) on the Google Cloud website. 

### The Cloud Storage bucket has versioning disabled
<a name="versioning-disabled"></a>

 With Object Versioning, Cloud Storage keeps a noncurrent version each time you replace or delete a live object. When it's off, you can recover replaced or deleted objects only while soft delete retains them. Following data protection best practices, turn on Object Versioning for your Cloud Storage buckets. 

**Remediation: Turn on Object Versioning**  
 Turn on Object Versioning for the bucket. Noncurrent versions are billed at the same rate as live objects, so use Object Lifecycle Management rules to remove older ones. Object Versioning doesn't protect against bucket deletion, but soft delete does. For more information, see [Object Versioning](https://docs.cloud.google.com/storage/docs/object-versioning) on the Google Cloud website. 

### The Cloud Storage bucket has Bucket Lock disabled
<a name="object-lock-disabled"></a>

 A retention policy keeps objects from being deleted or replaced until they're older than the retention period. The bucket has no retention policy, or its policy isn't locked with Bucket Lock. Anyone with sufficient permissions, including an attacker with stolen credentials, can shorten or remove an unlocked policy. Following data protection best practices, use a locked retention policy to protect data that you must retain. 

**Remediation: Set and lock a retention policy**  
 Set a retention policy on the bucket, and then lock it with Bucket Lock. Locking is irreversible. No one can then remove the policy or shorten the retention period, and you can't delete the bucket until every object meets the retention period. Before you lock the policy, make sure that the retention period fits your requirements. For more information, see [Bucket Lock](https://docs.cloud.google.com/storage/docs/bucket-lock) on the Google Cloud website. 

### The Cloud Storage bucket has soft delete disabled
<a name="storage-account-soft-delete-disabled"></a>

 Soft delete keeps deleted or overwritten objects, and a deleted bucket, for a retention duration so that you can restore them. When soft delete is off, you can't restore a deleted bucket. Deleted or overwritten objects are permanently removed unless Object Versioning keeps them as noncurrent versions. Following data protection best practices, turn on soft delete for your Cloud Storage buckets. 

**Remediation: Turn on soft delete**  
 Turn on soft delete for the bucket with a retention duration from 7 to 90 days that meets your recovery requirements. Soft-deleted data is billed until it's permanently removed, so costs can rise for buckets that hold mostly temporary data. For more information, see [Soft delete](https://docs.cloud.google.com/storage/docs/soft-delete) on the Google Cloud website. 