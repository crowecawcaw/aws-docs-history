# Step 6: Configure connection and authorize your

Outposts server

To authorize the server, you must connect your laptop to the server with a USB cable, then
use a command-based serial protocol to test the connection and authorize the server. In addition
to IAM credentials, you need a USB cable, a laptop, and serial terminal software, such as
PuTTY or **screen**, to complete these steps.

Consider the following information about authorizing the server:

- To authorize the server, you or the party installing the server needs IAM credentials
  in the AWS account that contains the Outpost. For more information, see [Step 1: Grant permissions to install the Outposts server](install-grant.md "install-grant.md").
- You do not need to authenticate with the IAM credentials to test your connection.
- Consider testing the connection before you use the export command to set IAM
  credentials as environment variables.
- To protect your account, Outpost Configuration Tool never saves your IAM credentials.
- To connect your laptop to the server, always plug the USB cable into your laptop first
  and then into the server.

###### Tasks

- [Connect your laptop](authorize-1.md "authorize-1.md")
- [Create a serial connection](authorize-2.md "authorize-2.md")
- [Configure and test the connection](authorize-3.md "authorize-3.md")
- [Authorize the server](authorize-4.md "authorize-4.md")
- [Verify the NSK LEDs](authorize-5.md "authorize-5.md")
