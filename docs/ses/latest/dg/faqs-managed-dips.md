# Dedicated IP addresses (managed) FAQs

While [Dedicated IP addresses (managed)](managed-dedicated-sending.md "managed-dedicated-sending.md") offers numerous automated features for
dedicated IP management, scaling, and warmup, there has been some misunderstanding about the
extent of this automation and SES' responsibilities. It would be incorrect to assume
that "managed" means SES completely handles all aspects of IP reputation and listing
issues. To clarify these misconceptions, we need to emphasize that while the service
automates technical aspects like scaling and warmup, you remain responsible for maintaining
your sending reputation and managing any reputation related issues such as getting listed in
a Reputation Block List (RBL).

These FAQs address common misconceptions about the feature's scope and clarify the shared
responsibility model between you and SES.
These FAQS highlight that while the "managed" aspect refers to technical infrastructure
management, you must still actively monitor and maintain your sending reputation, keep
bounce rates low, and handle most RBL delisting requests yourself.

## Q1. Can I ask SES to remove my dedicated IP address (managed) from

being listed in an RBL?

If your dedicated IP address (managed) is listed in any
RBL of recipient mail providers, it is not the responsibility of SES
and you must request removal yourself directly to the RBL administrator. It's important
to monitor your dedicated IPs (managed) by tracking both bounce notifications and SMTP response
messages to identify blocks. This monitoring helps protect your email sending reputation
and allows you to quickly address any RBL incidents that may occur, ensuring consistent
email deliverability.

## Q2. Can I ask SES to allocate a new dedicated IP address (managed)

to replace a current one that is listed in an RBL that is not offered by
Spamhaus?

No. SES does not rotate dedicated IP addresses. As you are responsible for your
dedicated IP addresses, managed or standard, you need to figure out why they are getting
listed in the RBL and get them delisted yourself.

## Q3. Can SES monitor the bounce rate of a

dedicated IP address (managed) assigned to my account and rotate the address when the bounce rate
becomes high?

No. SES does not rotate dedicated IP addresses when an account experiences a
high bounce rate. When you lease a dedicated IP address (managed), only your account has exclusive rights to
send email through that dedicated IP address, thus SES cannot monitor your
account. It is [your responsibility to
manage your sender reputation](dedicated-ip.md#dedicated-ip-reputation-control "dedicated-ip.md#dedicated-ip-reputation-control") and email components, including managing
complaints and maintaining a [bounce rate below 2%](faqs-enforcement.md#bn-q4 "faqs-enforcement.md#bn-q4").

## Q4. I just leased a dedicated IP address (managed) and the email sent

through it is bouncing because the address is on an RBL. Does SES check the
reputation of an dedicated IP address (managed) before leasing it to an account?

Yes. SES does reset any dedicated IP address (managed) (30 days) before leasing it to an SES
account. The reputation typically resets to most major providers. SES makes sure
that the address is not on any RBL, like Spamhaus; however, SES does not monitor
all RBLs available, such as smaller, regional RBLs. If you have any concerns about an
RBL due to B2B focus or a regional provider focus that uses those domains, you would
need to review the reputation state of the dedicated IP address (managed) yourself.

## Q5. If SES does not take action when dedicated IP addresses (managed)

get listed in an RBL, other than Spamhus, why should I use them?

Dedicated IP addresses (managed) are managed in terms of auto-scaling by adding and removing IP addresses
based on traffic. Also, it saves you time in terms of [per-ISP warm-up](managed-dedicated-sending.md#intel-warmup "managed-dedicated-sending.md#intel-warmup") management; thus, a managed pool keeps track of how many
emails can go out through every IP address based on historic sending patterns. More
benefits can be found in [Benefits and features of dedicated IPs (managed)](managed-dedicated-sending.md#dedicated-ip-benefits-mds "managed-dedicated-sending.md#dedicated-ip-benefits-mds").

## Q6. How can I track dedicated IP addresses (managed) leased to my

account?

You can use an SES configuration set with an [event publishing destination](event-destinations-manage.md#event-destination-add "event-destinations-manage.md#event-destination-add") defined for
either a Amazon Data Firehose or an Amazon SNS topic. SES delivery events include the tag [ses:outgoing-ip](event-publishing-retrieving-sns-examples.md#event-publishing-retrieving-sns-delivery "event-publishing-retrieving-sns-examples.md#event-publishing-retrieving-sns-delivery"). Thus, if an email was bounced due to the
reputation of a dedicated IP address (managed), you can find the offending dedicated IP address (managed) in the bounce event's
`ses:outgoing-ip` tag.
