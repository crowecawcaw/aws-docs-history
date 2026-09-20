

# Amazon SNS person-to-person long codes
<a name="channels-sms-originating-identities-long-codes"></a>

**Important**  
Effective August 31, 2023, a dedicated number such as a [10DLC](https://docs.aws.amazon.com/sms-voice/latest/userguide/registrations.html) number or a [toll-free number](https://docs.aws.amazon.com/sms-voice/latest/userguide/registrations-tfn.html) is required to send SMS text messages to the United States and its territories (Puerto Rico, Guam, American Samoa Islands and the US Virgin Islands). Your long code request will be rejected if you use the United States as the location for these regions.

Person-to-person long codes (P2P) are phone numbers that use the number format of the country or region where your recipients are located. P2P long codes are also called long numbers or virtual mobile numbers. For example, in the United States and Canada, P2P long codes contain 11 digits. They include the number 1 (the country code), a three-digit area code, and a seven-digit phone number.

For more information about requesting P2P long codes, see [Requesting dedicated long codes for SMS messaging](https://docs.aws.amazon.com/sms-voice/latest/userguide/phone-numbers-request.html).

**Advantages**

Dedicated P2P long codes are reserved for your Amazon SNS account only—they aren't shared with other users. When you use dedicated P2P long codes, you can specify which P2P long code to use for each message. If you send multiple messages to the same customer, each message appears to be sent from the same phone number. Dedicated P2P long codes can help establish your brand or identity.

**Disadvantages**

P2P long codes aren't supported for A2P communications to US destinations. 

If you send several hundred messages per day from a dedicated P2P long code, mobile carriers might flag your number as one that sends unsolicited messages. If your P2P long code is flagged, your messages might not reach your recipients.

P2P long codes also have limited throughput. The maximum sending rate varies by country. Contact AWS Support for more information. If you plan to send large volumes of SMS messages or send at a rate greater than one message per second, purchase a dedicated short code.

Some carriers don't allow P2P long codes for A2P SMS messages. This includes carriers in the US. An A2P SMS is a message sent to a customer's mobile device when that customer submits his or her mobile number to an application. A2P messages are one-way conversations, such as marketing messages, one-time passwords, and appointment reminders. If you plan to send A2P messages, purchase a dedicated short code (for customers in the United States or Canada). Or, use a sender ID (for recipients in a country or region where sender IDs are supported).

A 10DLC number is used only for sending messages within the US. Using a 10DLC number requires that you register your company brand and the campaign to associate with the number. After approval, you can request a 10DLC phone number on the **SMS and voice** page of the Amazon Pinpoint console at [https://console.aws.amazon.com/pinpoint/](https://console.aws.amazon.com/pinpoint/). The time to receive approval is 7-10 days. The number can't be used with any other campaigns.