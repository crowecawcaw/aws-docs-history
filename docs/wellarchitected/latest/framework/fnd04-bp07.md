

# FND04-BP07 Establish cross-Region replication and failover capabilities

 Cross-Region replication and failover are technical capabilities that workloads with high availability or disaster recovery requirements depend on. Without central patterns, workload teams design their own replication approaches and failover mechanisms. During the first real event, they discover that a critical item (a key, a route, a quota, or a piece of state) is missing from the secondary Region. A central foundation for replication and failover gives workload teams tested primitives so they can meet their resilience requirements without reinventing the mechanics. 

 **Desired outcome:** 
+  Your foundation team provides standard patterns for cross-Region replication of shared services and common data stores, published as reusable infrastructure-as-code modules. 
+  Your critical shared services (identity, DNS, key management, central logging) are available in a secondary Region so that workload failover does not depend on the primary Region being reachable. 
+  Your failover controls are managed centrally through Amazon Application Recovery Controller (ARC) or equivalent, so that the organization has a single place to initiate and audit Region failovers. 
+  Your workload teams have clear guidance on which replication pattern fits which data tier, and they inherit the underlying infrastructure (multi-Region keys, cross-Region networking, DNS failover) rather than building it. 
+  Your cross-Region capability is exercised regularly so that the secondary Region actually works when it is needed. 

 **Common anti-patterns:** 
+  Designing cross-Region replication per workload with no central pattern, so each team makes different trade-offs and the organization has no shared path for failover. 
+  Running shared services (identity, DNS, KMS keys, central logging) only in the primary Region, so every workload's disaster recovery plan depends on a Region that by definition is degraded. 
+  DR is defaulted to copying data to another Region without planning for control-plane dependencies: how the failover is triggered, how DNS cuts over, how secrets and certificates are accessible in the target Region. 
+  Using separate KMS keys per Region and relying on custom re-encryption during replication, then discovering during a failover that data in the target Region is unreadable. 
+  Never exercising the secondary Region, so the first real failover is the one that has to work. 
+  Failing to size service quotas in the secondary Region for the failover load, so the target Region cannot absorb production traffic when the cut-over happens. 

 **Benefits of establishing this best practice:** 
+  Faster and more reliable failover because shared services and replication patterns are already in place and exercised rather than assembled during an incident. 
+  Fewer failed failovers because the common failure modes (missing keys, missing routes, missing DNS entries, missing quotas) are handled at the foundation level once rather than repeatedly at the workload level. 
+  Consistent replication posture across the organization because workload teams consume the same well-understood patterns. 
+  Lower operational cost because multi-Region keys, shared networking, and central failover controls are built once and reused. 
+  Clearer audit and compliance position because failover controls and replication status are visible from a central location. 

 **Level of risk exposed if this best practice is not established:** Medium 

