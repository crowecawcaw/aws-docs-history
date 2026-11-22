

# OPS05-BP03 Create support plans for production workloads

 Production workloads depend on software and services that your team does not operate. When one of those dependencies fails, your ability to respond depends on the support agreement you arranged in advance. A support plan defines the response you can expect, how to reach the vendor, and how to escalate during an incident. 

 **Desired outcome:** 
+  Every software and service dependency your production workload relies on has an active support plan. 
+  Each of your support plans matches the response time your service-level needs require. 
+  Your team has documentation that records each support level and how to request and escalate support. 
+  Your support contacts stay current through a mechanism that keeps them up to date. 

 **Common anti-patterns:** 
+  A critical vendor has no support plan, so the team cannot expedite a fix or get timely updates when the vendor's software disrupts the workload. 
+  The one person who held a vendor relationship leaves, and the team cannot reach vendor support directly. 
+  A production incident involves a vendor, and no one has documented how to file a support case. 
+  Support contact details go stale because nothing keeps them current. 

 **Benefits of establishing this best practice:** 
+  The team gets vendor responses within the time frame their service-level needs require. 
+  A supported relationship lets the team escalate during production issues. 
+  Vendors help troubleshoot during an incident under the agreed support terms. 
+  Documented support processes remove delay and guesswork when an incident starts. 

 **Level of risk exposed if this best practice is not established:** Low 

## Implementation guidance
<a name="implementation-guidance"></a>

 Higher support tiers cost more and provide faster response times, deeper access, and stronger escalation. Reserve them for dependencies that can take your workload down, and revisit the choice as a workload's criticality changes. 

 A vendor relationship often lives in one engineer's inbox. Document how to request and escalate support, and store it where the whole team can reach it. Keep contacts current, and meet with vendors regularly. 

 For workloads on AWS, activate [AWS Business Support\+](https://aws.amazon.com/premiumsupport/plans/business-plus/) or greater on every account that runs production. Beyond faster response times, these tiers provide programmatic access to [AWS Trusted Advisor](https://docs.aws.amazon.com/awssupport/latest/user/trusted-advisor.html) and [AWS Health](https://docs.aws.amazon.com/health/latest/ug/what-is-aws-health.html). You can integrate their recommendations and event notifications into your own systems. Choose the tier that matches the response time your production service levels require. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Inventory your production dependencies:** Work with stakeholders across your organization to list every software and service vendor your workload relies on in production. Record each dependency so the list can be reviewed and kept current. 

1.  **Determine service-level needs and select a support level:** For each dependency, decide how quickly you need a vendor response based on how the dependency affects your workload. Select the support level that meets that need without over-buying for low-criticality dependencies. 

1.  **Establish support plans with vendors:** Arrange a support plan with each commercial vendor that matches the level you chose. For AWS accounts running production workloads, we recommend [AWS Business\+ Support](https://aws.amazon.com/premiumsupport/plans/business-plus/) or [AWS Enterprise Support](https://aws.amazon.com/premiumsupport/plans/enterprise/), which provide faster response times and API access to AWS Trusted Advisor and AWS Health. [AWS Unified Operations](https://aws.amazon.com/premiumsupport/plans/unified-operations/) combines proven expertise with AI-powered insights to help reduce operational and security risks, resolve issues faster, and help you architect more resilient cloud solutions from the start, accelerating your most critical cloud initiatives. If you do not have premium support, define an action plan for issues that need vendor help. 

1.  **Document support processes:** Record each support plan in your knowledge management system, including how to request support, who to notify when a case is filed, and how to escalate during an incident. A wiki lets any team member update the documentation when processes or contacts change. 

1.  **Keep support contacts current:** Put a mechanism in place to review and update support contacts on a regular cadence, and meet with vendors periodically to stay current on their support offerings and processes. This reduces reliance on any single person's relationship with a vendor. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [OPS05-BP04 Assess operational readiness](ops05-bp04.md) 
+  [OPS05-BP02 Develop and test playbooks to respond to incidents](ops05-bp02.md) 

 **Related documents:** 
+  [Support Plans](https://docs.aws.amazon.com/awssupport/latest/user/aws-support-plans.html) 

 **Related services:** 
+  [AWS Business\+ Support](https://aws.amazon.com/premiumsupport/plans/business-plus/) 
+  [AWS Enterprise Support](https://aws.amazon.com/premiumsupport/plans/enterprise/) 
+  [AWS Unified Operations](https://aws.amazon.com/premiumsupport/plans/unified-operations/) 