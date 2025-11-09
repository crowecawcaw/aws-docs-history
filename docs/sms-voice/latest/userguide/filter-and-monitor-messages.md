# Country rule modes in AWS End User Messaging SMS

Artificially inflated traffic (AIT) occurs when bots or bad actors target web or mobile
applications that trigger SMS message sends. This results in unwanted and unaccepted SMS
message charges. To help lessen the impact of an SMS AIT attack on your web or mobile
application, set country rules to either block (prevent all messages to a country), or
filter (to use the End User Messaging AIT detection model to filter suspected AIT message
requests).

## What are the country rule modes in

AWS End User Messaging SMS

You can apply different country modes to individual countries or geographic regions,
like North America. The country rule mode can be overridden with a [phone number override
rule](protect-rule-override-rules-processing.md#protect-rule-override-rules-processing.title "protect-rule-override-rules-processing.md#protect-rule-override-rules-processing.title") for specific phone numbers.

| Country rule mode | Mode name                                                                                                                        | Description |
| ----------------- | -------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| Block             | Block sending of messages to the destination country.                                                                            |
| Allow             | Allow sending message to the destination country.                                                                                |
| Monitor           | Allow sending messages to the destination country, but include the<br>SMS protect blocking recommendation in metrics and events. |
| Filter            | Allow sending messages to the destination country, but block messages<br>that the End User Messaging suspects as AIT.            |

###### Important

- Messages using “monitor” or “filter” mode incur additional charges for AIT
  risk evaluation. See [pricing for
  details](https://aws.amazon.com/end-user-messaging/pricing/ "https://aws.amazon.com/end-user-messaging/pricing/").
- Protect’s filter and monitor modes use statistical models that generate
  AIT risk predictions based on patterns in data. We are always working to
  improve these models, but, as with any such models, the accuracy of their
  predictions is not guaranteed (e.g., there is a chance that legitimate SMS
  messages may be flagged as an AIT risk).
- Filter and monitor modes are designed to help you mitigate the impacts of
  AIT, but do not guarantee complete protection from AIT. We recommend using
  additional safeguards on your web and mobile applications for well- rounded
  AIT protection.

## Set a country mode in AWS End User Messaging SMS

Each protect configuration can apply a country rule mode to each country or geographic
region. The country rule mode can be to
_Allow_, _Block_, _Monitor_, or
_Filter_ messages to that country. Use phone number overrides to
create allow and deny exceptions for specific phone numbers.

To edit a protect configuration country rules using the AWS End User Messaging SMS console, follow these
steps:

1. Open the AWS End User Messaging SMS console at
   [https://console.aws.amazon.com/sms-voice/](https://console.aws.amazon.com/sms-voice/ "https://console.aws.amazon.com/sms-voice/").
2. In the navigation pane, under **Protect**, choose
   **Protect configuration**.
3. On the **Protect configuration** page, choose a protect
   configuration and then choose **Edit**.
4. In the protect configuration details table choose the **SMS
   rules** or **Voice rules** tab.
5. In the **SMS/Voice country rules** tab check the countries to
   change the rules for and then choose **Allow**,
   **Block**, **Monitor**, or
   **Filter**. You can sort and filter the country
   list based on **Country**, **Region** and
   **Rule**.
6. In the **Status change confirmation** window review your
   changes and then choose **Confirm** to apply them.

The new country rule set is now used for the protect configuration.
