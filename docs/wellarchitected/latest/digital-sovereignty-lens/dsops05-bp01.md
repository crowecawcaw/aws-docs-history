# DSOPS05-BP01 Enable independent root cause analysis and

remediation

Provide engineering teams with the tools, knowledge, and permissions
necessary to independently identify, analyze, and resolve compliance
violations. Self-service capabilities reduce dependency on
centralized security teams while accelerating remediation timelines
and improving the overall security posture.

**Desired outcome:** Engineering
teams can independently conduct root cause analysis and implement
remediation for compliance violations within their scope of
responsibility, using standardized tools and processes.

**Common anti-patterns**:

- Manual scanning of compliance reports and findings
- A limited number of fully vetted persons have access to security
  and compliance findings
- No standardized process for root cause analysis
- Missing automation and self-service capabilities
- Lack of historical compliance data for trend analysis

**Benefits of establishing this best
practice:**

- Reduced Mean Time to Remediation through immediate team action
- Improved compliance posture through faster issue resolution
- Decreased operational load on security and compliance teams
- Enhanced security awareness and capability within engineering
  teams
- Better allocation of specialized security expertise towards
  resolving complex issues
- Improved team ownership and accountability for security outcomes

**Level of risk exposed if this best practice
is not established:** Low

## Implementation guidance

Effective Root Cause Analysis (RCA) and remediation requires the
following steps:

1. Identifying resources having compliance issues
2. Collecting data related to those resources
3. Determining the root cause
4. Remediating the problem
5. Verifying that the remediation was successful
6. Documenting the solution

### Implementation steps

1.  **Identify and collect
    data**: Your chosen compliance and security tooling
    should create consolidated findings for developers to
    review. Consider the following.
    - **Scoped access**:
      Developers should only see compliance information about
      the resources they are responsible for.
    - **Cross-Service
      correlation**: Developers expect tools to
      correlate logs and events across multiple services, and
      generate a single set of actionable findings.
    - **Information
      relevancy**: Developers expect the following
      minimum information from findings.
      - Affected Resource ID, Account ID, and Region ID
      - Severity of the finding
      - Source of evaluation. (For example,
        [AWS Config](../../../config/latest/developerguide/WhatIsConfig.md "../../../config/latest/developerguide/WhatIsConfig.md") Rules,
        [Amazon Macie](../../../macie/latest/user/what-is-macie.md "../../../macie/latest/user/what-is-macie.md") evaluations,
        [Amazon GuardDuty](../../../guardduty/latest/ug/what-is-guardduty.md "../../../guardduty/latest/ug/what-is-guardduty.md") evaluations)
      - Date of evaluation
      - The estimated impact of the finding
      - Suggested remediation

