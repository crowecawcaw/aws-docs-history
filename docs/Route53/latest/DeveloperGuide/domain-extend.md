# Extending the registration period for a domain

When you register a domain with Amazon Route 53 or you transfer domain registration to
Route 53, we configure the domain to renew automatically. The automatic renewal period is
typically one year, although the registries for some top-level domains (TLDs) have
longer renewal periods.

Note the following:

**Maximum renewal period**

All generic TLDs and many country-code TLDs let you extend domain
registration for longer periods, typically up to ten years in one-year
increments. To determine whether you can extend the registration period for
your domain, see [Domains that you can register with Amazon Route 53](registrar-tld-list.md "registrar-tld-list.md"). If longer registration periods are
allowed, perform the following procedure.

**Restrictions on when you can renew or extend a domain registration**

Some TLD registries have restrictions on when you can renew or extend a
domain registration, for example, the last two months before the domain
expires. Even if the registry allows extending the registration period for a
domain, they might not allow it at the current number of days before the
domain expires.

###### Note

For example, if the maximum allowable renewal period is 5 years for
the TLDs that you have your domain with, you can add yearly renewals at
any time until you reach the 5-year limit. More specifically, if you
have a domain that currently has 2.5 years of validity, you can only
renew it for up to 2 more years.

**AWS credits**

You can't use AWS credits to pay the fee for extending the registration
period for a domain.

###### To extend the registration period for your

domain

1. Open the Route 53 console at
   [https://console.aws.amazon.com/route53/](https://console.aws.amazon.com/route53/ "https://console.aws.amazon.com/route53/").
2. In the navigation pane, choose **Registered Domains**.
3. Choose the name of the domain for which you want to extend the registration
   period.
4. In the **Details** section, in the
   **Actions** dropdown choose **Renew domain
   registration**.
5. In the **Renew domain registrations** dialog box, in the
   **Renewal period** dropdown, choose the number of years
   that you want to extend the registration for.

The list shows all the current options based on the current expiration date
and the maximum registration period allowed by the registry for this domain. The
expiration date with that number of years applied is listed under the
duration. 6. Choose **Renew domain registration**.

When we receive confirmation from the registry that they've updated your
expiration date, we send you an email to confirm that we've changed the
expiration date. 7. If you encounter issues while extending the registration period for a domain,
you can contact AWS Support for free. For more information, see [Contacting AWS Support about domain registration issues](domain-contact-support.md "domain-contact-support.md").
