# Amazon Pinpoint in AWS GovCloud (US)

###### Important

**End of support notice:** On October 30, 2026, AWS will end support for Amazon Pinpoint. After October 30, 2026, you will no longer be able to access the Amazon Pinpoint console or Amazon Pinpoint resources (endpoints, segments, campaigns, journeys, and analytics). For more information, see [Amazon Pinpoint end of support](../../../console/pinpoint/migration-guide.md "../../../console/pinpoint/migration-guide.md"). **Note:** APIs related to SMS, voice, mobile push, OTP, and phone number validate are not impacted by this change and are supported by AWS End User Messaging.

Amazon Pinpoint is an AWS service that you can use to engage with you customers across multiple messaging channels. You can use Amazon Pinpoint to send push notifications, emails, SMS text messages, and voice messages.

The Amazon Pinpoint API is currently available in AWS GovCloud (US-West).

## How Amazon Pinpoint differs for AWS GovCloud (US)

- Amazon Pinpoint API
  - You can’t use the SendMessages operation in the Amazon Pinpoint API to send voice messages.
  - The **Machine learning modules** section isn’t available in the Amazon Pinpoint console.
  - The **Analytics** section of the Amazon Pinpoint console doesn’t include the **Events** page.
  - When you create a campaign, you can’t configure the campaign to be sent when an event occurs.
  - When you create a journey, you can only configure the **Journey entry** activity to add participants who are in a specific segment. You can’t configure the **Journey entry** activity to add participants when they perform an activity (also known as an event).
  - You can’t create message templates that include recommendations provided by Amazon Personalize.
  - The In-App channel is unavailable.
  - Time zone estimation is not supported.

## Documentation for Amazon Pinpoint

Amazon Pinpoint
[documentation](../../../pinpoint/latest/userguide/pinpoint-ug.md "../../../pinpoint/latest/userguide/pinpoint-ug.md") and Amazon Pinpoint API [documentaiton](../../../pinpoint/latest/apireference/welcome.md "../../../pinpoint/latest/apireference/welcome.md").

## Export-controlled content

For AWS Services architected within the AWS GovCloud (US) Regions, the following list explains how certain components of data may leave the AWS GovCloud (US) Regions in the normal course of the service offerings. The list can be used as a guide to help meet applicable customer compliance obligations. Data not included in the following list remains within the AWS GovCloud (US) Regions.

- Amazon Pinpoint metadata is not permitted to contain export-controlled data. This metadata includes all the configuration data that you enter when creating and maintaining your Amazon Pinpoint tables, such as table names, hash attribute names, and range attribute names.
- Do not enter export-controlled data in the following fields:
  - Keyspace names
  - Table names
  - Column names
  - Resource tags

If you are processing export-controlled data with this service, use the SSL (HTTPS) endpoint to maintain export compliance. For more information, see [Service Endpoints](using-govcloud-endpoints.md "using-govcloud-endpoints.md").
