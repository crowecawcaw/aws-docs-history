

# DSREL01-BP02 Select and operationalize sovereignty-compliant recovery sites
<a name="dsrel01-bp02"></a>

 Select and configure recovery sites that maintain data residency and regulatory compliance throughout the recovery process. Recovery procedures must not move data outside approved jurisdictions, even temporarily. Automate recovery using infrastructure as code, test regularly, and train teams to operate under time pressure while maintaining compliance. 

 **Desired outcome:** 
+  Recovery sites preserve data residency and regulatory adherence during both normal operations and failover scenarios. 
+  Recovery procedures are automated, tested, and documented. 
+  Teams can restore critical workloads within defined recovery time objectives (RTOs) and recovery point objectives (RPOs). 

 **Common anti-patterns:** 
+  Replicating data to recovery sites without first classifying data by sensitivity and residency requirements, or verifying that the target Region is within an approved jurisdiction. 
+  Relying on manual, untested recovery procedures instead of automated, validated processes that maintain compliance throughout the recovery path. 
+  Training only specific individuals on recovery procedures, creating single points of failure and knowledge bottlenecks during incidents. 
+  Assuming automated recovery mechanisms work in every scenario without maintaining contingency procedures for critical operations. 

 **Benefits of establishing this best practice:** 
+  Data and workloads remain within approved jurisdictions throughout recovery, maintaining regulatory adherence even during disruptions. 
+  Automated, tested recovery procedures reduce downtime and human error while achieving defined RTOs and RPOs consistently. 
+  Regular testing and cross-training build team confidence and identify weaknesses before actual incidents occur. 
+  Clear documentation and compliance checks at each recovery stage support audit readiness and demonstrate due diligence. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 Sovereignty-compliant recovery site selection begins with understanding which data privacy legislations and cybersecurity standards apply to your workloads, where data can legally reside, and where operational recovery teams are located. Cross-functional alignment between IT, legal, compliance, and business stakeholders establishes clear policies for cross-border data movement during recovery scenarios and defines minimum service levels for each workload. Without this classification and alignment, recovery architectures risk violating residency constraints at the exact moment compliance is most scrutinized. 

 Recovery procedures must document full recovery timelines and communication plans for every stage until full restoration is achieved. A recovery path that introduces compliance issues, even temporarily, undermines the purpose of sovereignty controls. 

 AWS infrastructure provides several architectural properties and managed services that support sovereignty-compliant recovery: 
