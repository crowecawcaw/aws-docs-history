# Connecting to

Babelfish via PostgreSQL endpoint on the PostgreSQL port

You can utilize group logins created from the TDS port to connect through PostgreSQL
port as well. To connect through PostgreSQL port, you need to specify the AD user's name
in the format `<ad_username@FQDN>` from the PostgreSQL client
applications. You can't use the `<DNS domain name\ad_username>`
format.

PostgreSQL uses case-sensitive comparisons by default for usernames. For Aurora
PostgreSQL to interpret Kerberos usernames as case-insensitive, you must set the
krb_caseins_users parameter as true in the custom Babelfish cluster parameter group.
This parameter is set to false by default. For more information, see [Configuring your Aurora PostgreSQL DB cluster for case-insensitive user
names](postgresql-kerberos-setting-up.md#postgresql-kerberos-setting-up.create-logins.set-case-insentive "postgresql-kerberos-setting-up.md#postgresql-kerberos-setting-up.create-logins.set-case-insentive").

## Behavior differences

between T-SQL and PostgreSQL endpoints when an AD user is part of multiple
groups

Consider that AD user user1 is part of two AD security groups
[corp\accounts-group] and [corp\sales-group] and DB admin has set the user mapping
in following way.

```

postgres=> select * from pgadmap_read_mapping();
 `ad_sid | pg_role | weight | ad_grp
-------------+---------------------------------+--------+---------------
S-1-5-67-980 | accounts-group@CORP.EXAMPLE.COM | 7 | accounts-group
S-1-2-34-560 | sales-group@CORP.EXAMPLE.COM | 10 | sales-group
(2 rows)`

```

If the user is connecting from the T-SQL endpoint then during the authorization,
it will inherit the privileges from all the associated T-SQL logins. In this example
user1 will inherit the union of privileges from both the T-SQL group login and
weights will be ignored. This is inline with the standard T-SQL behavior.

However if same user connects from the PostgreSQL endpoint then it can inherit
privileges from only one associated T-SQL login with the highest weight. If the two
T-SQL group login were assigned same weight then AD user will inherit the privileges
of the T-SQL login corresponding to the mapping that was added most recently. For
the PostgreSQL, the recommendation is to specify weights that reflect the relative
permissions/privileges of individual DB roles to avoid the ambiguity. In below
example, user1 connected through PSQL endpoint and inherited only sales-groups
privileges.

```

babelfish_db=> select session_user, current_user;
`session_user | current_user
------------------------------+---------------------------
 sales-group@CORP.EXAMPLE.COM | sales-group@CORP.EXAMPLE.COM
(1 row)`

babelfish_db=> select principal, gss_authenticated from pg_stat_gssapi where pid = pg_backend_pid();
`principal | gss_authenticated
------------------------+-------------------
 user1@CORP.EXAMPLE.COM | t
(1 row)`

```
