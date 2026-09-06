

# Proactive response and alert triaging
<a name="proactive-response-alert-triaging"></a>

AWS Security Incident Response monitors and investigates threat alerts generated from Amazon GuardDuty and third-party threat detection tools using Security Hub CSPM integrations. AWS Security Incident Response automatically triages all supported alerts so your team can focus on the most critical issues.

**Important**  
AWS Security Incident Response doesn't require you to enable Amazon GuardDuty. However, the proactive response feature relies on receiving threat findings from detection services. If you don't have Amazon GuardDuty or Security Hub CSPM configured to ingest findings, AWS Security Incident Response won't have alerts to monitor and investigate, which limits the value of this feature.

AWS Security Incident Response monitors and investigates findings across all covered accounts and active supported AWS Regions in your organization. To facilitate this functionality, AWS Security Incident Response automatically creates a service-linked role in all covered member accounts within your AWS Organizations.

If you [onboard](deploy-configure.md) to AWS Security Incident Response in the AWS Management Console, Security Incident Response automatically creates the `AWSServiceRoleForSecurityIncidentResponse_Triage` service-linked role in your AWS Organizations management account and in all accounts that are in scope. If you onboarding using the API/CLI, then you must create the role manually. For more information, see [Enable Security Incident Response and configure your incident response team using the API/CLI](enable-sir-using-cli.md).

If you experience onboarding issues or need help enabling Amazon GuardDuty or Security Hub CSPM, [create an AWS Support case](https://docs.aws.amazon.com/awssupport/latest/user/case-management.html#creating-a-support-case) for assistance.

**Note**  
If you have questions about Amazon GuardDuty suppression rules, alert triaging configurations, or proactive response workflows, you can create an AWS supported case with the case type **Investigations and Inquiries** to consult with the AWS Security Incident Response team. For more information, see [Create an AWS supported case](create-an-aws-supported-case.md).

**Containment:** In the event of a security incident, AWS Security Incident Response can execute containment actions to quickly mitigate the impact, such as isolating compromised hosts or rotating credentials. Security Incident Response doesn't enable containment capabilities by default. To execute these containment actions, you must first grant the necessary permissions to the service. This can be done by deploying an [AWS CloudFormation StackSet](https://docs.aws.amazon.com/security-ir/latest/userguide/working-with-stacksets.html), which creates the required roles.