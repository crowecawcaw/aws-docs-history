**End of support notice:** On October
30, 2026, AWS will end support for Amazon Pinpoint. After October 30, 2026, you will no
longer be able to access the Amazon Pinpoint console or Amazon Pinpoint resources (endpoints,
segments, campaigns, journeys, and analytics). For more information, see [Amazon Pinpoint end of
support](../../../console/pinpoint/migration-guide.md "../../../console/pinpoint/migration-guide.md"). **Note:** APIs related to SMS, voice,
mobile push, OTP, and phone number validate are not impacted by this change and are
supported by AWS End User Messaging.

# Troubleshooting

###### Note

The following troubleshooting topics have been moved:

- [Troubleshooting segments](segments-troubleshooting.md "segments-troubleshooting.md")
- [Troubleshooting campaigns](campaigns-troubleshooting.md "campaigns-troubleshooting.md")
- [Troubleshooting journeys](journeys-troubleshooting.md "journeys-troubleshooting.md")
- [Troubleshooting the SMS channel](channels-sms-troubleshooting.md "channels-sms-troubleshooting.md")
- [Troubleshooting the voice channel](channels-voice-troubleshooting.md "channels-voice-troubleshooting.md")
- [Troubleshooting the push channel](channels-push-troubleshooting.md "channels-push-troubleshooting.md")
- [Troubleshooting the email channel](channels-email-troubleshooting.md "channels-email-troubleshooting.md")
  Become familiar with troubleshooting information and possible solutions to help resolve
  issues when using Amazon Pinpoint.

**Monitoring and logging**

As a best practice, consider logging events in Amazon Pinpoint by:

- Turning on Events Streams through Amazon Kinesis Data Streams following the instructions in
  [Streaming events with Amazon Pinpoint](analytics-streaming.md "analytics-streaming.md").
