

**End of support notice:** On October 30, 2026, AWS will end support for Amazon Pinpoint. After October 30, 2026, you will no longer be able to access the Amazon Pinpoint console or Amazon Pinpoint resources (endpoints, segments, campaigns, journeys, and analytics). For more information, see [Amazon Pinpoint end of support](https://docs.aws.amazon.com/console/pinpoint/migration-guide). **Note:** APIs related to SMS, voice, mobile push, OTP, and phone number validate are not impacted by this change and are supported by AWS End User Messaging.

# Add unsubscribe headers to email using Amazon Pinpoint
<a name="send-messages-email-cli"></a>

**Note**  
Before you can use email headers, you must set up an email orchestration sending role if you are sending email from a campaign or a journey. For direct send email, you must have permissions for `ses:SendEmail` and `ses:SendRawEmail`. For more information, see [Creating an email orchestration sending role](https://docs.aws.amazon.com/pinpoint/latest/userguide/channels-email-orchestration-sending-role.html) in the [Amazon Pinpoint User Guide](https://docs.aws.amazon.com/pinpoint/latest/userguide/).

Including an unsubscribe link in your email is a best practice, and in some countries it's a legal requirement. To add a One-click unsubscribe link add the following headers: 

1. Set the header **Name** to `List-Unsubscribe` and set **Value** to your unsubscribe link. The link must support HTTP POST requests to process the recipients unsubscribe request.

1. Set the header **Name** to `List-Unsubscribe-Post` and set **Value** to `List-Unsubscribe=One-Click`. 

You can add up to 15 headers to an email message. For a list of supported headers see [Amazon SES header fields](https://docs.aws.amazon.com/ses/latest/dg/header-fields.html) in the [Amazon Simple Email Service Developer Guide](https://docs.aws.amazon.com/ses/latest/DeveloperGuide/).

The following example shows how to send an email message with unsubscribe headers using the AWS Command Line Interface. For more information about configuring the AWS CLI, see [Configure the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-configure.html) in the [AWS Command Line Interface User Guide](https://docs.aws.amazon.com/cli/latest/userguide/).

In the following command, do the following:
+ Replace {{AppId}} with your application id.
+ Replace {{richard\_roe@example.com}} with the recipient's email address.
+ Replace {{https://example.com/unsub}} with your unsubscribe link.
+ Replace {{example123456}} with a unique identifier for the recipient.

```
aws pinpoint send-messages --application-id {{AppId}} --message-request '{
 "Addresses": {
   "{{richard_roe@example.com}}": {
     "ChannelType": "EMAIL"
   }
 },
 "MessageConfiguration": {
   "EmailMessage": {
     "Substitutions": {
       "url": [
         "{{https://example.com/unsub}}"
       ],
        "id1": [
          "/{{example123456}}"
        ]
     },
     "SimpleEmail": {
       "TextPart": {
         "Data": "Sample email message with an subscribe header",
         "Charset": "UTF-8"
       },
       "Subject": {
         "Data": "Hello",
         "Charset": "UTF-8"
       },
       "Headers": [
         {
           "Name": "List-Unsubscribe",
           "Value": "{{url}}{{id1}}"
         },
         {
           "Name": "List-Unsubscribe-Post",
           "Value": "List-Unsubscribe=One-Click"
         }
       ]
     }
   }
 }
}'
```