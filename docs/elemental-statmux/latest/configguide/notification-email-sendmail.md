This is version 2.20 of the AWS Elemental Statmux documentation.
This is the latest version. For prior versions, see the
_Previous Versions_ section of [AWS Elemental Statmux
and AWS Elemental Live Documentation](../../../elemental-live.md "../../../elemental-live.md").

# Configure Sendmail Relay Server

Use this procedure to set up a Sendmail relay server if your network doesn't accept open relay messages.

## Step A: Gather the mail server information

To configure AWS Elemental Statmux to relay
the notification emails through a mail server, you need the following information:

- The hostname of the mail server
- If your network doesn't have DNS configured, the IP address of the mail server

## Step B: Install the Sendmail configuration tool

###### To install the configuration tool

1. Install the `sendmail.cf` configuration tool by typing the following at the command line.

```
**sudo yum install sendmail-cf**
```

2. When you receive a caution message asking you to confirm that you want to run the command, enter `yes`.
3. When you receive the following prompt, enter `y`.

```
`Is this ok [y/N]:`
```

4. When you receive the following message, move on to the next step.

```
`Complete!`
```

## Step C: Edit the `sendmail.lic` file

Edit the `sendmail.lic` file to add the hostname of the mail server
that is performing the relay.

###### To edit the file

1. With a text editor, open the `sendmail.mc` file. If you use Nano, which comes
   installed on all AWS Elemental systems, type the following at the command line to open the file in Nano.

```
**sudo nano /etc/mail/sendmail.mc**
```

2. Locate the line that defines `SMART_HOST`. It's generally just past halfway
   down the page and should look like this.

```
`dnl define(`SMART_HOST', `smtp.your.provider')dnl`
```

3. Uncomment this line by deleting the `dnl`
   at the beginning and end of the line.
4. Change the following text to the hostname of the mail server that is performing the relay.

```
`smtp.your.provider`
```

5. Save and exit the file. For Nano, press **Ctrl**+**O** to save and
   **Ctrl**+**X** to exit.

## Step D: Check the `hosts` file

If your network isn't configured with DNS, add a static entry to the `hosts` file on AWS Elemental Statmux.

###### To add an entry to the `hosts` file

1. With a text editor, open the `/etc/hosts` file. If you use nano, type the following at the command line.

```
**sudo nano /etc/mail/hosts**
```

2. Add a line to the end of the file that has the IP address of the relay server, a space, and the hostname of the relay server. The following shows an example.

```
`10.24.34.2 ExampleMailHostname`
```

3. Save and exit the file. For nano, press **Ctrl**+**O** to save and
   **Ctrl**+**X** to exit.

## Step E: Apply the changes

1. To apply changes, enter the following command.

```
**sudo make -C /etc/mail**
```

The system responds as follows.

```
`make: Entering directory `/etc/mail'
make: Leaving directory `/etc/mail'`
```

2. Restart Sendmail by typing the following.

```
**sudo service sendmail restart**
```

## Step F: Test the new configuration

Test the relay by having the system email you an alert notification.

###### To test the configuration

1. If you haven't already, subscribe to global alert notifications as described in [Email Notification](notification-email.md "notification-email.md").
   Provide an email address that you have easy access to.
2. Generate a fake alert. A simple way to do so is to create and start a channel with a
   simple UDP input and output with a fake input address, such as
   `udp://1.1.1.1:1111`.
3. Check your email for the notifications message.
4. If necessary, return the global alert notifications to your desired settings.
