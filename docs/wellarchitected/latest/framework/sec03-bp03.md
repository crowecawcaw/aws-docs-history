

# SEC03-BP03 Analyze public and cross-account access

 Some resources need to be reachable from outside their own account, whether publicly or by another account, to support shared data or common tools. Such access tends to persist beyond the reason it was granted. Keep an inventory of which resources are shared and with whom, monitor it continuously, and reduce public and cross-account access to only the resources that require it. Apply the same scrutiny to internal access to sensitive resources, and verify which principals in your organization can reach them so access stays limited to those you intend. 

 **Desired outcome:** 
+  You know which of your resources are shared, whether publicly or cross-account, and with which principals. 
+  You know which internal principals in your organization can reach your sensitive resources, and confirm that access is intended. 
+  You monitor and audit shared resources continuously to confirm they are reachable only by authorized principals. 
+  Public access to any of your resources follows a documented approval process rather than appearing by default. 
+  You receive alerts on unexpected changes to public or cross-account access, routed to the team that owns the resource. 

 **Common anti-patterns:** 
+  Teams keep no inventory of which resources are shared externally. 
+  No approval process governs cross-account or public access to resources. 
+  Access grants outlive the need that justified them, because nothing prompts a review. 
+  Broad access is discovered only during an incident or audit, not through continuous monitoring. 
+  The same resource-based policy is reused across resources without checking who it actually grants access to. 

 **Benefits of establishing this best practice:** 
+  You detect unintended public or cross-account access before an external party does. 
+  Continuous analysis of access paths replaces point-in-time reviews that miss changes. 
+  An approval process for public access makes each exposure a deliberate decision with an owner. 
+  Alerting on access changes shortens the time between a misconfiguration and its correction. 
+  A current inventory of shared resources makes audits faster and findings easier to trace. 

 **Level of risk exposed if this best practice is not established:** Low 

