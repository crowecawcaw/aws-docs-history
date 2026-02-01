# DSOPS05-BP02 Automate compliance remediation

Implement automated remediation to detect and correct compliance
violations with minimal human intervention. Automation provides
consistent, rapid response to known compliance issues while
maintaining proper oversight and audit trails for remediation
actions.

**Desired outcome:** Resources are
automatically restored to compliance through reliable, tested, and
auditable remediation processes that minimize manual intervention
while maintaining oversight and rollback capabilities.

**Common anti-patterns**:

- Running untested remediation scripts in production
- Implementing remediations without rollback capabilities
- Missing approvals for high-risk changes
- Lack of audit trails for automated actions
- No handling of partial failures in multi-step remediations

**Benefits of establishing this best
practice**:

- Reduced mean time to compliance restoration
- Consistent application of fixes
- Decreased operational overhead
- Improved audit readiness through automated logging
- Reduced risk of human error

**Level of risk exposed if this best practice
is not established:** Low

## Implementation guidance

After identifying and analyzing compliance issues, developers need
the ability to select and apply automated remediations. The
approach depends on the urgency, risk level, and organizational
requirements for automation vs. manual control.

Consider the following aspects while setting up remediations.

1. **Start with low-risk
   remediations**: Begin with safe, reversible actions
   like removing public access
2. **Build a test environment**:
   Set up a controlled environment for testing remediations.
   Apply the same testing methods (unit test, integration test)
   as you use to test critical business functionality, to test
   your remediation scripts. Integrate your tests with your
   Continuous Integration (CI) pipeline.
3. **Implement approval gates**:
   Require approval before deploying high-impact changes
4. **Provide rollback
   capabilities**: Make sure remediations can be undone
   if needed
5. **Monitor remediation
   success**: Track remediation effectiveness and
   failure rates

### Implementation steps

1. **Setup AWS Systems Manager
   Automation**: Remediations are applied using
   [AWS Systems Manager Automation documents](../../../systems-manager/latest/userguide/systems-manager-automation.md "../../../systems-manager/latest/userguide/systems-manager-automation.md") and can be run
   automatically upon triggering of compliance violations.
   [AWS Config](../../../config/latest/developerguide/WhatIsConfig.md "../../../config/latest/developerguide/WhatIsConfig.md") allows you to remediate non-compliant
   resources by integrating with these automation documents.

