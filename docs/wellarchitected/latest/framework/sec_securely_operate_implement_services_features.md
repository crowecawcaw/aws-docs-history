# SEC01-BP08 Evaluate and implement new security services and

features regularly

Evaluate and implement security services and features from AWS and
AWS Partners that help you evolve the security posture of your
workload. 

**Desired outcome:** You have a
standard practice in place that informs you of new features and
services released by AWS and AWS Partners. You evaluate how these
new capabilities influence the design of current and new controls
for your environments and workloads.

**Common anti-patterns:**

- You don't subscribe to AWS blogs and RSS feeds to learn of
  relevant new features and services quickly
- You rely on news and updates about security services and
  features from second-hand sources
- You don't encourage AWS users in your organization to stay
  informed on the latest updates

**Benefits of establishing this best
practice:** When you stay on top of new security services
and features, you can make informed decisions about the
implementation of controls in your cloud environments and workloads.
These sources help raise awareness of the evolving security
landscape and how AWS services can be used to protect against new
and emerging threats.  

**Level of risk exposed if this best practice
is not established:** Low

## Implementation guidance

AWS informs customers of new security services and features
through several channels:

- [AWS What's
  New](https://aws.amazon.com/new "https://aws.amazon.com/new")
- [AWS News
  Blog](https://aws.amazon.com/blogs/aws/ "https://aws.amazon.com/blogs/aws/")
- [AWS Security Blog](https://aws.amazon.com/blogs/security/ "https://aws.amazon.com/blogs/security/")
- [AWS Security Bulletins](https://aws.amazon.com/security/security-bulletins/ "https://aws.amazon.com/security/security-bulletins/")
- [AWS documentation overview](https://aws.amazon.com/documentation/ "https://aws.amazon.com/documentation/")

You can subscribe to an
[AWS Daily Feature Updates](https://aws.amazon.com/blogs/aws/subscribe-to-aws-daily-feature-updates-via-amazon-sns/ "https://aws.amazon.com/blogs/aws/subscribe-to-aws-daily-feature-updates-via-amazon-sns/") topic using Amazon Simple Notification Service (Amazon SNS) for a comprehensive daily
summary of updates. Some security services, such as
[Amazon GuardDuty](../../../guardduty/latest/ug/guardduty_sns.md "../../../guardduty/latest/ug/guardduty_sns.md") and
[AWS Security Hub CSPM](../../../securityhub/latest/userguide/securityhub-announcements.md "../../../securityhub/latest/userguide/securityhub-announcements.md"), provide their own SNS topics to stay informed
about new standards, findings, and other updates for those
particular services.

New services and features are also announced and described in
detail during
[conferences,
events, and webinars](https://aws.amazon.com/events/ "https://aws.amazon.com/events/") conducted around the globe each year.
Of particular note is the annual
[AWS re:Inforce](https://reinforce.awsevents.com/ "https://reinforce.awsevents.com/") security conference and the more
general [AWS re:Invent](https://reinvent.awsevents.com/ "https://reinvent.awsevents.com/") conference. The previously-mentioned AWS news
channels share these conference announcements about security and
other services, and you can view deep dive educational breakout
sessions online at the
[AWS Events channel](https://www.youtube.com/c/AWSEventsChannel "https://www.youtube.com/c/AWSEventsChannel") on YouTube.

You can also ask your
[AWS account team](https://aws.amazon.com/startups/learn/meet-your-aws-account-team "https://aws.amazon.com/startups/learn/meet-your-aws-account-team") about the latest security service updates and
recommendations. You can reach out to your team through the
[Sales
Support form](https://aws.amazon.com/contact-us/sales-support/ "https://aws.amazon.com/contact-us/sales-support/") if you do not have their direct contact
information. Similarly, if you subscribed to
[AWS Enterprise Support,](https://aws.amazon.com/premiumsupport/plans/enterprise/ "https://aws.amazon.com/premiumsupport/plans/enterprise/")you will receive weekly updates from
your Technical Account Manager (TAM) and can schedule a regular
review meeting with them.

### Implementation steps

1. Subscribe to the various blogs and bulletins with your
   favorite RSS reader or to the Daily Features Updates SNS
   topic.
2. Evaluate which AWS events to attend to learn first-hand
   about new features and services.
3. Set up meetings with your AWS account team for any questions
   about updating security services and features.
4. Consider subscribing to Enterprise Support to have regular
   consultations with a Technical Account Manager (TAM).

## Resources

**Related best practices:**

- [PERF01-BP01
  Learn about and understand available cloud services and
  features](perf_architecture_understand_cloud_services_and_features.md "perf_architecture_understand_cloud_services_and_features.md")
- [COST01-BP07
  Keep up-to-date with new service releases](cost_cloud_financial_management_scheduled.md "cost_cloud_financial_management_scheduled.md")
