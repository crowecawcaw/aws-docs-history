**End of support notice:** On October
30, 2026, AWS will end support for Amazon Pinpoint. After October 30, 2026, you will no
longer be able to access the Amazon Pinpoint console or Amazon Pinpoint resources (endpoints,
segments, campaigns, journeys, and analytics). For more information, see [Amazon Pinpoint end of
support](../../../console/pinpoint/migration-guide.md "../../../console/pinpoint/migration-guide.md"). **Note:** APIs related to SMS, voice,
mobile push, OTP, and phone number validate are not impacted by this change and are
supported by AWS End User Messaging.

# Troubleshooting campaigns

Verify that logging is turned on to assist in identifying the cause of failure. For more information, see [Monitoring and logging](troubleshooting.md#troubleshooting-logging "troubleshooting.md#troubleshooting-logging") and [Campaign events](../developerguide/event-streams-data-campaign.md "../developerguide/event-streams-data-campaign.md").

## Some endpoints were not

processed or targeted successfully by the campaign

**Endpoints targeted**: The total number of endpoints that
will be targeted when the campaign runs for the chosen channel. This total excludes
duplicate or inactive endpoints from the segment.

**Endpoints processed**: The total number of endpoints that were successfully
targeted by the campaign run.

For **dynamic segments**, the endpoint count can change over time based on the criteria
defined for the audience therefore the number of endpoints per channel is only an
estimate. You may export the segment to get the total number of endpoints at any given
time.

- Throttling based on delivery channel constraints
- If you schedule the campaign to use recipient's local time (isLocalTime is set to true)
- If the campaign does not have sufficient time configured to process all endpoints
- Downstream delivery issues or rendering issues
- Permanent failure

### Throttling

- Review the Amazon CloudWatch metric `CampaignSendMessageThrottled`
  during the time frame that the campaign ran to confirm whether this is
  the issue. For more information, see [View Amazon Pinpoint metrics in CloudWatch](monitoring-view-metrics.md "monitoring-view-metrics.md").
- Throttling occurs when the endpoint delivery rate capability is exceeded. For more
  information, see Amazon Pinpoint [quotas](../developerguide/quotas.md "../developerguide/quotas.md").

### Using recipients timezone

When a campaign is scheduled to use a recipients’ local time ([isLocalTime](../apireference/apps-application-id-campaigns.md "../apireference/apps-application-id-campaigns.md") set to
true) for the Campaign, all endpoints must have a `Demographic.Timezone` attribute
value formatted correctly in the endpoint definition, else the endpoint will not be
targetedsuccessfully. This is because the [isLocalTime](../apireference/apps-application-id-campaigns.md "../apireference/apps-application-id-campaigns.md") option bases the
delivery time on each recipient's local time zone.

### Processing time

- When a campaign doesn't have sufficient time to process all targeted endpoints, the
  endpoints aren't processed and logs show a `campaign_send_status` of
  [`EXPIRED`](../developerguide/event-streams-data-campaign.md#event-streams-data-campaign-attributes-attrs "../developerguide/event-streams-data-campaign.md#event-streams-data-campaign-attributes-attrs").
- Based on the number of endpoints being targeted by your campaign, verify that the
  **Maximum amount of time for a campaign run** and
  **Maximum number of messages per second** is
  configured based on your use case and delivery channel. For more
  information, see [Editing a project's default settings](projects-manage-edit.md "projects-manage-edit.md").

### Delivery, render or permanent failure

- Delivery issues can occur when reaching the different endpoint types.
  Verify that logging is enabled to assist in identifying the cause of the
  failure. To troubleshoot downstream delivery issues further, see the
  delivery issues associated with the corresponding endpoint type [Troubleshooting the email channel](channels-email-troubleshooting.md "channels-email-troubleshooting.md"), [Troubleshooting the SMS channel](channels-sms-troubleshooting.md "channels-sms-troubleshooting.md"), [Troubleshooting the voice channel](channels-voice-troubleshooting.md "channels-voice-troubleshooting.md"), and [Troubleshooting the push channel](channels-push-troubleshooting.md "channels-push-troubleshooting.md").
- Rendering issues occur for the following reasons: when a message template
  is used and template data is missing, template data is incorrectly
  formatted, or there's a mismatch between the template parameters and
  endpoint data. For more information, see the email section under delivery
  issues.
- Permanent failures occur when the endpoint address might not be reached by Amazon Pinpoint. The
  reason for the permanent error is displayed in the logs. Permanent
  failures are not retried. Examples of permanent failures can include
  invalid address, such as an email address or a phone number, as well as
  permission issues, account in a sandbox, or insufficient quota.
