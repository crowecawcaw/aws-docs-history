

# FND05-BP11 Establish encryption and key management standards

 Encryption and key management are foundation services that every workload consumes. Without a central standard, each team decides where keys are stored, who can use them, how they rotate, and how they are shared across accounts. The result is fragmented key ownership, inconsistent rotation, and surprise lockouts when one account deletes a key that another account's workloads depend on. A central encryption foundation gives workload teams reliable primitives, so they do not design key management themselves. 

 **Desired outcome:** 
+  Your organization has a standard for which keys are customer-managed, which are AWS-managed, and who owns each customer-managed key. 
+  Your foundation team provides shared encryption keys for common patterns (central logging, shared services, cross-account replication) through AWS Key Management Service (KMS) with documented cross-account policies. 
+  Your critical workloads use multi-Region keys where required for failover without the operational cost of replicating data under different keys. 
+  Your key rotation, grant lifecycle, and cross-account sharing follow documented patterns that workload teams adopt rather than invent. 
+  Your secrets and certificates are managed through central services (AWS Secrets Manager, AWS Certificate Manager, AWS Private CA) rather than one-off key-value stores or self-signed certificates scattered across accounts. 

 **Common anti-patterns:** 
+  Each workload creating its own customer-managed keys with no central visibility into who owns them or what they protect. 
+  Relying entirely on AWS-managed keys even for data where the organization needs control over who can decrypt it. 
+  Rotating keys manually on one-time schedules that drift over time, leaving some keys rotating every 90 days and others never rotating at all. 
+  Creating separate keys per Region for workloads that need to replicate data across Regions, then building custom re-encryption workflows when data moves. 
+  Storing secrets in environment variables, container images, or configuration files instead of in AWS Secrets Manager, so credential rotation requires application redeployment. 
+  Issuing TLS certificates per workload team with no central authority, leading to inconsistent chain-of-trust and expired certificates that go unnoticed. 

 **Benefits of establishing this best practice:** 
