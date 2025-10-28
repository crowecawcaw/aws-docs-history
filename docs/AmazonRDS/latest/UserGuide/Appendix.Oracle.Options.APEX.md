# Upgrading and removing

Oracle APEX

To upgrade or remove Oracle APEX, follow the instructions in this topic:

###### Topics

- [Upgrading the Oracle APEX
  version](#Appendix.Oracle.Options.APEX.Upgrade "#Appendix.Oracle.Options.APEX.Upgrade")
- [Removing the APEX and APEX-DEV
  options](#Appendix.Oracle.Options.APEX.Remove "#Appendix.Oracle.Options.APEX.Remove")

## Upgrading the Oracle APEX

version

###### Important

Back up your DB instance before you upgrade Oracle APEX. For more information, see
[Creating a DB snapshot for a Single-AZ DB instance for Amazon RDS](USER_CreateSnapshot.md "USER_CreateSnapshot.md")
and [Testing an Oracle DB upgrade](USER_UpgradeDBInstance.Oracle.md "USER_UpgradeDBInstance.Oracle.md").

To upgrade Oracle APEX with your DB instance, do the following:

- Create a new option group for the upgraded version of your DB instance.
- Add the upgraded versions of the `APEX` and
  `APEX-DEV` options to the new option group. Be sure to
  include any other options that your DB instance uses. For more information, see
  [Option group considerations](USER_UpgradeDBInstance.Oracle.md#USER_UpgradeDBInstance.Oracle.OGPG.OG "USER_UpgradeDBInstance.Oracle.md#USER_UpgradeDBInstance.Oracle.OGPG.OG").
- When you upgrade your DB instance, specify the new option group for your
  upgraded DB instance.

After you upgrade your version of Oracle APEX, the Oracle APEX schema for the
previous version might still exist in your database. If you don't need it anymore,
you can drop the old Oracle APEX schema from your database after you upgrade.

If you upgrade the Oracle APEX version and RESTful services were not configured in
the previous Oracle APEX version, we recommend that you configure RESTful services.
For more information, see [Configuring RESTful services for Oracle APEX](Appendix.Oracle.Options.APEX.md#Appendix.Oracle.Options.APEX.ConfigureRESTful "Appendix.Oracle.Options.APEX.md#Appendix.Oracle.Options.APEX.ConfigureRESTful").

In some cases when you plan to do a major version upgrade of your DB instance, you might
find that you're using an Oracle APEX version that isn't compatible with
your target database version. In these cases, you can upgrade your version of Oracle
APEX before you upgrade your DB instance. Upgrading Oracle APEX first can reduce the
amount of time that it takes to upgrade your DB instance.

###### Note

After upgrading Oracle APEX, install and configure a listener for use with the
upgraded version. For instructions, see [Setting up Oracle APEX listener](Appendix.Oracle.Options.APEX.md#Appendix.Oracle.Options.APEX.Listener "Appendix.Oracle.Options.APEX.md#Appendix.Oracle.Options.APEX.Listener").

## Removing the APEX and APEX-DEV

options

You can remove the `APEX` and `APEX-DEV` options from a
DB instance. To remove these options from your DB instance, do one of the following:

- To remove the `APEX` and `APEX-DEV` options from
  multiple DB instances, remove the options from the option group they belong to.
  This change affects all DB instances that use the option group. When you remove
  the options from an option group that is attached to multiple DB instances, a
  brief outage occurs while the DB instances are restarted.

For more information, see [Removing an option from an option group](USER_WorkingWithOptionGroups.md#USER_WorkingWithOptionGroups.RemoveOption "USER_WorkingWithOptionGroups.md#USER_WorkingWithOptionGroups.RemoveOption").

- To remove the `APEX` and `APEX-DEV` options from a
  single DB instance, modify the DB instance and specify a different option group that
  doesn't include these options. You can specify the default (empty) option
  group, or a different custom option group. When you remove the options, a
  brief outage occurs while your DB instance is automatically restarted.

For more information, see [Modifying an Amazon RDS DB instance](Overview.DBInstance.md "Overview.DBInstance.md").

When you remove the `APEX` and `APEX-DEV` options from a
DB instance, the APEX schema is removed from your database.
