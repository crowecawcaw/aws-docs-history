# Pre-transfer checklist for domain transfers

Before you begin transferring your domain registration to Amazon Route 53, complete the following checks to avoid common transfer failures and ensure a smooth process.

## Decide what you want to transfer

Choose the option that matches your needs:

**Transfer domain registration to Route 53**

Your registrar becomes Amazon Route 53. You pay Route 53 for domain renewals and manage domain settings through the Route 53 console.

**Next step:** Continue with this checklist, then follow [Transferring registration for a domain to
Amazon Route 53](domain-transfer-to-route-53.md "domain-transfer-to-route-53.md").

**Use Route 53 for DNS hosting only**

Keep your current registrar but use Route 53 name servers for DNS resolution. You continue paying your current registrar for renewals.

**Next step:** Skip this checklist and follow [Configuring Amazon Route 53 as your DNS service](dns-configuring.md "dns-configuring.md").

## Prerequisites

checklist

Complete all of the following before starting your domain transfer.

###### Pre-transfer checklist (Complete all items)

1. **☐ Verify registrant email access**

Confirm that you can receive email at the registrant email address, as it will receive the domain transfer authorization email.

###### Important

If you cannot access the current registrant email address, update the email address for the registrant contact with your current registrar and wait 60 days before transferring. 2. **☐ Unlock domain**

Access your current registrar domain settings and disable the "Domain Lock" or "Transfer Lock" protection, if enabled.

###### Note

After disabling the lock, allow a few minutes for the change to take effect before starting your transfer. 3. **☐ Obtain authorization code**

Request an authorization code (auth code) from your current registrar and maintain its confidentiality. You'll enter this code in the Route 53 console later in the transfer process. 4. **☐ Verify domain age and eligibility**

Confirm your domain meets ICANN transfer requirements:

    * The domain must be at least 60 days old since initial
     registration.
    * If the domain registration expired and was restored, it must have been
     restored at least 60 days ago.

###### Tip

ICANN rules may temporarily block transfers if registrant contact details were updated recently (for example, changing your name or email). Some registrars let you opt out of this hold — check with your current registrar if you're unsure. 5. **☐ Prepare payment method**

Ensure your AWS account has a valid payment method. When you transfer a domain to Route 53, the transfer fee that we apply to your AWS account varies by top-level domain.

For current pricing, see [Route 53
Pricing](https://aws.amazon.com/route53/pricing/ "https://aws.amazon.com/route53/pricing/").

###### Note

You cannot use AWS credits to pay for domain transfers. Route 53 charges
the transfer fee before starting the process and provides an immediate
refund if the transfer fails. 6. **☐ Disable DNSSEC (if enabled)**

If DNSSEC is currently enabled with your current registrar, temporarily disable it before starting the transfer. This ensures the transfer can complete without DNS validation issues.

**Why this matters:**

When you transfer a domain, the DNSSEC keys (KSK/ZSK) and DS records stored at your current registrar are not automatically transferred to Route 53. If you re-enable DNSSEC without reconfiguring these keys in Route 53, your domain may fail DNS validation.

**Safe approach (recommended):**

    1. Disable DNSSEC at your current registrar before initiating the transfer.
    2. Complete the domain transfer and create your Route 53 hosted zone (if not already created).
    3. Verify that all DNS records are resolving correctly without DNSSEC enabled.
    4. Configure DNSSEC in Route 53 using your hosted zone's new KSK/ZSK values.
    5. Re-enable DNSSEC by publishing the new DS record with your TLD registrar (now Route 53).

###### Tip

If you are transferring your domain along with creating a new hosted zone in Route 53, disable DNSSEC before transferring, then wait until the hosted zone setup is verified and DNS resolution works correctly. Once confirmed, you can safely enable DNSSEC again from Route 53's console. Always verify your DNS configuration in Route 53 before re-enabling DNSSEC. For more information about DNSSEC with Route 53, see [Configuring DNSSEC for a domain](domain-configure-dnssec.md "domain-configure-dnssec.md").

## Optional: Transfer DNS service first

Consider transferring your DNS service to Route 53 before transferring domain registration. This approach provides these benefits:

- Reduces the risk of website or email downtime during the transfer
- Allows you to test Route 53 DNS functionality before committing to the full transfer
- Provides a fallback option if the domain transfer encounters issues

To transfer DNS service first, see [Configuring Amazon Route 53 as your DNS service](dns-configuring.md "dns-configuring.md").

## Next steps

After completing this checklist:

1. Follow the step-by-step transfer process in [Transferring registration for a domain to
   Amazon Route 53](domain-transfer-to-route-53.md "domain-transfer-to-route-53.md").
2. Monitor your email for authorization messages during the transfer process.
