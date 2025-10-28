# Use Active Directory or LDAP servers for authentication with

Amazon EMR

With Amazon EMR releases 6.12.0 and higher, you can use the LDAP over SSL (LDAPS) protocol to
launch a cluster that natively integrates with your corporate identity server. LDAP
(Lightweight Directory Access Protocol) is an open, vendor-neutral application protocol that
accesses and maintains data. LDAP is commonly used for user authentication against corporate
identity servers that are hosted on applications such as Active Directory (AD) and OpenLDAP.
With this native integration, you can use your LDAP server to authenticate users on
Amazon EMR.

Highlights of the Amazon EMR LDAP integration include:

- Amazon EMR configures the supported applications to authenticate with LDAP
  authentication on your behalf.
- Amazon EMR configures and maintains security for the supported applications with the
  Kerberos protocol. You don't need to input any commands or scripts.
- You get fine-grained access control (FGAC) through Apache Ranger authorization for
  Hive Metastore database and tables. See [Integrate Amazon EMR with Apache Ranger](emr-ranger.md "emr-ranger.md") for more information.
- When you require LDAP credentials to access a cluster, you get fine-grained access
  control (FGAC) over who can access your EMR clusters through SSH.
  The following pages provide a conceptual overview, prerequisites, and steps to launch an
  EMR cluster with the Amazon EMR LDAP integration.

###### Topics

- [Overview of LDAP with Amazon EMR](ldap-overview.md "ldap-overview.md")
- [LDAP components for Amazon EMR](ldap-components.md "ldap-components.md")
- [Application support and considerations with LDAP
  for Amazon EMR](ldap-considerations.md "ldap-considerations.md")
- [Configure and launch an EMR cluster with LDAP](ldap-setup.md "ldap-setup.md")
- [Examples using LDAP with Amazon EMR](ldap-examples.md "ldap-examples.md")