2.  **Integrate with AWS
    Services**: While there are several ways to
    identify and collect data related to non-compliant
    resources, we discuss 3 options below.
    - **Use AWS Security Hub and Amazon EventBridge**: Security Hub detects security
      and compliance issues by automatically correlating and
      enriching events from multiple sources. These include
      services providing security posture management (Security Hub CSPM), vulnerability management
      ([Amazon Inspector](../../../inspector/latest/user/what-is-inspector.md "../../../inspector/latest/user/what-is-inspector.md")), sensitive data detection (Amazon Macie), and threat detection (Amazon GuardDuty) related
      capabilities.

    Security Hub automatically sends new findings and
    updates to EventBridge as
    **events**. Findings
    appear as one of the following event types in
    EventBridge.

        + Security Hub Findings - Imported
        + Security Hub Findings - Custom Action
        + Security Hub Insight Results

    You can write EventBridge
    **rules** to match these
    event types. The following pattern will match the
    Security Hub Findings - Imported
    event type, extract the matching key-value pairs. For
    example, you can match against specific attributes like
    accountId, and
    region to selectively forward
    Security Hub generated events to the most appropriate
    recipients.

    ```

    {
      "source": [
        "aws.securityhub"
      ],
      "detail-type": [
        "Security Hub Findings - Imported"
      ],
      "detail": {
        "findings": {
          "Region": [ "us-east-1"],
          "AccountId" : ["123456789012"]
        }
      }
    }

    ```

    EventBridge rules output JSON data structures that can
    be delivered to multiple
    [targets](../../../eventbridge/latest/userguide/eb-targets.md "../../../eventbridge/latest/userguide/eb-targets.md"),
    including
    [Amazon SNS](../../../sns/latest/dg/welcome.md "../../../sns/latest/dg/welcome.md") topics. This approach allows developers to
    receive scoped but detailed diagnostic information to
    conduct further root cause analysis.
    - **Use Security Hub and Amazon Security Lake**: When you send Security Hub
      findings to Security Lake, it automatically constructs
      an
      [AWS Glue](../../../glue/latest/dg/what-is-glue.md "../../../glue/latest/dg/what-is-glue.md") database named
      amazon_security_lake_glue_db\_<region_name>
      with associated tables. The database and tables are
      managed through
      [AWS Lake Formation](../../../lake-formation/latest/dg/what-is-lake-formation.md "../../../lake-formation/latest/dg/what-is-lake-formation.md"). By default Security Hub findings
      reside in a table named
      amazon_security_lake_table\_<region_name>\_sh_findings_2_0.

    Having a tabular representation of Security Hub findings
    offers several advantages. For example, you can perform
    the following actions:

        + Use
         [Amazon Athena](../../../athena/latest/ug/what-is.md "../../../athena/latest/ug/what-is.md") to
         [query
         the Security Hub findings table](../../../security-lake/latest/userguide/security-hub-query-examples-sourceversion2.md "../../../security-lake/latest/userguide/security-hub-query-examples-sourceversion2.md").
        + Construct flattened views with a filtered set of
         columns, for example with
         accountid and
         region.
        + Additionally, apply
         [fine-grained
         access control (FGAC)](../../../lake-formation/latest/dg/data-filtering.md "../../../lake-formation/latest/dg/data-filtering.md") over your tables and
         views.

    - **Use API-based
      Filtering**: Use the
      GetFindings API and apply filters for
      specific resource ARNs or tags, region, accountId and so
      on. Then build team-specific dashboards with
      [Quick Suite](../../../quicksight/latest/user/welcome.md "../../../quicksight/latest/user/welcome.md") to display those findings.

3.  **Perform root cause
    analysis**: Once developers receive compliance
    notifications, they need access to root cause analysis (RCA)
    tools to investigate and understand the underlying issues.
    The specific tools and permissions required depend on the
    type of compliance violation and the AWS services involved.

