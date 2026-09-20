

# DSOPS05-BP02 Automate compliance remediation
<a name="dsops05-bp02"></a>

 When compliance findings are remediated manually, response times vary, fixes are inconsistent, and audit trails are incomplete. Automated remediation provides consistent, rapid response to known compliance issues while maintaining oversight and audit trails that support regulatory reporting across jurisdictions. 

 **Desired outcome:** 
+  Resources can be automatically restored to compliance through reliable, tested, and auditable remediation processes. 
+  Remediation actions are traceable to specific regulatory requirements and scoped by jurisdiction so that regional teams can verify that fixes meet local regulatory expectations. 

 **Common anti-patterns:** 
+  Running untested remediation scripts in production. 
+  Implementing remediations without rollback capabilities. 
+  Missing approvals for high-risk changes. In multi-jurisdictional environments, high-impact remediations may require approval from the regional compliance specialist. 
+  Lack of audit trails for automated actions, making it difficult to demonstrate remediation to auditors. 
+  Applying the same remediation globally without considering jurisdiction-specific requirements. 

 **Benefits of establishing this best practice:** 
+  Reduced mean time to compliance restoration. 
+  Consistent application of fixes across jurisdictions. 
+  Decreased operational overhead for regional and central teams. 
+  Improved audit readiness through automated logging of remediation actions traceable to regulatory requirements. 

 **Level of risk exposed if this best practice is not established:** Medium 

