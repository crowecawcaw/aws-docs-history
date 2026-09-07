

# LSSEC01-BP03 Set up alerts for IAM configuration changes and perform audits
<a name="lssec01-bp03"></a>

 Compliance-related access rules should be automated with alerting or automated risk mitigation actions. 

 **Desired outcome:** Ability to mitigate the risk of irregular access configurations. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 Set up alerts for monitoring activities by users with increased privileges. 

 Perform periodic audits of control effectiveness. 

### Implementation steps
<a name="implementation-steps"></a>

1.  [Set up alerts](https://aws.amazon.com/blogs/security/how-to-receive-alerts-when-your-iam-configuration-changes/) to notify on AWS IAM configuration changes including when an [IAM user is created](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/send-a-notification-when-an-iam-user-is-created.html) or when conflicting permissions are added to a user or role, such as being able to approve its own requests on a given workflow. 

   1.  The added notification can be set up using a combination of [AWS CloudTrail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-user-guide.html), [Amazon CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html), and [Amazon SNS](https://docs.aws.amazon.com/sns/latest/dg/welcome.html). 

1.  Automate permissions management and refinement through [IAM Access Analyzer](https://aws.amazon.com/iam/access-analyzer/) with security integration workflows that alert teams to access policy changes. For unused roles, access keys, or passwords, [IAM Access Analyzer](https://aws.amazon.com/iam/access-analyzer/) provides quick links in the console to assist you to delete them. For unused permissions, IAM Access Analyzer reviews your existing policies and recommends a refined policy that is tailored to your access activity. 