Two common RCA techniques are:

    * [Five
     Whys Analysis](https://wa.aws.amazon.com/wellarchitected/2020-07-02T19-33-23/wat.concept.fivewhys.en.html "https://wa.aws.amazon.com/wellarchitected/2020-07-02T19-33-23/wat.concept.fivewhys.en.html")
    * [Ishikawa
     Diagrams](https://en.wikipedia.org/wiki/Ishikawa_diagram "https://en.wikipedia.org/wiki/Ishikawa_diagram")

Both techniques require the ability to collect and analyze
data from multiple sources, such as logs, events, and
metrics.

When you enable Security Standards with Security Hub CSPM,
Security Hub consolidates findings from multiple services,
such as Config Rules, Macie, and GuardDuty, and generates a
single set of actionable insights. The following example
shows a non-compliant
[Amazon DynamoDB](../../../amazondynamodb/latest/developerguide/Introduction.md "../../../amazondynamodb/latest/developerguide/Introduction.md") table, where delete protection is not
enabled. The Security Hub finding provides the following
information:

    * Affected Resource ID, Account ID, and Region ID
    * Severity of the finding
    * Source of evaluation. (For example, Config Rules, Macie
     evaluations, GuardDuty evaluations). In this case the
     rule applied was
     [DynamoDB.6](../../../securityhub/latest/userguide/dynamodb-controls.md#dynamodb-6 "../../../securityhub/latest/userguide/dynamodb-controls.md#dynamodb-6").
    * Date of evaluation
    * The estimated impact of the finding
    * Suggested remediation

The following snippet is from a finding triggered by the
DynamoDB.6 rule

```

{
  "AwsAccountId": "XXXXXXX",
  "AwsAccountName": "XXXXXXX",
  "Compliance": {
    "Status": "FAILED",
    "SecurityControlId": "DynamoDB.6",
    "RelatedRequirements": ["NIST.800-53.r5 CA-9(1)", "NIST.800-53.r5 CM-2","NIST.800-53.r5 CM-2(2)", "NIST.800-53.r5 CM-3","NIST.800-53.r5 SC-5(2)"
    ],
    "AssociatedStandards": [
      {
        "StandardsId": "standards/nist-800-53/v/5.0.0"
      }
    ]
  },
  "CreatedAt": "2025-01-23T02:26:29.771Z",
  "Description": "This control checks whether an Amazon DynamoDB table has deletion protection enabled. The control fails if a DynamoDB table doesn't have deletion protection enabled.",
  "FindingProviderFields": {
    ....
  },
  ...
  "Remediation": {
    "Recommendation": {
      "Text": "For information on how to correct this issue, consult the AWS Security Hub controls documentation.",
      "Url": "https://docs.aws.amazon.com/console/securityhub/DynamoDB.6/remediation"
    }
  },
  "Resources": [
    {
      "Details": {
        "AwsDynamoDbTable": {
          "TableId": "XXXXXXXXXXXXX",
          "TableName": "Table-Name-XXXXXXXXXX",
          "DeletionProtectionEnabled": false
        }
      },
      "Id": "arn:aws:dynamodb:region-id:XXXXXXXXXX:table/Table-Name-XXXXXXXXXX",
      "Partition": "AWS",
      "Region": "region-id",
      "Type": "AwsDynamoDbTable"
    }
  ]
  ...
}

```

Extract findings using one of the methods described in step
2 and send findings over to concerned engineering teams.
Consider integrating with team messaging apps or your
organizational IT Service Management (ITSM) software to
enhance operational maturity. 4. **Remediation, verification, and
documentation**: Once the root cause is identified,
engineering teams can remediate the problem. This may
involve automated remediation, manual remediation, or a
combination of both. The team should also verify that the
remediation was successful, and document the solution for
future reference.

[AWS Systems Manager](../../../systems-manager/latest/userguide/what-is-systems-manager.md "../../../systems-manager/latest/userguide/what-is-systems-manager.md") automation provides several runbooks
to
[automatically
remediate](../../../systems-manager-automation-runbooks/latest/userguide/automation-runbook-reference.md "../../../systems-manager-automation-runbooks/latest/userguide/automation-runbook-reference.md") compliance violations. While there are no
runbooks yet to remediate the DynamoDB.6 finding listed in
this example, for more information, see
[this
re:Post entry](https://repost.aws/knowledge-center/dynamodb-accidental-delete-protection "https://repost.aws/knowledge-center/dynamodb-accidental-delete-protection") for remediation options.

## Resources

**Related best practices:**

- [SEC04-BP01
  Configure service and application logging](../security-pillar/sec_detect_investigate_events_app_service_logging.md "../security-pillar/sec_detect_investigate_events_app_service_logging.md")
- [SEC04-BP02
  Capture logs, findings, and metrics in standardized
  locations](../security-pillar/sec_detect_investigate_events_logs.md "../security-pillar/sec_detect_investigate_events_logs.md")
- [SEC04-BP03
  Correlate and enrich security alerts](../security-pillar/sec_detect_investigate_events_security_alerts.md "../security-pillar/sec_detect_investigate_events_security_alerts.md")
- [SEC04-BP04
  Initiate remediation for non-compliant resources](../security-pillar/sec_detect_investigate_events_noncompliant_resources.md "../security-pillar/sec_detect_investigate_events_noncompliant_resources.md")
- [SEC10-BP02
  Develop incident management plans](../security-pillar/sec_incident_response_develop_management_plans.md "../security-pillar/sec_incident_response_develop_management_plans.md")
- [SEC10-BP04
  Develop and test security incident response playbooks](../security-pillar/sec_incident_response_playbooks.md "../security-pillar/sec_incident_response_playbooks.md")
- [SEC10-BP05
  Pre-provision access](../security-pillar/sec_incident_response_pre_provision_access.md "../security-pillar/sec_incident_response_pre_provision_access.md")
- [SEC10-BP06
  Pre-deploy tools](../security-pillar/sec_incident_response_pre_deploy_tools.md "../security-pillar/sec_incident_response_pre_deploy_tools.md")
- [SEC10-BP07
  Run simulations](../security-pillar/sec_incident_response_run_game_days.md "../security-pillar/sec_incident_response_run_game_days.md")
- [SEC10-BP08
  Establish a framework for learning from incidents](../security-pillar/sec_incident_response_establish_incident_framework.md "../security-pillar/sec_incident_response_establish_incident_framework.md")

**Related documents:**

- [Visualizing
  AWS Config data using Amazon Athena and Quick Suite](https://aws.amazon.com/blogs/mt/visualizing-aws-config-data-using-amazon-athena-and-amazon-quicksight/ "https://aws.amazon.com/blogs/mt/visualizing-aws-config-data-using-amazon-athena-and-amazon-quicksight/")
- [Deploy
  Conformance Packs across an Organization with Automatic
  Remediation](https://aws.amazon.com/blogs/mt/deploying-conformance-packs-across-an-organization-with-automatic-remediation/ "https://aws.amazon.com/blogs/mt/deploying-conformance-packs-across-an-organization-with-automatic-remediation/")
- [Remediate
  non-compliant AWS Config rules with AWS Systems Manager
  Automation runbooks](https://aws.amazon.com/blogs/mt/remediate-noncompliant-aws-config-rules-with-aws-systems-manager-automation-runbooks/ "https://aws.amazon.com/blogs/mt/remediate-noncompliant-aws-config-rules-with-aws-systems-manager-automation-runbooks/")
- [Automated
  Response and Remediation with AWS Security Hub](https://aws.amazon.com/blogs/security/automated-response-and-remediation-with-aws-security-hub/ "https://aws.amazon.com/blogs/security/automated-response-and-remediation-with-aws-security-hub/")
- [Manage
  Custom AWS Config Rules with Remediation Using AWS Config
  Conformance Pack](https://aws.amazon.com/blogs/mt/manage-custom-aws-config-rules-with-remediation-using-conformance-packs/ "https://aws.amazon.com/blogs/mt/manage-custom-aws-config-rules-with-remediation-using-conformance-packs/")
- [Analyzing
  AWS CloudTrail in Amazon CloudWatch](https://aws.amazon.com/blogs/mt/analyzing-cloudtrail-in-cloudwatch/ "https://aws.amazon.com/blogs/mt/analyzing-cloudtrail-in-cloudwatch/")

**Related examples:**

- [Cloud
  Intelligence Dashboards - AWS Config Resource Compliance
  Dashboard (CRCD)](https://github.com/aws-samples/config-resource-compliance-dashboard "https://github.com/aws-samples/config-resource-compliance-dashboard")

**Related videos:**

- [AWS re:Invent 2025 - Building and validating cloud controls with
  generative AI (COP350)](https://www.youtube.com/watch?v=bRTSI-UKl0s "https://www.youtube.com/watch?v=bRTSI-UKl0s")
- [AWS re:Invent 2020: A security operator's guide to practical AWS CloudTrail analysis](https://www.youtube.com/watch?v=Tr78kq-Oa70&t=623s "https://www.youtube.com/watch?v=Tr78kq-Oa70&t=623s") - Learn more about the
  [AWS CloudTrail](../../../awscloudtrail/latest/userguide/cloudtrail-user-guide.md "../../../awscloudtrail/latest/userguide/cloudtrail-user-guide.md") service and its value for security
  operations. The session dives deep into sources of data
  enrichment and reviews how to leverage AWS CloudTrail as part
  of your security operations and incident response procedures.
- [Monitor
  AWS Resources with Scheduled Reports: 2024 Quick Suite
  Learning Series](https://www.youtube.com/watch?v=3QECLeNPKCE "https://www.youtube.com/watch?v=3QECLeNPKCE") - Landing zone managers want a
  centralized view to understand compliance of different
  accounts and resources within their AWS Environments. With
  [Quick Suite](../../../quicksight/latest/user/welcome.md "../../../quicksight/latest/user/welcome.md"), you can achieve one dashboard using data
  exported from
  [AWS Config](../../../config/latest/developerguide/WhatIsConfig.md "../../../config/latest/developerguide/WhatIsConfig.md") summarizing information on accounts in the
  organization. Lastly, we can create reports with actionable
  insights for the owners of those accounts.
