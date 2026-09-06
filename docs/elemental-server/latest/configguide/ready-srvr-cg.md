

This is version 2.18 of the AWS Elemental Server documentation. This is the latest version. For prior versions, see the *Previous Versions* section of [AWS Elemental Conductor File and AWS Elemental Server Documentation](https://docs.aws.amazon.com/elemental-server/).

# Getting Ready
<a name="ready-srvr-cg"></a>

Be aware of the following topics before starting phase 2 of the installation.

## Web Interface Access
<a name="ready-srvr-cg-access"></a>

Most of the steps in the configuration procedure involve working in the web interface.

**To access the web interface the first time**  
If you're accessing the web interface for the first time, or any time after if you haven't enabled user authentication, enter the IP address of the node in a browser. If you created a hostname through the install script, you can also use the hostname to access the node.

**To access the web interface with user authentication**

1. Enter the IP address or hostname of the node in a web browser.

1. At the login screen, enter your credentials for this node. If you haven't created additional users yet, use the REST API administrator credentials that you created when you enabled authentication.

**Important**  
You cannot log in using the *elemental* user credentials\!