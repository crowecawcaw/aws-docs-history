

# Sending emails programmatically through the Amazon SES SMTP interface
<a name="send-using-smtp-programmatically"></a>

To send an email using the Amazon SES SMTP interface, you can use an SMTP-enabled programming language, email server, or application. Before you start, complete the tasks in [Setting up Amazon Simple Email Service](setting-up.md). You also need to get the following information: 
+ Your Amazon SES SMTP credentials, which enable you to connect to the Amazon SES SMTP endpoint. To get your Amazon SES SMTP credentials, see [Obtaining Amazon SES SMTP credentials](smtp-credentials.md). 
**Important**  
Your SMTP credentials are different from your AWS credentials. For more information about credentials, see [Types of Amazon SES credentials](send-email-concepts-credentials.md).
+ The SMTP endpoint address. For a list of Amazon SES SMTP endpoints, see [Connecting to an Amazon SES SMTP endpoint](smtp-connect.md).
+ The Amazon SES SMTP interface port number, which depends on the connection method. For more information, see [Connecting to an Amazon SES SMTP endpoint](smtp-connect.md).

## Code examples
<a name="send-email-smtp-code-examples"></a>

You can access the Amazon SES SMTP interface by using an SMTP-enabled programming language. You provide the Amazon SES SMTP hostname and port number along with your SMTP credentials and then use the programming language's generic SMTP functions to send the email.

