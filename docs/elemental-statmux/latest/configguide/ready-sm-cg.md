This is version 2.20 of the AWS Elemental Statmux documentation.
This is the latest version. For prior versions, see the
_Previous Versions_ section of [AWS Elemental Statmux
and AWS Elemental Live Documentation](../../../elemental-live.md "../../../elemental-live.md").

# Getting Ready

Be aware of the following topics before starting phase 2 of installation.

## Web Interface Access

Most of the steps in the configuration procedure involve working in the web interface.

###### To access the web interface the first time

If you're accessing the web interface for the first time, or any time after if
you haven't enabled user authentication, enter the IP address of the node in a browser.
If you created a hostname through the install script, you can also use the hostname to access the node.

###### To access the web interface with user authentication

1. Enter the IP address or hostname of the node in a web browser.
2. At the login screen, enter your credentials for this node. If you haven't created additional
   users yet, use the REST API administrator credentials that you created when you enabled
   authentication.

###### Important

You cannot log in using the _elemental_ user credentials!
