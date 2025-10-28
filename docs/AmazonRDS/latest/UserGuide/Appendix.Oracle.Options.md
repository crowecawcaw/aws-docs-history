# Overview of Oracle DB options

To enable options for your Oracle database, add them to an option group, and then associate the option group
with your DB instance. For more information, see [Working with option groups](USER_WorkingWithOptionGroups.md "USER_WorkingWithOptionGroups.md").

###### Topics

- [Summary of Oracle Database options](#Appendix.Oracle.Options.summary "#Appendix.Oracle.Options.summary")
- [Options supported for different editions](#Appendix.Oracle.Options.editions "#Appendix.Oracle.Options.editions")
- [Memory requirements for specific options](#Appendix.Oracle.Options.memory "#Appendix.Oracle.Options.memory")

## Summary of Oracle Database options

You can add the following options for Oracle DB instances.

| Option                                                                                        | Option ID                   |
| --------------------------------------------------------------------------------------------- | --------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Amazon S3 integration](oracle-s3-integration.md "oracle-s3-integration.md")                  | `S3_INTEGRATION`            |
| [Oracle Application Express (APEX)](Appendix.Oracle.Options.md "Appendix.Oracle.Options.md")  | `APEX` `APEX-DEV`           |
| [Oracle Enterprise Manager](Oracle.Options.md "Oracle.Options.md")                            | `OEM` `OEM_AGENT`           |
| [Oracle Java virtual machine](oracle-options-java.md "oracle-options-java.md")                | `JVM`                       |
| [Oracle Label Security](Oracle.Options.md "Oracle.Options.md")                                | `OLS`                       |
| [Oracle Locator](Oracle.Options.md "Oracle.Options.md")                                       | `LOCATOR`                   |
| [Oracle native network encryption](Appendix.Oracle.Options.md "Appendix.Oracle.Options.md")   | `NATIVE_NETWORK_ENCRYPTION` |
| [Oracle OLAP](Oracle.Options.md "Oracle.Options.md")                                          | `OLAP`                      |
| [Oracle Secure Sockets Layer](Appendix.Oracle.Options.md "Appendix.Oracle.Options.md")        | `SSL`                       |
| [Oracle Spatial](Oracle.Options.md "Oracle.Options.md")                                       | `SPATIAL`                   |
| [Oracle SQLT](Oracle.Options.md "Oracle.Options.md")                                          | `SQLT`                      |
| [Oracle Statspack](Appendix.Oracle.Options.md "Appendix.Oracle.Options.md")                   | `STATSPACK`                 |
| [Oracle time zone](Appendix.Oracle.Options.md "Appendix.Oracle.Options.md")                   | `Timezone`                  |
| [Oracle time zone file autoupgrade](Appendix.Oracle.Options.md "Appendix.Oracle.Options.md")  | `TIMEZONE_FILE_AUTOUPGRADE` |
| [Oracle Transparent Data Encryption](Appendix.Oracle.Options.md "Appendix.Oracle.Options.md") | `TDE`                       |
| [Oracle UTL_MAIL](Oracle.Options.md "Oracle.Options.md")                                      | `UTL_MAIL`                  |
| [Oracle XML DB](Appendix.Oracle.Options.md "Appendix.Oracle.Options.md")                      | `XMLDB`                     | ## Options supported for different editions RDS for Oracle prevents you from adding options to an edition if they aren't supported. To find out which RDS options are supported in different Oracle Database editions, use the command `aws rds describe-option-group-options`. The following example lists supported options for Oracle Database 19c Enterprise Edition. `aws rds describe-option-group-options \ --engine-name oracle-ee \ --major-engine-version 19` For more information, see [describe-option-group-options](../../../cli/latest/reference/rds/describe-option-group-options.md "../../../cli/latest/reference/rds/describe-option-group-options.md") in the _AWS CLI Command Reference_. ## Memory requirements for specific options Some options require additional memory to run on your DB instance. For example, Oracle Enterprise Manager Database Control uses about 300 MB of RAM. If you enable this option for a small DB instance, you might encounter performance problems due to memory constraints. You can adjust the Oracle parameters so that the database requires less RAM. Alternatively, you can scale up to a larger DB instance. |
