

# Mapping Campaign objects to the standard communication record in Amazon Connect Customer Profiles
<a name="mapping-campaign-objects-to-the-standard-communication-record-in-amazon-connect-customer-profiles"></a>

 This topic lists which fields in Campaign objects map to fields in the standard communication record object in Customer Profiles. 

## Campaign-Email object
<a name="campaign-email-object"></a>

 For a list of all the fields in a Campaign-Email object see the [Email object ](https://docs.aws.amazon.com/ses/latest/dg/event-publishing-retrieving-sns-contents.html)in the Amazon SES documentation. 

**Mapping a Campaign-Email object to a standard communication record**

 A subset of the fields in the Campaign-Email object map to the standard communication record object in Customer Profiles. 

 The following table lists which fields can be mapped from the Campaign-Email object to the standard communication record. 


|  Campaign-Email source field  |  Standard communication record target field  | 
| --- | --- | 
|  campaign\_event\_id  |  Attributes.LastCampaignEventId  | 
|  outbound\_request\_id  |  Attributes.OutboundCampaignRequestId  | 
|  campaign\_message\_id  |  Attributes.CampaignMessageId  | 
| channel.name  |  Channel  | 
|  channel.subtype  |  Attributes.ChannelSubType  | 
|  endpoint\_address  |  Endpoint.EndpointAddress  | 
|  endpoint\_type  |  Endpoint.EndpointType  | 
|  instance\_arn  |  ConnectInstanceArn  | 
|  campaign\_name  |  Campaign.CampaignName  | 
|  campaign\_id  |  Campaign.CampaignId  | 
|  campaign\_run\_id  |  Campaign.CampaignRunId  | 
|  campaign\_activity\_id  |  Campaign.CampaignActivityId  | 
|  segment\_arn  |  Campaign.SegmentArn  | 
|  outbound\_request\_creation\_timestamp  |  CreatedDate  | 
|  campaign\_event\_timestamp  |  UpdatedDate  | 
|  campaign\_event\_type  |  LastEventType  | 
|  campaign\_event\_timestamp  |  Events.{{campaign\_event\_type}}.UpdatedDate  | 
|  campaign\_event\_id  |  Events.{{campaign\_event\_type}}.EventId  | 
|  campaign\_event\_type  |  Events.{{campaign\_event\_type}}.EventType  | 
|  email.bounce.bounceType  |  Events.Bounce.Attributes.BounceType  | 
|  email.bounce.bounceSubType  |  Events.Bounce.Attributes.BounceSubType  | 
|  email.choose.link  |  Events.Choose.Attributes.Link  | 
|  email.choose.ipAddress  |  Events.Choose.Attributes.IpAddress  | 
|  email.open.ipAddress  |  Events.Open.Attributes.IpAddress  | 
|  email.reject.reason  |  Events.Reject.Attributes.Reason  | 
|  email.renderingFailure.templateName  |  Events.RenderingFailure.Attributes.TemplateName  | 
|  email.renderingFailure.errorMessage  |  Events.RenderingFailure.Attributes.ErrorMessage  | 
|  email.deliveryDelay.delayType  |  Events.DeliveryDelay.Attributes.DelayType  | 
|  email.complaint.complaintFeedbackType  |  Events.Complaint.Attributes.ComplaintFeedbackType  | 
|  email.complaint.complaintSubType  |  Events.Complaint.Attributes.ComplaintSubType  | 
|  email.mail.commonHeaders.subject  |  Attributes.Subject  | 

## Campaign-SMS object
<a name="campaign-sms-object"></a>

 For a list of all the fields in a Campaign-SMS object see The [SMS object](https://docs.aws.amazon.com/sms-voice/latest/userguide/configuration-sets-event-format.html) in the AWS End User Messaging SMS documentation. 

**Mapping a Campaign-SMS object to a standard communication record**

 A subset of the fields in the Campaign-SMS object map to the standard communication record object in Customer Profiles. 

 The following table lists which fields can be mapped from the Campaign-SMS object to the standard communication record. 


|  Campaign-SMS source field  |  Standard communication record target field  | 
| --- | --- | 
|  campaign\_event\_id  |  Attributes.LastCampaignEventId  | 
|  outbound\_request\_id  |  Attributes.OutboundCampaignRequestId  | 
|  campaign\_message\_id  |  Attributes.CampaignMessageId  | 
| channel.name  |  Channel  | 
|  channel.subtype  |  Attributes.ChannelSubType  | 
|  endpoint\_address  |  Endpoint.EndpointAddress  | 
|  endpoint\_type  |  Endpoint.EndpointType  | 
|  instance\_arn  |  ConnectInstanceArn  | 
|  campaign\_name  |  Campaign.CampaignName  | 
|  campaign.campaign\_id  |  Campaign.CampaignId  | 
|  campaign.campaign\_run\_id  |  Campaign.CampaignRunId  | 
|  campaign\_activity\_id  |  Campaign.CampaignActivityId  | 
|  segment\_arn  |  Campaign.SegmentArn  | 
|  outbound\_request\_creation\_timestamp  |  CreatedDate  | 
|  campaign\_event\_timestamp  |  UpdatedDate  | 
|  campaign\_event\_type  |  LastEventType  | 
|  campaign\_event\_timestamp  |  Events.{{campaign\_event\_type}}.UpdatedDate  | 
|  campaign\_event\_id  |  Events.{{campaign\_event\_type}}.EventId  | 
|  campaign\_event\_type  |  Events.{{campaign\_event\_type}}.EventType  | 
|  sms.messageType  |  Events.{{campaign\_event\_type}}.Attributes.MessageType  | 
|  sms.messageStatus  |  Events.{{campaign\_event\_type}}.Attributes.MessageStatus  | 
|  sms.messageStatusDescription  |  Events.{{campaign\_event\_type}}.Attributes.MessageStatusDescription  | 
|  sms.totalMessagePrice  |  Events.{{campaign\_event\_type}}.Attributes.TotalMessagePrice  | 
|  sms.totalCarrierFee  |  Events.{{campaign\_event\_type}}.Attributes.TotalCarrierFee  | 
|  sms.isoCountryCode  |  Events.{{campaign\_event\_type}}.Attributes.IsoCountryCode  | 

## Campaign-Telephony object
<a name="campaign-telephony-object"></a>

For a list of all the fields in a Campaign-Telephony object, see the [Voice object](https://docs.aws.amazon.com/sms-voice/latest/userguide/configuration-sets-event-format.html) in the AWS End User Messaging SMS documentation.

**Mapping a Campaign-Telephony object to a standard communication record**

A subset of the fields in the Campaign-Telephony object map to the standard communication record object in Customer Profiles.

The following table lists which fields can be mapped from the Campaign-Telephony object to the standard communication record.


| Campaign-Telephony source field | Standard communication record target field | 
| --- | --- | 
| campaign\_event\_id | Attributes.LastCampaignEventId | 
| outbound\_request\_id | Attributes.OutboundCampaignRequestId | 
| campaign\_message\_id | Attributes.CampaignMessageId | 
| channel.name | Channel | 
| channel.subtype | Attributes.ChannelSubType | 
| endpoint.endpoint\_address | Endpoint.EndpointAddress | 
| endpoint.endpoint\_type | Endpoint.EndpointType | 
| instance\_arn | ConnectInstanceArn | 
| campaign.campaign\_name | Campaign.CampaignName | 
| campaign.campaign\_id | Campaign.CampaignId | 
| campaign.campaign\_run\_id | Campaign.CampaignRunId | 
| campaign.campaign\_activity\_id | Campaign.CampaignActivityId | 
| campaign.segment\_arn | Campaign.SegmentArn | 
| outbound\_request\_creation\_timestamp | CreatedDate | 
| campaign\_event\_timestamp | UpdatedDate | 
| campaign\_event\_type | LastEventType | 
| campaign\_event\_timestamp | Events.{{campaign\_event\_type}}.UpdatedDate | 
| campaign\_event\_id | Events.{{campaign\_event\_type}}.EventId | 
| campaign\_event\_type | Events.{{campaign\_event\_type}}.EventType | 
| voice.agentInfo.connectedToAgentTimestamp | Events.{{campaign\_event\_type}}.Attributes.ConnectedToAgentTimestamp | 
| voice.customerVoiceActivity.greetingEndTimestamp | Events.{{campaign\_event\_type}}.Attributes.GreetingEndTimestamp | 
| voice.answeringMachineDetectionStatus | Events.{{campaign\_event\_type}}.Attributes.AnsweringMachineDetectionStatus | 
| campaign\_event\_timestamp | SourceLastUpdatedTimestamp | 

## Campaign-WhatsApp object
<a name="campaign-whatsapp-object"></a>

**Mapping a Campaign-WhatsApp object to a standard communication record**

A subset of the fields in the Campaign-WhatsApp object map to the standard communication record object in Customer Profiles.

The following table lists which fields can be mapped from the Campaign-WhatsApp object to the standard communication record.


| Campaign-WhatsApp source field | Standard communication record target field | 
| --- | --- | 
| campaign\_event\_id | Attributes.LastCampaignEventId | 
| engagement.outbound\_request\_id | Attributes.OutboundCampaignRequestId | 
| campaign\_message\_id | Attributes.CampaignMessageId | 
| engagement.channel.name | Channel | 
| engagement.channel.subtype | Attributes.ChannelSubType | 
| engagement.endpoint.endpoint\_address | Endpoint.EndpointAddress | 
| engagement.endpoint.endpoint\_type | Endpoint.EndpointType | 
| instance\_arn | ConnectInstanceArn | 
| campaign.campaign\_name | Campaign.CampaignName | 
| campaign.campaign\_id | Campaign.CampaignId | 
| campaign.campaign\_run\_id | Campaign.CampaignRunId | 
| campaign.campaign\_activity\_id | Campaign.CampaignActivityId | 
| campaign.segment\_arn | Campaign.SegmentArn | 
| engagement.outbound\_request\_creation\_timestamp | CreatedDate | 
| campaign\_event\_timestamp | UpdatedDate | 
| campaign\_event\_type | LastEventType | 
| campaign\_event\_timestamp | Events.{{campaign\_event\_type}}.UpdatedDate | 
| campaign\_event\_id | Events.{{campaign\_event\_type}}.EventId | 
| campaign\_event\_type | Events.{{campaign\_event\_type}}.EventType | 
| engagement.engagement\_details.whatsapp.errors[].code | Events.{{campaign\_event\_type}}.Errors[].Code | 
| engagement.engagement\_details.whatsapp.errors[].message | Events.{{campaign\_event\_type}}.Errors[].Message | 
| campaign\_event\_timestamp | SourceLastUpdatedTimestamp | 

## Campaign-WebNotification object
<a name="campaign-webnotification-object"></a>

**Mapping a Campaign-WebNotification object to a standard communication record**

A subset of the fields in the Campaign-WebNotification object map to the standard communication record object in Customer Profiles.

The following table lists which fields can be mapped from the Campaign-WebNotification object to the standard communication record.


| Campaign-WebNotification source field | Standard communication record target field | 
| --- | --- | 
| campaign\_event\_id | Attributes.LastCampaignEventId | 
| engagement.outbound\_request\_id | Attributes.OutboundCampaignRequestId | 
| campaign\_message\_id | Attributes.CampaignMessageId | 
| engagement.channel.name | Channel | 
| engagement.channel.subtype | Attributes.ChannelSubType | 
| engagement.endpoint.endpoint\_address | Endpoint.EndpointAddress | 
| engagement.endpoint.endpoint\_type | Endpoint.EndpointType | 
| instance\_arn | ConnectInstanceArn | 
| campaign.campaign\_name | Campaign.CampaignName | 
| campaign.campaign\_id | Campaign.CampaignId | 
| campaign.campaign\_run\_id | Campaign.CampaignRunId | 
| campaign.campaign\_activity\_id | Campaign.CampaignActivityId | 
| campaign.segment\_arn | Campaign.SegmentArn | 
| engagement.outbound\_request\_creation\_timestamp | CreatedDate | 
| campaign\_event\_timestamp | UpdatedDate | 
| campaign\_event\_type | LastEventType | 
| campaign\_event\_timestamp | Events.{{campaign\_event\_type}}.UpdatedDate | 
| campaign\_event\_id | Events.{{campaign\_event\_type}}.EventId | 
| campaign\_event\_type | Events.{{campaign\_event\_type}}.EventType | 
| engagement.engagement\_details.webNotification.eventType | Events.{{campaign\_event\_type}}.Attributes.WebNotificationEventType | 
| engagement.engagement\_details.webNotification.notificationType | Events.{{campaign\_event\_type}}.Attributes.NotificationType | 
| engagement.engagement\_details.webNotification.deviceType | Events.{{campaign\_event\_type}}.Attributes.DeviceType | 
| engagement.engagement\_details.webNotification.deviceModel | Events.{{campaign\_event\_type}}.Attributes.DeviceModel | 
| engagement.engagement\_details.webNotification.browserName | Events.{{campaign\_event\_type}}.Attributes.BrowserName | 
| campaign\_event\_timestamp | SourceLastUpdatedTimestamp | 

## Campaign-Orchestration object
<a name="campaign-orchestration-object"></a>

**Mapping a Campaign-Orchestration object to a standard communication record**

A subset of the fields in the Campaign-Orchestration object map to the standard communication record object in Customer Profiles.

The following table lists which fields can be mapped from the Campaign-Orchestration object to the standard communication record.


| Campaign-Orchestration source field | Standard communication record target field | 
| --- | --- | 
| campaign\_event\_id | Attributes.LastCampaignEventId | 
| channel.name | Channel | 
| channel.subtype | Attributes.ChannelSubType | 
| instance\_arn | ConnectInstanceArn | 
| campaign.campaign\_name | Campaign.CampaignName | 
| campaign.campaign\_id | Campaign.CampaignId | 
| campaign.campaign\_run\_id | Campaign.CampaignRunId | 
| campaign.campaign\_activity\_id | Campaign.CampaignActivityId | 
| campaign.segment\_arn | Campaign.SegmentArn | 
| campaign\_event\_timestamp | UpdatedDate | 
| campaign\_event\_type | LastEventType | 
| campaign\_event\_timestamp | Events.{{campaign\_event\_type}}.UpdatedDate | 
| campaign\_event\_id | Events.{{campaign\_event\_type}}.EventId | 
| campaign\_event\_type | Events.{{campaign\_event\_type}}.EventType | 
| campaign\_event\_timestamp | SourceLastUpdatedTimestamp | 

## Example
<a name="example"></a>

 The following example shows how to map a source field to a target field: 

```
"channel": {
    "source": "_source.engagement.channel.name",
    "target": "_communicationRecord.Channel"
}
```