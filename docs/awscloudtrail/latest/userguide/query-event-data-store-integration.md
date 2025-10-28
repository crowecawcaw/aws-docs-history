# Create an integration with an event

source outside of AWS

You can use CloudTrail to log and store user activity data from any source in your hybrid
environments, such as in-house or SaaS applications hosted on-premises or in the cloud,
virtual machines, or containers. You can store, access, analyze, troubleshoot and take
action on this data without maintaining multiple log aggregators and reporting tools.

Activity events from non-AWS sources work by using _channels_ to
bring events into CloudTrail Lake from external partners that work with CloudTrail, or from your own
sources. When you create a channel, you choose one or more event data stores to store
events that arrive from the channel source. You can change the destination event data
stores for a channel as needed, as long as the destination event data stores are set to
log `eventCategory="ActivityAuditLog"` events. When you create a channel for
events from an external partner, you provide a channel ARN to the partner or
source application. The resource policy attached to the channel allows
the source to transmit events through the channel. If a channel does not have a resource policy,
only the channel owner can call the `PutAuditEvents` API on the channel.

CloudTrail has partnered with many event source providers, such as Okta and LaunchDarkly.
When you create an integration with an event source outside AWS, you can
choose one of these partners as your event source, or choose **My custom
integration** to integrate events from your own sources into CloudTrail.
A maximum of one channel is allowed per source.

There are two types of integrations: direct and
solution. With direct integrations, the partner calls the `PutAuditEvents`
API to deliver events to the event data store for your AWS account. With solution
integrations, the application runs in your AWS account and the application calls the
`PutAuditEvents` API to deliver events to the event data store for your
AWS account.

From the **Integrations** page, you can choose the **Available
sources** tab to the view the **Integration type**
for partners.

![Partner integration type](images/partner-integration-type.png)
To get started, create an integration to log events from partner or other application
sources using the CloudTrail console.

###### Topics

- [Create an integration with a CloudTrail partner with the console](query-event-data-store-integration-partner.md "query-event-data-store-integration-partner.md")
- [Create a custom integration with the console](query-event-data-store-integration-custom.md "query-event-data-store-integration-custom.md")
- [Create, update, and manage CloudTrail Lake integrations with the AWS CLI](lake-integrations-cli.md "lake-integrations-cli.md")
- [Additional information about integration partners](#cloudtrail-lake-partner-information "#cloudtrail-lake-partner-information")
- [CloudTrail Lake integrations event
  schema](query-integration-event-schema.md "query-integration-event-schema.md")

## Additional information about integration partners

The table in this section provides the source name for each integration partner and identifies the integration type (direct or solution).

The information in the **Source name** column is required when calling the `CreateChannel` API.
You specify the source name as the value for the `Source` parameter.

| Partner name (console)    | Source name (API)             | Integration type |
| ------------------------- | ----------------------------- | ---------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| My custom integration     | `Custom`                      | solution         |
| Cloud Storage Security    | `CloudStorageSecurityConsole` | solution         |
| Clumio                    | `Clumio`                      | direct           |
| CrowdStrike               | `CrowdStrike`                 | solution         |
| CyberArk                  | `CyberArk`                    | solution         |
| GitHub                    | `GitHub`                      | solution         |
| Kong Inc                  | `KongGatewayEnterprise`       | solution         |
| LaunchDarkly              | `LaunchDarkly`                | direct           |
| Netskope                  | `NetskopeCloudExchange`       | solution         |
| Nordcloud, an IBM Company | `IBMMulticloud`               | direct           |
| MontyCloud                | `MontyCloud`                  | direct           |
| Okta                      | `OktaSystemLogEvents`         | solution         |
| One Identity              | `OneLogin`                    | solution         |
| Shoreline.io              | `Shoreline`                   | solution         |
| Snyk.io                   | `Snyk`                        | direct           |
| Wiz                       | `WizAuditLogs`                | solution         | ### View partner documentation You can learn more about a partner's integration with CloudTrail Lake by viewing their documentation. **To view partner documentation** 1. Sign in to the AWS Management Console and open the CloudTrail console at [https://console.aws.amazon.com/cloudtrail/](https://console.aws.amazon.com/cloudtrail/ "https://console.aws.amazon.com/cloudtrail/"). 2. From the navigation pane, under **Lake**, choose **Integrations**. 3. From the **Integrations** page, choose **Available sources**, then choose **Learn more** for the partner whose documentation you want to view. |
