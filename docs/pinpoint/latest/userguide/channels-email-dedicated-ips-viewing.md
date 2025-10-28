**End of support notice:** On October
30, 2026, AWS will end support for Amazon Pinpoint. After October 30, 2026, you will no
longer be able to access the Amazon Pinpoint console or Amazon Pinpoint resources (endpoints,
segments, campaigns, journeys, and analytics). For more information, see [Amazon Pinpoint end of
support](../../../console/pinpoint/migration-guide.md "../../../console/pinpoint/migration-guide.md"). **Note:** APIs related to SMS, voice,
mobile push, OTP, and phone number validate are not impacted by this change and are
supported by AWS End User Messaging.

# Viewing a list of dedicated IP

addresses that are associated with your account

You can view a list of dedicated IP addresses that are associated with your Amazon Pinpoint account
in the current AWS Region. These IP addresses are available for use with both Amazon Pinpoint and
Amazon Simple Email Service (Amazon SES).

You can also use the Amazon Pinpoint console to quickly determine if any of your dedicated IP
addresses have been listed on Domain Name System-based Blackhole Lists
(_DNSBLs_). DNSBLs are also called _Realtime Blackhole
Lists_ (_RBLs_), _deny lists_,
_blocklists_, or _blacklists_). DNSBLs are lists
of IP addresses that are suspected of sending spam, malicious content, or other unsolicited
messages. Different DNSBLs have different impacts on email deliverability. The lists offered
by Spamhaus have the most serious impact on email delivery.

###### To view a list of dedicated IPs in your account

1. Open the Amazon Pinpoint console at
   [https://console.aws.amazon.com/pinpoint/](https://console.aws.amazon.com/pinpoint/ "https://console.aws.amazon.com/pinpoint/").
2. In the navigation pane, under **Email**, choose
   **Dedicated IPs**.

The list of IP addresses also includes the following information:

**Listing date**

If the IP address is currently listed on a DNSBL, this field shows the
date when it was most recently added.

**Reputation**

A description of the health of the IP address.

**Blacklist name**

If the IP address is currently listed on a DNSBL, this field shows the
name of the list that it's listed on.

**Blacklist reason**

If the IP address is currently listed on a DNSBL, this field displays
the reason that the address was added to the list. This text is provided
by the list providers themselves. Some providers offer detailed
explanations, while others offer generic information.
