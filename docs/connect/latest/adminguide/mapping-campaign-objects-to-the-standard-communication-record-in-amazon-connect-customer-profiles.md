# Mapping Campaign objects to the standard communication record in Amazon

Connect Customer Profiles

This topic lists which fields in Campaign objects map to fields in the
standard communication record object in Customer Profiles.

## Campaign-Email object

For a list of all the fields in a Campaign-Email object see the
[Email object](../../../ses/latest/dg/event-publishing-retrieving-sns-contents.md "../../../ses/latest/dg/event-publishing-retrieving-sns-contents.md")in the Amazon SES documentation.

**Mapping a Campaign-Email object to a standard
communication record**

A subset of the fields in the Campaign-Email object map to the
standard communication record object in Customer Profiles.

The following table lists which fields can be mapped from the
Campaign-Email object to the standard communication record.

| Campaign-Email source field           | Standard communication record target field        |
| ------------------------------------- | ------------------------------------------------- |
| campaign_event_id                     | Attributes.LastCampaignEventId                    |
| outbound_request_id                   | Attributes.OutboundCampaignRequestId              |
| campaign_message_id                   | Attributes.CampaignMessageId                      |
| channel.name                          | Channel                                           |
| channel.subtype                       | Attributes.ChannelSubType                         |
| endpoint_address                      | Endpoint.EndpointAddress                          |
| endpoint_type                         | Endpoint.EndpointType                             |
| instance_arn                          | ConnectInstanceArn                                |
| campaign_name                         | Campaign.CampaignName                             |
| campaign_id                           | Campaign.CampaignId                               |
| campaign_run_id                       | Campaign.CampaignRunId                            |
| campaign_activity_id                  | Campaign.CampaignActivityId                       |
| segment_arn                           | Campaign.SegmentArn                               |
| outbound_request_creation_timestamp   | CreatedDate                                       |
| campaign_event_timestamp              | UpdatedDate                                       |
| campaign_event_type                   | LastEventType                                     |
| campaign_event_timestamp              | Events.{{campaign\_event\_type}}.UpdatedDate      |
| campaign_event_id                     | Events.{{campaign\_event\_type}}.EventId          |
| campaign_event_type                   | Events.{{campaign\_event\_type}}.EventType        |
| email.bounce.bounceType               | Events.Bounce.Attributes.BounceType               |
| email.bounce.bounceSubType            | Events.Bounce.Attributes.BounceSubType            |
| email.click.link                      | Events.Click.Attributes.Link                      |
| email.click.ipAddress                 | Events.Click.Attributes.IpAddress                 |
| email.open.ipAddress                  | Events.Open.Attributes.IpAddress                  |
| email.reject.reason                   | Events.Reject.Attributes.Reason                   |
| email.renderingFailure.templateName   | Events.RenderingFailure.Attributes.TemplateName   |
| email.renderingFailure.errorMessage   | Events.RenderingFailure.Attributes.ErrorMessage   |
| email.deliveryDelay.delayType         | Events.DeliveryDelay.Attributes.DelayType         |
| email.complaint.complaintFeedbackType | Events.Complaint.Attributes.ComplaintFeedbackType |
| email.complaint.complaintSubType      | Events.Complaint.Attributes.ComplaintSubType      |
| email.mail.commonHeaders.subject      | Attributes.Subject                                |

## Campaign-SMS object

For a list of all the fields in a Campaign-SMS object see The [SMS object](../../../sms-voice/latest/userguide/configuration-sets-event-format.md "../../../sms-voice/latest/userguide/configuration-sets-event-format.md") in the AWS End User Messaging SMS
documentation.

**Mapping a Campaign-SMS object to a standard
communication record**

A subset of the fields in the Campaign-SMS object map to the standard
communication record object in Customer Profiles.

The following table lists which fields can be mapped from the
Campaign-SMS object to the standard communication record.

| Campaign-SMS source field           | Standard communication record target field                           |
| ----------------------------------- | -------------------------------------------------------------------- |
| campaign_event_id                   | Attributes.LastCampaignEventId                                       |
| outbound_request_id                 | Attributes.OutboundCampaignRequestId                                 |
| campaign_message_id                 | Attributes.CampaignMessageId                                         |
| channel.name                        | Channel                                                              |
| channel.subtype                     | Attributes.ChannelSubType                                            |
| endpoint_address                    | Endpoint.EndpointAddress                                             |
| endpoint_type                       | Endpoint.EndpointType                                                |
| instance_arn                        | ConnectInstanceArn                                                   |
| campaign_name                       | Campaign.CampaignName                                                |
| campaign.campaign_id                | Campaign.CampaignId                                                  |
| campaign.campaign_run_id            | Campaign.CampaignRunId                                               |
| campaign_activity_id                | Campaign.CampaignActivityId                                          |
| segment_arn                         | Campaign.SegmentArn                                                  |
| outbound_request_creation_timestamp | CreatedDate                                                          |
| campaign_event_timestamp            | UpdatedDate                                                          |
| campaign_event_type                 | LastEventType                                                        |
| campaign_event_timestamp            | Events.{{campaign\_event\_type}}.UpdatedDate                         |
| campaign_event_id                   | Events.{{campaign\_event\_type}}.EventId                             |
| campaign_event_type                 | Events.{{campaign\_event\_type}}.EventType                           |
| sms.messageType                     | Events.{{campaign\_event\_type}}.Attributes.MessageType              |
| sms.messageStatus                   | Events.{{campaign\_event\_type}}.Attributes.MessageStatus            |
| sms.messageStatusDescription        | Events.{{campaign\_event\_type}}.Attributes.MessageStatusDescription |
| sms.totalMessagePrice               | Events.{{campaign\_event\_type}}.Attributes.TotalMessagePrice        |
| sms.totalCarrierFee                 | Events.{{campaign\_event\_type}}.Attributes.TotalCarrierFee          |
| sms.isoCountryCode                  | Events.{{campaign\_event\_type}}.Attributes.IsoCountryCode           |

