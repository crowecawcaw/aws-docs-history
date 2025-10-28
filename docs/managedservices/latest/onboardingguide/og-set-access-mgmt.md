# SALZ: Set up access management

Using a network managed by AWS Managed Services (AMS) means giving AMS access to manage your cloud infrastructure. You’ll need to
configure a means of securely connecting between your private network and AMS. This starts with some decisions about the kinds of access you want to provide:

- _For AMS API/CLI and Console access_: You will want to install the AMS CLI (instructions are
  provided in [this document](../userguide/install-cli.md "../userguide/install-cli.md")).
  You use the AMS change management API to make change requests to AMS and the AMS SKMS API to learn about your AMS-managed resources.
  Using Active Directory Federation Services (AD FS), you can access the AMS Console.

###### Note

If you are setting up your own ITSM, you will need to use the AWS Support API (SAPI) for service requests and incident reports. SAPI is documented
in the [AWS Support API Reference](../../../awssupport/latest/APIReference/Welcome.md "../../../awssupport/latest/APIReference/Welcome.md").

- _For user access_: Whether you manage users with Windows Active Directory (AD), or a Linux/LDAP solution,
  connectivity needs to be established between AD on the AMS side (via Directory Services) and your directory.
- _For instance access_: Instance-level access is accomplished via a one-way Forest trust configuration.
  Directory Services trusts credentials in their CORP AD, allowing stacks within the AMS side to allow login with CORP credentials.

Note that your Active Directory (AD) that AMS sets up the trust to must be the directory that has the
accounts of users authorized by you to gain access to your AWS resources.

###### Important

To set up a Forest trust, AMS requires your domain controller **Local Policies ->
Security Options -> Network Access: Named Pipes that can be accessed anonymously**, have the **Netlogon**
and **lsarpc** pipes listed.
These pipes are listed by default, but are sometimes removed for security concerns. Once the trust is established, they
can be removed from the list again.
