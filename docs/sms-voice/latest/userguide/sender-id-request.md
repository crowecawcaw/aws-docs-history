# Request a sender ID in AWS End User Messaging SMS

Before you request a sender ID verify that they are available, see [Supported countries and regions for SMS
messaging with AWS End User Messaging SMS](phone-numbers-sms-by-country.md "phone-numbers-sms-by-country.md").

For the rules of which sender ID is displayed when you send SMS messages to countries where Sender IDs are supported, compared to those where Sender IDs aren't supported, see [Sender ID display name rules](sender-id.md#channels-sms-countries-sender-id "sender-id.md#channels-sms-countries-sender-id").

###### Note

Some countries require you to register your sender ID or open a support case to request the sender ID.

- **India sender ID registration** – Register a sender
  ID for use in India. For more information on completing the registration for see [India sender ID registration process in
  AWS End User Messaging SMS](registrations-sms-senderid-india.md "registrations-sms-senderid-india.md").
- **Singapore sender ID registration** – Register a sender ID
  in Singapore. For more information on completing the registration for see [Singapore sender ID registration form](registrations-sg-form.md "registrations-sg-form.md").
- **Request a Sender
  ID from Support** Senders are required to use a pre-registered alphabetic sender ID. To request a Sender
  ID from Support, [How to request a sender ID through Support](sender-id-awssupport-open.md "sender-id-awssupport-open.md"). Some countries require senders to meet specific
  requirements or abide by certain restrictions in order to obtain approval. In these cases,
  Support might contact you for additional information after you submit your sender ID request.
  For a list of countries that require a support ticket to request a sender ID, see the Supports
  Sender IDs column in [Supported countries and regions for SMS
  messaging with AWS End User Messaging SMS](phone-numbers-sms-by-country.md "phone-numbers-sms-by-country.md").
  To request a sender ID using the AWS End User Messaging SMS console, follow these steps:

###### Request a sender ID

1. Open the AWS End User Messaging SMS console at
   [https://console.aws.amazon.com/sms-voice/](https://console.aws.amazon.com/sms-voice/ "https://console.aws.amazon.com/sms-voice/").
2. In the navigation pane, under **Configurations**, choose
   **Sender ID** and then **Request originator**.
3. On the **Select country** page you must choose the country from the dropdown
   that messages will be sent to.

Choose **Next** to continue defining the use case and for a suggested
phone number or sender ID type. 4. On the **Messaging use case** section, enter the following:

    * Under **Number capabilities**, choose either **SMS**,
     **Voice** or both depending on your requirements.




    	+ **Text messages (SMS)** – Choose if you need SMS capabilities.
    	+ **Text to audio messages (Voice)** – Choose if you need SMS capabilities.

5. Under **Estimated monthly SMS message volume per month –
   optional**, choose the estimated number of SMS messages you will send each
   month.
6. For **Company headquarters - optional**, choose either of the following:
   - **Local** – Choose this if your companies headquarters is in
     the same country as your customers who will revive SMS messages. For example, you would choose this option if your headquarters is in the
     United States and your users who will receive messages are also in the United States.
   - **International** – Choose this if your companies headquarters is not in
     the same country as your customers who will revive SMS messages.

7. For **Two-way messaging**, choose **Yes** if you
   require two-way messaging.
8. Choose **Next**.
9. Under **Originator type**, choose Sender ID.

If sender ID isn't available then choose **Previous** to go back and
modify your use case. Also check the [Supported countries and regions for SMS
messaging with AWS End User Messaging SMS](phone-numbers-sms-by-country.md "phone-numbers-sms-by-country.md") to sender IDs are supported in the destination
country.

In the **Sender ID** field enter a sender ID. The sender ID must be 1-11 alphanumeric characters including letters (A-Z), numbers (0-9), or hyphens (-). The sender ID must begin with a letter. 10. Use **Resource policy** to share the sender ID with other
AWS accounts or AWS services. To share the sender ID at a later time, see [Sharing a phone number, pool, opt-out list, or sender ID](shared-resources.md#sharing-share "shared-resources.md#sharing-share"). For more information on
**Resource policy**, see [Working with shared resources in AWS End User Messaging SMS](shared-resources.md "shared-resources.md").

###### Note

You must use **Resource policy** to share the sender ID with Amazon Pinpoint or Amazon SNS
even if you are using the same AWS account.

    1. Choose **Pinpoint campaign orchestration(Amazon Pinpoint)** to share the pool
     with Amazon Pinpoint
    2. Choose **Simple notification Service (Amazon SNS)** to share the pool with
     Amazon SNS

11. Choose **Next**.
12. On **Review and request** you can verify and edit your request before submitting it. Choose **Request**.
13. A **Registration Required** window might appear depending on the type of
    number you requested. For more information about registrations requirements see [Origination identity registration in AWS End User Messaging SMS](registrations.md "registrations.md").
    1.  For **Registration form name** enter a name.
    2.  Choose **Complete registration** to finish registering the sender ID
        or **Register later**.

    ###### Important

    You are still billed the recurring monthly lease fee regardless of registration status.
