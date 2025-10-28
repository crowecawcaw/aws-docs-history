# Verified identities in Amazon SES

In Amazon SES, a _verified identity_ is a domain or email address that you
use to send or receive email. Before you can send an email using Amazon SES, you must create and
verify each identity that you're going to use as a "From", "Source", "Sender", or
"Return-Path" address. Verifying an identity with Amazon SES confirms that you own it and helps
prevent unauthorized use.

If your account is still in the Amazon SES sandbox, you also need to verify any email addresses
which you plan on sending email to, unless you're sending to test inboxes provided by the
[Amazon SES mailbox simulator](send-an-email-from-console.md#send-email-simulator "send-an-email-from-console.md#send-email-simulator"). For more
information, see [Using the mailbox simulator manually](send-an-email-from-console.md#send-email-simulator "send-an-email-from-console.md#send-email-simulator").

You can create an identity by using the Amazon SES console or the Amazon SES API. The identity
verification process depends on which type of identity you choose to create.

###### Tip

If you're a first time user of SES, you can use the [Get started wizard](setting-up.md#quick-start-verify-email-addresses "setting-up.md#quick-start-verify-email-addresses") to create and
verify your first identity (email address or domain).

###### Contents

- [Creating and verifying identities in Amazon SES](creating-identities.md "creating-identities.md")
- [Managing identities in Amazon SES](managing-identities.md "managing-identities.md")
- [Configuring identities in Amazon SES](configure-identities.md "configure-identities.md")
- [Sending test emails in Amazon SES with the
  simulator](send-an-email-from-console.md "send-an-email-from-console.md")
