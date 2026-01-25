# Transferring registration for a domain to

Amazon Route 53

###### Important

During the transfer of any country code top-level domains (ccTLDs) to Route 53,
except for .cc and .tv, updates to the owner contact are ignored and the owner
contact data from the registry is used. You can update the owner contact after the
transfer is complete. For more information, see [Updating contact information and ownership for
a domain](domain-update-contacts.md "domain-update-contacts.md").

To transfer the registration for a domain to Amazon Route 53, follow the procedures in this
topic.

## Transfer process overview

Domain transfer involves these key steps:

1. **Complete pre-transfer checklist**

Verify prerequisites to avoid transfer failures. See [Pre-transfer checklist for domain transfers](domain-transfer-checklist.md "domain-transfer-checklist.md"). 2. **Request transfer in Route 53 console**

Enter domain name and authorization code. See [Step 5: Request the
transfer](#domain-transfer-to-route-53-request-transfer "#domain-transfer-to-route-53-request-transfer"). 3. **Authorize via email** (_Customer action required)_

Click authorization link sent to registrant email within 5 days. See [Step 6: Click the
link in the confirmation and authorization emails](#domain-transfer-to-route-53-authorize-transfer "#domain-transfer-to-route-53-authorize-transfer"). 4. **Wait for completion**

Transfer completes automatically unless rejected by current registrar.
Monitor status in console.

###### Most common failure points

The following are solutions for common issues:

- **Email not received**: Verify registrant
  email is accessible and check spam folder
- **Domain locked**: Unlock at current
  registrar before starting transfer
- **Invalid auth code**: Request new
  authorization code from current registrar
- **60-day rule violation**: 60-day ICANN rule (eligibility
  window). Transfers are blocked within 60 days of initial registration or a
  registrant contact change. Some registrars allow an opt-out before the
  change—ask your current registrar if applicable.

###### Important

If you skip a step, your domain might become unavailable on the internet.

Note the following:

**Contacting AWS Support**

If you encounter issues while transferring a domain, you can contact AWS
Support for free. For more information, see [Contacting AWS Support about domain registration issues](domain-contact-support.md "domain-contact-support.md").

**Expiration date**

For information about how transferring your domain affects the current
expiration date, see [How transferring a domain to
Amazon Route 53 affects the expiration date for your domain registration](domain-transfer-to-route-53-expiration.md "domain-transfer-to-route-53-expiration.md").

**Transfer fee**

When you transfer a domain to Route 53, the transfer fee that we apply to
your AWS account depends on the top-level domain, such as .com or .org.
For more information, see [Route 53 Pricing](https://aws.amazon.com/route53/pricing/ "https://aws.amazon.com/route53/pricing/").

You can't use AWS credits to pay the fee, if any, for transferring a
domain to Route 53.

###### Note

Route 53 charges the fee for transferring your domain before we start the
transfer process. If a transfer fails for some reason, we immediately
credit your account for the cost of the transfer.

**Special and premium domain names**

TLD registries have assigned special or premium prices to some domain
names. You can't transfer a domain to Route 53 if the domain has a special or
premium price.

**Domain quotas**

The default maximum number of domains per AWS account is 20. You can
[request a higher quota](https://us-east-1.console.aws.amazon.com/servicequotas/home/services/route53/quotas/L-F767CB15 "https://us-east-1.console.aws.amazon.com/servicequotas/home/services/route53/quotas/L-F767CB15"). For more information, see [Quotas on domains](DNSLimitations.md#limits-api-entities-domains "DNSLimitations.md#limits-api-entities-domains").

**Name servers limit**

The maximum number of name servers per domain in Route 53 is 6.

###### Topics

- [Transfer requirements for
  top-level domains](#domain-transfer-to-route-53-requirements "#domain-transfer-to-route-53-requirements")
- [Step 1: Confirm that
  Amazon Route 53 supports the top-level domain](#domain-transfer-to-route-53-confirm-tld "#domain-transfer-to-route-53-confirm-tld")
- [Step 2 (Optional):
  Transfer your DNS service to Amazon Route 53 or another DNS service provider](#domain-transfer-to-route-53-transfer-dns "#domain-transfer-to-route-53-transfer-dns")
- [Step 3:
  Change settings with the current registrar](#domain-transfer-to-route-53-change-registrar-settings "#domain-transfer-to-route-53-change-registrar-settings")
- [Step 4: Get the names
  of your name servers](#domain-transfer-to-route-53-get-name-servers "#domain-transfer-to-route-53-get-name-servers")
- [Step 5: Request the
  transfer](#domain-transfer-to-route-53-request-transfer "#domain-transfer-to-route-53-request-transfer")
- [Step 6: Click the
  link in the confirmation and authorization emails](#domain-transfer-to-route-53-authorize-transfer "#domain-transfer-to-route-53-authorize-transfer")
- [Step 7: Update
  the domain configuration](#domain-transfer-to-route-53-change-configuration "#domain-transfer-to-route-53-change-configuration")

## Transfer requirements for

top-level domains

Most domain registrars enforce requirements on transferring a domain to another
registrar. The primary purpose of these requirements is to prevent the owners of
fraudulent domains from repeatedly transferring the domains to different registrars.
Requirements vary, but the following requirements are typical:

- You must have either registered the domain with the current registrar or
  transferred registration for the domain to the current registrar at least 60
  days ago.
- If the registration for a domain name expired and had to be restored, it
  must have been restored at least 60 days ago.
- The domain cannot have any of the following domain name status
  codes:
  - clientTransferProhibited
  - pendingDelete
  - pendingTransfer
  - redemptionPeriod
  - serverTransferProhibited

- The registries for some top-level domains don't allow transfers until
  changes are complete, such as changes to the domain owner.

For a current list of domain name status codes and an explanation of what each
code means, go to the [website for ICANN](https://www.icann.org/ "https://www.icann.org/"),
and search for EPP status codes. (Search on the ICANN website; web searches
sometimes return an old version of the document.)

###### Note

ICANN is the organization that establishes policies governing registration and
transfer of domain names.

You can also search for your domain name in [website for Whois](https://www.whois.com/whois/ "https://www.whois.com/whois/") to see status codes
and other information for your domain.

## Step 1: Confirm that

Amazon Route 53 supports the top-level domain

See [Domains that you can register with Amazon Route 53](registrar-tld-list.md "registrar-tld-list.md"). If
the top-level domain for the domain that you want to transfer is on the list, you
can transfer the domain to Amazon Route 53.

If a TLD is not on the list, you can't currently transfer the domain registration
to Route 53. We occasionally add more TLDs to the list, so check back to see if we've
added support for your domain.

## Step 2 (Optional):

Transfer your DNS service to Amazon Route 53 or another DNS service provider

**Why transfer DNS first?**

Some registrars provide free DNS service that might be disabled as soon as they
receive a request from Route 53 to transfer the domain's registration. If you'd like
Route 53 to provide DNS service for your domain, see [Making Amazon Route 53 the DNS service for an existing domain](MigratingDNS.md "MigratingDNS.md").

## Step 3:

Change settings with the current registrar

Using the method provided by your current registrar, do each of the following for
each domain that you want to transfer.

- [Confirm that the email for the registrant contact for your domain is up to date](#domain-transfer-to-route-53-change-registrar-settings-email "#domain-transfer-to-route-53-change-registrar-settings-email")
- [Unlock the domain so it can be transferred](#domain-transfer-to-route-53-change-registrar-settings-unlock "#domain-transfer-to-route-53-change-registrar-settings-unlock")
- [Confirm that the domain status allows you to transfer the domain](#domain-transfer-to-route-53-change-registrar-settings-status "#domain-transfer-to-route-53-change-registrar-settings-status")
- [Disable DNSSEC for the domain](#domain-transfer-to-route-53-change-registrar-settings-dnssec "#domain-transfer-to-route-53-change-registrar-settings-dnssec")
- [Get an authorization code](#domain-transfer-to-route-53-change-registrar-settings-code "#domain-transfer-to-route-53-change-registrar-settings-code")
- [Renew your domain registration before you transfer the domain (selected geographic TLDs)](#domain-transfer-to-route-53-change-registrar-settings-renew "#domain-transfer-to-route-53-change-registrar-settings-renew")

**Confirm that the email for the registrant contact for your domain is up to
date**

We'll send email to that email address to request authorization for
the transfer. You need to click a link in the email to authorize the
transfer. If you don't click the link, we must cancel the
transfer.

###### Important

The contact you list as the registrant will have certain rights as
the Registered Name Holder of the domain name, under the [ICANN Transfer Policy](https://www.icann.org/resources/pages/transfer-policy-2016-06-01-en "https://www.icann.org/resources/pages/transfer-policy-2016-06-01-en"). Most domains will be deleted
upon closure of your AWS account (for more information, see [My AWS account is closed or permanently
closed, and my domain is registered with Route 53](troubleshooting-account-closed.md "troubleshooting-account-closed.md")), however if a
domain remains in a closed account, the contact you listed as the
registrant may have the ability to request a transfer of the domain
name to an external registrar. Therefore, it is important that the
registrant contact you list is either yourself or another person you
trust to act responsibly.

**Unlock the
domain so it can be transferred**

ICANN, the governing body for domain registrations requires that you
unlock your domain before you transfer it.

**Confirm that the domain status allows you to transfer the domain**

For more information, see [Transfer requirements for
top-level domains](#domain-transfer-to-route-53-requirements "#domain-transfer-to-route-53-requirements").

**Disable DNSSEC for the
domain**

If you use DNSSEC with a domain and you transfer the domain
registration to Route 53, you must disable DNSSEC at the former registrar
first. Then, after you transfer the domain registration, take steps to
set up DNSSEC for the domain in Route 53. Route 53 supports DNSSEC for domain
registration and for DNSSEC signing. For more information, see [Configuring DNSSEC signing in Amazon Route 53](dns-configuring-dnssec.md "dns-configuring-dnssec.md").

###### Important

If you transfer a domain registration to Route 53 while DNSSEC is
configured, the DNSSEC public keys are transferred, too. If you
transfer DNS service to a provider that doesn't support DNSSEC, DNS
resolution fails intermittently until you delete the DNSSEC keys
from the domain. For more information, see [Deleting public keys for a domain](domain-configure-dnssec.md#domain-configure-dnssec-deleting-keys "domain-configure-dnssec.md#domain-configure-dnssec-deleting-keys").

**Get an authorization code**

An authorization code from the current registrar authorizes us to
request that registration for the domain be transferred to Route 53. You'll
enter this code in the Route 53 console later in the process.

Some top-level domains have additional requirements:

**.co.za domains**

You don't need to get an authorization code to transfer a
.co.za domain to Route 53.

**.uk, .co.uk, .me.uk, and .org.uk domains**

If you're transferring a .uk, .co.uk, .me.uk, or .org.uk
domain to Route 53, you don't need to get an authorization
code. Instead, use the method provided by your current
domain registrar to update the value of the IPS tag for the
domain to **GANDI**, all uppercase. (An IPS
tag is required by Nominet, the registry for .uk domain
names.) If your registrar doesn't provide a way to change
the value of the IPS tag, [contact Nominet](https://www.nominet.uk/domain-support/online-services "https://www.nominet.uk/domain-support/online-services").

Note the following about changing the IPS tag:

**You must request the transfer within five
days**

If you don't request the transfer within five
days after you change the IPS tag, the tag changes
back to the previous value. You must change the
value of the IPS tag again, or the transfer
request will fail.

**Viewing the IPS tag in WHOIS queries**

The change to the IPS tag doesn't appear in
WHOIS queries until after the transfer to Route 53
has completed.

**Email from Gandi**

You might receive an email from our registrar
associate, Gandi, about the transfer process. If
you receive an email from Gandi
(transfer-auth@gandi.net) about transferring your
domain, ignore the instructions in the email
because they aren't relevant to a .uk, .co.uk,
.me.uk, or .org.uk domains. Follow the
instructions in this topic instead.

**Renew your domain registration before you transfer the domain (selected
geographic TLDs)**

For most TLDs, when you transfer a domain, the registration is
automatically extended by one year. However, for some geographic TLDs,
registration is not extended when you transfer the domain. If you're
transferring a domain to Route 53 that has one of these TLDs, we recommend
that you renew the domain registration before you transfer the domain,
especially if the expiration date is approaching.

###### Important

If you don't renew the domain before you transfer it, the
registration could expire before the transfer is complete. If this
happens, the domain becomes unavailable on the internet, and the
domain name could become available for others to purchase.

Registration is not automatically extended when you transfer the
following domains to another registrar:

- .ch (Switzerland)
- .cl (Chile)
- .co.uk (United Kingdom)
- .co.za (South Africa)
- .com.au (Australia)
- .cz (Czech Republic)
- .es (Spain)
- .fi (Finland)
- .im (Isle of Man)
- .jp (Japan)
- .me.uk (United Kingdom)
- .net.au (Australia)
- .org.uk (United Kingdom)
- .se (Sweden)
- .uk (United Kingdom)

## Step 4: Get the names

of your name servers

If you're using Amazon Route 53 as your DNS service or you're continuing to use the
existing DNS service, we'll get the names of the name servers for you automatically
later in the process. Skip to [Step 5: Request the
transfer](#domain-transfer-to-route-53-request-transfer "#domain-transfer-to-route-53-request-transfer").

If you want to change the DNS service to a provider other than Route 53 at the same
time that you're transferring the domain to Route 53, use the procedure provided by the
DNS service provider to get the names of the name servers for each domain that you
want to transfer.

###### Important

If the registrar for your domain is also the DNS service provider for the
domain, transfer your DNS service to Route 53 or another DNS service provider
_before_ you continue with the process to transfer the
domain registration.

If you transfer DNS service at the same time that you transfer domain
registration, your website, email, and the web applications associated with the
domain might become unavailable. For more information, see [Step 2 (Optional):
Transfer your DNS service to Amazon Route 53 or another DNS service provider](#domain-transfer-to-route-53-transfer-dns "#domain-transfer-to-route-53-transfer-dns").

## Step 5: Request the

transfer

To transfer domain registration from the current registrar to Amazon Route 53, use the
Route 53 console to request the transfer. Route 53 handles the communication with the
current registrar for the domain.

You can use the console to transfer up to five domains.

The procedure that you use depends on whether you want to transfer a single domain
or up to five domains:

- [To transfer domain
  registration of a single domain to Route 53](#domain-transfer-to-route-53-single-procedure "#domain-transfer-to-route-53-single-procedure")
- [To transfer
  domain registration to Route 53 for up to five domains](#domain-transfer-to-route-53-up-to-five-procedure "#domain-transfer-to-route-53-up-to-five-procedure")

Use the **Transfer domain to your account** process to transfer a
single domain to your account.

###### To transfer domain

registration of a single domain to Route 53

1. Open the Route 53 console at
   [https://console.aws.amazon.com/route53/](https://console.aws.amazon.com/route53/ "https://console.aws.amazon.com/route53/").
2. In the navigation pane, choose **Registered
   domains**.
3. On the **Registered Domains** page, choose
   **Single domain** from the **Transfer
   in** dropdown.
4. On the **Transfer domain to your account** page, in the
   **Check domain transferability** section, enter the
   name of the domain for which you want to transfer registration to Route 53, and
   choose **Check**.
5. If the domain registration is available for transfer, verify that you have
   completed the transfer requirements for top-level domains, and choose
   **Next**.

If the domain registration is not available for transfer, the Route 53
console lists the reasons. Contact your registrar for information about how
to resolve the issues that prevent you from transferring the
registration. 6. On the **DNS service** page, review the information about
name servers, and choose **Next**. 7. If prompted, enter the authorization code or IPS tag that you got from
your current registrar in [Step 3:
Change settings with the current registrar](#domain-transfer-to-route-53-change-registrar-settings "#domain-transfer-to-route-53-change-registrar-settings").

###### Note

You don't need to enter an authorization code to transfer a .co.za,
.uk, .co.uk, .me.uk, or .org.uk domain to Route 53.

Choose **Next**. 8. On the **Domain pricing options** page, choose the number
of years that you want to register the domain you are transferring for and
whether you want us to automatically renew your domain registration before
the expiration date.

###### Note

Domain name registrations and renewals are not refundable. If you
enable automatic domain renewal and you decide that you don't want the
domain name after we renew the registration, you can't get a refund for
the cost of the renewal.

Choose **Next**. 9. On the **Contact information** page, enter contact
information for the domain registrant, admin, technical, and billing
contacts. The values that you enter here are applied to all of the domains
that you're registering. For more information, see [Values that you specify when you register or transfer a domain](domain-register-values-specify.md "domain-register-values-specify.md").

Note the following considerations:

**First Name and Last Name**

For **First Name** and **Last
Name**, we recommend that you specify the name on
your official ID. For some changes to domain settings, some
domain registries require that you provide proof of identity.
The name on your ID must match the name of the registrant
contact for the domain.

**Different contacts**

By default, we use the same information for all three
contacts. If you want to enter different information for one or
more contacts, change the value of **Same as registrant
contact** toggle switch to off position.

###### Note

For .it domains, the registrant and admin contacts must be
the same.

**Additional required information**

For some top-level domains (TLDs), we're required to collect
additional information. For these TLDs, enter the applicable
values after the **Postal/Zip Code**
field.

**Privacy protection**

Choose whether you want to hide your contact information from
WHOIS queries.

###### Note

You must specify the same privacy setting for the admin,
registrant, and technical contacts.

For more information, see the following topics:

    * [Enabling or disabling privacy protection for
     contact information for a domain](domain-privacy-protection.md "domain-privacy-protection.md")
    * [Domains that you can register with Amazon Route 53](registrar-tld-list.md "registrar-tld-list.md")

###### Note

To enable privacy protection for .uk, .co.uk, .me.uk, and
.org.uk domains, you must open a support case and request
privacy protection.

Choose **Next**. 10. On the **Review** page, review the information that you
entered, and optionally correct it. Read the terms of service, and select
the check box to confirm that you've read the terms of service.

Choose **Submit request**. 11. In the navigation pane, choose **Domains** and then
**Requests**.

On this page, you can view the status of domain and also if you need to
respond to registrant contact verification email. You can also choose to
resend the verification email.

If you specified an email address for the registrant contact that has
never been used to register a domain with Route 53, some TLD registries require
you to verify that the address is valid.

We send a verification email from one of the following email
addresses:

    * **noreply@registrar.amazon** – for TLDs
     registered by Amazon Registrar.
    * **noreply@domainnameverification.net** or **noreply@emailverification.info** –
     for TLDs registered by our registrar associate, Gandi. To determine
     who the registrar is for your TLD, see [Finding your registrar](find-your-registrar.md "find-your-registrar.md").

###### Important

The registrant contact must follow the instructions in the email to
verify that the email was received, or we must suspend the domain as
required by ICANN. When a domain is suspended, it's not accessible on
the internet.

    1. When you receive the verification email, choose the link in the
     email that verifies that the email address is valid. If you don't
     receive the email immediately, check your junk email folder.
    2. Return to the **Requests** page. If the status
     doesn't automatically update to say **email-address is
     verified**, choose **Refresh
     status**.

12. When domain transfer is complete, your next step depends on whether you
    want to use Route 53 or another DNS service as the DNS service for the
    domain:
    - **Route 53** – In the hosted zone
      that Route 53 created when you registered the domain, create records to
      tell Route 53 how you want to route traffic for the domain and
      subdomains.

    For example, when someone enters your domain name in a browser and
    that query is forwarded to Route 53, do you want Route 53 to respond to
    the query with the IP address of a web server in your data center or
    with the name of an Elastic Load Balancing load balancer?

    For more information, see [Working with records](rrsets-working-with.md "rrsets-working-with.md").

    ###### Important

    If you create records in a hosted zone other than the one that
    Route 53 creates automatically, you must update the name servers
    for the domain to use the name servers for the new hosted
    zone.
    - **Another DNS service** –
      Configure your new domain to route DNS queries to the other DNS
      service. Perform the procedure [Updating name servers to use another
      registrar](domain-register-other-dns-service.md "domain-register-other-dns-service.md").

Use the following procedure to transfer up to five domains to your account.

###### To transfer

domain registration to Route 53 for up to five domains

1. Open the Route 53 console at
   [https://console.aws.amazon.com/route53/](https://console.aws.amazon.com/route53/ "https://console.aws.amazon.com/route53/").
2. In the navigation pane, choose **Registered
   domains**.
3. On the **Registered domains** page, choose
   **Multiple domains** from the **Transfer
   in** dropdown.
4. On the **Transfer multiple domains to your account**
   page, enter up to five domains you want to transfer, and their authorization
   code, if required, per line, and choose **Check**.
5. If the domain registration is available for transfer, it is listed in the
   **Domain availability** list as available. Select the
   check-box next to each domain for which you want to transfer the
   registration, verify that you have completed the transfer requirements for
   top-level domains, and choose **Next**.

If the domain registration is not available for transfer, the Route 53
console lists the reasons. Contact your registrar for information about how
to resolve the issues that prevent you from transferring the
registration. 6. On the **DNS service** page, review the information about
name servers, and choose **Next**.

###### Note

Domain name registrations and renewals are nonrefundable. If you
enable automatic domain renewal and you decide that you don't want the
domain name after we renew the registration, you can't get a refund for
the cost of the renewal. 7. On the **Contact information** page, enter contact
information for the domain registrant, admin, and tech contacts. The values
that you enter here are applied to all the domains that you're transferring.

###### Important

We recommend that you specify the following values for the registrant
contact (the domain owner):

    * **First and last name**: We
     recommend that you specify the name that appears on your
     official ID. For some changes to domain settings, some domain
     registries require that you provide proof of identity. The name
     on your ID must match the name of the registrant contact for the
     domain.
    * **Contact details**: During the
     domain transfer, we recommend that you specify the same values
     as are specified with the current registrar. When you change
     contact details for the registrant contact, you change the
     domain owner, and some TLD registries don't allow you to change
     the domain owner during a domain transfer. If you change contact
     details for the registrant contact, the transfer might fail. You
     can change contact details for the registrant contact after you
     transfer the domain.

By default, we use the same information for all three contacts. If you
want to enter different information for one or more contacts, set the value
of **Same as the registrant contact** to off
position.

###### Note

For .it domains, the registrant and admin contacts must be the
same.

For more information, see [Values that you specify when you register or transfer a domain](domain-register-values-specify.md "domain-register-values-specify.md"). 8. For some TLDs, we're required to collect additional information. For these
TLDs, enter the applicable values after the **Postal/Zip
Code** field. 9. If the value of **Contact Type** is
**Person**, choose whether you want to hide your
contact information from WHOIS queries. For more information, see [Enabling or disabling privacy protection for
contact information for a domain](domain-privacy-protection.md "domain-privacy-protection.md"). 10. Choose **Submit**. 11. Review the information you entered, read the terms of service, and select
the check box to confirm that you've read the terms of service. 12. Choose **Submit request**.

We confirm that the domains are eligible for transfer, and we send an
email to the registrant contacts for the domain to request authorization to
transfer the domain. 13. In the navigation pane, choose **Domains** and then
**Requests**.

On this page you can view the status of domain and also if you need to
respond to registrant contact verification email. You can also choose to
resend the verification email.

If you specified an email address for the registrant contact that has
never been used to register a domain with Route 53, some TLD registries require
you to verify that the address is valid.

We send a verification email from one of the following email
addresses:

    * **noreply@registrar.amazon** – for TLDs
     registered by Amazon Registrar.
    * **noreply@domainnameverification.net** or **noreply@emailverification.info** –
     for TLDs registered by our registrar associate, Gandi. To determine
     who the registrar is for your TLD, see [Finding your registrar](find-your-registrar.md "find-your-registrar.md").

###### Important

The registrant contact must follow the instructions in the email to
verify that the email was received, or we must suspend the domain as
required by ICANN. When a domain is suspended, it's not accessible on
the internet.

    1. When you receive the verification email, choose the link in the
     email that verifies that the email address is valid. If you don't
     receive the email immediately, check your junk email folder.
    2. Return to the **Requests** page. If the status
     doesn't automatically update to say **email-address is
     verified**, choose **Refresh
     status**.

14. When domain transfer is complete, your next step depends on whether you
    want to use Route 53 or another DNS service as the DNS service for the
    domain:
    - **Route 53** – In the hosted zone
      that Route 53 created when you registered the domain, create records to
      tell Route 53 how you want to route traffic for the domain and
      subdomains.

    For example, when someone enters your domain name in a browser and
    that query is forwarded to Route 53, do you want Route 53 to respond to
    the query with the IP address of a web server in your data center or
    with the name of an ELB load balancer?

    For more information, see [Working with records](rrsets-working-with.md "rrsets-working-with.md").

    ###### Important

    If you create records in a hosted zone other than the one that
    Route 53 creates automatically, you must update the name servers
    for the domain to use the name servers for the new hosted
    zone.
    - **Another DNS service** –
      Configure your new domain to route DNS queries to the other DNS
      service. Perform the procedure [Updating name servers to use another
      registrar](domain-register-other-dns-service.md "domain-register-other-dns-service.md").

## Step 6: Click the

link in the confirmation and authorization emails

Soon after you request the transfer, we might send one or more emails to the
registrant contact for the domain:

**Email to confirm that the registrant contact is reachable**

If you've never registered a domain with Route 53 or transferred a domain
to Route 53, we send you an email that asks you to confirm that the email
address is valid. We retain this information so we don't have to send
this confirmation email again.

**Email to get authorization to transfer the domain**

For some TLDs, you need to respond to an email to authorize transfer
of the domain.

**Generic TLDs such as .com, .net, and .org**

Authorization isn't required for domains that have a
[generic TLD](registrar-tld-list.md#registrar-tld-list-generic "registrar-tld-list.md#registrar-tld-list-generic"), such as .com, .net, or
.org.

**Geographic TLDs such as .co.uk and .jp**

For domains that have a [geographic TLD](registrar-tld-list.md#registrar-tld-list-geographic "registrar-tld-list.md#registrar-tld-list-geographic"), we're required to get your
authorization to transfer the domain. If you transfer 10
domains, we have to send you 10 emails, and you have to
click the authorization link in each one.

The emails all go to the registrant contact for the domain:

- If you're the registrant contact for the domain, follow the instructions
  in the email to authorize the transfer.
- If someone else is the registrant contact, ask that person to follow the
  instructions in the email to authorize the transfer.

###### Important

If you're transferring a domain that has a geographic TLD, we wait up to five
days for the registrant contact to authorize the transfer. If the registrant
contact doesn't respond within five days, we cancel the transfer operation and
send an email to the registrant contact about the cancellation.

###### Topics

- [Authorization email for a new owner or email address](#domain-transfer-to-route-53-authorize-transfer-additional-email "#domain-transfer-to-route-53-authorize-transfer-additional-email")
- [Email addresses that authorization emails come from](#domain-transfer-to-route-53-authorize-transfer-email-addresses "#domain-transfer-to-route-53-authorize-transfer-email-addresses")
- [Approval from the current registrar](#domain-transfer-to-route-53-authorize-transfer-registrar-approval "#domain-transfer-to-route-53-authorize-transfer-registrar-approval")
- [What
  happens next](#domain-transfer-to-route-53-authorize-transfer-what-next "#domain-transfer-to-route-53-authorize-transfer-what-next")

### Authorization email for a new owner or email address

If you changed the following values, we send you a separate email that asks
for your authorization:

**Domain owner**

If you change the owner of the domain, as described in [What triggers a domain
ownership change?](domain-update-contacts.md#domain-update-contacts-who-is-domain-owner "domain-update-contacts.md#domain-update-contacts-who-is-domain-owner"), we
send email to the registrant contact for the domain.

**Email address for the registrant contact (only for some TLDs)**

For some TLDs, if you change the email address for the registrant
contact, we send an email to the old and the new email address for
the registrant contact. Someone at both email addresses must follow
the instructions in the email to authorize the change.

For changes to the domain owner or the email address for the registrant
contact, if we don't receive authorization for the change within 3-15 days,
depending on the top-level domain, we must cancel the request as required by
ICANN.

### Email addresses that authorization emails come from

All email comes from one of the following email addresses.

| TLDs                | Email address that authorization email comes from                                                                                                                                                                                     |
| ------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| .com.au and .net.au | no-reply@ispapi.net<br>The email contains a link to<br>http://transfers.ispapi.net.                                                                                                                                                   |
| .fr                 | nic@nic.fr, if you're changing the registrant contact for<br>a .fr domain name at the same time that you're transferring<br>the domain. (The email is sent both to the current<br>registrant contact and the new registrant contact.) |
| All others          | One of the following email addresses:<br>• noreply@registrar.amazon<br>• noreply@domainnameverification.net<br>• noreply@emailverification.info                                                                                       |

To determine who the registrar is for your TLD, see [Domains that you can register with Amazon Route 53](registrar-tld-list.md "registrar-tld-list.md").

### Approval from the current registrar

If the registrant contact authorizes the transfer, we start to work with your
current registrar to transfer your domain. This step might take up to ten days,
depending on the TLD for your domain:

- [Generic top-level domains](registrar-tld-list-generic.md "registrar-tld-list-generic.md") – take up to
  seven days
- [Geographic top-level domains](registrar-tld-list-geographic.md "registrar-tld-list-geographic.md") (also known as
  country code top-level domains) – take up to ten days

If your current registrar doesn't reply to our transfer request, which is
common among registrars, the transfer happens automatically. If your current
registrar rejects the transfer request, we send an email notification to the
current registrant contact. The registrant needs to contact the current
registrar and resolve the issues with the transfer.

### What

happens next

When your domain transfer has been approved, we send another email to the
registrant contact. For more information about the process, see [Viewing the status of a domain
transfer](domain-transfer-to-route-53-status.md "domain-transfer-to-route-53-status.md").

We charge your AWS account for the domain transfer as soon as the transfer
is complete. For a list of charges by TLD, see [Amazon Route 53 Pricing for Domain Registration](https://d32ze2gidvkk54.cloudfront.net/Amazon_Route_53_Domain_Registration_Pricing_20140731.pdf "https://d32ze2gidvkk54.cloudfront.net/Amazon_Route_53_Domain_Registration_Pricing_20140731.pdf").

###### Note

This is a one-time charge, so the charge doesn't appear in your CloudWatch
billing metrics. For more information about CloudWatch metrics, see [Using Amazon CloudWatch
metrics](../../../AmazonCloudWatch/latest/monitoring/working_with_metrics.md "../../../AmazonCloudWatch/latest/monitoring/working_with_metrics.md") in the _Amazon CloudWatch User Guide_.

## Step 7: Update

the domain configuration

After the transfer is complete, you can optionally change the following
settings:

**Transfer lock**

To transfer the domain to Route 53, you had to disable the transfer lock.
If you want to re-enable the lock to prevent unauthorized transfers, see
[Locking a domain to prevent unauthorized transfer to
another registrar](domain-lock.md "domain-lock.md").

**Automatic renewal**

We configure the transferred domain to automatically renew as the
expiration date approaches. For information about how to change this
setting, see [Enabling or disabling automatic
renewal for a domain](domain-enable-disable-auto-renewal.md "domain-enable-disable-auto-renewal.md").

**Extended registration period**

By default, Route 53 renews the domain annually. If you want to register
the domain for a longer period, see [Extending the registration period for a domain](domain-extend.md "domain-extend.md").

**DNSSEC**

For information about configuring DNSSEC for the domain, see [Configuring DNSSEC for a domain](domain-configure-dnssec.md "domain-configure-dnssec.md").
