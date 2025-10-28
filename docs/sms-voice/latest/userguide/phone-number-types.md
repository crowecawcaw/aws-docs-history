# Choosing an origination identity

Dedicated phone numbers are country-specific. You can't request a dedicated phone number
for one country but then use it as an identity for another country.

When you send SMS or MMS messages using AWS End User Messaging SMS, you can identify yourself to your
recipients by using a sender ID, long code, 10 digit long code(10DLC), short code or
toll-free number. Each of these types of identities has its own advantages and
disadvantages, which are discussed in the following sections. Origination identities are
resources that are unique to each AWS Region, so they can't be shared across
AWS Regions. You can grant cross AWS account and AWS Region access to your origination
identities.

For example if your use case requires you to send message to the United States and Canada
you have to provision origination identities for both of those countries. You do not need to
provision the origination identities in AWS Regions that are local to that country. You
could provision both origination identities in US West (Oregon). As another example if
your use case requires you to send message to the United States and India you might want to
provision the origination identities in AWS Regions that are geographically close to their
message destinations to reduce latency. For more information see the [Amazon Pinpoint Resilient
Architecture Guide](../../../pinpoint/latest/archguide/welcome.md "../../../pinpoint/latest/archguide/welcome.md").

Using the AWS End User Messaging SMS console, we’ll recommend one of the below origination identities depending
on your use-case. Recommendations are based on your input criteria including if you require
SMS and/or voice capabilities, a two-way number, and estimate monthly messages.

###### Topics

