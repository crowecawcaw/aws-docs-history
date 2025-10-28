# Detection

Detection consists of two parts: detection of unexpected or unwanted configuration changes,
and the detection of unexpected behavior. The first can take place at multiple places in an
application delivery lifecycle. Using infrastructure as code (for example, a CloudFormation
template), you can check for unwanted configuration before a workload is deployed by
implementing checks in the CI/CD pipelines or source control. Then, as you deploy a workload
into non-production and production environments, you can check configuration using native AWS,
open source, or AWS Partner tools. These checks can be for configuration that does not meet
security principles or best practices, or for changes that were made between a tested and
deployed configuration. For a running application, you can check whether the configuration has
been changed in an unexpected fashion, including outside of a known deployment or automated
scaling event.

For the second part of detection, unexpected behavior, you can use tools or by alerting on
an increase in a particular type of API call. Using Amazon GuardDuty, you can be alerted when
unexpected and potentially unauthorized or malicious activity occurs within your AWS accounts.
You should also explicitly monitor for mutating API calls that you would not expect to be used
in your workload, and API calls that change the security posture.

Detection allows you to identify a potential security misconfiguration, threat, or
unexpected behavior. It’s an essential part of the security lifecycle and can be used to support
a quality process, a legal or compliance obligation, and for threat identification and response
efforts. There are different types of detection mechanisms. For example, logs from your workload
can be analyzed for exploits that are being used. You should regularly review the detection
mechanisms related to your workload to ensure that you are meeting internal and external
policies and requirements. Automated alerting and notifications should be based on defined
conditions to allow your teams or tools to investigate. These mechanisms are important reactive
factors that can help your organization identify and understand the scope of anomalous activity.

In AWS, there are a number of approaches you can use when addressing detective mechanisms.
The following sections describe how to use these approaches:

###### Best practices

- [SEC04-BP01 Configure service and application logging](sec_detect_investigate_events_app_service_logging.md "sec_detect_investigate_events_app_service_logging.md")
- [SEC04-BP02 Capture logs, findings, and metrics
  in standardized locations](sec_detect_investigate_events_logs.md "sec_detect_investigate_events_logs.md")
- [SEC04-BP03 Correlate and enrich security alerts](sec_detect_investigate_events_security_alerts.md "sec_detect_investigate_events_security_alerts.md")
- [SEC04-BP04 Initiate remediation for non-compliant
  resources](sec_detect_investigate_events_noncompliant_resources.md "sec_detect_investigate_events_noncompliant_resources.md")
