# Sending emails programmatically through

the Amazon SES SMTP interface

To send an email using the Amazon SES SMTP interface, you can use an SMTP-enabled programming
language, email server, or application. Before you start, complete the tasks in [Setting up Amazon Simple Email Service](setting-up.md "setting-up.md"). You also need to get the following
information:

- Your Amazon SES SMTP credentials, which enable you to connect to the Amazon SES SMTP
  endpoint. To get your Amazon SES SMTP credentials, see [Obtaining Amazon SES SMTP credentials](smtp-credentials.md "smtp-credentials.md").

###### Important

Your SMTP credentials are different from your AWS credentials. For more
information about credentials, see [Types of Amazon SES credentials](send-email-concepts-credentials.md "send-email-concepts-credentials.md").

- The SMTP endpoint address. For a list of Amazon SES SMTP endpoints, see [Connecting to an Amazon SES SMTP endpoint](smtp-connect.md "smtp-connect.md").
- The Amazon SES SMTP interface port number, which depends on the connection method. For
  more information, see [Connecting to an Amazon SES SMTP endpoint](smtp-connect.md "smtp-connect.md").

## Code examples

You can access the Amazon SES SMTP interface by using an SMTP-enabled programming language.
You provide the Amazon SES SMTP hostname and port number along with your SMTP credentials and
then use the programming language's generic SMTP functions to send the email.