- [Sender ID](#phone-number-types-sender-id "#phone-number-types-sender-id")
- [Long codes](#phone-number-types-long-code "#phone-number-types-long-code")
- [10 digit long code (10DLC)](#phone-number-types-10dlc "#phone-number-types-10dlc")
- [Short codes](#phone-number-types-short-code "#phone-number-types-short-code")
- [Toll-free number (TFN)](#phone-number-types-tfn "#phone-number-types-tfn")
- [General considerations for choosing an
  origination identity](#phone-number-types-choosing-general "#phone-number-types-choosing-general")
- [Choosing an origination identity
  for one-way messaging use cases](#phone-number-types-choosing-oneway "#phone-number-types-choosing-oneway")
- [Choosing an origination identity
  for two-way messaging use cases](#phone-number-types-choosing-twoway "#phone-number-types-choosing-twoway")

## Sender ID

A sender ID is an alphanumeric name that identifies the sender of an SMS message. When
you send an SMS message using a sender ID, and the recipient is in an area where sender
ID authentication is supported, your sender ID appears on the recipient's device instead
of a phone number. A sender ID provides SMS recipients with more information about the
sender than a phone number or short code provides.

Sender IDs are supported in several countries and regions around the world. In some
places, if you're a business that sends SMS messages to individual customers, you must
use a sender ID that's pre-registered with a regulatory agency or industry group. For a
complete list of countries and regions that support or require sender IDs, see [SMS and MMS country capabilities and limitations](phone-numbers-sms-support-by-country.md "phone-numbers-sms-support-by-country.md").

**Advantages**

Sender IDs provide the recipient with more information about the message sender. It's
easier to establish your brand identity by using a sender ID than by using a short or
long code. There's no additional charge for using a sender ID.

**Disadvantages**

Support and requirements for sender ID authentication aren't consistent across all
countries or regions. Several major markets (including Canada, China, and the United
States) don't support sender ID. In some areas, you must have your sender IDs
pre-approved by a regulatory agency before you can use them. Sender IDs do not support
two-way SMS messaging.

## Long codes

Long codes are phone numbers that use the number format of the country or region where
your recipients are located. Long codes are also referred to as long numbers or virtual
mobile numbers. For example, in the United States and Canada, long codes contain 11
digits: the number 1 (the country code), a three-digit area code, and a seven-digit
phone number. Long codes support MMS in the United States and Canada.

**Advantages**

Dedicated long codes are reserved for use by your AWS End User Messaging SMS account only—they aren't
shared with other users. When you use dedicated long codes, you can specify which long
code you want to use when you send each message. If you send multiple messages to the
same customer, each message appears to be sent from the same phone number. For this
reason, dedicated long codes can be helpful in establishing your brand or identity.
Dedicated long codes support two-way SMS messages and you can receive incoming messages
from your customers.

**Disadvantages**

If you send several hundred messages per day from a dedicated long code, mobile
carriers might identify your number as one that sends unsolicited messages. If your long
code is flagged, your messages might not be delivered to your recipients.

Long codes also have limited throughput. In the United States and Canada, where long
codes are most commonly used, you can send a maximum of one message per second. The
maximum sending rates for other countries vary. Contact AWS Support for more
information. If you plan to send large volumes of SMS messages, or you plan to send at a
rate greater than one message per second, you should purchase a dedicated short
code.

In the United States, local long codes cannot be used for A2P SMS messages. For more
information see [10 digit long code (10DLC)](#phone-number-types-10dlc "#phone-number-types-10dlc").

## 10 digit long code (10DLC)

If you want to use local long codes in the United States to send SMS or MMS messages
you need to request a 10DLC, which is a ten-digit long code dedicated only for use in
the United States.

Many jurisdictions have restrictions related to using long codes to send
Application-to-Person (A2P) SMS messages. An A2P SMS or MMS is a message that's sent to
a customer's mobile device when that customer submits his or her mobile number to an
application. A2P messages are one-way conversations, such as marketing messages,
one-time passwords, and appointment reminders. If you plan to send A2P messages, you
should purchase a dedicated short code (if your customers are in the United States or
Canada), request a 10DLC (only if your customers are in the United States), or use a
sender ID (if your recipients are in a country or region where sender IDs are
supported).

A 10DLC number is used only for sending messages within the US. Using a 10DLC number
requires that you register your company brand and the campaign that you want to
associate the number with. After approval you can request a 10DLC phone number. Once
requested, the time to receive approval is 7-10 days. The number can't be used with any
other campaigns.

## Short codes

Short codes are numeric sequences that are shorter than a regular phone number. For
example, in the United States and Canada, standard phone numbers (long codes) contain 11
digits, while short codes typically contain five to seven digits. If you send a large
volume of SMS or MMS messages to recipients in the United States or Canada, you can
purchase a short code. This short code is reserved for your exclusive use. Short codes
support MMS in the United States and Canada.

**Advantages**

Using a memorable short code can help build trust. If you need to send sensitive
information, such as one-time passwords, it's a good idea to send it using a short code
so that your customer can quickly determine whether a message is actually from you.

If you're running a new customer acquisition campaign, you can invite potential
customers to send a keyword to your short code (for example, "Text FOOTBALL to 10987 for
football news and information"). Short codes are easier to remember than long codes, and
it's easier for customers to enter short codes into their devices. By reducing the
amount of difficulty that customers encounter when they sign up for your marketing
programs, you can increase the effectiveness of your campaigns.

Because mobile carriers must approve new short codes before making them active, they
are less likely to flag messages sent from short codes as unsolicited.

When you use short codes to send SMS or MMS messages, you can send a higher volume of
messages per 24-hour period than you can when you use other types of originating
identities. In other words, you have a much higher _sending quota_.
You can also send a much higher volume of messages per second. That is, you have a much
higher _sending rate_.

**Disadvantages**

There are additional costs to acquire short codes, and they can take a long time to
implement. For example, in the United States, there's a one-time setup fee for each
short code, plus an additional recurring charge per month for each short code. It can
take 8–12 weeks for short codes to become active on all carrier networks. For more
information on pricing, see [AWS End User Messaging Pricing](https://aws.amazon.com/end-user-messaging/pricing/ "https://aws.amazon.com/end-user-messaging/pricing/").

## Toll-free number (TFN)

Toll-free numbers are typically used for transactional messaging, such as registration
confirmation or for sending one-time passwords and only used within the US. They can be
used for voice, SMS and MMS messaging. Average throughput is three message parts per
second (MPS); however, this throughput is affected by character encoding. For more
information about how character encoding affects message parts, see [SMS and MMS limits and restrictions](sms-limitations.md "sms-limitations.md").

US mobile carriers require that you register your toll-free number before live
messaging will be enabled, see [Registrations](registrations.md "registrations.md"). When using or registering a toll-free number, it's
best to follow the guidelines in the Best Practices section for [Prohibited message content](best-practices.md#best-practices-sms-message-content "best-practices.md#best-practices-sms-message-content")

## General considerations for choosing an

origination identity

There are several guidelines to consider when you're deciding what type of origination
identity to use:

- Sender IDs are a great option for one-way use cases. However, they're not
  available in all countries.
- Short codes are a great option for two-way use cases. If you have to choose
  between using a short code or a long code, you should choose the short
  code.
- In some countries (such as India and Saudi Arabia), long codes can be used to
  receive incoming messages, but can't be used to send outgoing messages. You can
  use these inbound-only long codes to provide your recipients with a way to opt
  out of messages that you send using a Sender ID.
- In some countries, we maintain a pool of shared origination identities. If you
  send messages to recipients in a particular country, but you don't have a
  dedicated origination identity in that country, we make an effort to deliver
  your message using one of these shared identities. Shared identities are
  unavailable in some countries, including the United States and China.
- The mobile industry changes rapidly. In many countries, there is a trend
  toward increased regulation of commercial SMS messages. Carriers can, with
  little or no warning, decide to disallow messages sent from shared origination
  identities. If this happens, we will attempt to tell you about these changes
  with as much advance warning as possible. However, carriers generally provide us
  with little advance notice of these changes. For these reasons, dedicated
  origination identities are always preferred to shared ones.

## Choosing an origination identity

for one-way messaging use cases

A _one-way messaging_ use case is a use case that only involves
sending outgoing SMS messages to your recipients. This section provides information
about choosing the right type of origination identity for your one-way messaging use
case. If your use case requires two-way messaging—that is, the ability to both
send outgoing messages and receive incoming messages—answer the questions in [Choosing an origination identity
for two-way messaging use cases](#phone-number-types-choosing-twoway "#phone-number-types-choosing-twoway") instead.

One-way messaging use cases can use short codes, long codes, toll-free numbers, or
alphanumeric Sender IDs as their origination identity. The right kind of origination
identity to use depends on your specific needs, and on the countries that your
recipients are located in.

Answer the following questions to determine the right type of origination identity for
your needs. If you have recipients in multiple countries, answer these questions for
each country that your recipients are located in.

1. Are you planning to send messages to recipients in
   the United States?
   - If you answered **Yes**, proceed to [question 2](#one-way-q2 "#one-way-q2").
   - If you answered **No**, proceed to [question 3](#one-way-q3 "#one-way-q3").

2. Which of the following throughput rates best fits
   your use case? Your throughput rate is the number of message parts that you can
   send each second.
   - **1–3 message parts per second**:
     Use a toll-free number. You can also use 10DLC numbers or short codes.
     These number types provide plenty of room for growth, but also cost more
     and take longer to obtain than a toll-free number.

   For more information about requesting a toll-free number, see [Request a phone number](phone-numbers-request.md "phone-numbers-request.md").

   If you want to determine what kind of origination number to use for
   another country, return to [question 1](#one-way-q1 "#one-way-q1").
   Otherwise, **stop here**.
   - **10–75 message parts per second**:
     Use a 10DLC number. You can also use a short code, which would provide
     additional room for growth, but would also cost more.

   For more information about setting up 10DLC, see [United States 10DLC registration](registrations-10dlc.md "registrations-10dlc.md").

   If you want to determine what kind of origination number to use for
   another country, return to [question 1](#one-way-q1 "#one-way-q1").
   Otherwise, **stop here**.
   - **100 message parts per second or more**:
     Use a short code. When you create your request in the
     AWS Support Center Console, specify the throughput rate that you want your
     short code to support. US short codes support 100 message parts per
     second by default, but the throughput rate can be increased beyond that
     rate for an additional monthly fee.

   For more information about requesting a short code, see [Requesting dedicated short codes](phone-numbers-request-short-code.md "phone-numbers-request-short-code.md").

   If you want to determine what kind of origination number to use for
   another country, return to [question 1](#one-way-q1 "#one-way-q1").
   Otherwise, **stop here**.

3. Is it important for all of your messages to come from
   the same origination identity?
   - If you answered **Yes**, proceed to [question 4](#one-way-q4 "#one-way-q4").
   - If you answered **No**, proceed to [question 6](#one-way-q6 "#one-way-q6").

4. Are Sender IDs supported in the country that you plan
   to send messages to? For a list of countries that support Sender IDs, see [Supported countries and regions
   for SMS](phone-numbers-sms-by-country.md "phone-numbers-sms-by-country.md").
   - If you answered **Yes**, proceed to [question 5](#one-way-q5 "#one-way-q5").
   - If you answered **No**, proceed to [question 7](#one-way-q7 "#one-way-q7").

5. Does the country that you plan to send messages to
   require pre-registration of Sender IDs? For a list of countries that require
   Sender ID registration, see [Supported countries and regions
   for SMS](phone-numbers-sms-by-country.md "phone-numbers-sms-by-country.md").
   - If you answered **Yes**, complete the
     Sender ID process for the destination country. When the registration
     process is complete, you can use your Sender ID to send messages.

   If you want to determine what kind of origination identity to use for
   another country, return to [question 1](#one-way-q1 "#one-way-q1").
   Otherwise, **stop here**.
   - If you answered **No**, you can specify
     your Sender ID when you send your messages.

   If you want to determine what kind of origination identity to use for
   another country, return to [question 1](#one-way-q1 "#one-way-q1").
   Otherwise, **stop here**.

6. Are you planning to send messages to recipients in
   India?
   - If you answered **Yes**, you can start
     sending immediately. However, the messages that you send are charged at
     the International Long-Distance Operator (ILDO) rate, which costs
     several times more than messages sent using a registered Sender ID. If
     costs are an important factor, you should consider registering your
     company and use case in India. When you complete this registration
     process, you can send messages at the less-expensive local rate.

   If you want to determine what kind of origination identity to use for
   another country, return to [question 1](#one-way-q1 "#one-way-q1").
   Otherwise, **stop here**.
   - If you answered **No**, you can start
     sending without obtaining an origination identity. Your messages are
     sent using an origination identity that is shared with other AWS End User Messaging SMS
     users. The capabilities of the mobile networks in the destination
     country determine what identity is shown to recipients when they receive
     a message from you. In countries that support unregistered Sender IDs,
     your messages are sent using a generic Sender ID (such as "NOTICE"). In
     countries that don't support Sender IDs, your messages are sent from a
     random long code or short code.

   If you want to determine what kind of origination identity to use for
   another country, return to [question 1](#one-way-q1 "#one-way-q1").
   Otherwise, **stop here**.

7. Are dedicated short codes available in the country
   that you plan to send messages to? For a list of countries that support
   dedicated short codes, see [Supported countries and regions
   for SMS](phone-numbers-sms-by-country.md "phone-numbers-sms-by-country.md").
   - If you answered **Yes**, you should use a
     **short code**.
   - If you answered **No**, proceed to [question 8](#one-way-q8 "#one-way-q8").

8. Are dedicated long codes available in the country
   that you plan to send messages to? For a list of countries that support
   dedicated long codes, see [Supported countries and regions
   for SMS](phone-numbers-sms-by-country.md "phone-numbers-sms-by-country.md").
   - If you answered **Yes**, you can use a
     dedicated long code. However, if any other type of dedicated identity is
     available in that country (such as Sender IDs or short codes), you
     should use the other identity type instead. Carriers are more likely to
     block messages that are sent using long codes if other origination
     identity types are also available.

   For more information about requesting dedicated SMS long codes, see
   [Requesting dedicated long codes](phone-numbers-request-long-code.md "phone-numbers-request-long-code.md").

   If you want to determine what kind of origination identity to use for
   another country, return to [question 1](#one-way-q1 "#one-way-q1").
   Otherwise, **stop here**.
   - If you answered **No**, you can start
     sending without obtaining an origination ID. Your messages are sent
     using an origination identity that is shared with other users. The
     capabilities of the mobile networks in the destination country determine
     what identity is shown to recipients when they receive a message from
     you. In countries that support unregistered Sender IDs, your messages
     are sent using a generic Sender ID (such as "NOTICE"). In countries that
     don't support Sender IDs, your messages are sent from a random long code
     or short code.

   If you want to determine what kind of origination identity to use for
   another country, return to [question 1](#one-way-q1 "#one-way-q1").
   Otherwise, **stop here**.

## Choosing an origination identity

for two-way messaging use cases

A _two-way messaging_ use case is a use case that involves both
sending outgoing SMS messages to your customers and receiving incoming SMS messages from
them. This section provides information about choosing the right type of origination
identity for your two-way messaging use case. If your use case requires one-way
messaging—that is, only the ability to send outgoing messages—answer the
questions in [Choosing an origination identity
for one-way messaging use cases](#phone-number-types-choosing-oneway "#phone-number-types-choosing-oneway") instead.

If you plan to receive incoming SMS messages, you must have a dedicated phone number.
There are different types of dedicated phone numbers depending on the country where your
customers are located.

Answer the following questions to determine the right type of origination identity for
your needs. If you have recipients in multiple countries, answer these questions for
each country that your recipients are located in.

1. Is two-way messaging supported in the country that
   you plan to send messages to? For a full list of countries that support two-way
   messaging, see [Supported countries and regions
   for SMS](phone-numbers-sms-by-country.md "phone-numbers-sms-by-country.md").
   - If you answered **Yes**, proceed to [question 2](#two-way-q2 "#two-way-q2").
   - If you answered **No**, your two-way
     messaging use case isn't supported, but you can still send one-way
     messages. To find an origination ID for sending one-way messages, see
     [Choosing an origination identity
     for one-way messaging use cases](#phone-number-types-choosing-oneway "#phone-number-types-choosing-oneway").

2. Are you planning to send messages to recipients in
   the United States?
   - If you answered **Yes**, proceed to [question 3](#two-way-q3 "#two-way-q3").
   - If you answered **No**, proceed to [question 4](#two-way-q3 "#two-way-q3").

3. Which of the following throughput rates best fits
   your requirements? Your throughput rate is the number of message parts that you
   can send each second.
   - **1–3 message parts per second**:
     Use a toll-free number. You can also use 10DLC numbers or short codes.
     These number types will provide plenty of room for growth, but will also
     cost more and take longer to obtain.

   For more information about requesting a toll-free number, see [Request a phone number](phone-numbers-request.md "phone-numbers-request.md").

   If you want to determine what kind of origination number to use for
   another country, return to [question 1](#two-way-q1 "#two-way-q1").
   Otherwise, **stop here**.
   - **10–75 message parts per second**:
     Use a 10DLC number. A short code will also work for your use case, and
     will provide additional room for growth, but it will also cost
     more.

   For more information about setting up 10DLC, see [United States 10DLC registration](registrations-10dlc.md "registrations-10dlc.md").

   If you want to determine what kind of origination number to use for
   another country, return to [question 1](#two-way-q1 "#two-way-q1").
   Otherwise, **stop here**.
   - **100 message parts per second or more**:
     Use a short code. When you create your request in the
     AWS Support Center Console, specify the throughput rate that you want your
     short code to support. US short codes support 100 message parts per
     second by default, but the throughput rate can be increased beyond that
     rate for an additional monthly fee.

   For more information about requesting a short code, see [Requesting dedicated short codes](phone-numbers-request-short-code.md "phone-numbers-request-short-code.md").

   If you want to determine what kind of origination number to use for
   another country, return to [question 1](#two-way-q1 "#two-way-q1").
   Otherwise, **stop here**.

4. Are dedicated short codes available in the country
   that you plan to send messages to? For a list of countries where short codes are
   available, see [Supported countries and regions for SMS
   messaging with AWS End User Messaging SMS](phone-numbers-sms-by-country.md "phone-numbers-sms-by-country.md").
   - If you answered **Yes**, use a dedicated
     short code. For more information about requesting a short code, see
     [Requesting dedicated short codes](phone-numbers-request-short-code.md "phone-numbers-request-short-code.md").

   If you want to determine what kind of origination number to use for
   another country, return to [question 1](#two-way-q1 "#two-way-q1").
   Otherwise, **stop here**.
   - If you answered **No**, use a dedicated
     long code. For more information about requesting dedicated SMS long
     codes, see [Requesting dedicated long codes](phone-numbers-request-long-code.md "phone-numbers-request-long-code.md").

   ###### Note

   If both dedicated short codes and dedicated long codes are
   available in the destination country, you should use a dedicated
   short code. Mobile carriers are more likely to block or limit the
   messages that are sent from long codes if short codes are also
   available.

   If you want to determine what kind of origination number to use for
   another country, return to [question 1](#two-way-q1 "#two-way-q1").
   Otherwise, **stop here**.
