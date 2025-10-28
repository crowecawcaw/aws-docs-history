# Sending email through Amazon SES using

an AWS SDK

You can use an AWS SDK to send email through Amazon SES. AWS SDKs are available for several
programming languages. For more information, see [Tools for Amazon Web Services](https://aws.amazon.com/tools/#sdk "https://aws.amazon.com/tools/#sdk").

## Prerequisites

The following prerequisites must be completed in order to complete any of the code
samples in the next section:

- If you haven't already done so, complete the tasks in [Setting up Amazon Simple Email Service](setting-up.md "setting-up.md").
- Verify your email address with
  Amazon SES—Before you can send an email with Amazon SES, you must verify
  that you own the sender's email address. If your account is still in the Amazon SES
  sandbox, you must also verify the recipient email address. We recommend you use
  the Amazon SES console to verify email addresses. For more information, see [Creating an email address
  identity](creating-identities.md#verify-email-addresses-procedure "creating-identities.md#verify-email-addresses-procedure").
- Get your AWS credentials—You need an
  AWS access key ID and AWS secret access key to access Amazon SES using an SDK.
  You can find your credentials by using the [Security
  Credentials](https://console.aws.amazon.com/iam/home?#security_credential "https://console.aws.amazon.com/iam/home?#security_credential") page in the AWS Management Console. For more information about
  credentials, see [Types of Amazon SES credentials](send-email-concepts-credentials.md "send-email-concepts-credentials.md").
- Create a shared credentials file—For the
  sample code in this section to function properly, you must create a shared
  credentials file. For more information, see [Creating a shared credentials file to use when sending email through Amazon SES using an AWS SDK](create-shared-credentials-file.md "create-shared-credentials-file.md").

## Code

examples

###### Important

In the following tutorials, you send an email to yourself so that you can check to
see if you received it. For further experimentation or load testing, use the Amazon SES
mailbox simulator. Emails that you send to the mailbox simulator do not count toward
your sending quota or your bounce and complaint rates. For more information, see
[Using the mailbox simulator manually](send-an-email-from-console.md#send-email-simulator "send-an-email-from-console.md#send-email-simulator").

###### Select a programing language to view the example for that

language:

.NET
The following procedure shows you how to send an email through Amazon SES using
[Visual Studio](https://www.visualstudio.com/ "https://www.visualstudio.com/") and the
AWS SDK for .NET.

This solution was tested using the following components:

- Microsoft Visual Studio Community 2017, version 15.4.0.
- Microsoft .NET Framework version 4.6.1.
- The AWSSDK.Core package (version 3.3.19), installed using
  NuGet.
- The AWSSDK.SimpleEmail package (version 3.3.6.1), installed using
  NuGet.

###### Before you begin, perform the following tasks:

- Install Visual Studio—Visual Studio is
  available at [https://www.visualstudio.com/](https://www.visualstudio.com/ "https://www.visualstudio.com/").

###### To send an email using the AWS SDK for .NET

1. Create a new project by performing the following steps:
   1. Start Visual Studio.
   2. On the **File** menu, choose
      **New**, **Project**.
   3. On the **New Project**
      window, in the panel on the left, expand **Installed**, and then expand
      **Visual C#**.
   4. In the panel on the right, choose **Console App (.NET Framework)**.
   5. For **Name**, type
      `AmazonSESSample`, and then choose
      **OK**.

2. Use NuGet to include the Amazon SES packages in your solution by
   completing the following steps:
   1. In the **Solution Explorer** pane,
      right-click your project, and then choose **Manage
      NuGet Packages**.
   2. On the **NuGet: AmazonSESSample** tab,
      choose **Browse**.
   3. In the search box, type
      `AWSSDK.SimpleEmail`.
   4. Choose the **AWSSDK.SimpleEmail**
      package, and then choose
      **Install**.
   5. On the **Preview Changes** window, choose
      **OK**.

3. On the **Program.cs** tab, paste the following
   code:

```
using Amazon;
using System;
using System.Collections.Generic;
using Amazon.SimpleEmail;
using Amazon.SimpleEmail.Model;

namespace AmazonSESSample
{
    class Program
    {
        // Replace sender@example.com with your "From" address.
        // This address must be verified with Amazon SES.
        static readonly string senderAddress = "`sender@example.com`";

        // Replace recipient@example.com with a "To" address. If your account
        // is still in the sandbox, this address must be verified.
        static readonly string receiverAddress = "`recipient@example.com`";

        // The configuration set to use for this email. If you do not want to use a
        // configuration set, comment out the following property and the
        // ConfigurationSetName = configSet argument below.
        static readonly string configSet = "`ConfigSet`";

        // The subject line for the email.
        static readonly string subject = "Amazon SES test (AWS SDK for .NET)";

        // The email body for recipients with non-HTML email clients.
        static readonly string textBody = "Amazon SES Test (.NET)\r\n"
                                        + "This email was sent through Amazon SES "
                                        + "using the AWS SDK for .NET.";

        // The HTML body of the email.
        static readonly string htmlBody = @"<html>
<head></head>
<body>
  <h1>Amazon SES Test (SDK for .NET)</h1>
  <p>This email was sent with
    <a href='https://aws.amazon.com/ses/'>Amazon SES</a> using the
    <a href='https://aws.amazon.com/sdk-for-net/'>
      AWS SDK for .NET</a>.</p>
</body>
</html>";

        static void Main(string[] args)
        {
            // Replace USWest2 with the AWS Region you're using for Amazon SES.
            // Acceptable values are EUWest1, USEast1, and USWest2.
            using (var client = new AmazonSimpleEmailServiceClient(RegionEndpoint.`USWest2`))
            {
                var sendRequest = new SendEmailRequest
                {
                    Source = senderAddress,
                    Destination = new Destination
                    {
                        ToAddresses =
                        new List<string> { receiverAddress }
                    },
                    Message = new Message
                    {
                        Subject = new Content(subject),
                        Body = new Body
                        {
                            Html = new Content
                            {
                                Charset = "UTF-8",
                                Data = htmlBody
                            },
                            Text = new Content
                            {
                                Charset = "UTF-8",
                                Data = textBody
                            }
                        }
                    },
                    // If you are not using a configuration set, comment
                    // or remove the following line
                    ConfigurationSetName = configSet
                };
                try
                {
                    Console.WriteLine("Sending email using Amazon SES...");
                    var response = client.SendEmail(sendRequest);
                    Console.WriteLine("The email was sent successfully.");
                }
                catch (Exception ex)
                {
                    Console.WriteLine("The email was not sent.");
                    Console.WriteLine("Error message: " + ex.Message);

                }
            }

            Console.Write("Press any key to continue...");
            Console.ReadKey();
        }
    }
}
```

4.  In the code editor, do the following:

        * Replace `sender@example.com` with
         the "From:" email address. This address must be verified.
         For more information, see [Verified identities in Amazon SES](verify-addresses-and-domains.md "verify-addresses-and-domains.md").
        * Replace `recipient@example.com`
         with the "To:" address. If your account is still in the
         sandbox, this address must also be verified.
        * Replace `ConfigSet` with the name
         of the configuration set to use when sending this
         email.
        * Replace `USWest2` with the name
         of the AWS Region endpoint you use to send email using
         Amazon SES. For a list of regions where Amazon SES is available, see
         [Amazon Simple Email Service
         (Amazon SES)](../../../general/latest/gr/rande.md#ses_region "../../../general/latest/gr/rande.md#ses_region") in the
         *AWS General Reference*.

    When you finish, save `Program.cs`.

5.  Build and run the application by completing the following
    steps:
    1. On the **Build** menu, choose
       **Build Solution**.
    2. On the **Debug** menu, choose
       **Start Debugging**. A
       console window appears.

6.  Review the output of the console. If the email was successfully
    sent, the console displays "`The email was sent
successfully.`"
7.  If the email was successfully sent, sign in to the email client of
    the recipient address. You will see the message that you
    sent.

Java
The following procedure shows you how to use [Eclipse IDE for Java EE Developers](http://www.eclipse.org/ "http://www.eclipse.org/")
and [AWS Toolkit for Eclipse](../../../toolkit-for-jetbrains/latest/userguide/welcome.md "../../../toolkit-for-jetbrains/latest/userguide/welcome.md") to create an AWS SDK project and modify the Java
code to send an email through Amazon SES.

###### Before you begin, perform the following tasks:

- Install Eclipse—Eclipse is
  available at [https://www.eclipse.org/downloads](https://www.eclipse.org/downloads "https://www.eclipse.org/downloads"). The code in this
  tutorial was tested using Eclipse Neon.3 (version 4.6.3), running
  version 1.8 of the Java Runtime Environment.
- Install the
  AWS Toolkit for Eclipse—Instructions for adding the AWS Toolkit for Eclipse to your
  Eclipse installation are available at [https://aws.amazon.com/eclipse](https://aws.amazon.com/eclipse "https://aws.amazon.com/eclipse"). The code in this
  tutorial was tested using version 2.3.1 of the AWS Toolkit for Eclipse.

###### To send an email using the AWS SDK for Java

1. Create an AWS Java Project in Eclipse by performing the
   following steps:
   1. Start Eclipse.
   2. On the **File** menu, choose
      **New**, and then choose
      **Other**. On the **New** window, expand the **AWS** folder, and then choose
      **AWS Java
      Project**.
   3. In the **New AWS Java
      Project** dialog box, do the following:
      1. For **Project name**,
         type a project name.
      2. Under **AWS SDK for Java
         Samples**, select **Amazon Simple Email Service JavaMail Sample**.
      3. Choose **Finish**.

2. In Eclipse, in the **Package
   Explorer** pane, expand your project.
3. Under your project, expand the `src/main/java`
   folder, expand the `com.amazon.aws.samples`
   folder, and then double-click
   `AmazonSESSample.java`.
4. Replace the entire contents of
   `AmazonSESSample.java` with the following
   code:

```
package com.amazonaws.samples;

import java.io.IOException;

import com.amazonaws.regions.Regions;
import com.amazonaws.services.simpleemail.AmazonSimpleEmailService;
import com.amazonaws.services.simpleemail.AmazonSimpleEmailServiceClientBuilder;
import com.amazonaws.services.simpleemail.model.Body;
import com.amazonaws.services.simpleemail.model.Content;
import com.amazonaws.services.simpleemail.model.Destination;
import com.amazonaws.services.simpleemail.model.Message;
import com.amazonaws.services.simpleemail.model.SendEmailRequest;

public class AmazonSESSample {

  // Replace sender@example.com with your "From" address.
  // This address must be verified with Amazon SES.
  static final String FROM = "`sender@example.com`";

  // Replace recipient@example.com with a "To" address. If your account
  // is still in the sandbox, this address must be verified.
  static final String TO = "`recipient@example.com`";

  // The configuration set to use for this email. If you do not want to use a
  // configuration set, comment the following variable and the
  // .withConfigurationSetName(CONFIGSET); argument below.
  static final String CONFIGSET = "`ConfigSet`";

  // The subject line for the email.
  static final String SUBJECT = "Amazon SES test (AWS SDK for Java)";

  // The HTML body for the email.
  static final String HTMLBODY = "<h1>Amazon SES test (AWS SDK for Java)</h1>"
      + "<p>This email was sent with <a href='https://aws.amazon.com/ses/'>"
      + "Amazon SES</a> using the <a href='https://aws.amazon.com/sdk-for-java/'>"
      + "AWS SDK for Java</a>";

  // The email body for recipients with non-HTML email clients.
  static final String TEXTBODY = "This email was sent through Amazon SES "
      + "using the AWS SDK for Java.";

  public static void main(String[] args) throws IOException {

    try {
      AmazonSimpleEmailService client =
          AmazonSimpleEmailServiceClientBuilder.standard()
          // Replace US_WEST_2 with the AWS Region you're using for
          // Amazon SES.
            .withRegion(Regions.`US_WEST_2`).build();
      SendEmailRequest request = new SendEmailRequest()
          .withDestination(
              new Destination().withToAddresses(TO))
          .withMessage(new Message()
              .withBody(new Body()
                  .withHtml(new Content()
                      .withCharset("UTF-8").withData(HTMLBODY))
                  .withText(new Content()
                      .withCharset("UTF-8").withData(TEXTBODY)))
              .withSubject(new Content()
                  .withCharset("UTF-8").withData(SUBJECT)))
          .withSource(FROM)
          // Comment or remove the next line if you are not using a
          // configuration set
          .withConfigurationSetName(CONFIGSET);
      client.sendEmail(request);
      System.out.println("Email sent!");
    } catch (Exception ex) {
      System.out.println("The email was not sent. Error message: "
          + ex.getMessage());
    }
  }
}
```

5. In `AmazonSESSample.java`, replace the
   following with your own values:

###### Important

The email addresses are case-sensitive. Make sure that the
addresses are exactly the same as the ones you verified.

    * `SENDER@EXAMPLE.COM`—Replace with your
     "From" email address. You must verify this address before
     you run this program. For more information, see [Verified identities in Amazon SES](verify-addresses-and-domains.md "verify-addresses-and-domains.md").
    * `RECIPIENT@EXAMPLE.COM`—Replace with your
     "To" email address. If your account is still in the sandbox,
     you must verify this address before you use it. For more
     information, see [Request production access (Moving out of the
     Amazon SES sandbox)](request-production-access.md "request-production-access.md").
    * (Optional)
     `us-west-2`—If you want to use
     Amazon SES in a Region other than US West (Oregon), replace
     this with the Region you want to use. For a list of Regions
     where Amazon SES is available, see [Amazon Simple Email Service
     (Amazon SES)](../../../general/latest/gr/rande.md#ses_region "../../../general/latest/gr/rande.md#ses_region") in the
     *AWS General Reference*.

6. Save `AmazonSESSample.java`.
7. To build the project, choose **Project** and then choose **Build
   Project**.

###### Note

If this option is disabled, automatic building may be enabled;
if so, skip this step. 8. To start the program and send the email, choose **Run** and then choose **Run** again. 9. Review the output of the console pane in Eclipse. If the email was
successfully sent, the console displays "`Email
 sent!`" Otherwise, it displays an error
message. 10. If the email was successfully sent, sign in to the email client of
the recipient address. You will see the message that you
sent.

PHP
This topic shows how to use the [AWS SDK for PHP](https://aws.amazon.com/sdk-for-php/ "https://aws.amazon.com/sdk-for-php/") to send an email through Amazon SES.

###### Before you begin, perform the following tasks:

- Install PHP—PHP is available
  at [http://php.net/downloads.php](http://php.net/downloads.php "http://php.net/downloads.php"). This tutorial requires
  PHP version 5.5 or higher. After you install PHP, add the path to
  PHP in your environment variables so that you can run PHP from any
  command prompt. The code in this tutorial was tested using PHP
  7.2.7.
- Install the AWS SDK for PHP version
  3—For download and installation instructions, see the
  [AWS SDK for PHP documentation](../../../aws-sdk-php/v3/guide/getting-started/installation.md "../../../aws-sdk-php/v3/guide/getting-started/installation.md"). The code in this tutorial was
  tested using version 3.64.13 of the SDK.

###### To send an email through Amazon SES using the AWS SDK for PHP

1. In a text editor, create a file named
   `amazon-ses-sample.php`. Paste the following
   code:

```
<?php

// If necessary, modify the path in the require statement below to refer to the
// location of your Composer autoload.php file.
require 'vendor/autoload.php';

use Aws\Ses\SesClient;
use Aws\Exception\AwsException;

// Create an SesClient. Change the value of the region parameter if you're
// using an AWS Region other than US West (Oregon). Change the value of the
// profile parameter if you want to use a profile in your credentials file
// other than the default.
$SesClient = new SesClient([
    'profile' => 'default',
    'version' => '2010-12-01',
    'region'  => '`us-west-2`'
]);

// Replace sender@example.com with your "From" address.
// This address must be verified with Amazon SES.
$sender_email = '`sender@example.com`';

// Replace these sample addresses with the addresses of your recipients. If
// your account is still in the sandbox, these addresses must be verified.
$recipient_emails = ['`recipient1@example.com`','`recipient2@example.com`'];

// Specify a configuration set. If you do not want to use a configuration
// set, comment the following variable, and the
// 'ConfigurationSetName' => $configuration_set argument below.
$configuration_set = '`ConfigSet`';

$subject = 'Amazon SES test (AWS SDK for PHP)';
$plaintext_body = 'This email was sent with Amazon SES using the AWS SDK for PHP.' ;
$html_body =  '<h1>AWS Amazon Simple Email Service Test Email</h1>'.
              '<p>This email was sent with <a href="https://aws.amazon.com/ses/">'.
              'Amazon SES</a> using the <a href="https://aws.amazon.com/sdk-for-php/">'.
              'AWS SDK for PHP</a>.</p>';
$char_set = 'UTF-8';

try {
    $result = $SesClient->sendEmail([
        'Destination' => [
            'ToAddresses' => $recipient_emails,
        ],
        'ReplyToAddresses' => [$sender_email],
        'Source' => $sender_email,
        'Message' => [
          'Body' => [
              'Html' => [
                  'Charset' => $char_set,
                  'Data' => $html_body,
              ],
              'Text' => [
                  'Charset' => $char_set,
                  'Data' => $plaintext_body,
              ],
          ],
          'Subject' => [
              'Charset' => $char_set,
              'Data' => $subject,
          ],
        ],
        // If you aren't using a configuration set, comment or delete the
        // following line
        'ConfigurationSetName' => $configuration_set,
    ]);
    $messageId = $result['MessageId'];
    echo("Email sent! Message ID: $messageId"."\n");
} catch (AwsException $e) {
    // output error message if fails
    echo $e->getMessage();
    echo("The email was not sent. Error message: ".$e->getAwsErrorMessage()."\n");
    echo "\n";
}

```

2. In `amazon-ses-sample.php`, replace the
   following with your own values:
   - `path_to_sdk_inclusion`—Replace
     with the path required to include the AWS SDK for PHP in the
     program. For more information, see the [AWS SDK for PHP documentation](../../../aws-sdk-php/v3/guide/getting-started/basic-usage.md "../../../aws-sdk-php/v3/guide/getting-started/basic-usage.md").
   - `sender@example.com`—Replace
     with an email address that you have verified with Amazon SES. For
     more information, see [Verified identities](verify-addresses-and-domains.md "verify-addresses-and-domains.md").
     Email addresses in Amazon SES are case-sensitive. Make sure that
     the address you enter is exactly the same as the one you
     verified.
   - `recipient1@example.com`,
     `recipient2@example.com`—Replace
     with the addresses of your recipients. If your account is
     still in the sandbox, your recipients' addresses must also
     be verified. For more information, see [Request production access (Moving out of the
     Amazon SES sandbox)](request-production-access.md "request-production-access.md"). Make sure
     that the address you enter is exactly the same as the one
     you verified.
   - (Optional)
     `ConfigSet`—If you want to use
     a configuration set when sending this email, replace this
     value with the name of the configuration set. For more
     information about configuration sets, see [Using configuration sets in Amazon SES](using-configuration-sets.md "using-configuration-sets.md").
   - (Optional)
     `us-west-2`—If you want to use
     Amazon SES in a Region other than US West (Oregon), replace
     this with the Region you want to use. For a list of Regions
     where Amazon SES is available, see [Amazon Simple Email Service
     (Amazon SES)](../../../general/latest/gr/rande.md#ses_region "../../../general/latest/gr/rande.md#ses_region") in the
     _AWS General Reference_.

3. Save `amazon-ses-sample.php`.
4. To run the program, open a command prompt in the same directory as
   `amazon-ses-sample.php`, and then type the
   following command:

```
`$` `php amazon-ses-sample.php`
```

5. Review the output. If the email was successfully sent, the console
   displays "`Email sent!`" Otherwise,
   it displays an error message.

###### Note

If you encounter a "cURL error 60: SSL certificate problem"
error when you run the program, download the latest CA bundle as
described in the [AWS SDK for PHP documentation](../../../aws-sdk-php/v3/guide/faq.md#what-do-i-do-about-a-curl-ssl-certificate-error "../../../aws-sdk-php/v3/guide/faq.md#what-do-i-do-about-a-curl-ssl-certificate-error"). Then, in
`amazon-ses-sample.php`, add the
following lines to the `SesClient::factory` array,
replace `path_of_certs` with the path to the CA
bundle you downloaded, and re-run the program.

```
'http' => [
   'verify' => 'path_of_certs\ca-bundle.crt'
]
```

6. Sign in to the email client of the recipient address. You will see
   the message that you sent.

Ruby
This topic shows how to use the [AWS SDK for Ruby](https://aws.amazon.com/sdk-for-ruby/ "https://aws.amazon.com/sdk-for-ruby/") to send an email through Amazon SES.

###### Before you begin, perform the following tasks:

- Install Ruby—Ruby is
  available at [https://www.ruby-lang.org/en/downloads/](https://www.ruby-lang.org/en/downloads/ "https://www.ruby-lang.org/en/downloads/"). The code in
  this tutorial was tested using Ruby 1.9.3. After you install Ruby,
  add the path to Ruby in your environment variables so that you can
  run Ruby from any command prompt.
- Install the AWS SDK for Ruby—For
  download and installation instructions, see [Installing the
  AWS SDK for Ruby](../../../sdk-for-ruby/latest/developer-guide/setup-install.md "../../../sdk-for-ruby/latest/developer-guide/setup-install.md") in the _AWS SDK for Ruby Developer Guide_.
  The sample code in this tutorial was tested using version 2.9.36 of
  the AWS SDK for Ruby.
- Create a shared credentials
  file—For the sample code in this section to function
  properly, you must create a shared credentials file. For more
  information, see [Creating a shared credentials file to use when sending email through Amazon SES using an AWS SDK](create-shared-credentials-file.md "create-shared-credentials-file.md").

###### To send an email through Amazon SES using the AWS SDK for Ruby

1. In a text editor, create a file named
   `amazon-ses-sample.rb`. Paste the following
   code into the file:

```
require 'aws-sdk'

# Replace sender@example.com with your "From" address.
# This address must be verified with Amazon SES.
sender = "`sender@example.com`"

# Replace recipient@example.com with a "To" address. If your account
# is still in the sandbox, this address must be verified.
recipient = "`recipient@example.com`"

# Specify a configuration set. If you do not want to use a configuration
# set, comment the following variable and the
# configuration_set_name: configsetname argument below.
configsetname = "`ConfigSet`"

# Replace us-west-2 with the AWS Region you're using for Amazon SES.
awsregion = "`us-west-2`"

# The subject line for the email.
subject = "Amazon SES test (AWS SDK for Ruby)"

# The HTML body of the email.
htmlbody =
  '<h1>Amazon SES test (AWS SDK for Ruby)</h1>'\
  '<p>This email was sent with <a href="https://aws.amazon.com/ses/">'\
  'Amazon SES</a> using the <a href="https://aws.amazon.com/sdk-for-ruby/">'\
  'AWS SDK for Ruby</a>.'

# The email body for recipients with non-HTML email clients.
textbody = "This email was sent with Amazon SES using the AWS SDK for Ruby."

# Specify the text encoding scheme.
encoding = "UTF-8"

# Create a new SES resource and specify a region
ses = Aws::SES::Client.new(region: awsregion)

# Try to send the email.
begin

  # Provide the contents of the email.
  resp = ses.send_email({
    destination: {
      to_addresses: [
        recipient,
      ],
    },
    message: {
      body: {
        html: {
          charset: encoding,
          data: htmlbody,
        },
        text: {
          charset: encoding,
          data: textbody,
        },
      },
      subject: {
        charset: encoding,
        data: subject,
      },
    },
  source: sender,
  # Comment or remove the following line if you are not using
  # a configuration set
  configuration_set_name: configsetname,
  })
  puts "Email sent!"

# If something goes wrong, display an error message.
rescue Aws::SES::Errors::ServiceError => error
  puts "Email not sent. Error message: #{error}"

end
```

2. In `amazon-ses-sample.rb`, replace the
   following with your own values:
   - `sender@example.com`—Replace
     with an email address that you have verified with Amazon SES. For
     more information, see [Verified identities](verify-addresses-and-domains.md "verify-addresses-and-domains.md").
     Email addresses in Amazon SES are case-sensitive. Make sure that
     the address you enter is exactly the same as the one you
     verified.
   - `recipient@example.com`—Replace
     with the address of the recipient. If your account is still
     in the sandbox, you must verify this address before you use
     it. For more information, see [Request production access (Moving out of the
     Amazon SES sandbox)](request-production-access.md "request-production-access.md"). Make sure
     that the address you enter is exactly the same as the one
     you verified.
   - (Optional)
     `us-west-2`—If you want to use
     Amazon SES in a Region other than US West (Oregon), replace
     this with the Region you want to use. For a list of Regions
     where Amazon SES is available, see [Amazon Simple Email Service
     (Amazon SES)](../../../general/latest/gr/rande.md#ses_region "../../../general/latest/gr/rande.md#ses_region") in the
     _AWS General Reference_.

3. Save `amazon-ses-sample.rb`.
4. To run the program, open a command prompt in the same directory as
   `amazon-ses-sample.rb`, and type
   **ruby amazon-ses-sample.rb**
5. Review the output. If the email was successfully sent, the console
   displays "`Email sent!`" Otherwise,
   it displays an error message.
6. Sign in to the email client of the recipient address. You will
   find the message that you sent.

Python
This topic shows how to use the [AWS SDK for Python (Boto)](https://aws.amazon.com/sdk-for-python/ "https://aws.amazon.com/sdk-for-python/") to send an
email through Amazon SES.

###### Before you begin, perform the following tasks:

- Verify your email address with
  Amazon SES—Before you can send an email with Amazon SES,
  you must verify that you own the sender's email address. If your
  account is still in the Amazon SES sandbox, you must also verify the
  recipient email address. We recommend you use the Amazon SES console to
  verify email addresses. For more information, see [Creating an email address
  identity](creating-identities.md#verify-email-addresses-procedure "creating-identities.md#verify-email-addresses-procedure").
- Get your AWS
  credentials—You need an AWS access key ID and AWS
  secret access key to access Amazon SES using an SDK. You can find your
  credentials by using the [Security
  Credentials](https://console.aws.amazon.com/iam/home?#security_credential "https://console.aws.amazon.com/iam/home?#security_credential") page of the AWS Management Console. For more information
  about credentials, see [Types of Amazon SES credentials](send-email-concepts-credentials.md "send-email-concepts-credentials.md").
- Install Python—Python is
  available at [https://www.python.org/downloads/](https://www.python.org/downloads/ "https://www.python.org/downloads/"). The code in this
  tutorial was tested using Python 2.7.6 and Python 3.6.1. After you
  install Python, add the path to Python in your environment variables
  so that you can run Python from any command prompt.
- Install the AWS SDK for Python (Boto)—For
  download and installation instructions, see the [AWS SDK for Python (Boto) documentation](https://boto3.readthedocs.io/en/latest/guide/quickstart.html#installation "https://boto3.readthedocs.io/en/latest/guide/quickstart.html#installation"). The sample code in this
  tutorial was tested using version 1.4.4 of the SDK for Python.

###### To send an email through Amazon SES using the SDK for Python

1. In a text editor, create a file named
   `amazon-ses-sample.py`. Paste the following
   code into the file:

```
import boto3
from botocore.exceptions import ClientError

# Replace sender@example.com with your "From" address.
# This address must be verified with Amazon SES.
SENDER = "`Sender Name <sender@example.com>`"

# Replace recipient@example.com with a "To" address. If your account
# is still in the sandbox, this address must be verified.
RECIPIENT = "`recipient@example.com`"

# Specify a configuration set. If you do not want to use a configuration
# set, comment the following variable, and the
# ConfigurationSetName=CONFIGURATION_SET argument below.
CONFIGURATION_SET = "`ConfigSet`"

# If necessary, replace us-west-2 with the AWS Region you're using for Amazon SES.
AWS_REGION = "`us-west-2`"

# The subject line for the email.
SUBJECT = "Amazon SES Test (SDK for Python)"

# The email body for recipients with non-HTML email clients.
BODY_TEXT = ("Amazon SES Test (Python)\r\n"
             "This email was sent with Amazon SES using the "
             "AWS SDK for Python (Boto)."
            )

# The HTML body of the email.
BODY_HTML = """<html>
<head></head>
<body>
  <h1>Amazon SES Test (SDK for Python)</h1>
  <p>This email was sent with
    <a href='https://aws.amazon.com/ses/'>Amazon SES</a> using the
    <a href='https://aws.amazon.com/sdk-for-python/'>
      AWS SDK for Python (Boto)</a>.</p>
</body>
</html>
            """

# The character encoding for the email.
CHARSET = "UTF-8"

# Create a new SES resource and specify a region.
client = boto3.client('ses',region_name=AWS_REGION)

# Try to send the email.
try:
    #Provide the contents of the email.
    response = client.send_email(
        Destination={
            'ToAddresses': [
                RECIPIENT,
            ],
        },
        Message={
            'Body': {
                'Html': {
                    'Charset': CHARSET,
                    'Data': BODY_HTML,
                },
                'Text': {
                    'Charset': CHARSET,
                    'Data': BODY_TEXT,
                },
            },
            'Subject': {
                'Charset': CHARSET,
                'Data': SUBJECT,
            },
        },
        Source=SENDER,
        # If you are not using a configuration set, comment or delete the
        # following line
        ConfigurationSetName=CONFIGURATION_SET,
    )
# Display an error if something goes wrong.
except ClientError as e:
    print(e.response['Error']['Message'])
else:
    print("Email sent! Message ID:"),
    print(response['MessageId'])
```

2. In `amazon-ses-sample.py`, replace the
   following with your own values:
   - `sender@example.com`—Replace
     with an email address that you have verified with Amazon SES. For
     more information, see [Verified identities](verify-addresses-and-domains.md "verify-addresses-and-domains.md").
     Email addresses in Amazon SES are case sensitive. Make sure that
     the address you enter is exactly the same as the one you
     verified.
   - `recipient@example.com`—Replace
     with the address of the recipient. If your account is still
     in the sandbox, you must verify this address before you use
     it. For more information, see [Request production access (Moving out of the
     Amazon SES sandbox)](request-production-access.md "request-production-access.md"). Make sure
     that the address you enter is exactly the same as the one
     you verified.
   - (Optional)
     `us-west-2`—If you want to use
     Amazon SES in a Region other than US West (Oregon), replace
     this with the Region you want to use. For a list of Regions
     where Amazon SES is available, see [Amazon Simple Email Service
     (Amazon SES)](../../../general/latest/gr/rande.md#ses_region "../../../general/latest/gr/rande.md#ses_region") in the
     _AWS General Reference_.

3. Save `amazon-ses-sample.py`.
4. To run the program, open a command prompt in the same directory as
   `amazon-ses-sample.py`, and then type
   **python amazon-ses-sample.py**.
5. Review the output. If the email was successfully sent, the console
   displays "`Email sent!`" Otherwise,
   it displays an error message.
6. Sign in to the email client of the recipient address. You will see
   the message that you sent.
