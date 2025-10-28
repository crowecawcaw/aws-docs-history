# Mapping T-SQL group logins with

AD security group

You need to explicitly provision T-SQL Windows Group Login for each AD security group
that requires access to the database server. An AD user, who is part of at least one
provisioned AD security group, will get access to the database server.

###### Note

This T-SQL login can no longer authenticate using a password based
authentication.

For example, accounts-group is a security group in AD and if you would like to
provision this security group in Babelfish, you must use the format
[corp\accounts-group].

- AD Security Group : accounts-group
- TSQL Login : [corp\accounts-group]
- Equivalent PG role for given TSQL Login :
  accounts-group@CORP.EXAMPLE.COM
  Admin can now proceed to create the mapping between AD security group and T-SQL login
  from PostgreSQL endpoint via following psql command. For more information on the
  function usage, see [Using functions from the
  pg_ad_mapping extension](AD.Security.md#AD.Security.Groups.functions "AD.Security.md#AD.Security.Groups.functions").

###### Note

T-SQL login should be specified in login_name@FQDN format while adding the
mapping. Weights are ignored when connecting through TDS endpoint. For more
information about usage of weights, see [Connecting to
Babelfish via PostgreSQL endpoint on the PostgreSQL port](babelfish-kerberos-securityad-connect-pgendpoint.md "babelfish-kerberos-securityad-connect-pgendpoint.md").

```
postgres=>select pgadmap_set_mapping('accounts-group', 'accounts-group@CORP.EXAMPLE.COM', <SID>, <Weight>);
```

For information on retrieving SID of AD security group, see [Retrieving Active Directory Group SID in
PowerShell](AD.Security.md#AD.Security.Groups.retrieving "AD.Security.md#AD.Security.Groups.retrieving").

The following table shows a sample mapping from AD security groups to T-SQL
logins:

| AD Security Groups | TSQL Logins           | Equivalent PG role for given TSQL Login | Weight |
| ------------------ | --------------------- | --------------------------------------- | ------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------ | -------------- | ------- | -------------------------------------------------------------------------------------------------------------------- | -------------- | ------------------- | ------------------------------- | -------------- | ----------- | ---------------- | ---------------------------- | --------------- | --------- | -------------- | -------------------------- | -------------- |
| accounts-group     | [corp\accounts-group] | accounts-group@CORP.EXAMPLE.COM         | 7      |
| sales-group        | [corp\sales-group]    | sales-group@CORP.EXAMPLE.COM            | 10     |
| dev-group          | [corp\dev-group]      | dev-group@CORP.EXAMPLE.COM              | 7      | ``` postgres=> select admap.ad_sid, admap.ad_grp, lgn.orig_loginname, lgn.rolname, admap.weight from pgadmap_read_mapping() as admap, sys.babelfish_authid_login_ext as lgn where admap.pg_role = lgn.rolname; ad_sid | ad_grp | orig_loginname | rolname | weight --------------+----------------+---------------------+---------------------------------+-------- S-1-5-67-890 | accounts-group | corp\accounts-group | accounts-group@CORP.EXAMPLE.COM | 7 S-1-2-34-560 | sales-group | corp\sales-group | sales-group@CORP.EXAMPLE.COM | 10 S-1-8-43-612 | dev-group | corp\dev-group | dev-group@CORP.EXAMPLE.COM | 7 (7 rows) ``` |
