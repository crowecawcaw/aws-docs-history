# MSFTSEC02-BP02 Implement logging to track access and

authorization changes

Regularly log, analyze, and audit user access and authorization
events in your Microsoft systems. Consolidate security events from
Microsoft applications and databases with other architectural
components to enable comprehensive tracing during security
incidents. Implement a centralized security information and event
management (SIEM) system to automate event analysis, allowing your
operations team to identify unusual or suspicious activities.

This integrated approach to security monitoring enhances your
ability to detect and respond to potential threats across your
entire Microsoft environment, strengthening your overall security
posture and enabling more effective incident management.

**Desired outcome:** Establish
comprehensive logging and monitoring capabilities that capture,
analyze, and correlate access and authorization events across
Microsoft workloads, enabling rapid detection of security incidents
and providing detailed audit trails for compliance and forensic
analysis.

**Common anti-patterns:**

- Collecting logs from individual systems without centralized
  aggregation and correlation, making it difficult to identify
  patterns or conduct comprehensive security analysis across the
  Microsoft environment.
- Focusing only on successful authentication events while ignoring
  failed attempts, authorization changes, and privilege
  escalations that could indicate security threats or policy
  violations.
- Storing logs locally on individual systems without proper
  retention, backup, or protection mechanisms, risking log loss
  during security incidents when they are most needed for
  investigation.

**Benefits of establishing this best
practice:**

- Enhanced threat detection through comprehensive logging that
  captures authentication attempts, authorization changes, and
  access patterns, enabling early identification of suspicious
  activities and potential security breaches.
- Improved incident response capabilities through centralized log
  aggregation and correlation that provides security teams with
  complete visibility into user activities and system events
  during security investigations.
- Strengthened regulatory posture through detailed audit trails
  that document user access, privilege changes, and administrative
  activities, supporting regulatory requirements and internal
  security policies.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Implementing comprehensive access and authorization logging
requires a systematic approach to log collection, centralization,
and analysis. Focus on capturing relevant security events from
each Microsoft workload component while protecting, retaining, and
documenting for analysis and compliance purposes.

### Implementation steps

1. Configure Windows Event Logging on your Microsoft workload
   systems to capture security events, including authentication
   attempts, privilege changes, and administrative activities.
2. Enable SQL Server audit logging to track database access,
   permission changes, and data access patterns for
   comprehensive database security monitoring.
3. Set up Amazon CloudWatch Logs or AWS CloudTrail to collect
   and centralize logs from Microsoft workloads running on AWS
   infrastructure.
4. Configure log forwarding from Microsoft applications and
   databases to a centralized SIEM solution such as Amazon
   Security Lake or third-party security platforms.
5. Implement log parsing and normalization for consistent event
   formats, enabling effective correlation across different
   Microsoft technologies and AWS services.
6. Set up automated alerting and monitoring rules to detect
   suspicious access patterns, failed authentication attempts,
   and unauthorized privilege escalations.
7. Establish log retention policies that meet regulatory
   requirements while balancing storage costs and operational
   needs for security analysis.
8. Create regular reporting and analysis procedures to review
   access patterns, identify security trends, and validate the
   effectiveness of access controls.

## Resources

**Related documents:**

- [Security
  Best Practices for Modernizing .NET Framework Applications on
  AWS - Application Logging](../../../prescriptive-guidance/latest/modernization-net-applications-security/logging.md "../../../prescriptive-guidance/latest/modernization-net-applications-security/logging.md")
- [AWS Security Best Practices](../framework/sec-detection.md "../framework/sec-detection.md")

**Related tools:**

- [Amazon CloudWatch Logs](../../../AmazonCloudWatch/latest/logs/WhatIsCloudWatchLogs.md "../../../AmazonCloudWatch/latest/logs/WhatIsCloudWatchLogs.md")
- [AWS CloudTrail](../../../awscloudtrail/latest/userguide/cloudtrail-user-guide.md "../../../awscloudtrail/latest/userguide/cloudtrail-user-guide.md")
- [Amazon
  Security Lake](https://aws.amazon.com/security-lake/ "https://aws.amazon.com/security-lake/")
- [SQL
  Server Audit](https://docs.microsoft.com/en-us/sql/relational-databases/security/auditing/sql-server-audit-database-engine "https://docs.microsoft.com/en-us/sql/relational-databases/security/auditing/sql-server-audit-database-engine")
