This is version 2.18 of the AWS Elemental Server documentation.
This is the latest version. For prior versions, see
the _Previous Versions_ section of [AWS Elemental Conductor File and AWS Elemental Server Documentation](../../../elemental-server.md "../../../elemental-server.md").

# Supported Types of User Authentication

AWS Elemental Server supports the following types of user authentication:

**Local authentication**
An administrator creates and manages user credentials from the AWS Elemental Server node.

Users logging in to nodes with local authentication enabled must enter valid credentials
for access. They must also supply credentials when using the REST API.

The credentials that users enter are validated against credentials that are housed locally
on the node that they're accessing.

**Privileged Access Management (PAM) authentication**
An administrator creates and manages user credentials from a Lightweight Directory Access Protocol (LDAP)
server
that's external from the AWS Elemental systems.

Users logging in to nodes with PAM authentication enabled must enter valid credentials
for access. They must also supply credentials when using the REST API.

The credentials that users enter are validated against credentials that are housed on an
external LDAP server.
