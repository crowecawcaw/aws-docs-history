

# DSREL03-BP01 Design workloads for greater interoperability and portability
<a name="dsrel03-bp01"></a>

 Design workloads so they can be deployed, migrated, or recovered within or across jurisdictions when conditions require. Abstract Region-specific, service-specific dependencies. Use standards-based storage formats, data formats, table formats, and protocols. Plan ahead for data export and migration scenarios. 

 **Desired outcome:** 
+  Workloads can be deployed to a different AWS Region or to another customer-managed environment in approved jurisdictions with minimal rework. 
+  Region-specific, service-specific dependencies are abstracted, data can be exported in standard formats, and the effort required to port a workload is understood and documented. 

 **Common anti-patterns:** 
+  Not knowing what your interoperability and portability goals are, including which operating Regions, environments, or jurisdictions to target. 
+  Treating interoperability and portability as an afterthought rather than a design consideration, resulting in architectures that are expensive to restructure when jurisdictional requirements change. 
+  Hard-coding Region-specific resources (for example, AMI IDs, ARNs, and endpoints) in application code or infrastructure templates, creating dependencies that block deployment to other Regions. 
+  Using proprietary data formats without evaluating standards-based alternatives, increasing the cost and complexity of migration. 
+  Not planning for data export scenarios, leaving organizations unable to extract data in usable formats when required by regulation or business need. 

 **Benefits of establishing this best practice:** 
+  Reduced time and cost to deploy workloads in new AWS Regions or jurisdictions when conditions change. 
+  Greater flexibility to respond to emerging sovereignty regulations that might mandate specific infrastructure choices or data residency requirements. 
+  Reduced vendor dependency risk by maintaining the ability to migrate critical workloads to alternative environments if required. 
+  Improved disaster recovery options by enabling failover to Regions in different jurisdictions when same-jurisdiction recovery isn't feasible. 

 **Level of risk exposed if this best practice is not established:** Medium 

## Implementation guidance
<a name="implementation-guidance"></a>

 Achieving workload interoperability and portability demands intentional architectural decisions, each carrying trade-offs in complexity, operational overhead, and delivery timelines that must be evaluated against your specific risk profile and business objectives. 

**Note**  
 : Although interoperability and portability sound similar, they address different concerns. In the context of this best practice, *Portability* refers to how easily you can move a workload and its data from one environment to another. *Interoperability* focuses on how many code changes are needed for the workload to function after the move. 

 Consider the following: 
+  How should application logic be decoupled from Region-specific and service-specific dependencies? How should environment-level configuration and runtime bindings be abstracted? 
+  Which standards-based formats should be adopted for file storage, data serialization, messaging, and network protocols? 
+  Which application packaging and machine image formats should be used to maximize deployment flexibility? 
+  How will interoperability and portability be verified and continuously validated as workloads evolve? 

 These decisions involve real trade-offs. Every abstraction layer has the potential to increase code complexity, introduce performance overhead, or constrain access to provider-specific functionality if not designed with care. It is also common for abstraction layers to accumulate over time, compounding complexity without proportional benefit. An abstraction introduced to mitigate a risk identified five years ago might no longer be justified. The underlying risk profile might have fundamentally changed. Periodically reassessing the value of existing abstractions is as important as introducing new ones. 

 Begin by clearly identifying the specific business risks driving your decisions. 