+  AWS Regions consist of multiple [Availability Zones](https://docs.aws.amazon.com/global-infrastructure/latest/regions/aws-regions.html) with independent power, cooling, and networking. Your workloads inherit this isolation. 
+  AWS services are designed for [static stability](https://docs.aws.amazon.com/whitepapers/latest/aws-fault-isolation-boundaries/static-stability.html). Data plane operations (serving requests, reading data, and running compute) continue even when control plane operations (creating resources and modifying configurations) are impaired. For sovereign workloads, this means your recovery paths must depend on data plane operations rather than control plane calls during a disruption. For example, pre-provisioned capacity in a recovery Region continues serving traffic even if the control plane in the primary Region is unavailable. See [AWS Fault Isolation Boundaries](https://docs.aws.amazon.com/whitepapers/latest/aws-fault-isolation-boundaries/abstract-and-introduction.html) for a detailed explanation of how AWS isolates failures across AZs, Regions, control planes, and data planes. 
+  [AWS Backup](https://aws.amazon.com/backup/) provides cross-Region and cross-account backup with encryption using customer-managed keys in the destination vault. [AWS Elastic Disaster Recovery](https://aws.amazon.com/disaster-recovery/) replicates servers to a recovery Region with sub-second RPOs. Both services handle the replication mechanics. Your responsibility is selecting recovery Regions that comply with data residency requirements and configuring encryption keys within approved jurisdictions. 
+  For jurisdictions where no second AWS Region exists, [AWS Outposts](https://aws.amazon.com/outposts/), [AWS Local Zones](https://aws.amazon.com/about-aws/global-infrastructure/localzones/), and [AWS Dedicated Local Zones](https://aws.amazon.com/dedicatedlocalzones/) provide in-country recovery options using the same APIs and tools as standard Regions. 

### Implementation steps
<a name="implementation-steps"></a>

 Before attempting these steps, make sure you understand [disaster recovery options in the cloud](https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/disaster-recovery-options-in-the-cloud.html), specifically the difference between Backup and Restore, Pilot Light, Warm standby, and Multi-site active-active. 

1.  **Assess data residency and regulatory requirements:** Identify the data protection, data privacy, and cybersecurity regulations that apply to your workloads in each operating jurisdiction. Determine your data residency requirements, including approvals and legal bases required for cross-border data transfers when backing up to a Region outside your jurisdiction. 

1.  **Select and validate recovery Regions:** Review [AWS Services by Region](https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/) to verify service availability in your chosen Regions, and use [AWS Artifact](https://aws.amazon.com/artifact/) to check compliance certifications and attestations for each Region. Test network latency between primary and recovery sites, and verify that each recovery Region meets data residency requirements for every data classification level. 

1.  **Select alternate recovery sites:** If no second AWS Region exists within the approved jurisdiction, evaluate alternative in-country options: 
   +  [AWS Outposts racks](https://aws.amazon.com/outposts/rack/) within your own data center or a colocation facility in the approved jurisdiction. 
   +  [AWS Local Zones](https://aws.amazon.com/about-aws/global-infrastructure/localzones/) or [AWS Dedicated Local Zones](https://aws.amazon.com/dedicatedlocalzones/) for in-country recovery capacity closer to your users. 
   +  Another service provider for temporary recovery within an approved jurisdiction. 
   +  Temporary waivers from regulators to deploy to another AWS Region in a different jurisdiction, with clearly stated duration, extension criteria, and obligations around resuming operations from the primary Region. 

    Document trade-offs for each option. For example, if your recovery strategy uses another service provider, interoperability and portability should be design goals with regular automated compatibility checks. 

1.  **Automate recovery infrastructure:** Use managed services for encryption and cross-Region backup replication. See [Creating backup copies across AWS Regions with AWS Backup](https://docs.aws.amazon.com/aws-backup/latest/devguide/cross-region-backup.html) and [Encryption for copies of a backup to a different account or AWS Region](https://docs.aws.amazon.com/aws-backup/latest/devguide/encryption.html#copy-encryption). When AWS Backup performs a cross-Region copy, data transfers over the AWS global backbone network through long-haul terrestrial fiber and sub-sea cables. Use [AWS Elastic Disaster Recovery](https://docs.aws.amazon.com/drs/latest/userguide/what-is-drs.html), [AWS Step Functions](https://aws.amazon.com/step-functions/), [Amazon EventBridge](https://aws.amazon.com/eventbridge/), and [AWS Lambda](https://aws.amazon.com/lambda/) to orchestrate recovery flows. 

1.  **Document recovery procedures:** Define RTOs and RPOs for each critical workload using [AWS Resilience Hub](https://docs.aws.amazon.com/resilience-hub/latest/userguide/what-is.html), and map system dependencies along the recovery path. Document step-by-step runbooks in [AWS Systems Manager Documents](https://docs.aws.amazon.com/systems-manager/latest/userguide/sysman-ssm-docs.html), including compliance validation checks at each stage. Define roles, responsibilities, escalation paths, and communication plans. Include manual fallback procedures for critical operations where automated recovery might not cover every scenario. 

1.  **Test and validate on a defined cadence:** Run recovery drills on a schedule aligned with your recovery objectives and audit cycle, and after any significant architecture or regulatory change, using [AWS Fault Injection Service](https://aws.amazon.com/fis/) and tabletop exercises, validating that procedures meet RTOs, RPOs, and data residency requirements. Train multiple team members on recovery procedures to avoid single points of failure, using [AWS Skill Builder](https://skillbuilder.aws/) and [AWS GameDay](https://aws.amazon.com/gameday/) for hands-on practice. Document test results, update procedures based on findings, and feed lessons learned back into the risk register. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [REL13-BP01 Define recovery objectives for downtime and data loss](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/rel_planning_for_recovery_objective_defined_recovery.html) 
+  [REL13-BP02 Use defined recovery strategies to meet the recovery objectives](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/rel_planning_for_recovery_disaster_recovery.html) 
+  [REL13-BP03 Test disaster recovery implementation to validate the implementation](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/rel_planning_for_recovery_dr_tested.html) 
+  [REL13-BP05 Automate recovery](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/rel_planning_for_recovery_auto_recovery.html) 
+  [SEC08-BP01 Implement secure key management](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_protect_data_rest_key_mgmt.html) 

 **Related documents:** 
+  [AWS Disaster Recovery Documentation](https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/disaster-recovery-workloads-on-aws.html) 
+  [AWS Resilience Hub User Guide](https://docs.aws.amazon.com/resilience-hub/latest/userguide/what-is.html) 
+  [Encryption best practices for AWS Key Management Service](https://docs.aws.amazon.com/prescriptive-guidance/latest/encryption-best-practices/kms.html) 
+  [AWS Regions](https://docs.aws.amazon.com/global-infrastructure/latest/regions/aws-regions.html) 

 **Related videos:** 
+  [AWS re:Inforce 2025 - Navigating sovereignty requirements: Architectures and solutions on AWS (DAP202)](https://www.youtube.com/watch?v=Eq0K0pxRjRk) 
+  [AWS re:Invent 2023: Backup and Disaster Recovery Strategies for Increased Resilience (ARC208)](https://aws.amazon.com/awstv/watch/173a403d06b/) 

 **Related services:** 
+  [AWS Resilience Hub](https://aws.amazon.com/resilience-hub/) 
+  [AWS Elastic Disaster Recovery](https://aws.amazon.com/disaster-recovery/) 
+  [AWS Backup](https://aws.amazon.com/backup/) 
+  [AWS KMS](https://aws.amazon.com/kms/) 
+  [AWS CloudHSM](https://aws.amazon.com/cloudhsm/) 
+  [AWS CloudFormation](https://aws.amazon.com/cloudformation/) 
+  [AWS Fault Injection Service](https://aws.amazon.com/fis/) 
+  [Amazon VPC](https://aws.amazon.com/vpc/) 
+  [AWS Transit Gateway](https://aws.amazon.com/transit-gateway/) 
+  [AWS Direct Connect](https://aws.amazon.com/directconnect/) 
+  [AWS Outposts](https://aws.amazon.com/outposts/) 
+  [AWS Local Zones](https://aws.amazon.com/about-aws/global-infrastructure/localzones/) 
+  [AWS Dedicated Local Zones](https://aws.amazon.com/dedicatedlocalzones/) 
+  [AWS Systems Manager](https://aws.amazon.com/systems-manager/) 