**End of support notice:** On October
30, 2026, AWS will end support for Amazon Pinpoint. After October 30, 2026, you will no
longer be able to access the Amazon Pinpoint console or Amazon Pinpoint resources (endpoints,
segments, campaigns, journeys, and analytics). For more information, see [Amazon Pinpoint end of
support](../../../console/pinpoint/migration-guide.md "../../../console/pinpoint/migration-guide.md"). **Note:** APIs related to SMS, voice,
mobile push, OTP, and phone number validate are not impacted by this change and are
supported by AWS End User Messaging.

# Using dedicated IP addresses with

Amazon Pinpoint

When you create a new Amazon Pinpoint account, your emails are sent from IP addresses that are
shared with other Amazon Pinpoint users. For [an additional monthly
charge](https://aws.amazon.com/pinpoint/pricing/#Dedicated_IP_Addresses "https://aws.amazon.com/pinpoint/pricing/#Dedicated_IP_Addresses"), you can lease dedicated IP addresses that are reserved for your
exclusive use. Both of these options offer unique benefits and drawbacks, which are
summarized in the following table.

| Benefit                                                                                                                                                                  | Shared IP addresses | Dedicated IP addresses |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------- | ---------------------- |
| [Ready to use with<br>no additional setup](#channels-email-dedicated-ips-simplicity "#channels-email-dedicated-ips-simplicity")                                          | Yes                 | No                     |
| [Reputation managed by AWS](#channels-email-dedicated-ips-managed-reputation "#channels-email-dedicated-ips-managed-reputation")                                         | Yes                 | No                     |
| [Good for<br>customers with continuous, predictable sending patterns](#channels-email-dedicated-ips-sending-patterns "#channels-email-dedicated-ips-sending-patterns")   | Yes                 | Yes                    |
| [Good for<br>customers with less predictable sending patterns](#channels-email-dedicated-ips-sending-patterns "#channels-email-dedicated-ips-sending-patterns")          | Yes                 | No                     |
| [Good for<br>high-volume senders](#channels-email-dedicated-ips-sending-volumes "#channels-email-dedicated-ips-sending-volumes")                                         | Yes                 | Yes                    |
| [Good for<br>low-volume senders](#channels-email-dedicated-ips-sending-volumes "#channels-email-dedicated-ips-sending-volumes")                                          | Yes                 | No                     |
| [Additional monthly<br>costs](#channels-email-dedicated-ips-costs "#channels-email-dedicated-ips-costs")                                                                 | No                  | Yes                    |
| [Complete<br>control over sender reputation](#channels-email-dedicated-ips-reputation-control "#channels-email-dedicated-ips-reputation-control")                        | No                  | Yes                    |
| [Isolates<br>reputation by email type, recipient, or other factors](#channels-email-dedicated-ips-isolate-reputation "#channels-email-dedicated-ips-isolate-reputation") | No                  | Yes                    |
| [Provides<br>known IP addresses that never change](#channels-email-dedicated-ips-known-addresses "#channels-email-dedicated-ips-known-addresses")                        | No                  | Yes                    |

###### Important

If you don't plan to send large volumes of email on a regular and predictable basis,
we recommend that you use shared IP addresses. If you use dedicated IP addresses in use
cases that involve sending low volumes of email, or if your sending patterns are highly
irregular, you might experience deliverability issues.

## Ease of setup

If you choose to use shared IP addresses, then you don't need to perform any
additional configuration. Your Amazon Pinpoint account is ready to send emails as soon as you
verify an email address and move out of the sandbox.

If you choose to lease dedicated IP addresses, you have to determine how many
dedicated IP addresses you need, submit a request, and optionally [create dedicated IP
pools](channels-email-dedicated-ips-pools.md "channels-email-dedicated-ips-pools.md").

## Reputation managed by

AWS

IP address reputations are based largely on historical sending patterns and volume. An
IP address that sends consistent volumes of email over a long period of time usually has
a good reputation.

Shared IP addresses are used by several Amazon Pinpoint customers. Together, these customers
send a large volume of email. AWS carefully manages this outbound traffic in order to
maximize the reputations of the shared IP addresses.

If you use dedicated IP addresses, it's your responsibility to maintain your sender
reputation by sending consistent and predictable volumes of email.

## Predictability of

sending patterns

An IP address with a consistent history of sending email has a better reputation than
one that suddenly starts sending out large volumes of email with no prior sending
history.

If your email sending patterns are irregular (they don't follow a predictable
pattern), then shared IP addresses are a better fit for your needs. When you use shared
IP addresses, you can increase or decrease your email-sending patterns as the situation
demands.

If you use dedicated IP addresses, you have to warm up those addresses by sending an
amount of email that gradually increases every day. The process of warming up new IP
addresses is described in [Warming up dedicated IP
addresses](channels-email-dedicated-ips-warming.md "channels-email-dedicated-ips-warming.md"). After your dedicated IP
addresses are warmed up, you must then maintain a consistent sending pattern.

## Volume of outbound

email

Dedicated IP addresses are more appropriately suited for customers who send large
volumes of email. Most internet service providers (ISPs) only track the reputation of a
given IP address if they receive a significant volume of mail from that address. For
each ISP with which you want to cultivate a reputation, you should send several hundred
emails within a 24-hour period at least once per month.

In some cases, you might be able to use dedicated IP addresses if you don't send large
volumes of email. For example, dedicated IP addresses might work well if you send to a
small, well-defined group of recipients whose mail servers accept or reject email using
a list of specific IP addresses, rather than IP address reputation.

## Additional costs

The use of shared IP addresses is included in the standard Amazon Pinpoint pricing. Leasing
dedicated IP addresses incurs an extra monthly cost beyond the standard costs that are
associated with sending email using Amazon Pinpoint. Each dedicated IP address incurs a separate
monthly charge. For pricing information, see the [Amazon Pinpoint pricing page](https://aws.amazon.com/pinpoint/pricing/ "https://aws.amazon.com/pinpoint/pricing/").

## Control over sender

reputation

When you use dedicated IP addresses, your Amazon Pinpoint account is the only one that is able
to send email from those addresses. For this reason, the sender reputation of the
dedicated IP addresses that you lease is determined by your email-sending
practices.

## Ability to isolate

sender reputation

By using dedicated IP addresses, you can isolate your sender reputation for different
components of your email program. If you lease more than one dedicated IP address for
use with Amazon Pinpoint, you can create _dedicated IP
pools_—groups of dedicated IP addresses that can be used for sending
specific types of email. For example, you can create one pool of dedicated IP addresses
for sending marketing email, and another for sending transactional email. To learn more,
see [Creating dedicated IP pools](channels-email-dedicated-ips-pools.md "channels-email-dedicated-ips-pools.md").

## Known, unchanging IP

addresses

When you use dedicated IP addresses, you can find the values of the addresses that
send your mail in the **Dedicated IPs** page of the Amazon Pinpoint console.
Dedicated IP addresses don't change.

With shared IP addresses, you don't know the IP addresses that Amazon Pinpoint uses to send your
mail, and they can change at any time.
