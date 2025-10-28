# Testing your connection to the Amazon SES

SMTP interface using the command line

You can use the methods described in this section from the command line to test your
connection to the Amazon SES SMTP endpoint, validate your SMTP credentials, and troubleshoot
connection issues. These procedures use tools and libraries that are included with most
common operating systems.

For additional information about troubleshooting SMTP connection problems, see [Amazon SES SMTP issues](troubleshoot-smtp.md "troubleshoot-smtp.md").

## Prerequisites

When you connect to the Amazon SES SMTP interface, you have to provide a set of SMTP
credentials. These SMTP credentials are different from your standard AWS credentials.
The two types of credentials aren't interchangeable. For more information about
obtaining your SMTP credentials, see [Obtaining Amazon SES SMTP credentials](smtp-credentials.md "smtp-credentials.md").

## Testing your connection to

the Amazon SES SMTP interface

You can use the command line to test your connection to the Amazon SES SMTP interface
without authenticating or sending any messages. This procedure is useful for
troubleshooting basic connectivity issues. If your test connection fails, see [SMTP issues](troubleshoot-smtp.md "troubleshoot-smtp.md").

This section includes procedures for testing your connection using both OpenSSL (which
is included with most Linux, macOS, and Unix distributions, and is also available for
Windows) and the `Test-NetConnection` cmdlet in PowerShell (which is
included with most recent versions of Windows).

Linux, macOS, or Unix
There are two ways to connect to the Amazon SES SMTP interface with OpenSSL:
using explicit SSL over port 587, or using implicit SSL over port 465.

###### To connect to the SMTP interface using explicit SSL

- At the command line, enter the following command to connect to the
  Amazon SES SMTP server:

```
openssl s_client -crlf -quiet -starttls smtp -connect `email-smtp.us-west-2.amazonaws.com`:587
```

In the preceding command, replace
`email-smtp.us-west-2.amazonaws.com` with the
URL of the Amazon SES SMTP endpoint for your AWS Region. For more
information, see [Regions and Amazon SES](regions.md "regions.md").

If the connection was successful, you see output similar to the
following:

```
depth=2 C = US, O = Amazon, CN = Amazon Root CA 1
verify return:1
depth=1 C = US, O = Amazon, OU = Server CA 1B, CN = Amazon
verify return:1
depth=0 CN = email-smtp.us-west-2.amazonaws.com
verify return:1
250 Ok
```

The connection automatically closes after about 10 seconds of
inactivity.

Alternatively, you can use implicit SSL to connect to the SMTP interface
over port 465.

###### To connect to the SMTP interface using implicit SSL

- At the command line, enter the following command to connect to the
  Amazon SES SMTP server:

```
openssl s_client -crlf -quiet -connect `email-smtp.us-west-2.amazonaws.com`:465
```

In the preceding command, replace
`email-smtp.us-west-2.amazonaws.com` with the
URL of the Amazon SES SMTP endpoint for your AWS Region. For more
information, see [Regions and Amazon SES](regions.md "regions.md").

If the connection was successful, you see output similar to the
following:

```
depth=2 C = US, O = Amazon, CN = Amazon Root CA 1
verify return:1
depth=1 C = US, O = Amazon, OU = Server CA 1B, CN = Amazon
verify return:1
depth=0 CN = email-smtp.us-west-2.amazonaws.com
verify return:1
220 email-smtp.amazonaws.com ESMTP SimpleEmailService-d-VCSHDP1YZ A1b2C3d4E5f6G7h8I9j0
```

The connection automatically closes after about 10 seconds of
inactivity.

