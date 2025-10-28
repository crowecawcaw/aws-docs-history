# Choose your Route 53 transfer type

When you want to use Amazon Route 53 with your domain, you have two options. Understanding the
difference will help you choose the right approach for your needs:

## Transfer domain registration to Route 53

With this option, Route 53 becomes your domain registrar. This means you'll manage your domain
renewals, contact information, and DNS settings all through Route 53.

**Choose this option if you want to:**

- Consolidate domain management and DNS hosting in one place
- Take advantage of Route 53 domain management features
- Simplify billing by having domain renewals on your AWS bill

**What to expect:**

- **Time to complete:** 5-7 days
- **Prerequisites:** Authorization code from current registrar,
  unlock domain, verify registrant email
- **Who you pay for renewals:** Route 53

**Next step:** Complete the [Pre-transfer checklist for domain transfers](domain-transfer-checklist.md "domain-transfer-checklist.md") to prepare for the transfer.

## Use Route 53 for DNS hosting only

With this option, you keep your current domain registrar but use Route 53 as your DNS service.

**Choose this option if you want to:**

- Keep your existing registrar relationship
- Use Route 53 advanced DNS features without changing registrars
- Get started quickly with minimal prerequisites

**What to expect:**

- **Time to complete:** Up to 2 days (depends on DNS propagation)
- **Prerequisites:** None
- **Who you pay for renewals:** Your current registrar

**Next step:** Go to [Configuring Amazon Route 53 as your DNS service](dns-configuring.md "dns-configuring.md") to set up DNS hosting.

###### Important

You don't have to transfer your domain registration to use Route 53 as your DNS service. You
can keep your existing registrar and use Route 53 only for DNS hosting.
