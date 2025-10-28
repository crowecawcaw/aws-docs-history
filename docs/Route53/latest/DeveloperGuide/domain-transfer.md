# Transferring domains

You can transfer domain registration from another registrar to Amazon Route 53, from one AWS
account to another, or from Route 53 to another registrar. There is no cost for transferring
domains from one AWS account to another.

The topics in this section cover the following topics related to transferring domains:

1.  [Choose your transfer type](domain-transfer-decision-guide.md "domain-transfer-decision-guide.md")
    - Understand the difference between transferring domain registration to Route 53
      versus using Route 53 for DNS hosting only.
    - Learn which option is right for your needs based on your goals for domain
      management and DNS hosting.

2.  [Pre-transfer checklist](domain-transfer-checklist.md "domain-transfer-checklist.md")
    - Complete essential preparation steps before transferring your domain to
      Route 53 to avoid common transfer failures.
    - Verify domain eligibility, obtain authorization codes, and prepare your
      DNS settings for a smooth transfer process.

3.  [Transferring registration for a domain to
    Amazon Route 53](domain-transfer-to-route-53.md "domain-transfer-to-route-53.md")
    - Learn the step-by-step procedure for transferring a domain from another
      registrar to Route 53, including prerequisites, authorization codes, and
      updating DNS settings.
    - Understand how transferring a domain affects the expiration date and the
      considerations for different top-level domains (TLDs).

4.  [Common transfer
    issues](domain-transfer-troubleshooting.md "domain-transfer-troubleshooting.md")
    - Prevent common transfer issues by understanding domain requirements,
      authorization processes, and timing considerations.
    - Learn how to resolve transfer problems and what to do if your transfer
      is delayed or rejected.

5.  [Transferring a domain from Amazon Route 53 to
    another registrar](domain-transfer-from-route-53.md "domain-transfer-from-route-53.md")
    - Understand the process of transferring a domain from Route 53 to another
      registrar, including obtaining the authorization code, updating DNS
      settings, and responding to confirmation emails.
    - Be aware of the considerations when transferring DNS service to another
      provider and the potential impact on Route 53-specific features like alias
      records and routing policies.

6.  [Transferring a domain to a
    different AWS account](domain-transfer-between-aws-accounts.md "domain-transfer-between-aws-accounts.md")
    - Find out how to transfer a domain from one AWS account to another,
      including the roles and permissions required for initiating and accepting
      the transfer.
    - Learn about the optional step of migrating the hosted zone to the new
      account after the domain transfer.

7.  [Transfer status](domain-transfer-to-route-53-status.md "domain-transfer-to-route-53-status.md")
    - Discover how to view the status of a domain transfer request and the
      meaning of different status codes during the transfer process.

8.  [How transferring a domain to
    Amazon Route 53 affects the expiration date for your domain registration](domain-transfer-to-route-53-expiration.md "domain-transfer-to-route-53-expiration.md")

        * Find out how transferring a domain to Route 53 might affect the expiration
         date for the domain.

    By following the information provided in the topics listed above, you can effectively
    transfer domains to and from Route 53, manage the transfer process, and ensure a smooth
    transition while maintaining proper DNS configuration and routing.