PowerShell
You can use the [Test-NetConnection](https://docs.microsoft.com/en-us/powershell/module/nettcpip/test-netconnection "https://docs.microsoft.com/en-us/powershell/module/nettcpip/test-netconnection") cmdlet in PowerShell to connect to the
Amazon SES SMTP server.

###### Note

The `Test-NetConnection` cmdlet can determine whether your
computer can connect to the Amazon SES SMTP endpoint. However, it doesn't
test whether your computer can make an implicit or explicit SSL
connection to the SMTP endpoint. To test an SSL connection, you can
install OpenSSL for
Windows
to send a test email.

###### To connect to the SMTP interface using the

`Test-NetConnection` cmdlet

- In PowerShell, enter the following command to connect to the
  Amazon SES SMTP server:

```
Test-NetConnection -Port `587` -ComputerName `email-smtp.us-west-2.amazonaws.com`
```

In the preceding command, replace
`email-smtp.us-west-2.amazonaws.com` with the
URL of the Amazon SES SMTP endpoint for your AWS Region, and replace
`587` with the port number. For more
information about regional endpoints in Amazon SES, see [Regions and Amazon SES](regions.md "regions.md").

If the connection was successful, you see output that resembles
the following example:

```
ComputerName     : email-smtp.us-west-2.amazonaws.com
RemoteAddress    : 198.51.100.126
RemotePort       : 587
InterfaceAlias   : Ethernet
SourceAddress    : 203.0.113.46
TcpTestSucceeded : True
```

## Using the command line to send email using

the Amazon SES SMTP interface

You can also use the command line to send messages using the Amazon SES SMTP interface.
This procedure is useful for testing SMTP credentials and for testing the ability of
specific recipients to receive messages that you send by using Amazon SES.

Linux, macOS, or Unix
When an email sender connects to an SMTP server, the client issues a
standard set of requests, and the server replies to each request with a
standard response. This series of requests and responses is called an
_SMTP conversation_. When you connect to the Amazon SES
SMTP server using OpenSSL, the server expects an SMTP conversation to
occur.

When you use OpenSSL to connect to the SMTP interface, you have to encode
your SMTP credentials using base64 encoding. This section includes
procedures for encoding your credentials using base64.

###### To send an email from the command line using the SMTP

interface

1. Enter the following at the command line and replace
   `email-smtp.us-west-2.amazonaws.com` with the
   URL of the Amazon SES SMTP endpoint for your AWS Region. For more
   information, see [Regions and Amazon SES](regions.md "regions.md").:

```
#!/bin/bash

# Prompt user to provide following information
read -p "Configuration set: " CONFIGSET
read -p "Enter SMTP username: " SMTPUsername
read -p "Enter SMTP password: " SMTPPassword
read -p "Sender email address: " MAILFROM
read -p "Receiver email address: " RCPT
read -p "Email subject: " SUBJECT
read -p "Message to send: " DATA

echo

# Encode SMTP username and password using base64
EncodedSMTPUsername=$(echo -n "$SMTPUsername" | openssl enc -base64)
EncodedSMTPPassword=$(echo -n "$SMTPPassword" | openssl enc -base64)

# Construct the email
Email="EHLO example.com
AUTH LOGIN
$EncodedSMTPUsername
$EncodedSMTPPassword
MAIL FROM: $MAILFROM
RCPT TO: $RCPT
DATA
X-SES-CONFIGURATION-SET: $CONFIGSET
From: $MAILFROM
To: $RCPT
Subject: $SUBJECT

$DATA
.
QUIT"

echo "$Email" | openssl s_client -crlf -quiet -starttls smtp -connect `email-smtp.us-west-2.amazonaws.com`:587
```

2. At the prompt for each variable, enter your values.
3. - To send using implicit SSL over port 465, use:
     ``
	openssl s_client -crlf -quiet -connect `email-smtp.us-west-2.amazonaws.com`:465
	``
     If the message was accepted by Amazon SES, you see output that
     resembles the following example:

```
250 Ok 01010160d7de98d8-21e57d9a-JZho-416c-bbe1-8ebaAexample-000000
```

The string of numbers and text that follows `250 Ok` is
the message ID of the email.

###### Note

The connection closes automatically after about 10 seconds of
inactivity.

PowerShell
You can use the [Net.Mail.SmtpClient](https://docs.microsoft.com/en-us/dotnet/api/system.net.mail.smtpclient?view=netframework-4.8 "https://docs.microsoft.com/en-us/dotnet/api/system.net.mail.smtpclient?view=netframework-4.8") class to send email using explicit SSL over
port 587.

###### Note

The `Net.Mail.SmtpClient` class is officially obsolete, and
Microsoft recommends that you use third-party libraries. This code is
intended for testing purposes only, and shouldn't be used for production
workloads.

###### To send an email through PowerShell using explicit SSL

1. In a text editor, create a new file. Paste the following code into
   the file:

```
function SendEmail($Server, $Port, $Sender, $Recipient, $Subject, $Body) {
    $Credentials = [Net.NetworkCredential](Get-Credential)

    $SMTPClient = New-Object Net.Mail.SmtpClient($Server, $Port)
    $SMTPClient.EnableSsl = $true
    $SMTPClient.Credentials = New-Object System.Net.NetworkCredential($Credentials.Username, $Credentials.Password);

    try {
        Write-Output "Sending message..."
        $SMTPClient.Send($Sender, $Recipient, $Subject, $Body)
        Write-Output "Message successfully sent to $($Recipient)"
    } catch [System.Exception] {
        Write-Output "An error occurred:"
        Write-Error $_
    }
}

function SendTestEmail(){
    $Server = "`email-smtp.us-west-2.amazonaws.com`"
    $Port = 587

    $Subject = "Test email sent from Amazon SES"
    $Body = "This message was sent from Amazon SES using PowerShell (explicit SSL, port 587)."

    $Sender = "`sender@example.com`"
    $Recipient = "`recipient@example.com`"

    SendEmail $Server $Port $Sender $Recipient $Subject $Body
}

SendTestEmail
```

When you finish, save the file as
`SendEmail.ps1`. 2. Make the following changes to the file that you created in the
previous step:

    * Replace `sender@example.com` with
     the email address that you want to send the message
     from.
    * Replace `recipient@example.com`
     with the email address that you want to send the message
     to.
    * Replace
     `email-smtp.us-west-2.amazonaws.com`
     with the URL of the Amazon SES SMTP endpoint for your AWS
     Region. For more information, see [Regions and Amazon SES](regions.md "regions.md").

3. In PowerShell, enter the following command:

```
.\`path\to\SendEmail.ps1`
```

In the preceding command, replace
`path\to\SendEmail.ps1` with the path
to the file that you created in step 1. 4. When prompted, enter your SMTP user name and password.

Alternatively, you can use the [System.Web.Mail.SmtpMail](https://docs.microsoft.com/en-us/dotnet/api/system.web.mail.smtpmail?view=netframework-4.8 "https://docs.microsoft.com/en-us/dotnet/api/system.web.mail.smtpmail?view=netframework-4.8") class to send email using implicit SSL
over port 465.

###### Note

The `System.Web.Mail.SmtpMail` class is officially
obsolete, and Microsoft recommends that you use third-party libraries.
This code is intended for testing purposes only, and shouldn't be used
for production workloads.

###### To send an email through PowerShell using implicit SSL

1. In a text editor, create a new file. Paste the following code into
   the file:

```
[System.Reflection.Assembly]::LoadWithPartialName("System.Web") > $null

function SendEmail($Server, $Port, $Sender, $Recipient, $Subject, $Body) {
    $Credentials = [Net.NetworkCredential](Get-Credential)

    $mail = New-Object System.Web.Mail.MailMessage
    $mail.Fields.Add("http://schemas.microsoft.com/cdo/configuration/smtpserver", $Server)
    $mail.Fields.Add("http://schemas.microsoft.com/cdo/configuration/smtpserverport", $Port)
    $mail.Fields.Add("http://schemas.microsoft.com/cdo/configuration/smtpusessl", $true)
    $mail.Fields.Add("http://schemas.microsoft.com/cdo/configuration/sendusername", $Credentials.UserName)
    $mail.Fields.Add("http://schemas.microsoft.com/cdo/configuration/sendpassword", $Credentials.Password)
    $mail.Fields.Add("http://schemas.microsoft.com/cdo/configuration/smtpconnectiontimeout", $timeout / 1000)
    $mail.Fields.Add("http://schemas.microsoft.com/cdo/configuration/sendusing", 2)
    $mail.Fields.Add("http://schemas.microsoft.com/cdo/configuration/smtpauthenticate", 1)

    $mail.From = $Sender
    $mail.To = $Recipient
    $mail.Subject = $Subject
    $mail.Body = $Body

    try {
        Write-Output "Sending message..."
        [System.Web.Mail.SmtpMail]::Send($mail)
        Write-Output "Message successfully sent to $($Recipient)"
    } catch [System.Exception] {
        Write-Output "An error occurred:"
        Write-Error $_
    }
}

function SendTestEmail(){
    $Server = "`email-smtp.us-west-2.amazonaws.com`"
    $Port = 465

    $Subject = "Test email sent from Amazon SES"
    $Body = "This message was sent from Amazon SES using PowerShell (implicit SSL, port 465)."

    $Sender = "`sender@example.com`"
    $Recipient = "`recipient@example.com`"

    SendEmail $Server $Port $Sender $Recipient $Subject $Body
}

SendTestEmail
```

When you finish, save the file as
`SendEmail.ps1`. 2. Make the following changes to the file that you created in the
previous step:

    * Replace `sender@example.com` with
     the email address that you want to send the message
     from.
    * Replace `recipient@example.com`
     with the email address that you want to send the message
     to.
    * Replace
     `email-smtp.us-west-2.amazonaws.com`
     with the URL of the Amazon SES SMTP endpoint for your AWS
     Region. For more information, see [Regions and Amazon SES](regions.md "regions.md").

3. In PowerShell, enter the following command:

```
.\`path\to\SendEmail.ps1`
```

In the preceding command, replace
`path\to\SendEmail.ps1` with the path
to the file that you created in step 1. 4. When prompted, enter your SMTP user name and password.
