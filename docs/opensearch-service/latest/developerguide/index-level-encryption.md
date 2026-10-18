

# Index level encryption for Amazon OpenSearch Service
<a name="index-level-encryption"></a>

Index level encryption for OpenSearch Service is an encryption option that lets you encrypt data at rest on a per-index basis using AWS Key Management Service (AWS KMS) customer managed keys. With index level encryption, you can use different customer managed keys for different indices on the same domain. Index level encryption extends domain-level encryption at rest. For more information, see [Encryption of data at rest for Amazon OpenSearch Service](encryption-at-rest.md).

**Important**  
To enable index level encryption, select **Native** for **Encryption mode** when you create the domain.

## How index level encryption works
<a name="ile-how-it-works"></a>

Index level encryption builds upon the existing encryption at rest capability in OpenSearch Service. While domain-level encryption at rest uses a single AWS KMS key to encrypt all data on a domain, with index level encryption, you can specify different customer managed keys for individual indices.

When you enable index level encryption, data is encrypted as follows:

**Encrypted at the index level (using customer managed keys):**
+ All user-created data (indices and snapshots)

**Encrypted at the domain level (using the domain default key that you specify in `KmsKeyId` when you create the domain):**
+ System indices
+ OpenSearch logs

**Note**  
If you create an index without specifying a key, OpenSearch Service encrypts it using the domain default key.

## AWS Region support
<a name="ile-region-support"></a>

Index level encryption is supported on OpenSearch Service domains that are running OpenSearch version 3.3 or later in the following AWS Regions:
+ US East (Ohio) (us-east-2)
+ US East (N. Virginia) (us-east-1)
+ US West (Oregon) (us-west-2)
+ Asia Pacific (Mumbai) (ap-south-1)
+ Asia Pacific (Seoul) (ap-northeast-2)
+ Asia Pacific (Singapore) (ap-southeast-1)
+ Asia Pacific (Sydney) (ap-southeast-2)
+ Asia Pacific (Tokyo) (ap-northeast-1)
+ Canada (Central) (ca-central-1)
+ Europe (Frankfurt) (eu-central-1)
+ Europe (Ireland) (eu-west-1)
+ Europe (London) (eu-west-2)
+ Europe (Paris) (eu-west-3)
+ South America (São Paulo) (sa-east-1)

## Prerequisites
<a name="ile-prerequisites"></a>

Before enabling index level encryption, ensure that your domain meets the following requirements:
+ **New domain only**: Index level encryption can only be enabled on new domains during creation and cannot be enabled on existing domains. Additionally, once enabled, this option cannot be disabled.
+ **OpenSearch version**: Your domain must run OpenSearch 3.3 or later.
+ **Encryption at rest**: Encryption of data at rest option must be enabled (EncryptionAtRestOptions is set to true).
+ **IAM permissions**: You need permissions to register AWS KMS keys and create indices.

## Important considerations before enabling index level encryption
<a name="ile-considerations"></a>

Consider the following important considerations when using index level encryption:
+ Index level encryption is not supported with the following features:
  + UltraWarm
  + Multi-Tier Storage and Writable Warm
  + Optimized Engine
  + S3 Vectors
  + Cross-cluster replication
+ **Memory requirements**: Index level encryption requires a data node instance type with at least 16 GB of memory.
+ **KNN plugin engine limitations**: When using the k-nearest neighbors (KNN) plugin with index level encryption, only the Lucene engine is supported. The FAISS engine is not supported with index level encryption.
+ **Key recovery**: If you delete a customer managed key, you cannot recover data encrypted with that key. Always maintain proper key lifecycle management practices.
+ **Manual snapshots**: Data in manual snapshots stored in Amazon S3 is not encrypted with index-level keys. Use Amazon S3 server-side encryption for snapshot repository buckets.
+ **Fine-grained access control integration**: Index level encryption does not replace Fine-Grained Access Control. Use both features together for comprehensive security.
+ **Key deletion impact**: If you disable or delete your AWS KMS key without unregistering it from your domain, the index turns red.
+ **Performance**: Search and analytics queries that use multi-term aggregations may experience higher latency on encrypted indices. Test your application performance with index-level encryption enabled before deploying to production.

