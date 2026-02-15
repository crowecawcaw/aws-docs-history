# Strategies for updating your

time zone file

Upgrading your DB engine and adding the `TIMEZONE_FILE_AUTOUPGRADE` option
to an option group are separate operations. Adding the
`TIMEZONE_FILE_AUTOUPGRADE` option initiates the update of your time zone
file if a more current one is available. You run the following commands (only relevant
options are shown) either immediately or at the next maintenance window:

- Upgrade your DB engine only using the following RDS CLI command:

```
modify-db-instance --engine-version `name` ...
```

- Add the `TIMEZONE_FILE_AUTOUPGRADE` option only using the following
  CLI command:

```
add-option-to-option-group --option-group-name `name` --options OptionName=TIMEZONE_FILE_AUTOUPGRADE ...
```

- Upgrade your DB engine and add a new option group to your instance using the
  following CLI command:

```
modify-db-instance --engine-version `name` --option-group-name `name` ...
```

Your update strategy depends on whether you want to upgrade your database and time
zone file together or perform just one of these operations. Keep in mind that if you
update your option group and then upgrade your DB engine in separate API operations, it's
possible for a time zone file update to be currently in progress when you upgrade your
DB engine.

The examples in this section assume the following:

- You have not yet added `TIMEZONE_FILE_AUTOUPGRADE` to the option
  group currently associated with your DB instance.
- Your DB instance uses database version 19.0.0.0.ru-2019-07.rur-2019-07.r1 and time
  zone file DSTv33.
- Your DB instance file system includes file DSTv34.
- Release update 19.0.0.0.ru-2022-10.rur-2022-10.r1 includes DSTv35.
  To update your time zone file, you can use the following strategies.

###### Topics

- [Update the time zone file without upgrading the engine](#Appendix.Oracle.Options.Timezone-file-autoupgrade.strategies.no-upgrade "#Appendix.Oracle.Options.Timezone-file-autoupgrade.strategies.no-upgrade")
- [Upgrade the time zone file and DB engine version](#Appendix.Oracle.Options.Timezone-file-autoupgrade.strategies.upgrade "#Appendix.Oracle.Options.Timezone-file-autoupgrade.strategies.upgrade")
- [Upgrade your DB engine version without updating the time zone file](#Appendix.Oracle.Options.Timezone-file-autoupgrade.strategies.upgrade-only "#Appendix.Oracle.Options.Timezone-file-autoupgrade.strategies.upgrade-only")

## Update the time zone file without upgrading the engine

In this scenario, your database is using DSTv33, but DSTv34 is available on your
DB instance file system. You want to update the time zone file used by your DB instance from
DSTv33 to DSTv34, but you don't want to upgrade your engine to a new minor version,
which includes DSTv35.

In an `add-option-to-option-group` command, add
`TIMEZONE_FILE_AUTOUPGRADE` to the option group used by your DB instance.
Specify whether to add the option immediately or defer it to the maintenance window.
After applying the `TIMEZONE_FILE_AUTOUPGRADE` option, RDS does the
following:

1. Checks for a new DST version.
2. Determines that DSTv34 is available on the file system.
3. Updates the time zone file immediately.

## Upgrade the time zone file and DB engine version

In this scenario, your database is using DSTv33, but DSTv34 is available on your
DB instance file system. You want to upgrade your DB engine to minor version
19.0.0.0.ru-2022-10.rur-2022-10.r1, which includes DSTv35, and update your time zone
file to DSTv35 during the engine upgrade. Thus, your goal is to skip DSTv34 and
update your time zone files directly to DSTv35.

To upgrade the engine and time zone file together, run
`modify-db-instance` with the `--option-group-name` and
`--engine-version` options. You can run the command immediately or
defer it to maintenance window. `In --option-group-name`, specify an
option group that includes the `TIMEZONE_FILE_AUTOUPGRADE` option. For
example:

```
aws rds modify-db-instance
    --db-instance-identifier `my-instance` \
    --engine-version `new-version` \
    ----option-group-name `og-with-timezone-file-autoupgrade` \
    --apply-immediately
```

RDS begins upgrading your engine to 19.0.0.0.ru-2022-10.rur-2022-10.r1. After
applying the `TIMEZONE_FILE_AUTOUPGRADE` option, RDS checks for a new DST
version, sees that DSTv35 is available in 19.0.0.0.ru-2022-10.rur-2022-10.r1, and
immediately starts the update to DSTv35.

To upgrade your engine immediately and then upgrade your a timezone file, perform
the operations in sequence:

1. Upgrade your DB engine only using the following CLI command:

```
aws rds modify-db-instance \
    --db-instance-identifier `my-instance` \
    --engine-version `new-version` \
    --apply-immediately
```

2. Add the `TIMEZONE_FILE_AUTOUPGRADE` option to the option group
   attached to your instance using the following CLI command:

```
aws rds add-option-to-option-group \
    --option-group-name `og-in-use-by-your-instance` \
    --options OptionName=TIMEZONE_FILE_AUTOUPGRADE \
    --apply-immediately
```

## Upgrade your DB engine version without updating the time zone file

In this scenario, your database is using DSTv33, but DSTv34 is available on your
DB instance file system. You want to upgrade your DB engine to version
19.0.0.0.ru-2022-10.rur-2022-10.r1, which includes DSTv35, but retain time zone file
DSTv33. You might choose this strategy for the following reasons:

- Your data doesn't use the `TIMESTAMP WITH TIME ZONE` data
  type.
- Your data uses the `TIMESTAMP WITH TIME ZONE` data type, but
  your data is not affected by the time zone changes.
- You want to postpone updating the time zone file because you can't
  tolerate the extra downtime.

Your strategy depends on which of the following possibilities are true:

- Your DB instance isn't associated with an option group that includes
  `TIMEZONE_FILE_AUTOUPGRADE`. In your
  `modify-db-instance` command, don't specify a new option
  group so that RDS doesn't update your time zone file.
- Your DB instance is currently associated with an option group that includes
  `TIMEZONE_FILE_AUTOUPGRADE`. Within a single
  `modify-db-instance` command, associate your DB instance with an
  option group that doesn't include `TIMEZONE_FILE_AUTOUPGRADE` and
  upgrade your DB engine to 19.0.0.0.ru-2022-10.rur-2022-10.r1.
