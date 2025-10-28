# Amazon GuardDuty for Amazon EBS

Amazon GuardDuty is a threat detection service that helps protect your accounts, containers,
workloads, and the data within your AWS environment. Using machine learning (ML) models,
and anomaly and threat detection capabilities, GuardDuty continuously monitors different log
sources and runtime activity to identify and prioritize potential security risks and
malicious activities in your environment.

The [Malware Protection](../../../guardduty/latest/ug/malware-protection.md "../../../guardduty/latest/ug/malware-protection.md") feature within GuardDuty scans the Amazon EBS volumes associated with
your Amazon EC2 instances and container workloads to detect potential threats. GuardDuty offers two
ways to do this:

- **Enable Malware Protection** — When GuardDuty
  generates a finding that is indicative of potential presence of malware in an Amazon EC2
  instance or a container workload, it will automatically initiate a malware scan on the
  potentially compromised resource.
- **Use on-demand malware scan without enabling Malware Protection**
  — Provide the Amazon Resource Name (ARN) of your Amazon EC2 instance to initiate an
  on-demand scan.
  For more information, see the [Amazon GuardDuty User Guide](../../../guardduty/latest/ug/what-is-guardduty.md "../../../guardduty/latest/ug/what-is-guardduty.md").