## Authorization model
<a name="ile-authorization-model"></a>

Index level encryption uses a two-phase authorization model:
+ **Key registration phase**: When you register an AWS KMS key using the `_plugins/_opensearch_storage_encryption/_register_key` API, OpenSearch Service performs authorization checks to verify that you have permission to use the key. The service creates appropriate AWS KMS grants for the key and stores the key reference in Amazon S3.
+ **Index creation phase**: When you create an index with encryption settings, OpenSearch Service uses the grant created during registration. If the grant does not exist, index creation fails, ensuring only registered keys can encrypt indices.
+ If you don't specify an AWS KMS key, OpenSearch Service uses the domain default key to encrypt the index. You don't need to register the domain default key.

**Note**  
The AWS KMS authorization check occurs when you register and when you unregister a key. If you have cluster access and the appropriate fine-grained access control permissions, you can create indices using registered keys without direct AWS KMS permissions.

### AWS KMS key limits
<a name="ile-kms-key-limits"></a>

With index level encryption, you can use a maximum of 10,000 unique AWS KMS keys per OpenSearch Service domain. For other service quotas, see [Amazon OpenSearch Service quotas](limits.md).

### Required IAM permissions
<a name="ile-iam-permissions"></a>

To register AWS KMS keys, you need the following permissions:

