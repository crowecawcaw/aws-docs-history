# Implementation priorities

For security management, we recommend that you deploy your
security capabilities (XDR, CSPM, etc.) using the same mechanisms
as the base foundation of capabilities for
each of your accounts. In the [Controls](controls.md "controls.md")
section, we recommend that you begin with assessing your risk
posture and
[developing
a threat model](https://aws.amazon.com/blogs/security/how-to-approach-threat-modeling/ "https://aws.amazon.com/blogs/security/how-to-approach-threat-modeling/"), and thereafter selecting appropriate
controls for each environment. In addition, you should set a
foundation with specific security tools aligned to your
environments and accounts, additional logging, and integration to
your incident management and security analytics capabilities.

## Design a Well-Architected security environment

Design capabilities with governance and security instrumentation
in mind, following the best practices described in the
[AWS Well-Architected Security Pillar](../security-pillar/welcome.md "../security-pillar/welcome.md"). Your
[security
foundations](../framework/a-sec-security.md "../framework/a-sec-security.md") should include:

- Separating and securing your workloads across a multi-account
  strategy
- Identifying and validating control objectives based on your
  compliance requirements and risk assessments
- Recognizing and staying up to date with the latest security
  threats and vectors, recommendations, and effective controls
- Establishing secure baselines and templates for security
  mechanisms that are tested and validated continually as part
  of your build, pipelines, and processes
- Identifying and prioritizing risks using threat modeling
- Evolving the security posture of your workloads using new features and enhancements
  of AWS and AWS Partner services
- Enabling encryption at rest and in motion for cloud storage,
  databases and traffic that includes sensitive data in motion

## Choose security tools to match your enterprise needs

Security monitoring tools should allow for granular security
monitoring across infrastructure, applications, and workloads as
well as provide aggregated views for pattern analysis. As with all
other security management tools, it is important to extend your
XDR tools to provide functions to assess, detect, respond, and
remediate the security of your applications, resources, and
environments on AWS. Using these tools with the interoperable
functions of the M&G Guide can provide a mechanism for you to
enable further use cases for compliance monitoring, incident
response, DevSecOps integration, risk assessment and
visualization. Cloud Security Posture Management (CSPM) tools can
also be used to manage and remediate common vulnerabilities and
exposures (CVEs) in your AWS environments. Use a vulnerability
management solution that assesses infrastructure and applications
for vulnerabilities or deviations from best practices, and
produces a detailed list of findings prioritized by level of
severity. 

## Analyze and model for threats

Implement continual monitoring and measurement against industry
and security benchmarks. When designing your instrumentation
approach, determine what types of event data and information will
best inform your security management functions. This monitoring
should encompass several attack vectors including service usage.
Your security foundations should include a comprehensive secure
logging and analytics capability across your multi-account
environments that includes the ability to correlate events from
multiple sources.

Prevent changes to this configuration with specific controls and
guardrails. AWS Security Hub and AWS Partner tools provide
dashboards across a multi-account environment and should be
integrated with
[event-triggering
systems](https://aws.amazon.com/solutions/implementations/aws-security-hub-automated-response-and-remediation/ "https://aws.amazon.com/solutions/implementations/aws-security-hub-automated-response-and-remediation/") in AWS for security and incident event management
functions. Develop thresholds and metrics based on expected
behavior of your environments. Use anomaly detection to identify
unintended activities when thresholds are exceeded. Configure and
monitor Amazon CloudWatch alarms for exceeded thresholds across
IAM activity, resource creation, failed access attempts, policy
and configuration changes, VPC-related changes (security groups,
NACLs, gateways, and route tables), API calls, and activities in
unapproved AWS Regions.

Develop a threat modeling practice to engage with business
stakeholders, cloud infrastructure architects, compliance,
application developers, security and other key stakeholders.
The AWS Well-Architected Framework calls out threat modeling as a
specific best practice within the Security Pillar, under the
question [SEC 1: How do you securely operate your workload?](../framework/a-sec-security.md "../framework/a-sec-security.md")
Preventive, detective, and responsive controls should be put in
place as responses to both workload and environment level threats
identified in threat modeling exercises.

Enable log aggregation as a foundation for your threat modeling
and log analytics capabilities that is extended as new accounts or
environments are created, updated, or deleted. Use XDR with
multiple telemetry sources to identify if correlated events
qualify as recordable incidents. Use the threat model as the basis
for table top exercises, building incident response playbooks and
runbooks, and develop automated testing. Codify your compliance
objectives using AWS Config or AWS Partner products.

## Automate incident management workflows, findings, and campaigns

The
[Security
Pillar](../security-pillar/welcome.md "../security-pillar/welcome.md") outlines how to build a comprehensive detective
capability with options that include automated remediation and AWS
Partner integrations. This capability is enabled through the
[configuration
of environments](../security-pillar/configure.md "../security-pillar/configure.md") with centralized analysis of logs,
findings, and metrics. Typical automation might include AWS Lambda
function “responders” that react to specific changes in the
environment, orchestrating automatic scaling, isolating suspect
system components, deploying just-in-time investigative tools, and
creating workflow and ticketing to shut down and learn from a
closed loop organizational response. Each account, application, or
resource should be provisioned with a baseline configuration
aligned with your security operations. This includes provisioning
specific security tools, which also align to your observability
requirements. Develop remediation processes which allow you to
isolate cloud resources for forensic analysis.

## Select, measure, and continually improve your security metrics

Follow the guidance of “_what gets measured, gets done_”. Implement
metrics for each part of your security organization and review
regularly to verify you have the right level of organization
buy-in and attention. Measure the performance of your security
operations along with the threats themselves. Include metrics
around your security operations paired with metrics around
security campaigns, findings, and tools. For example, mean time to
identify (MTTI) root cause and mean time to respond (MTTR) provide
insights into your security incident response effectiveness. Drive
operational insights and reviews to continually improve your
threat modeling, threat detection, incident management, and
response and remediation capabilities.
