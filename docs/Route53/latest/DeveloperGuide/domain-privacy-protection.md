# Enabling or disabling privacy protection for

contact information for a domain

When you register a domain with Amazon Route 53 or transfer a domain to Route 53, we enable
privacy protection by default for all the contacts for the domain. This typically hides
most of your contact information from WHOIS ("Who is") queries and reduces the amount of
spam that you receive. When you enable privacy protection, your contact information is
replaced with contact information for the registrar or with the phrase "REDACTED FOR
PRIVACY", or "On behalf of <domain name> owner."

If you choose to disable privacy protection, you must disable it for all contacts for
a domain. If you do disable privacy protection, anyone can send a WHOIS query for the
domain and, for most top-level domains (TLDs), might be able to get all the contact
information that you provided when you registered or transferred the domain, including
name, address, phone number, and email address. The WHOIS command is widely available;
it's included in many operating systems, and it's also available as a web application on
many websites.

If you are transferring a domain to another registrar, and privacy protection is
enabled for the domain contacts, the email to verify the transfer will be delivered from
identity-protect.org addresses for TLDs registered with Amazon Registrar. To determine
who the registrar is for your TLD, see [Finding your registrar](find-your-registrar.md "find-your-registrar.md").

The information that you can hide from WHOIS queries depends on two main
factors:

**The registry for the top level domain**

Most TLD registries hide all contact information automatically, some allow
you to choose to hide all contact information, some allow you to hide only
some information, and some do not allow you to hide any information.
**Some TLD registries intentionally suppress
privacy protection to comply with local regulations or registry
policies.**

When privacy protection on a domain is enabled, your contact information
is replaced either with contact information for the privacy protection
service, or with the phrase "REDACTED FOR PRIVACY." The privacy protection
service applies spam prevention features (address rotation and SPF/DKIM/spam
analysis) and will, in most cases, automatically forward emails passing
these filters. However, it is not advisable to send critical emails to
privacy protected email addresses because the spam mechanism might prevent
them from being forwarded.

Additionally, the choice of which privacy protection mechanism is used for
a domain is not configurable and is auto-selected by the system. The contact
detail for our privacy protection service can't be manually updated.

###### Note

To enable or disable privacy protection for some domains, you must
open a support case and request privacy protection. For more
information, see the applicable section in [Domains that you can register with Amazon Route 53](registrar-tld-list.md "registrar-tld-list.md"):

- [.co.uk (United Kingdom)](registrar-tld-list.md#registrar-tld-list#co.uk "registrar-tld-list.md#registrar-tld-list#co.uk")
- [.me.uk (United Kingdom)](registrar-tld-list.md#registrar-tld-list#me.uk "registrar-tld-list.md#registrar-tld-list#me.uk")
- [.org.uk (United Kingdom)](registrar-tld-list.md#registrar-tld-list#org.uk "registrar-tld-list.md#registrar-tld-list#org.uk")
- [.link](registrar-tld-list.md#registrar-tld-list#link "registrar-tld-list.md#registrar-tld-list#link")

**The registrar**

When you register a domain with Route 53 or transfer a domain to Route 53, the
registrar for the domain is either Amazon Registrar or our registrar
associate, Gandi. Amazon Registrar and Gandi hide different information by
default:

- **Amazon Registrar** – By
  default, all of your contact information is hidden. However,
  regulations for the TLD registry take precedence.
- **Gandi** – By default, all of
  your contact information is hidden except organization name, if any.
  However, regulations for the TLD registry take precedence.

For [geographic TLDs](registrar-tld-list.md#registrar-tld-list-geographic "registrar-tld-list.md#registrar-tld-list-geographic") that don't allow privacy protection,
your personal information will be marked as "redacted" on the [Whois Directory Search](https://v4.gandi.net/whois "https://v4.gandi.net/whois")
page on the Gandi website. However, your personal information might
be available at the domain registry or on third-party WHOIS
websites.

To find out what information is hidden for the TLD for your domain, see [Domains that you can register with Amazon Route 53](registrar-tld-list.md "registrar-tld-list.md").

When you want to enable or disable privacy protection for a domain that you registered
using Route 53, perform the following procedure.

###### Important

**Privacy protection availability:** Privacy
protection is not available for all TLDs. Common TLDs that don't support privacy
protection include .de, .us, .com.au, .es, and several others.

If you don't see a "Privacy protection" section when editing your domain's
contact information, privacy protection is not supported for your domain's TLD.

For a complete list of TLDs that don't support privacy protection, see [TLDs that don't support privacy
protection](privacy-protection-tld-support.md "privacy-protection-tld-support.md"). For detailed information
about privacy protection support for any TLD, see [Domains that you can register with Amazon Route 53](registrar-tld-list.md "registrar-tld-list.md").

###### To enable or disable privacy

protection for contact information for a domain

1. Sign in to the AWS Management Console and open the Route 53 console at
   [https://console.aws.amazon.com/route53/](https://console.aws.amazon.com/route53/ "https://console.aws.amazon.com/route53/").
2. In the navigation pane, choose **Registered domains**.
3. Choose the name of the domain that you want to enable or disable privacy
   protection for.
4. In the **Contact information** section, choose
   **Edit**.
5. In the **Privacy protection** section, choose whether to hide
   contact information. You must specify the same privacy setting for all four
   contacts: admin, registrant, technical, and billing.

###### Note

If the **Privacy protection** section is not displayed,
privacy protection is not supported for your domain's TLD. Your contact
information will be publicly visible in WHOIS queries for domains that don't
support privacy protection. 6. Choose **Save changes**. 7. If you encounter issues while enabling or disabling privacy protection, you
can contact AWS Support for free. For more information, see [Contacting AWS Support about domain registration issues](domain-contact-support.md "domain-contact-support.md").