**For the IAM principal registering keys:**

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "kms:CreateGrant",
        "kms:DescribeKey",
        "kms:GenerateDataKey",
        "kms:Encrypt",
        "kms:Decrypt"
      ],
      "Resource": "arn:aws:kms:{{region}}:{{account-id}}:key/{{key-id}}"
    },
    {
      "Effect": "Allow",
      "Action": [
        "es:ESHttpPost"
      ],
      "Resource": [
        "arn:aws:es:{{region}}:{{account-id}}:domain/{{domain-name}}/_plugins/_opensearch_storage_encryption/_register_key",
        "arn:aws:es:{{region}}:{{account-id}}:domain/{{domain-name}}/_plugins/_opensearch_storage_encryption/_unregister_key"
      ]
    }
  ]
}
```

## Understanding AWS KMS integration
<a name="ile-kms-integration"></a>

This section explains how OpenSearch Service uses AWS KMS permissions, what types of AWS KMS keys are supported, and how encryption context works with index-level encryption.

### How OpenSearch uses AWS KMS permissions
<a name="ile-kms-permissions"></a>

OpenSearch Service requires the following AWS KMS permissions to implement index-level encryption. Each permission serves a specific purpose in the encryption workflow:

`kms:CreateGrant`  
Creates a grant during key registration that allows OpenSearch to encrypt and decrypt data on your behalf without requiring users to have direct AWS KMS permissions for daily operations.

`kms:DescribeKey`  
Validates that the AWS KMS key exists, is enabled, and is a valid symmetric encryption key during registration.

`kms:GenerateDataKey`  
Generates data encryption keys (DEKs) when writing data to encrypted indices using envelope encryption.

`kms:Decrypt`  
Decrypts the data encryption keys when reading data from encrypted indices.

`kms:Encrypt`  
Encrypts metadata or small data elements directly with the AWS KMS key (used occasionally).

### Supported AWS KMS key types
<a name="ile-supported-key-types"></a>

Index-level encryption supports:
+ **Symmetric encryption keys only** (SYMMETRIC\_DEFAULT key spec)
+ **Both single-region and multi-region** customer managed keys

Asymmetric keys, HMAC keys, and other key types are not supported for index-level encryption.

### Encryption context
<a name="ile-encryption-context"></a>

OpenSearch Service uses encryption context to ensure encrypted data can only be decrypted in the proper context.

**Encryption context (added and managed by the service)**
+ `domainARN` - The full ARN of your OpenSearch domain (automatically included in all encryption operations)

**Optional encryption context:**

Custom key-value pairs you specify during key registration (e.g., `department: "engineering"`, `environment: "production"`). If you specify custom encryption context during key registration, you must provide the exact same context when creating indices with that key.

## Enabling index level encryption
<a name="ile-enabling"></a>

Enabling index level encryption is a three-step process:

1. **Enable index level encryption on your domain** - Configure the domain to support per-index encryption

1. **Register AWS KMS keys** - Register one or more customer managed keys with your domain

1. **Create encrypted indices** - Create indices with encryption settings that reference the registered keys

### Step 1: Enable index level encryption on your domain
<a name="ile-enable-domain"></a>

You can enable index level encryption only on new domains during creation using either the AWS console or APIs.

#### Using the AWS console
<a name="ile-enable-console"></a>

To enable index level encryption when creating a new domain:

1. Open the OpenSearch Service console at [https://console.aws.amazon.com/opensearch/](https://console.aws.amazon.com/opensearch/).

1. Choose **Create domain**.

1. Configure your domain settings (name, OpenSearch version 3.3\+, deployment type, etc.).

1. In the **Security** section, select **Enable encryption of data at rest**.

1. In the **Choose an AWS KMS key** section, select **Choose a different AWS KMS key (advanced)**.

1. In the **Encryption mode** section, select **Native**.
   + **Disk** - Default encryption mode that encrypts entire domain at rest
   + **Native** - Index level encryption mode that allows per-index KMS keys

1. Select your customer managed KMS key or create a new one.

1. Complete the remaining domain configuration and choose **Create domain**.

When creating a new domain with OpenSearch 3.3\+ and a customer managed AWS KMS key, the console displays encryption mode options as shown below. To enable index level encryption, you must select **Native** for **Encryption mode**.

![The Encryption section of the Create domain page in the console. Native is selected for Encryption mode, and Choose a different AWS KMS key (advanced) is selected.](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/images/ile-console-encryption-mode.png)


The console encryption settings section displays:
+ **Require HTTPS for all traffic to the domain** (enabled) - Your domain only accepts requests over HTTPS.
+ **Node-to-node encryption** (enabled) - Provides an additional layer of security with TLS encryption for all communications within the VPC.
+ **Enable encryption of data at rest** (enabled) - Secures indexes and automated snapshots.
+ **Encryption mode** section with two options:
  + **Disk** - Default encryption mode that encrypts entire domain at rest using AWS KMS
  + **Native** (selected) - Data is encrypted before it is written to disk. The AWS KMS key selected below is your domain default, with the option to specify a different key per index.
+ **Choose an AWS KMS key** section with options for AWS owned key or customer managed key

**Note**  
The **Native** encryption mode option only appears when you select a customer managed AWS KMS key and your domain runs OpenSearch 3.3 or later.

#### Using the API
<a name="ile-enable-api"></a>

You can enable index level encryption using the AWS CLI or AWS SDKs through the OpenSearch Service configuration API.

**For new domains (CreateDomain API):**

```
{
  "DomainName": "my-encrypted-domain",
  "EngineVersion": "OpenSearch_3.3",
  "ClusterConfig": {
    "InstanceType": "r6g.large.search",
    "InstanceCount": 1
  },
  "EBSOptions": {
    "EBSEnabled": true,
    "VolumeType": "gp3",
    "VolumeSize": 20
  },
  "EncryptionAtRestOptions": {
    "Enabled": true,
    "KmsKeyId": "arn:aws:kms:us-east-1:123456789012:key/12345678-1234-1234-1234-123456789012",
    "EncryptionMode": "NATIVE"
  }
}
```

**AWS CLI example for new domains:**

```
aws opensearch create-domain \
  --domain-name my-encrypted-domain \
  --engine-version OpenSearch_3.3 \
  --cluster-config InstanceType=r6g.large.search,InstanceCount=1 \
  --ebs-options EBSEnabled=true,VolumeType=gp3,VolumeSize=20 \
  --encryption-at-rest-options Enabled=true,KmsKeyId=arn:aws:kms:us-east-1:123456789012:key/12345678-1234-1234-1234-123456789012,EncryptionMode=NATIVE \
  --node-to-node-encryption-options Enabled=true \
  --domain-endpoint-options EnforceHTTPS=true
