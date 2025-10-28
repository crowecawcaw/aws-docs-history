# Authenticate to Amazon EMR cluster

nodes

SSH clients can use an Amazon EC2 key pair to authenticate to cluster instances. Alternatively,
with Amazon EMR releases 5.10.0 and higher, you can configure Kerberos to authenticate users and
SSH connections to the primary node. And with Amazon EMR releases 5.12.0 and higher, you can
authenticate with LDAP.

###### Topics

- [Use an EC2 key pair for SSH credentials for Amazon EMR](emr-plan-access-ssh.md "emr-plan-access-ssh.md")
- [Use Kerberos for
  authentication with Amazon EMR](emr-kerberos.md "emr-kerberos.md")
- [Use Active Directory or LDAP servers for authentication with
  Amazon EMR](ldap.md "ldap.md")
