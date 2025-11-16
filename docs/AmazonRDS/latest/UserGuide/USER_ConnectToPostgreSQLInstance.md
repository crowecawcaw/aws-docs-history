# Troubleshooting

connections to your RDS for PostgreSQL instance

###### Topics

- [Error
  – FATAL: database name does not exist](#USER_ConnectToPostgreSQLInstance.Troubleshooting-DBname "#USER_ConnectToPostgreSQLInstance.Troubleshooting-DBname")
- [Error
  – Could not connect to server: Connection timed out](#USER_ConnectToPostgreSQLInstance.Troubleshooting-timeout "#USER_ConnectToPostgreSQLInstance.Troubleshooting-timeout")
- [Errors with security group access rules](#USER_ConnectToPostgreSQLInstance.Troubleshooting-AccessRules "#USER_ConnectToPostgreSQLInstance.Troubleshooting-AccessRules")

## Error

– FATAL: database `name` does not exist

If when trying to connect you receive an error like `FATAL: database
 `name` does not exist`, try using the default
database name **postgres** for the
`--dbname` option.

## Error

– Could not connect to server: Connection timed out

If you can't connect to the DB instance, the most common error is `Could
 not connect to server: Connection timed out.` If you receive this error,
check the following:

- Check that the host name used is the DB instance endpoint and that the
  port number used is correct.
- Make sure that the DB instance's public accessibility is set to
  **Yes** to allow external connections. To modify the
  **Public access** setting, see [Modifying an Amazon RDS DB instance](Overview.DBInstance.md "Overview.DBInstance.md").
- Make sure that the user connecting to the database has CONNECT access to
  it. You can use the following query to provide connect access to the
  database.

```
GRANT CONNECT ON DATABASE `database name` TO `username`;
```

- Check that the security group assigned to the DB instance has rules to
  allow access through any firewall your connection might go through. For
  example, if the DB instance was created using the default port of 5432, your
  company might have firewall rules blocking connections to that port from
  external company devices.

To fix this, modify the DB instance to use a different port. Also, make
sure that the security group applied to the DB instance allows connections
to the new port. To modify the **Database port** setting,
see [Modifying an Amazon RDS DB instance](Overview.DBInstance.md "Overview.DBInstance.md").

- Check whether the port you're attempting to use is already occupied by a
  local instance of PostgreSQL or another service running on your computer.
  For example, if you have a local PostgreSQL database running on the same
  port (default is 5432), it might prevent a successful connection to the
  RDS for PostgreSQL DB instance. Make sure that the port is free, or try
  connecting with a different port number if possible.
- See also [Errors with security group access rules](#USER_ConnectToPostgreSQLInstance.Troubleshooting-AccessRules "#USER_ConnectToPostgreSQLInstance.Troubleshooting-AccessRules").

##

Errors with security group access rules

By far the most common connection problem is with the security group's access
rules assigned to the DB instance. If you used the default security group when you
created the DB instance, the security group likely didn't have access rules
that allow you to access the instance.

For the connection to work, the security group you assigned to the DB instance at
its creation must allow access to the DB instance. For example, if the DB instance
was created in a VPC, it must have a VPC security group that authorizes connections.
Check if the DB instance was created using a security group that doesn't
authorize connections from the device or Amazon EC2 instance where the application is
running.

You can add or edit an inbound rule in the security group. For
**Source**, choosing **My IP** allows access
to the DB instance from the IP address detected in your browser. For more
information, see [Provide access to your DB instance in your VPC by
creating a security group](CHAP_SettingUp.md#CHAP_SettingUp.SecurityGroup "CHAP_SettingUp.md#CHAP_SettingUp.SecurityGroup").

Alternatively, if the DB instance was created outside of a VPC, it must have a
database security group that authorizes those connections.

For more information about Amazon RDS security groups, see [Controlling access with security
groups](Overview.md "Overview.md").
