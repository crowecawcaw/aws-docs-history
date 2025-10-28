**End of support notice:** On October
30, 2026, AWS will end support for Amazon Pinpoint. After October 30, 2026, you will no
longer be able to access the Amazon Pinpoint console or Amazon Pinpoint resources (endpoints,
segments, campaigns, journeys, and analytics). For more information, see [Amazon Pinpoint end of
support](../../../console/pinpoint/migration-guide.md "../../../console/pinpoint/migration-guide.md"). **Note:** APIs related to SMS, voice,
mobile push, OTP, and phone number validate are not impacted by this change and are
supported by AWS End User Messaging.

# Create a custom channel in Amazon Pinpoint using a webhook or Lambda function

Amazon Pinpoint includes built-in support for sending messages through the push notification, email,
SMS, and voice channels. You can also configure Amazon Pinpoint to send messages through other
channels by creating custom channels. Custom channels in Amazon Pinpoint allow you to send messages
through any service that has an API, including third-party services. You can interact with
APIs by using a webhook, or by calling an AWS Lambda function.

The segments that you send custom channel campaigns to can contain endpoints of all types
(that is, endpoints where the value of the `ChannelType` attribute is EMAIL,
VOICE, SMS, CUSTOM, or one of the various push notification endpoint types).

## Use a webhook

If you use a webhook to send custom channel messages, the URL of the webhook must
begin with "https://". The webhook URL can only contain alphanumeric characters, plus
the following symbols: hyphen (-), period (.), underscore (\_), tilde (~), question mark
(?), slash or solidus (/), pound or hash sign (#), and semicolon (:). The URL has to
comply with [RFC3986](https://datatracker.ietf.org/doc/html/rfc3986 "https://datatracker.ietf.org/doc/html/rfc3986").

When you create a campaign that specifies a webhook URL, Amazon Pinpoint issues an HTTP
`HEAD` to that URL. The response to the `HEAD` request must
contain a header called `X-Amz-Pinpoint-AccountId`. The value of this header
must equal your AWS account ID.

## Use a Lambda function

If you opt to instead send custom channel messages by creating a Lambda function, it's best to
first familiarize yourself with the data that Amazon Pinpoint emits. When a Amazon Pinpoint campaign sends
messages over a custom channel, it sends a payload to the target Lambda function that
resembles the following example:

```
{
  "Message":{},
  "Data":"The payload that's provided in the CustomMessage object in MessageConfiguration",
  "ApplicationId":"3a9b1f4e6c764ba7b031e7183example",
  "CampaignId":"13978104ce5d6017c72552257example",
  "TreatmentId":"0",
  "ActivityId":"575cb1929d5ba43e87e2478eeexample",
  "ScheduledTime":"2020-04-08T19:00:16.843Z",
  "Endpoints":{
    "1dbcd396df28ac6cf8c1c2b7fexample":{
      "ChannelType":"EMAIL",
      "Address":"mary.major@example.com",
      "EndpointStatus":"ACTIVE",
      "OptOut":"NONE",
      "Location":{
        "City":"Seattle",
        "Country":"USA"
      },
      "Demographic":{
        "Make":"OnePlus",
        "Platform":"android"
      },
      "EffectiveDate":"2020-04-01T01:05:17.267Z",
      "Attributes":{
        "CohortId":[
          "42"
        ]
      },
      "CreationDate":"2020-04-01T01:05:17.267Z"
    }
  }
}
```

The event data provides the following attributes:

- `ApplicationId` – The ID of the Amazon Pinpoint project that the
  campaign belongs to.
- `CampaignId` – The ID of the Amazon Pinpoint campaign that invoked the
  Lambda function.
- `TreatmentId` – The ID of the campaign variant. If you
  created a standard campaign, this value is always 0. If you created an A/B test
  campaign, this value is an integer between 0 and 4.
- `ActivityId` – The ID of the activity being performed by the
  campaign.
- `ScheduledTime` – The time when Amazon Pinpoint executed the campaign,
  shown in ISO 8601 format.
- `Endpoints` – A list of the endpoints that were targeted by
  the campaign. Each payload can contain up to 50 endpoints. If the segment that
  the campaign was sent to contains more than 50 endpoints, Amazon Pinpoint invokes the
  function repeatedly, with up to 50 endpoints at a time, until all endpoints have
  been processed.

You can use this sample data when creating and testing your custom channel Lambda
function.
