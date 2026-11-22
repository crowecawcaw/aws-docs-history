

# SEC08-BP03 Automate data at rest protection

 Manual data protection controls drift out of compliance as storage grows and changes. Automation enforces those controls continuously, catches misconfigurations before deployment, and remediates drift at runtime. It also creates the backups and detective coverage that protect data through operational failures and security events. 

 **Desired outcome:** 
+  Your data storage locations are scanned continuously for misconfigured controls, unauthorized access, and unexpected use. 
+  You remediate detected misconfigurations automatically, without waiting for a human operator. 
+  Your pipelines block noncompliant storage configurations before they reach production. 
+  Your automated processes create encrypted backups and store immutable copies outside the original environment. 

 **Common anti-patterns:** 
+  Teams skip encrypt-by-default settings on storage services where those settings are available. 
+  Teams plan backup and recovery for operational failures only, and overlook security events such as ransomware. 
+  Teams leave public access settings unenforced on storage resources. 
+  Teams configure controls once and never monitor or audit them for drift. 

 **Benefits of establishing this best practice:** 
+  Automated checks keep misconfigured storage out of production, which shortens exposure windows. 
+  Continuous monitoring detects and corrects drift that manual review would miss. 
+  Immutable, off-environment backups support recovery from both operational and security events. 
+  Consistent enforcement scales protection across accounts without proportional operator effort. 

 **Level of risk exposed if this best practice is not established:** Medium 

## Implementation guidance
<a name="implementation-guidance"></a>

 Data at rest protection usually fails because someone forgets to apply a control or a later change removes it. Automation solves these problems by enforcing controls without human action. *Preventive controls* stop a noncompliant resource from being created. *Detective controls* find resources that became noncompliant after creation. Use both controls to cover the full lifecycle of a storage resource. 

 Infrastructure as code (IaC) is the foundation for preventive control. When storage configuration lives in version-controlled templates, you can inspect and reject noncompliant changes before deployment, which is cheaper than responding to an incident. Coverage is limited, as not every setting is expressible in a template, and resources created outside the pipeline escape this gate. Pipeline checks and runtime controls are useful checks for these issues. 

 Runtime monitoring tools such as [AWS Config](https://aws.amazon.com/config/) watch deployed resources for changes to encryption, public access, and other controls, and they can trigger remediation when a resource drifts. Permissions are also part of data at rest protection. Review access to data and decryption keys continuously, because permissions granted for a one-time need often outlive it. Automated permission analysis surfaces access you can reduce, so least privilege stays in effect. 

 [Amazon GuardDuty](https://aws.amazon.com/guardduty/) watches for anomalous access patterns against storage, such as unusual read volumes or access from unexpected principals, which static configuration checks cannot detect. [Amazon Macie](https://docs.aws.amazon.com/macie/latest/user/what-is-macie.html) finds regulated data in storage that was never meant to hold it. Design backups to cover security events such as ransomware and unauthorized deletion, alongside hardware failures. Store immutable copies outside the source environment so they survive attacks on the original. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Define storage configuration as code and check it in the pipeline:** Capture encryption, access, and public-access settings for your storage in [AWS CloudFormation](https://aws.amazon.com/cloudformation/) or another IaC tool. Validate those templates against policy with [AWS CloudFormation Guard](https://docs.aws.amazon.com/cfn-guard/latest/ug/what-is-guard.html), and run AWS Config rules in [proactive mode](https://docs.aws.amazon.com/config/latest/developerguide/evaluate-config_turn-on-proactive-rules.html) to check a resource for compliance before it is created. 

1.  **Monitor deployed storage for configuration drift:** Use AWS Config to track control changes on storage resources, and configure [automatic remediation](https://docs.aws.amazon.com/config/latest/developerguide/remediation.html) so a detected misconfiguration is corrected without manual action. 

1.  **Continuously reduce data access permissions:** Run [IAM Access Analyzer](https://aws.amazon.com/iam/access-analyzer/) to generate findings when permissions to data or keys can be reduced, and route those findings to the team that owns the resource. 

1.  **Detect anomalous access to storage:** Enable Amazon GuardDuty to alert on threat signatures and deviations from baseline access for resources such as [Amazon EBS volumes](https://docs.aws.amazon.com/guardduty/latest/ug/malware-protection.html), [Amazon S3 buckets](https://docs.aws.amazon.com/guardduty/latest/ug/s3-protection.html), and [Amazon RDS databases](https://docs.aws.amazon.com/guardduty/latest/ug/rds-protection.html). 

1.  **Find sensitive data in unexpected locations:** Use Amazon Macie to scan your object storage for sensitive data, and initiate an automated response when it appears where it does not belong. 

1.  **Automate encrypted, recoverable backups:** Use [AWS Backup](https://docs.aws.amazon.com/aws-backup/latest/devguide/whatisbackup.html) to create encrypted backups of your data sources on a schedule, and use [Elastic Disaster Recovery](https://aws.amazon.com/disaster-recovery/) for continuous replication with a recovery point objective measured in seconds. Store copies outside the source environment so they survive unauthorized access to the original. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [SEC08-BP04 Enforce access control](sec08-bp04.md) 
+  [SEC08-BP02 Enforce encryption at rest](sec08-bp02.md) 
+  [SEC01-BP05 Automate deployment of standard security controls](sec01-bp05.md) 
+  [SEC07-BP03 Automate identification and classification](sec07-bp03.md) 
+  [REL09-BP03 Perform data backup automatically](rel09-bp03.md) 

 **Related documents:** 
+  [Automatically encrypt existing and new Amazon EBS volumes](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/automatically-encrypt-existing-and-new-amazon-ebs-volumes.html) 

 **Related videos:** 
+  [AWS re:Invent 2023 - Implement proactive data protection using Amazon EBS snapshots (STG226)](https://www.youtube.com/watch?v=d7C6XsUnmHc) 

 **Related examples:** 
+  [How to use AWS Config proactive rules and AWS CloudFormation Hooks to prevent creation of noncompliant cloud resources](https://aws.amazon.com/blogs/mt/how-to-use-aws-config-proactive-rules-and-aws-cloudformation-hooks-to-prevent-creation-of-non-complaint-cloud-resources/) 
+  [Automate and centrally manage data protection for Amazon S3 with AWS Backup](https://aws.amazon.com/blogs/storage/automate-and-centrally-manage-data-protection-for-amazon-s3-with-aws-backup/) 
+  [AWS Compliance Programs](https://aws.amazon.com/compliance/programs/) 

 **Related tools:** 
+  [AWS CloudFormation Guard Rules Registry](https://github.com/aws-cloudformation/aws-guard-rules-registry) 