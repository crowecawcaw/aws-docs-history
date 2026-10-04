

# Multi-step carrier approval (out-of-band requirement)
<a name="nx-rcs-launch-gb-out-of-band"></a>

**Important**  
In addition to the console registration, you must complete a multi-step out-of-band approval process. Different carriers use different verification methods, and you will receive emails from multiple parties. Your registration cannot be fully approved until all carrier approvals are complete. CC `aws-end-user-messaging-rcs-approvals@amazon.com` on all emails you send as part of this process.

**Step 1: Proactive brand approval email (Three and Vodafone).** After you submit your registration, send a proactive brand approval email authorizing these carriers to enable RCS messaging for your brand. Send it to Three (`dan.cottle@three.co.uk`) and Vodafone (`wholesaleorders@vodafone.com`).

**Step 2: Brand Assure verification (BT/EE).** A third-party service called Brand Assure contacts your brand point of contact directly from `uksupport@brandassure.com` with instructions for verifying your brand identity for BT/EE. You must respond to this email to complete the BT/EE approval.

**Warning**  
Ensure that your email system does not block or filter emails from the `@brandassure.com` domain, and add it to your allowlist before submitting your registration. The Brand Assure approval has a 30-day validity period; if it expires before your registration is complete, you must restart the process, which may incur additional fees.

**Step 3: Aegis verification (O2).** A third-party service called Aegis contacts your brand point of contact from `certify@aegismobile.com` with a two-factor authentication (2FA) PIN that you must use to complete the verification. The 2FA PIN is valid for 7 days and the overall Aegis verification process is valid for 45 days.

**Warning**  
Ensure that your email system does not block or filter emails from the `@aegismobile.com` domain, and add it to your allowlist before submitting your registration. If the Aegis email is filtered to spam or blocked, you will miss the 2FA PIN and the verification will expire.

**Note**  
Because each carrier has an independent approval process, your agent may reach PARTIAL status (some carriers approved) before all carriers complete their review. You can begin sending RCS messages to recipients on approved carriers while waiting for remaining approvals.

For general compliance guidance that applies to all countries, see [How to get set up](nx-rcs-get-set-up.md).