# REL13-BP05 Automate recovery

Implement tested and automated recovery mechanisms that are
reliable, observable, and reproducible to reduce the risk and
business impact of failure.

**Desired outcome:** You have
implemented a well-documented, standardized, and thoroughly-tested
automation workflow for recovery processes. Your recovery automation
automatically corrects minor issues that pose low risk of data loss
or unavailability. You are able to quickly invoke recovery processes
for serious incidents, observe the remediation behavior while they
operate, and end the processes if you observe dangerous situations
or failures.

**Common anti-patterns:**

- You depend on components or mechanisms that are in a failed or
  degraded state as part of your recovery plan.
- Your recovery processes require manual intervention, such as
  console access (also known as _click ops_).
- You automatically initiate recovery procedures in situations
  that present a high risk of data loss or unavailability.
- You fail to include a mechanism to abort a recovery procedure
  (like an _Andon cord_ or _big red
  stop button_) that is not working or that poses
  additional risks.

**Benefits of establishing this best
practice:**

- Increased reliability, predictability, and consistency of
  recovery operations.
- Ability to meet more stringent recovery objectives, including
  Recovery Time Objective (RTO) and Recovery Point Objective
  (RPO).
- Reduced likelihood of recovery failing during an incident.
- Reduced risk of failures associated with manual recovery
  processes that are prone to human error.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

To implement automated recovery, you need a comprehensive approach
that uses AWS services and best practices. To start, identify
critical components and potential failure points in your workload.
Develop automated processes that can recover your workloads and
data from failures without human intervention.

