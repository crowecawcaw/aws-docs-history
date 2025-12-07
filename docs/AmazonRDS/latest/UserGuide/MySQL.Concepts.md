# Local time zone for MySQL DB instances

By default, the time zone for a MySQL DB instance is Universal Time Coordinated
(UTC). You can set the time zone for your DB instance to the local time zone for your application instead.

To set the local time zone for a DB instance, set the `time_zone` parameter
in the parameter group for your DB instance to one of the supported values listed later
in this section. When you set the `time_zone` parameter for a parameter
group, all DB instances and read replicas that are using that parameter group change to
use the new local time zone. For information on setting parameters in a parameter group,
see [Parameter groups for Amazon RDS](USER_WorkingWithParamGroups.md "USER_WorkingWithParamGroups.md").

After you set the local time zone, all new connections to the database reflect the change. If you have any
open connections to your database when you change the local time zone, you won't see the local time zone update
until after you close the connection and open a new connection.

You can set a different local time zone for a DB instance and one or more of its read
replicas. To do this, use a different parameter group for the DB instance and the
replica or replicas and set the `time_zone` parameter in each parameter group
to a different local time zone.

If you are replicating across AWS Regions, then the source DB instance and the
read replica use different parameter groups (parameter groups are unique to an AWS Region).
To use the same local time zone for each instance, you must set the
`time_zone` parameter in the instance's and read replica's parameter
groups.

When you restore a DB instance from a DB snapshot, the local time zone is set to UTC. You can update the
time zone to your local time zone after the restore is complete. If you restore a DB instance to a point
in time, then the local time zone for the restored DB instance is the time zone setting from the
parameter group of the restored DB instance.

The Internet Assigned Numbers Authority (IANA) publishes new time zones at [https://www.iana.org/time-zones](https://www.iana.org/time-zones "https://www.iana.org/time-zones") several times a year. Every time RDS releases a new minor maintenance release of MySQL,
it ships with the latest time zone data at the time of the release. When you use the latest RDS for MySQL versions, you have recent
time zone data from RDS. To ensure that your DB instance has recent time zone data, we recommend upgrading to a higher DB
engine version. Alternatively, you can modify the time zone tables in MariaDB DB instances manually. To do so, you can use
SQL commands or run the [mysql_tzinfo_to_sql tool](https://dev.mysql.com/doc/refman/8.0/en/mysql-tzinfo-to-sql.html "https://dev.mysql.com/doc/refman/8.0/en/mysql-tzinfo-to-sql.html")
in a SQL client. After updating the time zone data manually, reboot your DB instance so that the changes take effect. RDS doesn't
modify or reset the time zone data of running DB instances. New time zone data is installed only when you perform a database engine
version upgrade.

You can set your local time zone to one of the following values.

| Zone      | Time zone                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| --------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Africa    | Africa/Cairo, Africa/Casablanca, Africa/Harare, Africa/Monrovia,<br>Africa/Nairobi, Africa/Tripoli, Africa/Windhoek                                                                                                                                                                                                                                                                                                                            |
| America   | America/Araguaina, America/Asuncion, America/Bogota,<br>America/Buenos_Aires, America/Caracas, America/Chihuahua,<br>America/Cuiaba, America/Denver, America/Fortaleza, America/Guatemala,<br>America/Halifax, America/Manaus, America/Matamoros, America/Monterrey,<br>America/Montevideo, America/Phoenix, America/Santiago,<br>America/Tijuana                                                                                              |
| Asia      | Asia/Amman, Asia/Ashgabat, Asia/Baghdad, Asia/Baku, Asia/Bangkok,<br>Asia/Beirut, Asia/Calcutta, Asia/Damascus, Asia/Dhaka, Asia/Irkutsk,<br>Asia/Jerusalem, Asia/Kabul, Asia/Karachi, Asia/Kathmandu,<br>Asia/Krasnoyarsk, Asia/Magadan, Asia/Muscat, Asia/Novosibirsk,<br>Asia/Riyadh, Asia/Seoul, Asia/Shanghai, Asia/Singapore, Asia/Taipei,<br>Asia/Tehran, Asia/Tokyo, Asia/Ulaanbaatar, Asia/Vladivostok,<br>Asia/Yakutsk, Asia/Yerevan |
| Atlantic  | Atlantic/Azores                                                                                                                                                                                                                                                                                                                                                                                                                                |
| Australia | Australia/Adelaide, Australia/Brisbane, Australia/Darwin,<br>Australia/Hobart, Australia/Perth, Australia/Sydney                                                                                                                                                                                                                                                                                                                               |
| Brazil    | Brazil/DeNoronha, Brazil/East                                                                                                                                                                                                                                                                                                                                                                                                                  |
| Canada    | Canada/Newfoundland, Canada/Saskatchewan, Canda/Yukon                                                                                                                                                                                                                                                                                                                                                                                          |
| Europe    | Europe/Amsterdam, Europe/Athens, Europe/Dublin, Europe/Helsinki,<br>Europe/Istanbul, Europe/Kaliningrad Europe/Moscow, Europe/Paris,<br>Europe/Prague, Europe/Sarajevo                                                                                                                                                                                                                                                                         |
| Pacific   | Pacific/Auckland, Pacific/Fiji, Pacific/Guam, Pacific/Honolulu,<br>Pacific/Samoa                                                                                                                                                                                                                                                                                                                                                               |
| US        | US/Alaska, US/Central, US/East-Indiana, US/Eastern,<br>US/Pacific                                                                                                                                                                                                                                                                                                                                                                              |
| UTC       | UTC                                                                                                                                                                                                                                                                                                                                                                                                                                            |
