# Opting out of using your data for service

improvement

You can choose to opt out of having your data used to develop and improve GuardDuty and other
AWS security services by using the AWS Organizations opt-out policy. You can choose to opt out even
if GuardDuty doesn't currently collect any such data. For more information about how to opt out,
see [AI services
opt-out policies](../../../organizations/latest/userguide/orgs_manage_policies_ai-opt-out.md "../../../organizations/latest/userguide/orgs_manage_policies_ai-opt-out.md") in the _AWS Organizations User Guide_.

###### Note

For you to use the opt-out policy, your AWS accounts must be centrally managed by
AWS Organizations. If you haven't already created an organization for your AWS accounts, see [Creating
and managing an organization](../../../organizations/latest/userguide/orgs_manage_org.md "../../../organizations/latest/userguide/orgs_manage_org.md") in the _AWS Organizations User Guide_.

Opting out has the following effects:

- GuardDuty will delete the data that it collected and stored for service improvement
  purposes prior to your opt out (if any).
- After you opt out, GuardDuty will no longer collect or store this data for service
  improvement purposes.
  The following topics explain how each feature within GuardDuty potentially handles your data
  for service improvement.

###### Contents

- [GuardDuty Runtime Monitoring](#runtime-monitoring-data-opt-out "#runtime-monitoring-data-opt-out")
- [GuardDuty Malware Protection](#malware-protection-data-opt-out "#malware-protection-data-opt-out")

## GuardDuty Runtime Monitoring

GuardDuty Runtime Monitoring provides runtime threat detection for Amazon Elastic Kubernetes Service (Amazon EKS) clusters,
AWS Fargate Amazon Elastic Container Service(Amazon ECS) only, and Amazon Elastic Compute Cloud (Amazon EC2) instances in your AWS
environment. After you enable Runtime Monitoring and deploy the GuardDuty security agent for your
resource, GuardDuty starts to monitor and analyze the runtime events associated with your
resource. These runtime event types include process events, container events, DNS events,
and more. For more information, see [Collected runtime event types that GuardDuty
uses](runtime-monitoring-collected-events.md "runtime-monitoring-collected-events.md").

GuardDuty collects both commands (such as `curl`,
`systemctl`, and `cron`) and their associated arguments (such as
`start`, `stop`, `disable`) from your workloads.
For example, when someone runs `systemctl stop `service-name``,
 GuardDuty captures both the command `systemctl` and its arguments 
 `stop `service-name``. This detailed information helps GuardDuty to detect sophisticated
threats by analyzing command patterns and correlating multiple events. For example, GuardDuty
can identify when an attacker attempts to disable security services or executes known malicious files. While
GuardDuty actively uses this data for threat detection, it **doesn't**
currently use these commands and arguments for service improvement purposes (it may do so in the future).
Your trust, privacy, and
the security of your content are our highest priority, and ensure that our use complies with
our commitments to you. For more information, see [Data Privacy FAQ](https://aws.amazon.com//compliance/data-privacy-faq/ "https://aws.amazon.com//compliance/data-privacy-faq/").

## GuardDuty Malware Protection

GuardDuty Malware Protection scans and detects malware contained in EBS volumes attached to
your potentially compromised Amazon EC2 instance and container workloads, newly uploaded
files in your selected Amazon S3 buckets, and backup resources. Currently, GuardDuty doesn't collect or use detected
malware for service improvement. However, in the future, when GuardDuty Malware Protection
identifies an EBS volume file, backup file, or an S3 file as being malicious or harmful, GuardDuty Malware
Protection will collect and store this file to develop and improve its malware detections,
and the GuardDuty service. This file may also be used to develop and improve other AWS
security services. Your trust, privacy, and the security of your content are our highest
priority, and ensure that our use complies with our commitments to you. For more
information, see [Data Privacy
FAQ](https://aws.amazon.com//compliance/data-privacy-faq/ "https://aws.amazon.com//compliance/data-privacy-faq/").
