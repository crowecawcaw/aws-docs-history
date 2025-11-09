# Sending test emails in Amazon SES with the

simulator

We recommend using the Amazon SES console to send a test email with Amazon SES.
Because the console requires you to manually enter information, you typically only use it to
send test emails. After you get started with Amazon SES, you will most likely send your
emails by using either the Amazon SES SMTP interface or API. However,the console is
useful for monitoring your sending activity.

###### The following topics explain how to use the mailbox simulator from both

the console and manually by sending emails:

- [Using the mailbox simulator from the console](#send-test-email "#send-test-email")
- [Using the mailbox simulator manually](#send-email-simulator "#send-email-simulator")

## Using the mailbox simulator from the console

###### Important

- In this tutorial, you send an email to yourself from the console so that
  you can check to see if you received it. For further experimentation or load
  testing, see [Using the mailbox simulator manually](#send-email-simulator "#send-email-simulator").
- Emails that you send to the mailbox simulator do not count toward your
  sending quota or your bounce and complaint rates, nor do they affect Virtual Deliverability Manager
  metrics.

Before you follow these steps, complete the tasks in [Setting up Amazon Simple Email Service](setting-up.md "setting-up.md").

###### To send a test email message from the Amazon SES console

1. Sign in to the AWS Management Console and open the Amazon SES console at [https://console.aws.amazon.com/ses/](https://console.aws.amazon.com/ses/ "https://console.aws.amazon.com/ses/").
2. In the navigation pane under **Configuration** choose
   **Identities**.
3. From the **Identities** table, select a verified email
   identity (by clicking directly on the identity name as opposed to selecting its
   checkbox). _If you don't have a verified email identity, see [Creating an email address
   identity](creating-identities.md#verify-email-addresses-procedure "creating-identities.md#verify-email-addresses-procedure")._
4. On the selected email identity's detail page, choose **Send test
   email**.
5. For **Message details**, choose the **Email Format**. The two choices are as follows:
   - **Formatted**—This is the simplest option.
     Choose this option if you simply want to type the text of your message
     into the **Body** text box. When you send
     the email, Amazon SES puts the text into email format for you.
   - **Raw**—Choose this option if you want to send a
     more complex message, such as a message that includes HTML or an
     attachment. Because of this flexibility, you need to format the message,
     as described in [Sending raw email using the Amazon SES API v2](send-email-raw.md "send-email-raw.md"), yourself, and then paste the
     entire formatted message, including the headers, into the **Body** text box. You can use the following
     example, which contains HTML, to send a test email using the **Raw** email format. Copy and paste this message
     in its entirety into the **Body** text box.
     Ensure that there is not a blank line between the
     `MIME-Version` header and the `Content-Type`
     header; a blank line between these two lines causes the email to be
     formatted as plain text instead of HTML.

   ```
   Subject: Amazon SES Raw Email Test
   MIME-Version: 1.0
   Content-Type: text/html

   <!DOCTYPE html>
   <html>
   <body>
   <h1>This text should be large, because it is formatted as a header in HTML.</h1>
   <p>Here is a formatted link: <a href="https://docs.aws.amazon.com/ses/latest/DeveloperGuide/Welcome.html">Amazon Simple Email Service Developer Guide</a>.</p>
   </body>
   </html>
   ```

6. Choose the type of simulated email scenario you want to test by expanding the
   **Scenario** list box.
   1. If you choose **Custom** and you're still in the
      Amazon SES sandbox, make sure that the address in the
      **Custom recipient** field is a verified email
      address. For more information, see [Creating an email address
      identity](creating-identities.md#verify-email-addresses-procedure "creating-identities.md#verify-email-addresses-procedure").

7. Fill out the remaining fields as desired.
8. Choose **Send test email**.
9. Sign in to the email client of the address you sent the email to. You will
   find the message that you sent.

## Using the mailbox simulator manually

Amazon SES includes a mailbox simulator that you can use to test how your application
handles different email sending scenarios. The mailbox simulator is useful when, for
example, you want to test an email sending application without creating fictitious email
addresses, or when you want to find your system's maximum throughput without impacting
your daily sending quota.

### Important

considerations

Consider the following features and limitations when you use the Amazon SES mailbox
simulator:

- You can use the mailbox simulator even if your account is in the Amazon SES
  sandbox.
- Emails that you send to the mailbox simulator are limited by your
  account's maximum sending rate, but they don't affect your daily sending
  quota. For example, if your account is authorized to send 10,000 messages
  per 24-hour period, and you send 100 messages to the mailbox simulator, you
  can still send up to 10,000 messages to regular recipients without reaching
  your sending quota.
- Emails that you send to the mailbox simulator don't impact your email
  deliverability or reputation metrics. For example, if you send a large
  number of messages to the bounce address of the email simulator, it doesn't
  display a message warning you that your bounce rate is too high on the [reputation metrics console
  page](reputation-dashboard-dg.md "reputation-dashboard-dg.md").
- For billing purposes, emails that you send to the Amazon SES mailbox simulator
  are the same as any other email you send using Amazon SES. In other words, we
  bill you the same amount for messages that you send to the mailbox simulator
  as for those that you send to regular recipients.
- The mailbox simulator supports labeling, which enables you to send emails
  to the same mailbox simulator address in multiple ways, or to see how your
  application handles Variable Envelope Return Path (VERP). For example, you
  can send an email to
  *bounce+label1@simulator.amazonses.com* and
  *bounce+label2@simulator.amazonses.com* to see if
  your application can match a bounce message with the email address that
  caused the bounce.
- If you use the mailbox simulator to simulate multiple bounces from the
  same sending request, Amazon SES combines the bounce responses into a single
  response.

### Using the mailbox

simulator

To use the email simulator, find the scenario in the following table, and then
send an email to the corresponding email address.

###### Note

When you send an email to a mailbox simulator address, you must send it
through Amazon SES, by using the AWS CLI, an AWS SDK, the Amazon SES console, the Amazon SES
SMTP interface, or the Amazon SES API. The mailbox simulator doesn't respond to
emails that it receives from external sources.

| Simulated scenario                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | Email address                           |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------- |
| Successful delivery—The<br>recipient's email provider accepts your email. If you set up<br>delivery notifications as described in [Setting up event<br>notifications for Amazon SES](monitor-sending-activity-using-notifications.md "monitor-sending-activity-using-notifications.md"),<br>Amazon SES sends you a delivery notification through Amazon Simple Notification Service (Amazon SNS).                                                                                                                                                                                                                                                                                                                                                                                                                                                   | success@simulator.amazonses.com         |
| Bounce—The recipient's email<br>provider rejects your email with an SMTP 550 5.1.1 ("Unknown User")<br>response code. Amazon SES generates a bounce notification and, depending<br>on how you set up your account, sends it to you in an email or sends<br>a notification to an Amazon SNS topic. The mailbox simulator email<br>address isn't placed on the Amazon SES suppression list, which would<br>normally happen when a hard bounce occurs. The bounce response that<br>you receive from the mailbox simulator is compliant with [RFC 3464](https://tools.ietf.org/html/rfc3464 "https://tools.ietf.org/html/rfc3464"). For<br>information about how to receive bounce feedback, see [Setting up event<br>notifications for Amazon SES](monitor-sending-activity-using-notifications.md "monitor-sending-activity-using-notifications.md"). | bounce@simulator.amazonses.com          |
| Automatic responses—The<br>recipient's email provider accepts your email and delivers it to the<br>recipient’s inbox. The email provider sends an automatic response,<br>such as an "out of the office" (OOTO) message, to the address in the<br>Return-Path header of the email, or the envelope sender ("MAIL<br>FROM") address if the Return-Path header isn't present. The<br>automatic response that you receive from the mailbox simulator is<br>compliant with [RFC<br>3834](https://tools.ietf.org/html/rfc3834 "https://tools.ietf.org/html/rfc3834").                                                                                                                                                                                                                                                                                     | ooto@simulator.amazonses.com            |
| Complaint—The recipient's<br>email provider accepts your email and delivers it to the recipient’s<br>inbox. The recipient decides that your message is unsolicited and<br>clicks "Mark as Spam" in his or her email client. Amazon SES then<br>forwards the complaint notification to you by email or by notifying<br>an Amazon SNS topic, depending on how you set up your account. The<br>complaint response that you receive from the mailbox simulator is<br>compliant with [RFC<br>5965](https://tools.ietf.org/html/rfc5965 "https://tools.ietf.org/html/rfc5965"). For information about how to receive complaint<br>feedback, see [Setting up event<br>notifications for Amazon SES](monitor-sending-activity-using-notifications.md "monitor-sending-activity-using-notifications.md").                                                    | complaint@simulator.amazonses.com       |
| Recipient address on suppression<br>list—Amazon SES generates a hard bounce as if the<br>recipient's address is on the global suppression list.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | suppressionlist@simulator.amazonses.com |

### Testing Reject events

Every message that you send through Amazon SES is scanned for viruses. If you send a
message that contains a virus, Amazon SES accepts the message, detects the virus, and
rejects the entire message. When Amazon SES rejects the message, it stops processing the
message, and doesn't attempt to deliver it to the recipient's mail server. It then
generates a Reject event.

The Amazon SES mailbox simulator doesn't include an address for testing Reject events.
However, you can test Reject events by using a European Institute for Computer
Antivirus Research (EICAR) test file. This file is an industry-standard method of
testing antivirus software in a safe manner. To create an EICAR test file, paste the
following text into a file:

```
X5O!P%@AP[4\PZX54(P^)7CC)7}$EICAR-STANDARD-ANTIVIRUS-TEST-FILE!$H+H*
```

Save the file as `sample.txt`, attach it to an email, and then
send the email to a verified address. If there are no other issues with the email,
Amazon SES accepts the message, but then rejects it as it would if it contained an actual
virus.

###### Note

Rejected emails—including those that you send by using the procedure
above—count against your daily sending quota. We bill you for each message
that you send, including rejected messages.

To learn more about EICAR test files, see the [EICAR test file page on
Wikipedia](https://en.wikipedia.org/wiki/EICAR_test_file "https://en.wikipedia.org/wiki/EICAR_test_file").