+  **Operational resilience:** Organizations exposed to international trade policy changes, regional disruptions, or natural disasters often adopt interoperability and portability as core design principles. This approach broadens deployment flexibility, enabling workloads to span multiple AWS Regions or other customer-managed infrastructure, reducing single points of failure and strengthening continuity of operations. 
+  **Licensing and commercial terms:** Changes to licensing terms, pricing models, or usage entitlements can affect workload economics and operational continuity. Architecting with open standards and portable interfaces widens the range of available options if commercial terms change. 
+  **Technology obsolescence and migration risk:** Tight coupling to proprietary formats creates long-term technical debt. If those dependencies are deprecated, undergo breaking changes, or fall behind evolving requirements, organizations face disruptive and high-cost migration paths. Designing for interoperability through abstraction layers, standard protocols, and open data specification enables incremental technology evolution and protects long-term return on investment. 

 Each of these risks has a distinct impact on your digital sovereignty posture and demands a tailored mitigation strategy. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Abstract Region-specific and service-specific dependencies:** Separate environment-specific configuration from application logic. Use [AWS Systems Manager Parameter Store](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-parameter-store.html) or [AWS Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/intro.html) for Region-specific settings (endpoints, ARNs, and encryption key IDs). Define infrastructure using [AWS CloudFormation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html) or [AWS CDK](https://docs.aws.amazon.com/cdk/v2/guide/home.html) with parameterized Region configurations so templates can be deployed to any approved AWS Region without modification. 

    When portability to environments outside AWS Cloud is a requirement, abstract service-specific dependencies. Wrap AWS service interactions behind interfaces that can be swapped for alternative implementations. 

1.  **Evaluate standards alignment:** Where practical, use standards-based storage, data, message, and protocol formats to widen interoperability and portability options. Consider the following: 
   +  Open and standards-based data formats (Parquet, ORC, JSON, and CSV) rather than proprietary formats where only a single vendor provides encoders/decoders. 
   +  Standard protocols and APIs (HTTP, REST, and GraphQL) rather than proprietary interfaces. 
   +  Open source aligned databases and analytics engines (for example, [Amazon Aurora](https://aws.amazon.com/rds/aurora/), [Amazon OpenSearch Service](https://aws.amazon.com/opensearch-service/), and [Amazon ElastiCache (Redis OSS) OSS](https://aws.amazon.com/elasticache/redis/)) rather than legacy proprietary database engines. 
   +  Container orchestration with [Amazon EKS](https://aws.amazon.com/eks/) (Kubernetes) for workloads that might need to run on other Kubernetes-compatible infrastructure, including [Amazon EKS Hybrid Nodes](https://docs.aws.amazon.com/eks/latest/userguide/hybrid-nodes-overview.html), [AWS Outposts](https://aws.amazon.com/outposts/), or third-party environments. 

    AWS services across analytics, storage, data integration, and machine learning support open data and open table formats. AWS services are accessible through standard REST APIs over HTTPS, and purpose-built services such as [Amazon API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/welcome.html) and [AWS AppSync](https://docs.aws.amazon.com/appsync/latest/devguide/what-is-appsync.html) enable organizations to expose their own workloads through RESTful and GraphQL interfaces with built-in support for OpenAPI, OAuth 2.0, and OpenID Connect. This means you retain full control over your data and can move, replicate, or process it using any toolchain that supports these widely adopted open standards. 

    When selecting your technology stack, you might need to carefully evaluate the trade-off between portability and the operational benefits of using managed services. For example, you can install and manage your own version of an open source database engine on an Amazon EC2 cluster, but does this improve operational resilience or reduce licensing risks? AWS services such as [Aurora MySQL](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.AuroraMySQL.html), [Aurora PostgreSQL](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.AuroraPostgreSQL.html), [Aurora PostgreSQL Limitless Database](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/limitless.html), and [Aurora Serverless v2](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-serverless-v2.html) provide the best of both. They offer [open source compatibility](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/CHAP_AuroraOverview.html) with reduced operational overhead by automating time-consuming administration tasks like hardware provisioning, database setup, patching, and backups while providing security, availability, and reliability of commercial databases. 

1.  **Plan for data export and migration:** Document how data can be extracted from each critical workload in standard formats. For each data store, document: 
   +  Export format and tooling (for example, [AWS Database Migration Service](https://aws.amazon.com/dms/) for database migration, and S3 export for object storage) 
   +  Estimated data volume and transfer time 
   +  Encryption key dependencies: can the data be decrypted and re-encrypted with keys in the target jurisdiction? 
   +  Regulatory constraints on data transfer (data residency requirements and transfer impact assessments) 

    Review your cloud service provider's data center exit policies and the tools available for data migration. AWS provides [free data transfer out](https://aws.amazon.com/blogs/aws/free-data-transfer-out-to-internet-when-moving-out-of-aws/) for customers leaving AWS. 

1.  **Test for interoperability and portability:** Periodically deploy your workload to a different approved AWS Region or another approved jurisdiction to verify interoperability and portability. Use [AWS CloudFormation StackSets](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/what-is-cfnstacksets.html) to deploy infrastructure across multiple AWS Regions from a single template, and run identical test suites in each environment to verify consistent functionality. Document the effort, issues encountered, and any Region-specific and service-specific adjustments required. This testing validates your portability assumptions and identifies hidden dependencies before they become urgent during an actual migration. 

1.  **Assess and document portability posture:** For each critical workload, document: 
   +  Portability tier (high, medium, or low) based on the effort required to deploy in a new jurisdiction 
   +  Region-specific and service-specific dependencies that might need to change or require alternative implementations 
   +  Estimated migration timeline and cost 
   +  Regulatory prerequisites for migration (data transfer approvals and new certifications) 

    Review this assessment regularly or when significant architectural changes are made. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [REL13-BP02 Use defined recovery strategies to meet the recovery objectives](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/rel_planning_for_recovery_disaster_recovery.html) 
+  [REL13-BP04 Manage configuration drift at the DR site or Region](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/rel_planning_for_recovery_config_drift.html) 
+  [DRHCOPS03-BP02 Understand factors that determine your data replication strategy](https://docs.aws.amazon.com/wellarchitected/latest/data-residency-hybrid-cloud-services-lens/drhcops03-bp02.html) 

 **Related documents:** 
+  [AWS Disaster Recovery Documentation](https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/disaster-recovery-workloads-on-aws.html) 
+  [Free data transfer out to internet when moving out of AWS](https://aws.amazon.com/blogs/aws/free-data-transfer-out-to-internet-when-moving-out-of-aws/) 
+  [AWS designated as a critical third-party provider under EU's DORA regulation](https://aws.amazon.com/blogs/security/aws-designated-as-a-critical-third-party-provider-under-eus-dora-regulation/) 

 **Related videos:** 
+  [AWS re:Invent 2025 - Digital sovereignty and data residency with AWS Hybrid and Edge services (HMC310)](https://www.youtube.com/watch?v=CxkRvW42Hgc) 
+  [AWS re:Invent 2025 - Architecting resilient multicloud operations, feat. Monzo Bank (HMC201)](https://www.youtube.com/watch?v=oDroYE4unmY) 

 **Related services:** 
+  [AWS CloudFormation](https://aws.amazon.com/cloudformation/) 
+  [AWS CDK](https://aws.amazon.com/cdk/) 
+  [Amazon EKS](https://aws.amazon.com/eks/) 
+  [AWS Outposts](https://aws.amazon.com/outposts/) 
+  [AWS Database Migration Service](https://aws.amazon.com/dms/) 
+  [AWS Systems Manager](https://aws.amazon.com/systems-manager/) 
+  [AWS Secrets Manager](https://aws.amazon.com/secrets-manager/) 
+  [Amazon S3](https://aws.amazon.com/s3/) 