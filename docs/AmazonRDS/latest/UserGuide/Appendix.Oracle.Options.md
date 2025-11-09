# Oracle time zone

To change the system time zone used by your Oracle DB instance, use the time zone option. For example, you might
change the time zone of a DB instance to be compatible with an on-premises environment, or a legacy application. The
time zone option changes the time zone at the host level. Changing the time zone impacts all date columns and values,
including `SYSDATE` and `SYSTIMESTAMP`.

The time zone option differs from the `rdsadmin_util.alter_db_time_zone` command. The
`alter_db_time_zone` command changes the time zone only for certain data types. The time zone option
changes the time zone for all date columns and values. For more information about `alter_db_time_zone`,
see [Setting the
database time zone](Appendix.Oracle.CommonDBATasks.md "Appendix.Oracle.CommonDBATasks.md"). For more information about upgrade
considerations, see [Time zone considerations](USER_UpgradeDBInstance.Oracle.md#USER_UpgradeDBInstance.Oracle.OGPG.DST "USER_UpgradeDBInstance.Oracle.md#USER_UpgradeDBInstance.Oracle.OGPG.DST").

## Restrictions for setting

the time zone

The time zone option is a permanent and persistent option. Therefore, you can't do the
following:

- Remove the option from an option group after you add the time zone
  option.
- Remove the option group from a DB instance after you add the group.
- Modify the time zone setting of the option to a different time zone.

## Recommendations for setting

the time zone

Before you add the time zone option to your production database, we strongly recommend
that you do the following:

- Take a snapshot of your DB instance. If you accidentally set the time zone
  incorrectly, you must recover your DB instance to its previous time zone setting. For
  more information, see [Creating a DB snapshot for a Single-AZ DB instance for Amazon RDS](USER_CreateSnapshot.md "USER_CreateSnapshot.md").
- Add the time zone option to a test DB instance. Adding the time zone option can
  cause problems with tables that use the system date to add dates or times. We
  recommend that you analyze your data and applications on the test instance. This
  way you can assess the impact of changing the time zone on your production
  instance.

If your DB instance uses the default option group, then follow these steps:

1. Take a snapshot of your DB instance.
2. Add the time zone option to your DB instance.

If your DB instance currently uses a nondefault option group, then follow these
steps:

1. Take a snapshot of your DB instance.
2. Create a new option group.
3. Add the time zone option to it, along with all other options that are
   currently associated with the existing option group.

This prevents the existing options from being uninstalled while enabling the
time zone option. 4. Add the option group to your DB instance.

## Time zone option settings

Amazon RDS supports the following settings for the time zone option.

| Option setting | Valid values                                                                                                                                                             | Description                             |
| -------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | --------------------------------------- |
| `TIME_ZONE`    | One of the available time zones.<br>For the full list, see<br>[Available time zones](#Appendix.Oracle.Options.Timezone.Zones "#Appendix.Oracle.Options.Timezone.Zones"). | The new time zone for your DB instance. |

## Adding the time zone option

Complete the following steps to add the time zone option to your DB instance:

1. (Recommended) Take a snapshot of your DB instance.
2. Do one of the following tasks:
   - Create a new option group from scratch. For more information, see [Creating an option group](USER_WorkingWithOptionGroups.md#USER_WorkingWithOptionGroups.Create "USER_WorkingWithOptionGroups.md#USER_WorkingWithOptionGroups.Create").
   - Copy an existing option group using the AWS CLI or API. For more information,
     see [Copying an option group](USER_WorkingWithOptionGroups.md#USER_WorkingWithOptionGroups.Copy "USER_WorkingWithOptionGroups.md#USER_WorkingWithOptionGroups.Copy").
   - Reuse an existing non-default option group. A best practice is to use an
     option group that isn't currently associated with any DB instances or
     snapshots.

3. Add the new option to the option group from the preceding step.
4. If the option group that is currently associated with your DB instance has options enabled,
   add these options to your new option group. This strategy prevents the existing options
   from being uninstalled while enabling the new option.
5. Add the new option group to your DB instance.

When you add the time zone option,
a brief outage occurs
while your DB instance is automatically restarted.

###### To add the time zone option to an option group and associate it with a

DB instance

1.  In the RDS console, choose **Option groups.**
2.  Choose the name of the option group to which you want to add the
    option.
3.  Choose **Add option**.
4.  For **Option name**, choose
    **Timezone**, and then configure the option
    settings.
5.  Associate the option group with a new or existing DB instance:

        * For a new DB instance, apply the option group when you launch the instance. For more
         information, see [Creating an Amazon RDS DB instance](USER_CreateDBInstance.md "USER_CreateDBInstance.md").
        * For an existing DB instance, apply the option group by modifying the instance and
         attaching the new option group. When you add the new option to an existing DB instance, a
         brief outage occurs while your DB instance is automatically restarted. For more
         information, see [Modifying an Amazon RDS DB instance](Overview.DBInstance.md "Overview.DBInstance.md").

    The following example uses the AWS CLI [add-option-to-option-group](../../../cli/latest/reference/rds/add-option-to-option-group.md "../../../cli/latest/reference/rds/add-option-to-option-group.md") command to add the `Timezone`
    option and the `TIME_ZONE` option setting to an option group called
    `myoptiongroup`. The time zone is set to
    `Africa/Cairo`.

For Linux, macOS, or Unix:

```
aws rds add-option-to-option-group \
    --option-group-name "`myoptiongroup`" \
    --options "`OptionName=Timezone,OptionSettings=[{Name=TIME_ZONE,Value=Africa/Cairo}]`" \
    --apply-immediately
```

For Windows:

```
aws rds add-option-to-option-group ^
    --option-group-name "`myoptiongroup`" ^
    --options "`OptionName=Timezone,OptionSettings=[{Name=TIME_ZONE,Value=Africa/Cairo}]`" ^
    --apply-immediately
```

## Modifying time zone settings

The time zone option is a permanent and persistent option.
You can't remove the option from an option group after you add it.
You can't remove the option group from a DB instance after you add it.
You can't modify the time zone setting of the option to a different time zone.
If you set the time zone incorrectly,
restore a snapshot of your DB instance from before you added the time zone option.

## Removing the time zone option

The time zone option is a permanent and persistent option.
You can't remove the option from an option group after you add it.
You can't remove the option group from a DB instance after you add it.
To remove the time zone option,
restore a snapshot of your DB instance from before you added the time zone option.

## Available time zones

You can use the following values for the time zone option.

| Zone      | Time zone                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Africa    | Africa/Cairo, Africa/Casablanca, Africa/Harare, Africa/Lagos,<br>Africa/Luanda, Africa/Monrovia, Africa/Nairobi, Africa/Tripoli,<br>Africa/Windhoek                                                                                                                                                                                                                                                                                                                                                                             |
| America   | America/Araguaina, America/Argentina/Buenos_Aires, America/Asuncion, America/Bogota,<br>America/Caracas, America/Chicago, America/Chihuahua, America/Cuiaba,<br>America/Denver, America/Detroit, America/Fortaleza, America/Godthab,<br>America/Guatemala, America/Halifax, America/Lima, America/Los_Angeles,<br>America/Manaus, America/Matamoros, America/Mexico_City, America/Monterrey,<br>America/Montevideo, America/New_York, America/Phoenix, America/Santiago,<br>America/Sao_Paulo, America/Tijuana, America/Toronto |
| Asia      | Asia/Amman, Asia/Ashgabat, Asia/Baghdad, Asia/Baku,<br>Asia/Bangkok, Asia/Beirut, Asia/Calcutta, Asia/Damascus,<br>Asia/Dhaka, Asia/Hong_Kong, Asia/Irkutsk, Asia/Jakarta,<br>Asia/Jerusalem, Asia/Kabul, Asia/Karachi, Asia/Kathmandu,<br>Asia/Kolkata, Asia/Krasnoyarsk, Asia/Magadan, Asia/Manila,<br>Asia/Muscat, Asia/Novosibirsk, Asia/Rangoon, Asia/Riyadh,<br>Asia/Seoul, Asia/Shanghai, Asia/Singapore, Asia/Taipei,<br>Asia/Tehran, Asia/Tokyo, Asia/Ulaanbaatar, Asia/Vladivostok,<br>Asia/Yakutsk, Asia/Yerevan     |
| Atlantic  | Atlantic/Azores, Atlantic/Cape_Verde                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Australia | Australia/Adelaide, Australia/Brisbane, Australia/Darwin, Australia/Eucla,<br>Australia/Hobart, Australia/Lord_Howe, Australia/Perth, Australia/Sydney                                                                                                                                                                                                                                                                                                                                                                          |
| Brazil    | Brazil/DeNoronha, Brazil/East                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Canada    | Canada/Newfoundland, Canada/Saskatchewan                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| Etc       | Etc/GMT-3                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Europe    | Europe/Amsterdam, Europe/Athens, Europe/Berlin, Europe/Dublin,<br>Europe/Helsinki, Europe/Kaliningrad, Europe/London, Europe/Madrid,<br>Europe/Moscow, Europe/Paris, Europe/Prague, Europe/Rome,<br>Europe/Sarajevo                                                                                                                                                                                                                                                                                                             |
| Pacific   | Pacific/Apia, Pacific/Auckland, Pacific/Chatham, Pacific/Fiji,<br>Pacific/Guam, Pacific/Honolulu, Pacific/Kiritimati, Pacific/Marquesas,<br>Pacific/Samoa, Pacific/Tongatapu, Pacific/Wake                                                                                                                                                                                                                                                                                                                                      |
| US        | US/Alaska, US/Central, US/East-Indiana, US/Eastern,<br>US/Pacific                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| UTC       | UTC                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
