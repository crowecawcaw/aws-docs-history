# REL13-BP04 Manage configuration drift at the DR site or

Region

To perform a successful disaster recovery (DR) procedure, your
workload must be able to resume normal operations in a timely manner
with no relevant loss of functionality or data once the DR
environment has been brought online. To achieve this goal, it's
essential to maintain consistent infrastructure, data, and
configurations between your DR environment and the primary
environment.

**Desired outcome:** Your disaster
recovery site's configuration and data are in parity with the
primary site, which facilitates rapid and complete recovery when
needed.

**Common anti-patterns:**

- You fail to update recovery locations when changes are made to
  the primary locations, which results in outdated configurations
  that could hinder recovery efforts.
- You do not consider potential limitations such as service
  differences between primary and recovery locations, which can
  lead to unexpected failures during failover.
- You rely on manual processes to update and synchronize the DR
  environment, which increases the risk of human error and
  inconsistency.
- You fail to detect configuration drift, which leads to a false
  sense of DR site readiness prior to an incident.

**Benefits of establishing this best
practice:** Consistency between the DR environment and the
primary environment significantly improves the likelihood of a
successful recovery after an incident and reduces the risk of a
failed recovery procedure.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

A comprehensive approach to configuration management and failover
readiness can help you verify that the DR site is consistently
updated and prepared to take over in the event of a primary site
failure.

To achieve consistency between your primary and disaster recovery
(DR) environments, validate that your delivery pipelines
distribute applications to both your primary and DR sites. Roll
out changes to the DR sites after an appropriate evaluation period
(also known as _staggered deployments_) to
detect problems at the primary site and halt the deployment before
they spread. Implement monitoring to detect configuration drift,
and track changes and compliance across your environments. Perform
automated remediation in the DR site to keep it fully consistent
and ready to take over in the event of an incident.

### Implementation steps

1. Validate that the DR region contains the AWS services and
   features required for a successful execution of your DR
   plan.
