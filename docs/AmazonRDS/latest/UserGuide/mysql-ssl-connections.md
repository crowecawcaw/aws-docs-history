# Requiring SSL/TLS for

specific user accounts to a MySQL DB instance on Amazon RDS

You can require SSL/TLS encryption for specified user account connections to your
MySQL DB instances on Amazon RDS. Protecting sensitive information from unauthorized access
or interception is crucial to enforce security policies where data confidentiality is a
concern.

To require SSL/TLS connections for specific users' accounts, use one of the following
statements, depending on your MySQL version, to require SSL/TLS connections on the user
account `encrypted_user`.

To do so, use the following statement.

```
ALTER USER 'encrypted_user'@'%' REQUIRE SSL;
```

For more information on SSL/TLS connections with MySQL, see the [Using
encrypted connections](https://dev.mysql.com/doc/refman/8.0/en/encrypted-connections.html "https://dev.mysql.com/doc/refman/8.0/en/encrypted-connections.html") in the MySQL documentation.
