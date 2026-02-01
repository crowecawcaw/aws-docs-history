# DSREL01-BP03 Document recovery procedures

Document your disaster recovery procedures to enable operations to
recover quickly, while maintaining your regulatory posture. Include
steps to recover critical systems and data, meet recovery timelines,
and establish clear lines of accountability. Keep your documentation
up to date, simple to follow, and ready for audits.

**Desired outcome:** Organizations
maintain current, tested recovery documentation that enables rapid
system restoration. Recovery procedures consistently meet regulatory
requirements and achieve defined RTOs and RPOs. Teams run efficient
recovery operations during disruptions without confusion or delays.

**Common anti-patterns:**

- Maintaining outdated or untested recovery procedures stored in
  single locations without version control or regular updates
  after infrastructure changes.
- Failing to define clear roles, responsibilities, and system
  interdependencies in recovery plans, leading to confusion during
  actual recovery operations.
- Using generic, manual recovery procedures instead of automated
  workflows tailored to specific system requirements and
  compliance needs.
- Missing essential compliance checks and audit requirements in
  recovery documentation, creating regulatory gaps during recovery
  operations.

**Benefits of establishing this best
practice:**

- Accelerates recovery operations through clear, step-by-step
  automated procedures that anyone can follow consistently
  regardless of who performs them.
- Supports regulatory adherence and audit readiness with
  well-documented procedures that include essential compliance
  checks and reporting capabilities.
- Reduces data loss and recovery time through automated processes
  that achieve defined RTOs and RPOs consistently.
- Maintains current, effective procedures through version control
  and regular updates, allowing teams to identify and address
  weaknesses proactively.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

To document your recovery procedures:

- Start with your most critical systems.
- Create clear steps that anyone can follow.
- Define who does what.
- Add automated steps where possible.
- Include compliance requirements.

Key implementation elements:

- Define RTOs and RPOs.
- Map dependencies between applications, data stores, and
  services.
- Use infrastructure as code (IaC) to automate environment
  rebuilds.
- Regularly review and update documentation after infrastructure
  changes.

### Implementation steps

1. Define and document recovery objectives for each system
   using
   [AWS Resilience Hub](https://aws.amazon.com/resilience-hub/ "https://aws.amazon.com/resilience-hub/") (Resilience Hub). Use this service to
   set recovery targets, track compliance requirements, and
   monitor resilience metrics.
2. Create a system inventory and dependency maps using
   [AWS Systems Manager](https://aws.amazon.com/systems-manager/ "https://aws.amazon.com/systems-manager/") and
   [resource
   groups](../../../ARG/latest/userguide/resource-groups.md "../../../ARG/latest/userguide/resource-groups.md").
3. Establish a recovery team structure with defined roles and
   communication procedures, including clear contact
   information and escalation paths for effective incident
   response.
4. Implement infrastructure as code (IaC) using
   [AWS CloudFormation](https://aws.amazon.com/cloudformation/ "https://aws.amazon.com/cloudformation/") (CloudFormation) and
   [AWS Cloud Development Kit (AWS CDK) (CDK)](https://aws.amazon.com/cdk/ "https://aws.amazon.com/cdk/") to create templates for
   automated recovery.
5. Document recovery procedures in
   [Systems
   Manager](https://aws.amazon.com/systems-manager/ "https://aws.amazon.com/systems-manager/") documents. Configure backup and recovery
   workflows using
   [AWS Backup](https://aws.amazon.com/backup/ "https://aws.amazon.com/backup/") for system backups and enable
   [Amazon S3](https://aws.amazon.com/s3/ "https://aws.amazon.com/s3/") versioning for data protection.
6. Set up automated recovery processes using
   [AWS Auto Scaling](https://aws.amazon.com/autoscaling/ "https://aws.amazon.com/autoscaling/") for capacity management and
   [Amazon EventBridge](https://aws.amazon.com/eventbridge/ "https://aws.amazon.com/eventbridge/") with
   [AWS Lambda](https://aws.amazon.com/lambda/ "https://aws.amazon.com/lambda/") for automation. Configure monitoring with
   [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/ "https://aws.amazon.com/cloudwatch/") and audit logging with
   [AWS CloudTrail](https://aws.amazon.com/cloudtrail/ "https://aws.amazon.com/cloudtrail/").

## Resources

**Related best practices:**

- [REL13-BP05
  Automate recovery](../reliability-pillar/rel_planning_for_recovery_auto_recovery.md "../reliability-pillar/rel_planning_for_recovery_auto_recovery.md")

**Related documents:**

- [AWS Disaster Recovery Documentation](../../../whitepapers/latest/disaster-recovery-workloads-on-aws/disaster-recovery-workloads-on-aws.md "../../../whitepapers/latest/disaster-recovery-workloads-on-aws/disaster-recovery-workloads-on-aws.md")
- [AWS Resilience Hub User Guide](../../../resilience-hub/latest/userguide/what-is.md "../../../resilience-hub/latest/userguide/what-is.md")

**Related videos:**

- [Backup
  and Disaster Recovery Strategies for Increased Resilience: Leveraging AWS Services for Cost-Effective Business Continuity](https://aws.amazon.com/awstv/watch/173a403d06b/ "https://aws.amazon.com/awstv/watch/173a403d06b/")

**Related services:**

- [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/ "https://aws.amazon.com/cloudwatch/")
- [Amazon EventBridge](https://aws.amazon.com/eventbridge/ "https://aws.amazon.com/eventbridge/")
- [Amazon Simple Storage Service (S3)](https://aws.amazon.com/s3/ "https://aws.amazon.com/s3/")
- [AWS Auto Scaling](https://aws.amazon.com/autoscaling/ "https://aws.amazon.com/autoscaling/")
- [AWS Backup](https://aws.amazon.com/backup/ "https://aws.amazon.com/backup/")
- [AWS CDK](https://aws.amazon.com/cdk/ "https://aws.amazon.com/cdk/")
- [AWS CloudFormation](https://aws.amazon.com/cloudformation/ "https://aws.amazon.com/cloudformation/")
- [AWS CloudTrail](https://aws.amazon.com/cloudtrail/ "https://aws.amazon.com/cloudtrail/")
- [AWS Resilience Hub](https://aws.amazon.com/resilience-hub/ "https://aws.amazon.com/resilience-hub/")
- [AWS Resource Groups](https://aws.amazon.com/resource-groups/ "https://aws.amazon.com/resource-groups/")
- [AWS Systems Manager](https://aws.amazon.com/systems-manager/ "https://aws.amazon.com/systems-manager/")
