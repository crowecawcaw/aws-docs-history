# Monitor AgentCore resources across accounts

You can use Amazon CloudWatch cross-account observability to monitor Amazon Bedrock AgentCore resources across multiple AWS accounts from a single monitoring account. This enables you to view agent metrics, traces, sessions, and resource data from source accounts without switching between accounts.

When cross-account observability is enabled, the AgentCore Observability console in your monitoring account automatically displays data from all linked source accounts alongside your local account data.

## Prerequisites

Before you can monitor AgentCore resources across accounts, you must complete the following:

- **Set up a monitoring account** – Configure a central AWS account as your monitoring account in CloudWatch Settings. For instructions, see [CloudWatch cross-account observability](../../../AmazonCloudWatch/latest/monitoring/CloudWatch-Unified-Cross-Account.md "../../../AmazonCloudWatch/latest/monitoring/CloudWatch-Unified-Cross-Account.md").
- **Link source accounts** – Link one or more source accounts to your monitoring account using AWS Organizations or individual account linking. Source accounts must share the required telemetry types (Metrics and Logs).
- **Deploy AgentCore resources** – Ensure your AgentCore agents, gateways, memory, identity, and built-in tool resources are deployed in the source accounts with observability enabled.

## How to set up cross-account monitoring

### Step 1: Configure the monitoring account

- Open the [CloudWatch console](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
- In the left navigation pane, choose **Settings**.
- In the **Monitoring account configuration** section, choose **Configure**.
- Select the telemetry types to share:
  - At minimum, select **Metrics** and **Logs** to enable AgentCore cross-account observability.

- Complete the monitoring account setup wizard.

### Step 2: Link source accounts

Link your source accounts to the monitoring account using one of the following methods:

- **AWS Organizations** (recommended) – Automatically links all accounts in your organization or organizational unit. New accounts are onboarded automatically.
- **Individual account linking** – Use a CloudFormation template or URL to link specific accounts.

When configuring source accounts, ensure the same telemetry types selected in the monitoring account are also enabled in the source account.

For detailed instructions, see [Link monitoring accounts with source accounts](../../../AmazonCloudWatch/latest/monitoring/CloudWatch-Unified-Cross-Account-Setup.md "../../../AmazonCloudWatch/latest/monitoring/CloudWatch-Unified-Cross-Account-Setup.md").

### Step 3: View cross-account data in AgentCore Observability

- Open the [AgentCore Observability console](https://console.aws.amazon.com/cloudwatch/home#gen-ai-observability "https://console.aws.amazon.com/cloudwatch/home#gen-ai-observability") in your monitoring account.
- The console automatically displays data from all linked source accounts.

## Filtering cross-account data

You can filter data by account in the sessions and traces tables:

- Use the property filter in the table.
- Select **Account ID** as the filter property.
- Enter the source account ID to filter results to a specific account.

## Limitations

- **Cross-account resource actions** – Some actions are unavailable for cross-account resources, such as navigating to the Bedrock console for resource details. You must sign in to the source account directly to perform these actions.
- **OAM link required** – Cross-account data is only visible while the OAM link between the monitoring and source accounts is active. If the link is removed, cross-account data will no longer appear.
- **Telemetry types** – Both the monitoring account and source account must have Metrics and Logs enabled for full AgentCore observability. If only a subset is shared, some data may be missing.
- **Regional** – Cross-account observability works within a single AWS Region. The monitoring account and source accounts must be in the same Region.

## Related resources

- [CloudWatch cross-account observability](../../../AmazonCloudWatch/latest/monitoring/CloudWatch-Unified-Cross-Account.md "../../../AmazonCloudWatch/latest/monitoring/CloudWatch-Unified-Cross-Account.md")
- [Get started with AgentCore Observability](observability-get-started.md "observability-get-started.md")
- [View observability data for your Amazon Bedrock AgentCore agents](observability-view.md "observability-view.md")
- [Observability Access Manager API Reference](../../../OAM/latest/APIReference/Welcome.md "../../../OAM/latest/APIReference/Welcome.md")