## Implementation guidance
<a name="implementation-guidance"></a>

 Not all compliance findings are suitable for immediate automated remediation. The decision to automate depends on the risk profile of the remediation action, its reversibility, and whether jurisdiction-specific requirements affect how the fix is applied. A progressive approach starts with low-risk, reversible actions (for example, removing public access from a storage resource or enabling encryption) where the consequences of the action are well understood and readily reversed. As confidence grows, automation expands to cover more complex scenarios. 

 High-impact remediations require oversight before execution. In multi-jurisdictional environments, a remediation that modifies resource configurations in a jurisdiction may need approval from the regional compliance specialist responsible for that scope. Approval gates scoped by jurisdiction provide this oversight without creating a global bottleneck. Low-risk remediations execute immediately within guardrails, while high-impact actions queue for jurisdiction-appropriate approval before proceeding. This tiered approach balances speed for routine fixes with governance for consequential changes. 

 Remediation is most effective when bundled with the detection rule that triggers it. When a detection rule and its corresponding remediation are packaged together as a deployable unit, they can be versioned, tested, and deployed as one artifact. This pairing reduces the gap between finding detection and fix availability, and it enables remediation actions to be deployed alongside detection rules without requiring separate coordination between teams. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Set up AWS Config remediations with conformance packs:** Remediations are applied using [AWS Systems Manager (SSM) Automation documents](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-automation.html) and can run automatically when compliance violations are detected. [AWS Config](https://docs.aws.amazon.com/config/latest/developerguide/remediation.html) integrates with these automation documents to remediate noncompliant resources. 

    With AWS Config, you can group both [managed](https://docs.aws.amazon.com/config/latest/developerguide/evaluate-config_use-managed-rules.html) and [custom rules](https://docs.aws.amazon.com/config/latest/developerguide/evaluate-config_develop-rules.html) into [conformance packs](https://docs.aws.amazon.com/config/latest/developerguide/conformance-packs.html). A conformance pack can include remediations alongside the rules. This means you can bundle a detection rule and its remediation action into a single deployable unit. Conformance packs are deployed per-Region and can be deployed across an organization using [organizational conformance packs](https://docs.aws.amazon.com/config/latest/developerguide/conformance-pack-organization-apis.html), which matches the jurisdiction-specific conformance pack model. 

    The following abbreviated example shows the pattern: a detection rule paired with a RemediationConfiguration that invokes an SSM document (AWS-DisableS3BucketPublicReadWrite) in one template. Parameters are omitted for brevity. For the complete version, see [Operational Best Practices for Amazon S3 with Remediation](https://github.com/awslabs/aws-config-rules/blob/master/aws-config-conformance-packs/Operational-Best-Practices-for-Amazon-S3-with-Remediation.yaml). 

   ```
   Resources:
     # Detection rule
     S3BucketPublicReadProhibited:
       Type: AWS::Config::ConfigRule
       Properties:
         ConfigRuleName: S3BucketPublicReadProhibited
         Source:
           Owner: AWS
           SourceIdentifier: S3_BUCKET_PUBLIC_READ_PROHIBITED
     # Remediation bundled with the rule
     S3BucketPublicReadProhibitedRemediation:
       DependsOn: S3BucketPublicReadProhibited
       Type: AWS::Config::RemediationConfiguration
       Properties:
         ConfigRuleName: S3BucketPublicReadProhibited
         TargetType: SSM_DOCUMENT
         TargetId: AWS-DisableS3BucketPublicReadWrite
         Automatic: true
         # Parameters (AutomationAssumeRole, S3BucketName) omitted for brevity
   ```

    You can also define custom rules using [CloudFormation Guard](https://docs.aws.amazon.com/cfn-guard/latest/ug/what-is-guard.html) domain-specific language (DSL) or [Lambda functions](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html), bundle them into custom conformance packs, and trigger automated remediations. Sample conformance pack templates, including versions that bundle rules with their remediations, are available from the [AWS Config Rules GitHub repository](https://github.com/awslabs/aws-config-rules/tree/master/aws-config-conformance-packs). 

1.  **Build customized remediation workflows:** Instead of triggering automated remediations immediately, staging is another approach where compliance findings are collected, analyzed, and then the most appropriate response is determined. For example, AWS customer Lockheed Martin developed a [custom remediation workflow](https://www.youtube.com/watch?v=DnIn-LZFQow&t=1234s) that checks for exemptions before triggering Systems Manager Automations. 

    Consider developing your own remediation workflows when you: 
   +  Need to stage findings and choose between multiple remediation options. 
   +  Need manual approvals before running automated runbooks. 
   +  Need to apply different remediations based on the jurisdiction where the resource is deployed. 

1.  **Create your own Systems Manager runbooks:** You can [create your own runbooks](https://docs.aws.amazon.com/systems-manager/latest/userguide/automation-documents.html) to automate remediation tasks. Runbooks are written using YAML or JSON. You can use the [visual design experience](https://docs.aws.amazon.com/systems-manager/latest/userguide/automation-visual-designer.html) to create custom workflows by dragging and dropping actions such as "Invoke Lambda Functions", "Start Step Function Execution", or "EventBridge Put Events" into the execution graph. 

    When regional teams use pre-approved runbooks to remediate findings within their delegated scope, feed recurring remediation patterns back into the runbook library. This creates a feedback loop where root cause analysis outcomes drive improvements to automated remediations. 

1.  **Trigger remediation from AWS Security Hub CSPM findings:** Use [AWS Security Hub CSPM](https://docs.aws.amazon.com/securityhub/latest/userguide/what-is-securityhub.html) and [Amazon EventBridge](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-what-is.html) to trigger remediations based on compliance findings. For a reference architecture pattern, see [Automate remediation for AWS Security Hub CSPM standard findings](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/automate-remediation-for-aws-security-hub-standard-findings.html). The pattern provides a framework implementation you can use as a starting point. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [DSOPS01-BP01 Organize compliance for multi-jurisdictional operations](dsops01-bp01.html) 
+  [DSOPS01-BP02 Enable distributed compliance execution](dsops01-bp02.html) 
+  [DSOPS05-BP01 Enable independent root cause analysis and remediation](dsops05-bp01.html) 
+  [DSOPS04-BP01 Maintain continuous visibility of your compliance status](dsops04-bp01.html) 
+  [SEC04-BP04 Initiate remediation for non-compliant resources](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_detect_investigate_events_noncompliant_resources.html) 

 **Related documents:** 
+  [Remediating noncompliant resources with AWS Config](https://docs.aws.amazon.com/config/latest/developerguide/remediation.html) 
+  [Create your own Systems Manager runbooks](https://docs.aws.amazon.com/systems-manager/latest/userguide/automation-documents.html) 
+  [Automate remediation for AWS Security Hub CSPM standard findings](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/automate-remediation-for-aws-security-hub-standard-findings.html) 
+  [Deploy conformance packs across an organization with automatic remediation](https://aws.amazon.com/blogs/mt/deploying-conformance-packs-across-an-organization-with-automatic-remediation/) 

 **Related videos:** 
+  [AWS re:Invent 2025 - From Reactive to Proactive: Infrastructure governance by design (COP352)](https://www.youtube.com/watch?v=iXor74El2D8) 
+  [Lockheed Martin: Custom remediation workflow](https://www.youtube.com/watch?v=DnIn-LZFQow&t=1234s) 

 **Related examples:** 
+  [AWS Config Conformance Pack Samples with Remediations](https://github.com/awslabs/aws-config-rules/tree/master/aws-config-conformance-packs) 
+  [AWS Security Hub CSPM Automated Response and Remediation](https://github.com/aws-solutions/automated-security-response-on-aws) 

 **Related services:** 
+  [AWS Systems Manager Automation](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-automation.html) 
+  [AWS Config](https://aws.amazon.com/config/) 
+  [AWS Security Hub CSPM](https://aws.amazon.com/security-hub/) 
+  [Amazon EventBridge](https://aws.amazon.com/eventbridge/) 
+  [AWS Lambda](https://aws.amazon.com/lambda/) 
+  [AWS CloudFormation Guard](https://docs.aws.amazon.com/cfn-guard/latest/ug/what-is-guard.html) 