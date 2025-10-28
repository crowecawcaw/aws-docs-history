# Authenticating Email with SPF in

Amazon SES

_Sender Policy Framework_ (SPF) is an email validation standard that's
designed to prevent email spoofing. Domain owners use SPF to tell email providers which
servers are allowed to send email from their domains. SPF is defined in [RFC 7208](https://tools.ietf.org/html/rfc7208 "https://tools.ietf.org/html/rfc7208").

Messages that you send through Amazon SES automatically use a subdomain of
`amazonses.com` as the default MAIL FROM domain. SPF authentication
successfully validates these messages because the default MAIL FROM domain matches the
application that sent the email—in this case, SES. Therefore, in SES,
SPF is implicitly set up for you.

However, if you don't want to use the SES default MAIL FROM domain, and would
rather use a subdomain of a domain that you own, this is referred to in SES as using
a _custom_ MAIL FROM domain. To do this, it requires you to publish your
own SPF record for your custom MAIL FROM domain. In addition,
SES also requires you to set up an MX record so that your custom MAIL FROM domain can
receive the bounce and complaint notifications that email providers send you.

###### Learn how to set up SPF authentication

Instructions are given for configuring your domain with SPF and how to publish the MX
and SPF (type TXT) records in [Using a custom MAIL FROM domain](mail-from.md "mail-from.md").