- Using a custom logging solution. For more information, see [Digital User Engagement Events Database](https://aws.amazon.com/solutions/implementations/digital-user-engagement-events-database/ "https://aws.amazon.com/solutions/implementations/digital-user-engagement-events-database/"). Multiple services are
  involved and additional costs are incurred.
- Using Amazon CloudWatch metrics supported by Amazon Pinpoint. For more information, see
  [Monitoring Amazon Pinpoint with Amazon CloudWatch](monitoring.md "monitoring.md").
- Using Amazon Pinpoint API calls logged in CloudTrail. For more information, see [Logging
  Amazon Pinpoint API calls with AWS CloudTrail](../developerguide/logging-using-cloudtrail.md "../developerguide/logging-using-cloudtrail.md") in the
  _Amazon Pinpoint Developer Guide_.

###### Topics

- [CLI examples of common tasks](#troubleshooting-cli-examples "#troubleshooting-cli-examples")

## CLI examples of common tasks

The following examples are common CLI commands for Amazon Pinpoint.

- Get Endpoint Data: [get-endpoint](../../../cli/latest/reference/pinpoint/get-endpoint.md "../../../cli/latest/reference/pinpoint/get-endpoint.md") CLI

```
aws pinpoint get-endpoint —application-id `AppId` —endpoint-id `EndpointId`
```

###### In the preceding command, make the following changes:

    + Replace `AppId` with the ID of the Amazon Pinpoint
     project that contains the endpoint.
    + Replace `EndpointId` with the ID of an
     existing endpoint that you're retrieving.

- Get User Data: [get-user-endpoints](../../../cli/latest/reference/pinpoint/get-user-endpoints.md "../../../cli/latest/reference/pinpoint/get-user-endpoints.md") CLI

```
aws pinpoint get-user-endpoints —application-id `AppId` —user-id `UserId`
```

###### In the preceding command, make the following changes:

    + Replace `AppId` with the ID of the Amazon Pinpoint
     project that contains the endpoint.
    + Replace `UserId` with the ID of the
     user.

- Update or Create New Endpoint: [update-endpoint](../../../cli/latest/reference/pinpoint/update-endpoint.md "../../../cli/latest/reference/pinpoint/update-endpoint.md") CLI

```
aws pinpoint update-endpoint —application-id `AppId` —endpoint-id `EndpointId` —endpoint-request '{"ChannelType":"SMS","Address":"+12345678","Location":{"Country":"USA"},"User":{"UserId":"`UserId`"}}'
```

###### In the preceding command, make the following changes:

    + Replace `AppId` with the ID of the Amazon Pinpoint
     project that contains the endpoint.
    + Replace `EndpointId` with the ID of an
     existing endpoint that you're creating or updating.
    + Replace `UserId` with the ID of the
     user.

- Delete Endpoint: [delete-endpoint](../../../cli/latest/reference/pinpoint/delete-endpoint.md "../../../cli/latest/reference/pinpoint/delete-endpoint.md") CLI

```
aws pinpoint delete-endpoint —application-id `AppId` —endpoint-id `EndpointId`
```

###### In the preceding command, make the following changes:

    + Replace `AppId` with the ID of the Amazon Pinpoint
     project that contains the endpoint.
    + Replace `EndpointId` with the ID of an
     existing endpoint that you're deleting.

- Validate a phone number: [phone-number-validate](../../../cli/latest/reference/pinpoint/phone-number-validate.md "../../../cli/latest/reference/pinpoint/phone-number-validate.md") CLI

```
aws pinpoint phone-number-validate —number-validate-request PhoneNumber=`+12065550100`
```

###### In the preceding command, make the following changes:

    + Replace `+12065550100` with the phone number
     that you want to validate.

- [send-messages](../../../cli/latest/reference/pinpoint/send-messages.md "../../../cli/latest/reference/pinpoint/send-messages.md") Examples CLI: SMS to a number

```
aws pinpoint send-messages --application-id `AppID` --message-request '{"MessageConfiguration": {"SMSMessage":{"Body":"This is a test message"}},"Addresses": {"`DestinationPhoneNumber`": {"ChannelType":"SMS"}}}‘
```

###### In the preceding command, make the following changes:

    + Replace `AppId` with the ID of the Amazon Pinpoint
     project that contains the endpoint.
    + Replace `DestinationPhoneNumber` with the
     phone number that you want to send to.

- [send-messages](../../../cli/latest/reference/pinpoint/send-messages.md "../../../cli/latest/reference/pinpoint/send-messages.md") Examples CLI: origination number to SMS

```
aws pinpoint send-messages --application-id `AppID` --message-request '{"MessageConfiguration": {"SMSMessage":{"Body":"hello, how are you?","OriginationNumber": "`OriginPhoneNumber`"}},"Addresses": {"`DestinationPhoneNumber`": {"ChannelType":"SMS"}}}‘
```

###### In the preceding command, make the following changes:

    + Replace `AppId` with the ID of the Amazon Pinpoint
     project that contains the endpoint.
    + Replace `OriginPhoneNumber` with the phone
     number that you want to send the message from.
    + Replace `DestinationPhoneNumber` with the
     phone number that you want to send to.

- [send-messages](../../../cli/latest/reference/pinpoint/send-messages.md "../../../cli/latest/reference/pinpoint/send-messages.md") Examples CLI: SMS to an endpoint

```
aws pinpoint send-messages —application-id `AppID`  —message-request '{"MessageConfiguration": {"SMSMessage":{"Body":"This is a test message"}},"Endpoints": {"`EndPointId`": {}}}'
```

###### In the preceding command, make the following changes:

    + Replace `AppId` with the ID of the Amazon Pinpoint
     project that contains the endpoint.
    + Replace `EndPointId` with the ID of an
     existing endpoint that you're sending to.

- [send-messages](../../../cli/latest/reference/pinpoint/send-messages.md "../../../cli/latest/reference/pinpoint/send-messages.md") Examples CLI: SMS to a userId

```
aws pinpoint send-users-messages —application-id `AppID` —send-users-message-request '{"MessageConfiguration": {"SMSMessage":{"Body":"This is a test"}},"Users": {"`UserId`": {}}}'
```

###### In the preceding command, make the following changes:

    + Replace `AppId` with the ID of the Amazon Pinpoint
     project that contains the endpoint.
    + Replace `UserId` with the ID of the
     user.

- Campaign Creation With [Amazon Pinpoint message templates](messages-templates.md "messages-templates.md")
  [create-campaign](../../../cli/latest/reference/pinpoint/create-campaign.md "../../../cli/latest/reference/pinpoint/create-campaign.md") CLI

```
aws pinpoint create-campaign —application-id `AppId` —write-campaign-request file://campaignclirequest.json

file://campaignclirequest.json
{
	"Description": "CLITestCampaign",
	"HoldoutPercent": 0,
	"MessageConfiguration":
	{
		"DefaultMessage":
		{
			"Body": "TestFromCLI"
		}
	},
	"Name": "TestingCLICampaign",
	"Schedule":
	{
		"StartTime": "IMMEDIATE"
	},
	"TemplateConfiguration":
		{
		"EmailTemplate":
			{
			"Name": "`TemplateName`",
			"Version": "`Version`"
			}
		},
	"SegmentId": "`SegmentID`",
	"SegmentVersion": 1
}
```

###### In the preceding command and file, make the following changes:

    + Replace `AppId` with the ID of the Amazon Pinpoint
     project that contains the endpoint.
    + Replace `TemplateName` with the name of the
     template.
    + Replace `Version` with the version of the
     template.
    + Replace `SegmentID` with the ID of the
     segment to target.
