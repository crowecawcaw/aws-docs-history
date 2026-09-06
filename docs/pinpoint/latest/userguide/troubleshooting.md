

**End of support notice:** On October 30, 2026, AWS will end support for Amazon Pinpoint. After October 30, 2026, you will no longer be able to access the Amazon Pinpoint console or Amazon Pinpoint resources (endpoints, segments, campaigns, journeys, and analytics). For more information, see [Amazon Pinpoint end of support](https://docs.aws.amazon.com/console/pinpoint/migration-guide). **Note:** APIs related to SMS, voice, mobile push, OTP, and phone number validate are not impacted by this change and are supported by AWS End User Messaging.

# Troubleshooting
<a name="troubleshooting"></a>

**Note**  
The following troubleshooting topics have been moved:  
[Troubleshooting segments](segments-troubleshooting.md)
[Troubleshooting campaigns](campaigns-troubleshooting.md)
[Troubleshooting journeys](journeys-troubleshooting.md)
[Troubleshooting the SMS channel](channels-sms-troubleshooting.md)
[Troubleshooting the voice channel](channels-voice-troubleshooting.md)
[Troubleshooting the push channel](channels-push-troubleshooting.md)
[Troubleshooting the email channel](channels-email-troubleshooting.md)

 Become familiar with troubleshooting information and possible solutions to help resolve issues when using Amazon Pinpoint.<a name="troubleshooting-logging"></a>

**Monitoring and logging**

As a best practice, consider logging events in Amazon Pinpoint by:
+ Turning on Events Streams through Amazon Kinesis Data Streams following the instructions in [Streaming events with Amazon Pinpoint](analytics-streaming.md). 
+ Using a custom logging solution. For more information, see [Digital User Engagement Events Database](https://aws.amazon.com/solutions/implementations/digital-user-engagement-events-database/). Multiple services are involved and additional costs are incurred.
+ Using Amazon CloudWatch metrics supported by Amazon Pinpoint. For more information, see [Monitoring Amazon Pinpoint with Amazon CloudWatch](monitoring.md). 
+ Using Amazon Pinpoint API calls logged in CloudTrail. For more information, see [Logging Amazon Pinpoint API calls with AWS CloudTrail](https://docs.aws.amazon.com/pinpoint/latest/developerguide/logging-using-cloudtrail.html) in the *Amazon Pinpoint Developer Guide*.

**Topics**
+ [CLI examples of common tasks](#troubleshooting-cli-examples)

## CLI examples of common tasks
<a name="troubleshooting-cli-examples"></a>

The following examples are common CLI commands for Amazon Pinpoint.
+ Get Endpoint Data: [get-endpoint](https://docs.aws.amazon.com/cli/latest/reference/pinpoint/get-endpoint.html) CLI

  ```
  aws pinpoint get-endpoint —application-id {{AppId}} —endpoint-id {{EndpointId}}
  ```

**In the preceding command, make the following changes:**
  + Replace {{AppId}} with the ID of the Amazon Pinpoint project that contains the endpoint.
  + Replace {{EndpointId}} with the ID of an existing endpoint that you're retrieving.
+ Get User Data: [get-user-endpoints](https://docs.aws.amazon.com/cli/latest/reference/pinpoint/get-user-endpoints.html) CLI

  ```
  aws pinpoint get-user-endpoints —application-id {{AppId}} —user-id {{UserId}}
  ```

**In the preceding command, make the following changes:**
  + Replace {{AppId}} with the ID of the Amazon Pinpoint project that contains the endpoint.
  + Replace {{UserId}} with the ID of the user.
+ Update or Create New Endpoint: [update-endpoint](https://docs.aws.amazon.com/cli/latest/reference/pinpoint/update-endpoint.html) CLI

  ```
  aws pinpoint update-endpoint —application-id {{AppId}} —endpoint-id {{EndpointId}} —endpoint-request '{"ChannelType":"SMS","Address":"+12345678","Location":{"Country":"USA"},"User":{"UserId":"{{UserId}}"}}'
  ```

**In the preceding command, make the following changes:**
  + Replace {{AppId}} with the ID of the Amazon Pinpoint project that contains the endpoint.
  + Replace {{EndpointId}} with the ID of an existing endpoint that you're creating or updating.
  + Replace {{UserId}} with the ID of the user.
+ Delete Endpoint: [delete-endpoint](https://docs.aws.amazon.com/cli/latest/reference/pinpoint/delete-endpoint.html) CLI

  ```
  aws pinpoint delete-endpoint —application-id {{AppId}} —endpoint-id {{EndpointId}} 
  ```

**In the preceding command, make the following changes:**
  + Replace {{AppId}} with the ID of the Amazon Pinpoint project that contains the endpoint.
  + Replace {{EndpointId}} with the ID of an existing endpoint that you're deleting.
+ Validate a phone number: [phone-number-validate](https://docs.aws.amazon.com/cli/latest/reference/pinpoint/phone-number-validate.html) CLI

  ```
  aws pinpoint phone-number-validate —number-validate-request PhoneNumber={{+12065550100}}
  ```

**In the preceding command, make the following changes:**
  + Replace {{\+12065550100}} with the phone number that you want to validate.
+ [send-messages](https://docs.aws.amazon.com/cli/latest/reference/pinpoint/send-messages.html) Examples CLI: SMS to a number

  ```
  aws pinpoint send-messages --application-id {{AppID}} --message-request '{"MessageConfiguration": {"SMSMessage":{"Body":"This is a test message"}},"Addresses": {"{{DestinationPhoneNumber}}": {"ChannelType":"SMS"}}}‘
  ```

**In the preceding command, make the following changes:**
  + Replace {{AppId}} with the ID of the Amazon Pinpoint project that contains the endpoint.
  + Replace {{DestinationPhoneNumber}} with the phone number that you want to send to.
+ [send-messages](https://docs.aws.amazon.com/cli/latest/reference/pinpoint/send-messages.html) Examples CLI: origination number to SMS

  ```
  aws pinpoint send-messages --application-id {{AppID}} --message-request '{"MessageConfiguration": {"SMSMessage":{"Body":"hello, how are you?","OriginationNumber": "{{OriginPhoneNumber}}"}},"Addresses": {"{{DestinationPhoneNumber}}": {"ChannelType":"SMS"}}}‘
  ```

**In the preceding command, make the following changes:**
  + Replace {{AppId}} with the ID of the Amazon Pinpoint project that contains the endpoint.
  + Replace {{OriginPhoneNumber}} with the phone number that you want to send the message from.
  + Replace {{DestinationPhoneNumber}} with the phone number that you want to send to.
+ [send-messages](https://docs.aws.amazon.com/cli/latest/reference/pinpoint/send-messages.html) Examples CLI: SMS to an endpoint

  ```
  aws pinpoint send-messages —application-id {{AppID}}  —message-request '{"MessageConfiguration": {"SMSMessage":{"Body":"This is a test message"}},"Endpoints": {"{{EndPointId}}": {}}}'
  ```

**In the preceding command, make the following changes:**
  + Replace {{AppId}} with the ID of the Amazon Pinpoint project that contains the endpoint.
  + Replace {{EndPointId}} with the ID of an existing endpoint that you're sending to.
+ [send-messages](https://docs.aws.amazon.com/cli/latest/reference/pinpoint/send-messages.html) Examples CLI: SMS to a userId

  ```
  aws pinpoint send-users-messages —application-id {{AppID}} —send-users-message-request '{"MessageConfiguration": {"SMSMessage":{"Body":"This is a test"}},"Users": {"{{UserId}}": {}}}'
  ```

**In the preceding command, make the following changes:**
  + Replace {{AppId}} with the ID of the Amazon Pinpoint project that contains the endpoint.
  + Replace {{UserId}} with the ID of the user.
+ Campaign Creation With [Amazon Pinpoint message templates](messages-templates.md) [create-campaign](https://docs.aws.amazon.com/cli/latest/reference/pinpoint/create-campaign.html) CLI

  ```
  aws pinpoint create-campaign —application-id {{AppId}} —write-campaign-request file://campaignclirequest.json 
  
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
  			"Name": "{{TemplateName}}",
  			"Version": "{{Version}}"
  			}
  		},
  	"SegmentId": "{{SegmentID}}",
  	"SegmentVersion": 1
  }
  ```

**In the preceding command and file, make the following changes:**
  + Replace {{AppId}} with the ID of the Amazon Pinpoint project that contains the endpoint.
  + Replace {{TemplateName}} with the name of the template.
  + Replace {{Version}} with the version of the template.
  + Replace {{SegmentID}} with the ID of the segment to target.