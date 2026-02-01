# FSISEC05: How are you monitoring your ongoing cloud environment for potential threats?

Financial services organizations require in-depth visibility
into the security of their infrastructure and applications.
Achieving this high level of visibility requires the
collection of logs and audit trails and the reservation of
these logs for analytics and reporting. AWS services and
partners' cloud-based solutions help you implement real-time
monitoring in your environment for security threats and
alerting on threats once detected. With generative AI systems,
monitoring extends to model behaviors, response validation,
and potential misuse of AI capabilities.

## FSISEC05-BP01 Track configuration changes

As part of monitoring the environment against threats, it is
critical to identify changes in the security settings that
keep the environment protected. One of the benefits of the
cloud is being able to maintain full visibility of what is
changing in the environment. Establishing a security
baseline of the deployed resources is key for a FIs first
line of defense to manage the risk of its infrastructure, as
well as to track changes over time.

Use
[AWS Config](../../../config/latest/developerguide/WhatIsConfig.md "../../../config/latest/developerguide/WhatIsConfig.md") to audit and evaluate the
configuration settings of your AWS resources. AWS Config
continually tracks the configuration changes that occur in
your resources, and by using
[AWS Config Managed
Rules](../../../config/latest/developerguide/evaluate-config_use-managed-rules.md "../../../config/latest/developerguide/evaluate-config_use-managed-rules.md"), it checks to see if these changes
comply with the your defined desired state. This allows you
to identify and correct configuration deviations as soon as
they happen, and also helps the second and third lines of
defense respond quickly.

For generative AI systems, establish comprehensive
monitoring of model endpoint configurations, prompt catalog
changes, and AI service policy modifications while
implementing guardrails for response validation and tracking
data access patterns across AI workflows.

## FSISEC05-BP02 Detect unusual and unauthorized activity early

Cloud processing of large event data helps detect unauthorized
activity early, which is crucial in a financial institution's
incident response strategy.

Threat detection services like
[Amazon GuardDuty](../../../guardduty/latest/ug/what-is-guardduty.md "../../../guardduty/latest/ug/what-is-guardduty.md") can continually monitor for
unauthorized behavior to protect your AWS accounts and
workloads by focusing on indication of compromise of
credentials, resources, accounts or buckets.
[Enable Amazon GuardDuty on all of the](../../../guardduty/latest/ug/guardduty_organizations.md "../../../guardduty/latest/ug/guardduty_organizations.md")
[accounts](../../../guardduty/latest/ug/guardduty_organizations.md "../../../guardduty/latest/ug/guardduty_organizations.md")
in your AWS Organization and for all of the AWS Regions, as it
can detect unintended activities in unused Regions as well.

AWS Security Hub CSPM provides you with a comprehensive view of the
security state in AWS and helps you check your environment
against
[security
industry standards and best practices](../../../securityhub/latest/userguide/securityhub-standards.md "../../../securityhub/latest/userguide/securityhub-standards.md"). The
activities surrounding Amazon GuardDuty and AWS Security Hub CSPM
must also be tracked and analyzed using AWS CloudTrail, and
they can feed a normalized central data-lake of your
security-related information on
[Amazon Security Lake](https://aws.amazon.com/security-lake/ "https://aws.amazon.com/security-lake/").

Detecting malware in your environment is essential. Consider
enabling
[malware protection](../../../guardduty/latest/ug/malware-protection.md "../../../guardduty/latest/ug/malware-protection.md") in Amazon GuardDuty to identify
your resources that are at risk or have already been
compromised by malware. Whenever Amazon GuardDuty detects
suspicious behavior on an EC2 instance or a container
workload, malware protection automatically initiates an
agentless scan on the EBS volume attached to the resource to
detect the presence of malware.

Additionally, you should also consider scanning data coming in
through third party sources and often landing in your S3
buckets, as they may expose you to potentially malicious files,
objects that may be infected with malware, ransomware, or
viruses. To do this, leverage AWS Partner solutions found in
the
[AWS Marketplace](https://aws.amazon.com/marketplace/solutions/security "https://aws.amazon.com/marketplace/solutions/security").

[AWS CloudTrail insights](../../../awscloudtrail/latest/userguide/view-insights-events.md "../../../awscloudtrail/latest/userguide/view-insights-events.md") helps AWS users identify
and respond to unusual activity associated with API calls by
continually analyzing CloudTrail management events, and should
[be enabled in your trails](../../../awscloudtrail/latest/userguide/logging-insights-events-with-cloudtrail.md "../../../awscloudtrail/latest/userguide/logging-insights-events-with-cloudtrail.md").

You can
[track configuration changes at the edge with AWS Config](../../../AmazonCloudFront/latest/DeveloperGuide/TrackingChanges.md "../../../AmazonCloudFront/latest/DeveloperGuide/TrackingChanges.md"), by recording and tracking CloudFront distribution settings changes.

## Resources

**Related documents:**

- [Cloud security software - AWS Marketplace](https://aws.amazon.com/marketplace/solutions/security "https://aws.amazon.com/marketplace/solutions/security")
- [GuardDuty Malware Protection FAQ](https://aws.amazon.com/guardduty/faqs/#GuardDuty_Malware_Protection "https://aws.amazon.com/guardduty/faqs/#GuardDuty_Malware_Protection")

**Related videos:**

- [The top 7 ways to operationalize AWS Security Hub CSPM](https://www.youtube.com/watch?v=ZEgCsKHPpFI&ab_channel=AWSOnlineTechTalks "https://www.youtube.com/watch?v=ZEgCsKHPpFI&ab_channel=AWSOnlineTechTalks")
