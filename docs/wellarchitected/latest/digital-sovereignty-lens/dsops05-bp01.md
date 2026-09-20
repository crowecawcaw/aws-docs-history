

# DSOPS05-BP01 Enable independent root cause analysis and remediation
<a name="dsops05-bp01"></a>

 When compliance findings are routed to a central team for investigation, remediation slows down and the central team becomes a bottleneck. When regional and account teams can independently investigate and resolve compliance findings within their scope, they reduce mean time to remediation and free specialized security expertise for complex issues. 

 **Desired outcome:** 
+  Engineering teams can independently conduct root cause analysis and remediate compliance findings within their delegated scope, using standardized tools and processes. 
+  Regional teams investigate jurisdiction-specific findings without waiting for central team involvement. 

 **Common anti-patterns:** 
+  A limited number of specialists have access to security and compliance findings. Other teams wait for the central team to investigate and triage. 
+  Developers receive compliance alerts but lack the permissions or tooling to investigate the root cause independently. 
+  No standardized process for root cause analysis. Each team approaches investigation differently, leading to inconsistent outcomes. 
+  Regional teams can't scope findings to their jurisdiction, making it difficult to identify which findings are relevant to them. 
+  Findings are remediated without documenting the root cause, so the same issues recur. 

 **Benefits of establishing this best practice:** 
+  Reduced mean time to remediation through immediate team action within delegated scope. 
+  Decreased operational load on centralized security and compliance teams. 
+  Better allocation of specialized security expertise towards complex, cross-jurisdictional issues. 
+  Improved team ownership and accountability for compliance outcomes within their jurisdiction. 

 **Level of risk exposed if this best practice is not established:** Medium 

