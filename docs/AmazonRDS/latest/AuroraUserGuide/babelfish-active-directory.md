# Kerberos authentication with Babelfish

Babelfish for Aurora PostgreSQL 15.2 version supports authentication to your DB cluster using Kerberos. This
method allows you to use Microsoft Windows Authentication to authenticate users when they
connect to your Babelfish database. To do so, you must first configure your DB
cluster to use AWS Directory Service for Microsoft Active Directory for Kerberos authentication. For more information, see
[What
is Directory Service?](../../../directoryservice/latest/admin-guide/what_is.md "../../../directoryservice/latest/admin-guide/what_is.md") in the _AWS Directory Service Administration Guide_.

## Setting up Kerberos Authentication

Babelfish for Aurora PostgreSQL DB cluster can connect using two different ports, but Kerberos
authentication setup is a one-time process. Therefore, you must first set up Kerberos
authentication for your DB cluster. For more information, see [Setting
up Kerberos authentication](postgresql-kerberos-setting-up.md "postgresql-kerberos-setting-up.md"). After completing the setup, ensure that you can
connect with a PostgreSQL client using Kerberos. For more information, see [Connecting with Kerberos Authentication](postgresql-kerberos-connecting.md "postgresql-kerberos-connecting.md").

## Login and user provisioning in

Babelfish

Windows logins created from the Tabular Data Stream (TDS) port can be used either
with the TDS port or the PostgreSQL port. First, the login that can use Kerberos for
authentication must be provisioned from the TDS port before it is used by the T-SQL
users and applications to connect to a Babelfish database. When creating Windows
logins, administrators can provide the login using either the DNS domain name or the
NetBIOS domain name. Typically, NetBIOS domain is the subdomain of the DNS domain name.
For example, if the DNS domain name is `CORP.EXAMPLE.COM`, then the NetBIOS domain can
be `CORP`. If the NetBIOS domain name format is provided for a login, a
mapping must exist to the DNS domain name.

### Managing NetBIOS domain name to DNS domain name mapping

To manage mappings between the NetBIOS domain name and DNS domain name, Babelfish
provides system stored procedures to add, remove, and truncate mappings. Only a user
with a `sysadmin` role can run these procedures.

To create mapping between NetBIOS and DNS domain name, use the Babelfish provided
system stored procedure `babelfish_add_domain_mapping_entry`. Both
arguments must have a valid value and are not NULL.

```
EXEC babelfish_add_domain_mapping_entry 'netbios_domain_name', 'fully_qualified_domain_name'
```

The following example shows how to create the mapping between the NetBIOS name
CORP and DNS domain name CORP.EXAMPLE.COM.

```
EXEC babelfish_add_domain_mapping_entry 'corp', 'corp.example.com'
```

To delete an existing mapping entry, use the system stored procedure
babelfish_remove_domain_mapping_entry.

```
EXEC babelfish_remove_domain_mapping_entry 'netbios_domain_name'
```

The following example shows how to remove the mapping for the NetBIOS name
CORP.

```
EXEC babelfish_remove_domain_mapping_entry 'corp'
```

To remove all existing mapping entries, use the system stored procedure
babelfish_truncate_domain_mapping_table:

```
EXEC babelfish_truncate_domain_mapping_table
```

To view all mappings between NetBIOS and DNS domain name, use the following query.

```
SELECT netbios_domain_name, fq_domain_name FROM babelfish_domain_mapping;
```

### Managing Logins

######

Create logins

Connect to the DB through the TDS endpoint using a login that has the correct
permissions. If there is no database user created for the login, then the login
is mapped to guest user. If the guest user is not enabled, then the login
attempt fails.

Create a Windows login using the following query. The `FROM WINDOWS`
option allows authentication using Active Directory.

```
CREATE LOGIN login_name FROM WINDOWS [WITH DEFAULT_DATABASE=database]
```

The following example shows creating a login for the Active Directory user [corp\test1] with a
default database of db1.

```
CREATE LOGIN [corp\test1] FROM WINDOWS WITH DEFAULT_DATABASE=db1
```

This example assumes that there is a mapping between the NetBIOS domain CORP and
the DNS domain name CORP.EXAMPLE.COM. If there is no mapping, then you must provide the DNS domain name
[CORP.EXAMPLE.COM\test1].

###### Note

Logins based on Active Directory users, are limited to names of fewer than 21 characters.

######

Drop login

To drop a login, use the same syntax as for any login, as shown in the
following example:

```
DROP LOGIN [DNS domain name\login]
```

######

Alter login

To alter a login, use the same syntax as for any login, as in the following
example:

```
ALTER LOGIN [DNS domain name\login] { ENABLE|DISABLE|WITH DEFAULT_DATABASE=[master] }
```

The ALTER LOGIN command supports limited options for Windows logins, including the
following:

- DISABLE – To disable a login. You can't use a disabled login for
  authentication.
- ENABLE – To enable a disabled login.
- DEFAULT_DATABASE – To change the default database of a
  login.

###### Note

All password management is performed through Directory Service, so the ALTER LOGIN command doesn't allow
database administrators to change or set passwords for Windows logins.

### Connecting to Babelfish

for Aurora PostgreSQL with Kerberos authentication

Typically, the database users who authenticate using Kerberos are doing so from
their client machines. These machines are members of the Active Directory domain.
They use Windows Authentication from their client applications to access the
Babelfish for Aurora PostgreSQL server on the TDS port.

### Connecting to

Babelfish for Aurora PostgreSQL on the PostgreSQL port with Kerberos
authentication

You can use logins created from the TDS port with either the TDS port or the
PostgreSQL port. However, PostgreSQL uses case-sensitive comparisons by default for
usernames. For Aurora PostgreSQL to interpret Kerberos usernames as case-insensitive,
you must set the `krb_caseins_users` parameter as `true` in
the custom Babelfish cluster parameter group. This parameter is set to
`false` by default. For more information, see [Configuring for case-insensitive user names](postgresql-kerberos-setting-up.md#postgresql-kerberos-setting-up.create-logins.set-case-insentive "postgresql-kerberos-setting-up.md#postgresql-kerberos-setting-up.create-logins.set-case-insentive"). In addition, you must
specify the login username in the format <login@DNS domain name> from the PostgreSQL
client applications. You can't use <DNS domain name\login> format.

### Frequently occurring errors

You can configure forest trust relationships between your on-premises Microsoft
Active Directory and the AWS Managed Microsoft AD. For more information, see [Create a trust relationship](postgresql-kerberos-setting-up.md#postgresql-kerberos-setting-up.create-trust "postgresql-kerberos-setting-up.md#postgresql-kerberos-setting-up.create-trust"). Then, you must connect using a specialized
domain specific endpoint instead of using the Amazon domain
`rds.amazonaws.com` in the host endpoint. If you don't use the
correct domain specific endpoint, you might encounter the following error:

```
`Error: “Authentication method "NTLMSSP" not supported (Microsoft SQL Server, Error: 514)"`
```

This error occurs when the TDS client can't cache the service ticket for the
supplied endpoint URL. For more information, see [Connecting with Kerberos](postgresql-kerberos-connecting.md "postgresql-kerberos-connecting.md").
