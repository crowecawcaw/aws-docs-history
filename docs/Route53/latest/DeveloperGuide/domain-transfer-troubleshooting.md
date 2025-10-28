# Preventing common Route 53 transfer issues

If you encounter issues while your domain transfer is in progress, here are the most common problems and how to resolve them:

###### Note

If your transfer has already failed, see [Transferring my domain to
Amazon Route 53 failed](troubleshooting-domain-transfer-failed.md "troubleshooting-domain-transfer-failed.md") for post-failure
troubleshooting.

**You didn't receive the authorization email**

If you don't receive the authorization email from Route 53, here are the most common causes and solutions:

- **Check your spam folder** - Authorization emails are sometimes filtered by email providers.
- **Verify your email address** - Confirm that the registrant email address in your domain's contact information is current and accessible.
- **Update your contact information** - If the email address is outdated, update it with your current registrar before starting the transfer.
- **Resend the authorization email** - In the Route 53 console, click "Resend authorization email" for the domain in transfer status.

**You're getting an "invalid authorization code" error**

If you receive an "invalid authorization code" error, try these solutions:

- **Double-check the code** - Authorization codes are case-sensitive. Copy and paste the code directly from your registrar's interface to avoid typing errors.
- **Check if the code has expired** - Authorization codes can expire between 5-30 days depending on your current registrar. Request a new code if yours has expired.
- **Remove extra spaces** - Make sure there are no leading or trailing spaces when you enter the code.
- **Get a new authorization code** - If the code continues to fail, request a new authorization code from your current registrar.

**Your domain is locked at the current registrar**

Domain transfers can fail when your current registrar has a transfer lock enabled (also known as "Domain Lock" or "Client Transfer Prohibited"). This is a common security setting that prevents unauthorized transfers.

To resolve this issue:

- **Unlock your domain** - Log in to your current registrar's control panel and disable the domain transfer lock.
- **Verify the lock is removed** - You can use any public WHOIS lookup tool to confirm that the domain status shows "OK" instead of "clientTransferProhibited."
- **Get help from your registrar** - If you don't see an option to unlock your domain, contact your current registrar's support team. They can help you remove the lock.

**Your domain isn't eligible for transfer**

If your domain transfer is rejected due to eligibility issues, check the following:

- **Verify domain age** - Your domain must be at least 60 days old since registration or last transfer.
- **Check TLD support** - Confirm that Route 53 supports your domain's top-level domain (TLD). See [Domains that you can register with Amazon Route 53](registrar-tld-list.md "registrar-tld-list.md") for supported TLDs.
- **Review domain status** - Domains with certain status codes (such as "pendingTransfer" or "redemptionPeriod") cannot be transferred.
- **Check expiration date** - Domains that are expired or within 15 days of expiration may not be transferable.
- **Resolve billing issues** - Make sure all outstanding fees with your current registrar are paid.

**Your transfer is taking longer than expected**

If your transfer seems to be delayed, here's what you should know:

- **Normal timeframe** - Most transfers complete within 5-7 days, but can take up to 10 days.
- **Monitor transfer status** - Check your transfer progress in the Route 53 console. For more information, see [Viewing the status of a domain
  transfer](domain-transfer-to-route-53-status.md "domain-transfer-to-route-53-status.md").
- **Respond to emails quickly** - Both registrars may send confirmation emails that require your response to proceed.
- **Contact your current registrar** - If the transfer is delayed, contact your current registrar to make sure they're not blocking the transfer.

**When to contact AWS Support**

Contact AWS Support if you've tried the solutions above and still have issues, or if you encounter:

- Transfer failures after multiple attempts with correct information
- Billing or payment issues during the transfer process
- Technical errors in the Route 53 console that prevent you from starting a transfer
- Transfers that remain in "pending" status for more than 10 days

When you contact support, include your domain name, transfer request ID (if available), and details about the specific error or issue you're experiencing.
