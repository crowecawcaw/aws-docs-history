

# Assess
<a name="assess-rel"></a>

 The Assess phase involves evaluating the current state of the workloads that are targeted for the migration. To achieve this, we will focus on assessing the existing workloads for any potential points of failure during the migration process. 


| MIG-REL-01: Do you have any existing compliance requirements around service availability or service-level agreements (SLA) that apply to applications within the migration scope? | 
| --- | 
|   | 

 Existing applications have current service levels which must be maintained during migration. During migration assessment, it is important to understand the existing availability requirements, and then define the migration strategy and target architecture. 

## MIG-REL-BP-1.1: Define SLAs across all applications or environments (like production, development, or test) and confirm them with your business team
<a name="mig-rel-bp-1.1-define-slas-across-all-applications-or-environments"></a>

 This BP applies to the following best practice areas: Foundations 

### Implementation guidance
<a name="implementation-guidance-34"></a>

 **Suggestion 1.1.1:** Evaluate the unique aspects of your applications to understand if you have different availability requirements for each application. 

 Define goals for each application based on [availability](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/availability.html). 

## MIG-REL-BP-1.2: Define and automate runbooks and communicate them to your teams
<a name="mig-rel-bp-1.2-define-and-automate-runbooks-and-communicate-them-to-your-teams"></a>

 This BP applies to the following best practice areas: Foundations

