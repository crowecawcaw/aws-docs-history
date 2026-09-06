

# Setting the database time zone
<a name="Appendix.Oracle.CommonDBATasks.TimeZoneSupport"></a>

You can set the time zone of your Amazon RDS Oracle database in the following ways: 
+ The `Timezone` option

  The `Timezone` option changes the time zone at the host level and affects all date columns and values such as `SYSDATE`. For more information, see [Oracle time zone](Appendix.Oracle.Options.Timezone.md). 
+ The Amazon RDS procedure `rdsadmin.rdsadmin_util.alter_db_time_zone`

  The `alter_db_time_zone` procedure changes the time zone for only certain data types, and doesn't change `SYSDATE`. There are additional restrictions on setting the time zone listed in the [Oracle documentation](https://docs.oracle.com/en/database/oracle/oracle-database/19/nlspg/datetime-data-types-and-time-zone-support.html). 

**Note**  
You can also set the default time zone for Oracle Scheduler. For more information, see [Setting the time zone for Oracle Scheduler jobs](Appendix.Oracle.CommonDBATasks.Scheduler.md#Appendix.Oracle.CommonDBATasks.Scheduler.TimeZone).

The `alter_db_time_zone` procedure has the following parameters. 



| Parameter name | Data type | Default | Required | Description | 
| --- | --- | --- | --- | --- | 
| `p_new_tz` | varchar2 | — | Yes | The new time zone as a named region or an absolute offset from Coordinated Universal Time (UTC). Valid offsets range from -12:00 to \+14:00.  | 

The following example changes the time zone to UTC plus three hours. 

```
EXEC rdsadmin.rdsadmin_util.alter_db_time_zone(p_new_tz => '{{+3:00}}');
```

The following example changes the time zone to the Africa/Algiers time zone. 

```
EXEC rdsadmin.rdsadmin_util.alter_db_time_zone(p_new_tz => '{{Africa/Algiers}}');
```

After you alter the time zone by using the `alter_db_time_zone` procedure, reboot your DB instance for the change to take effect. For more information, see [Rebooting a DB instance](USER_RebootInstance.md). For information about upgrading time zones, see [Time zone considerations](USER_UpgradeDBInstance.Oracle.OGPG.md#USER_UpgradeDBInstance.Oracle.OGPG.DST).