Develop your recovery automation using infrastructure as code
(IaC) principles. This makes your recovery environment consistent
with the source environment and allows for version control of your
recovery processes. To orchestrate complex recovery workflows,
consider solutions such as
[AWS Systems Manager Automations](../../../systems-manager/latest/userguide/systems-manager-automation.md "../../../systems-manager/latest/userguide/systems-manager-automation.md") or
[AWS Step Functions](https://aws.amazon.com/step-functions/ "https://aws.amazon.com/step-functions/").

Automation of recovery processes provides significant benefits and
can help you more easily achieve your Recovery Time Objective
(RTO) and Recovery Point Objective (RPO). However, they can
encounter unexpected situations that may cause them to fail or
create new risks of their own such as additional downtime and data
loss. To mitigate this risk, provide the ability to quickly halt a
recovery automation in progress. Once halted, you can investigate
and take corrective steps.

For supported workloads, consider solutions such as AWS Elastic
Disaster Recovery (AWS DRS) to provide automated failover. AWS DRS
continually replicates your machines (including operating system,
system state configuration, databases, applications, and files)
into a staging area in your target AWS account and preferred
Region. If an incident occurs, AWS DRS automates the conversion of
your replicated servers into fully-provisioned workloads in your
recovery Region on AWS.

Maintenance and improvement of automated recovery is an ongoing
process. Continually test and refine your recovery procedures
based on lessons learned, and stay updated on new AWS services and
features that can enhance your recovery capabilities.

### Implementation steps

1. **Plan for automated
   recovery**
   1. Conduct a thorough review of your workload architecture,
      components, and dependencies to identify and plan
      automated recovery mechanisms. Categorize your
      workload's dependencies into _hard_
      and _soft_ dependencies. Hard
      dependencies are those that the workload cannot operate
      without and for which no substitute can be provided.
      Soft dependencies are those that the workload ordinarily
      uses but are replaceable with temporary substitute
      systems or processes or can be handled by
      [graceful
      degradation](../reliability-pillar/rel_mitigate_interaction_failure_graceful_degradation.md "../reliability-pillar/rel_mitigate_interaction_failure_graceful_degradation.md").
   2. Establish processes to identify and recover missing or
      corrupted data.
   3. Define steps to confirm a recovered steady state after
      recovery actions have been completed.
   4. Consider any actions required to make the recovered
      system ready for full service, such as pre-warming and
      populating caches.
   5. Consider problems that could be encountered during the
      recovery process and how to detect and remediate them.
   6. Consider scenarios where the primary site and its
      control plane are inaccessible. Verify that recovery
      actions can be performed independently without reliance
      on the primary site. Consider solutions such as
      [Amazon Application Recovery Controller (ARC)](https://aws.amazon.com/application-recovery-controller/ "https://aws.amazon.com/application-recovery-controller/") to
      redirect traffic without the need to manually mutate DNS
      records.

2. **Develop automated recovery
   process**
   1. Implement automated fault detection and failover
      mechanisms for hands-free recovery. Build dashboards
      such as with
      [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/ "https://aws.amazon.com/cloudwatch/") to report the progress and health of
      automated recovery procedures. Include procedures to
      validate successful recovery. Provide a mechanism to
      abort a recovery in process.
   2. Build
      [playbooks](../reliability-pillar/rel_testing_resiliency_playbook_resiliency.md "../reliability-pillar/rel_testing_resiliency_playbook_resiliency.md")
      as a fallback process for faults that cannot be
      automatically recovered from, and take into
      consideration your
      [disaster
      recovery plan](https://aws.amazon.com/disaster-recovery/faqs/#Core_concepts "https://aws.amazon.com/disaster-recovery/faqs/#Core_concepts").
   3. Test recovery processes as discussed in
      [REL13-BP03](rel_planning_for_recovery_dr_tested.md "rel_planning_for_recovery_dr_tested.md").

3. **Prepare for recovery**
   1. Evaluate the state of your recovery site and deploy
      critical components to it in advance. For more detail,
      see
      [REL13-BP04](../reliability-pillar/rel_planning_for_recovery_config_drift.md "../reliability-pillar/rel_planning_for_recovery_config_drift.md").
   2. Define clear roles, responsibilities, and
      decision-making processes for recovery operations,
      involving relevant stakeholders and teams across the
      organization.
   3. Define the conditions to initiate your recovery
      processes.
   4. Create a plan to revert the recovery process and fall
      back to your primary site if required or after it's
      considered safe.

## Resources

**Related best practices:**

- [REL07-BP01
  Use automation when obtaining or scaling resources](rel_adapt_to_changes_autoscale_adapt.md "rel_adapt_to_changes_autoscale_adapt.md")
- [REL11-BP01
  Monitor all components of the workload to detect
  failures](rel_withstand_component_failures_monitoring_health.md "rel_withstand_component_failures_monitoring_health.md")
- [REL13-BP02
  Use defined recovery strategies to meet the recovery
  objectives](../reliability-pillar/rel_planning_for_recovery_disaster_recovery.md "../reliability-pillar/rel_planning_for_recovery_disaster_recovery.md")
- [REL13-BP03
  Test disaster recovery implementation to validate the
  implementation](rel_planning_for_recovery_dr_tested.md "rel_planning_for_recovery_dr_tested.md")
- [REL13-BP04
  Manage configuration drift at the DR site or Region](../reliability-pillar/rel_planning_for_recovery_config_drift.md "../reliability-pillar/rel_planning_for_recovery_config_drift.md")

**Related documents:**

- [AWS Architecture Blog: Disaster Recovery Series](https://aws.amazon.com/blogs/architecture/tag/disaster-recovery-series/ "https://aws.amazon.com/blogs/architecture/tag/disaster-recovery-series/")
- [Disaster
  Recovery of Workloads on AWS: Recovery in the Cloud (AWS Whitepaper)](../../../whitepapers/latest/disaster-recovery-workloads-on-aws/disaster-recovery-workloads-on-aws.md "../../../whitepapers/latest/disaster-recovery-workloads-on-aws/disaster-recovery-workloads-on-aws.md")
- [Orchestrate
  Disaster Recovery Automation using Amazon Route 53 ARC and AWS Step Functions](https://aws.amazon.com/blogs/networking-and-content-delivery/orchestrate-disaster-recovery-automation-using-amazon-route-53-arc-and-aws-step-functions/ "https://aws.amazon.com/blogs/networking-and-content-delivery/orchestrate-disaster-recovery-automation-using-amazon-route-53-arc-and-aws-step-functions/")
- [Build
  AWS Systems Manager Automation runbooks using AWS CDK](https://aws.amazon.com/blogs/mtbuild-aws-systems-manager-automation-runbooks-using-aws-cdk/ "https://aws.amazon.com/blogs/mtbuild-aws-systems-manager-automation-runbooks-using-aws-cdk/")
- [AWS Marketplace: Products That Can Be Used for Disaster
  Recovery](https://aws.amazon.com/marketplace/search/results?searchTerms=Disaster+recovery "https://aws.amazon.com/marketplace/search/results?searchTerms=Disaster+recovery")
- [AWS Systems Manager Automation](../../../systems-manager/latest/userguide/systems-manager-automation.md "../../../systems-manager/latest/userguide/systems-manager-automation.md")
- [AWS Elastic Disaster Recovery](https://aws.amazon.com/disaster-recovery/ "https://aws.amazon.com/disaster-recovery/")
- [Using
  Elastic Disaster Recovery for Failover and Failback](../../../drs/latest/userguide/failback.md "../../../drs/latest/userguide/failback.md")
- [AWS Elastic Disaster Recovery Resources](https://aws.amazon.com/disaster-recovery/resources/ "https://aws.amazon.com/disaster-recovery/resources/")
- [APN
  Partner: Partners That Can Help with Disaster Recovery](https://aws.amazon.com/partners/find/results/?keyword=Disaster+Recovery "https://aws.amazon.com/partners/find/results/?keyword=Disaster+Recovery")

**Related videos:**

- [AWS re:Invent
  2018: Architecture Patterns for Multi-Region Active-Active
  Applications (ARC209-R2)](https://youtu.be/2e29I3dA8o4 "https://youtu.be/2e29I3dA8o4")
- [AWS re:Invent
  2022: AWS On Air ft. AWS Failback for AWS Elastic Disaster
  Recovery](https://youtu.be/Ok-vpV8b1Hs "https://youtu.be/Ok-vpV8b1Hs")