### Implementation guidance
<a name="implementation-guidance-35"></a>

 **Suggestion 1.2.1:** Prepare, document and validate procedures for your workload to minimize the disruption of your workload during events. 

 It is recommended to automate runbook procedures so runbook activities are performed consistently. For more detail, see [OPS07-BP03 Use runbooks to perform procedures](https://docs.aws.amazon.com/wellarchitected/latest/operational-excellence-pillar/ops_ready_to_support_use_runbooks.html). 

## MIG-REL-BP-1.3: Map AWS Global Infrastructure to your business SLAs before migrations starts
<a name="mig-rel-bp-1.3-map-global-infrastructure-to-your-business-slas-before-migrations-starts"></a>

 This BP applies to the following best practice areas: Foundations 

### Implementation guidance
<a name="implementation-guidance-36"></a>

 **Suggestion 1.3.1:** Understand [AWS Global Infrastructure](https://aws.amazon.com/about-aws/global-infrastructure/regions_az/) terminology and definitions. 

If you operate multiple datacenters on-premises today, how does this map to AWS infrastructure and your existing availability requirements? **Suggestion 1.3.2** Identify the services you plan to use when you migrate and compare the [AWS Service Level Agreements](https://aws.amazon.com/legal/service-level-agreements/) to your existing business SLAs.

 Your existing SLAs may need to be updated based on AWS Service Level Agreements. 

## MIG-REL-BP-1.4: Select tools to monitor SLAs and notify you in case thresholds are exceeded
<a name="mig-rel-bp-1.4-select-tools-to-monitor-slas-and-notify-you-in-case-thresholds-are-exceeded"></a>

 This BP applies to the following best practice areas: Foundations 

### Implementation guidance
<a name="implementation-guidance-37"></a>

 **Suggestion 1.4.1:** Reduce communication to on-premises monitoring tools. 

If you choose to use existing monitoring tools on your migrated workloads, you should optimize data egress to systems which are remaining on-premises. This is achieved differently by different tools, but a common method is to deploy a collector within AWS that optimizes communication. When migrating to AWS, there may be agents which are no longer needed (for example, VMware Tools and tools for physical hardware monitoring). Use [custom post-launch actions](https://docs.aws.amazon.com/mgn/latest/ug/post-launch-settings-custom-actions.html) to remove these agents during migration with AWS Application Migration Service.

**Suggestion 1.4.2:** Use managed services to reduce operational overhead and save licensing costs.

Before migrating, assess if changing monitoring tools for AWS Managed Services like [Amazon Cloudwatch](https://aws.amazon.com/cloudwatch/) and [AWS Systems Manager](https://aws.amazon.com/systems-manager/) could reduce the overhead of running these tools and the licensing costs from those tools.

**Suggestion 1.4.3:** Monitor networking links during migration.

Measure the additional migration related network traffic and prevent this traffic from affecting business applications. For example, if you are using AWS Direct Connect between your on-premises solution and AWS, you can monitor the throughput of the migrated workload using [AWS Direct Connect resources](https://docs.aws.amazon.com/directconnect/latest/UserGuide/monitoring-overview.html) and set up [Amazon CloudWatch alarm throughput notification](https://repost.aws/knowledge-center/cloudwatch-throughput-direct-connect).

**Suggestion 1.4.4:** Use metrics and logs from AWS Migration Services to monitor inflight migrations.

 For more detail, see [Monitoring Application Migration Service](https://docs.aws.amazon.com/mgn/latest/ug/monitoring-overview.html) and [Monitoring AWS DMS tasks](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Monitoring.html). 


| MIG-REL-02: What is your business continuity plan for the migrated workload? | 
| --- | 
|   | 

Each organization has different set of requirements to build a business continuity plan (BCP) or disaster recovery (DR) plan. The BCP needs to be updated during migration, as the locations of workloads are changing. The risks associated with cloud services need to be added to the BCP. For more detail, see [Disaster Recovery of Workloads on AWS: Recovery in the Cloud](https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/disaster-recovery-workloads-on-aws.html).

## MIG-REL-BP-2.1: Keep your business impact analysis up-to-date
<a name="mig-rel-bp-2.1-keep-your-business-impact-analysis-up-to-date"></a>

 This BP applies to the following best practice areas: Failure management

### Implementation guidance
<a name="implementation-guidance-38"></a>

 **Suggestion 2.1.1:** Check that your portfolio and CMDB data is correct. 

 Keeping application metadata up-to-date is challenging. Commonly, application metadata (for example, number of users) is only updated periodically. Additionally, applications which were once important might not be so critical as alternatives become available. The application metadata should be verified so the correct BCP is put in place as part of the migration project. 

## MIG-REL-BP-2.2: Update the risk assessment for the type of disaster events covered by your BCP
<a name="mig-rel-bp-2.2-update-the-risk-assessment-for-the-type-of-disaster-events-covered-by-your-bcp"></a>

 This BP applies to the following best practice areas: Failure management 

### Implementation guidance
<a name="implementation-guidance-39"></a>

 **Suggestion 2.2.1:** Add new events for your cloud environment. 

 Various events in the cloud environment for example complete loss of AWS Region, complete loss of an AWS Availability zone or service degradation of a single AWS service need a risk assessment. A risk assessment measures how likely an event will occur vs the impact of that event to business applications and helps determine the recovery targets for certain events. 

## MIG-REL-BP-2.3: Define the recovery point objective (RPO) and recovery time objective (RTO) targets
<a name="mig-rel-bp-2.3-define-the-recovery-point-objective-rpo-and-recovery-time-objective-rto-targets"></a>

 This BP applies to the following best practice areas: Failure management 

### Implementation guidance
<a name="implementation-guidance-40"></a>

 **Suggestion 2.3.1:** Create a small number of different RPO and RTO classes.

 Migrations can have hundreds of applications in scope, and creating many different RPO or RTO targets which map to different disaster recovery strategies can increase the complexity of migration. 

## MIG-REL-BP-2.4: Select a disaster recovery strategy based on cloud best practices
<a name="mig-rel-bp-2.4-select-a-disaster-recovery-strategy-based-on-cloud-best-practices"></a>

** **This BP applies to the following best practice areas: Failure management

### Implementation guidance
<a name="implementation-guidance-41"></a>

 **Suggestion 2.4.1:** Familiarize yourself with [disaster recovery options in the cloud](https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/disaster-recovery-options-in-the-cloud.html). 

You must a select disaster recovery option which meets your RPO and RTO targets and addresses risks defined in your BCP. For example, [AWS Elastic Disaster Recovery](https://aws.amazon.com/disaster-recovery/) replicates Amazon EC2 instances to another AWS Availability Zone (or another Region) to address the risk of disasters within AWS.

**Suggestion 2.4.2:** Automate disaster recovery options to be implemented as migrations occur.

 For example, in migrations using AWS Application Migration Service, there is a post-launch action to [configure AWS Elastic Disaster Recovery (AWS DRS)](https://docs.aws.amazon.com/mgn/latest/ug/predefined-post-launch-actions.html#predefined-elastic-disaster-recovery). 


| MIG-REL-03: What is the maintenance window for the migration cutover? | 
| --- | 
|   | 

 During migration activity, business process may not be resilient to extend downtime windows. Align the migration event based on your business need. 

## MIG-REL-BP-3.1: Estimate the required maintenance window
<a name="mig-rel-bp-3.1-estimate-the-required-maintenance-window"></a>

 This BP applies to the following best practice areas: Change management 

### Implementation guidance
<a name="implementation-guidance-42"></a>

 **Suggestion 3.1.1:** Migration to AWS could involve a brief or extended outage of service during the cutover from the current environment. 

 A typical application cutover involves shutting down the source application, then running a final synchronization of data. The amount of data in the final synchronization, combined with the speed of network links, determines the outage period required for the migration. For example, database migrations can be performed using a [backup and restore method or AWS Database Migration Service](https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-database-rehost-tools/dms.html). These methods offer different cutover windows. Users of the applications being migrated need to be informed of the accurate outage period, with appropriate lead time to assess the impact and plan contingencies. 

## MIG-REL-BP-3.2: Test the migration window and impact
<a name="mig-rel-bp-3.2-test-the-migration-window-and-impact"></a>

 This BP applies to the following best practice areas: Change management 

### Implementation guidance
<a name="implementation-guidance-43"></a>

 **Suggestion 3.2.1:** Dry-run the migration activities to validate that they can be completed in the defined maintenance window. 

Perform dry-run tests in environments with similar data volume or anticipate the additional volume of data that the production environment has compared to non-production testing (usually significant). Monitoring tools can help provide accurate data change rates. For more detail, see [Running a proof of concept](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_BestPractices.html#CHAP_BestPractices.RunPOC).

**Suggestion 3.2.2:** In case the migration data synchronization activities or testing take longer than the defined maintenance window, define a process to measure the impact on your business and set a contingency plan.

 For some applications, it may be fine to extend the maintenance period, but for others, immediate rollback of the migration is required. For more detail, see [Developing a cutover plan](https://docs.aws.amazon.com/prescriptive-guidance/latest/best-practices-migration-cutover/pre-cutover-stage.html#cutover-plan). 

## MIG-REL-BP-3.3: Plan for failure
<a name="mig-rel-bp-3.3-plan-for-failure"></a>

 This BP applies to the following best practice areas: Change management 

### Implementation guidance
<a name="implementation-guidance-44"></a>

 **Suggestion 3.3.1:** Calculate and document the time required to rollback. 

A migration checkpoint should be put in place to enable rollback to be performed within the defined maintenance window. For more detail, see [Rollback](https://docs.aws.amazon.com/prescriptive-guidance/latest/best-practices-migration-cutover/cutover-stage.html#rollback).

**Suggestion 3.3.2:** Define a communication channel for the migration event and communication intervals agreed with stakeholders.

Communication channels should be used to make decisions during unexpected events. For example, if the maintenance window needs to be extended, a message can be sent to application owners to approve extension or initiate rollback. For more detail, see [Communication and governance planning](https://docs.aws.amazon.com/prescriptive-guidance/latest/best-practices-migration-cutover/communication-governance-planning.html).

**Suggestion 3.3.3:** Determine how data can be copied back to the source environment.

 After deciding to rollback a migration, you may need to copy data back to the source environment. For EC2 instances, AWS Elastic Disaster Recovery can be used to [perform a failback](https://docs.aws.amazon.com/drs/latest/userguide/failback-performing-main.html) from AWS to on-premises environments. For databases, depending on the amount of data to be synchronized, native replication tools can be used, or a database backup and restore can be performed. 