```

**Important**  
Index level encryption requires both `EncryptionAtRestOptions.Enabled=true` and a customer managed `KmsKeyId` with `EncryptionMode=NATIVE`.

**Warning**  
You cannot disable index level encryption after it has been enabled on a domain. Plan your encryption strategy carefully before enabling this feature.

### Step 2: Register AWS KMS keys
<a name="ile-register-keys"></a>

Before you can use a customer managed key for index encryption, you must register it with your domain. Registration performs authorization checks, creates the necessary AWS KMS grants, and makes the key available for use with indices.

**Note**  
The `_register_key` and `_unregister_key` API calls must be signed with SigV4.

**To register an AWS KMS key using the OpenSearch API:**

```
POST _plugins/_opensearch_storage_encryption/_register_key
{
  "key_id": "arn:aws:kms:us-east-1:123456789012:key/12345678-1234-1234-1234-123456789012",
  "encryption_context": "department=engineering,environment=production"
}
```

**Request parameters:**

`key_id` (required)  
The full key ARN of the customer managed key (`arn:aws:kms:{{region}}:{{account-id}}:key/{{key-id}}`). Key IDs and alias ARNs are not accepted.

`encryption_context` (optional)  
A string of comma-separated key-value pairs in the format `key1=value1,key2=value2`. If specified, you must provide the same encryption context when you create indices with this key and when you unregister the key. You can't use `domainARN` as a key, because the service adds it automatically.

**Sample response:**

```
{
  "acknowledged": true,
  "status": "available",
  "message": "Key registered successfully. Typically it takes a few seconds but it may take several minutes for permissions to propagate before the key can be used for encrypting indices.",
  "key_id": "arn:aws:kms:us-east-1:123456789012:key/12345678-1234-1234-1234-123456789012",
  "encryption_context": "department=engineering,environment=production,domainARN=arn:aws:es:us-east-1:123456789012:domain/my-domain"
}
```

The `encryption_context` in the response includes the `domainARN` value that the service adds.

**Important**  
Only IAM principals with AWS KMS permissions mentioned above can register keys. After registration, any authenticated user with cluster access can create indices using the registered key.

### Step 3: Create encrypted indices
<a name="ile-create-indices"></a>

After registering an AWS KMS key, you can create indices that use the key for encryption.

**To create an encrypted index:**

```
PUT /logs-2025
{
  "settings": {
    "index.store.type": "cryptofs",
    "index.store.crypto.key_provider": "aws-kms",
    "index.store.crypto.kms.key_arn": "arn:aws:kms:us-east-1:123456789012:key/12345678-1234-1234-1234-123456789012",
    "index.store.crypto.kms.encryption_context": "department=engineering,environment=production"
  }
}
```

**Index settings:**
+ `index.store.type`: Must be set to `cryptofs` to enable encryption
+ `index.store.crypto.key_provider`: Must be set to `aws-kms` to use AWS KMS as the key provider
+ `index.store.crypto.kms.key_arn`: The ARN of a registered customer managed key
+ `index.store.crypto.kms.encryption_context` (optional): A string in the format `key1=value1,key2=value2`. Required if the key was registered with an encryption context, and must match it exactly. Don't include `domainARN`.

**Sample response:**

```
{
  "acknowledged": true,
  "shards_acknowledged": true,
  "index": "logs-2025"
}
```

After creating an encrypted index, all data written to the index is automatically encrypted using the specified customer managed key.

#### Using index templates
<a name="ile-index-templates"></a>

You can use index templates to automatically apply encryption settings to new indices that match a specific pattern:

```
PUT _index_template/encrypted-logs-template
{
  "index_patterns": ["logs-*"],
  "template": {
    "settings": {
      "index": {
        "store.type": "cryptofs",
        "store.crypto.key_provider": "aws-kms",
        "store.crypto.kms.key_arn": "arn:aws:kms:us-east-1:123456789012:key/12345678-1234-1234-1234-123456789012",
        "store.crypto.kms.encryption_context": "department=engineering,environment=production"
      }
    }
  }
}
```

**Note**  
If you registered the key with an encryption context, the template must include the same `encryption_context`. Otherwise, index creation fails with a `KMS key unusable` error.

## Managing encryption keys
<a name="ile-key-management"></a>

### Rotating AWS KMS keys
<a name="ile-key-rotation"></a>

AWS KMS supports automatic key rotation for customer managed keys. When you enable automatic key rotation, AWS KMS rotates the key every year, and the key ARN remains the same. These rotations are transparent to end users and clients and do not require any action or changes to be made by users.

### Unregistering AWS KMS keys
<a name="ile-unregister-keys"></a>

You can unregister an AWS KMS key when you no longer need it for encryption. Unregistering a key revokes the AWS KMS grant and removes the key reference from your domain.

**To unregister an AWS KMS key:**

```
POST _plugins/_opensearch_storage_encryption/_unregister_key
{
  "key_id": "arn:aws:kms:us-east-1:123456789012:key/12345678-1234-1234-1234-123456789012",
  "encryption_context": "department=engineering,environment=production"
}
```

If you registered the key with an encryption context, you must pass the same `encryption_context` when you unregister it.

**Important**  
Before unregistering a key, reindex or delete any indices encrypted with the key. If any index still uses the key, the request fails with a `409` error and the key stays registered.

**Warning**  
If you disable or delete an AWS KMS key that is still in use, you will not be able to access data encrypted with that key. OpenSearch Service cannot recover encrypted data if the key is lost or deleted.

## Manual snapshots
<a name="ile-manual-snapshots"></a>

Manual snapshots are stored in Amazon S3 repositories that you manage. When you create manual snapshots of encrypted indices:
+ Data is exported to your Amazon S3 bucket in unencrypted form (following standard OpenSearch snapshot behavior).
+ You should enable Amazon S3 server-side encryption on your snapshot repository bucket.
+ You can use Amazon S3-managed keys (SSE-S3) or AWS KMS keys (SSE-KMS) for Amazon S3 bucket encryption. This encryption is configured at the bucket level and is separate from the customer managed keys used for index-level encryption.

**To enable Amazon S3 encryption on your snapshot repository:**

```
PUT _snapshot/my-repository
{
  "type": "s3",
  "settings": {
    "bucket": "my-snapshot-bucket",
    "region": "us-east-1",
    "role_arn": "arn:aws:iam::123456789012:role/snapshot-role",
    "server_side_encryption": true
  }
}
```

## Monitoring off-heap encryption memory and scaling up
<a name="ile-monitoring"></a>

Index level encryption keeps recently accessed decrypted data in a dedicated off-heap memory pool on each data node. OpenSearch Service publishes the following metrics for this pool to CloudWatch under the `AWS/ES` namespace. Use these metrics to monitor memory pressure and decide when to scale. Each metric is emitted per data node (with a `NodeId` dimension) and as a domain-level aggregate. These metrics are emitted only on data nodes of domains running OpenSearch 3.3 or later with index level encryption enabled.


| Metric | Unit | Description | 
| --- | --- | --- | 
| IleDirectMemoryReserved | Kilobytes | The off-heap memory ceiling reserved on the node for the encryption pool. This is the upper bound the working set can grow into. | 
| IleDirectMemoryWorkingSetPercentage | Percent | The share of the reserved pool that is actively in use (the working set of decrypted data). This is the primary signal of memory pressure. | 
| IleDirectMemoryBlockReloadPercentage | Percent | The per-interval rate at which previously cached blocks had to be reloaded (decrypted again) because they were evicted from the pool. Sustained high values indicate the pool cannot hold the active working set. | 
| IleDirectMemoryCircuitBreakerTriggered | 0 or 1 | 1 when the pool's circuit breaker has tripped to protect the node from exhausting off-heap memory. While triggered, operations that would grow the pool may be rejected until pressure subsides. | 

**Reading the working set metric**
+ A low-to-moderate `IleDirectMemoryWorkingSetPercentage` means the active decrypted data fits comfortably within the reserved pool. No action is needed.
+ A consistently high `IleDirectMemoryWorkingSetPercentage` (approaching 100%) means the active data set is close to filling the reserved pool. This is the earliest indication that the node is approaching its off-heap memory limit.
+ When the working set stays high, watch `IleDirectMemoryBlockReloadPercentage`. A rising block-reload percentage means blocks are being evicted and then decrypted again (cache thrashing), which adds latency to search and indexing.
+ `IleDirectMemoryCircuitBreakerTriggered = 1` is the most severe signal: the pool has hit its limit and the node is actively shedding load to stay healthy.

**When and how to scale up**

Scale up when `IleDirectMemoryWorkingSetPercentage` is sustained near its ceiling, `IleDirectMemoryBlockReloadPercentage` is elevated, or `IleDirectMemoryCircuitBreakerTriggered` reaches `1`. To relieve the pressure:
+ **Scale vertically** — move to a larger instance type with more memory. The reserved off-heap pool scales with node memory, so a larger instance provides a larger encryption pool.
+ **Scale horizontally** — add more data nodes so shards, and their working sets, are distributed across more nodes, reducing the per-node pool demand.
+ Alarm on the domain-level `IleDirectMemoryWorkingSetPercentage` and `IleDirectMemoryCircuitBreakerTriggered` metrics so you are notified before sustained pressure affects query and indexing performance.

## Additional configuration required on fine-grained access control-enabled domains
<a name="ile-fgac-config"></a>

On fine-grained access control domains, invoking the `_plugins/_opensearch_storage_encryption/_register_key` and `_plugins/_opensearch_storage_encryption/_unregister_key` APIs requires the following three fine-grained access control permissions to be enabled on the roles mapped to the fine-grained access control user invoking the API.

**Note**  
Even on fine-grained access control domains, only SigV4-signed requests can invoke these two APIs, and the IAM user or role invoking this API needs to have the above-mentioned IAM permissions to access the AWS KMS keys.

### Available permissions
<a name="ile-fgac-permissions"></a>

The Storage Encryption plugin provides the following cluster-level permissions:
+ `opensearch_storage_encryption:register_key` - Register encryption keys
+ `opensearch_storage_encryption:unregister_key` - Unregister encryption keys
+ `cluster:admin/opensearch/storage_encryption/get_index_count_for_key` - Required for unregister. The unregister API uses it internally to check whether any index still uses the key. You can't call it directly. Without this permission, unregister fails with a `503` error.

### Configuration steps
<a name="ile-fgac-config-steps"></a>

#### Step 1: Create an action group
<a name="ile-fgac-action-group"></a>

Action groups bundle individual permissions for easier role management.

**Using OpenSearch Dashboards**
+ Navigate to **Security** → **Permissions** → **Action Groups**
+ Choose **Create action group**
+ Enter the following details:
  + **Action group name**: `storage_encryption_manage`
  + **Description**: Manage storage encryption keys
  + **Type**: Select **Cluster**
+ In the **Permissions** section, add the following permissions:
  + `opensearch_storage_encryption:register_key`
  + `opensearch_storage_encryption:unregister_key`
  + `cluster:admin/opensearch/storage_encryption/get_index_count_for_key`
+ Choose **Create**

**Using the Security API**

```
PUT /_plugins/_security/api/actiongroups/storage_encryption_manage
{
  "allowed_actions": [
    "opensearch_storage_encryption:register_key",
    "opensearch_storage_encryption:unregister_key",
    "cluster:admin/opensearch/storage_encryption/get_index_count_for_key"
  ],
  "type": "cluster",
  "description": "Manage storage encryption keys"
}
```

#### Step 2: Create a role
<a name="ile-fgac-create-role"></a>

Create a role that uses the action group.

**Using OpenSearch Dashboards**
+ Navigate to **Security** → **Roles**
+ Choose **Create role**
+ Enter the following details:
  + **Role name**: `storage_encryption_admin`
  + **Description**: Administrator role for storage encryption
+ In the **Cluster permissions** section:
  + Select `storage_encryption_manage` from the dropdown
+ Choose **Create**

**Using the Security API**

```
PUT /_plugins/_security/api/roles/storage_encryption_admin
{
  "cluster_permissions": [
    "storage_encryption_manage"
  ],
  "index_permissions": [],
  "description": "Administrator role for storage encryption"
}
```

#### Step 3: Map users to the role
<a name="ile-fgac-map-users"></a>

Assign the role to users or backend roles.

**Using OpenSearch Dashboards**
+ Navigate to **Security** → **Roles**
+ Find and click on `storage_encryption_admin`
+ Go to the **Mapped users** tab
+ Choose **Map users**
+ Add users or backend roles:
  + **Users**: Enter IAM user ARNs (e.g., `arn:aws:iam::123456789012:user/encryption-operator`)
  + **Backend roles**: Enter IAM role ARNs (e.g., `arn:aws:iam::123456789012:role/EncryptionAdminRole`)
+ Choose **Map**

**Using the Security API**

```
PUT /_plugins/_security/api/rolesmapping/storage_encryption_admin
{
  "users": [
    "arn:aws:iam::123456789012:user/encryption-operator"
  ],
  "backend_roles": [
    "arn:aws:iam::123456789012:role/EncryptionAdminRole",
    "arn:aws:iam::123456789012:role/EncryptionTeamRole"
  ]
}
```

## Monitoring and auditing
<a name="ile-monitoring-auditing"></a>

### AWS CloudTrail logging
<a name="ile-cloudtrail-logging"></a>

When you register a key, OpenSearch Service creates an AWS KMS grant on that key. AWS CloudTrail logs this as a `CreateGrant` event from `kms.amazonaws.com`. The grant's `encryptionContextSubset` constraint contains your domain ARN and any custom encryption context that you specified when you registered the key. The `_register_key` and `_unregister_key` calls themselves aren't logged as OpenSearch Service events. Only the resulting AWS KMS calls appear in AWS CloudTrail. You can use these AWS CloudTrail logs to audit encryption key lifecycle operations.

**Example CloudTrail log entry for key registration:**

```
{
  "eventVersion": "1.11",
  "userIdentity": {
    "type": "AWSService",
    "invokedBy": "aoss.opensearchservice.amazonaws.com"
  },
  "eventTime": "2025-01-15T10:30:00Z",
  "eventSource": "kms.amazonaws.com",
  "eventName": "CreateGrant",
  "awsRegion": "us-east-1",
  "sourceIPAddress": "aoss.opensearchservice.amazonaws.com",
  "userAgent": "aoss.opensearchservice.amazonaws.com",
  "requestParameters": {
    "keyId": "arn:aws:kms:us-east-1:123456789012:key/1234abcd-12ab-34cd-56ef-1234567890ab",
    "constraints": {
      "encryptionContextSubset": {
        "department": "engineering",
        "domainARN": "arn:aws:es:us-east-1:123456789012:domain/my-domain",
        "environment": "production"
      }
    },
    "granteePrincipal": "es.us-east-1.amazonaws.com",
    "retiringPrincipal": "es.us-east-1.amazonaws.com",
    "operations": [
      "Encrypt",
      "Decrypt",
      "GenerateDataKey",
      "GenerateDataKeyPairWithoutPlaintext",
      "ReEncryptFrom",
      "ReEncryptTo",
      "DescribeKey"
    ]
  },
  "responseElements": {
    "grantId": "0c237a1b2c3d4e5f60718293a4b5c6d7e8f90a1b2c3d4e5f60718293a4b5c6d7",
    "keyId": "arn:aws:kms:us-east-1:123456789012:key/1234abcd-12ab-34cd-56ef-1234567890ab"
  },
  "requestID": "f9f2c63e-c50f-4e70-8e23-ef8fea38cac7",
  "eventID": "a92a2f4f-ed11-38e5-8a0b-37df394ec2ec",
  "readOnly": false,
  "resources": [
    {
      "accountId": "AWS Internal",
      "type": "AWS::KMS::Key",
      "ARN": "arn:aws:kms:us-east-1:123456789012:key/1234abcd-12ab-34cd-56ef-1234567890ab"
    }
  ],
  "eventType": "AwsApiCall",
  "managementEvent": true,
  "recipientAccountId": "123456789012",
  "sharedEventID": "b1c2d3e4-5f60-4a7b-8c9d-0e1f2a3b4c5d",
  "eventCategory": "Management"
}
```

### AWS KMS metrics
<a name="ile-kms-metrics"></a>

AWS KMS doesn't publish separate request-count metrics for `GenerateDataKey` or `Decrypt`. To track AWS KMS usage in CloudWatch, use the `CallCount` metric in the `AWS/Usage` namespace with the resource `CryptographicOperationsSymmetric`. This metric counts all symmetric cryptographic operations together. For per-operation detail, use the AWS KMS events in AWS CloudTrail.

## Troubleshooting
<a name="ile-troubleshooting"></a>

### Understanding encrypted index creation responses
<a name="ile-index-creation-responses"></a>

When creating an encrypted index, the response indicates whether the operation was successful. This section explains how to interpret the response and resolve common issues.

**Successful index creation**

When an encrypted index is created successfully with a registered key, the response shows:

```
{
  "acknowledged": true,
  "shards_acknowledged": true,
  "index": "my-index"
}
```
+ `"acknowledged": true` - Index metadata was created
+ `"shards_acknowledged": true` - All primary shards were started successfully
+ Both values must be `true` for a fully successful operation.

**Failed index creation (KMS key unusable)**

If OpenSearch Service can't use the AWS KMS key, the request fails with a `400` error and no index is created. Common causes include:
+ The key isn't registered on the domain.
+ The `encryption_context` doesn't match the context used when the key was registered.
+ The key is disabled, deleted, or not accessible.

**Request:**

```
PUT /my-index
{
  "settings": {
    "index": {
      "store": {
        "type": "cryptofs",
        "crypto.key_provider": "aws-kms",
        "crypto.kms.key_arn": "arn:aws:kms:us-east-1:111122223333:key/abcd1234-5678-90ef-ghij-klmnopqrstuv",
        "crypto.kms.encryption_context": "Environment=Production,Application=Logging"
      }
    }
  }
}
```

**Response:**

```
{
  "error": {
    "root_cause": [
      {
        "type": "illegal_argument_exception",
        "reason": "KMS key unusable for index [my-index] setting [index.store.crypto.kms.key_arn]. Verify the KMS key is enabled and accessible."
      }
    ],
    "type": "illegal_argument_exception",
    "reason": "KMS key unusable for index [my-index] setting [index.store.crypto.kms.key_arn]. Verify the KMS key is enabled and accessible."
  },
  "status": 400
}
```

To resolve this error, register the key (see [Step 2: Register AWS KMS keys](#ile-register-keys)), confirm that `encryption_context` matches the registered context exactly, and confirm that the key is enabled. Then retry the request.

## Additional resources
<a name="ile-additional-resources"></a>
+ [Fine-grained access control in Amazon OpenSearch Service](fgac.md)
+ [Manual snapshots](#ile-manual-snapshots)
+ [AWS Key Management Service Developer Guide](https://docs.aws.amazon.com/kms/latest/developerguide/)
+ [Using grants in AWS KMS](https://docs.aws.amazon.com/kms/latest/developerguide/grants.html)
+ [OpenSearch Security documentation](https://opensearch.org/docs/latest/security/)

## Pricing
<a name="ile-pricing"></a>

Index level encryption is available at no additional cost. You pay only for:
+ Standard AWS KMS charges for API requests (GenerateDataKey, Decrypt operations)
+ Standard OpenSearch Service domain costs

For detailed AWS KMS pricing information, see [AWS KMS Pricing](https://aws.amazon.com/kms/pricing/).