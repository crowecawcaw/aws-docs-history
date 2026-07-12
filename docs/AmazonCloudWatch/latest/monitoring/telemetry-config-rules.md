# Telemetry enablement rules

You can create telemetry enablement rules to automatically configure telemetry
collection for your AWS resources. Rules help you standardize telemetry collection across
your organization or accounts and ensure consistent monitoring coverage.

###### Topics

- [How rules work](#telemetry-config-rules-behavior "#telemetry-config-rules-behavior")
- [Creating a telemetry enablement rule](#telemetry-config-rules-create "#telemetry-config-rules-create")
- [Managing telemetry rules](#telemetry-config-rules-manage "#telemetry-config-rules-manage")
- [Supported data sources](#telemetry-config-troubleshoot-service "#telemetry-config-troubleshoot-service")

## How rules work

Telemetry configuration follows specific patterns when evaluating and applying
rules.

### Rule evaluation hierarchy

Enablement rules are evaluated according to a hierarchical pattern. Organizational
rules are evaluated first, then rules that apply to organizational units (OUs), and finally
rules that apply to individual accounts. Rules at the organizational level provide the
baseline required telemetry for your organization. Rules at the OU and account level can
collect additional telemetry data, but they cannot collect less telemetry data. If such a
rule is created, it will create a rule conflict.

Within each scope (organization, OU, or account), rules must maintain uniqueness based
on their resource type, telemetry type, and destination configuration. Duplicate rules
trigger a conflict exception. If the same rule exists in different scopes, such as an
organization level rule for Amazon VPC Flow logs to CloudWatch and an OU level rule for Amazon VPC Flow
logs, the rule higher in the hierarchy is applied. However, if there are multiple
conflicting rules, none of the rules are applied.

When multiple rules apply to the same resource, telemetry configuration resolves
conflicts using these priorities:

1. Organizational-level rules take precedence over account-level rules
2. More specific tag matches take precedence over general rules
3. If there are multiple conflicting rules, none of the rules are applied. You must
   resolve the conflicts first.

### Rule behavior on updates

If you update an enablement rule, only new resources that match the rule adopt the
updated configuration. The existing telemetry settings remain unchanged for existing
resources. If a resource becomes non-compliant with an existing rule due to manual deletion
of telemetry data, the new enablement rule is adopted once the resource is brought back
into compliance.

For Amazon VPC Flow logs, telemetry config only creates new flow logs for resources that
match the rule scope. It does not delete or impact previously established Amazon VPC Flow logs,
even if they differ from current rule parameters. For CloudWatch Logs, existing log groups are
maintained provided they match the resource pattern.

### Integration with AWS Config

CloudWatch telemetry auditing and configuration integrates with AWS Config to automatically
discover resources that match your enablement rule and apply it to your telemetry data
collection. When you create an enablement rule, the telemetry configuration creates a
corresponding AWS Config recorder. This recorder includes configuration items for the specific
resource types you define in the enablement rule.

Amazon CloudWatch uses AWS Config Internal service linked recorder.
You are not charged for CIs that CloudWatch uses as part of the Internal Service Linked Recorders.

###### Note

When you create an enablement rule, we discover non-compliant resources (those
without telemetry enabled) through AWS Config Configuration Items (CIs) before turning
them on based on your enablement rule scope. The initial discovery of the resources may
take up to 24 hours to complete in some cases.

Telemetry config uses AWS Config to:

- Discover resources across your organization or accounts
- Track telemetry configuration changes

### Rules across Regions

When you create a rule with target Regions, the current Region becomes the
_home Region_ for that rule. The rule is automatically replicated to the
spoke Regions you select.

Key concepts for multi-Region rules:

- Replicated rules cannot be edited or deleted in spoke Regions. You must navigate to
  the home Region to modify or remove them.
- If you select **All regions**, new Regions are automatically
  included when you opt in to them.
- The system periodically reconciles rules across Regions to correct any drift between
  the home Region and spoke Regions.
- Tags applied to rules in the home Region are replicated to spoke Regions.

When a replicated rule is created, updated, or deleted in a spoke Region, AWS CloudTrail
records an `AwsServiceEvent` in the spoke Region. These events are logged with
`observabilityadmin.amazonaws.com` as the invoking service and include the
rule ARN in the spoke Region. You can use these events to audit multi-Region rule
replication activity.

The following is an example AWS CloudTrail event recorded when a replicated rule is created
in a spoke Region:

```
{
    "eventVersion": "1.11",
    "userIdentity": {
        "accountId": "`123456789012`",
        "invokedBy": "observabilityadmin.amazonaws.com"
    },
    "eventTime": "2026-04-06T19:50:37Z",
    "eventSource": "observabilityadmin.amazonaws.com",
    "eventName": "CreateTelemetryRule",
    "awsRegion": "`us-east-1`",
    "sourceIPAddress": "observabilityadmin.amazonaws.com",
    "userAgent": "observabilityadmin.amazonaws.com",
    "requestParameters": null,
    "responseElements": null,
    "eventID": "`435d6da2-d099-4775-8944-1e039418de6f`",
    "readOnly": false,
    "resources": [
        {
            "accountId": "`123456789012`",
            "type": "AWS::ObservabilityAdmin::TelemetryRule",
            "ARN": "arn:aws:observabilityadmin:`us-east-1`:`123456789012`:telemetry-rule/`my-multi-region-rule`"
        }
    ],
    "eventType": "AwsServiceEvent",
    "managementEvent": true,
    "recipientAccountId": "`123456789012`",
    "eventCategory": "Management"
}
```

The `eventName` field reflects the operation performed on the replicated
rule: `CreateTelemetryRule`, `UpdateTelemetryRule`, or
`DeleteTelemetryRule`. The `eventType` is always
`AwsServiceEvent` because the operation is performed by the
ObservabilityAdmin service on behalf of the customer, not by a direct customer API call.

## Creating a telemetry enablement rule

When you create a telemetry enablement rule, you specify:

- The scope of the rule (organization, organizational unit, or account)
- The resource types the rule applies to
- The telemetry types to enable (metrics, logs, or traces)
- Optional tags to filter which resources the rule affects
- Optional target Regions to replicate the rule across multiple Regions

###### To create a telemetry enablement rule

1. Open the CloudWatch console at
   [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. In the navigation pane, choose **Ingestion**.
3. Choose the **Enablement rules** tab.
4. Choose **Add rule**.
5. For **Rule name**, enter a name for your rule.
6. For **Rule scope**, choose one of the following:

   - **Organization** – Rule applies across your entire
     AWS Organizations
   - **Organizational unit** – Rule applies to a specific
     OU
   - **Account** – Rule applies to a single account

7. For **Data source**, select the AWS service to configure.
8. For **Telemetry type**, select the types of telemetry to
   enable.
9. (Optional) Add tags to filter which resources the rule affects.
10. (Optional) For **Target regions**, select the Regions where you want
    this rule to apply. The current Region is automatically designated as the home Region for
    the rule. If you select **All regions**, new Regions are automatically
    included when you opt in to them.
11. Choose **Create rule**.

## Managing telemetry rules

After creating rules, you can edit or delete them. You can also view which resources
each rule affects and monitor rule compliance.

###### To manage an existing rule

1. Open the CloudWatch console at
   [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. In the navigation pane, choose **Ingestion**.
3. Choose the **Enablement rules** tab.
4. Select a rule to view its details or choose one of these actions:

   - **Edit rule** – Modify rule settings
   - **Delete** – Remove the rule

### Managing replicated rules

When you view a replicated rule in a spoke Region, the console displays an
informational alert indicating that the rule was replicated from another Region. The
**Edit rule** and **Delete** actions are disabled for
replicated rules in spoke Regions.

To edit or delete a replicated rule, navigate to the home Region where the rule was
originally created. The home Region is displayed in the informational alert.

You can add or modify tags on replicated rules in spoke Regions. Tag changes made in
spoke Regions apply only to the local copy of the rule and are not replicated back to the
home Region.

## Supported data sources

The following data sources are supported by telemetry enablement rules. Each data
source has specific behavior and configuration considerations.

**Amazon VPC Flow Logs**

When creating flow logs:

- Uses default pattern /aws/vpc/vpc-id if none specified
- Existing customer-created flow logs are preserved
- Rule updates only affect new flow logs
- You can use <vpc-id>, <account-id> macros to split log groups.
- CloudWatch does not create flow logs for VPCs that already are ingesting logs to CloudWatch
  Logs
- When you enable automatic configuration updates on a rule, CloudWatch monitors the flow
  logs it created and remediates configuration drift. Drift occurs when the log format,
  traffic type, maximum aggregation interval, or destination log group name pattern of a
  rule-managed flow log no longer matches the rule. To remediate, CloudWatch creates a new flow
  log with the correct configuration and then deletes the outdated one.
- Automatic configuration updates apply only to Amazon VPC Flow Logs. CloudWatch never modifies
  or deletes flow logs that you created.

**Amazon EKS Control Plane Logs**

When enabling control plane logging:

- Uses default CloudWatch log group pattern /aws/eks/<cluster-name>/cluster. Amazon
  EKS creates Log Group per Cluster automatically.
- Rule updates only affect new clusters or only clusters that do not have the scoped
  log types enabled
- Can enable specific log types: api, audit, authenticator, controllerManager,
  scheduler

**AWS WAF Web ACL Logs**

When creating WAF logs:

- Uses default CloudWatch log group pattern and always prefixes with aws-waf-logs-
- Rule updates only affect new Web ACLs or existing Web ACLs that do not have
  logging enabled to CloudWatch Logs
- CloudWatch does not enable logs for Web ACLs that already are ingesting logs to CloudWatch
  Logs

**Amazon Route 53 Resolver Logs**

When enabling resolver query logging:

- Uses default CloudWatch log group pattern /aws/route53resolver if none specified
- You can use <account-id> macros to split log groups.
- CloudWatch does not create resolver query logs for VPCs that already are ingesting logs
  to CloudWatch Logs
- Enablement rules configure Route 53 query logging for your VPCs based on rule
  scope. CloudWatch does not discover Route 53 profiles and related configurations.

**NLB Access Logs**

When enabling access logs:

- Uses default CloudWatch log group pattern with prefix /aws/nlb/access-logs if none
  specified
- CloudWatch does not enable log deliveries for NLBs that already are ingesting logs to
  CloudWatch Logs

**CloudTrail Logs using service-linked channel**

When enabling CloudTrail logs using the SLC path:

- Uses managed CloudWatch log groups aws/cloudtrail/<event-types>
- Existing customer-created CloudTrail Trail forwarding configurations are
  preserved
- CloudWatch Enablement Rules only uses service-linked channel to ingest logs
- Events use the retention period configured for the log group
- For CloudTrail events, as part of the enablement wizard, you can choose at least
  one event type to ingest to CloudWatch.
- If events are delivered with delay (indicated by addendum reason DELIVERY\_DELAY)
  and you previously configured a shorter retention period, delayed events might only be
  available for the duration of the shorter retention period.

###### Tip

To configure CloudTrail logs across multiple Regions, use the
**Target regions** selector when creating your enablement rule. This
replicates the rule to your selected Regions automatically from the home Region.

**Amazon Amazon EC2 Detailed Metrics**

When enabling detailed monitoring:

- Instance state changes may affect metric collection

**AWS Security Hub**

When enabling Security Hub logging:

- Uses managed CloudWatch log group pattern aws/securityhub\_cspm/findings
- CloudWatch does not enable log deliveries for Security Hub that already are ingesting
  logs to managed CloudWatch Logs

**Amazon Bedrock AgentCore**

- Enable both logs and traces emitted from all available Bedrock AgentCore
  primitives such as Runtime, Browser Tools, Code Interpreter Tools, etc. Follow the
  Telemetry Configure console experience for creating a logs delivery rule then followed
  by creating a traces delivery rule.
- When creating a trace delivery rule, Transaction Search will be enabled and
  additional permission policy will be created to allow for CloudWatch X-Ray to send correlated
  trace to managed log group in your account. In addition, X-Ray resource policy will be
  created to allow for current and new Bedrock AgentCore primitives to deliver traces to
  your account.

**Amazon Bedrock Agentcore Gateway**

When enabling Bedrock Agentcore Gateway logging:

- Uses default CloudWatch log group pattern /aws/bedrock/agentcore if none specified
- CloudWatch does not enable log deliveries for Bedrock Agentcore Gateway that already are
  ingesting logs to CloudWatch Logs

**Amazon Bedrock Agentcore Memory**

When enabling Bedrock Agentcore Memory logging:

- Uses default CloudWatch log group pattern /aws/bedrock/agentcore if none specified
- CloudWatch does not enable log deliveries for Bedrock Agentcore Memory that already are
  ingesting logs to CloudWatch Logs

**Amazon CloudFront Distribution**

When enabling CloudFront Distribution logging:

- CloudWatch does not enable log deliveries for CloudFront distributions that already are
  ingesting logs to CloudWatch Logs

**Amazon S3 Server Access Logs**

S3 server access logging has the following constraints:

- Supports the LOGS telemetry type with log type
  `S3_SERVER_ACCESS_LOGS` only.
- Supports only CloudWatch Logs as the destination type.
- Supports only tag-based selection criteria to target specific S3 buckets.

**Amazon MSK Cluster Metrics**

When enabling MSK Cluster metrics:

- Only supports METRICS telemetry type
- You can configure enhanced monitoring levels (PER\_BROKER, PER\_TOPIC\_PER\_BROKER,
  etc.) to control the granularity of metrics collected
- Rules with different enhanced monitoring levels can coexist for the same MSK
  cluster

**OpenTelemetry Enrichment Metrics**

When enabling OpenTelemetry Enrichment metrics:

- Only supports METRICS telemetry type
- This is an account-level enablement with no user-configurable destination
- Resource-level selection criteria is not supported

**Amazon Bedrock Agentcore Workload Identity**

When enabling Bedrock Agentcore Workload Identity logging:

- Uses default CloudWatch log group pattern /aws/bedrock/agentcore if none
  specified
- CloudWatch does not enable log deliveries for Bedrock Agentcore Workload Identity that
  already are ingesting logs to CloudWatch Logs
