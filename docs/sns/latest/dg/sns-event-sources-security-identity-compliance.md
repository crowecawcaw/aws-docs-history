

# Security, identity, & compliance services
<a name="sns-event-sources-security-identity-compliance"></a>

The following table describes how Amazon SNS integrates with AWS security, identity, and compliance services, such as Directory Service, Amazon GuardDuty, Amazon Inspector, and AWS Security Hub CSPM, to provide notifications for directory status changes, security findings, Inspector events, and security hub announcements. 

These integrations help you to maintain robust security practices by offering timely alerts and updates on security and compliance events.


| AWS service | Benefit of using with Amazon SNS | 
| --- | --- | 
| [AWS Directory Service](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/what_is.html) – Provides multiple ways to use Microsoft Active Directory (AD) with other AWS services. | Receive email or text (SMS) messages when the status of your directory changes. For more information, see [Configure directory status notifications](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ms_ad_enable_notifications.html) in the *AWS Directory Service Administration Guide*. | 
| [Amazon GuardDuty](https://docs.aws.amazon.com/guardduty/latest/ug/what-is-guardduty.html) – Provides continuous security monitoring to help to identify unexpected and potentially unauthorized or malicious activity in your AWS environment. | Receive notifications about newly released finding types, updates to the existing finding types, and other functionality changes. For more information, see [Subscribing to GuardDuty announcements SNS topic](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_sns.html) in the *Amazon GuardDuty User Guide*. | 
| [Amazon Inspector](https://docs.aws.amazon.com/inspector/latest/userguide/inspector_introduction.html) – Tests the network accessibility of your Amazon EC2 instances and the security state of your applications that run on those instances. | Receive notifications for Amazon Inspector events. For more information, see [Setting up an SNS topic for Amazon Inspector notifications](https://docs.aws.amazon.com/inspector/latest/userguide/inspector_assessments.html#sns-topic) in the *Amazon Inspector User Guide*. | 
| [AWS Security Hub CSPM](https://aws.amazon.com/security-hub/) – Automates AWS security checks and centralizes security alerts. | Receive notifications about AWS Security Hub CSPM announcements, including notifications about AWS Security Hub CSPM controls or standards that have been added, edited, or retired. For more information, see [Subscribing to AWS Security Hub CSPM announcements with Amazon SNS](https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-announcements.html). | 