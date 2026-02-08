# MSFTREL03-BP01 Use Microsoft logs for incident analysis

Microsoft workloads generate rich diagnostic information through
specialized logging systems that provide deeper visibility into
application behavior, security events, and system performance than
standard infrastructure monitoring alone. These Microsoft log
sources offer unique insights into Active Directory authentication
patterns, SQL Server performance bottlenecks, IIS application
errors, and Windows system events that are essential for
comprehensive incident analysis and root cause identification.

**Desired outcome:** The
implementation of comprehensive incident analysis should result in a
detailed incident timeline constructed from CloudWatch and diverse
Microsoft log sources including categorized Windows Event Logs
(System, Security, Application events), Active Directory
authentication and directory service logs, SQL Server operational
and audit logs, IIS web server logs, Exchange messaging logs, and
SharePoint service logs, accompanied by thorough post-incident
documentation. Infrastructure improvements, derived from root cause
analysis, should be automated through infrastructure as code and
systematically deployed through AWS Systems Manager, providing for
consistent security patch management and configuration updates
across your Windows instances.

**Common anti-patterns:**

- Reactive manual patching and configuration changes without
  proper documentation or version control, leading to inconsistent
  Windows environments and untraceable security vulnerabilities.
- Neglecting to collect or analyze Windows Event Logs (or general
  logs) during incidents, resulting in incomplete incident
  understanding and recurring issues due to unidentified root
  causes.
- Implementing infrastructure changes directly through the AWS Management Console instead of infrastructure as code, causing configuration
  drift and making it impossible to reliably replicate or roll
  back environment changes.

**Benefits of establishing this best
practice:**

- Systematic log analysis and documented post-mortems enable
  faster, more effective resolution of future incidents and reduce
  mean time to recovery (MTTR).
- Infrastructure as code (IaC) creates reproducible,
  version-controlled environment configurations, eliminating
  manual errors and configuration drift.
- Centralized patch management through AWS Systems Manager
  maintains security standards across Windows instances while
  reducing operational overhead.
- ßComprehensive documentation and standardized runbooks preserve
  institutional knowledge, enabling better team collaboration and
  reducing dependency on specific individuals.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Review Amazon CloudWatch and comprehensive Microsoft log sources
to analyze incidents, including: - Windows event logs (system,
security, application, setup, and forwarded events) - Active
Directory logs (security events, directory service logs, DNS
server logs) - SQL Server logs (error logs, agent logs, audit
logs, transaction logs) - IIS or .NET logs (access logs, error
logs, ASP.NET application logs) - Exchange Server logs (message
tracking, protocol logs, connectivity logs) - SharePoint ULS
(Unified Logging Service) logs.

Document findings in a post-incident report covering root cause,
impact, and fixes. Update infrastructure code (using AWS CloudFormation or AWS CDK) with improvements and revise Windows
configurations. Automate future security updates using AWS Systems Manager.

Begins with establishing a robust logging strategy using
CloudWatch and Windows event logs. A standardized post-incident
template should include sections for incident timeline, root cause
analysis, impact assessment, and remediation steps.

Migrate infrastructure to infrastructure as code using AWS CloudFormation or AWS CDK, incorporating lessons learned from
incidents. Configure AWS Systems Manager to automate regular
security patching and configuration updates across Windows
instances, maintaining consistent application of security
policies. Runbooks require regular review and updates to reflect
the latest best practices and incident response procedures.

### Implementation steps

1. Configure comprehensive logging through CloudWatch and
   Windows Event Logs, establishing appropriate retention
   periods and log analysis workflows.
2. Create standardized templates for incident documentation,
   including post-incident analysis, root cause identification,
   and remediation tracking.
3. Develop infrastructure as code templates using
   CloudFormation or CDK to manage and version control your
   infrastructure components.
4. Set up AWS Systems Manager for automated patch management
   and configuration updates across Windows instances.
5. Establish regular review cycles for runbooks and
   documentation to maintain accuracy and incorporate new
   learnings from incidents.

## Resources

**Related documents:**

- [Run
  an automated operation powered by Systems Manager
  Automation](../../../systems-manager/latest/userguide/running-simple-automations.md "../../../systems-manager/latest/userguide/running-simple-automations.md")
- [Quick
  Start: Enable your Amazon EC2 instances running Windows Server 2016 to send logs to CloudWatch Logs using the CloudWatch Logs agent](../../../AmazonCloudWatch/latest/logs/QuickStartWindows2016.md "../../../AmazonCloudWatch/latest/logs/QuickStartWindows2016.md")
- [Monitoring
  Windows services with Amazon CloudWatch](https://aws.amazon.com/blogs/mt/monitoring-windows-services-with-amazon-cloudwatch-2/ "https://aws.amazon.com/blogs/mt/monitoring-windows-services-with-amazon-cloudwatch-2/")

**Related tools:**

- [AWS Systems Manager](https://aws.amazon.com/systems-manager/ "https://aws.amazon.com/systems-manager/")
- [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/ "https://aws.amazon.com/cloudwatch/")
