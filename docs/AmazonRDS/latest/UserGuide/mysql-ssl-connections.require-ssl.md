

# Requiring SSL/TLS for all connections to a MySQL DB instance on Amazon RDS

Use the `require_secure_transport` parameter to require that all user connections to your MySQL DB instance use SSL/TLS. The default value depends on the MySQL version:
+ For MySQL 9.7, the `require_secure_transport` parameter defaults to `1` (ON). Amazon RDS rejects connections that don't use SSL/TLS. To allow connections that don't use SSL/TLS, set the `require_secure_transport` parameter to `0` (OFF) in a custom DB parameter group.
+ For MySQL 8.4 and lower, the `require_secure_transport` parameter is set to `0` (OFF) by default. You can set the `require_secure_transport` parameter to `1` (ON) to require SSL/TLS for connections to your DB instance.

You can set the `require_secure_transport` parameter value by updating the DB parameter group for your DB instance. You don't need to reboot your DB instance for the change to take effect.

When the `require_secure_transport` parameter is set to `ON` for a DB instance, a database client can connect to it if it can establish an encrypted connection. Otherwise, an error message similar to the following is returned to the client:

```bash
MySQL Error 3159 (HY000): Connections using insecure transport are prohibited while --require_secure_transport=ON.
```

For information about setting parameters, see [Modifying parameters in a DB parameter group in Amazon RDS](USER_WorkingWithParamGroups.Modifying.md).

For more information about the `require_secure_transport` parameter, see the [ MySQL documentation](https://dev.mysql.com/doc/refman/8.0/en/server-system-variables.html#sysvar_require_secure_transport).