Amazon Elastic Compute Cloud (Amazon EC2) restricts email traffic over port 25 by default. To avoid timeouts when sending email through the SMTP endpoint from Amazon EC2, you can request that these restrictions be removed. For more information, see [How do I remove the restriction on port 25 from my Amazon EC2 instance or AWS Lambda function?](https://aws.amazon.com/premiumsupport/knowledge-center/ec2-port-25-throttle/) in the AWS Knowledge Center.

The code examples in this section for Java and PHP use port 587 to avoid this issue. 

**Note**  
In these tutorials, you send an email to yourself so that you can check to see if you received it. For further experimentation or load testing, use the Amazon SES mailbox simulator. Emails that you send to the mailbox simulator do not count toward your sending quota or your bounce and complaint rates. For more information, see [Using the mailbox simulator manually](send-an-email-from-console.md#send-email-simulator).

**Select a programing language to view the example for that language:**

**Warning**  
Amazon SES does not recommend using static credentials. Refer to [AWS Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/intro.html) to learn how to improve your security posture by removing hard-coded credentials from your source code. This tutorial is only provided for the purpose of testing the Amazon SES SMTP interface in a non-production environment.

------
#### [ Java ]

This example uses the [Eclipse IDE](http://www.eclipse.org/) and the [JavaMail API](https://github.com/javaee/javamail/releases) to send email through Amazon SES using the SMTP interface.

Before you perform the following procedure, complete the tasks in [Setting up Amazon Simple Email Service](setting-up.md).

**To send an email using the Amazon SES SMTP interface with Java**

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

   ```
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
    20.     // Replace smtp_username with your Amazon SES SMTP user name.
    21.     static final String SMTP_USERNAME = "smtp_username";
    22.       
    23.     // The name of the Configuration Set to use for this message.
    24.     // If you comment out or remove this variable, you will also need to
    25.     // comment out or remove the header below.
    26.     static final String CONFIGSET = "ConfigSet";
    27.     
    28.     // Amazon SES SMTP host name. This example uses the US West (Oregon) region.
    29.     // See https://docs.aws.amazon.com/ses/latest/DeveloperGuide/regions.html#region-endpoints
    30.     // for more information.
    31.     static final String HOST = "email-smtp.us-west-2.amazonaws.com";
    32.     
    33.     // The port you will connect to on the Amazon SES SMTP endpoint. 
    34.     static final int PORT = 587;
    35.     
    36.     static final String SUBJECT = "Amazon SES test (SMTP interface accessed using Java)";
    37.     
    38.     static final String BODY = String.join(
    39.             System.getProperty("line.separator"),
    40.             "<h1>Amazon SES SMTP Email Test</h1>",
    41.             "<p>This email was sent with Amazon SES using the ", 
    42.             "<a href='https://github.com/javaee/javamail'>Javamail Package</a>",
    43.             " for <a href='https://www.java.com'>Java</a>."
    44.         );
    45. 
    46.     public static void main(String[] args) throws Exception {
    47. 
    48.         // Create a Properties object to contain connection configuration information.
    49.         Properties props = System.getProperties();
    50.         props.put("mail.transport.protocol", "smtp");
    51.         props.put("mail.smtp.port", PORT); 
    52.         props.put("mail.smtp.starttls.enable", "true");
    53.         props.put("mail.smtp.auth", "true");
    54. 
    55.         // Create a Session object to represent a mail session with the specified properties. 
    56.         Session session = Session.getDefaultInstance(props);
    57. 
    58.         // Create a message with the specified information. 
    59.         MimeMessage msg = new MimeMessage(session);
    60.         msg.setFrom(new InternetAddress(FROM,FROMNAME));
    61.         msg.setRecipient(Message.RecipientType.TO, new InternetAddress(TO));
    62.         msg.setSubject(SUBJECT);
    63.         msg.setContent(BODY,"text/html");
    64.         
    65.         // Add a configuration set header. Comment or delete the 
    66.         // next line if you are not using a configuration set
    67.         msg.setHeader("X-SES-CONFIGURATION-SET", CONFIGSET);
    68.             
    69.         // Create a transport.
    70.         Transport transport = session.getTransport();
    71. 
    72.         // Get the password 
    73.         String SMTP_PASSWORD = fetchSMTPPasswordFromSecureStorage();
    74.                     
    75.         // Send the message.
    76.         try
    77.         {
    78.             System.out.println("Sending...");
    79.             
    80.             // Connect to Amazon SES using the SMTP username and password you specified above.
    81.             transport.connect(HOST, SMTP_USERNAME, SMTP_PASSWORD);
    82.             
    83.             // Send the email.
    84.             transport.sendMessage(msg, msg.getAllRecipients());
    85.             System.out.println("Email sent!");
    86.         }
    87.         catch (Exception ex) {
    88.             System.out.println("The email was not sent.");
    89.             System.out.println("Error message: " + ex.getMessage());
    90.         }
    91.         finally
    92.         {
    93.             // Close and terminate the connection.
    94.             transport.close();
    95.         }
    96.     }
    97. 
    98.     static String fetchSMTPPasswordFromSecureStorage() {
    99.         /* IMPLEMENT THIS METHOD */
   100.         // For example, you might fetch it from a secure location or AWS Secrets Manager: https://aws.amazon.com/secrets-manager/
   101.     }
   102. }
   ```

1. In **AmazonSESSample.java**, replace the following email addresses with your own values:
**Important**  
The email addresses are case-sensitive. Make sure that the addresses are exactly the same as the ones you verified.
   + {{sender@example.com}} – Replace with your "From" email address. You must verify this address before you run this program. For more information, see [Verified identities in Amazon SES](verify-addresses-and-domains.md).
   + {{recipient@example.com}} – Replace with your "To" email address. If your account is still in the sandbox, you must verify this address before you use it. For more information, see [Request production access (Moving out of the Amazon SES sandbox)](request-production-access.md).

1. In **AmazonSESSample.java** replace the following with your own values:
   + {{smtp\_username}} – Replace with your SMTP user name credential. Note that your SMTP user name credential is a 20-character string of letters and numbers, not an intelligible name.
   + {{smtp\_password}} – Implement ``fetchSMTPPasswordFromSecureStorage`` to fetch the password.

1. (Optional) If you want to use an Amazon SES SMTP endpoint in an AWS Region other than {{email-smtp.us-west-2.amazonaws.com}}, change the value of the variable `HOST` to the endpoint you want to use. For a list of regions where Amazon SES is available, see [Amazon Simple Email Service (Amazon SES)](https://docs.aws.amazon.com/general/latest/gr/rande.html#ses_region) in the *AWS General Reference*.

1. (Optional) If you want to use a configuration set when sending this email, change the value of the variable {{ConfigSet}} to the name of the configuration set. For more information about configuration sets, see [Using configuration sets in Amazon SES](using-configuration-sets.md).

1. Save **AmazonSESSample.java**.

1. To build the project, choose **Project** and then choose **Build Project**. (If this option is disabled, then you may have automatic building enabled.)

1. To start the program and send the email, choose **Run** and then choose **Run** again.

1. Review the output. If the email was successfully sent, the console displays *"Email sent\!"* Otherwise, it displays an error message.

1. Sign into the email client of the recipient address. You will see the message that you sent.

------
#### [ PHP  ]

This example uses the PHPMailer class to send email through Amazon SES using the SMTP interface. 

Before you perform the following procedure you must complete the tasks in [Setting up Amazon Simple Email Service](setting-up.md). In addition to setting up Amazon SES you must complete the following prerequisites to sending email with PHP:

**Prerequisites:**
+ **Install PHP** – PHP is available at [http://php.net/downloads.php](https://php.net/downloads.php). After you install PHP, add the path to PHP in your environment variables so that you can run PHP from any command prompt.
+ **Install the Composer dependency manager** – After you install the Composer dependency manager, you can download and install the PHPMailer class and its dependencies. To install Composer, follow the installation instructions at [https://getcomposer.org/download](https://getcomposer.org/download).
+ **Install the PHPMailer class** – After you install Composer, run the following command to install PHPMailer: 

  ```
  {{path/to/}}composer require phpmailer/phpmailer
  ```

  In the preceding command, replace {{path/to/}} with the path where you installed Composer.

**To send an email using the Amazon SES SMTP interface with PHP**

1. Create a file named **amazon-ses-smtp-sample.php**. Open the file with a text editor and paste in the following code:

   ```
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
   21. // Replace smtp_username with your Amazon SES SMTP user name.
   22. $usernameSmtp = 'smtp_username';
   23. 
   24. // Specify a configuration set. If you do not want to use a configuration
   25. // set, comment or remove the next line.
   26. $configurationSet = 'ConfigSet';
   27. 
   28. // If you're using Amazon SES in a region other than US West (Oregon),
   29. // replace email-smtp.us-west-2.amazonaws.com with the Amazon SES SMTP
   30. // endpoint in the appropriate region.
   31. $host = 'email-smtp.us-west-2.amazonaws.com';
   32. $port = 587;
   33. 
   34. // The subject line of the email
   35. $subject = 'Amazon SES test (SMTP interface accessed using PHP)';
   36. 
   37. // The plain-text body of the email
   38. $bodyText =  "Email Test\r\nThis email was sent through the
   39.     Amazon SES SMTP interface using the PHPMailer class.";
   40. 
   41. // The HTML-formatted body of the email
   42. $bodyHtml = '<h1>Email Test</h1>
   43.     <p>This email was sent through the
   44.     <a href="https://aws.amazon.com/ses">Amazon SES</a> SMTP
   45.     interface using the <a href="https://github.com/PHPMailer/PHPMailer">
   46.     PHPMailer</a> class.</p>';
   47. 
   48. $mail = new PHPMailer(true);
   49. 
   50. try {
   51.     // Specify the SMTP settings.
   52.     $mail->isSMTP();
   53.     $mail->setFrom($sender, $senderName);
   54.     $mail->Username   = $usernameSmtp;
   55.     $mail->Password   = fetchSMTPPasswordFromSecureStorage();
   56.     $mail->Host       = $host;
   57.     $mail->Port       = $port;
   58.     $mail->SMTPAuth   = true;
   59.     $mail->SMTPSecure = 'tls';
   60.     $mail->addCustomHeader('X-SES-CONFIGURATION-SET', $configurationSet);
   61. 
   62.     // Specify the message recipients.
   63.     $mail->addAddress($recipient);
   64.     // You can also add CC, BCC, and additional To recipients here.
   65. 
   66.     // Specify the content of the message.
   67.     $mail->isHTML(true);
   68.     $mail->Subject    = $subject;
   69.     $mail->Body       = $bodyHtml;
   70.     $mail->AltBody    = $bodyText;
   71.     $mail->Send();
   72.     echo "Email sent!" , PHP_EOL;
   73. } catch (phpmailerException $e) {
   74.     echo "An error occurred. {$e->errorMessage()}", PHP_EOL; //Catch errors from PHPMailer.
   75. } catch (Exception $e) {
   76.     echo "Email not sent. {$mail->ErrorInfo}", PHP_EOL; //Catch errors from Amazon SES.
   77. }
   78. function fetchSMTPPasswordFromSecureStorage() {
   79. /* IMPLEMENT THIS METHOD */
   80. // For example, you might fetch it from a secure location or AWS Secrets Manager: https://aws.amazon.com/secrets-manager/
   81. }
   82. 
   83. ?>
   ```

1. In **amazon-ses-smtp-sample.php**, replace the following with your own values:
   + {{sender@example.com}} – Replace with an email address that you have verified with Amazon SES. For more information, see [Verified identities](verify-addresses-and-domains.md). Email addresses in Amazon SES are case-sensitive. Make sure that the address you enter is exactly the same as the one you verified.
   + {{recipient@example.com}} – Replace with the address of the recipient. If your account is still in the sandbox, you must verify this address before you use it. For more information, see [Request production access (Moving out of the Amazon SES sandbox)](request-production-access.md). Make sure that the address you enter is exactly the same as the one you verified.
   + {{smtp\_username}} – Replace with your SMTP user name credential, which you obtained from the [SMTP Settings](https://console.aws.amazon.com/ses/home?#smtp-settings:) page of the Amazon SES console. This is **not** the same as your AWS access key ID. Note that your SMTP user name credential is a 20-character string of letters and numbers, not an intelligible name.
   + {{smtp\_password}} – Implement ``fetchSMTPPasswordFromSecureStorage`` to fetch the password.
   + (Optional) {{ConfigSet}} – If you want to use a configuration set when sending this email, replace this value with the name of the configuration set. For more information about configuration sets, see [Using configuration sets in Amazon SES](using-configuration-sets.md).
   + (Optional) {{email-smtp.us-west-2.amazonaws.com}} – If you want to use an Amazon SES SMTP endpoint in a Region other than US West (Oregon), replace this with the Amazon SES SMTP endpoint in the Region you want to use. For a list of SMTP endpoint URLs for the AWS Regions where Amazon SES is available, see [Amazon Simple Email Service (Amazon SES)](https://docs.aws.amazon.com/general/latest/gr/rande.html#ses_region) in the *AWS General Reference*.

1. Save **amazon-ses-smtp-sample.php**.

1. To run the program, open a command prompt in the same directory as **amazon-ses-smtp-sample.php**, and then type **php amazon-ses-smtp-sample.php**.

1. Review the output. If the email was successfully sent, the console displays *"Email sent\!"* Otherwise, it displays an error message.

1. Sign in to the email client of the recipient address. You will see the message that you sent.

------