## Implementation guidance
<a name="implementation-guidance"></a>

 Independent investigation capability requires three things: scoped access to findings, standardized analysis techniques, and a feedback mechanism that leads to [correction of errors](https://aws.amazon.com/blogs/mt/why-you-should-develop-a-correction-of-error-coe/). Without all three, teams either lack the visibility to act, apply inconsistent approaches to root cause analysis, or solve the same problems repeatedly. 

 Teams need visibility into findings that relate to their resources and jurisdiction without exposure to findings from other scopes. This scoping reduces noise (teams see only what they are responsible for) and enforces jurisdictional boundaries (teams in one jurisdiction don't access compliance data from another). The delegation boundaries established in earlier best practices define what teams can remediate, and scoped findings access defines what they can see and investigate. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Scope findings to the responsible team:** 
   +  Configure findings delivery so that developers see only compliance information about the resources they are responsible for. Use [Amazon EventBridge](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-what-is.html) rules to match Security Hub CSPM findings by accountId and region, then route them to the appropriate team through [Amazon SNS](https://docs.aws.amazon.com/sns/latest/dg/welcome.html) topics or team messaging integrations. 
   +  Where teams need to query historical findings, consider using [Amazon Security Lake](https://aws.amazon.com/security-lake/) with [AWS Lake Formation](https://docs.aws.amazon.com/lake-formation/latest/dg/what-is-lake-formation.html) fine-grained access control (FGAC) to restrict query results by account and Region. This allows regional teams to investigate findings within their jurisdictional scope without accessing data from other jurisdictions. 

1.  **Standardize root cause analysis:** 
   +  Establish a consistent root cause analysis (RCA) process across teams. Two common techniques are: 
     +  : iteratively asking "why" to trace a finding back to its root cause. 
     +  [Ishikawa Diagrams](https://en.wikipedia.org/wiki/Ishikawa_diagram): mapping contributing factors across categories (people, process, technology, and environment). 
   +  Both techniques require the ability to collect and analyze data from multiple sources, such as logs, events, and metrics. When you enable security standards with [AWS Security Hub CSPM](https://docs.aws.amazon.com/securityhub/latest/userguide/what-is-securityhub.html), Security Hub CSPM consolidates findings from multiple services and generates actionable insights that include the affected resource, severity, source of evaluation, and suggested remediation. 
   +  The following example shows a Security Hub CSPM finding for a noncompliant [Amazon DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Introduction.html) table where delete protection isn't enabled. The finding maps to specific NIST 800-53 controls, giving the investigating team both the technical detail and the regulatory context: 
**Note**  
 The code snippets shown here are for illustration only and may not be accurate. Validate against your own environment and requirements unique to your workload. 

     ```
     {
       "AwsAccountId": "XXXXXXX",
       "Compliance": {
         "Status": "FAILED",
         "SecurityControlId": "DynamoDB.6",
         "RelatedRequirements": [
           "NIST.800-53.r5 CA-9(1)",
           "NIST.800-53.r5 CM-2",
           "NIST.800-53.r5 CM-3",
           "NIST.800-53.r5 SC-5(2)"
         ],
         "AssociatedStandards": [
           { "StandardsId": "standards/nist-800-53/v/5.0.0" }
         ]
       },
       "Description": "This control checks whether an Amazon DynamoDB table has deletion protection enabled.",
       "Remediation": {
         "Recommendation": {
           "Text": "For information on how to correct this issue, consult the AWS Security Hub CSPM controls documentation.",
           "Url": "https://docs.aws.amazon.com/console/securityhub/DynamoDB.6/remediation"
         }
       },
       "Resources": [
         {
           "Details": {
             "AwsDynamoDbTable": {
               "TableName": "Table-Name-XXXXXXXXXX",
               "DeletionProtectionEnabled": false
             }
           },
           "Id": "arn:aws:dynamodb:region-id:XXXXXXXXXX:table/Table-Name-XXXXXXXXXX",
           "Region": "region-id",
           "Type": "AwsDynamoDbTable"
         }
       ]
     }
     ```
   +  For jurisdiction-specific findings (for example, a missing data residency tag or a cross-Region replication violation), review the jurisdiction-specific controls from the compliance baseline to determine whether the finding represents a baseline violation or a jurisdiction-specific extension violation. This distinction affects remediation priority and escalation path. 

1.  **Verify and document:** 
   +  After remediation, verify that the finding resolves in Security Hub CSPM. Track the time from detection to resolution as part of the mean time to remediation (MTTR) metric. 
   +  Document the root cause, the remediation applied, and whether the issue is likely to recur. Feed recurring issues into compliance training content and into the automated remediation library. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [DSOPS01-BP02 Enable distributed compliance execution](dsops01-bp02.html) 
+  [DSOPS01-BP03 Implement compliance training and awareness](dsops01-bp03.html) 
+  [DSOPS04-BP01 Maintain continuous visibility of your compliance status](dsops04-bp01.html) 
+  [DSOPS05-BP02 Automate compliance remediation](dsops05-bp02.html) 
+  [SEC04-BP03 Correlate and enrich security alerts](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_detect_investigate_events_security_alerts.html) 
+  [SEC04-BP04 Initiate remediation for non-compliant resources](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_detect_investigate_events_noncompliant_resources.html) 
+  [SEC10-BP08 Establish a framework for learning from incidents](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_incident_response_establish_incident_framework.html) 
+  [OPS11-BP04 Perform knowledge management](https://docs.aws.amazon.com/wellarchitected/latest/operational-excellence-pillar/ops_evolve_ops_knowledge_management.html) 

 **Related documents:** 
+  [Visualizing AWS Config data using Amazon Athena and Quick](https://aws.amazon.com/blogs/mt/visualizing-aws-config-data-using-amazon-athena-and-amazon-quicksight/) 
+  [Remediate non-compliant AWS Config rules with AWS Systems Manager Automation runbooks](https://aws.amazon.com/blogs/mt/remediate-noncompliant-aws-config-rules-with-aws-systems-manager-automation-runbooks/) 
+  [Automated Response and Remediation with AWS Security Hub CSPM](https://aws.amazon.com/blogs/security/automated-response-and-remediation-with-aws-security-hub/) 

 **Related videos:** 
+  [AWS re:Invent 2025 - Building and validating cloud controls with generative AI (COP350)](https://www.youtube.com/watch?v=bRTSI-UKl0s) 

 **Related examples:** 
+  [Cloud Intelligence Dashboards - AWS Config Resource Compliance Dashboard](https://github.com/aws-samples/config-resource-compliance-dashboard) 
+  [AWS Security Hub CSPM Automated Response and Remediation](https://github.com/aws-solutions/automated-security-response-on-aws) 

 **Related services:** 
+  [AWS Security Hub CSPM](https://aws.amazon.com/security-hub/) 
+  [Amazon EventBridge](https://aws.amazon.com/eventbridge/) 
+  [Amazon Security Lake](https://aws.amazon.com/security-lake/) 
+  [AWS Lake Formation](https://aws.amazon.com/lake-formation/) 
+  [Amazon SNS](https://aws.amazon.com/sns/) 
+  [AWS Systems Manager](https://aws.amazon.com/systems-manager/) 