+  Consistent encryption posture across the organization because every workload inherits the same central standards for key ownership, rotation, and access. 
+  Reduced operational effort for workload teams because shared keys for common patterns are provided rather than built. 
+  Clearer compliance demonstration because a central key inventory maps keys to workloads, data classifications, and rotation status. 
+  Fewer failure modes during cross-Region replication and disaster recovery because multi-Region keys replace custom re-encryption workflows. 
+  Lower credential exposure risk because secrets and certificates flow through services with rotation and access control built in. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 Encryption involves decisions about key ownership, lifecycle, sharing, and integration with the services that use it. When each workload team makes these decisions independently, the organization accumulates customer-managed keys with no central record, inconsistent rotation policies, and key policies that are either too permissive or too restrictive. You pay these costs later, when auditors ask for a key inventory, when a cross-account failover fails because the target account cannot decrypt the data, or when a team deletes a key that another workload references. 

 The foundation team's role is to establish central encryption primitives and publish the patterns workload teams consume. Workload teams still own the keys that protect workload-specific data. The organization sets a shared standard for which keys belong where, how they are named and tagged, how they rotate, and how they are shared across accounts. 

 Keys that protect organization-wide infrastructure (central logging, shared services, cross-account replication, AWS Organizations-wide backup) belong to the foundation or security team, typically in a dedicated key management account. Keys that protect workload-specific data belong to the workload team, in the account that owns the workload. Document the split explicitly so every key has a named owner. 

 [AWS-managed keys](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#aws-managed-cmk) carry no additional charge and require no management, but you cannot control who can decrypt the data beyond the service-level trust boundary. Customer-managed keys add cost and operational overhead but let you revoke access, rotate independently, and apply custom key policies. Use customer-managed keys for sensitive data where access control matters (regulated data, secrets, cross-account replicated data), and AWS-managed keys where the additional control is not needed. 

 Multi-Region keys are the right pattern for data that replicates across Regions. Without them, each Region has its own key and data replicated across Regions has to be re-encrypted at the boundary. [Multi-Region KMS keys](https://docs.aws.amazon.com/kms/latest/developerguide/multi-region-keys-overview.html) share the same key material across Regions, so encrypted data remains decryptable in the target Region without custom workflows. Use them for disaster recovery and for services such as S3 Cross-Region Replication, DynamoDB Global Tables, and Aurora Global Database. 

 Automate rotation wherever KMS supports it. [Automatic key rotation](https://docs.aws.amazon.com/kms/latest/developerguide/rotate-keys.html) rotates the key material annually (or on a configurable cadence) without changing the key ARN, so workloads using the key are unaffected. For keys in services that do not support automatic rotation, establish a documented rotation procedure and schedule. 

 The log archive account's CloudTrail key must be usable by every member account, the shared services account's secrets must be decryptable by workload accounts, and the backup vault key must be usable by the AWS Backup service across accounts. Key policies and grants are the mechanisms, but they need discipline: trust policies scoped too broadly remove the value of using a customer-managed key. Scope cross-account permissions to specific principals or roles, not to the root account. 

 [AWS Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/intro.html) stores and rotates secrets with integrations for databases and common services. [AWS Certificate Manager](https://docs.aws.amazon.com/acm/latest/userguide/acm-overview.html) issues and renews public TLS certificates for AWS services automatically. [AWS Private CA](https://docs.aws.amazon.com/privateca/latest/userguide/PcaWelcome.html) provides a private certificate authority for internal TLS, which avoids self-signed certificates scattered across workloads. Share these services centrally so workload teams consume certificates and secrets without designing the service themselves. Replicate Secrets Manager secrets to workload accounts, share ACM certificates through AWS Resource Access Manager, and distribute Private CA hierarchies to workload accounts. 

**Important**  
 Deleting a KMS key is irreversible after the pending deletion window closes, and any data encrypted with it becomes unrecoverable. Treat KMS key deletion as a high-risk operation with approval gates, and prefer disabling keys over deleting them until you are certain no data depends on them. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Establish a key ownership model:** Document which keys belong to the foundation team and which belong to workload teams, and publish the naming and tagging standard for customer-managed keys. At minimum, tag each key with its owner, the data classification it protects, and the workload or system that depends on it. This is the foundation for the key inventory that every later step consumes. 

1.  **Deploy central keys for shared infrastructure:** Provision customer-managed [AWS KMS](https://aws.amazon.com/kms/) keys for central logging (CloudTrail, VPC Flow Logs, Config), the log archive account, the security tooling account, and other shared services. Keys owned by the foundation team live in a dedicated key management account (or in the relevant shared services account) and are shared to member accounts through explicit [key policies](https://docs.aws.amazon.com/kms/latest/developerguide/key-policies.html) and [grants](https://docs.aws.amazon.com/kms/latest/developerguide/grants.html). 

1.  **Configure multi-Region keys for replicating data:** For workloads that replicate data across Regions (S3 Cross-Region Replication, DynamoDB Global Tables, Aurora Global Database, AWS Backup cross-Region copies), use [multi-Region keys](https://docs.aws.amazon.com/kms/latest/developerguide/multi-region-keys-overview.html). Create the primary key in the primary Region and replicate it to secondary Regions rather than creating separate keys per Region. 

1.  **Enable automatic key rotation:** Turn on [automatic rotation](https://docs.aws.amazon.com/kms/latest/developerguide/rotate-keys.html) on all customer-managed keys where it is supported. Review and document the rotation cadence in your key standards. Annually is the default, but regulated workloads might require shorter intervals. For keys that do not support automatic rotation, establish a manual rotation procedure and schedule it in your operational calendar. 

1.  **Publish cross-account sharing patterns:** Document the standard key policy templates for common cross-account scenarios: log archive account receiving logs from member accounts, shared services account providing secrets to workload accounts, backup vault keys used by AWS Backup across accounts, and customer-managed keys shared with partner accounts. Scope principals to specific roles, not to the root account, and include the AWS Organizations principal condition (aws:PrincipalOrgID) to contain trust within the organization. 

1.  **Centralize secret and certificate management:** Deploy [AWS Secrets Manager](https://aws.amazon.com/secrets-manager/) as the standard for application secrets, with automatic rotation enabled for supported database and service credentials. For shared secrets, use [cross-account secret access](https://docs.aws.amazon.com/secretsmanager/latest/userguide/auth-and-access_examples_cross.html) or [Secrets Manager replication](https://docs.aws.amazon.com/secretsmanager/latest/userguide/replicate-secrets.html). Use [AWS Certificate Manager](https://aws.amazon.com/certificate-manager/) for public TLS certificates on AWS services, and deploy [AWS Private CA](https://aws.amazon.com/private-ca/) with a shared private CA hierarchy for internal TLS needs. 

1.  **Build a central key inventory:** Use [AWS Config](https://aws.amazon.com/config/) aggregators to build an organization-wide view of KMS keys, their configuration, and their usage. Pair this with tag-based queries to identify keys missing owner or data-classification tags, keys without rotation enabled, and keys with overly permissive policies. Use the inventory to drive remediation campaigns and as the source of truth for compliance reporting. 

1.  **Detect and alert on risky key events:** Create [Amazon EventBridge](https://aws.amazon.com/eventbridge/) rules on CloudTrail events for high-risk KMS operations such as ScheduleKeyDeletion, DisableKey, and PutKeyPolicy with broadening changes. Route alerts to the security team so a key deletion or policy change cannot go unnoticed. Configure [AWS Config rules](https://docs.aws.amazon.com/config/latest/developerguide/managed-rules-by-aws-config.html) such as kms-cmk-not-scheduled-for-deletion and cmk-backing-key-rotation-enabled to flag drift from the standard. 

1.  **Exercise cross-account decryption in recovery tests:** Include cross-account encryption paths in disaster recovery and game-day exercises. Verify that a workload account can decrypt data that was replicated from a source account, that backup restoration works end-to-end with the keys it depends on, and that secrets and certificates remain accessible during failover. Gaps discovered during tests are much less costly than gaps discovered during real incidents. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [SEC08-BP01 Implement secure key management](sec08-bp01.md) 
+  [SEC09-BP02 Enforce encryption in transit](sec09-bp02.md) 
+  [FND02-BP08 Audit and rotate credentials periodically](fnd02-bp08.md) 
+  [FND05-BP03 Configure audit logging of cloud operations](fnd05-bp03.md) 
+  [FND05-BP09 Establish security tooling for investigating incidents](fnd05-bp09.md) 

 **Related documents:** 
+  [AWS KMS Developer Guide](https://docs.aws.amazon.com/kms/latest/developerguide/overview.html) 
+  [Multi-Region keys in AWS KMS](https://docs.aws.amazon.com/kms/latest/developerguide/multi-region-keys-overview.html) 
+  [Key policies in AWS KMS](https://docs.aws.amazon.com/kms/latest/developerguide/key-policies.html) 
+  [Rotating AWS KMS keys](https://docs.aws.amazon.com/kms/latest/developerguide/rotate-keys.html) 
+  [AWS Secrets Manager User Guide](https://docs.aws.amazon.com/secretsmanager/latest/userguide/intro.html) 
+  [AWS Certificate Manager User Guide](https://docs.aws.amazon.com/acm/latest/userguide/acm-overview.html) 
+  [AWS Private CA User Guide](https://docs.aws.amazon.com/privateca/latest/userguide/PcaWelcome.html) 
+  [AWS Security Reference Architecture](https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture/security-tooling.html) 

 **Related examples:** 
+  [How to deploy an Amazon KMS multi-Region key for disaster recovery](https://aws.amazon.com/blogs/security/encrypt-global-data-client-side-with-aws-kms-multi-region-keys/) 
+  [Share Secrets Manager secrets across AWS accounts](https://aws.amazon.com/blogs/security/how-to-access-secrets-across-aws-accounts-by-attaching-resource-based-policies/) 

 **Related services:** 
+  [AWS Key Management Service (KMS)](https://aws.amazon.com/kms/) 
+  [AWS Secrets Manager](https://aws.amazon.com/secrets-manager/) 
+  [AWS Certificate Manager](https://aws.amazon.com/certificate-manager/) 
+  [AWS Private CA](https://aws.amazon.com/private-ca/) 