# Active Directory Domain Environment

Your active directory domain environment must meet the following requirements.

- You must have a Microsoft Active Directory domain to which to join your
  streaming instances. If you don't have an Active Directory domain or you
  want to use your on-premises Active Directory environment, see [Active Directory Domain Services on AWS Partner Solution Deployment
  Guide](https://aws-solutions-library-samples.github.io/cfn-ps-microsoft-activedirectory/ "https://aws-solutions-library-samples.github.io/cfn-ps-microsoft-activedirectory/").
- You must have a domain service account with permissions to create and manage
  computer objects in the domain that you intend to use with AppStream 2.0. For
  information, see [How to
  Create a Domain Account in Active Directory](<https://msdn.microsoft.com/en-us/library/aa545262(v=cs.70).aspx> "https://msdn.microsoft.com/en-us/library/aa545262(v=cs.70).aspx") in the Microsoft
  documentation.

When you associate this Active Directory domain with AppStream 2.0, provide
the service account name and password. AppStream 2.0 uses this account to create and
manage computer objects in the directory. For more information, see [Granting Permissions to Create and Manage
Active Directory Computer Objects](active-directory-permissions.md "active-directory-permissions.md").

- When you register your Active Directory domain with AppStream 2.0, you must provide
  an organizational unit (OU) distinguished name. Create an OU for this purpose.
  The default Computers container is not an OU and cannot be used by AppStream 2.0. For
  more information, see [Finding the Organizational Unit Distinguished
  Name](active-directory-oudn.md "active-directory-oudn.md").
- The directories that you plan to use with AppStream 2.0 must be accessible through
  their fully qualified domain names (FQDNs) through the virtual private cloud
  (VPC) in which your streaming instances are launched. For more information, see
  [Active Directory and Active Directory Domain Services Port
  Requirements](https://technet.microsoft.com/en-us/library/dd772723.aspx "https://technet.microsoft.com/en-us/library/dd772723.aspx") in the Microsoft documentation.
