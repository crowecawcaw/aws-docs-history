# REL01-BP02 Manage service quotas across accounts and

regions

If you are using multiple accounts or Regions,
request the appropriate quotas in all environments
in which your production workloads run.

**Desired outcome:** Services and applications
should not be affected by service quota exhaustion for configurations that
span accounts or Regions or that have resilience designs using zone, Region,
or account failover.

**Common anti-patterns:**

- Allowing resource usage in one isolation Region
  to grow with no mechanism to maintain capacity in the
  other ones.
- Manually setting all quotas independently in isolation Regions.
- Not considering the effect of resiliency architectures
  (like active or passive) in future quota needs during a
  degradation in the non-primary Region.
- Not evaluating quotas regularly and making necessary
  changes in every Region and account the workload runs.
- Not leveraging [quota request templates](../../../servicequotas/latest/userguide/organization-templates.md "../../../servicequotas/latest/userguide/organization-templates.md")
  to request increases across multiple Regions and accounts.
- Not updating service quotas due to incorrectly
  thinking that increasing quotas has cost implications
  like compute reservation requests.

**Benefits of establishing this best
practice:** Verifying that you can handle your
current load in secondary regions or accounts if regional
services become unavailable. This can help reduce the number
of errors or levels of degradations that occur during region
loss.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Service quotas are tracked per account. Unless otherwise
noted, each quota is AWS Region-specific. In addition to
the production environments, also manage quotas in all
applicable non-production environments so that testing
and development are not hindered. Maintaining a high
degree of resiliency requires that service quotas are
assessed continually (whether automated or manual).

With more workloads spanning Regions due to the implementation
of designs using _Active/Active_,
_Active/Passive – Hot_,
_Active/Passive-Cold_, and
_Active/Passive-Pilot Light_ approaches,
it is essential to understand all Region and account quota levels.
Past traffic patterns are not always a good indicator if the
service quota is set correctly.

Equally important, the service quota name limit is not always
the same for every Region. In one Region, the value could be
five, and in another region the value could be ten. Management
of these quotas must span all the same services, accounts, and
Regions to provide consistent resilience under load.

Reconcile all the service quota differences across different
Regions (Active Region or Passive Region) and create processes
to continually reconcile these differences. The testing plans
of passive Region failovers are rarely scaled to peak active
capacity, meaning that game day or table top exercises can
fail to find differences in service quotas between Regions
and also then maintain the correct limits.

_Service quota drift_, the condition where service quota limits
for a specific named quota is changed in one Region and not
all Regions, is very important to track and assess. Changing
the quota in Regions with traffic or potentially could carry
traffic should be considered.

- Select relevant accounts and Regions based on your service requirements, latency,
  regulatory, and disaster recovery (DR) requirements.
- Identify service quotas across all relevant accounts, Regions, and
  Availability Zones. The limits are scoped to account and Region. These
  values should be compared for differences.

**Implementation steps**

- Review Service Quotas values that might have
  breached beyond the a risk level of usage.
  AWS Trusted Advisor provides alerts for 80% and 90%
  threshold breaches.
- Review values for service quotas in any Passive
  Regions (in an Active/Passive design). Verify
  that load will successfully run in secondary
  Regions in the event of a failure in the primary
  Region.
- Automate assessing if any service quota drift has
  occurred between Regions in the same account and
  act accordingly to change the limits.
- If the customer Organizational Units (OU) are structured
  in the supported manner, service quota templates should
  be updated to reflect changes in any quotas that should
  be applied to multiple Regions and accounts.
  - Create a template and associate Regions to the quota change.
  - Review all existing service quota templates for any changes
    required (Region, limits, and accounts).

## Resources

**Related best practices:**

- [REL01-BP01 Aware of service quotas and constraints](rel_manage_service_limits_aware_quotas_and_constraints.md "rel_manage_service_limits_aware_quotas_and_constraints.md")
- [REL01-BP03 Accommodate fixed service quotas and constraints
  through architecture](rel_manage_service_limits_aware_fixed_limits.md "rel_manage_service_limits_aware_fixed_limits.md")
- [REL01-BP04 Monitor and manage quotas](rel_manage_service_limits_monitor_manage_limits.md "rel_manage_service_limits_monitor_manage_limits.md")
- [REL01-BP05 Automate quota management](rel_manage_service_limits_automated_monitor_limits.md "rel_manage_service_limits_automated_monitor_limits.md")
- [REL01-BP06 Ensure that a sufficient gap exists between the
  current quotas and the maximum usage to accommodate failover](rel_manage_service_limits_suff_buffer_limits.md "rel_manage_service_limits_suff_buffer_limits.md")
- [REL03-BP01 Choose how to segment your workload](rel_service_architecture_monolith_soa_microservice.md "rel_service_architecture_monolith_soa_microservice.md")
- [REL10-BP01 Deploy the workload to multiple locations](rel_fault_isolation_multiaz_region_system.md "rel_fault_isolation_multiaz_region_system.md")
- [REL11-BP01 Monitor all components of the workload to detect
  failures](rel_withstand_component_failures_monitoring_health.md "rel_withstand_component_failures_monitoring_health.md")
- [REL11-BP03 Automate healing on all layers](rel_withstand_component_failures_auto_healing_system.md "rel_withstand_component_failures_auto_healing_system.md")
- [REL12-BP04 Test resiliency using chaos engineering](rel_testing_resiliency_failure_injection_resiliency.md "rel_testing_resiliency_failure_injection_resiliency.md")

**Related documents:**

