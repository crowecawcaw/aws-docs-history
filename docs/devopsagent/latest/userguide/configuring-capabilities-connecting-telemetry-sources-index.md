# Connecting telemetry sources

AWS DevOps Agent provides three ways to connect to your telemetry sources.

## Built-in, 2-way integration

Currently, AWS DevOps Agent supports Dynatrace users with a built-in, 2-way integration enabling the following:

- **Topology resource mapping** - AWS DevOps Agent will augment your DevOps Agent Space Topology with entities and relationships available to it via a AWS DevOps Agent-hosted Dynatrace MCP server.
- **Automated Investigation triggering** - Dynatrace Workflows can be configured to trigger incident resolution Investigations from Dynatrace Problems.
- **Telemetry introspection** - AWS DevOps Agent can introspect Dynatrace telemetry as it investigates an issue via the AWS DevOps Agent-hosted Dynatrace MCP server.
- **Status updates** - AWS DevOps Agent will publish key investigation findings, root cause analyses, and generated mitigation plans to the Dynatrace user interface.

Next steps: Setup your Dynatrace connection See Dynatrace documentation (coming soon)]

## Built-in, 1 way integration

Currently, AWS DevOps Agent supports AWS CloudWatch, Datadog, New Relic, and Splunk users with built-in, 1 way integrations. The AWS CloudWatch built-in, 1-way integration requires no additional setup and enables the following:

- **Topology resource mapping** - AWS DevOps Agent will augment your DevOps Agent Space Topology with entities and relationships available to it via your configured primary and secondary AWS cloud accounts.
- **Telemetry introspection** - AWS DevOps Agent can introspect AWS CloudWatch telemetry as it investigates an issue via the IAM role(s) provided during primary and secondary AWS cloud account configuration.

The Datadog, New Relic, and Splunk built-in, 1 way integrations require setup and enable the following:

- **Automated Investigation triggering -** Datadog, New Relic, and Splunk events can be configured to trigger AWS DevOps Agent incident resolution Investigations via AWS DevOps Agent webhooks.
- **Telemetry introspection** - AWS DevOps Agent can introspect Datadog, New Relic, and Splunk telemetry as it investigates an issue via the each providers remote MCP server.

Next steps: Setup your Datadog connection [Connecting Datadog](configuring-capabilities-connecting-telemetry-sources-datadog.md "configuring-capabilities-connecting-telemetry-sources-datadog.md")] Next steps: Setup your New Relic connection [Connecting New Relic](configuring-capabilities-connecting-telemetry-sources-newrelic.md "configuring-capabilities-connecting-telemetry-sources-newrelic.md")] Next steps: Setup your Splunk connection [Connecting Splunk](configuring-capabilities-connecting-telemetry-sources-splunk.md "configuring-capabilities-connecting-telemetry-sources-splunk.md")]

## Bring-your-own telemetry sources

For any other telemetry source, including Grafana dashboards/alarms and Prometheus metrics, you can leverage AWS DevOps Agent’s support for both webhook and MCP server integration.

## Onboarding Process

Onboarding your observability system involves three stages:

1. **Connect** - Establish connection to your telemetry provider by configuring account access credentials
2. **Enable** - Activate your connected telemetry provider in specific Agent spaces
3. **Configure webhooks** - Capture webhook details to trigger investigations in designated Agent spaces

## Connections

- Dynatrace
- DataDog
- New Relic
- Splunk