## Implementation guidance
<a name="implementation-guidance"></a>

 Cross-account access comes from two mechanisms. A resource-based policy such as a bucket policy can name principals in other accounts, or a principal in another account can assume a role in yours. Trust policies decide the conditions under which a role can be assumed. Condition keys such as aws:PrincipalOrgID can deny any attempt to assume a role from outside your organization. Organization membership changes the options: you can grant access to the whole organization, an organizational unit, or individual accounts. A standalone account can share only with individual accounts. 

 Reading policies manually does not scale, because a policy's effect depends on how it combines with others. [IAM Access Analyzer](https://docs.aws.amazon.com/IAM/latest/UserGuide/what-is-access-analyzer.html) uses [provable security](https://aws.amazon.com/security/provable-security/) to identify every access path to a resource from outside its account, and reviews resource policies continuously. It can [preview findings](https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-access-preview.html) before you deploy a policy change, so you can confirm the change grants only the access you intend. Configuring it at the organization level gives you one view across every account. 

 Internal principals can reach resources beyond what was intended, and reading every identity policy, SCP, and RCP does not scale either. [IAM Access Analyzer internal access findings](https://docs.aws.amazon.com/IAM/latest/UserGuide/what-is-access-analyzer.html) extend the same automated reasoning to internal access. The analyzer evaluates identity-based policies, service control policies, and resource control policies together to report which IAM users and roles in your organization can access a resource. An organization-level analyzer evaluates every principal in the organization, and an account-level analyzer evaluates principals in that account. Internal access analysis supports sensitive resource types such as Amazon S3 buckets, Amazon DynamoDB tables, and Amazon RDS snapshots (for the full set of resources, see [current list of supported resource types](https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-resources.html)). Collect findings in a resource-centric dashboard, and route them through [Amazon EventBridge](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-what-is.html) to notify the owning team so they can remove unintended access. Because internal access analysis is priced per monitored resource, scope it to the resources whose exposure matters most. 

 Use both detective and preventive controls. Detective controls tell you when access has changed, while preventive controls stop the change from happening. [AWS Config](https://docs.aws.amazon.com/config/latest/developerguide/operational-best-practices-for-Publicly-Accessible-Resources.html) reports misconfigured and publicly accessible resources, and services such as [AWS Control Tower](https://docs.aws.amazon.com/controltower/latest/controlreference/controls-reference.html) and [AWS Security Hub CSPM](https://docs.aws.amazon.com/securityhub/latest/userguide/what-is-securityhub.html) deploy detective controls across an organization. For prevention, a service control policy can block changes to public-access settings so a broad grant cannot be made. Level of scrutiny also depends on what the resource holds (for example, a bucket of public marketing assets and a bucket of regulated records call for different treatment). Factor data sensitivity into how strictly you review each grant. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Aggregate findings across your organization:** Use [AWS Config for AWS Organizations](https://docs.aws.amazon.com/organizations/latest/userguide/services-that-can-integrate-config.html) to collect findings from member accounts into a delegated administrator account, and [deploy AWS Config rules across accounts](https://docs.aws.amazon.com/config/latest/developerguide/config-rule-multi-account-deployment.html) to detect publicly accessible resources. This gives you one place to see external access rather than checking each account. 

1.  **Configure IAM Access Analyzer for external access:** Enable [IAM Access Analyzer](https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-getting-started.html) at the organization level to identify resources, such as buckets and roles, that are shared with an external entity. Review its findings continuously and confirm each shared resource is reachable only by principals you intend. 

1.  **Verify internal access to sensitive resources:** Create an [internal access analyzer](https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-create-internal.html) with your organization as the zone of trust, and point it at the sensitive resources that most warrant scrutiny, such as Amazon S3 buckets, Amazon DynamoDB tables, and Amazon RDS snapshots that hold regulated or confidential data. Review the findings to confirm only intended IAM users and roles can reach each resource, and route new findings through [Amazon EventBridge](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-what-is.html) to the owning team so unintended access is removed. Because this analysis is priced per monitored resource, scope it to your highest-sensitivity resources rather than enabling it for everything. 

1.  **Auto-remediate public access on storage:** Configure [AWS Config with auto-remediation](https://aws.amazon.com/blogs/security/how-to-use-aws-config-to-monitor-for-and-respond-to-amazon-s3-buckets-allowing-public-access/) to turn on Amazon S3 Block Public Access when a bucket becomes public. Automated correction closes the window between a misconfiguration and its fix. 

1.  **Monitor and prevent changes to public-access settings:** Alert when Amazon S3 Block Public Access is turned off, and use a [service control policy](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps.html) to prevent changes to public-access policies. For a resource-side guardrail, attach a [resource control policy (RCP)](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_rcps.html) that enforces aws:PrincipalOrgID on supported resources so access is denied to any principal outside your organization even if a resource-based policy is misconfigured. Complement this with [AWS Trusted Advisor](https://docs.aws.amazon.com/awssupport/latest/user/trusted-advisor.html) checks for buckets that grant open access. 

1.  **Factor in data sensitivity:** Use [Amazon Macie](https://docs.aws.amazon.com/macie/latest/user/data-classification.html) to discover sensitive data such as personally identifiable information, protected health information, and credentials. Prioritize review of shared resources by the sensitivity of the data they hold, use it to choose which resources to monitor with an internal access analyzer, and apply stricter controls where the impact of exposure is highest. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [SEC03-BP04 Share resources securely within your organization](sec03-bp04.md) 
+  [SEC03-BP05 Share resources securely with a third party](sec03-bp05.md) 
+  [SEC03-BP01 Grant least privilege access in workload components](sec03-bp01.md) 

 **Related documents:** 
+  [Using AWS Identity and Access Management Access Analyzer](https://docs.aws.amazon.com/IAM/latest/UserGuide/what-is-access-analyzer.html) 
+  [IAM Access Analyzer internal access analysis](https://docs.aws.amazon.com/IAM/latest/UserGuide/what-is-access-analyzer.html) 
+  [Verify internal access to critical AWS resources with new IAM Access Analyzer capabilities](https://aws.amazon.com/blogs/aws/verify-internal-access-to-critical-aws-resources-with-new-iam-access-analyzer-capabilities/) 
+  [How to use trust policies with IAM roles](https://aws.amazon.com/blogs/security/how-to-use-trust-policies-with-iam-roles/) 
+  [AWS Control Tower controls library](https://docs.aws.amazon.com/controltower/latest/controlreference/controls-reference.html) 
+  [AWS Foundational Security Best Practices standard](https://docs.aws.amazon.com/securityhub/latest/userguide/fsbp-standard.html) 
+  [AWS Config managed rules](https://docs.aws.amazon.com/config/latest/developerguide/evaluate-config_use-managed-rules.html) 
+  [AWS Trusted Advisor check reference](https://docs.aws.amazon.com/awssupport/latest/user/trusted-advisor-check-reference.html) 
+  [Monitoring AWS Trusted Advisor check results with Amazon EventBridge](https://docs.aws.amazon.com/awssupport/latest/user/cloudwatch-events-ta.html) 
+  [Block public access to AMIs in Amazon EC2](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/block-public-access-to-amis.html) 
+  [Declarative policy to block new public access of AMIs across an AWS Organization](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_ec2_syntax.html) 

 **Related examples:** 
+  [Data perimeter policy examples](https://github.com/aws-samples/data-perimeter-policy-examples) 