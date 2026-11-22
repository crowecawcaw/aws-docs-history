

# Sending emails programmatically over SMTP

Use an SMTP-enabled programming language or application to send email through Amazon SES. Before you start, complete the tasks in [Getting started with sending email](getting-started-sending.md).

Get the SMTP endpoint, user name, and password from one of the following credential topics:
+ [Creating SMTP credentials using Mail Manager](smtp-credentials-mail-manager.md) (recommended)
+ [Obtaining Amazon SES SMTP credentials using IAM](smtp-credentials.md)

The examples use STARTTLS on port `587`, which both SMTP options support. For other settings, see [Choose SMTP connection settings](smtp-connect.md).

**Important**  
Do not use your AWS access key ID and secret access key as SMTP credentials. For more information, see [Types of Amazon SES credentials](send-email-concepts-credentials.md).

## Code examples
<a name="send-email-smtp-code-examples"></a>

Provide the SMTP endpoint, port, user name, and password to your programming language's SMTP library. The library connects and sends the email.

Amazon Elastic Compute Cloud (Amazon EC2) restricts email traffic over port `25` by default. To avoid timeouts, request removal of the restriction or use port `587`. For more information, see [How do I remove the restriction on port 25 from my Amazon EC2 instance or AWS Lambda function?](https://aws.amazon.com/premiumsupport/knowledge-center/ec2-port-25-throttle/) in the AWS Knowledge Center.

**Note**  
In these tutorials, you send an email to yourself so that you can check to see if you received it. For further experimentation or load testing, use the Amazon SES mailbox simulator. Emails that you send to the mailbox simulator do not count toward your sending quota or your bounce and complaint rates. For more information, see [Using the mailbox simulator manually](send-an-email-from-console.md#send-email-simulator).

**Select a programing language to view the example for that language:**

**Warning**  
Do not store SMTP credentials in your source code. Use secure storage such as [AWS Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/intro.html). These examples are for testing in a non-production environment.

------
#### [ Java ]

This example uses the [Eclipse IDE](http://www.eclipse.org/) and the [JavaMail API](https://github.com/javaee/javamail/releases) to send email through Amazon SES over SMTP.

Before you perform the following procedure, complete the tasks in [Getting started with sending email](getting-started-sending.md).

**To send an email over SMTP with Java**

1. In a web browser, go to the [JavaMail GitHub page](https://github.com/javaee/javamail/releases). Under **Assets**, choose **javax.mail.jar** to download the latest version of JavaMail.
**Important**  
This tutorial requires JavaMail version 1.5 or later. These procedures were tested using JavaMail version 1.6.1.

1. In a web browser, go to the [Jakarta Activation GitHub page](https://github.com/eclipse-ee4j/jaf/releases), and under [JavaBeans Activation Framework 1.2.1 Final Release](https://github.com/eclipse-ee4j/jaf/releases/tag/1.2.1), download the **jakarta.activation.jar**

1. Create a project in Eclipse by performing the following steps:

   1. Start Eclipse.

   1. In Eclipse, choose **File**, choose **New**, and then choose **Java Project**.

   1. In the **Create a Java Project** dialog box, type a project name and then choose **Next.**

   1. In the **Java Settings** dialog box, choose the **Libraries** tab.

   1. Select **Classpath** and add the two external jar files **javax.mail.jar** and **jakarta.activation.jar** using the **Add External JARs** button.

   1. Choose **Add External JARs**.

   1. Browse to the folder in which you downloaded JavaMail. Choose the file `javax.mail.jar`, and then choose **Open**.

   1. In the **Java Settings** dialog box, choose **Finish**.

1. In Eclipse, in the **Package Explorer** window, expand your project.

1. Under your project, right-click the **src** directory, choose **New**, and then choose **Class**.

1. In the **New Java Class** dialog box, in the **Name** field, type `AmazonSESSample` and then choose **Finish**.

1. Replace the entire contents of **AmazonSESSample.java** with the following code:

   ```java
    1. import java.util.Properties;
    2. 
    3. import javax.mail.Message;
    4. import javax.mail.Session;
    5. import javax.mail.Transport;
    6. import javax.mail.internet.InternetAddress;
    7. import javax.mail.internet.MimeMessage;
    8. 
    9. public class AmazonSESSample {
   10. 
   11.     // Replace sender@example.com with your "From" address.
   12.     // This address must be verified.
   13.     static final String FROM = "sender@example.com";
   14.     static final String FROMNAME = "Sender Name";
   15.     
   16.     // Replace recipient@example.com with a "To" address. If your account 
   17.     // is still in the sandbox, this address must be verified.
   18.     static final String TO = "recipient@example.com";
   19.     
   20.     // Replace smtp_username with the user name from your SMTP credentials.
   21.     static final String SMTP_USERNAME = "smtp_username";
   22. 
   23.     // The name of the configuration set to use for this message.
   24.     static final String CONFIGURATION_SET = "ConfigSet";
   25.     
   26.     // Replace smtp_endpoint with the endpoint from your SMTP credentials.
   27.     static final String HOST = "smtp_endpoint";
   28.     
   29.     // Both SMTP credential types support STARTTLS on port 587.
   30.     static final int PORT = 587;
   31.     
   32.     static final String SUBJECT = "Amazon SES test email sent over SMTP";
   33.     
   34.     static final String BODY = String.join(
   35.             System.getProperty("line.separator"),
   36.             "<h1>Amazon SES SMTP Email Test</h1>",
   37.             "<p>This email was sent with Amazon SES using the ", 
   38.             "<a href='https://github.com/javaee/javamail'>Javamail Package</a>",
   39.             " for <a href='https://www.java.com'>Java</a>."
   40.         );
   41. 
   42.     public static void main(String[] args) throws Exception {
   43. 
   44.         // Create a Properties object to contain connection configuration information.
   45.         Properties props = System.getProperties();
   46.         props.put("mail.transport.protocol", "smtp");
   47.         props.put("mail.smtp.port", PORT); 
   48.         props.put("mail.smtp.starttls.enable", "true");
   49.         props.put("mail.smtp.auth", "true");
   50. 
   51.         // Create a Session object to represent a mail session with the specified properties. 
   52.         Session session = Session.getDefaultInstance(props);
   53. 
   54.         // Create a message with the specified information. 
   55.         MimeMessage msg = new MimeMessage(session);
   56.         msg.setFrom(new InternetAddress(FROM,FROMNAME));
   57.         msg.setRecipient(Message.RecipientType.TO, new InternetAddress(TO));
   58.         msg.setSubject(SUBJECT);
   59.         msg.setContent(BODY,"text/html");
   60. 
   61.         // Add the configuration set header.
   62.         msg.setHeader("X-SES-CONFIGURATION-SET", CONFIGURATION_SET);
   63.             
   64.         // Create a transport.
   65.         Transport transport = session.getTransport();
   66. 
   67.         // Get the password 
   68.         String SMTP_PASSWORD = fetchSMTPPasswordFromSecureStorage();
   69.                     
   70.         // Send the message.
   71.         try
   72.         {
   73.             System.out.println("Sending...");
   74.             
   75.             // Connect using the SMTP endpoint, user name, and password specified above.
   76.             transport.connect(HOST, SMTP_USERNAME, SMTP_PASSWORD);
   77.             
   78.             // Send the email.
   79.             transport.sendMessage(msg, msg.getAllRecipients());
   80.             System.out.println("Email sent!");
   81.         }
   82.         catch (Exception ex) {
   83.             System.out.println("The email was not sent.");
   84.             System.out.println("Error message: " + ex.getMessage());
   85.         }
   86.         finally
   87.         {
   88.             // Close and terminate the connection.
   89.             transport.close();
   90.         }
   91.     }
   92. 
   93.     static String fetchSMTPPasswordFromSecureStorage() {
   94.         /* IMPLEMENT THIS METHOD */
   95.         // For example, you might fetch it from a secure location or AWS Secrets Manager: https://aws.amazon.com/secrets-manager/
   96.     }
   97. }
   ```

1. In **AmazonSESSample.java**, replace the following email addresses with your own values:
**Important**  
The email addresses are case-sensitive. Make sure that the addresses are exactly the same as the ones you verified.
   + {{sender@example.com}} – Replace with your "From" email address. You must verify this address before you run this program. For more information, see [Verified identities in Amazon SES](verify-addresses-and-domains.md).
   + {{recipient@example.com}} – Replace with your "To" email address. If your account is still in the sandbox, you must verify this address before you use it. For more information, see [Request production access (Moving out of the Amazon SES sandbox)](request-production-access.md).

1. In **AmazonSESSample.java** replace the following with your own values:
   + {{smtp\_username}} – Replace with the user name from your SMTP credentials.
   + {{smtp\_password}} – Implement ``fetchSMTPPasswordFromSecureStorage`` to fetch the password.

1. Replace {{smtp\_endpoint}} with the endpoint from your SMTP credentials.

1. (Optional) To use a configuration set, set `CONFIGURATION_SET` to its name. For more information, see [Specifying a configuration set when you send email](using-configuration-sets-in-email.md).

1. Save **AmazonSESSample.java**.

1. To build the project, choose **Project** and then choose **Build Project**. (If this option is disabled, then you may have automatic building enabled.)

1. To start the program and send the email, choose **Run** and then choose **Run** again.

1. Review the output. If the email was successfully sent, the console displays *"Email sent\!"* Otherwise, it displays an error message.

1. Sign into the email client of the recipient address. You will see the message that you sent.

------
#### [ PHP  ]

This example uses the PHPMailer class to send email through Amazon SES over SMTP.

Before you perform the following procedure you must complete the tasks in [Getting started with sending email](getting-started-sending.md). In addition to setting up Amazon SES you must complete the following prerequisites to sending email with PHP:

**Prerequisites:**
+ **Install PHP** – PHP is available at [http://php.net/downloads.php](https://php.net/downloads.php). After you install PHP, add the path to PHP in your environment variables so that you can run PHP from any command prompt.
+ **Install the Composer dependency manager** – After you install the Composer dependency manager, you can download and install the PHPMailer class and its dependencies. To install Composer, follow the installation instructions at [https://getcomposer.org/download](https://getcomposer.org/download).
+ **Install the PHPMailer class** – After you install Composer, run the following command to install PHPMailer: 

  ```
  {{path/to/}}composer require phpmailer/phpmailer
  ```

  In the preceding command, replace {{path/to/}} with the path where you installed Composer.

**To send an email over SMTP with PHP**

1. Create a file named **amazon-ses-smtp-sample.php**. Open the file with a text editor and paste in the following code:

   ```php
    1. <?php
    2. 
    3. // Import PHPMailer classes into the global namespace
    4. // These must be at the top of your script, not inside a function
    5. use PHPMailer\PHPMailer\PHPMailer;
    6. use PHPMailer\PHPMailer\Exception;
    7. 
    8. // If necessary, modify the path in the require statement below to refer to the
    9. // location of your Composer autoload.php file.
   10. require 'vendor/autoload.php';
   11. 
   12. // Replace sender@example.com with your "From" address.
   13. // This address must be verified with Amazon SES.
   14. $sender = 'sender@example.com';
   15. $senderName = 'Sender Name';
   16. 
   17. // Replace recipient@example.com with a "To" address. If your account
   18. // is still in the sandbox, this address must be verified.
   19. $recipient = 'recipient@example.com';
   20. 
   21. // Replace smtp_username with the user name from your SMTP credentials.
   22. $usernameSmtp = 'smtp_username';
   23. 
   24. // The name of the configuration set to use for this message.
   25. $configurationSet = 'ConfigSet';
   26. 
   27. // Replace smtp_endpoint with the endpoint from your SMTP credentials.
   28. $host = 'smtp_endpoint';
   29. 
   30. // Both SMTP credential types support STARTTLS on port 587.
   31. $port = 587;
   32. 
   33. // The subject line of the email
   34. $subject = 'Amazon SES test email sent over SMTP';
   35. 
   36. // The plain-text body of the email
   37. $bodyText =  "Email Test\r\nThis email was sent to Amazon SES over SMTP
   38.     using the PHPMailer class.";
   39. 
   40. // The HTML-formatted body of the email
   41. $bodyHtml = '<h1>Email Test</h1>
   42.     <p>This email was sent to
   43.     <a href="https://aws.amazon.com/ses">Amazon SES</a> over SMTP
   44.     using the <a href="https://github.com/PHPMailer/PHPMailer">
   45.     PHPMailer</a> class.</p>';
   46. 
   47. $mail = new PHPMailer(true);
   48. 
   49. try {
   50.     // Specify the SMTP settings.
   51.     $mail->isSMTP();
   52.     $mail->setFrom($sender, $senderName);
   53.     $mail->Username   = $usernameSmtp;
   54.     $mail->Password   = fetchSMTPPasswordFromSecureStorage();
   55.     $mail->Host       = $host;
   56.     $mail->Port       = $port;
   57.     $mail->SMTPAuth   = true;
   58.     $mail->SMTPSecure = 'tls';
   59. 
   60.     // Add the configuration set header.
   61.     $mail->addCustomHeader('X-SES-CONFIGURATION-SET', $configurationSet);
   62. 
   63.     // Specify the message recipients.
   64.     $mail->addAddress($recipient);
   65.     // You can also add CC, BCC, and additional To recipients here.
   66. 
   67.     // Specify the content of the message.
   68.     $mail->isHTML(true);
   69.     $mail->Subject    = $subject;
   70.     $mail->Body       = $bodyHtml;
   71.     $mail->AltBody    = $bodyText;
   72.     $mail->Send();
   73.     echo "Email sent!" , PHP_EOL;
   74. } catch (phpmailerException $e) {
   75.     echo "An error occurred. {$e->errorMessage()}", PHP_EOL; //Catch errors from PHPMailer.
   76. } catch (Exception $e) {
   77.     echo "Email not sent. {$mail->ErrorInfo}", PHP_EOL; //Catch errors from Amazon SES.
   78. }
   79. function fetchSMTPPasswordFromSecureStorage() {
   80. /* IMPLEMENT THIS METHOD */
   81. // For example, you might fetch it from a secure location or AWS Secrets Manager: https://aws.amazon.com/secrets-manager/
   82. }
   83. 
   84. ?>
   ```

1. In **amazon-ses-smtp-sample.php**, replace the following with your own values:
   + {{sender@example.com}} – Replace with an email address that you have verified with Amazon SES. For more information, see [Verified identities](verify-addresses-and-domains.md). Email addresses in Amazon SES are case-sensitive. Make sure that the address you enter is exactly the same as the one you verified.
   + {{recipient@example.com}} – Replace with the address of the recipient. If your account is still in the sandbox, you must verify this address before you use it. For more information, see [Request production access (Moving out of the Amazon SES sandbox)](request-production-access.md). Make sure that the address you enter is exactly the same as the one you verified.
   + {{smtp\_username}} – Replace with the user name from your SMTP credentials.
   + {{smtp\_password}} – Implement ``fetchSMTPPasswordFromSecureStorage`` to fetch the password.
   + {{smtp\_endpoint}} – Replace with the endpoint from your SMTP credentials.
   + (Optional) {{configurationSet}} – To use a configuration set, set this value to its name. For more information, see [Specifying a configuration set when you send email](using-configuration-sets-in-email.md).

1. Save **amazon-ses-smtp-sample.php**.

1. To run the program, open a command prompt in the same directory as **amazon-ses-smtp-sample.php**, and then type **php amazon-ses-smtp-sample.php**.

1. Review the output. If the email was successfully sent, the console displays *"Email sent\!"* Otherwise, it displays an error message.

1. Sign in to the email client of the recipient address. You will see the message that you sent.

------