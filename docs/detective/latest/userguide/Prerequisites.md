# Before you begin integrating Detective with Security Lake

This topic describes the preliminary steps such as delegating a Security Lake administrator for your organization, enabling Security Lake for your Detective administrator account, and verifying that Security Lake is collecting logs and events.

Security Lake integrates with AWS Organizations to manage log collection across multiple accounts in an
organization. To use Security Lake for an organization, your AWS Organizations management account must
first designate a delegated Security Lake administrator for your organization. The delegated Security Lake
administrator must then enable Security Lake, and enable log and event collection for member
accounts in the organization.

Before you integrate Security Lake with Detective, make sure that Security Lake is enabled for the Detective administrator account. You must first configure your data lake settings and set up log collection by enabling Security Lake using the Security Lake console. For the detailed steps on how to enable Security Lake, see [Getting Started](../../../security-lake/latest/userguide/getting-started.md "../../../security-lake/latest/userguide/getting-started.md") in the Amazon Security Lake User Guide.

Also, verify that Security Lake is collecting logs and events from AWS CloudTrail management events and Amazon Virtual Private Cloud (Amazon VPC) Flow Logs. For more details about log collection in Security Lake, see [Collecting data from AWS services](../../../security-lake/latest/userguide/internal-sources.md#cloudtrail-event-logs "../../../security-lake/latest/userguide/internal-sources.md#cloudtrail-event-logs") in the Amazon Security Lake User Guide.