## Campaign-Telephony

object

For a list of all the fields in a Campaign-Telephony object, see the
[Voice object](../../../sms-voice/latest/userguide/configuration-sets-event-format.md "../../../sms-voice/latest/userguide/configuration-sets-event-format.md") in the AWS End User Messaging SMS
documentation.

**Mapping a Campaign-Telephony object to a
standard communication record**

A subset of the fields in the Campaign-Telephony object map to the
standard communication record object in Customer Profiles.

The following table lists which fields can be mapped from the
Campaign-Telephony object to the standard communication record.

| Campaign-Telephony source field                  | Standard communication record target field                                  |
| ------------------------------------------------ | --------------------------------------------------------------------------- |
| campaign_event_id                                | Attributes.LastCampaignEventId                                              |
| outbound_request_id                              | Attributes.OutboundCampaignRequestId                                        |
| campaign_message_id                              | Attributes.CampaignMessageId                                                |
| channel.name                                     | Channel                                                                     |
| channel.subtype                                  | Attributes.ChannelSubType                                                   |
| endpoint.endpoint_address                        | Endpoint.EndpointAddress                                                    |
| endpoint.endpoint_type                           | Endpoint.EndpointType                                                       |
| instance_arn                                     | ConnectInstanceArn                                                          |
| campaign.campaign_name                           | Campaign.CampaignName                                                       |
| campaign.campaign_id                             | Campaign.CampaignId                                                         |
| campaign.campaign_run_id                         | Campaign.CampaignRunId                                                      |
| campaign.campaign_activity_id                    | Campaign.CampaignActivityId                                                 |
| campaign.segment_arn                             | Campaign.SegmentArn                                                         |
| outbound_request_creation_timestamp              | CreatedDate                                                                 |
| campaign_event_timestamp                         | UpdatedDate                                                                 |
| campaign_event_type                              | LastEventType                                                               |
| campaign_event_timestamp                         | Events.{{campaign\_event\_type}}.UpdatedDate                                |
| campaign_event_id                                | Events.{{campaign\_event\_type}}.EventId                                    |
| campaign_event_type                              | Events.{{campaign\_event\_type}}.EventType                                  |
| voice.agentInfo.connectedToAgentTimestamp        | Events.{{campaign\_event\_type}}.Attributes.ConnectedToAgentTimestamp       |
| voice.customerVoiceActivity.greetingEndTimestamp | Events.{{campaign\_event\_type}}.Attributes.GreetingEndTimestamp            |
| voice.answeringMachineDetectionStatus            | Events.{{campaign\_event\_type}}.Attributes.AnsweringMachineDetectionStatus |
| campaign_event_timestamp                         | SourceLastUpdatedTimestamp                                                  |

## Campaign-Orchestration

object

**Mapping a Campaign-Orchestration object to a
standard communication record**

A subset of the fields in the Campaign-Orchestration object map to the
standard communication record object in Customer Profiles.

The following table lists which fields can be mapped from the
Campaign-Orchestration object to the standard communication
record.

| Campaign-Orchestration source field | Standard communication record target field   |
| ----------------------------------- | -------------------------------------------- |
| campaign_event_id                   | Attributes.LastCampaignEventId               |
| channel.name                        | Channel                                      |
| channel.subtype                     | Attributes.ChannelSubType                    |
| instance_arn                        | ConnectInstanceArn                           |
| campaign.campaign_name              | Campaign.CampaignName                        |
| campaign.campaign_id                | Campaign.CampaignId                          |
| campaign.campaign_run_id            | Campaign.CampaignRunId                       |
| campaign.campaign_activity_id       | Campaign.CampaignActivityId                  |
| campaign.segment_arn                | Campaign.SegmentArn                          |
| campaign_event_timestamp            | UpdatedDate                                  |
| campaign_event_type                 | LastEventType                                |
| campaign_event_timestamp            | Events.{{campaign\_event\_type}}.UpdatedDate |
| campaign_event_id                   | Events.{{campaign\_event\_type}}.EventId     |
| campaign_event_type                 | Events.{{campaign\_event\_type}}.EventType   |
| campaign_event_timestamp            | SourceLastUpdatedTimestamp                   |

## Example

The following example shows how to map a source field to a target
field:

```
"channel": {
    "source": "_source.engagement.channel.name",
    "target": "_communicationRecord.Channel"
}
```
