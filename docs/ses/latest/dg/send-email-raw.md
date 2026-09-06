

# Sending raw email using the Amazon SES API v2
<a name="send-email-raw"></a>

You can use the Amazon SES API v2 `SendEmail` operation with the content type specified as `raw` to send customized messages to your recipients using the raw email format.

## About email header fields
<a name="send-email-raw-headers"></a>

Simple Mail Transfer Protocol (SMTP) specifies how email messages are to be sent by defining the mail envelope and some of its parameters, but it does not concern itself with the content of the message. Instead, the Internet Message Format ([RFC 5322](https://www.ietf.org/rfc/rfc5322.txt)) defines how the message is to be constructed.

With the Internet Message Format specification, every email message consists of a header and a body. The header consists of message metadata, and the body contains the message itself. For more information about email headers and bodies, see [Email format in Amazon SES](send-email-concepts-email-format.md).

## Using raw email MIME message construction
<a name="send-email-raw-mime"></a>

The SMTP protocol was originally designed to send email messages that only contained 7-bit ASCII characters. This specification makes SMTP insufficient for non-ASCII text encodings (such as Unicode), binary content, or attachments. The Multipurpose Internet Mail Extensions standard (MIME) was developed to make it possible to send many other kinds of content using SMTP.

The MIME standard works by breaking the message body into multiple parts and then specifying what is to be done with each part. For example, one part of an email message body might be plain text, while another might be HTML. In addition, MIME allows email messages to contain one or more attachments. Message recipients can view the attachments from within their email clients, or they can save the attachments.

The message header and content are separated by a blank line. Each part of the email is separated by a boundary, a string of characters that denotes the beginning and ending of each part.

The multipart message in the following example contains a text and an HTML part, and an attachment. The attachment should be placed just below the [attachment headers](#send-email-mime-encoding-files) and is most often encoded in `base64` as shown in this example.

```
 1. From: "Sender Name" <sender@example.com>
 2. To: recipient@example.com
 3. Subject: Customer service contact info
 4. Content-Type: multipart/mixed;
 5.     boundary="a3f166a86b56ff6c37755292d690675717ea3cd9de81228ec2b76ed4a15d6d1a"
 6. 
 7. --a3f166a86b56ff6c37755292d690675717ea3cd9de81228ec2b76ed4a15d6d1a
 8. Content-Type: multipart/alternative;
 9.     boundary="sub_a3f166a86b56ff6c37755292d690675717ea3cd9de81228ec2b76ed4a15d6d1a"
10. 
11. --sub_a3f166a86b56ff6c37755292d690675717ea3cd9de81228ec2b76ed4a15d6d1a
12. Content-Type: text/plain; charset=iso-8859-1
13. Content-Transfer-Encoding: quoted-printable
14. 
15. Please see the attached file for a list of customers to contact.
16. 
17. --sub_a3f166a86b56ff6c37755292d690675717ea3cd9de81228ec2b76ed4a15d6d1a
18. Content-Type: text/html; charset=iso-8859-1
19. Content-Transfer-Encoding: quoted-printable
20. 
21. <html>
22. <head></head>
23. <body>
24. <h1>Hello!</h1>
25. <p>Please see the attached file for a list of customers to contact.</p>
26. </body>
27. </html>
28. 
29. --sub_a3f166a86b56ff6c37755292d690675717ea3cd9de81228ec2b76ed4a15d6d1a--
30. 
31. --a3f166a86b56ff6c37755292d690675717ea3cd9de81228ec2b76ed4a15d6d1a
32. Content-Type: text/plain; name="customers.txt"
33. Content-Description: customers.txt
34. Content-Disposition: attachment;filename="customers.txt";
35.     creation-date="Sat, 05 Aug 2017 19:35:36 GMT";
36. Content-Transfer-Encoding: base64
37. 
38. SUQsRmlyc3ROYW1lLExhc3ROYW1lLENvdW50cnkKMzQ4LEpvaG4sU3RpbGVzLENhbmFkYQo5MjM4
39. OSxKaWUsTGl1LENoaW5hCjczNCxTaGlybGV5LFJvZHJpZ3VleixVbml0ZWQgU3RhdGVzCjI4OTMs
40. QW5heWEsSXllbmdhcixJbmRpYQ==
41. 
42. --a3f166a86b56ff6c37755292d690675717ea3cd9de81228ec2b76ed4a15d6d1a--
```

The content type for the message is `multipart/mixed`, which indicates that the message has many parts (in this example, a body and an attachment), and the receiving client must handle each part separately.

Nested within the body section is a second part that uses the `multipart/alternative` content type. This content type indicates that each part contains alternative versions of the same content (in this case, a text version and an HTML version). If the recipient's email client can display HTML content, then it shows the HTML version of the message body. If the recipient's email client can't display HTML content, then it shows the plain text version of the message body.

Both versions of the message also contain an attachment (in this case, a short text file that contains some customer names).

When you nest a MIME part within another part, as in this example, the nested part must use a `boundary` parameter that is distinct from the `boundary` parameter in the parent part. These boundaries should be unique strings of characters. To define a boundary between MIME parts, type two hyphens (--) followed by the boundary string. At the end of a MIME part, place two hyphens at both the beginning and the end of the boundary string.

**Note**  
A message cannot have more than 500 MIME parts.

### MIME Encoding
<a name="send-email-mime-encoding"></a>

To maintain compatibility with older systems, Amazon SES honors the 7-bit ASCII limitation of SMTP as defined in [RFC 2821](https://tools.ietf.org/html/rfc2821). If you want to send content that contains non-ASCII characters, you must encode those characters into a format that uses 7-bit ASCII characters.

#### Email addresses
<a name="send-email-mime-encoding-addresses"></a>

The email address string must be 7-bit ASCII. If you want to send to or from email addresses that contain Unicode characters in the domain part of an address, you must encode the domain using Punycode. Punycode is not permitted in the local part of the email address (the part before the @ sign) nor in the "friendly from" name. If you want to use Unicode characters in the "friendly from" name, you must encode the "friendly from" name using MIME encoded-word syntax, as described in this section. For more information about Punycode, see [RFC 3492](http://tools.ietf.org/html/rfc3492).

**Note**  
This rule only applies to email addresses that you specify in the message envelope, not the message headers. When you use the Amazon SES API v2 `SendEmail` operation, the addresses you specify in the `Source` and `Destinations` parameters define the envelope sender and recipients, respectively.

#### Email headers
<a name="send-email-mime-encoding-headers"></a>

To encode a message header, use MIME encoded-word syntax. MIME encoded word syntax uses the following format:

```
=?{{charset}}?{{encoding}}?{{encoded-text}}?=
```

The value of `{{encoding}}` can be either `Q` or `B`. If the value of encoding is `Q`, then the value `{{encoded-text}}` has to use Q-encoding. If the value of encoding is `B`, then the value of `{{encoded-text}}` has to use base64 encoding.

For example, if you want to use the string "Як ти поживаєш?" in the subject line of an email, you can use either of the following encodings:
+ **Q-encoding**

  ```
  =?utf-8?Q?=D0=AF=D0=BA_=D1=82=D0=B8_=D0=BF=D0=BE=D0=B6=D0=B8=D0=B2=D0=B0=D1=94=D1=88=3F?=
  ```
+ **Base64 encoding**

  ```
  =?utf-8?B?0K/QuiDRgtC4INC/0L7QttC40LLQsNGU0Yg/?=
  ```

For more information about Q-encoding, see [RFC 2047](https://tools.ietf.org/html/rfc2047). For more information about base64 encoding, see [RFC 2045](https://tools.ietf.org/html/rfc2045).

#### Message body
<a name="send-email-mime-encoding-body"></a>

To encode the body of a message, you can use quoted-printable encoding or base64 encoding. Then, use the `Content-Transfer-Encoding` header to indicate which encoding scheme you used.

For example, assume the body of your message contains the following text: 

१९७२ मे रे टॉमलिंसन ने पहला ई-मेल संदेश भेजा \| रे टॉमलिंसन ने ही सर्वप्रथम @ चिन्ह का चयन किया और इन्ही को ईमेल का आविष्कारक माना जाता है

If you choose to encode this text using base64 encoding, first specify the following header:

```
Content-Transfer-Encoding: base64
```

Then, in the body section of the email, include the base64-encoded text:

```
4KWn4KWv4KWt4KWoIOCkruClhyDgpLDgpYcg4KSf4KWJ4KSu4KSy4KS/4KSC4KS44KSoIOCkqOCl
hyDgpKrgpLngpLLgpL4g4KSILeCkruClh+CksiDgpLjgpILgpKbgpYfgpLYg4KSt4KWH4KSc4KS+
IHwg4KSw4KWHIOCkn+ClieCkruCksuCkv+CkguCkuOCkqCDgpKjgpYcg4KS54KWAIOCkuOCksOCl
jeCkteCkquCljeCksOCkpeCkriBAIOCkmuCkv+CkqOCljeCkuSDgpJXgpL4g4KSa4KSv4KSoIOCk
leCkv+Ckr+CkviDgpJTgpLAg4KSH4KSo4KWN4KS54KWAIOCkleCliyDgpIjgpK7gpYfgpLIg4KSV
4KS+IOCkhuCkteCkv+Ckt+CljeCkleCkvuCksOCklSDgpK7gpL7gpKjgpL4g4KSc4KS+4KSk4KS+
IOCkueCliAo=
```

**Note**  
In some cases, you can use the 8bit `Content-Transfer-Encoding` in messages that you send using Amazon SES. However, if Amazon SES has to make any changes to your messages (for example, when you use [open and click tracking](faqs-metrics.md)), 8-bit-encoded content might not appear correctly when it arrives in recipients' inboxes. For this reason, you should always encode content that isn't 7-bit ASCII.

#### File attachments
<a name="send-email-mime-encoding-files"></a>

To attach a file to an email, you have to encode the attachment using base64 encoding. Attachments are typically placed in dedicated MIME message parts, which include the following headers:
+ **Content-Type** – The file type of the attachment. The following are examples of common MIME Content-Type declarations:
  + **Plain text file** – `Content-Type: text/plain; name="sample.txt"`
  + **Microsoft Word Document** – `Content-Type: application/msword; name="document.docx"`
  + **JPG image** – `Content-Type: image/jpeg; name="photo.jpeg"`
+ **Content-Disposition** – Specifies how the recipient's email client should handle the content. For attachments, this value is `Content-Disposition: attachment`.
+ **Content-Transfer-Encoding** – The scheme that was used to encode the attachment. For file attachments, this value is almost always `base64`.
+ **The encoded attachment** – You must encode the actual attachment and include it in the body below the attachment headers as [shown in the example](#send-email-raw-mime).

Amazon SES accepts most common file types. For a list of file types that Amazon SES doesn't accept, see [SES unsupported attachment types](attachments.md#mime-types).

## Sending raw email using the Amazon SES API v2
<a name="send-email-raw-api"></a>

The Amazon SES API v2 provides the `SendEmail` action, which lets you compose and send an email message in the format that you specify when you set the content type to either simple, raw, or templated. For a complete description, see [`SendEmail`](https://docs.aws.amazon.com/ses/latest/APIReference-V2/API_SendEmail.html). The following example will specify the content type as `raw` to send a messages using the raw email format.

**Note**  
For tips on how to increase your email sending speed when you make multiple calls to `SendEmail`, see [Increasing throughput with Amazon SES](troubleshoot-throughput-problems.md).

The message body must contain a properly formatted, raw email message, with appropriate header fields and message body encoding. Although it's possible to construct the raw message manually within an application, it's much easier to do so using existing mail libraries. 

------
#### [ Java ]

The following code example shows how to use the [JavaMail](https://javaee.github.io/javamail/) library and the [AWS SDK for Java](https://aws.amazon.com/sdk-for-java) to compose and send a raw email.

```
  1. package com.amazonaws.samples;
  2. 
  3. import java.io.ByteArrayOutputStream;
  4. import java.io.IOException;
  5. import java.io.PrintStream;
  6. import java.nio.ByteBuffer;
  7. import java.util.Properties;
  8. 
  9. // JavaMail libraries. Download the JavaMail API 
 10. // from https://javaee.github.io/javamail/
 11. import javax.activation.DataHandler;
 12. import javax.activation.DataSource;
 13. import javax.activation.FileDataSource;
 14. import javax.mail.Message;
 15. import javax.mail.MessagingException;
 16. import javax.mail.Session;
 17. import javax.mail.internet.AddressException;
 18. import javax.mail.internet.InternetAddress;
 19. import javax.mail.internet.MimeBodyPart;
 20. import javax.mail.internet.MimeMessage;
 21. import javax.mail.internet.MimeMultipart;
 22. 
 23. // AWS SDK libraries. Download the AWS SDK for Java 
 24. // from https://aws.amazon.com/sdk-for-java
 25. import com.amazonaws.regions.Regions;
 26. import com.amazonaws.services.simpleemail.AmazonSimpleEmailService;
 27. import com.amazonaws.services.simpleemail.AmazonSimpleEmailServiceClientBuilder;
 28. import com.amazonaws.services.simpleemail.model.RawMessage;
 29. import com.amazonaws.services.simpleemail.model.SendRawEmailRequest;
 30. 
 31. public class AmazonSESSample {
 32. 
 33. 	// Replace sender@example.com with your "From" address.
 34. 	// This address must be verified with Amazon SES.
 35. 	private static String SENDER = "{{Sender Name}} <{{sender@example.com}}>";
 36. 
 37. 	// Replace recipient@example.com with a "To" address. If your account 
 38. 	// is still in the sandbox, this address must be verified.
 39. 	private static String RECIPIENT = "{{recipient@example.com}}";
 40. 
 41. 	// Specify a configuration set. If you do not want to use a configuration
 42. 	// set, comment the following variable, and the 
 43. 	// ConfigurationSetName=CONFIGURATION_SET argument below.
 44. 	private static String CONFIGURATION_SET = "{{ConfigSet}}";
 45. 
 46. 	// The subject line for the email.
 47. 	private static String SUBJECT = "Customer service contact info";
 48. 
 49. 	// The full path to the file that will be attached to the email.
 50. 	// If you're using Windows, escape backslashes as shown in this variable.
 51. 	private static String ATTACHMENT = "C:\\Users\\sender\\customers-to-contact.xlsx";
 52. 
 53. 	// The email body for recipients with non-HTML email clients.
 54. 	private static String BODY_TEXT = "Hello,\r\n"
 55.                                         + "Please see the attached file for a list "
 56.                                         + "of customers to contact.";
 57. 
 58. 	// The HTML body of the email.
 59. 	private static String BODY_HTML = "<html>"
 60.                                         + "<head></head>"
 61.                                         + "<body>"
 62.                                         + "<h1>Hello!</h1>"
 63.                                         + "<p>Please see the attached file for a "
 64.                                         + "list of customers to contact.</p>"
 65.                                         + "</body>"
 66.                                         + "</html>";
 67. 
 68.     public static void main(String[] args) throws AddressException, MessagingException, IOException {
 69.             	
 70.     	Session session = Session.getDefaultInstance(new Properties());
 71.         
 72.         // Create a new MimeMessage object.
 73.         MimeMessage message = new MimeMessage(session);
 74.         
 75.         // Add subject, from and to lines.
 76.         message.setSubject(SUBJECT, "UTF-8");
 77.         message.setFrom(new InternetAddress(SENDER));
 78.         message.setRecipients(Message.RecipientType.TO, InternetAddress.parse(RECIPIENT));
 79. 
 80.         // Create a multipart/alternative child container.
 81.         MimeMultipart msg_body = new MimeMultipart("alternative");
 82.         
 83.         // Create a wrapper for the HTML and text parts.        
 84.         MimeBodyPart wrap = new MimeBodyPart();
 85.         
 86.         // Define the text part.
 87.         MimeBodyPart textPart = new MimeBodyPart();
 88.         textPart.setContent(BODY_TEXT, "text/plain; charset=UTF-8");
 89.                 
 90.         // Define the HTML part.
 91.         MimeBodyPart htmlPart = new MimeBodyPart();
 92.         htmlPart.setContent(BODY_HTML,"text/html; charset=UTF-8");
 93.                 
 94.         // Add the text and HTML parts to the child container.
 95.         msg_body.addBodyPart(textPart);
 96.         msg_body.addBodyPart(htmlPart);
 97.         
 98.         // Add the child container to the wrapper object.
 99.         wrap.setContent(msg_body);
100.         
101.         // Create a multipart/mixed parent container.
102.         MimeMultipart msg = new MimeMultipart("mixed");
103.         
104.         // Add the parent container to the message.
105.         message.setContent(msg);
106.         
107.         // Add the multipart/alternative part to the message.
108.         msg.addBodyPart(wrap);
109.         
110.         // Define the attachment
111.         MimeBodyPart att = new MimeBodyPart();
112.         DataSource fds = new FileDataSource(ATTACHMENT);
113.         att.setDataHandler(new DataHandler(fds));
114.         att.setFileName(fds.getName());
115.         
116.         // Add the attachment to the message.
117.         msg.addBodyPart(att);
118. 
119.         // Try to send the email.
120.         try {
121.             System.out.println("Attempting to send an email through Amazon SES "
122.                               +"using the AWS SDK for Java...");
123. 
124.             // Instantiate an Amazon SES client, which will make the service 
125.             // call with the supplied AWS credentials.
126.             AmazonSimpleEmailService client = 
127.                     AmazonSimpleEmailServiceClientBuilder.standard()
128.                     // Replace US_WEST_2 with the AWS Region you're using for
129.                     // Amazon SES.
130.                     .withRegion(Regions.US_WEST_2).build();
131.             
132.             // Print the raw email content on the console
133.             PrintStream out = System.out;
134.             message.writeTo(out);
135. 
136.             // Send the email.
137.             ByteArrayOutputStream outputStream = new ByteArrayOutputStream();
138.             message.writeTo(outputStream);
139.             RawMessage rawMessage = 
140.             		new RawMessage(ByteBuffer.wrap(outputStream.toByteArray()));
141. 
142.             SendRawEmailRequest rawEmailRequest = 
143.             		new SendRawEmailRequest(rawMessage)
144.             		    .withConfigurationSetName(CONFIGURATION_SET);
145.             
146.             client.sendRawEmail(rawEmailRequest);
147.             System.out.println("Email sent!");
148.         // Display an error if something goes wrong.
149.         } catch (Exception ex) {
150.           System.out.println("Email Failed");
151.             System.err.println("Error message: " + ex.getMessage());
152.             ex.printStackTrace();
153.         }
154.     }
155. }
```

------
#### [ Python ]

The following code example shows how to use the [Python email.mime](https://docs.python.org/3.8/library/email.mime.html) packages and the [AWS SDK for Python (Boto)](https://aws.amazon.com/sdk-for-python) to compose and send a raw email.

```
 1. import json
 2. import boto3
 3. from botocore.exceptions import ClientError
 4. from email.mime.multipart import MIMEMultipart
 5. from email.mime.text import MIMEText
 6. from email.mime.application import MIMEApplication
 7. import os
 8. 
 9. def boto3_rawemailv2():
10.     SENDER = "Sender <sender@example.com>"
11.     RECIPIENT = "recipient@example.com"
12.     CONFIGURATION_SET = "ConfigSet"
13.     AWS_REGION = "us-east-1"
14.     SUBJECT = "Customer service contact info"
15.     ATTACHMENT = "path/to/customers-to-contact.xlsx"
16.     BODY_TEXT = "Hello,\r\nPlease see the attached file for a list of customers to contact."
17. 
18.     # The HTML body of the email.
19.     BODY_HTML = """\
20.     <html>
21.     <head/>
22.     <body>
23.     <h1>Hello!</h1>
24.     <p>Please see the attached file for a list of customers to contact.</p>
25.     </body>
26.     </html>
27.     """
28. 
29.     # The character encoding for the email.
30.     CHARSET = "utf-8"
31.     msg = MIMEMultipart('mixed')
32.     # Add subject, from and to lines.
33.     msg['Subject'] = SUBJECT 
34.     msg['From'] = SENDER 
35.     msg['To'] = RECIPIENT
36.     
37.     # Create a multipart/alternative child container.
38.     msg_body = MIMEMultipart('alternative')
39.     
40.     # Encode the text and HTML content and set the character encoding. This step is
41.     # necessary if you're sending a message with characters outside the ASCII range.
42.     textpart = MIMEText(BODY_TEXT.encode(CHARSET), 'plain', CHARSET)
43.     htmlpart = MIMEText(BODY_HTML.encode(CHARSET), 'html', CHARSET)
44.     
45.     # Add the text and HTML parts to the child container.
46.     msg_body.attach(textpart)
47.     msg_body.attach(htmlpart)
48.     
49.     # Define the attachment part and encode it using MIMEApplication.
50.     att = MIMEApplication(open(ATTACHMENT, 'rb').read())
51.     
52.     # Add a header to tell the email client to treat this part as an attachment,
53.     # and to give the attachment a name.
54.     att.add_header('Content-Disposition','attachment',filename=os.path.basename(ATTACHMENT))
55.     
56.     # Attach the multipart/alternative child container to the multipart/mixed
57.     # parent container.
58.     msg.attach(msg_body)
59.     msg.attach(att)
60. 
61.     #changes start from here
62.     strmsg = str(msg)
63.     body = bytes (strmsg, 'utf-8')
64. 
65. 
66. 
67.     
68.     client = boto3.client('sesv2')
69.     response = client.send_email(
70.     FromEmailAddress=SENDER,
71.     Destination={
72.         'ToAddresses': [RECIPIENT]
73.     },
74.     Content={
75.         'Raw': {
76.             'Data': body
77.         }
78.     }
79.     )
80.     print(response)
81. boto3_rawemailv2 ()
```

------