- [AWS Well-Architected Framework’s Reliability Pillar: Availability](../reliability-pillar/availability.md "../reliability-pillar/availability.md")
- [AWS Service Quotas (formerly referred to as service limits)](../../../general/latest/gr/aws_service_limits.md "../../../general/latest/gr/aws_service_limits.md")
- [AWS Trusted Advisor Best Practice Checks (see the Service Limits
  section)](https://aws.amazon.com/premiumsupport/technology/trusted-advisor/best-practice-checklist/ "https://aws.amazon.com/premiumsupport/technology/trusted-advisor/best-practice-checklist/")
- [AWS limit monitor on AWS answers](https://aws.amazon.com/answers/account-management/limit-monitor/ "https://aws.amazon.com/answers/account-management/limit-monitor/")
- [Amazon EC2 Service Limits](../../../AWSEC2/latest/UserGuide/ec2-resource-limits.md "../../../AWSEC2/latest/UserGuide/ec2-resource-limits.md")
- [What
  is Service Quotas?](../../../servicequotas/latest/userguide/intro.md "../../../servicequotas/latest/userguide/intro.md")
- [How to Request Quota Increase](../../../servicequotas/latest/userguide/request-quota-increase.md "../../../servicequotas/latest/userguide/request-quota-increase.md")
- [Service endpoints and quotas](../../../general/latest/gr/aws-service-information.md "../../../general/latest/gr/aws-service-information.md")
- [Service Quotas User Guide](../../../servicequotas/latest/userguide/intro.md "../../../servicequotas/latest/userguide/intro.md")
- [Quota Monitor for AWS](https://aws.amazon.com/solutions/implementations/quota-monitor/ "https://aws.amazon.com/solutions/implementations/quota-monitor/")
- [AWS Fault Isolation Boundaries](../../../whitepapers/latest/aws-fault-isolation-boundaries/abstract-and-introduction.md "../../../whitepapers/latest/aws-fault-isolation-boundaries/abstract-and-introduction.md")
- [Availability with redundancy](../../../whitepapers/latest/availability-and-beyond-improving-resilience/availability-with-redundancy.md "../../../whitepapers/latest/availability-and-beyond-improving-resilience/availability-with-redundancy.md")
- [AWS for Data](https://aws.amazon.com/data/ "https://aws.amazon.com/data/")
- [What is Continuous Integration?](https://aws.amazon.com/devops/continuous-integration/ "https://aws.amazon.com/devops/continuous-integration/")
- [What is Continuous Delivery?](https://aws.amazon.com/devops/continuous-delivery/ "https://aws.amazon.com/devops/continuous-delivery/")
- [APN Partner: partners that can help with configuration management](https://partners.amazonaws.com/search/partners?keyword=Configuration+Management&ref=wellarchitected "https://partners.amazonaws.com/search/partners?keyword=Configuration+Management&ref=wellarchitected")
- [Managing the account lifecycle in account-per-tenant SaaS environments on AWS](https://aws.amazon.com/blogs/mt/managing-the-account-lifecycle-in-account-per-tenant-saas-environments-on-aws/ "https://aws.amazon.com/blogs/mt/managing-the-account-lifecycle-in-account-per-tenant-saas-environments-on-aws/")
- [Managing and monitoring API throttling in your workloads](https://aws.amazon.com/blogs/mt/managing-monitoring-api-throttling-in-workloads/ "https://aws.amazon.com/blogs/mt/managing-monitoring-api-throttling-in-workloads/")
- [View AWS Trusted Advisor recommendations at scale with AWS Organizations](https://aws.amazon.com/blogs/mt/organizational-view-for-trusted-advisor/ "https://aws.amazon.com/blogs/mt/organizational-view-for-trusted-advisor/")
- [Automating Service Limit Increases and Enterprise Support with AWS Control Tower](https://aws.amazon.com/blogs/mt/automating-service-limit-increases-enterprise-support-aws-control-tower/ "https://aws.amazon.com/blogs/mt/automating-service-limit-increases-enterprise-support-aws-control-tower/")

**Related videos:**

- [AWS Live
  re:Inforce 2019 - Service Quotas](https://youtu.be/O9R5dWgtrVo "https://youtu.be/O9R5dWgtrVo")
- [View and Manage Quotas for AWS Services Using Service Quotas](https://www.youtube.com/watch?v=ZTwfIIf35Wc "https://www.youtube.com/watch?v=ZTwfIIf35Wc")
- [AWS IAM Quotas Demo](https://www.youtube.com/watch?v=srJ4jr6M9YQ "https://www.youtube.com/watch?v=srJ4jr6M9YQ")

**Related services:**

- [Amazon CodeGuru Reviewer](https://aws.amazon.com/codeguru/ "https://aws.amazon.com/codeguru/")
- [AWS CodeDeploy](https://aws.amazon.com/codedeploy/ "https://aws.amazon.com/codedeploy/")
- [AWS CloudTrail](https://aws.amazon.com/cloudtrail/ "https://aws.amazon.com/cloudtrail/")
- [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/ "https://aws.amazon.com/cloudwatch/")
- [Amazon EventBridge](https://aws.amazon.com/eventbridge/ "https://aws.amazon.com/eventbridge/")
- [Amazon DevOps Guru](https://aws.amazon.com/devops-guru/ "https://aws.amazon.com/devops-guru/")
- [AWS Config](https://aws.amazon.com/config/ "https://aws.amazon.com/config/")
- [AWS Trusted Advisor](https://aws.amazon.com/premiumsupport/technology/trusted-advisor/ "https://aws.amazon.com/premiumsupport/technology/trusted-advisor/")
- [AWS CDK](https://aws.amazon.com/cdk/ "https://aws.amazon.com/cdk/")
- [AWS Systems Manager](https://aws.amazon.com/systems-manager/ "https://aws.amazon.com/systems-manager/")
- [AWS Marketplace](https://aws.amazon.com/marketplace/search/results?searchTerms=CMDB "https://aws.amazon.com/marketplace/search/results?searchTerms=CMDB")
