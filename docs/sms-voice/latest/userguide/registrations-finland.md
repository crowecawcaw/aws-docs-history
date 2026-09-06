

# Finland sender ID registration in AWS End User Messaging SMS
<a name="registrations-finland"></a>

Follow these directions to register your sender ID in Finland. As required by Finnish regulation (Traficom Order 28 L/2025 M), all sender IDs used to send SMS messages to Finnish mobile numbers must be pre-registered with local operators.

1. Open the AWS End User Messaging SMS console at [https://console.aws.amazon.com/sms-voice/](https://console.aws.amazon.com/sms-voice/).

1. In the navigation pane, under **Registrations**, choose **Create registration**.
**Note**  
If you already created a registration when requesting the origination identity then you should use that registration form. 

   For **Registration form name** enter a friendly name.

   Choose **Next**.

1. In the **Sender ID info** section, enter the following:
   + For **Sender ID**, enter the sender ID to request. The sender ID must be between 3 and 11 alphanumeric characters. For more information on sender ID formatting rules, see [Considerations for a sender ID](sender-id.md#sender-id-considerations)

   Choose **Next**.

1. In the **Company info** section, enter the following:
   + For **Company Name**, enter the name of your company as officially registered.
   + For **Company identification number – optional**, enter your tax ID or business registration number (such as a Finnish Business ID or VAT number), if available.
   + For **Company website**, enter the URL for your company's website.

   Choose **Next**.

1. In **Messaging Use Case**, do the following:
   + For **Use case category**, choose one of the following use case types:
     + **One-time passwords** – Use this for sending a user a one-time password or verification code.
     + **Account or security alerts** – Use this for sending account notifications or security alerts.
     + **Purchase or delivery notifications** – Use this if you only intend to send your users important notifications.
     + **Public service announcements** – An informational message that is meant to raise the audience's awareness about an important issue.
     + **Polling and surveys** – Use this to poll users on their preferences.
     + **Info on demand** – This is for sending users messages after they have sent a request.
     + **Promotions and marketing** – Use this for sending promotional or marketing messages.
     + **Other** – Use this if your use case doesn't fall into any other category. Be sure that you fill out the **Use case details** for this option.
   + Complete **Use case description** to provide additional context to the selected **Use case category**.

   Choose **Next**.

1. In **Message samples**, do the following:
   + For **Message Sample 1**, enter an example message of an SMS message body that will be sent to your end users.
   + For **Message Sample 2 – optional** and **Message Sample 3 – optional**, enter additional example messages, if needed, of the SMS message body that will be sent.

   Choose **Next**.

1. On the **Review and submit** page verify the information you are about to submit is correct. To make updates choose **Edit** next to the section.

1. Choose **Submit registration**.