Amazon Elastic Compute Cloud (Amazon EC2) restricts email traffic over port 25 by default. To avoid timeouts
when sending email through the SMTP endpoint from Amazon EC2, you can request that these
restrictions be removed. For more information, see [How do I
remove the restriction on port 25 from my Amazon EC2 instance or AWS Lambda
function?](https://aws.amazon.com/premiumsupport/knowledge-center/ec2-port-25-throttle/ "https://aws.amazon.com/premiumsupport/knowledge-center/ec2-port-25-throttle/") in the AWS Knowledge Center.

The code examples in this section for Java and PHP use port 587 to avoid this issue.

###### Note

In these tutorials, you send an email to yourself so that you can check to see if
you received it. For further experimentation or load testing, use the Amazon SES mailbox
simulator. Emails that you send to the mailbox simulator do not count toward your
sending quota or your bounce and complaint rates. For more information, see [Using the mailbox simulator manually](send-an-email-from-console.md#send-email-simulator "send-an-email-from-console.md#send-email-simulator").

**Select a programing language to view the example for that
language:**

###### Warning

Amazon SES does not recommend using static credentials. Refer to [AWS Secrets Manager](../../../secretsmanager/latest/userguide/intro.md "../../../secretsmanager/latest/userguide/intro.md") to learn how to improve your
security posture by removing hard-coded credentials from your source code. This
tutorial is only provided for the purpose of testing the Amazon SES SMTP interface in a
non-production environment.

Java
This example uses the [Eclipse
IDE](http://www.eclipse.org/ "http://www.eclipse.org/") and the [JavaMail API](https://github.com/javaee/javamail/releases "https://github.com/javaee/javamail/releases")
to send email through Amazon SES using the SMTP interface.

Before you perform the following procedure, complete the tasks in [Setting up Amazon Simple Email Service](setting-up.md "setting-up.md").

###### To send an email using the Amazon SES SMTP interface with Java

1. In a web browser, go to the [JavaMail
   GitHub page](https://github.com/javaee/javamail/releases "https://github.com/javaee/javamail/releases"). Under **Assets**, choose
   **javax.mail.jar** to download the latest
   version of JavaMail.

###### Important

This tutorial requires JavaMail version 1.5 or later. These
procedures were tested using JavaMail version 1.6.1. 2. In a web browser, go to the [Jakarta
Activation GitHub page](https://github.com/eclipse-ee4j/jaf/releases "https://github.com/eclipse-ee4j/jaf/releases"), and under [JavaBeans Activation Framework 1.2.1 Final Release](https://github.com/eclipse-ee4j/jaf/releases/tag/1.2.1 "https://github.com/eclipse-ee4j/jaf/releases/tag/1.2.1"),
download the **jakarta.activation.jar** 3. Create a project in Eclipse by performing the following
steps:

    1. Start Eclipse.
    2. In Eclipse, choose **File**,
     choose **New**, and then choose
     **Java Project**.
    3. In the **Create a Java
     Project** dialog box, type a project name and
     then choose **Next.**
    4. In the **Java Settings**
     dialog box, choose the **Libraries** tab.
    5. Select **Classpath** and add the two
     external jar files **javax.mail.jar** and
     **jakarta.activation.jar** using the
     **Add External JARs** button.
    6. Choose **Add External
     JARs**.
    7. Browse to the folder in which you downloaded JavaMail.
     Choose the file `javax.mail.jar`, and
     then choose **Open**.
    8. In the **Java Settings**
     dialog box, choose **Finish**.

4. In Eclipse, in the **Package
   Explorer** window, expand your project.
5. Under your project, right-click the **src** directory, choose **New**, and then choose **Class**.
6. In the **New Java Class** dialog box,
   in the **Name** field, type
   `AmazonSESSample` and then choose **Finish**.
7. Replace the entire contents of
   **AmazonSESSample.java** with the following
   code:

```
import java.util.Properties;

import javax.mail.Message;
import javax.mail.Session;
import javax.mail.Transport;
import javax.mail.internet.InternetAddress;
import javax.mail.internet.MimeMessage;

public class AmazonSESSample {

    // Replace sender@example.com with your "From" address.
    // This address must be verified.
    static final String FROM = "sender@example.com";
    static final String FROMNAME = "Sender Name";

    // Replace recipient@example.com with a "To" address. If your account
    // is still in the sandbox, this address must be verified.
    static final String TO = "recipient@example.com";

    // Replace smtp_username with your Amazon SES SMTP user name.
    static final String SMTP_USERNAME = "smtp_username";

    // The name of the Configuration Set to use for this message.
    // If you comment out or remove this variable, you will also need to
    // comment out or remove the header below.
    static final String CONFIGSET = "ConfigSet";

    // Amazon SES SMTP host name. This example uses the US West (Oregon) region.
    // See https://docs.aws.amazon.com/ses/latest/DeveloperGuide/regions.html#region-endpoints
    // for more information.
    static final String HOST = "email-smtp.us-west-2.amazonaws.com";

    // The port you will connect to on the Amazon SES SMTP endpoint.
    static final int PORT = 587;

    static final String SUBJECT = "Amazon SES test (SMTP interface accessed using Java)";

    static final String BODY = String.join(
            System.getProperty("line.separator"),
            "<h1>Amazon SES SMTP Email Test</h1>",
            "<p>This email was sent with Amazon SES using the ",
            "<a href='https://github.com/javaee/javamail'>Javamail Package</a>",
            " for <a href='https://www.java.com'>Java</a>."
        );

    public static void main(String[] args) throws Exception {

        // Create a Properties object to contain connection configuration information.
        Properties props = System.getProperties();
        props.put("mail.transport.protocol", "smtp");
        props.put("mail.smtp.port", PORT);
        props.put("mail.smtp.starttls.enable", "true");
        props.put("mail.smtp.auth", "true");

        // Create a Session object to represent a mail session with the specified properties.
        Session session = Session.getDefaultInstance(props);

        // Create a message with the specified information.
        MimeMessage msg = new MimeMessage(session);
        msg.setFrom(new InternetAddress(FROM,FROMNAME));
        msg.setRecipient(Message.RecipientType.TO, new InternetAddress(TO));
        msg.setSubject(SUBJECT);
        msg.setContent(BODY,"text/html");

        // Add a configuration set header. Comment or delete the
        // next line if you are not using a configuration set
        msg.setHeader("X-SES-CONFIGURATION-SET", CONFIGSET);

        // Create a transport.
        Transport transport = session.getTransport();

        // Get the password
        String SMTP_PASSWORD = fetchSMTPPasswordFromSecureStorage();

        // Send the message.
        try
        {
            System.out.println("Sending...");

            // Connect to Amazon SES using the SMTP username and password you specified above.
            transport.connect(HOST, SMTP_USERNAME, SMTP_PASSWORD);

            // Send the email.
            transport.sendMessage(msg, msg.getAllRecipients());
            System.out.println("Email sent!");
        }
        catch (Exception ex) {
            System.out.println("The email was not sent.");
            System.out.println("Error message: " + ex.getMessage());
        }
        finally
        {
            // Close and terminate the connection.
            transport.close();
        }
    }

    static String fetchSMTPPasswordFromSecureStorage() {
        /* IMPLEMENT THIS METHOD */
        // For example, you might fetch it from a secure location or AWS Secrets Manager: https://aws.amazon.com/secrets-manager/
    }
}
```

8. In **AmazonSESSample.java**, replace the
   following email addresses with your own values:

###### Important

The email addresses are case-sensitive. Make sure that the
addresses are exactly the same as the ones you verified.

    * `sender@example.com` –
     Replace with your "From" email address. You must verify this
     address before you run this program. For more information,
     see [Verified identities in Amazon SES](verify-addresses-and-domains.md "verify-addresses-and-domains.md").
    * `recipient@example.com` –
     Replace with your "To" email address. If your account is
     still in the sandbox, you must verify this address before
     you use it. For more information, see [Request production access (Moving out of the
     Amazon SES sandbox)](request-production-access.md "request-production-access.md").

9. In **AmazonSESSample.java** replace the following
   with your own values:
   - `smtp_username` – Replace
     with your SMTP user name credential. Note that your SMTP
     user name credential is a 20-character string of letters and
     numbers, not an intelligible name.
   - `smtp_password` –
     Implement `fetchSMTPPasswordFromSecureStorage`
     to fetch the password.

10. (Optional) If you want to use an Amazon SES SMTP endpoint in an
    AWS Region other than
    `email-smtp.us-west-2.amazonaws.com`, change the
    value of the variable `HOST` to the endpoint you want to
    use. For a list of regions where Amazon SES is available, see [Amazon Simple Email Service (Amazon SES)](../../../general/latest/gr/rande.md#ses_region "../../../general/latest/gr/rande.md#ses_region") in
    the _AWS General Reference_.
11. (Optional) If you want to use a configuration set when sending
    this email, change the value of the variable
    `ConfigSet` to the name of the
    configuration set. For more information about configuration sets,
    see [Using configuration sets in Amazon SES](using-configuration-sets.md "using-configuration-sets.md").
12. Save **AmazonSESSample.java**.
13. To build the project, choose **Project** and then choose **Build
    Project**. (If this option is disabled, then you may
    have automatic building enabled.)
14. To start the program and send the email, choose **Run** and then choose **Run** again.
15. Review the output. If the email was successfully sent, the console
    displays _"Email sent!"_ Otherwise, it displays
    an error message.
16. Sign into the email client of the recipient address. You will see
    the message that you sent.

PHP
This example uses the PHPMailer class to send email through Amazon SES using
the SMTP interface.

Before you perform the following procedure you must complete the tasks in
[Setting up Amazon Simple Email Service](setting-up.md "setting-up.md"). In addition to
setting up Amazon SES you must complete the following prerequisites to sending
email with PHP:

###### Prerequisites:

- Install PHP – PHP is
  available at [http://php.net/downloads.php](https://php.net/downloads.php "https://php.net/downloads.php"). After you install PHP,
  add the path to PHP in your environment variables so that you can
  run PHP from any command prompt.
- Install the Composer dependency
  manager – After you install the Composer
  dependency manager, you can download and install the PHPMailer class
  and its dependencies. To install Composer, follow the installation
  instructions at [https://getcomposer.org/download](https://getcomposer.org/download "https://getcomposer.org/download").
- Install the PHPMailer class
  – After you install Composer, run the following command to
  install PHPMailer:

```
`path/to/`composer require phpmailer/phpmailer
```

In the preceding command, replace
`path/to/` with the path where you
installed Composer.

###### To send an email using the Amazon SES SMTP interface with PHP

1. Create a file named
   **amazon-ses-smtp-sample.php**. Open the file
   with a text editor and paste in the following code:

```
<?php

// Import PHPMailer classes into the global namespace
// These must be at the top of your script, not inside a function
use PHPMailer\PHPMailer\PHPMailer;
use PHPMailer\PHPMailer\Exception;

// If necessary, modify the path in the require statement below to refer to the
// location of your Composer autoload.php file.
require 'vendor/autoload.php';

// Replace sender@example.com with your "From" address.
// This address must be verified with Amazon SES.
$sender = 'sender@example.com';
$senderName = 'Sender Name';

// Replace recipient@example.com with a "To" address. If your account
// is still in the sandbox, this address must be verified.
$recipient = 'recipient@example.com';

// Replace smtp_username with your Amazon SES SMTP user name.
$usernameSmtp = 'smtp_username';

// Specify a configuration set. If you do not want to use a configuration
// set, comment or remove the next line.
$configurationSet = 'ConfigSet';

// If you're using Amazon SES in a region other than US West (Oregon),
// replace email-smtp.us-west-2.amazonaws.com with the Amazon SES SMTP
// endpoint in the appropriate region.
$host = 'email-smtp.us-west-2.amazonaws.com';
$port = 587;

// The subject line of the email
$subject = 'Amazon SES test (SMTP interface accessed using PHP)';

// The plain-text body of the email
$bodyText =  "Email Test\r\nThis email was sent through the
    Amazon SES SMTP interface using the PHPMailer class.";

// The HTML-formatted body of the email
$bodyHtml = '<h1>Email Test</h1>
    <p>This email was sent through the
    <a href="https://aws.amazon.com/ses">Amazon SES</a> SMTP
    interface using the <a href="https://github.com/PHPMailer/PHPMailer">
    PHPMailer</a> class.</p>';

$mail = new PHPMailer(true);

try {
    // Specify the SMTP settings.
    $mail->isSMTP();
    $mail->setFrom($sender, $senderName);
    $mail->Username   = $usernameSmtp;
    $mail->Password   = fetchSMTPPasswordFromSecureStorage();
    $mail->Host       = $host;
    $mail->Port       = $port;
    $mail->SMTPAuth   = true;
    $mail->SMTPSecure = 'tls';
    $mail->addCustomHeader('X-SES-CONFIGURATION-SET', $configurationSet);

    // Specify the message recipients.
    $mail->addAddress($recipient);
    // You can also add CC, BCC, and additional To recipients here.

    // Specify the content of the message.
    $mail->isHTML(true);
    $mail->Subject    = $subject;
    $mail->Body       = $bodyHtml;
    $mail->AltBody    = $bodyText;
    $mail->Send();
    echo "Email sent!" , PHP_EOL;
} catch (phpmailerException $e) {
    echo "An error occurred. {$e->errorMessage()}", PHP_EOL; //Catch errors from PHPMailer.
} catch (Exception $e) {
    echo "Email not sent. {$mail->ErrorInfo}", PHP_EOL; //Catch errors from Amazon SES.
}
function fetchSMTPPasswordFromSecureStorage() {
/* IMPLEMENT THIS METHOD */
// For example, you might fetch it from a secure location or AWS Secrets Manager: https://aws.amazon.com/secrets-manager/
}

?>
```

2. In **amazon-ses-smtp-sample.php**, replace the
   following with your own values:
   - `sender@example.com` –
     Replace with an email address that you have verified with
     Amazon SES. For more information, see [Verified identities](verify-addresses-and-domains.md "verify-addresses-and-domains.md").
     Email addresses in Amazon SES are case-sensitive. Make sure that
     the address you enter is exactly the same as the one you
     verified.
   - `recipient@example.com` –
     Replace with the address of the recipient. If your account
     is still in the sandbox, you must verify this address before
     you use it. For more information, see [Request production access (Moving out of the
     Amazon SES sandbox)](request-production-access.md "request-production-access.md"). Make sure
     that the address you enter is exactly the same as the one
     you verified.
   - `smtp_username` – Replace
     with your SMTP user name credential, which you obtained from
     the [SMTP
     Settings](https://console.aws.amazon.com/ses/home?#smtp-settings: "https://console.aws.amazon.com/ses/home?#smtp-settings:") page of the Amazon SES console. This is
     **not** the same as your
     AWS access key ID. Note that your SMTP user name
     credential is a 20-character string of letters and numbers,
     not an intelligible name.
   - `smtp_password` –
     Implement `fetchSMTPPasswordFromSecureStorage`
     to fetch the password.
   - (Optional) `ConfigSet` –
     If you want to use a configuration set when sending this
     email, replace this value with the name of the configuration
     set. For more information about configuration sets, see
     [Using configuration sets in Amazon SES](using-configuration-sets.md "using-configuration-sets.md").
   - (Optional)
     `email-smtp.us-west-2.amazonaws.com`
     – If you want to use an Amazon SES SMTP endpoint in a
     Region other than US West (Oregon), replace this with the
     Amazon SES SMTP endpoint in the Region you want to use. For a
     list of SMTP endpoint URLs for the AWS Regions where Amazon SES
     is available, see [Amazon Simple Email Service (Amazon SES)](../../../general/latest/gr/rande.md#ses_region "../../../general/latest/gr/rande.md#ses_region") in the
     _AWS General Reference_.

3. Save **amazon-ses-smtp-sample.php**.
4. To run the program, open a command prompt in the same directory as
   **amazon-ses-smtp-sample.php**, and then type
   **php amazon-ses-smtp-sample.php**.
5. Review the output. If the email was successfully sent, the console
   displays _"Email sent!"_ Otherwise, it displays
   an error message.
6. Sign in to the email client of the recipient address. You will see
   the message that you sent.
