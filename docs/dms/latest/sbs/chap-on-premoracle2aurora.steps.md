# Troubleshooting

The two most common areas people have issues with when working with Oracle as a source and Aurora MySQL as a target are: supplemental logging and case sensitivity.

- Supplemental logging — With Oracle, in order to replication change data supplemental logging must be enabled. However, if you enable supplemental logging at the database level, it sometimes still need to enable it when creating new tables. The best remedy for this is to allow DMS to enable supplemental logging for you using the extra connection attribute:

```
addSupplementalLogging=Y
```

- Case sensitivity — Oracle is case-insensitive (unless you use quotes around your object names). However, text appears in the upper case. Thus, AWS DMS defaults to naming your target objects in the upper case. In most cases, you’ll want to use transformations to change schema, table and column names to lower case.
  For more tips, see the AWS DMS troubleshooting section in the [Troubleshooting migration tasks in Database Migration Service](../userguide/CHAP_Troubleshooting.md "../userguide/CHAP_Troubleshooting.md").

To troubleshoot issues specific to Oracle, see the Oracle troubleshooting section: [Troubleshooting issues with Oracle](../userguide/CHAP_Troubleshooting.md#CHAP_Troubleshooting.Oracle "../userguide/CHAP_Troubleshooting.md#CHAP_Troubleshooting.Oracle").

To troubleshoot Aurora MySQL issues, see the MySQL troubleshooting section: [Troubleshooting issues with MySQL](../userguide/CHAP_Troubleshooting.md#CHAP_Troubleshooting.MySQL "../userguide/CHAP_Troubleshooting.md#CHAP_Troubleshooting.MySQL").
