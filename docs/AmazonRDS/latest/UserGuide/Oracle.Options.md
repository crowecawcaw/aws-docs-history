# Oracle Label Security

Amazon RDS supports Oracle Label Security for the Enterprise Edition of Oracle Database through the use of the OLS
option.

Most database security controls access at the object level. Oracle Label Security provides fine-grained control of
access to individual table rows. For example, you can use Label Security to enforce regulatory compliance with a
policy-based administration model. You can use Label Security policies to control access to sensitive data, and
restrict access to only users with the appropriate clearance level. For more information, see [Introduction to Oracle Label Security](https://docs.oracle.com/database/121/OLSAG/intro.htm#OLSAG001 "https://docs.oracle.com/database/121/OLSAG/intro.htm#OLSAG001")
in the Oracle documentation.

###### Topics

- [Requirements for Oracle Label
  Security](#Oracle.Options.OLS.PreReqs "#Oracle.Options.OLS.PreReqs")
- [Considerations when using Oracle Label
  Security](#Oracle.Options.OLS.Using "#Oracle.Options.OLS.Using")
- [Adding the Oracle Label Security option](#Oracle.Options.OLS.Add "#Oracle.Options.OLS.Add")
- [Troubleshooting](#Oracle.Options.OLS.Troubleshooting "#Oracle.Options.OLS.Troubleshooting")

## Requirements for Oracle Label

Security

Familiarize yourself with the following requirements for Oracle Label Security:

- Your DB instance must use the Bring Your Own License model.
  For more information, see
  [RDS for Oracle licensing options](Oracle.Concepts.md "Oracle.Concepts.md").
- You must have a valid license for Oracle Enterprise Edition
  with Software Update License and Support.
- Your Oracle license must include the Label Security option.

## Considerations when using Oracle Label

Security

To use Oracle Label Security, you create policies that control access to specific rows
in your tables. For more information, see [Creating an
Oracle Label Security policy](https://docs.oracle.com/database/121/OLSAG/getstrtd.htm#OLSAG3096 "https://docs.oracle.com/database/121/OLSAG/getstrtd.htm#OLSAG3096") in the Oracle documentation.

Consider the following:

- Oracle Label Security is a permanent and persistent option. Because the option
  is permanent, you can't remove it from an option group. If you add Oracle Label
  Security to an option group and associate it with your DB instance, you can later
  associate a different option group with your DB instance, but this group must also
  contain the Oracle Label Security option.
- When you work with Label Security, you perform all actions as the
  `LBAC_DBA` role. The master user for your DB instance is granted the
  `LBAC_DBA` role. You can grant the `LBAC_DBA` role to
  other users so that they can administer Label Security policies.
- Make sure to grant access to the `OLS_ENFORCEMENT` package to any
  new users who require access to Oracle Label Security. To grant access to the
  `OLS_ENFORCEMENT` package, connect to the DB instance as the master
  user and run the following SQL statement:

```
GRANT ALL ON LBACSYS.OLS_ENFORCEMENT TO `username`;
```

- You can configure Label Security through Oracle Enterprise Manager (OEM) Cloud
  Control. Amazon RDS supports OEM Cloud Control through the Management Agent option.
  For more information, see [Oracle Management Agent for Enterprise Manager
  Cloud Control](Oracle.Options.md "Oracle.Options.md").

## Adding the Oracle Label Security option

The general process for adding the Oracle Label Security option to a DB instance is the following:

1. Create a new option group, or copy or modify an existing option group.
2. Add the option to the option group.

###### Important

Oracle Label Security is a permanent and persistent option. 3. Associate the option group with the DB instance.

After you add the Label Security option,
as soon as the option group is active, Label Security is active.

###### To add the label security option to a DB instance

1. Determine the option group you want to use.
   You can create a new option group or use an existing option group.
   If you want to use an existing option group, skip to the next step.
   Otherwise, create a custom DB option group with the following settings:
   1. For **Engine**,
      choose **oracle-ee**.
   2. For **Major engine version**,
      choose the version of your DB instance.For more information,
      see [Creating an option group](USER_WorkingWithOptionGroups.md#USER_WorkingWithOptionGroups.Create "USER_WorkingWithOptionGroups.md#USER_WorkingWithOptionGroups.Create").

2. Add the **OLS** option to the option group.
   For more information about adding options,
   see [Adding an option to an option group](USER_WorkingWithOptionGroups.md#USER_WorkingWithOptionGroups.AddOption "USER_WorkingWithOptionGroups.md#USER_WorkingWithOptionGroups.AddOption").

###### Important

If you add Label Security to an existing option group
that is already attached to one or more DB instances,
all the DB instances are restarted. 3. Apply the option group to a new or existing DB instance:

    * For a new DB instance, you apply the option group when you launch the instance.
     For more information, see [Creating an Amazon RDS DB instance](USER_CreateDBInstance.md "USER_CreateDBInstance.md").
    * For an existing DB instance, you apply the option group by modifying the instance and attaching
     the new option group. When you add the Label Security option to an existing DB instance, a brief
     outage occurs while your DB instance is automatically restarted. For more information, see [Modifying an Amazon RDS DB instance](Overview.DBInstance.md "Overview.DBInstance.md").

## Troubleshooting

The following are issues you might encounter when you use Oracle Label Security.

| Issue                                                                                                                                          | Troubleshooting suggestions                                                                                                                                                                                                                                                                                                                                                         |
| ---------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| When you try to create a policy, you see an error message similar<br>to the following: `insufficient authorization for the SYSDBA<br>package`. | A known issue with Oracle's Label Security feature prevents users<br>with usernames of 16 or 24 characters from running Label Security<br>commands. You can create a new user with a different number of<br>characters, grant LBAC_DBA to the new user, log in as the new user,<br>and run the OLS commands as the new user. For additional<br>information, contact Oracle Support. |