## Implementation guidance
<a name="implementation-guidance"></a>

 Cross-Region capability is difficult because of data-related aspects, such as the keys that encrypt the data, the DNS that points to it, the identity that accesses it, the network that connects it, the secrets and certificates the application depends on, and the control plane that triggers the failover. When a workload team designs cross-Region in isolation, they usually solve the data problem and discover the control-plane and dependency problems during the first exercise. 

 A central foundation for replication and failover deploys shared services in multiple Regions so that failover is not conditional on the primary Region's availability. Standard patterns are published so that workload teams consume tested building blocks rather than building from scratch. The control-plane concerns (how failover is initiated, audited, and coordinated across workloads) are handled through a central service rather than per-workload scripts. 

 At a minimum, every service that workloads depend on must be reachable from the secondary Region. [IAM Identity Center](https://aws.amazon.com/iam/identity-center/) supports automatic replication to a secondary Region, [Amazon Route 53](https://aws.amazon.com/route53/) is a global service, [AWS KMS multi-Region keys](https://docs.aws.amazon.com/kms/latest/developerguide/multi-region-keys-overview.html) replicate to secondary Regions, and central logging must flow to destinations reachable from the secondary Region. If any of these services depend on the primary Region, every workload's DR plan inherits that dependency. 

 Publish standard data replication patterns for the common data stores workload teams use: [S3 Cross-Region Replication](https://docs.aws.amazon.com/AmazonS3/latest/userguide/replication.html) for object storage, [DynamoDB Global Tables](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/GlobalTables.html) for active-active key-value, [Aurora Global Database](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-global-database.html) for active-passive or active-active relational, and [AWS Backup cross-Region copies](https://docs.aws.amazon.com/aws-backup/latest/devguide/cross-region-backup.html) for point-in-time restore. Publish these as reusable modules. Workload teams select the pattern that fits each data store. 

 [Amazon Application Recovery Controller (ARC)](https://aws.amazon.com/application-recovery-controller/) provides routing controls and Region switch plans that survive Region impairment, so you can execute failover even when the primary Region is unreachable. Adopt ARC when your organization exercises Region failover regularly. Otherwise, start with Route 53 failover routing and documented runbooks, and move to ARC as practice builds. 

 Identity, keys, network connectivity, secrets, certificates, and service quotas all need to be valid in the target Region when failover happens. Establish a dependency checklist that workload teams work through during readiness reviews, and verify each item during exercises. A single missing item can prevent failover: a certificate not issued for the failover domain, a secret not replicated, or a Direct Connect gateway that reaches only the primary Region. 

 Schedule exercises regularly, rotate which workloads participate, and capture the findings. Route foundation-level findings back into the shared patterns, and workload-level findings to the workload team. 

**Important**  
 Exercise the secondary Region at least as often as you update the primary. Treat unexercised DR as a known risk. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Define shared services Region strategy:** Identify the shared services every workload depends on and document which Regions each service is deployed in. At a minimum, confirm presence in the primary and designated DR Regions for identity (IAM Identity Center), DNS, central logging destinations, KMS keys, network transit (Transit Gateway or equivalent), and secrets and certificates. Document the Region strategy and review it when new shared services are introduced. 

1.  **Deploy identity and central security services to secondary Regions:** Configure [IAM Identity Center automatic Region replication](https://docs.aws.amazon.com/singlesignon/latest/userguide/) to designated DR Regions. Verify that Security Hub CSPM, GuardDuty, and central logging destinations are available in the secondary Region so workload failover does not lose visibility at the moment it is most needed. 

1.  **Enable multi-Region KMS keys for replicated data:** For workloads that will replicate data across Regions, use [multi-Region KMS keys](https://docs.aws.amazon.com/kms/latest/developerguide/multi-region-keys-overview.html) instead of separate per-Region keys. Refer to your encryption and key management standards for the policies that govern multi-Region key ownership and grant patterns. Publish multi-Region key creation as a standard pattern workload teams consume. 

1.  **Publish replication patterns for common data stores:** Create reusable infrastructure-as-code modules for the replication patterns the organization supports: [S3 Cross-Region Replication](https://docs.aws.amazon.com/AmazonS3/latest/userguide/replication.html), [DynamoDB Global Tables](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/GlobalTables.html), [Aurora Global Database](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-global-database.html), and [AWS Backup cross-Region copies](https://docs.aws.amazon.com/aws-backup/latest/devguide/cross-region-backup.html). Include the networking, IAM, and key dependencies in each module so that workload teams consume a complete replication capability rather than assembling one. 

1.  **Deploy Amazon Application Recovery Controller for critical workloads:** For workloads with strict RTO requirements, configure [Amazon Application Recovery Controller](https://docs.aws.amazon.com/r53recovery/latest/dg/) with routing controls and [Region switch](https://docs.aws.amazon.com/r53recovery/latest/dg/region-switch.html) plans. With ARC, the organization can exercise and invoke Region failovers from a control plane that survives Region impairment. For less critical workloads, Route 53 failover routing with documented runbooks is an acceptable starting point. 

1.  **Size secondary Region quotas for failover traffic:** Quotas in the secondary Region default to low values because the Region usually carries resting-state workloads. Size quotas in the secondary Region to the expected failover load, not the resting load. This aligns with the quota management practice and prevents a common failover failure mode. 

1.  **Replicate secrets and certificates to secondary Regions:** Configure [AWS Secrets Manager secret replication](https://docs.aws.amazon.com/secretsmanager/latest/userguide/replicate-secrets.html) for secrets that workloads need during failover. Issue [AWS Certificate Manager](https://docs.aws.amazon.com/acm/latest/userguide/acm-overview.html) certificates in both Regions where required, or use certificates with subject alternative names that cover both Region-specific hostnames. Verify that the failover path does not depend on credentials or certificates that exist only in the primary Region. 

1.  **Publish a dependency checklist for workload readiness:** Create a checklist workload teams use during design and readiness reviews: identity federation in the secondary Region, multi-Region keys for replicated data, secrets replicated, certificates valid, DNS records prepared, quotas sized, network paths in place. Include the checklist in your workload onboarding process so that gaps are caught before they become incidents. 

1.  **Exercise cross-Region failover regularly:** Schedule Region failover exercises with rotating workload teams. Each exercise covers the full path: invoking failover, validating traffic in the secondary Region, validating data consistency, and cutting back. Capture findings, classify them as foundation or workload gaps, and feed the foundation findings back into the shared patterns. Track which workloads have been exercised and when, so that unexercised workloads are visible as a known risk. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [FND04-BP06 Establish centralized backup standards and mechanisms](fnd04-bp06.md) 
+  [FND04-BP08 Establish resilience testing tooling](fnd04-bp08.md) 
+  [FND07-BP01 Define your network and connectivity strategy and centralized resources](fnd07-bp01.md) 
+  [FND07-BP03 Establish centralized DNS management](fnd07-bp03.md) 
+  [REL10-BP01 Deploy the workload to multiple locations](rel10-bp01.md) 
+  [REL13-BP02 Use defined recovery strategies to meet the recovery objectives](rel13-bp02.md) 

 **Related documents:** 
+  [Amazon Application Recovery Controller](https://docs.aws.amazon.com/r53recovery/latest/dg/) 
+  [Multi-Region keys in AWS KMS](https://docs.aws.amazon.com/kms/latest/developerguide/multi-region-keys-overview.html) 
+  [AWS Backup cross-Region backup](https://docs.aws.amazon.com/aws-backup/latest/devguide/cross-region-backup.html) 
+  [DynamoDB Global Tables](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/GlobalTables.html) 
+  [Aurora Global Database](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-global-database.html) 
+  [IAM Identity Center automatic Region replication](https://docs.aws.amazon.com/singlesignon/latest/userguide/) 
+  [AWS Multi-Region Fundamentals](https://docs.aws.amazon.com/prescriptive-guidance/latest/aws-multi-region-fundamentals/) 

 **Related examples:** 
+  [Creating disaster recovery mechanisms using Amazon Route 53](https://aws.amazon.com/blogs/networking-and-content-delivery/creating-disaster-recovery-mechanisms-using-amazon-route-53/) 
+  [Building a multi-Region serverless application](https://aws.amazon.com/blogs/compute/building-resilient-multi-region-serverless-applications-on-aws/) 

 **Related services:** 
+  [Amazon Application Recovery Controller](https://aws.amazon.com/application-recovery-controller/) 
+  [AWS Elastic Disaster Recovery](https://aws.amazon.com/disaster-recovery/) 