AWS Config allows you to group both
[managed](../../../config/latest/developerguide/evaluate-config_use-managed-rules.md "../../../config/latest/developerguide/evaluate-config_use-managed-rules.md")
and
[custom
rules](../../../config/latest/developerguide/evaluate-config_develop-rules.md "../../../config/latest/developerguide/evaluate-config_develop-rules.md") into
[Conformance
Packs](../../../config/latest/developerguide/custom-conformance-pack.md "../../../config/latest/developerguide/custom-conformance-pack.md"). It also provides several sample
[Conformance
Packs](../../../config/latest/developerguide/conformancepack-sample-templates.md "../../../config/latest/developerguide/conformancepack-sample-templates.md"). These are categorized under best practices by
service (for example S3, Lambda), or by standards (PCI DSS,
NIST). You can customize these conformance packs per your
needs and choose to enable rules applicable to you.
Conformance packs templates are available from the
[AWS Config Rules GitHub repository](https://github.com/awslabs/aws-config-rules/tree/master/aws-config-conformance-packs "https://github.com/awslabs/aws-config-rules/tree/master/aws-config-conformance-packs").

A powerful feature of conformance packs is you can include
remediations while adding the rules that make up the pack.
Consider the following code. Against the Config rule named
[S3BucketPublicReadProhibited](../../../config/latest/developerguide/s3-bucket-public-read-prohibited.md "../../../config/latest/developerguide/s3-bucket-public-read-prohibited.md"),
it also includes an automatic SSM remediation named
[AWS-DisableS3BucketPublicReadWrite](../../../systems-manager-automation-runbooks/latest/userguide/automation-aws-disables3bucketpublicreadwrite.md "../../../systems-manager-automation-runbooks/latest/userguide/automation-aws-disables3bucketpublicreadwrite.md").
The Depends On parameter establishes the
relation between the rule and the remediation. The following code is part of an
[example
operational best practices for Amazon DynamoDB that includes sample
remediations](https://github.com/awslabs/aws-config-rules/blob/master/aws-config-conformance-packs/Operational-Best-Practices-for-Amazon-DynamoDB-with-Remediation.yaml "https://github.com/awslabs/aws-config-rules/blob/master/aws-config-conformance-packs/Operational-Best-Practices-for-Amazon-DynamoDB-with-Remediation.yaml").

```

Resources:
  S3BucketPublicReadProhibited:
    Type: AWS::Config::ConfigRule
    Properties:
      ConfigRuleName: S3BucketPublicReadProhibited
      Description: >-
        Checks that your [Amazon S3](https://docs.aws.amazon.com/s3/index.html) buckets do not allow public read access.
        The rule checks the Block Public Access settings, the bucket policy, and the
        bucket access control list (ACL).
      Scope:
        ComplianceResourceTypes:
        - "AWS::S3::Bucket"
      Source:
        Owner: AWS
        SourceIdentifier: S3_BUCKET_PUBLIC_READ_PROHIBITED
      MaximumExecutionFrequency: Six_Hours
  S3BucketPublicReadProhibitedRemediation:
    DependsOn: S3BucketPublicReadProhibited
    Type: 'AWS::Config::RemediationConfiguration'
    Properties:
      ConfigRuleName: S3BucketPublicReadProhibited
      ResourceType: "AWS::S3::Bucket"
      TargetId: "AWS-DisableS3BucketPublicReadWrite"
      TargetType: "SSM_DOCUMENT"
      TargetVersion: "1"
      Parameters:
        AutomationAssumeRole:
          StaticValue:
            Values:
              - arn:aws:iam::<Account-Id>:role/S3OperationsAutomationsExecutionRole
       ...

```

With AWS Config you have the flexibility of defining your
own custom rules (using
[CloudFormation
Guard](../../../cfn-guard/latest/ug/what-is-guard.md "../../../cfn-guard/latest/ug/what-is-guard.md") DSL,
[Lambda
Functions](../../../lambda/latest/dg/welcome.md "../../../lambda/latest/dg/welcome.md")), bundle them into custom conformance packs
and trigger automated remediations. 2. **Build customized remediation
workflows**: Instead of triggering automated
remediations immediately, staging is another approach where
compliance findings are collected (for example in a queue or
a database), analyzed, and then the most appropriate
response is determined. For example, AWS customer Lockheed
Martin developed a
[custom
remediation workflow](https://www.youtube.com/watch?v=DnIn-LZFQow&t=1234s "https://www.youtube.com/watch?v=DnIn-LZFQow&t=1234s"), where they first check for
exemptions before triggering Systems Manager Automations.

Consider developing your own remediation workflows, when
you:

    * Need to stage findings and choose between multiple
     remediations options,
    * Or need manual approvals prior to execution of automated
     runbooks.

3. **Create your own Systems Manager
   runbooks**: You can
   [create
   your own runbooks](../../../systems-manager/latest/userguide/automation-documents.md "../../../systems-manager/latest/userguide/automation-documents.md") to automate remediation tasks.
   Runbooks are written using YAML or JSON. You can use the
   visual design experience to expedite the process of creating
   custom runbooks. With the visual designer you can also
   create your own custom workflows. For example, you can drag
   and drop "Invoke Lambda Functions",
   "Start Step Function Execution", or
   "EventBridge Put Events" into the execution
   graph.
4. **Trigger remediation from AWS Security Hub findings**: Here's a
   [typical
   architecture pattern](../../../prescriptive-guidance/latest/patterns/automate-remediation-for-aws-security-hub-standard-findings.md "../../../prescriptive-guidance/latest/patterns/automate-remediation-for-aws-security-hub-standard-findings.md") customers can use to remediate
   non-compliant resources using
   [AWS Security Hub](../../../securityhub/latest/userguide/what-is-securityhub.md "../../../securityhub/latest/userguide/what-is-securityhub.md") and
   [Amazon EventBridge](../../../eventbridge/latest/userguide/eb-what-is.md "../../../eventbridge/latest/userguide/eb-what-is.md"). Refer to
   [attachments](../../../prescriptive-guidance/latest/patterns/automate-remediation-for-aws-security-hub-standard-findings.md#attachments-a99f7107-9174-462a-ac2e-7205b355fd7b "../../../prescriptive-guidance/latest/patterns/automate-remediation-for-aws-security-hub-standard-findings.md#attachments-a99f7107-9174-462a-ac2e-7205b355fd7b")
   section. It provides a framework implementation that you can
   use as a starting point.

## Resources

**Related best practices:**

- [SEC04-BP04
  Initiate remediation for non-compliant resources](../security-pillar/sec_detect_investigate_events_noncompliant_resources.md "../security-pillar/sec_detect_investigate_events_noncompliant_resources.md")
- [SEC10-BP04
  Develop and test security incident response playbooks](../security-pillar/sec_incident_response_playbooks.md "../security-pillar/sec_incident_response_playbooks.md")

**Related documents:**

- [Create
  your own Systems Manager runbooks](../../../systems-manager/latest/userguide/automation-documents.md "../../../systems-manager/latest/userguide/automation-documents.md")
- [Create
  a Systems Manager workflow](../../../systems-manager/latest/userguide/visual-designer-tutorial.md#create-workflow "../../../systems-manager/latest/userguide/visual-designer-tutorial.md#create-workflow")
- [AWS Prescriptive Guidance: Automate remediation for AWS Security Hub standard findings](../../../prescriptive-guidance/latest/patterns/automate-remediation-for-aws-security-hub-standard-findings.md "../../../prescriptive-guidance/latest/patterns/automate-remediation-for-aws-security-hub-standard-findings.md")

**Related videos:**

- [AWS re:Invent 2025 - From Reactive to Proactive: Infrastructure
  governance by design (COP352)](https://www.youtube.com/watch?v=iXor74El2D8 "https://www.youtube.com/watch?v=iXor74El2D8")
