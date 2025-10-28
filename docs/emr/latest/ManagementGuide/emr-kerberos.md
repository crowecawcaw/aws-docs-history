# Use Kerberos for

authentication with Amazon EMR

Amazon EMR releases 5.10.0 and higher support Kerberos. Kerberos is a network
authentication protocol that uses secret-key cryptography to provide strong
authentication so that passwords or other credentials aren't sent over the network in an
unencrypted format.

In Kerberos, services and users that need to authenticate are known as
_principals_. Principals exist within a Kerberos
_realm_. Within the realm, a Kerberos server known as the
_key distribution center (KDC)_ provides the means for principals
to authenticate. The KDC does this by issuing _tickets_ for
authentication. The KDC maintains a database of the principals within its realm, their
passwords, and other administrative information about each principal. A KDC can also
accept authentication credentials from principals in other realms, which is known as a
_cross-realm trust_. In addition, an EMR cluster can use an
external KDC to authenticate principals.

A common scenario for establishing a cross-realm trust or using an external KDC is to
authenticate users from an Active Directory domain. This allows users to access an EMR
cluster with their domain account when they use SSH to connect to a cluster or work with
big data applications.

When you use Kerberos authentication, Amazon EMR configures Kerberos for the applications,
components, and subsystems that it installs on the cluster so that they are
authenticated with each other.

###### Important

Amazon EMR does not support AWS Directory Service for Microsoft Active Directory in a cross-realm trust or as an external
KDC.

Before you configure Kerberos using Amazon EMR, we recommend that you become familiar with
Kerberos concepts, the services that run on a KDC, and the tools for administering
Kerberos services. For more information, see [MIT Kerberos
documentation](http://web.mit.edu/kerberos/krb5-latest/doc/ "http://web.mit.edu/kerberos/krb5-latest/doc/"), which is published by the [Kerberos consortium](http://kerberos.org/ "http://kerberos.org/").

###### Topics

- [Supported applications with Amazon EMR](emr-kerberos-principals.md "emr-kerberos-principals.md")
- [Kerberos architecture options with Amazon EMR](emr-kerberos-options.md "emr-kerberos-options.md")
- [Configuring Kerberos on Amazon EMR](emr-kerberos-configure.md "emr-kerberos-configure.md")
- [Using SSH to connect to Kerberized
  clusters with Amazon EMR](emr-kerberos-connect-ssh.md "emr-kerberos-connect-ssh.md")
- [Tutorial: Configure an cluster-dedicated
  KDC with Amazon EMR](emr-kerberos-cluster-kdc.md "emr-kerberos-cluster-kdc.md")
- [Tutorial: Configure a cross-realm trust
  with an Active Directory domain](emr-kerberos-cross-realm.md "emr-kerberos-cross-realm.md")
