# Requiring SSL/TLS for all

connections to a MariaDB DB instance on Amazon RDS

Use the `require_secure_transport` parameter to require that all user
connections to your MariaDB DB instance use SSL/TLS. For versions 11.4 and earlier, the
`require_secure_transport` parameter is set to `OFF` by default. For 11.8 and later versions,
the default value is set to `ON`, enforcing SSL/TLS for connections to your DB instance. You can
change the `require_secure_transport` parameter to `OFF` if non-secure connections are needed.

###### Note

The `require_secure_transport` parameter is only supported for MariaDB
version 10.5 and higher.

You can set the `require_secure_transport` parameter value by updating the
DB parameter group for your DB instance. You don't need to reboot your DB instance for
the change to take effect.

When the `require_secure_transport` parameter is set to `ON` for
a DB instance, a database client can connect to it if it can establish an encrypted
connection. Otherwise, an error message similar to the following is returned to the
client:

```
ERROR 1045 (28000): Access denied for user '`USER`'@'localhost' (using password: `YES | NO`)
```

For information about setting parameters, see [Modifying parameters in a DB parameter group
in Amazon RDS](USER_WorkingWithParamGroups.md "USER_WorkingWithParamGroups.md").

For more information about the `require_secure_transport` parameter, see
the [MariaDB documentation](https://mariadb.com/docs/ent/ref/mdb/system-variables/require_secure_transport/ "https://mariadb.com/docs/ent/ref/mdb/system-variables/require_secure_transport/").