2. Use infrastructure as code (IaC). Keep your production
   infrastructure and application configuration templates
   accurate, and regularly apply them to your disaster recovery
   environment.
   [AWS CloudFormation](https://aws.amazon.com/cloudformation/ "https://aws.amazon.com/cloudformation/") can detect drift between what your
   CloudFormation templates specify and what is actually
   deployed.
3. Configure CI/CD pipelines to deploy applications and
   infrastructure updates to all environments, including
   primary and DR sites. CI/CD solutions such as
   [AWS CodePipeline](https://aws.amazon.com/codepipeline/ "https://aws.amazon.com/codepipeline/") can automate the deployment process,
   which reduces the risk of configuration drift.
4. Stagger deployments between the primary and DR environments.
   This approach allows updates to be initially deployed and
   tested in the primary environment, which isolates issues in
   the primary site before they are propagated to the DR site.
   This approach prevents defects from being simultaneously
   pushed to production and the DR site at the same time and
   maintains the integrity of the DR environment.
5. Continually monitor resource configurations in both primary
   and DR environments. Solutions such as
   [AWS Config](https://aws.amazon.com/config/ "https://aws.amazon.com/config/") can help to enforce configuration compliance
   and detect drift, which helps maintain the consistent
   configurations across environments.
6. Implement alerting mechanisms to track and notify upon any
   configuration drift or data replication interruption or lag.
7. Automate the remediation of detected configuration drift.
8. Schedule regular audits and compliance checks to verify
   ongoing alignment between primary and DR configurations.
   Periodic reviews help you maintain compliance with defined
   rules and identify any discrepancies that need to be
   addressed.
9. Check for mismatches in AWS provisioned capacity, service
   quotas, throttle limits, and configuration and version
   discrepancies.

## Resources

**Related best practices:**

- [REL01-BP01
  Aware of service quotas and constraints](../reliability-pillar/rel_manage_service_limits_aware_quotas_and_constraints.md "../reliability-pillar/rel_manage_service_limits_aware_quotas_and_constraints.md")
- [REL01-BP02
  Manage service quotas across accounts and regions](../reliability-pillar/rel_manage_service_limits_limits_considered.md "../reliability-pillar/rel_manage_service_limits_limits_considered.md")
- [REL01-BP04
  Monitor and manage quotas](../reliability-pillar/rel_manage_service_limits_monitor_manage_limits.md "../reliability-pillar/rel_manage_service_limits_monitor_manage_limits.md")
- [REL13-BP03
  Test disaster recovery implementation to validate the
  implementation](../reliability-pillar/rel_planning_for_recovery_dr_tested.md "../reliability-pillar/rel_planning_for_recovery_dr_tested.md")

**Related documents:**

- [Remediating
  Noncompliant AWS Resources by AWS Config Rules](../../../config/latest/developerguide/remediation.md "../../../config/latest/developerguide/remediation.md")
- [AWS Systems Manager Automation](../../../systems-manager/latest/userguide/systems-manager-automation.md "../../../systems-manager/latest/userguide/systems-manager-automation.md")
- [AWS CloudFormation: Detecting unmanaged configuration changes to
  stacks and resources](../../../AWSCloudFormation/latest/UserGuide/using-cfn-stack-drift.md "../../../AWSCloudFormation/latest/UserGuide/using-cfn-stack-drift.md")
- [AWS CloudFormation: Detect Drift on an Entire CloudFormation
  Stack](../../../AWSCloudFormation/latest/UserGuide/detect-drift-stack.md "../../../AWSCloudFormation/latest/UserGuide/detect-drift-stack.md")
- [AWS Systems Manager Automation](../../../systems-manager/latest/userguide/systems-manager-automation.md "../../../systems-manager/latest/userguide/systems-manager-automation.md")
- [Disaster
  Recovery of Workloads on AWS: Recovery in the Cloud (AWS Whitepaper)](../../../whitepapers/latest/disaster-recovery-workloads-on-aws/disaster-recovery-workloads-on-aws.md "../../../whitepapers/latest/disaster-recovery-workloads-on-aws/disaster-recovery-workloads-on-aws.md")
- [How
  do I implement an Infrastructure Configuration Management
  solution on AWS?](https://aws.amazon.com/answers/configuration-management/aws-infrastructure-configuration-management/?ref=wellarchitected "https://aws.amazon.com/answers/configuration-management/aws-infrastructure-configuration-management/?ref=wellarchitected")
- [Remediating
  Noncompliant AWS Resources by AWS Config Rules](../../../config/latest/developerguide/remediation.md "../../../config/latest/developerguide/remediation.md")

**Related videos:**

- [AWS re:Invent
  2018: Architecture Patterns for Multi-Region Active-Active
  Applications (ARC209-R2)](https://youtu.be/2e29I3dA8o4 "https://youtu.be/2e29I3dA8o4")

**Related examples:**

- [AWS CloudFormation
  Registry](https://aws.amazon.com/blogs/devops/identify-regional-feature-parity-using-the-aws-cloudformation-registry/ "https://aws.amazon.com/blogs/devops/identify-regional-feature-parity-using-the-aws-cloudformation-registry/")
- [Quota
  Monitor for AWS](https://aws.amazon.com/solutions/implementations/quota-monitor/ "https://aws.amazon.com/solutions/implementations/quota-monitor/")
- [Implement
  automatic drift remediation for AWS CloudFormation using
  Amazon CloudWatch and AWS Lambda](https://aws.amazon.com/blogs/mt/implement-automatic-drift-remediation-for-aws-cloudformation-using-amazon-cloudwatch-and-aws-lambda/ "https://aws.amazon.com/blogs/mt/implement-automatic-drift-remediation-for-aws-cloudformation-using-amazon-cloudwatch-and-aws-lambda/")
- [AWS Architecture Blog: Disaster Recovery Series](https://aws.amazon.com/blogs/architecture/tag/disaster-recovery-series/ "https://aws.amazon.com/blogs/architecture/tag/disaster-recovery-series/")
- [AWS Marketplace: products that can be used for disaster
  recovery](https://aws.amazon.com/marketplace/search/results?searchTerms=Disaster+recovery "https://aws.amazon.com/marketplace/search/results?searchTerms=Disaster+recovery")
- [Automating
  safe, hands-off deployments](https://aws.amazon.com/builders-library/automating-safe-hands-off-deployments/ "https://aws.amazon.com/builders-library/automating-safe-hands-off-deployments/")
