# Verifying your domain for Amazon SES email

receiving

As with any domain you want to use for sending or receiving email with Amazon SES, you must
first prove that you own it. The verification procedure includes initiating domain
verification with SES and then publishing the DNS records, either CNAME or TXT, to
your DNS provider depending on which verification method you use.

Through the console, you can verify your domains with either [Easy DKIM](send-email-authentication-dkim-easy.md "send-email-authentication-dkim-easy.md") or [Bring Your Own DKIM
(BYODKIM)](send-email-authentication-dkim-bring-your-own.md "send-email-authentication-dkim-bring-your-own.md") and easily copy their DNS records to publish to your DNS provider - how
to do this is explained in [Creating a domain identity](creating-identities.md#verify-domain-procedure "creating-identities.md#verify-domain-procedure"). Optionally, you can use either the SES
[`VerifyDomainDkim`](../APIReference/API_VerifyDomainDkim.md "../APIReference/API_VerifyDomainDkim.md") or [`VerifyDomainIdentity`](../APIReference/API_VerifyDomainIdentity.md "../APIReference/API_VerifyDomainIdentity.md") APIs.

You can easily confirm that your domain or email address is verified by looking at its
status in the [Verified identities](view-verified-domains.md "view-verified-domains.md") table in the
SES console or by using either the SES [`GetIdentityVerificationAttributes`](../APIReference/API_GetIdentityVerificationAttributes.md "../APIReference/API_GetIdentityVerificationAttributes.md") or [`GetEmailIdentity`](../APIReference-V2/API_GetEmailIdentity.md "../APIReference-V2/API_GetEmailIdentity.md")
APIs.
