# Setting the default displayed values for full redaction

To change the default displayed values for full redaction on your Amazon RDS Oracle
instance, use the Amazon RDS procedure
`rdsadmin.rdsadmin_util.dbms_redact_upd_full_rdct_val`. Note that you
create a redaction policy with the `DBMS_REDACT` PL/SQL package, as
explained in the Oracle Database documentation. The
`dbms_redact_upd_full_rdct_val` procedure specifies the characters to
display for different data types affected by an existing policy.

The `dbms_redact_upd_full_rdct_val` procedure has the following
parameters.

| Parameter name    | Data type                | Default | Required | Description                                                                            |
| ----------------- | ------------------------ | ------- | -------- | -------------------------------------------------------------------------------------- |
| `p_number_val`    | number                   | Null    | No       | Modifies the default value for columns of the<br>`NUMBER` data type.                   |
| `p_binfloat_val`  | binary_float             | Null    | No       | Modifies the default value for columns of the<br>`BINARY_FLOAT` data type.             |
| `p_bindouble_val` | binary_double            | Null    | No       | Modifies the default value for columns of the<br>`BINARY_DOUBLE` data type.            |
| `p_char_val`      | char                     | Null    | No       | Modifies the default value for columns of the<br>`CHAR` data type.                     |
| `p_varchar_val`   | varchar2                 | Null    | No       | Modifies the default value for columns of the<br>`VARCHAR2` data type.                 |
| `p_nchar_val`     | nchar                    | Null    | No       | Modifies the default value for columns of the<br>`NCHAR` data type.                    |
| `p_nvarchar_val`  | nvarchar2                | Null    | No       | Modifies the default value for columns of the<br>`NVARCHAR2` data type.                |
| `p_date_val`      | date                     | Null    | No       | Modifies the default value for columns of the<br>`DATE` data type.                     |
| `p_ts_val`        | timestamp                | Null    | No       | Modifies the default value for columns of the<br>`TIMESTAMP` data type.                |
| `p_tswtz_val`     | timestamp with time zone | Null    | No       | Modifies the default value for columns of the `TIMESTAMP<br>WITH TIME ZONE` data type. |
| `p_blob_val`      | blob                     | Null    | No       | Modifies the default value for columns of the<br>`BLOB` data type.                     |
| `p_clob_val`      | clob                     | Null    | No       | Modifies the default value for columns of the<br>`CLOB` data type.                     |
| `p_nclob_val`     | nclob                    | Null    | No       | Modifies the default value for columns of the<br>`NCLOB` data type.                    |

The following example changes the default redacted value to \* for the
`CHAR` data type:

```
EXEC rdsadmin.rdsadmin_util.dbms_redact_upd_full_rdct_val(p_char_val => '*');
```

The following example changes the default redacted values for `NUMBER`,
`DATE`, and `CHAR` data types:

```
BEGIN
rdsadmin.rdsadmin_util.dbms_redact_upd_full_rdct_val(
    p_number_val=>1,
    p_date_val=>to_date('1900-01-01','YYYY-MM-DD'),
    p_varchar_val=>'X');
END;
/
```

After you alter the default values for full redaction with the
`dbms_redact_upd_full_rdct_val` procedure, reboot your DB instance for the
change to take effect. For more information, see [Rebooting a DB instance](USER_RebootInstance.md "USER_RebootInstance.md").
