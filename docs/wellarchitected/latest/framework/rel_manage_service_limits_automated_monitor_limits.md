# REL01-BP05 Automate quota management

Service quotas, also referred to as limits in AWS services, are the
maximum values for the resources in your AWS account. Each AWS
service defines a set of quotas and their default values. To provide
your workload access to all the resources it needs, you might need
to increase your service quota values.

Growth in workload consumption of AWS resources can threaten
workload stability and impact the user experience if quotas are
exceeded. Implement tools to alert you when your workload approaches
the limits and consider creating quota increase requests
automatically.

**Desired outcome:** Quotas are
appropriately configured for the workloads running in each AWS account and Region.

**Common anti-patterns:**

- You fail to consider and adjust quotas appropriately to meet
  workload requirements.
- You track quotas and usage using methods that can become
  outdated, such as with spreadsheets.
- You only update service limits on periodic schedules.
- Your organization lacks operational processes to review existing
  quotas and request service quota increases when necessary.

**Benefits of establishing this best
practice:**

- Enhanced workload resiliency: You prevent errors caused by
  exceeding AWS resource quotas.
- Simplified disaster recovery: You can reuse automated quota
  management mechanisms built in the primary Region during DR
  setup in another AWS Region.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

View current quotas and track ongoing quota consumption through
mechanisms such as AWS Service Quotas console, AWS Command Line Interface (AWS CLI), and AWS SDKs. You can also integrate your
configuration management databases (CMDB) and IT service
management (ITSM) systems with the AWS Service Quota APIs.

Generate automated alerts if quota usage reaches your defined
thresholds, and define a process for submitting quota increase
requests when you receive alerts. If the underlying workload is
critical to your business, you can automate quota increase
requests, but carefully test the automation to avoid the risk of
runaway action such as a growth feedback loop.

Smaller quota increases are often automatically approved. Larger
quota requests may need to be manually processed by AWS support
and can take additional time to review and process. Allow for
additional time to process multiple requests or large increase
requests.

### Implementation steps

- Implement automated monitoring of service quotas, and issue
  alerts if your workload's resource utilization growth
  approaches your quota limits. For example,
  [Quota
  Monitor](../../../solutions/latest/quota-monitor-for-aws/solution-overview.md "../../../solutions/latest/quota-monitor-for-aws/solution-overview.md") for AWS can provide automated monitoring of
  service quotas. This tool integrates with AWS Organizations
  and deploys using Cloudformation StackSets so that new
  accounts are automatically monitored on creation.
- Use features such as
  [Service Quotas request templates](../../../servicequotas/latest/userguide/organization-templates.md "../../../servicequotas/latest/userguide/organization-templates.md") or
  [AWS Control Tower](https://www.youtube.com/watch?v=3WUShZ4lZGE "https://www.youtube.com/watch?v=3WUShZ4lZGE") to simplify Service Quotas setup for
  new accounts.
- Build dashboards of your current service quota use across
  all AWS accounts and regions and reference them as necessary
  to prevent exceeding your quotas.
  [Trusted
  Advisor Organizational (TAO) Dashboard](https://aws.amazon.com/blogs/mt/a-detailed-overview-of-trusted-advisor-organizational-dashboard/ "https://aws.amazon.com/blogs/mt/a-detailed-overview-of-trusted-advisor-organizational-dashboard/"), part of the
  [Cloud
  Intelligence Dashboards](https://catalog.workshops.aws/awscid/en-US "https://catalog.workshops.aws/awscid/en-US"), can get you quickly started
  with such a dashboard.
- Track service limit increase requests.
  [Consolidated
  Insights from Multiple Accounts(CIMA)](https://github.com/aws-samples/case-insights-for-multi-accounts "https://github.com/aws-samples/case-insights-for-multi-accounts") can provide an
  Organization-level view of all your requests.
- Test alert generation and any quota increase request
  automation by setting lower quota thresholds in
  non-production accounts. Do not conduct these tests in a
  production account.

## Resources

**Related best practices:**

- [OPS10-BP07
  Automate responses to events](../operational-excellence-pillar/ops_event_response_auto_event_response.md "../operational-excellence-pillar/ops_event_response_auto_event_response.md")

**Related documents:**

- [APN
  Partner: partners that can help with configuration
  management](https://aws.amazon.com/partners/find/results/?keyword=Configuration+Management "https://aws.amazon.com/partners/find/results/?keyword=Configuration+Management")
- [AWS Marketplace: CMDB products that help track limits](https://aws.amazon.com/marketplace/search/results?searchTerms=CMDB "https://aws.amazon.com/marketplace/search/results?searchTerms=CMDB")
- [AWS Service Quotas (formerly referred to as service limits)](../../../general/latest/gr/aws_service_limits.md "../../../general/latest/gr/aws_service_limits.md")
- [AWS Trusted Advisor Best Practice Checks (see the Service Limits
  section)](../../../awssupport/latest/user/trusted-advisor-check-reference.md "../../../awssupport/latest/user/trusted-advisor-check-reference.md")
- [Quota
  Monitor Solution on AWS - AWS Solution](https://aws.amazon.com/answers/account-management/limit-monitor/ "https://aws.amazon.com/answers/account-management/limit-monitor/")
- [What
  is Service Quotas?](../../../servicequotas/latest/userguide/intro.md "../../../servicequotas/latest/userguide/intro.md")
- [What
  is Service Quotas request templates?](../../../servicequotas/latest/userguide/intro.md "../../../servicequotas/latest/userguide/intro.md")

**Related videos:**

- [AWS Live
  re:Inforce 2019 - Service Quotas](https://youtu.be/O9R5dWgtrVo "https://youtu.be/O9R5dWgtrVo")
- [Automating
  Service Limit Increases and Enterprise Support with AWS Control Tower](https://www.youtube.com/watch?v=3WUShZ4lZGE "https://www.youtube.com/watch?v=3WUShZ4lZGE")

**Related tools:**

- [Quota
  Monitor for AWS](https://github.com/aws-solutions/quota-monitor-for-aws "https://github.com/aws-solutions/quota-monitor-for-aws")
