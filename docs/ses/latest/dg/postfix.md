# Integrating Amazon SES with Postfix

Postfix is an alternative to the widely used Sendmail Message Transfer Agent (MTA). For
information about Postfix, go to [http://www.postfix.org](http://www.postfix.org "http://www.postfix.org"). The procedures in this topic will work with
Linux, macOS, or Unix.

###### Note

Postfix is a third-party application, and isn't developed
or supported by Amazon Web Services. The procedures in this section are provided for informational purposes
only, and are subject to change without notice.

## Prerequisites

Before you complete the procedures in this section, you have to perform the following
tasks:

- Uninstall the Sendmail application if it's installed on your system. The
  procedure for completing this step varies depending on the operating system you
  use.

###### Important

Following references to _sendmail_ refer to the Postfix
command `sendmail`, not to be confused with the Sendmail
application.

- Install Postfix. The procedure for completing this step varies depending on
  the operating system you use.
- Install a SASL authentication package. The procedure for completing this step
  varies depending on the operating system you use. For example, if you use a
  RedHat-based system, you should install the `cyrus-sasl-plain`
  package. If you use a Debian- or Ubuntu-based system, you should install the
  `libsasl2-modules` package.
- Verify an email address or domain to use for sending email. For more
  information, see [Creating an email address
  identity](creating-identities.md#verify-email-addresses-procedure "creating-identities.md#verify-email-addresses-procedure").
- If your account is still in the sandbox, you can only send email to verified
  email addresses. For more information, see [Request production access (Moving out of the
  Amazon SES sandbox)](request-production-access.md "request-production-access.md").

## Configuring Postfix

Complete the following procedures to configure your mail server to send email through
Amazon SES using Postfix.

###### To configure Postfix

1. At the command line, type the following command:

```
sudo postconf -e "relayhost = [`email-smtp.us-west-2.amazonaws.com`]:587" \
"smtp_sasl_auth_enable = yes" \
"smtp_sasl_security_options = noanonymous" \
"smtp_sasl_password_maps = hash:/etc/postfix/sasl_passwd" \
"smtp_use_tls = yes" \
"smtp_tls_security_level = secure" \
"smtp_tls_note_starttls_offer = yes"
```

###### Note

If you use Amazon SES in an AWS Region other than US West (Oregon), replace
`email-smtp.us-west-2.amazonaws.com` in the preceding
command with the SMTP endpoint of the appropriate Region. For more
information, see [Regions and Amazon SES](regions.md "regions.md"). 2. In a text editor, open the file `/etc/postfix/master.cf`.
Search for the following entry:

```
-o smtp_fallback_relay=
```

If you find this entry, comment it out by placing a `#` (hash)
character at the beginning of the line. Save and close the file.

Otherwise, if this entry isn't present, continue to the next step. 3. In a text editor, open the file `/etc/postfix/sasl_passwd`.
If the file doesn't already exist, create it. 4. Add the following line to
`/etc/postfix/sasl_passwd`:

```
[`email-smtp.us-west-2.amazonaws.com`]:587 `SMTPUSERNAME`:`SMTPPASSWORD`
```

###### Note

Replace `SMTPUSERNAME` and
`SMTPPASSWORD` with your SMTP sign-in
credentials. Your SMTP sign-in credentials aren't the same as your AWS
access key ID and secret access key. For more information about credentials,
see [Obtaining Amazon SES SMTP credentials](smtp-credentials.md "smtp-credentials.md").

If you use Amazon SES in an AWS Region other than US West (Oregon), replace
`email-smtp.us-west-2.amazonaws.com` in the preceding
example with the SMTP endpoint of the appropriate Region. For more
information, see [Regions and Amazon SES](regions.md "regions.md").

Save and close `sasl_passwd`. 5. At a command prompt, type the following command to create a hashmap database
file containing your SMTP credentials:

```
sudo postmap hash:/etc/postfix/sasl_passwd
```

6. (Optional) The `/etc/postfix/sasl_passwd` and
   `/etc/postfix/sasl_passwd.db` files you created in the
   previous steps aren't encrypted. Because these files contain your SMTP
   credentials, we recommend that you modify the files' ownership and permissions
   in order to restrict access to them. To restrict access to these files:
   1. At a command prompt, type the following command to change the
      ownership of the files:

   ```
   sudo chown root:root /etc/postfix/sasl_passwd /etc/postfix/sasl_passwd.db
   ```

   2. At a command prompt, type the following command to change the
      permissions of the files so that only the root user can
      read or write to them:

   ```
   sudo chmod 0600 /etc/postfix/sasl_passwd /etc/postfix/sasl_passwd.db
   ```

7. Tell Postfix where to find the CA certificate (needed to verify the Amazon SES
   server certificate). The command you use in this step varies based on your
   operating system.
   - If you use Amazon Linux, Red Hat Enterprise Linux, or a related distribution,
     type the following command:

   ```
   sudo postconf -e 'smtp_tls_CAfile = /etc/ssl/certs/ca-bundle.crt'
   ```

   - If you use Ubuntu or a related distribution, type the following
     command:

   ```
   sudo postconf -e 'smtp_tls_CAfile = /etc/ssl/certs/ca-certificates.crt'
   ```

   - If you use macOS, you can generate the certificate from your system
     keychain. To generate the certificate, type the following command at the
     command line:

   ```
   sudo security find-certificate -a -p /System/Library/Keychains/SystemRootCertificates.keychain | sudo tee /etc/ssl/certs/ca-bundle.crt > /dev/null
   ```

   After you generate the certificate, type the following command:

   ```
   sudo postconf -e 'smtp_tls_CAfile = /etc/ssl/certs/ca-bundle.crt'
   ```

8. Type the following command to start the Postfix server (or to reload the
   configuration settings if the server is already running):

```
sudo postfix start; sudo postfix reload
```

9. Send a test email by typing the following at a command line, pressing Enter
   after each line. Replace `sender@example.com` with your
   From email address. The From address has to be verified for use with Amazon SES.
   Replace `recipient@example.com` with the destination
   address. If your account is still in the sandbox, the recipient address also has
   to be verified. Finally, the final line of the message has to contain a single
   period (.) with no other content.

```
sendmail -f `sender@example.com` `recipient@example.com`
From: `Sender Name` <`sender@example.com`>
Subject: Amazon SES Test
This message was sent using Amazon SES.
.
```

10. Check the mailbox associated with the recipient address. If the email doesn't
    arrive, check your junk mail folder. If you still can't locate the email, check
    the mail log on the system that you used to send the email (typically located at
    `/var/log/maillog`) for more information.

## Advanced usage example

This example shows how to send an email that uses a [configuration set](using-configuration-sets.md "using-configuration-sets.md"), and that uses
MIME-multipart encoding to send both a plain text and an HTML version of the message,
along with an attachment. It also includes a [link tag](faqs-metrics.md#sending-metric-faqs-clicks-q5 "faqs-metrics.md#sending-metric-faqs-clicks-q5"), which can be used for
categorizing click events. The content of the email is specified in an external file, so
that you do not have to manually type the commands in the Postfix session.

###### To send a multipart MIME email using Postfix

1. In a text editor, create a new file called
   `mime-email.txt`.
2. In the text file, paste the following content, replacing the values in red
   with the appropriate values for your account:

```
X-SES-CONFIGURATION-SET: `ConfigSet`
From:`Sender Name` <`sender@example.com`>
Subject:Amazon SES Test
MIME-Version: 1.0
Content-Type: multipart/mixed; boundary="YWVhZDFlY2QzMGQ2N2U0YTZmODU"

--YWVhZDFlY2QzMGQ2N2U0YTZmODU
Content-Type: multipart/alternative; boundary="3NjM0N2QwMTE4MWQ0ZTg2NTYxZQ"

--3NjM0N2QwMTE4MWQ0ZTg2NTYxZQ
Content-Type: text/plain; charset=UTF-8
Content-Transfer-Encoding: quoted-printable

Amazon SES Test

This message was sent from Amazon SES using the SMTP interface.

For more information, see:
http://docs.aws.amazon.com/ses/latest/DeveloperGuide/send-email-smtp.html

--3NjM0N2QwMTE4MWQ0ZTg2NTYxZQ
Content-Type: text/html; charset=UTF-8
Content-Transfer-Encoding: quoted-printable

<html>
  <head>
</head>
  <body>
    <h1>Amazon SES Test</h1>
      <p>This message was sent from Amazon SES using the SMTP interface.</p>
      <p>For more information, see
      <a ses:tags="samplekey0:samplevalue0;samplekey1:samplevalue1;"
      href="http://docs.aws.amazon.com/ses/latest/DeveloperGuide/send-email-smtp.html">
      Using the Amazon SES SMTP Interface to Send Email</a> in the <em>Amazon SES
      Developer Guide</em>.</p>
  </body>
</html>
--3NjM0N2QwMTE4MWQ0ZTg2NTYxZQ--
--YWVhZDFlY2QzMGQ2N2U0YTZmODU
Content-Type: application/octet-stream
MIME-Version: 1.0
Content-Transfer-Encoding: base64
Content-Disposition: attachment; filename="customers.txt"

SUQsRmlyc3ROYW1lLExhc3ROYW1lLENvdW50cnkKMzQ4LEpvaG4sU3RpbGVzLENh
bmFkYQo5MjM4OSxKaWUsTGl1LENoaW5hCjczNCxTaGlybGV5LFJvZHJpZ3VleixV
bml0ZWQgU3RhdGVzCjI4OTMsQW5heWEsSXllbmdhcixJbmRpYQ==
--YWVhZDFlY2QzMGQ2N2U0YTZmODU--
```

Save and close the file. 3. At the command line, type the following command. Replace
`sender@example.com` with your email address, and
replace `recipient@example.com` with the recipient's
email address.

```
sendmail -f `sender@example.com` `recipient@example.com` < mime-email.txt
```

If the command runs successfully, it exits without providing any
output. 4. Check your inbox for the email. If the message wasn't delivered, check your
system's mail log.
