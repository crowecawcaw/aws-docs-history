# Adding the SSL option

To use SSL, your RDS for Oracle DB instance must
be associated with an option group that includes the `SSL`
option.

###### To add the SSL option to an option group

1. Create a new option group or identify an existing option group to which
   you can add the `SSL` option.

For information about creating an option group, see
[Creating an option group](USER_WorkingWithOptionGroups.md#USER_WorkingWithOptionGroups.Create "USER_WorkingWithOptionGroups.md#USER_WorkingWithOptionGroups.Create"). 2. Add the `SSL` option to the option group.

If you want to use only FIPS-verified cipher suites for SSL
connections, set the option `FIPS.SSLFIPS_140` to
`TRUE`. For information about the FIPS standard, see
[FIPS support](Appendix.Oracle.Options.md#Appendix.Oracle.Options.SSL.FIPS "Appendix.Oracle.Options.md#Appendix.Oracle.Options.SSL.FIPS").

For information about adding an option to an option group, see
[Adding an option to an option group](USER_WorkingWithOptionGroups.md#USER_WorkingWithOptionGroups.AddOption "USER_WorkingWithOptionGroups.md#USER_WorkingWithOptionGroups.AddOption"). 3. Create a new RDS for Oracle DB instance and associate the option group with it, or
modify an RDS for Oracle DB instance to associate the option group with it.

For information about creating an DB instance, see
[Creating an Amazon RDS DB instance](USER_CreateDBInstance.md "USER_CreateDBInstance.md").

For information about modifying an DB instance, see
[Modifying an Amazon RDS DB instance](Overview.DBInstance.md "Overview.DBInstance.md").

###### To add the SSL option to an option group

1. Create a new option group or identify an existing option group to which
   you can add the `SSL` option.

For information about creating an option group, see
[Creating an option group](USER_WorkingWithOptionGroups.md#USER_WorkingWithOptionGroups.Create "USER_WorkingWithOptionGroups.md#USER_WorkingWithOptionGroups.Create"). 2. Add the `SSL` option to the option group.

Specify the following option settings:

    * `Port` – The SSL port number
    * `VpcSecurityGroupMemberships` – The VPC security group for which the option is enabled
    * `SQLNET.SSL_VERSION` – The TLS version that client can use to connect to the DB instance

For example, the following AWS CLI command adds the
`SSL` option to an option group named
`ora-option-group`.

###### Example

For Linux, macOS, or Unix:

```
aws rds add-option-to-option-group --option-group-name ora-option-group \
  --options 'OptionName=SSL,Port=2484,VpcSecurityGroupMemberships="sg-68184619",OptionSettings=[{Name=SQLNET.SSL_VERSION,Value=1.0}]'
```

For Windows:

```
aws rds add-option-to-option-group --option-group-name ora-option-group ^
  --options 'OptionName=SSL,Port=2484,VpcSecurityGroupMemberships="sg-68184619",OptionSettings=[{Name=SQLNET.SSL_VERSION,Value=1.0}]'
```

3. Create a new RDS for Oracle DB instance and associate the option group with it, or
   modify an RDS for Oracle DB instance to associate the option group with it.

For information about creating an DB instance, see
[Creating an Amazon RDS DB instance](USER_CreateDBInstance.md "USER_CreateDBInstance.md").

For information about modifying an DB instance, see
[Modifying an Amazon RDS DB instance](Overview.DBInstance.md "Overview.DBInstance.md").
