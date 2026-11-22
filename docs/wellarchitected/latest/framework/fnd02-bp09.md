

# FND02-BP09 Establish a process to continually review and refine permissions

 Continuously review and refine permissions to keep pace with your organization's changing needs. This process verifies that identities have requisite access only when they need it, reducing the risk of unauthorized access. A systematic approach to permission reviews strengthens security and improves operational efficiency across your cloud footprint. 

 **Desired outcome:** 
+  You reduce the risk of unauthorized access by continuously updating permissions so that all entities have only the necessary access needed to perform their current duties. 
+  Your continuous permissions reviews improve visibility and provide a clear, updated understanding of who has access to what resources across AWS environments. 
+  You can adapt to change and shifts in roles and responsibilities across the organization more efficiently. 

 **Common anti-patterns:** 
+  Configuring permissions once and never revisiting them, leading to outdated and potentially overly permissive permissions. 
+  Relying solely on manual processes for permission reviews, which can be error-prone and time-consuming in large environments. 
+  Failing to revoke or expire temporary access granted for specific tasks, and overlooking permissions granted to applications or services that can lead to the [confused deputy problem](https://docs.aws.amazon.com/IAM/latest/UserGuide/confused-deputy.html). 
+  Failing to document the rationale behind permission decisions, making future reviews and audits challenging. 
+  Only reviewing permissions after incidents occur, or failing to identify and remove permissions that are no longer being used. 
+  Inconsistent enforcement across teams, with different standards or processes applied for permission management across different parts of the organization. 

 **Benefits of establishing this best practice:** 
+  Stronger security posture through systematic identification and removal of excessive permissions, reducing the risk of unauthorized access. 
+  Improved compliance with security standards and regulatory requirements that mandate regular access control audits. 
+  Operational efficiency gains by identifying unused permissions and simplifying access patterns, giving teams a clearer view of their access rights. 
+  Better visibility into the permission landscape across multiple accounts, so teams can detect permission anomalies and security risks faster. 
+  Reduced manual burden through automated permission analysis tools, with improved accuracy and consistency in applying least privilege principles. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 The principle of least privilege (granting only the permissions necessary to perform a task) is foundational to cloud security. Access needs change as teams reorganize, projects shift priorities, and new services replace old ones. Permissions that were appropriate six months ago might now be unnecessary risk. Without a structured review process, your environment accumulates permission debt: roles with broader access than needed, unused credentials, and policies that no longer align with current responsibilities. 

 Analyze, refine, and document permissions on a predictable cycle that keeps them aligned with actual usage patterns. Standardize least privilege permissions for common roles and tasks to improve consistency and security. Apply these standards uniformly across AWS accounts through centralized management like AWS Organizations or custom scripts. 

 Distinguish permissions that are unused from those used infrequently but still necessary, such as break-glass roles for incident response or quarterly compliance reporting. Handle these edge cases with usage analysis over appropriate time windows, documented exceptions for legitimate infrequent access, and temporary elevation for privileged operations. Permission restrictions that impede legitimate work push teams toward workarounds, and lax restrictions leave unnecessary access in place. 

 [AWS IAM Access Analyzer](https://docs.aws.amazon.com/IAM/latest/UserGuide/what-is-access-analyzer.html) identifies permissions that have not been used within a defined period, providing evidence for removal decisions. [IAM Access Advisor](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_last-accessed.html) captures what services and actions identities use, revealing gaps between granted and needed permissions. [IAM Access Analyzer policy generation](https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-policy-generation.html) creates restrictive permission policies based on the actual services and actions a principal interacts with. [IAM Policy Autopilot](https://aws.amazon.com/blogs/security/iam-policy-autopilot-an-open-source-tool-that-brings-iam-policy-expertise-to-builders-and-ai-coding-assistants/) is an open-source tool that brings IAM policy expertise into builder workflows and AI coding assistants, helping teams refine policies in the same place they author them. With centralized identity management, you can apply review processes consistently across accounts and teams as a feedback loop. 

 Permission reviews must follow a defined schedule: quarterly for full reviews, more frequently for high-risk or privileged access. Reviews must involve both security teams and business stakeholders who understand the operational context behind access requirements. Decisions must be documented with clear rationale to create an audit trail for future reviews and compliance validation. Temporary access must follow formal approval and expiration workflows that automatically revoke elevated permissions when the task is complete. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Establish a permissions baseline:** Document roles and policies across all AWS accounts using infrastructure as code (IaC) technologies such as [AWS CloudFormation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html) or the [AWS CDK](https://docs.aws.amazon.com/cdk/v2/guide/home.html) to create permissions and track changes. Store these definitions in version control to create a traceable history. Use consistent naming conventions and [tagging](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html) to identify the purpose and owner of each role and policy. 

1.  **Schedule regular permission reviews:** Establish a regular schedule for full reviews (for example, quarterly) and more frequent checks for high-risk or sensitive permissions. Use [AWS IAM Access Analyzer](https://docs.aws.amazon.com/IAM/latest/UserGuide/what-is-access-analyzer.html) to identify unused permissions and fine-tune your policies. Configure Access Analyzer to run continuously and alert on new findings. 

1.  **Remove unused users and roles:** Determine an acceptable timeframe and usage policy for IAM users and roles. Use the [last accessed timestamp](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_last-accessed-view-data.html) to [identify unused users and roles](https://aws.amazon.com/blogs/security/identify-unused-iam-roles-remove-confidently-last-used-timestamp/) and remove them. Pay special attention to long-term credentials such as access keys that might have been created for temporary purposes but never rotated or deleted. 

1.  **Refine permissions based on access activity:** Review service and action last accessed information to [scope permissions for specific users and roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_last-accessed.html). [AWS IAM Access Analyzer policy generation](https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-policy-generation.html) can help you rightsize policies based on an IAM user or role's access activity, producing policies that reflect actual needs rather than anticipated needs. Use [IAM Policy Autopilot](https://aws.amazon.com/blogs/security/iam-policy-autopilot-an-open-source-tool-that-brings-iam-policy-expertise-to-builders-and-ai-coding-assistants/) to bring policy refinement into the builder workflow and into AI coding assistants, so teams can iterate on policies in the same environment where they author the rest of their infrastructure. 

1.  **Implement temporary elevated access management:** Create a workflow for [managing temporary elevated access](https://aws.amazon.com/blogs/security/temporary-elevated-access-management-with-iam-identity-center/) that includes request, approval, time-bound grant, and automatic revocation. Use session duration limits and scheduled access grants so that elevated permissions expire automatically when the task is complete. Document the business justification for each temporary elevation to create an audit trail and inform future permanent permission decisions. 

1.  **Enable data event logging in CloudTrail:** Consider [logging data events in AWS CloudTrail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.html). By default, CloudTrail does not log data events such as [Amazon S3](https://aws.amazon.com/s3/) object-level activity (for example, GetObject and DeleteObject) or [Amazon DynamoDB](https://aws.amazon.com/dynamodb/) table activities (for example, PutItem and DeleteItem). Data event logging provides the detail needed to scope permissions to specific resources rather than entire services, but comes with increased logging costs. Enable it selectively for sensitive data stores. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [FND02-BP04 Establish controls to manage access based on lifecycle](fnd02-bp04.md) 
+  [FND02-BP05 Grant least privilege access](fnd02-bp05.md) 
+  [FND02-BP08 Audit and rotate credentials periodically](fnd02-bp08.md) 

 **Related documents:** 
+  [Apply least-privilege permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#grant-least-privilege) 
+  [IAM Access Analyzer simplifies inspection of unused access in your organization](https://aws.amazon.com/blogs/security/iam-access-analyzer-simplifies-inspection-of-unused-access-in-your-organization/) 
+  [IAM Policy Autopilot — an open source tool that brings IAM policy expertise to builders and AI coding assistants](https://aws.amazon.com/blogs/security/iam-policy-autopilot-an-open-source-tool-that-brings-iam-policy-expertise-to-builders-and-ai-coding-assistants/) 
+  [Strategies for achieving least privilege at scale – Part 1](https://aws.amazon.com/blogs/security/strategies-for-achieving-least-privilege-at-scale-part-1/) 
+  [Strategies for achieving least privilege at scale – Part 2](https://aws.amazon.com/blogs/security/strategies-for-achieving-least-privilege-at-scale-part-2/) 
+  [Refine permissions in AWS using last accessed information](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_last-accessed.html) 
+  [IAM Access Analyzer findings - unused access, external access, and internal access](https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-findings.html) 
+  [Identify unused IAM roles and remove them confidently using last used timestamp](https://aws.amazon.com/blogs/security/identify-unused-iam-roles-remove-confidently-last-used-timestamp/) 

 **Related videos:** 
+  [AWS re:Invent 2023 - IAM Access Analyzer deep dive: From configuration to remediation (SEC340)](https://www.youtube.com/watch?v=0PM1NB8T4DE) 