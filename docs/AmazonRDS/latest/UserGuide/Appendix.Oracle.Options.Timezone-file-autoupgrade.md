# Preparing to update the time

zone file

A time zone file upgrade has two separate phases: prepare and upgrade. While not required, we strongly
recommend that you perform the prepare step. In this step, you find out which data will be affected by
running the PL/SQL procedure `DBMS_DST.FIND_AFFECTED_TABLES`. For more information about the
prepare window, see [Upgrading the Time Zone File and Timestamp with Time Zone Data](https://docs.oracle.com/en/database/oracle/oracle-database/19/nlspg/datetime-data-types-and-time-zone-support.html#GUID-B0ACDB2E-4B49-4EB4-B4CC-9260DAE1567A "https://docs.oracle.com/en/database/oracle/oracle-database/19/nlspg/datetime-data-types-and-time-zone-support.html#GUID-B0ACDB2E-4B49-4EB4-B4CC-9260DAE1567A") in the Oracle Database
documentation.

###### To prepare to update the time zone file

1. Connect to your Oracle database using a SQL client.
2. Determine the current timezone file version used.

```
SELECT * FROM V$TIMEZONE_FILE;
```

3. Determine the latest timezone file version available on your DB instance.

```
SELECT DBMS_DST.GET_LATEST_TIMEZONE_VERSION FROM DUAL;
```

4. Determine the total size of tables that have columns of type `TIMESTAMP WITH LOCAL TIME
ZONE` or `TIMESTAMP WITH TIME ZONE`.

```
SELECT SUM(BYTES)/1024/1024/1024 "Total_size_w_TSTZ_columns_GB"
FROM   DBA_SEGMENTS
WHERE  SEGMENT_TYPE LIKE 'TABLE%'
AND    (OWNER, SEGMENT_NAME) IN
         (SELECT OWNER, TABLE_NAME
          FROM   DBA_TAB_COLUMNS
          WHERE  DATA_TYPE LIKE 'TIMESTAMP%TIME ZONE');
```

5. Determine the names and sizes of segments that have columns of type `TIMESTAMP WITH LOCAL TIME
ZONE` or `TIMESTAMP WITH TIME ZONE`.

```
SELECT OWNER, SEGMENT_NAME, SUM(BYTES)/1024/1024/1024 "SEGMENT_SIZE_W_TSTZ_COLUMNS_GB"
FROM   DBA_SEGMENTS
WHERE  SEGMENT_TYPE LIKE 'TABLE%'
AND    (OWNER, SEGMENT_NAME) IN
         (SELECT OWNER, TABLE_NAME
          FROM   DBA_TAB_COLUMNS
          WHERE  DATA_TYPE LIKE 'TIMESTAMP%TIME ZONE')
GROUP BY OWNER, SEGMENT_NAME;
```

6.  Run the prepare step.

        * The procedure `DBMS_DST.CREATE_AFFECTED_TABLE` creates a table to store any
         affected data. You pass the name of this table to the
         `DBMS_DST.FIND_AFFECTED_TABLES` procedure. For more information, see [CREATE\_AFFECTED\_TABLE Procedure](https://docs.oracle.com/en/database/oracle/oracle-database/19/arpls/DBMS_DST.html#GUID-C53BAABA-914A-404C-9CD5-823257BE0B00 "https://docs.oracle.com/en/database/oracle/oracle-database/19/arpls/DBMS_DST.html#GUID-C53BAABA-914A-404C-9CD5-823257BE0B00") in the Oracle Database documentation.
        * This procedure `CREATE_ERROR_TABLE` creates a table to
         log errors. For more information, see [CREATE\_ERROR\_TABLE Procedure](https://docs.oracle.com/en/database/oracle/oracle-database/19/arpls/DBMS_DST.html#GUID-6A7EA024-B02D-4486-B1D6-EF6ABF5DE507 "https://docs.oracle.com/en/database/oracle/oracle-database/19/arpls/DBMS_DST.html#GUID-6A7EA024-B02D-4486-B1D6-EF6ABF5DE507") in the Oracle Database
         documentation.

    The following example creates the affected data and error tables, and finds all affected
    tables.

```
EXEC DBMS_DST.CREATE_ERROR_TABLE('`my_error_table`')
EXEC DBMS_DST.CREATE_AFFECTED_TABLE('`my_affected_table`')

EXEC DBMS_DST.BEGIN_PREPARE(`new_version`);
EXEC DBMS_DST.FIND_AFFECTED_TABLES('`my_affected_table`', TRUE, '`my_error_table`');
EXEC DBMS_DST.END_PREPARE;

SELECT * FROM `my_affected_table`;
SELECT * FROM `my_error_table`;
```

7. Query the affected and error tables.

```
SELECT * FROM `my_affected_table`;
SELECT * FROM `my_error_table`;
```
