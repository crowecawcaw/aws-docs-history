

# Configure sendmail relay server
<a name="notification-email-sendmail"></a>

Use this procedure to set up a Sendmail relay server if your network doesn't accept open relay messages.

## Step A: Gather the mail server information
<a name="notification-email-sendmail-ready"></a>

To configure Conductor Live to relay the notification emails through a mail server, you need the following information:
+ The hostname of the mail server
+ If your network doesn't have DNS configured, the IP address of the mail server

## Step B: Install the sendmail configuration tool
<a name="notification-email-sendmail-tool"></a>

**To install the configuration tool**

1. Install the `sendmail.cf` configuration tool by typing the following at the command line.

   ```
   sudo yum install sendmail-cf
   ```

1. When you receive a caution message asking you to confirm that you want to run the command, enter **yes**.

1. When you receive the following prompt, enter **y**.

   ```
   Is this ok [y/N]:
   ```

1. When you receive the following message, move on to the next step.

   ```
   Complete!
   ```

## Step C: Edit the license file
<a name="notification-email-sendmail-edit"></a>

**To edit the file**

1. With a text editor, open the `sendmail.mc` file. If you use Nano, which comes installed on all AWS Elemental systems, type the following at the command line to open the file in Nano.

   ```
   sudo nano /etc/mail/sendmail.mc
   ```

1. Find the line that defines `SMART_HOST`. It's generally just past halfway down the page and should look like this.

   ```
   dnl define(`SMART_HOST', `smtp.your.provider')dnl
   ```

1. Uncomment this line by deleting the `dnl` at the beginning and end of the line.

1. Change the following text to the hostname of the mail server that is performing the relay.

   ```
   smtp.your.provider
   ```

1. Save and exit the file. For Nano, press Ctrl\+O to save and Ctrl\+X to exit.

## Step D: Check the `hosts` file
<a name="notification-email-sendmail-hosts"></a>

If your network isn't configured with DNS, add a static entry to the `hosts` file on Conductor Live.

**To add an entry to the `hosts` file**

1. With a text editor, open the `/etc/hosts` file. If you use nano, type the following at the command line.

   ```
   sudo nano /etc/mail/hosts
   ```

1. Add a line to the end of the file that has the IP address of the relay server, a space, and the hostname of the relay server. The following shows an example.

   ```
    10.24.34.2 ExampleMailHostname
   ```

1. Save and exit the file. For nano, press Ctrl\+O to save and Ctrl\+X to exit.

## Step E: Apply the changes
<a name="notification-email-sendmail-apply"></a>

1. To apply changes, enter the following command.

   ```
   sudo make -C /etc/mail
   ```

   The system responds as follows.

   ```
   make: Entering directory `/etc/mail'
   make: Leaving directory `/etc/mail'
   ```

1. Restart Sendmail by typing the following.

   ```
   sudo service sendmail restart
   ```

## Step F: Test the new configuration
<a name="notification-email-sendmail-test"></a>

Test the relay by having the system email you an alert notification.

**To test the configuration**

1. If you haven't already, subscribe to global alert notifications as described in [Email notification](notification-email.md). Provide an email address that you have easy access to.

1. Generate a fake alert. A simple way to do so is to create and start a channel with a simple UDP input and output with a fake input address, such as **udp://1.1.1.1:1111**.

1. Check your email for the notifications message.

1. If necessary, return the global alert notifications to your desired settings.