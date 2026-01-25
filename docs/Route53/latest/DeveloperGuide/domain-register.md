# Registering a new domain

###### Register a new domain or update name servers for an existing domain

You can use Amazon Route 53 with domains you register with Route 53, and with domains you have
registered with other DNS providers. Depending on your DNS provider, choose one
of the following procedures to register and use a new domain with Route 53:

- For registering a new domain, see [To register a new domain using Route 53](#domain-register-procedure-section "#domain-register-procedure-section").
- For an existing domain, see [Making Amazon Route 53 the DNS service for an existing domain](MigratingDNS.md "MigratingDNS.md").
- For moving a domain to another registrar, see [update name servers when you
  want to use another DNS service](domain-register-other-dns-service.md "domain-register-other-dns-service.md").

###### Considerations for domain registration

Before you start, note the following:

**Contacting AWS Support**
If you encounter issues while registering a domain, you can contact AWS Support for free. For more information, see
[Contacting AWS Support about domain registration issues](domain-contact-support.md "domain-contact-support.md").

**Domain registration pricing**
For information about the cost to register domains, see
[Amazon Route 53 Pricing for Domain Registration](https://d32ze2gidvkk54.cloudfront.net/Amazon_Route_53_Domain_Registration_Pricing_20140731.pdf "https://d32ze2gidvkk54.cloudfront.net/Amazon_Route_53_Domain_Registration_Pricing_20140731.pdf").

**Supported domains**
For a list of supported TLDs, see [Domains that you can register with Amazon Route 53](registrar-tld-list.md "registrar-tld-list.md").

**You can't change a domain name after you register it**
If you accidentally register the wrong domain name, you can't change it. Instead, you need to register another
domain name and specify the correct name. You also can't get a refund for a domain name that you registered accidentally.

**AWS credits**
You can't use AWS credits to pay the fee for registering a new domain with Route 53.

**Special or premium prices**
TLD registries have assigned special or premium prices to some domain names. You can't use Route 53 to
register a domain that has a special or premium price.

**Charges for hosted zones**
When you register a domain with Route 53, we automatically create a hosted zone for the domain and
charge a small monthly fee for the hosted zone in addition to the annual charge for the domain registration.
This hosted zone is where you store information about how to route traffic for your domain, for example, to an
Amazon EC2 instance or a CloudFront distribution. If you don't want to use your domain right now, you can delete the hosted zone;
if you delete it within 12 hours of registering the domain, there won't be any charge for the hosted zone on your
AWS bill. We also charge a small fee for the DNS queries that we receive for your domain. For more information, see
[Amazon Route 53 Pricing](https://aws.amazon.com/route53/pricing/ "https://aws.amazon.com/route53/pricing/").

**Replacing the hosted zone for a domain**
If you create a new hosted zone for a domain, you must also update the name servers for the
domain to use the same name servers as the new hosted zone. For details
see, [Replacing the hosted zone for a domain that is registered with Route 53](domain-replace-hosted-zone.md "domain-replace-hosted-zone.md")

## To register a new domain using Route 53

###### To register a new domain using Route 53

1.  Sign in to the AWS Management Console and open the Route 53 console at
    [https://console.aws.amazon.com/route53/](https://console.aws.amazon.com/route53/ "https://console.aws.amazon.com/route53/").
2.  In the navigation pane, choose **Domains** and then **Registered domains**.
3.  On the **Registered domains** page, choose **Register domains**.
    1. In the **Search for domain** section, enter the domain name that you want to register, and choose **Search** to find out whether the domain
       name is available.

    If the domain name that you want to register contains characters other than a-z, A-Z, 0-9, and - (hyphen),
    note the following:

        * You can enter the name using the applicable characters. You don't need to convert the name
         to Punycode.
        * A list of languages appears. Choose the language of the specified name. For example,
         if you enter příklad ("example" in Czech), choose Czech (CES) or Czech (CZE).


        ###### Note

        For languages that have more than one code, you might need to try both of them.
         Even though CES and CZE are synonymous, some TLD registries support only one or the other.


        For information about how to specify characters other than a-z, 0-9, and - (hyphen) and how to specify internationalized domain names,
         see [DNS domain name format](DomainNameFormat.md "DomainNameFormat.md").

    If the domain you entered is available, it will be displayed, if not, similar
    domains will be displayed as suggestions.

    You can choose up to five domains to register. The domains you select appear in the
    **Selected domains** list. 2. To register more domains, repeat steps 3a through 3b.

4.  Choose **Proceed to checkout**.
5.  On the **Pricing** page, choose the number of years that you
    want to register the domain for and whether you want us to
    automatically renew your domain registration before the
    expiration date.

###### Note

Domain name registrations and renewals are not
refundable. If you enable automatic domain renewal
and you decide that you don't want the domain name
after we renew the registration, you can't get a
refund for the cost of the renewal.

Choose **Next**. 6. On the **Contact information** page, enter contact information for the domain
registrant, admin, tech, and billing contacts. The values that
you enter here are applied to all of the domains that you're
registering. For more information, see [Values that you specify when you register or transfer a domain](domain-register-values-specify.md "domain-register-values-specify.md").

###### Important

The contact you list as the registrant during domain registration will have certain rights as
the Registered Name Holder of the domain name, under the [ICANN Transfer Policy](https://www.icann.org/resources/pages/transfer-policy-2016-06-01-en "https://www.icann.org/resources/pages/transfer-policy-2016-06-01-en").
Most domains will be deleted upon closure of your
AWS account (for more information, see [My AWS account is closed or permanently
closed, and my domain is registered with Route 53](troubleshooting-account-closed.md "troubleshooting-account-closed.md")), however if a
domain remains in a closed account, the contact you listed as the
registrant may have the ability to request a transfer of the domain
name to an external registrar. Therefore, it is important that the
registrant contact you list is either yourself or another person you
trust to act responsibly.

Note the following considerations:

**First Name and Last Name**
For **First Name** and **Last Name**, we recommend that you specify the name
on your official ID. For some changes to domain settings, some domain registries require that you provide
proof of identity. The name on your ID must match the name of the registrant contact for the domain.

**Different contacts**
By default, we use the same information for all three contacts. If you want to enter different
information for one or more contacts, change the
value of **Same as registrant
contact** toggle switch to
off position.

###### Note

For .it domains, the registrant and administrative contacts must be the same.

###### Note

For .jp domains, the technical and administrative contacts must be the same.

**Multiple domains**

If you're registering more than one domain, we use the same contact information for all of the domains.

**Additional required information**

For some top-level domains (TLDs), we're required to collect additional information. For these TLDs,
enter the applicable values after the **Postal/Zip Code** field.

**Privacy protection**
Choose whether you want to hide your contact information from WHOIS queries.

###### Note

You must specify the same privacy setting for the administrative, registrant, technical, and billing contacts.

For more information, see the following topics:

    * [Enabling or disabling privacy protection for
     contact information for a domain](domain-privacy-protection.md "domain-privacy-protection.md")
    * [Domains that you can register with Amazon Route 53](registrar-tld-list.md "registrar-tld-list.md")

###### Note

To enable privacy protection for .uk, .co.uk, .me.uk, and .org.uk domains, you must open a support case and request
privacy protection.

Choose **Next**. 7. On the **Review** page, review the information that you entered,
and optionally correct it, read the terms of service, and select the check box to confirm that you've read the terms of service.

Choose **Submit**. 8. In the navigation pane, choose **Domains** and then **Requests**.

On this page you can view the status of domain and also if you need to respond to
registrant contact verification email. You can also choose
to resend the verification email.

If you specified an email address for the registrant contact that has never been used to register a domain with
Route 53, some TLD registries require you to verify that the address is valid.

We send a verification email from one of the following email addresses:

    * **noreply@registrar.amazon** – for TLDs registered by Amazon Registrar.
    * **noreply@domainnameverification.net** or **noreply@emailverification.info** – for TLDs registered by our registrar associate, Gandi.
     To determine who the registrar is for your TLD, see [Finding your registrar](find-your-registrar.md "find-your-registrar.md").

###### Important

The registrant contact must follow the instructions in the email to verify that the email was received, or
we must suspend the domain as required by ICANN. When a domain is suspended, it's not accessible on the internet.

    1. When you receive the verification email, choose the link in the email that verifies that the email address is valid.
     If you don't receive the email immediately, check your junk email folder.
    2. Return to the **Requests** page. If the status doesn't automatically update
     to say **email-address is
     verified**, refresh the browser.

9. When domain registration is complete, your next step depends on whether you want to use Route 53
   or another DNS service as the DNS service for the
   domain:
   - **Route 53** – In the hosted zone that Route 53 created when you registered
     the domain, create records to tell Route 53 how you want to route traffic for the domain and subdomains.

   For example, when someone enters your domain name in a browser and that query is forwarded to Route 53,
   do you want Route 53 to respond to the query with the IP address of a web server in your data center or with the name
   of an ELB load balancer?

   For more information, see [Working with records](rrsets-working-with.md "rrsets-working-with.md").

   ###### Important

   If you create records in a hosted zone other than the one that Route 53 creates automatically,
   you must update the name servers for the domain to
   use the name servers for the new hosted
   zone.
   - **Another DNS service** – Configure your new domain to route DNS queries to
     the other DNS service. Perform the procedure
     [Updating name servers to use another
     registrar](domain-register-other-dns-service.md "domain-register-other-dns-service.md").
