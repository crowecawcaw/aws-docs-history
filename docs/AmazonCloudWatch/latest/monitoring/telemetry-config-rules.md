# Working with telemetry enablement rules

You can create telemetry enablement rules to automatically configure telemetry collection
for your AWS resources. Rules help you standardize telemetry collection across your
organization or accounts and ensure consistent monitoring coverage.

###### Topics

- [Enablement rule integration with AWS Config](#telemetry-config-automated "#telemetry-config-automated")
- [Understanding enablement rule behavior](#telemetry-config-rules-behavior "#telemetry-config-rules-behavior")
- [Creating telemetry enablement rules](#telemetry-config-rules-create "#telemetry-config-rules-create")
- [Managing telemetry rules](#telemetry-config-rules-manage "#telemetry-config-rules-manage")
- [Troubleshooting telemetry configuration](#telemetry-config-troubleshoot "#telemetry-config-troubleshoot")

## Enablement rule integration with AWS Config

CloudWatch telemetry auditing and configuration integrates with AWS Config to automatically discover
resources that match your enablement rule and apply it to your telemetry data collection. When
you create an enablement rule, the telemetry configuration creates a corresponding AWS Config
recorder. This recorder includes configuration items for the specific resource types you define
in the enablement rule.

Amazon CloudWatch uses AWS Config Internal service linked recorder.
You are not charged for CIs that CloudWatch uses as part of the Internal Service Linked Recorders.

###### Note

When you create an enablement rule, we discover non-compliant resources (those without
telemetry enabled) through AWS Config Configuration Items (CIs) before turning them on based
on your enablement rule scope. The initial discovery of the resources may take upto 24 hours to
complete in some cases.

Telemetry config uses AWS Config to:

- Discover resources across your organization or accounts
- Track telemetry configuration changes

## Understanding enablement rule behavior

Telemetry configuration follows specific patterns when evaluating and applying
rules:

Enablement rules are evaluated according to a hierarchical pattern. Organizational rules
are evaluated first, then rules that apply to organizational units (OUs), and finally rules that
apply to individual accounts. Rules at the organizational level provide the baseline required
telemetry for your organization. Rules at the OU and account level can collect additional
telemetry data, but they cannot collect less telemetry data. If such a rule is created, it will
create a rule conflict.

Within each scope (organization, OU, or account), rules must maintain uniqueness based on
their resource type, telemetry type, and destination configuration. Duplicate rules trigger a
conflict exception. If the same rule exists in different scopes, such as an organization level
rule for VPC Flow logs to CloudWatch and an OU level rule for VPC Flow logs, the rule higher in the
hierarchy is applied. However, if there are multiple rules in conflict, none of the rules are
applied.

For VPC Flow logs, Telemetry Config only creates new flow logs for resources that match the
rule scope. It does not delete or impact previously established VPC Flow logs, even if they
differ from current rule parameters. For CloudWatch Logs, existing log groups are maintained provided they
match the resource pattern.

If you update an enablement rule, only new resources that match the rule adopt the updated
configuration, the existing telemetry settings remain unchanged for existing resources. If a
resource becomes non-compliant with an existing rule due to manual deletion of telemetry data,
the new enablement rule is adopted once the resource is brought back into compliance.

## Creating telemetry enablement rules

When you create a telemetry enablement rule, you specify:

- The scope of the rule (organization, organizational unit, or account)
- The resource types the rule applies to
- The telemetry types to enable (metrics, logs, or traces)
- Optional tags to filter which resources the rule affects

###### To create a telemetry enablement rule

1. Open the CloudWatch console at
   [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. In the navigation pane, choose **Telemetry config**.
3. Choose the **Enablement rules** tab.
4. Choose **Add rule**.
5. For **Rule name**, enter a name for your rule.
6. For **Rule scope**, choose one of the following:
   - **Organization** - Rule applies across your entire AWS Organizations
   - **Organizational unit** - Rule applies to a specific OU
   - **Account** - Rule applies to a single account

7. For **Data source**, select the AWS service to configure.
8. For **Telemetry type**, select the types of telemetry to enable.
9. Optional: Add tags to filter which resources the rule affects.
10. Choose **Create rule**.

## Managing telemetry rules

After creating rules, you can edit or delete them. You can also view which resources each
rule affects and monitor rule compliance.

###### To manage an existing rule

1. Open the CloudWatch console at
   [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. In the navigation pane, choose **Telemetry config**.
3. Choose the **Enablement rules** tab.
4. Select a rule to view its details or choose one of these actions:
   - **Edit** - Modify rule settings
   - **Delete** - Remove the rule

## Troubleshooting telemetry configuration

This section describes common issues you might encounter when using telemetry configuration
and how to resolve them.

### Rule conflicts and resolution

When multiple rules apply to the same resource, telemetry configuration resolves conflicts
using these priorities:

1. Organizational-level rules take precedence over account-level rules
2. More specific tag matches take precedence over general rules
3. If there are multiple conflicting rules, none of the rules are applied, you must resolve
   the conflicts first.

### Common issues

Resources not appearing in discovery

Verify that:

- The resource type is supported
- AWS Config recorder is enabled
- You have appropriate IAM permissions

Rules not applying automatically

Check:

- Rule scope configuration
- Tag filters

###### Note

When you create an enablement rule, we discover non-compliant resources (those without
telemetry enabled) through AWS Config Configuration Items (CIs) before turning them on based
on your enablement rule scope. The initial discovery of the resources may take upto 24 hours
to complete in some cases.

### Service-specific considerations

**Amazon VPC Flow Logs**

When creating flow logs:

- Uses default pattern /aws/vpc/vpc-id if none specified
- Existing customer-created flow logs are preserved
- Rule updates only affect new flow logs
- You can use <vpc-id>, <account-id> macros to split log groups.
- CloudWatch does not create flow logs for VPCs that already are ingesting logs to CloudWatch
  Logs

**Amazon EKS Control Plane Logging**

When enabling control plane logging:

- Uses default CloudWatch log group pattern /aws/eks/<cluster-name>/cluster. Amazon EKS
  creates Log Group per Cluster automatically.
- Rule updates only affect new clusters or only clusters that do not have the scoped
  log types enabled
- Can enable specific log types: api, audit, authenticator, controllerManager,
  scheduler

**AWS WAF Web ACL Logs**

When creating WAF logs:

- Uses default CloudWatch log group pattern and always prefixes with aws-waf-logs-
- Rule updates only affect new Web ACLs or existing Web ACLs that do not have logging
  enabled to CloudWatch Logs
- CloudWatch does not enable logs for Web ACLs that already are ingesting logs to CloudWatch
  Logs

**Amazon Route 53 Resolver Logs**

When enabling resolver query logging:

- Uses default CloudWatch log group pattern /aws/route53resolver if none specified
- CloudWatch does not create resolver query logs for VPCs that already are ingesting logs to
  CloudWatch Logs
- Enablement rules configure Route 53 query logging for the your VPCs based on rule
  scope. CloudWatch does not discover Route 53 profiles and related configurations.

**NLB Access Logs**

When enabling access logs:

- Uses default CloudWatch log group pattern pattern with prefix /aws/nlb/access-logs if none
  specified
- CloudWatch does not enable log deliveries for NLBs that already are ingesting logs to CloudWatch
  Logs

**Amazon Bedrock AgentCore Telemetry**

- Enable both logs and traces emitted from all available Bedrock AgentCore primitives such as Runtime, Browser Tools, Code Interpreter Tools, etc.
  Follow the Telemetry Configure console experience for creating a logs delivery rule then followed by creating a traces delivery rule.
- When creating a trace delivery rule, Transaction Search will be enabled and additional permission policy will be created to allow
  for CloudWatch X-Ray to send correlated trace to managed log group in your account.
  In addition, X-Ray resource policy will be created to allow for current and new Bedrock AgentCore primitives to deliver traces to your account.

**CloudTrail Logs using service-linked channel**

When enabling CloudTrail logs using the SLC path:

- Uses managed CloudWatch log groups aws/cloudtrail/<event-types>
- Existing customer-created CloudTrail Trail forwarding configurations are
  preserved
- CloudWatch Enablement Rules only uses service-linked channel to ingest logs
- Events use the retention period configured for the log group
- For CloudTrail events, as part of the enablement wizard, you can choose at least one
  event type to ingest to CloudWatch.
- If events are delivered with delay (indicated by addendum reason DELIVERY_DELAY) and
  you previously configured a shorter retention period, delayed events might only be
  available for the duration of the shorter retention period.
- **Important**: For multi-region deployments: CloudWatch Enablement
  rules requires separate configuration in each AWS region and is not yet available in all
  regions. For comprehensive multi-region coverage, consider continuing to use CloudTrail
  trails sending events to CloudWatch until regional availability expands.
