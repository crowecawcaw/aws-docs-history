# CloudWatch investigations

The CloudWatch investigations feature is a generative AI-powered assistant that can help you respond to
incidents in your system. It uses generative AI to scan your system's telemetry and quickly
surface telemetry data and suggestions that might be related to your issue. These
suggestions include metrics, logs, deployment events, and root-cause hypotheses with visual
representations when multiple resources are involved. For a complete list of types of data
that the AI assistant can surface, see [Insights that CloudWatch investigations can surface in
investigations](Investigations-SuggestionTypes.md "Investigations-SuggestionTypes.md").

You can conduct investigations without any additional configuration in CloudWatch operational
troubleshooting. When you start an investigation, CloudWatch investigations uses the permissions associated with
the signed-in user to investigate and analyze the resources associated with the alarm,
metrics, or Logs Insights query and provide troubleshooting suggestions. No resources are
created by the investigation, and every action taken by CloudWatch investigations is logged in CloudTrail for
traceability. The investigation provides you the following information to assist you with
operational troubleshooting:

- View AI-generated observations, suggestions, and hypotheses
- Access visual representations of multi-resource hypotheses
- Review natural language explanations and root cause analysis
- Access AI analysis of telemetry data, including metrics, logs, deployment events,
  AWS Health events, CloudTrail change events, X-Ray trace data, and CloudWatch Logs
  Insights queries

Configuring CloudWatch investigations will provide you with more in depth
investigations.
When you configure CloudWatch investigations, your investigations have the following additional capabilities:

- Accept or discard suggestions and observations

For each suggestion, you decide whether to add it to the investigation findings or
to discard it. This helps CloudWatch investigations refine and iterate toward the root cause of the
issue. CloudWatch investigations can help you find the root cause without having to manually identify and
query multiple metrics and other sources of telemetry and events. A troubleshooting
issue that would have taken hours of searching and switching between different
consoles can be solved in a much shorter time.

- Configure cross account access

Use CloudWatch cross-account observability to enable investigation to collect data from
other source accounts.

- Add new telemetry sources to the investigation

Adding data from CloudTrail event history helps CloudWatch investigations associate issues with change
events. Adding X-Ray provides improved topology and application mapping. You can
also add data from Application Signals to dive deeper into the health of your applications
and services, combining that telemetry with the other telemetry sources. If you use
Amazon EKS Clusters you can provide CloudWatch investigations access to your EKS resources, to provide more
granular information about the cluster resources that might be involved in the issue
under investigation.

- Add notes or comments to investigation findings

Being able to provide additional context to investigation finding to give
perspective during reporting or auditing.

- Execute suggested runbook remediations

CloudWatch investigations might suggest that you use an Automation runbook to attempt to automatically
resolve the issue. Automation is a capability in Systems Manager, another AWS
service. Automation runbooks define a series of steps, or actions, to be run on the
resources that you select. Each runbook is designed to address a specific issue.

- Share investigation results with team members

Without additional configuration investigation are linked with the signed-in
user's session. Other user's can't view the investigation results or continue the
investigation. After configuring CloudWatch investigations investigations are available to all users in
the account that have been granted the required permissions.

- End, archive, or reopen the investigation manually

Before CloudWatch investigations is configured in your account investigations run once and then
complete. Once CloudWatch investigations is configured, investigations can continue until resolved. After
the issue is resolved, the investigation is archived. If you have resolved the
issue, but the conditions that caused the investigation are still present, you can
manually close the investigation. If the conditions re-emerge you can restart (or
reopen) the investigation.

- Investigation reporting

When you complete an investigation, you can generate a comprehensive investigation
report that automatically captures all investigation findings, timeline events, and
recommended actions.
Configuration of CloudWatch investigations creates an investigation group in your account.
Each account can have one investigation group with up to 2 concurrent active investigations
in the investigation group. Each month, each account can create up to 150 enhanced
investigations with AI analysis. Investigation groups are account-level configurations. When
an investigation group is created in an account, it is used with all investigations started
in the account.

###### Note

When you configure CloudWatch investigations , CloudWatch will use the provided IAM role to periodically scan
resources in your account for the purpose of mapping resources and telemetry. Some
services like Lambda will invoke the KMS decrypt API on behalf of CloudWatch for certain API
calls related to describing or listing resources. This background process is performed
to ensure that the topology reflects the most recent state of the account and its
dependencies. This refresh occurs regardless of whether there is an active investigation
or not.

###### Topics

- [Methods to create an investigation](creation-methods.md "creation-methods.md")
- [Understanding hypothesis
  visualizations](Investigations-HypothesisVisualization.md "Investigations-HypothesisVisualization.md")
- [How CloudWatch investigations finds data for suggestions](data-usage-considerations.md "data-usage-considerations.md")
- [Costs associated with CloudWatch investigations](investigations-costs.md "investigations-costs.md")
- [Insights that CloudWatch investigations can surface in
  investigations](Investigations-SuggestionTypes.md "Investigations-SuggestionTypes.md")
- [AWS services where investigations are
  supported](Investigations-Services.md "Investigations-Services.md")
- [Conduct an CloudWatch investigation without
  additional configuration](Investigations-Ephemeral.md "Investigations-Ephemeral.md")
- [Configure CloudWatch investigations](Investigations-GetStarted.md "Investigations-GetStarted.md")
- [(Recommended) Best practices to
  enhance investigations](Investigations-RecommendedServices.md "Investigations-RecommendedServices.md")
- [Investigate operational issues in your
  environment](Investigations-Investigate.md "Investigations-Investigate.md")
- [Cross-account investigations](Investigations-cross-account.md "Investigations-cross-account.md")
- [Generate incident reports](Investigations-Incident-Reports.md "Investigations-Incident-Reports.md")
- [Integrations with other systems](Investigations-Integrations.md "Investigations-Integrations.md")
- [Security in CloudWatch investigations](Investigations-Security.md "Investigations-Security.md")
- [CloudWatch investigations data retention](Investigations-Retention.md "Investigations-Retention.md")
- [Troubleshooting](Investigations-Troubleshooting.md "Investigations-Troubleshooting.md")
