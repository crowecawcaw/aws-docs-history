# Customized findings responses

You can choose how you want AMS Accelerate to respond to some findings (non-compliant Config rules). You can configure AMS to respond to findings it by remediating the finding,
asking for your approval to remediate, or just reporting to you in your next Monthly Business Review (MBR). You can change the default responses for
AMS Accelerate Config rules. To see the rules, go to [Configuration Compliance > Table of rules](acc-sec-compliance.md "acc-sec-compliance.md")
or download the rules table as a ZIP file [ams_config_rules.zip](samples/ams_config_rules.md "samples/ams_config_rules.md").

Changing default responses helps you to increase the security and compliance state of your account by allowing more findings to be remediated. When you remediate more findings,
you have fewer cases that need to wait for a manual review and approval. The extensive library of AMS remediation runbooks constantly fixes non-compliant
resources and you are contacted only when required.

Customized responses are used only with new resources or existing resources with new events. For example, a resource that became
non-compliant after a change. This is because older resources tend to require a deeper inspection before remediation and it's easier to enforce
the resource remediation as they are created or changed. To request remediation of the finding for any resource at any time, submit a service request.

## Requesting a change in the default responses

Cloud Architects (CAs) work with you during on-boarding to collect your preferences. CAs
then setup the initial configuration on internal AMS systems. After onboarded, create a Service Request to request
updates to your configurations. You can request configuration updates as many times as needed.
Please note that Operations only updates configurations for the account in which the
service request was created. If you need to update multiple accounts at the same time,
contact your Cloud Architect. Your CA will ask you to cut a service request with
your preferences for audit purposes.

## Changing default responses for your findings and accounts

You always need a response preference for each account and finding. AMS provides a default response (see
[Configuration Compliance](acc-sec-compliance.md "acc-sec-compliance.md")), so this configuration is optional.
You can change the default responses for each finding to the following options:

- Remediate: AMS manually or automatically remediates the finding. AMS reviews the remediation and lets you know if it fails.
- Request approval: AMS creates an outbound case to notify you about the finding. Use this option when you want to to review the finding
  before approving its remediation or exempting it. AMS then executes the action you prefer.
- No action (report only): AMS takes no action to remediate or escalate the finding. The findings might still appear on the console and
  reports presented during MBRs.

###### Note

You can't change the configuration of rules that must be remediated by AMS. For example, enabling Amazon GuardDuty and VPC Flow Logs.

## Changing default responses by resources

You can further configure the response to specific resources using tags. You can use your pre-existing tags or tag resources
using Resource Tagger. For details, see [Accelerate Resource Tagger](acc-resource-tagger.md "acc-resource-tagger.md")).
Configuration for resources with tags take precedence over the default action for the finding. When a resource has multiple tags with different
associated configurations, AMS can't run customized remediations. Instead, AMS sends you an outbound Service Request to inform you of the situation. For example, for the
[s3-bucket-server-side-encryption-enabled](../../../config/latest/developerguide/s3-bucket-server-side-encryption-enabled.md "../../../config/latest/developerguide/s3-bucket-server-side-encryption-enabled.md") finding you can:

- Change the response to 'remediate' unencrypted S3 buckets with the tag key value pair "Regulated: True"
- Change the response to 'no action' when unencrypted S3 buckets has the tags "Regulated: False", and
- Change the default response of unencrypted S3 buckets to be 'ask for approval. This applies for all S3 buckets that don’t have the tags
  "Regulated: True" or "Regulated: False"

You can also add the input required to run custom finding response. For example, for
remediations that require an encryption key, you can provide your key IDs to AMS. You can change the input parameters
of the remediation runbooks, but AMS doesn't support integration with custom runbooks. For a description of AMS remediation
runbooks in the Config Report, see [AWS Config Control Compliance report](acc-report-config-control-compliance.md "acc-report-config-control-compliance.md").
