

# SEC01-BP07 Evaluate and implement new security services and features regularly

 Cloud providers release new security capabilities continually. If you do not track them, your controls fall behind. Implement a repeatable way to learn about, evaluate, and adopt new features to keep your security posture current as the environment and threats evolve. 

 **Desired outcome:** 
+  You have a standard practice that informs you of new features and services as they release. 
+  You evaluate how new capabilities affect the design of current and planned controls. 
+  You share awareness of new security capabilities across the teams that build and operate workloads. 

 **Common anti-patterns:** 
+  Teams do not subscribe to provider blogs or feeds, so they learn of relevant features late. 
+  Information about new security services comes mainly from second-hand sources. 
+  Users in the organization are not encouraged to stay informed of updates. 

 **Benefits of establishing this best practice:** 
+  Informed decisions about new controls become possible as capabilities emerge. 
+  Awareness of newly released security capabilities improves across teams. 
+  Workloads adopt protections against new and emerging threats sooner. 

 **Level of risk exposed if this best practice is not established:** Low 

## Implementation guidance
<a name="implementation-guidance"></a>

 AWS announces new security services and features across several channels. The primary written sources are [AWS What's New](https://aws.amazon.com/new/), the [AWS News Blog](https://aws.amazon.com/blogs/aws/), the [AWS Security Blog](https://aws.amazon.com/blogs/security/), [AWS Security Bulletins](https://aws.amazon.com/security/security-bulletins/), and the [AWS documentation overview](https://aws.amazon.com/documentation-overview/). Filter these sources to what is relevant to your workloads. 

 Push mechanisms scale better than checking pages manually. You can subscribe to a daily summary of updates through an Amazon Simple Notification Service (Amazon SNS) topic, and to service-specific topics such as [Amazon GuardDuty](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_sns.html) and [AWS Security Hub CSPM](https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-announcements.html). Announcements also arrive at conferences, such as the AWS re:Inforce security conference and the broader AWS re:Invent conference, with deep-dive sessions available afterward on the [AWS Events channel](https://www.youtube.com/c/AWSEventsChannel). 

 Assign owners to triage incoming updates, decide which ones matter for your controls, and share the relevant ones with the teams that build and operate workloads. Your AWS account team is another channel for updates and recommendations. If you subscribe to AWS Enterprise Support, you receive regular updates from a Technical Account Manager (TAM) and can schedule review meetings to discuss how new capabilities apply to your environment. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Subscribe to update channels:** Subscribe to the relevant blogs and bulletins with your preferred RSS reader, and subscribe to the [AWS Daily Feature Updates](https://aws.amazon.com/blogs/aws/subscribe-to-aws-daily-feature-updates-via-amazon-sns/) SNS topic for a comprehensive daily summary. 

1.  **Select events to attend:** Evaluate which [AWS events](https://aws.amazon.com/events/) to attend to learn first-hand about new features and services relevant to your workloads. 

1.  **Engage your AWS account team:** Ask your AWS account team about recent security updates and recommendations, reaching them through the [Sales Support form](https://aws.amazon.com/contact-us/sales-support/) if you do not have direct contact details. 

1.  **Consider Enterprise Support:** Consider [AWS Enterprise Support](https://aws.amazon.com/premiumsupport/plans/enterprise/) for regular consultations with a Technical Account Manager on updating security services and features. 

1.  **Share updates across teams:** Assign ownership for triaging updates and distributing the relevant ones to the teams that build and operate workloads, so awareness does not stop with one person. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [SEC01-BP03 Stay up to date with security threats and recommendations](sec01-bp03.md) 
+  [COST01-BP04 Keep up-to-date with new service releases](cost01-bp04.md) 

 **Related documents:** 
+  [AWS What's New](https://aws.amazon.com/new/) 
+  [AWS Security Blog](https://aws.amazon.com/blogs/security/) 