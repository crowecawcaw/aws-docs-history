This is version 2.20 of the AWS Elemental Statmux documentation.
This is the latest version. For prior versions, see the
_Previous Versions_ section of [AWS Elemental Statmux
and AWS Elemental Live Documentation](../../../elemental-live.md "../../../elemental-live.md").

# Supported Types of User Authentication

AWS Elemental Statmux supports the following types of user authentication:

**Local authentication**
An administrator creates and manages user credentials from the AWS Elemental Statmux node.

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
