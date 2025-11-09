# Options for MySQL DB instances

Following, you can find a description of options, or additional features, that are available for Amazon RDS
instances running the MySQL DB engine. To enable these options, you can add them to a custom
option group, and then associate the option group with your DB instance. For more
information about working with option groups, see [Working with option groups](USER_WorkingWithOptionGroups.md "USER_WorkingWithOptionGroups.md").

Amazon RDS supports the following options for MySQL:

| Option                                                                                             | Option ID              | Engine versions                                                                     |
| -------------------------------------------------------------------------------------------------- | ---------------------- | ----------------------------------------------------------------------------------- |
| [MariaDB Audit Plugin support for<br>MySQL](Appendix.MySQL.Options.md "Appendix.MySQL.Options.md") | `MARIADB_AUDIT_PLUGIN` | All MySQL 8.4 versionsMySQL 8.0.28 and higher 8.0<br>versionsAll MySQL 5.7 versions |
| [MySQL memcached support](Appendix.MySQL.Options.md "Appendix.MySQL.Options.md")                   | `MEMCACHED`            | All MySQL 5.7 and 8.0 versions                                                      |
