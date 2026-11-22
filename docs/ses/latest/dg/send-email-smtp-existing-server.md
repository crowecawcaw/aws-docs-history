

# Integrating Amazon SES with your existing email server

If you administer your own email server, configure it to send outgoing email through Amazon SES. You do not need to modify the email clients or applications that use the server.

Use the SMTP endpoint, user name, and password from [Creating SMTP credentials using Mail Manager](smtp-credentials-mail-manager.md) or [Obtaining Amazon SES SMTP credentials using IAM](smtp-credentials.md). Postfix uses port `587`. Sendmail uses port `25` by default. Windows IIS SMTP supports ports `25` and `587`. Both credential types support these ports with STARTTLS.

**Important**  
Do not use your AWS access key ID and secret access key as SMTP credentials. For more information, see [Types of Amazon SES credentials](send-email-concepts-credentials.md).

**Topics**
+ [Integrating Amazon SES with Postfix](postfix.md)
+ [Integrating Amazon SES with Sendmail](send-email-sendmail.md)
+ [Integrating Amazon SES with Microsoft Windows Server IIS SMTP](send-email-windows-server.md)