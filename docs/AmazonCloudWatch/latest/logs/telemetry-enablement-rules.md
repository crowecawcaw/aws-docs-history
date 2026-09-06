

# Automate log enablement with telemetry enablement rules
<a name="telemetry-enablement-rules"></a>

You can use telemetry enablement rules to automatically configure log collection for your AWS resources. Rules help you standardize log collection across your organization or accounts and ensure consistent monitoring coverage.

Enablement rules let you:
+ Automatically enable logging for new and existing resources that match your rule scope
+ Apply rules at the organization, organizational unit (OU), or individual account level
+ Filter which resources a rule affects using tags

Enablement rules currently support the following AWS telemetry sources: Amazon VPC Flow Logs, AWS WAF Logs, Route 53 Resolver Query Logs, NLB Access Logs, Amazon EKS Control Plane Logs, CloudTrail Data and Management Events, Amazon Bedrock AgentCore Logs, Amazon EC2 Detailed Metrics, AWS Security Hub, Amazon Bedrock AgentCore Gateway, Amazon Bedrock AgentCore Memory, and CloudFront Distribution.

For complete details on enablement rules including rule behavior, managing rules, troubleshooting, and service-specific considerations, see [Telemetry enablement rules](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/telemetry-config-rules.html) in the *Amazon CloudWatch User Guide*.

## Rule evaluation hierarchy
<a name="enablement-rules-hierarchy"></a>

Enablement rules are evaluated hierarchically: organizational rules first, then OU-level rules, then account-level rules. Rules at higher levels provide the baseline telemetry. Lower-level rules can add additional telemetry but cannot reduce it. If conflicting rules exist at the same scope, none are applied until the conflict is resolved.

## Creating an enablement rule
<a name="enablement-rules-create"></a>

**To create a telemetry enablement rule**

1. Open the CloudWatch console at [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/).

1. In the navigation pane, choose **Telemetry config**.

1. Choose the **Enablement rules** tab.

1. Choose **Add rule**.

1. Specify the rule name, scope (organization, OU, or account), data source, and telemetry type.

1. Optionally add tags to filter which resources the rule affects.

1. Choose **Create rule**.