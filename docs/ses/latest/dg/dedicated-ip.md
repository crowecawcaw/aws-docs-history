# Dedicated IP addresses for Amazon SES

When you create a new Amazon SES account, by default your emails are sent from IP addresses
that are shared with other SES users.
You can also use dedicated IP addresses that are
reserved for your exclusive use by leasing them for
[an additional cost](https://aws.amazon.com/ses/pricing "https://aws.amazon.com/ses/pricing"). This
gives you complete control over your sender reputation and enables you to isolate your
reputation for different segments within email programs. Amazon SES offers two ways to provision
and manage a dedicated IP address:

- Standard—refers to dedicated IP addresses
  that you manually set up and manage, including the option to manually warm them up
  and scale them out, and to manually move them in and out of IP pools. (These were
  formerly referred to as _dedicated IP addresses_ in SES.)
- Managed—refers to dedicated IP addresses that
  are automatically set up on your behalf by SES to provide a quick and easy
  way to start using dedicated IP addresses that are managed by SES; they
  automatically warm up for each ISP individually and auto-scale based on your sending
  volume to help ensure that your dedicated IP addresses are used optimally based on
  how you send email.
  When deciding between shared IP addresses or the two types of dedicated IP addresses
  defined above, choose the one that provides the most benefits for the type, volume, and
  patterns of email that you send. To help you make your decision, these benefits are
  summarized in the following table. Choose an item in the **Benefit** column
  for additional information.

| Benefit                                                                                                                                 | Shared IP addresses | Dedicated IP addresses (standard) | Dedicated IP addresses (managed) |
| --------------------------------------------------------------------------------------------------------------------------------------- | ------------------- | --------------------------------- | -------------------------------- |
| [Ready to use<br>immediately](#dedicated-ip-simplicity "#dedicated-ip-simplicity")                                                      | Yes                 | No                                | No                               |
| [Additional setup<br>required](#dedicated-ip-simplicity "#dedicated-ip-simplicity")                                                     | No                  | Yes                               | Yes                              |
| [IP addresses &<br>reputation isolated from other SES customers](#dedicated-ip-managed-reputation "#dedicated-ip-managed-reputation")   | No                  | Yes                               | Yes                              |
| [Capacity increases<br>automatically as traffic increases](#dedicated-ip-sending-patterns "#dedicated-ip-sending-patterns")             | No                  | No                                | Yes                              |
| [Good for customers with<br>continuous, predictable sending patterns](#dedicated-ip-sending-patterns "#dedicated-ip-sending-patterns")  | Yes                 | Yes                               | Yes                              |
| [Good for customers with<br>less predictable sending patterns](#dedicated-ip-sending-patterns "#dedicated-ip-sending-patterns")         | Yes                 | No                                | Yes                              |
| [Good for high-volume<br>senders](#dedicated-ip-sending-volumes "#dedicated-ip-sending-volumes")                                        | Yes                 | Yes                               | Yes                              |
| [Good for low-volume<br>senders](#dedicated-ip-sending-volumes "#dedicated-ip-sending-volumes")                                         | Yes                 | No                                | No                               |
| [Additional monthly<br>costs](#dedicated-ip-costs "#dedicated-ip-costs")                                                                | No                  | Yes                               | Yes                              |
| [Complete control over<br>sender reputation](#dedicated-ip-reputation-control "#dedicated-ip-reputation-control")                       | No                  | Yes                               | Yes                              |
| [Isolate reputation by<br>email type, recipient, or other factors](#dedicated-ip-isolate-reputation "#dedicated-ip-isolate-reputation") | No                  | Yes                               | Yes                              |
| [Provides known IP addresses<br>that never change](#dedicated-ip-known-addresses "#dedicated-ip-known-addresses")                       | No                  | Yes                               | No                               |

###### Important

If you don't plan to send large volumes of email on a regular and predictable basis,
we recommend that you use shared IP addresses. If you want to use dedicated IP addresses
in situations where your sending
patterns are highly
irregular, using
_Dedicated IPs (managed)_ is the better option.

## Ease of setup

Shared IP addresses—you don't need to perform any
additional configuration. Your SES account is ready to send email as soon as you
verify an email address and move out of the sandbox.

Dedicated IP addresses (standard)—you must [submit a request](dedicated-ip-case.md "dedicated-ip-case.md") through the AWS Support Center
and optionally [configure dedicated IP
pools](dedicated-ip-pools.md "dedicated-ip-pools.md").

Dedicated IP addresses (managed)—you don’t need to submit a request
for dedicated IP addresses. They'll automatically be allocated when you opt in and do a
one-time walkthrough to create your managed dedicated pool.

## Reputation management

IP address reputations are based largely on historical sending patterns and volume. An
IP address that sends consistent volumes of email over a long period of time typically
has a good reputation.

Shared IP addresses—shared between several
SES customers, these addresses collectively send a large volume of email and
AWS carefully manages the outbound traffic to maximize the reputations of the shared
IP addresses.

Dedicated IP addresses (standard)—after warmup, your IP addresses are
isolated from the SES shared pool and you maintain your own sender reputation by
sending consistent and predictable volumes of email.

###### Note

For information about Smart Network Data Services (SNDS) data for your dedicated IPs (standard),
see [SNDS metrics for dedicated IPs](snds-metrics-dedicated-ips.md "snds-metrics-dedicated-ips.md").

Dedicated IP addresses (managed)—after warmup of your new IPs, they're
isolated from the SES shared pool and you maintain your own sender reputation.
There's the added benefit of tracking the reputation for each ISP and optimally
scheduling outgoing sending accordingly. So while you still maintain your sender
reputation, this automation helps to improve overall deliverability and reduce bounce
rates when compared to equivalent workloads on manually configured dedicated IP
addresses.

## Predictability of sending

patterns

An IP address with a consistent history of sending email has a better reputation than
one that suddenly starts sending out large volumes of email with no prior sending
history.

Shared IP addresses—good for email sending
patterns that don't follow a predictable pattern. With shared IP addresses, you can
increase or decrease your email sending patterns as the situation demands.

Dedicated IP addresses (standard)—you must warm up addresses by
sending an amount of email that gradually increases every day. The process of warming up
new IP addresses is described in [Warming up dedicated IP addresses (standard)](dedicated-ip-warming.md "dedicated-ip-warming.md"). After your dedicated IP addresses are warmed
up, you must then maintain a consistent sending pattern.

Dedicated IP addresses (managed)—your dedicated IP addresses are
warmed up automatically for each IP in the managed pool by using an adaptive warmup
strategy (in conjunction with the SES shared pool) that takes into account actual
sending patterns to optimize the warmup for each ISP individually. The managed IP pool
automatically scales out per ISP based on usage and consideration of ISP-specific
policies.

## Volume of outbound email

Shared IP addresses —best for customers who send
low volumes of email.

Dedicated IP addresses (standard) | Dedicated IP addresses (managed)—both are suited for
customers who send large volumes of email. Most ISPs only track the reputation of a
given IP address if they receive a significant volume of mail from that address. For
each ISP with which you want to cultivate a reputation, you should send several hundred
emails within a 24-hour period at least once per month. In some cases, both types of
dedicated IP addresses may also work for smaller volumes of email. For example, they may
work well if you send to a small, well-defined group of recipients whose mail servers
accept or reject email using a list of specific IP addresses, rather than IP address
reputation.

## Additional costs

Shared IP addresses—included in the standard
SES pricing.

Dedicated IP addresses (standard)—are available for an additional
monthly fee per IP address that you lease. For pricing information, see
the [SES pricing page](https://aws.amazon.com/ses/pricing/ "https://aws.amazon.com/ses/pricing/").

Dedicated IP addresses (managed)—are available for a standard monthly
fee (regardless of the amount of IPs needed) and a per message usage charge. For pricing
information, see the [SES pricing
page](https://aws.amazon.com/ses/pricing/ "https://aws.amazon.com/ses/pricing/").

## Control over sender reputation

Shared IP addresses—your sender reputation is
controlled by SES.

Dedicated IP addresses (standard) | Dedicated IP addresses (managed)—your sender reputation
is completely under your control. Your SES account is the only one that is able
to send email from those addresses. For this reason, the sender reputation is determined
by your email sending practices. Additionally, dedicated IPs (managed) actively
monitors outbound IP addresses used for email sending by using the highest performing IP
addresses to improve email deliverability to your recipients. Utilization data can be
surfaced by using additional services such as Amazon CloudWatch metrics and the built-in
dashboards that are in Amazon SES.

## Ability to isolate sender

reputation

Shared IP addresses—your sender reputation is set
at the account level and can't be isolated.

Dedicated IP addresses (standard) | Dedicated IP addresses (managed)—you can isolate your
sender reputation for different components within your email program
by creating _dedicated IP
pools_—groups of dedicated IP addresses that can be used for sending
specific types of email. For example, you can create one pool of dedicated IP addresses
for sending marketing email, and another for sending transactional email.

## Known, unchanging IP addresses

Shared IP addresses—you don't know the IP
addresses that SES uses to send your mail, and they can change at any
time.

Dedicated IP addresses (standard)—you can find the values of the
addresses that send your mail in the **Dedicated IPs** page of the
SES console. This is because dedicated IP addresses are static.

Dedicated IP addresses (managed)—SES will automatically
configure the optimal number of dedicated IP addresses based on your sending patterns.
While SES manages the automatic scaling of your IP pool, you can view all
dedicated IP addresses currently allocated to your account through the SES
console or API. The number of IPs in your pool will continue to dynamically increase or
decrease based upon your sending demand.
