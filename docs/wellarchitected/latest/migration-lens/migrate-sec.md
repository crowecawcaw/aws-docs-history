# Migrate

As the migration progresses, security remains top priority. It's
essential to understand the data security and compliance,
establish a secure credential mechanism, and have robust
mechanisms in place for monitoring, identifying, and responding to
any security incidents or anomalies. This involves not only
employing the right tools, but also training teams and preparing
them to respond effectively. In this phase, you also implement
mechanisms to protect the migrated resources of compute, network,
databases and applications.

| MIG-SEC-12: Have you performed a security review of your migration tools? |
| ------------------------------------------------------------------------- |
|                                                                           |

When using AWS migration tools to move data and applications
from on-premises or other cloud environments to AWS, it's
essential to consider security throughout the migration process.
This section contains key security considerations when using AWS
migration tools.

## MIG-SEC-BP-12.1: Understand the data security and compliance

This BP applies to the following best practice areas: Data
protection

### Implementation guidance

**Suggestion 12.1.1:**
Verify data encryption and integrity.

Data transferred during the migration process should be
[encrypted
in transit](../../../prescriptive-guidance/latest/encryption-best-practices/welcome.md "../../../prescriptive-guidance/latest/encryption-best-practices/welcome.md"). [AWS migration tools](../../../whitepapers/latest/overview-aws-cloud-data-migration-services/overview-aws-cloud-data-migration-services.md "../../../whitepapers/latest/overview-aws-cloud-data-migration-services/overview-aws-cloud-data-migration-services.md"), such as AWS DataSync, [AWS Database Migration Service](https://repost.aws/knowledge-center/validation-feature-dms "https://repost.aws/knowledge-center/validation-feature-dms"), and [AWS Application Migration Service](https://aws.amazon.com/application-migration-service/ "https://aws.amazon.com/application-migration-service/") support TLS encryption
to secure data as it moves between your on-premise and AWS
environments. Verify the integrity of data during migration
by using cryptographic hashes or checksums. This helps
detect any unauthorized changes or tampering during transit.

**Suggestion 12.1.2:
Implement** secure
credential management.

Safeguard access credentials used by migration tools. Follow
the principle of [least
privilege](../../../IAM/latest/UserGuide/best-practices.md#grant-least-privilege "../../../IAM/latest/UserGuide/best-practices.md#grant-least-privilege"), granting only the necessary permissions to
migration tools and their associated IAM roles or users. Use
a credential management system, such as [AWS Secrets Manager](https://aws.amazon.com/secrets-manager/ "https://aws.amazon.com/secrets-manager/"), to limit sharing and proliferations
of credentials. Also, limit the use of long-term credentials
when possible, and use [IAM
Roles Anywhere](../../../rolesanywhere/latest/userguide/introduction.md "../../../rolesanywhere/latest/userguide/introduction.md") to prevent the need for storage
secrets.

| MIG-SEC-13: How do you detect and investigate security events? |
| -------------------------------------------------------------- |
|                                                                |

Migrating your workloads from on-premises to AWS also requires
you to update your security detection and investigation
processes. Detective controls, crucial for governance and
compliance, help identify potential threats and support threat
identification and response. These controls include asset
inventory for informed decision-making (you must know what
resources you have so you know how to protect them) and internal
auditing of information systems to align practices with policies
and correctly set automated alerting notifications. Such
controls are pivotal in pinpointing and understanding anomalous
activity.

## MIG-SEC-BP-13.1: Understand AWS service capabilities for event detection and investigation

This BP applies to the following best practice areas: Incident
response

### Implementation guidance

**Suggestion
13.1.1:** Configure
service and application logging.

Retain [security
event logs](../../../prescriptive-guidance/latest/logging-monitoring-for-application-owners/logging-applications-aws-cloud.md "../../../prescriptive-guidance/latest/logging-monitoring-for-application-owners/logging-applications-aws-cloud.md") from services and applications, a
fundamental principle for audit, investigations, and
operational use cases. This retention must be in line with
governance, risk, and compliance (GRC) requirements and
industry-specific standards. Ahead of security
investigations, capture logs to reconstruct AWS account
activity. Select [log
sources](../../../prescriptive-guidance/latest/logging-monitoring-for-application-owners/aws-services-logging-monitoring.md "../../../prescriptive-guidance/latest/logging-monitoring-for-application-owners/aws-services-logging-monitoring.md") pertinent to your workloads based on your
business use cases and any regulatory or compliance
requirements you may have. Establish a logging trail for
each AWS account, and in each region using [AWS CloudTrail](../../../awscloudtrail/latest/userguide/best-practices-security.md "../../../awscloudtrail/latest/userguide/best-practices-security.md") or an AWS Organizations trail, store logs
in a dedicated and centralized Amazon S3 bucket.

**Suggestion 13.1.2:**
Analyze logs, findings, and metrics centrally.

As you migrate to AWS, security operations teams should use
advanced data search and analytics tools, especially given
the volume of data from complex architectures and
applications. Reliance on manual data analysis is not suited
for the majority of most customer security requirements and
could impact your ability to investigate potential security
issues in a timely manner. Use services such as [AWS Security Hub](https://aws.amazon.com/security-hub/ "https://aws.amazon.com/security-hub/") to aggregate security events and alerts
from other security services, evaluate your security
posture, and automate remediations. [Amazon
Detective](https://aws.amazon.com/detective/ "https://aws.amazon.com/detective/") can help you investigate security events by
contextualizing events in relationship across several
service and log sources.

For more detail, see the following: 

- [Collect, analyze, and display Amazon CloudWatch Logs in a single dashboard with the Centralized Logging on AWS solution](../../../solutions/latest/centralized-logging-on-aws/solution-overview.md "../../../solutions/latest/centralized-logging-on-aws/solution-overview.md")
- [Amazon Security Lake](https://aws.amazon.com/security-lake/ "https://aws.amazon.com/security-lake/")
- [AWS Security Competency Partners](https://aws.amazon.com/security/partner-solutions/#Logging_and_Monitoring "https://aws.amazon.com/security/partner-solutions/#Logging_and_Monitoring")
- [Searching
  and analyzing logs in CloudWatch](../../../prescriptive-guidance/latest/implementing-logging-monitoring-cloudwatch/cloudwatch-search-analysis.md "../../../prescriptive-guidance/latest/implementing-logging-monitoring-cloudwatch/cloudwatch-search-analysis.md")

**Suggestion
13.1.3:** Automate
and implement the response to security events.

Using [automation](https://aws.amazon.com/solutions/implementations/automated-security-response-on-aws/ "https://aws.amazon.com/solutions/implementations/automated-security-response-on-aws/")
to investigate and remediate events reduces human effort and
error, [quickens
responses](../../../whitepapers/latest/aws-security-incident-response-guide/detection.md "../../../whitepapers/latest/aws-security-incident-response-guide/detection.md"), and allows you to scale investigation
capabilities. Regular reviews help you tune automation tools
and continually iterate. AWS provides guidance on how this
can be achieved using a combination of AWS security services
and patterns. Consider the impact to the availability of
your workloads carefully when implementing security
automations, as you may not be able to fully automate all [remediation
activities](https://youtu.be/nyh4imv8zuk "https://youtu.be/nyh4imv8zuk").

For more detail, see [Threat management in the cloud: Amazon GuardDuty and AWS Security Hub](https://youtu.be/vhYsm5gq9jE "https://youtu.be/vhYsm5gq9jE").

| MIG-SEC-14: Do you have security incident response capabilities in place? |
| ------------------------------------------------------------------------- |
|                                                                           |

To migrate your security incident response capabilities from
on-premises to AWS, careful planning and adopting cloud-native
practices are essential. It's crucial to understand AWS security
incident response concepts, prepare and educate your teams, and
identify automation-based remediation methods for faster and
more consistent responses. Additionally, it is key to understand
your compliance and regulatory requirements for your security
incident response program, and how they relate to building a
security incident response program to fulfill those
requirements. 

## MIG-SEC-BP-14.1: Understand AWS best practices for incident response

This BP applies to the following best practice areas: Incident
response

### Implementation guidance

**Suggestion
14.1:** Develop and test an incident response plan.

The first document to develop for incident response is the
[incident
response plan](../../../whitepapers/latest/aws-security-incident-response-guide/detection.md "../../../whitepapers/latest/aws-security-incident-response-guide/detection.md"), which is designed to serve
as the foundation for your incident response program. It
typically includes:

1. **An incident response team
   overview**: Outlines the goals and functions of
   the incident response team.
2. **Roles and
   responsibilities**: Lists stakeholders and
   their incident roles.
3. **A communication plan**:
   Details contact information and how to communicate
   during incidents. Emphasizes the best practice of having
   out-of-band communication as a
   backup. 

[AWS Wickr](https://aws.amazon.com/wickr/ "https://aws.amazon.com/wickr/") can be used as a secure out-of-band
communications channel. 4. **Phases of incident response and
actions to take**: Enumerates response phases
(like detect, analyze, eradicate, contain, and recover)
and associated high-level actions. 5. **Incident severity and
prioritization definitions**: Explains incident
severity classification, prioritization, and their
impact on escalation procedures.

While these sections are common, each organization's plan is
unique and should be tailored accordingly.

| MIG-SEC-15: How do you protect your compute and network resources in AWS? |
| ------------------------------------------------------------------------- |
|                                                                           |

Compute resources that support your workloads require multiple
layers of defense to help protect from external and internal
threats. Compute resources include EC2 instances, containers,
AWS Lambda functions, database services, and IoT devices.

## MIG-SEC-BP-15.1: Protect your network resources

This BP applies to the following best practice areas:
Infrastructure protection 

### Implementation guidance

**Suggestion 15.1.1:** Create
a layered networking architecture with isolation boundaries.

Components such as Amazon Elastic Compute Cloud (Amazon EC2)
instances, Amazon Relational Database Service (Amazon RDS)
database clusters, and AWS Lambda functions that share
reachability requirements can be segmented into layers
formed by subnets. Consider deploying serverless workloads,
such as [Lambda](../../../lambda/index.md "../../../lambda/index.md")
functions, within a VPC or behind an [Amazon API Gateway](../../../apigateway/latest/developerguide/welcome.md "../../../apigateway/latest/developerguide/welcome.md"). [AWS Fargate](https://aws.amazon.com/fargate/getting-started/ "https://aws.amazon.com/fargate/getting-started/") tasks (and all other compute workloads) that
have no need for internet access should be placed in subnets
with no route to or from the internet. This layered approach
mitigates the impact of a single layer misconfiguration,
which could allow unintended access. For AWS Lambda, you can
run your functions in your VPC to take advantage of
VPC-based controls. Regardless of your workload type, it is
imperative to understand the data flow between layers of
your application, and implement the controls necessary to
restrict ingress and egress traffic to only authorized users
and services.

For more detail, see the following: 

- [Well-Architected
  Lab - Automated Deployment of VPC](https://catalog.workshops.aws/well-architected-security/en-US/4-infrastructure-protection/automated-deployment-of-vpc "https://catalog.workshops.aws/well-architected-security/en-US/4-infrastructure-protection/automated-deployment-of-vpc")
- [Amazon VPC | AWS Security Blog](https://aws.amazon.com/blogs/security/tag/amazon-vpc/ "https://aws.amazon.com/blogs/security/tag/amazon-vpc/")

**Suggestion 15.1.2:** Create centralized policies for network security.

Use [AWS Firewall Manager](https://aws.amazon.com/firewall-manager/ "https://aws.amazon.com/firewall-manager/") to centrally configure and manage your network security policies across all accounts and applications in your organization, simplifying the administration of AWS WAF, AWS Shield Advanced, AWS Network Firewall, and [Amazon VPC](https://www.wellarchitectedlabs.com/security/200_labs/200_automated_deployment_of_vpc/ "https://www.wellarchitectedlabs.com/security/200_labs/200_automated_deployment_of_vpc/") security groups.

With [AWS Network Firewall](https://aws.amazon.com/network-firewall/ "https://aws.amazon.com/network-firewall/"), you can define firewall rules that
provide fine-grained control over network traffic. Network Firewall works together with AWS Firewall Manager, so you
can build policies based on Network Firewall rules and then
centrally apply those policies across your virtual private
clouds (VPCs) and accounts.

| MIG-SEC-16: What are your authentication and authorization processes for applications and databases? |
| ---------------------------------------------------------------------------------------------------- |
|                                                                                                      |

When migrating databases and applications to AWS, it's essential
to have robust authentication and authorization controls to
secure access to sensitive data. AWS offers several services and
best practices to achieve this.

## MIG-SEC-BP-16.1: Manage authentication for applications and databases

This BP applies to the following best practice
areas: 

[Identity
and access management](../container-build-lens/identity-and-access-management.md "../container-build-lens/identity-and-access-management.md")

### Implementation guidance

**Suggestion 16.1.1**:
Consider more secure database authentication
and authorization methods.

When moving databases to AWS managed services, such as RDS
(Relational Database Service) and Aurora databases, you can
enable

[IAM
database authentication](../../../AmazonRDS/latest/UserGuide/UsingWithRDS.md "../../../AmazonRDS/latest/UserGuide/UsingWithRDS.md"). This allows you to use IAM
roles instead of static or [hard
coded credentials](../../../secretsmanager/latest/userguide/hardcoded-db-creds.md "../../../secretsmanager/latest/userguide/hardcoded-db-creds.md") to authenticate and access the
databases, improving security by removing the need to manage
database passwords. Define database-level roles and
permissions to control access to specific tables, views, and
stored procedures within your databases.

**Suggestion 16.1.2**:
Consider stronger application authentication and
authorization mechanisms for applications.

Implement strong authentication mechanisms for your
applications. Use protocols like OAuth 2.0 or OpenID Connect
for web applications, and consider token-based
authentication for APIs. Implement [role-based
access control (RBAC)](https://aws.amazon.com/identity/ "https://aws.amazon.com/identity/") within your applications. Map
AWS IAM roles to application roles, and control access to
application features and data based upon business need. [Verified Permissions](https://aws.amazon.com/verified-permissions/ "https://aws.amazon.com/verified-permissions/") can also be leveraged to help
manage permissions and fine-grained authorizations in
applications.

**Suggestion 16.1.3**:
Use AWS Secrets Manager
for storing credentials.

Use [AWS Secrets Manager](https://aws.amazon.com/secrets-manager/ "https://aws.amazon.com/secrets-manager/") to manage, retrieve, and rotate
database credentials, application credentials, OAuth tokens,
API keys, and other secrets throughout their lifecycles.
Secrets Manager helps you improve your security posture,
because you no longer need [hard-coded
credentials](../../../secretsmanager/latest/userguide/hardcoded-db-creds.md "../../../secretsmanager/latest/userguide/hardcoded-db-creds.md") in application source code. Storing the
credentials in Secrets Manager helps avoid possible
compromise by anyone who can inspect your application or the
components.
