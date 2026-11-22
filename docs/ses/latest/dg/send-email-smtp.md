

# Using SMTP to send email

Use SMTP or the Amazon SES API to send production email through Amazon SES. For more information about the API, see [Using the Amazon SES API to send email](send-email-api.md).

SMTP is a standard protocol for sending email that many applications and email servers support.

## Choose an SMTP sending option
<a name="send-email-smtp-options"></a>

Choose a credential option based on its AWS Region and connection support. The following topics explain each option.

[Mail Manager SMTP](smtp-credentials-mail-manager.md) (recommended)  
Use an authenticated Mail Manager ingress endpoint. The SES console configures the required resources.  
Mail Manager message-processing charges apply when a traffic policy accepts a recipient and Mail Manager receives the message. For current prices, see [SES pricing](https://aws.amazon.com/ses/pricing/).

[Amazon SES SMTP interface](smtp-credentials.md)  
Use credentials from an AWS Identity and Access Management (IAM) user. The linked topic lists the current Region availability and setup instructions.

## Requirements to send email over SMTP
<a name="send-email-smtp-requirements"></a>

For either SMTP option, you need the following:
+ Client software that supports Transport Layer Security (TLS).
+ An email address that you've verified with Amazon SES. For more information, see [Verified identities in Amazon SES](verify-addresses-and-domains.md).
+ Increased sending quotas, if you want to send large quantities of email. For more information, see [Managing your Amazon SES sending limits](manage-sending-quotas.md).

## Methods to send email over SMTP
<a name="send-email-methods"></a>

Use any of the following methods with either SMTP credential type.
+ To configure SMTP-enabled software, see [Sending email through Amazon SES using software packages](send-email-smtp-software-package.md).
+ To program an application, see [Sending emails programmatically over SMTP](send-using-smtp-programmatically.md).
+ To configure your existing email server, see [Integrating Amazon SES with your existing email server](send-email-smtp-existing-server.md).
+ To test a connection from the command line, see [Testing your connection to the Amazon SES SMTP interface using the command line](send-email-smtp-client-command-line.md).

For solutions to common problems, see [Amazon SES SMTP issues](troubleshoot-smtp.md). For SMTP response codes, see [SMTP response codes returned by Amazon SES](troubleshoot-smtp.md#troubleshoot-smtp-response-codes).