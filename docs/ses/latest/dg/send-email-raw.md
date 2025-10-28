# Sending raw email using the Amazon SES API v2

You can use the Amazon SES API v2 `SendEmail` operation with the content type
specified as `raw` to send customized messages to your recipients using the raw
email format.

## About email header fields

Simple Mail Transfer Protocol (SMTP) specifies how email messages are to be sent by
defining the mail envelope and some of its parameters, but it does not concern itself
with the content of the message. Instead, the Internet Message Format ([RFC 5322](https://www.ietf.org/rfc/rfc5322.txt "https://www.ietf.org/rfc/rfc5322.txt")) defines how the message
is to be constructed.

With the Internet Message Format specification, every email message consists of a
header and a body. The header consists of message metadata, and the body contains the
message itself. For more information about email headers and bodies, see [Email format in Amazon SES](send-email-concepts-email-format.md "send-email-concepts-email-format.md").

## Using raw email MIME message construction

The SMTP protocol was originally designed to send email messages that only contained
7-bit ASCII characters. This specification makes SMTP insufficient for non-ASCII text
encodings (such as Unicode), binary content, or attachments. The Multipurpose Internet
Mail Extensions standard (MIME) was developed to make it possible to send many other
kinds of content using SMTP.

The MIME standard works by breaking the message body into multiple parts and then
specifying what is to be done with each part. For example, one part of an email message
body might be plain text, while another might be HTML. In addition, MIME allows email
messages to contain one or more attachments. Message recipients can view the attachments
from within their email clients, or they can save the attachments.

The message header and content are separated by a blank line. Each part of the email
is separated by a boundary, a string of characters that denotes the beginning and ending
of each part.

The multipart message in the following example contains a text and an HTML part, and
an attachment. The attachment should be placed just below the [attachment headers](#send-email-mime-encoding-files "#send-email-mime-encoding-files") and is most often
encoded in `base64` as shown in this example.

```
From: "Sender Name" <sender@example.com>
To: recipient@example.com
Subject: Customer service contact info
Content-Type: multipart/mixed;
    boundary="a3f166a86b56ff6c37755292d690675717ea3cd9de81228ec2b76ed4a15d6d1a"

--a3f166a86b56ff6c37755292d690675717ea3cd9de81228ec2b76ed4a15d6d1a
Content-Type: multipart/alternative;
    boundary="sub_a3f166a86b56ff6c37755292d690675717ea3cd9de81228ec2b76ed4a15d6d1a"

--sub_a3f166a86b56ff6c37755292d690675717ea3cd9de81228ec2b76ed4a15d6d1a
Content-Type: text/plain; charset=iso-8859-1
Content-Transfer-Encoding: quoted-printable

Please see the attached file for a list of customers to contact.

--sub_a3f166a86b56ff6c37755292d690675717ea3cd9de81228ec2b76ed4a15d6d1a
Content-Type: text/html; charset=iso-8859-1
Content-Transfer-Encoding: quoted-printable

<html>
<head></head>
<body>
<h1>Hello!</h1>
<p>Please see the attached file for a list of customers to contact.</p>
</body>
</html>

--sub_a3f166a86b56ff6c37755292d690675717ea3cd9de81228ec2b76ed4a15d6d1a--

--a3f166a86b56ff6c37755292d690675717ea3cd9de81228ec2b76ed4a15d6d1a
Content-Type: text/plain; name="customers.txt"
Content-Description: customers.txt
Content-Disposition: attachment;filename="customers.txt";
    creation-date="Sat, 05 Aug 2017 19:35:36 GMT";
Content-Transfer-Encoding: base64

SUQsRmlyc3ROYW1lLExhc3ROYW1lLENvdW50cnkKMzQ4LEpvaG4sU3RpbGVzLENhbmFkYQo5MjM4
OSxKaWUsTGl1LENoaW5hCjczNCxTaGlybGV5LFJvZHJpZ3VleixVbml0ZWQgU3RhdGVzCjI4OTMs
QW5heWEsSXllbmdhcixJbmRpYQ==

--a3f166a86b56ff6c37755292d690675717ea3cd9de81228ec2b76ed4a15d6d1a--

```

The content type for the message is `multipart/mixed`, which indicates that
the message has many parts (in this example, a body and an attachment), and the
receiving client must handle each part separately.

Nested within the body section is a second part that uses the
`multipart/alternative` content type. This content type indicates that
each part contains alternative versions of the same content (in this case, a text
version and an HTML version). If the recipient's email client can display HTML content,
then it shows the HTML version of the message body. If the recipient's email client
can't display HTML content, then it shows the plain text version of the message
body.

Both versions of the message also contain an attachment (in this case, a short text
file that contains some customer names).

When you nest a MIME part within another part, as in this example, the nested part
must use a `boundary` parameter that is distinct from the
`boundary` parameter in the parent part. These boundaries should be
unique strings of characters. To define a boundary between MIME parts, type two hyphens
(--) followed by the boundary string. At the end of a MIME part, place two hyphens at
both the beginning and the end of the boundary string.

###### Note

A message cannot have more than 500 MIME parts.

### MIME Encoding

To maintain compatibility with older systems, Amazon SES honors the 7-bit ASCII
limitation of SMTP as defined in [RFC 2821](https://tools.ietf.org/html/rfc2821 "https://tools.ietf.org/html/rfc2821"). If you want to send content that contains non-ASCII
characters, you must encode those characters into a format that uses 7-bit ASCII
characters.

#### Email addresses

The email address string must be 7-bit ASCII. If you want to send to or from
email addresses that contain Unicode characters in the domain part of an
address, you must encode the domain using Punycode. Punycode is not permitted in
the local part of the email address (the part before the @ sign) nor in the
"friendly from" name. If you want to use Unicode characters in the "friendly
from" name, you must encode the "friendly from" name using MIME encoded-word
syntax, as described in this section. For more information about Punycode, see
[RFC 3492](http://tools.ietf.org/html/rfc3492 "http://tools.ietf.org/html/rfc3492").

###### Note

This rule only applies to email addresses that you specify in the message
envelope, not the message headers. When you use the Amazon SES API v2
`SendEmail` operation, the addresses you specify in the
`Source` and `Destinations`
parameters define the envelope sender and recipients, respectively.

#### Email headers

To encode a message header, use MIME encoded-word syntax. MIME encoded word
syntax uses the following format:

```
=?`charset`?`encoding`?`encoded-text`?=
```

The value of `encoding` can be either
`Q` or `B`. If the value of encoding is
`Q`, then the value
`encoded-text` has to use Q-encoding.
If the value of encoding is `B`, then the value of
`encoded-text` has to use base64
encoding.

For example, if you want to use the string
"Як ти поживаєш?"
in the subject line of an email, you can use either of the following
encodings:

- Q-encoding

```
=?utf-8?Q?=D0=AF=D0=BA_=D1=82=D0=B8_=D0=BF=D0=BE=D0=B6=D0=B8=D0=B2=D0=B0=D1=94=D1=88=3F?=
```

- Base64 encoding

```
=?utf-8?B?0K/QuiDRgtC4INC/0L7QttC40LLQsNGU0Yg/?=
```

For more information about Q-encoding, see [RFC 2047](https://tools.ietf.org/html/rfc2047 "https://tools.ietf.org/html/rfc2047"). For more
information about base64 encoding, see [RFC 2045](https://tools.ietf.org/html/rfc2045 "https://tools.ietf.org/html/rfc2045").

#### Message body

To encode the body of a message, you can use quoted-printable encoding or
base64 encoding. Then, use the `Content-Transfer-Encoding`
header to indicate which encoding scheme you used.

For example, assume the body of your message contains the following text:

१९७२ मे रे
टॉमलिंसन ने
पहला ई-मेल
संदेश भेजा |
रे टॉमलिंसन
ने ही
सर्वप्रथम @
चिन्ह का चयन
किया और इन्ही
को ईमेल का
आविष्कारक
माना जाता है

If you choose to encode this text using base64 encoding, first specify the
following header:

```
Content-Transfer-Encoding: base64
```

Then, in the body section of the email, include the base64-encoded
text:

```
4KWn4KWv4KWt4KWoIOCkruClhyDgpLDgpYcg4KSf4KWJ4KSu4KSy4KS/4KSC4KS44KSoIOCkqOCl
hyDgpKrgpLngpLLgpL4g4KSILeCkruClh+CksiDgpLjgpILgpKbgpYfgpLYg4KSt4KWH4KSc4KS+
IHwg4KSw4KWHIOCkn+ClieCkruCksuCkv+CkguCkuOCkqCDgpKjgpYcg4KS54KWAIOCkuOCksOCl
jeCkteCkquCljeCksOCkpeCkriBAIOCkmuCkv+CkqOCljeCkuSDgpJXgpL4g4KSa4KSv4KSoIOCk
leCkv+Ckr+CkviDgpJTgpLAg4KSH4KSo4KWN4KS54KWAIOCkleCliyDgpIjgpK7gpYfgpLIg4KSV
4KS+IOCkhuCkteCkv+Ckt+CljeCkleCkvuCksOCklSDgpK7gpL7gpKjgpL4g4KSc4KS+4KSk4KS+
IOCkueCliAo=
```

###### Note

In some cases, you can use the 8bit `Content-Transfer-Encoding`
in messages that you send using Amazon SES. However, if Amazon SES has to make any
changes to your messages (for example, when you use [open and click tracking](faqs-metrics.md "faqs-metrics.md")), 8-bit-encoded
content might not appear correctly when it arrives in recipients' inboxes.
For this reason, you should always encode content that isn't 7-bit
ASCII.

#### File attachments

To attach a file to an email, you have to encode the attachment using base64
encoding. Attachments are typically placed in dedicated MIME message parts,
which include the following headers:

- Content-Type – The file type of
  the attachment. The following are examples of common MIME Content-Type
  declarations:
  - Plain text file –
    `Content-Type: text/plain;
name="sample.txt"`
  - Microsoft Word Document
    – `Content-Type: application/msword;
name="document.docx"`
  - JPG image –
    `Content-Type: image/jpeg;
name="photo.jpeg"`

- Content-Disposition – Specifies
  how the recipient's email client should handle the content. For
  attachments, this value is `Content-Disposition:
attachment`.
- Content-Transfer-Encoding – The
  scheme that was used to encode the attachment. For file attachments,
  this value is almost always `base64`.
- The encoded attachment – You
  must encode the actual attachment and include it in the body below the
  attachment headers as [shown in the
  example](#send-email-raw-mime "#send-email-raw-mime").

Amazon SES accepts most common file types. For a list of file types that Amazon SES
doesn't accept, see [SES unsupported attachment types](attachments.md#mime-types "attachments.md#mime-types").

## Sending raw email using the Amazon SES API v2

The Amazon SES API v2 provides the `SendEmail` action, which lets you compose and
send an email message in the format that you specify when you set the content type to
either simple, raw, or templated. For a complete description, see [`SendEmail`](../APIReference-V2/API_SendEmail.md "../APIReference-V2/API_SendEmail.md"). The following example will specify the content
type as `raw` to send a messages using the raw email format.

###### Note

For tips on how to increase your email sending speed when you make multiple calls
to `SendEmail`, see [Increasing throughput with Amazon SES](troubleshoot-throughput-problems.md "troubleshoot-throughput-problems.md").

The message body must contain a properly formatted, raw email message, with
appropriate header fields and message body encoding. Although it's possible to construct
the raw message manually within an application, it's much easier to do so using existing
mail libraries.

Java
The following code example shows how to use the [JavaMail](https://javaee.github.io/javamail/ "https://javaee.github.io/javamail/") library and
the [AWS SDK for Java](https://aws.amazon.com/sdk-for-java "https://aws.amazon.com/sdk-for-java") to compose
and send a raw email.

```
package com.amazonaws.samples;

import java.io.ByteArrayOutputStream;
import java.io.IOException;
import java.io.PrintStream;
import java.nio.ByteBuffer;
import java.util.Properties;

// JavaMail libraries. Download the JavaMail API
// from https://javaee.github.io/javamail/
import javax.activation.DataHandler;
import javax.activation.DataSource;
import javax.activation.FileDataSource;
import javax.mail.Message;
import javax.mail.MessagingException;
import javax.mail.Session;
import javax.mail.internet.AddressException;
import javax.mail.internet.InternetAddress;
import javax.mail.internet.MimeBodyPart;
import javax.mail.internet.MimeMessage;
import javax.mail.internet.MimeMultipart;

// AWS SDK libraries. Download the AWS SDK for Java
// from https://aws.amazon.com/sdk-for-java
import com.amazonaws.regions.Regions;
import com.amazonaws.services.simpleemail.AmazonSimpleEmailService;
import com.amazonaws.services.simpleemail.AmazonSimpleEmailServiceClientBuilder;
import com.amazonaws.services.simpleemail.model.RawMessage;
import com.amazonaws.services.simpleemail.model.SendRawEmailRequest;

public class AmazonSESSample {

	// Replace sender@example.com with your "From" address.
	// This address must be verified with Amazon SES.
	private static String SENDER = "`Sender Name` <`sender@example.com`>";

	// Replace recipient@example.com with a "To" address. If your account
	// is still in the sandbox, this address must be verified.
	private static String RECIPIENT = "`recipient@example.com`";

	// Specify a configuration set. If you do not want to use a configuration
	// set, comment the following variable, and the
	// ConfigurationSetName=CONFIGURATION_SET argument below.
	private static String CONFIGURATION_SET = "`ConfigSet`";

	// The subject line for the email.
	private static String SUBJECT = "Customer service contact info";

	// The full path to the file that will be attached to the email.
	// If you're using Windows, escape backslashes as shown in this variable.
	private static String ATTACHMENT = "C:\\Users\\sender\\customers-to-contact.xlsx";

	// The email body for recipients with non-HTML email clients.
	private static String BODY_TEXT = "Hello,\r\n"
                                        + "Please see the attached file for a list "
                                        + "of customers to contact.";

	// The HTML body of the email.
	private static String BODY_HTML = "<html>"
                                        + "<head></head>"
                                        + "<body>"
                                        + "<h1>Hello!</h1>"
                                        + "<p>Please see the attached file for a "
                                        + "list of customers to contact.</p>"
                                        + "</body>"
                                        + "</html>";

    public static void main(String[] args) throws AddressException, MessagingException, IOException {

    	Session session = Session.getDefaultInstance(new Properties());

        // Create a new MimeMessage object.
        MimeMessage message = new MimeMessage(session);

        // Add subject, from and to lines.
        message.setSubject(SUBJECT, "UTF-8");
        message.setFrom(new InternetAddress(SENDER));
        message.setRecipients(Message.RecipientType.TO, InternetAddress.parse(RECIPIENT));

        // Create a multipart/alternative child container.
        MimeMultipart msg_body = new MimeMultipart("alternative");

        // Create a wrapper for the HTML and text parts.
        MimeBodyPart wrap = new MimeBodyPart();

        // Define the text part.
        MimeBodyPart textPart = new MimeBodyPart();
        textPart.setContent(BODY_TEXT, "text/plain; charset=UTF-8");

        // Define the HTML part.
        MimeBodyPart htmlPart = new MimeBodyPart();
        htmlPart.setContent(BODY_HTML,"text/html; charset=UTF-8");

        // Add the text and HTML parts to the child container.
        msg_body.addBodyPart(textPart);
        msg_body.addBodyPart(htmlPart);

        // Add the child container to the wrapper object.
        wrap.setContent(msg_body);

        // Create a multipart/mixed parent container.
        MimeMultipart msg = new MimeMultipart("mixed");

        // Add the parent container to the message.
        message.setContent(msg);

        // Add the multipart/alternative part to the message.
        msg.addBodyPart(wrap);

        // Define the attachment
        MimeBodyPart att = new MimeBodyPart();
        DataSource fds = new FileDataSource(ATTACHMENT);
        att.setDataHandler(new DataHandler(fds));
        att.setFileName(fds.getName());

        // Add the attachment to the message.
        msg.addBodyPart(att);

        // Try to send the email.
        try {
            System.out.println("Attempting to send an email through Amazon SES "
                              +"using the AWS SDK for Java...");

            // Instantiate an Amazon SES client, which will make the service
            // call with the supplied AWS credentials.
            AmazonSimpleEmailService client =
                    AmazonSimpleEmailServiceClientBuilder.standard()
                    // Replace US_WEST_2 with the AWS Region you're using for
                    // Amazon SES.
                    .withRegion(Regions.US_WEST_2).build();

            // Print the raw email content on the console
            PrintStream out = System.out;
            message.writeTo(out);

            // Send the email.
            ByteArrayOutputStream outputStream = new ByteArrayOutputStream();
            message.writeTo(outputStream);
            RawMessage rawMessage =
            		new RawMessage(ByteBuffer.wrap(outputStream.toByteArray()));

            SendRawEmailRequest rawEmailRequest =
            		new SendRawEmailRequest(rawMessage)
            		    .withConfigurationSetName(CONFIGURATION_SET);

            client.sendRawEmail(rawEmailRequest);
            System.out.println("Email sent!");
        // Display an error if something goes wrong.
        } catch (Exception ex) {
          System.out.println("Email Failed");
            System.err.println("Error message: " + ex.getMessage());
            ex.printStackTrace();
        }
    }
}
```

Python
The following code example shows how to use the [Python
email.mime](https://docs.python.org/3.8/library/email.mime.html "https://docs.python.org/3.8/library/email.mime.html") packages and the [AWS SDK for Python (Boto)](https://aws.amazon.com/sdk-for-python "https://aws.amazon.com/sdk-for-python") to compose and
send a raw email.

```
import json
import boto3
from botocore.exceptions import ClientError
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
import os

def boto3_rawemailv2():
    SENDER = "Sender <sender@example.com>"
    RECIPIENT = "recipient@example.com"
    CONFIGURATION_SET = "ConfigSet"
    AWS_REGION = "us-east-1"
    SUBJECT = "Customer service contact info"
    ATTACHMENT = "path/to/customers-to-contact.xlsx"
    BODY_TEXT = "Hello,\r\nPlease see the attached file for a list of customers to contact."

    # The HTML body of the email.
    BODY_HTML = """\
    <html>
    <head/>
    <body>
    <h1>Hello!</h1>
    <p>Please see the attached file for a list of customers to contact.</p>
    </body>
    </html>
    """

    # The character encoding for the email.
    CHARSET = "utf-8"
    msg = MIMEMultipart('mixed')
    # Add subject, from and to lines.
    msg['Subject'] = SUBJECT
    msg['From'] = SENDER
    msg['To'] = RECIPIENT

    # Create a multipart/alternative child container.
    msg_body = MIMEMultipart('alternative')

    # Encode the text and HTML content and set the character encoding. This step is
    # necessary if you're sending a message with characters outside the ASCII range.
    textpart = MIMEText(BODY_TEXT.encode(CHARSET), 'plain', CHARSET)
    htmlpart = MIMEText(BODY_HTML.encode(CHARSET), 'html', CHARSET)

    # Add the text and HTML parts to the child container.
    msg_body.attach(textpart)
    msg_body.attach(htmlpart)

    # Define the attachment part and encode it using MIMEApplication.
    att = MIMEApplication(open(ATTACHMENT, 'rb').read())

    # Add a header to tell the email client to treat this part as an attachment,
    # and to give the attachment a name.
    att.add_header('Content-Disposition','attachment',filename=os.path.basename(ATTACHMENT))

    # Attach the multipart/alternative child container to the multipart/mixed
    # parent container.
    msg.attach(msg_body)
    msg.attach(att)

    #changes start from here
    strmsg = str(msg)
    body = bytes (strmsg, 'utf-8')




    client = boto3.client('sesv2')
    response = client.send_email(
    FromEmailAddress=SENDER,
    Destination={
        'ToAddresses': [RECIPIENT]
    },
    Content={
        'Raw': {
            'Data': body
        }
    }
    )
    print(response)
boto3_rawemailv2 ()
```
