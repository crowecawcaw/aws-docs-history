# Supported data types

AWS IoT SiteWise query language supports the following data types.

| Scalar value | **Data type**                                                                                              | **Description**        |
| ------------ | ---------------------------------------------------------------------------------------------------------- | ---------------------- | ----------------------------------------------- | --------------------------------------------- |
| `STRING`     | A string of maximum length 1024 bytes.                                                                     |
| `INTEGER`    | A signed 32-bit integer with a range from `-2,147,483,648 to<br>2,147,483,647` .                           |
| `DOUBLE`     | A floating point number with range from `–10^100 to 10^100`,<br>or `Nan` with `IEEE 754` double precision. |
| `BOOLEAN`    | `true` or `false`.                                                                                         |
| `TIMESTAMP`  | ISO-8601 compliant timestamps:<br>• '`yyyy-MM-dd HH:mm:ss[.SSS]`'<br>• `TIMESTAMP` '`yyyy-MM-dd[\s         | T]HH:mm:ss[.SSS]+HH:mm | 'Z']`'<br>• '`yyyy-MM-dd'T'HH:mm:ss[.SSS]+HH:mm | 'Z']`'<br>• '`yyyy-MM-dd'T'HH:mm:ss+[hh:mm]`' |

###### Note

`Null`: A boolean `true` indicating a lack of defined data.

`TIMESTAMP` value examples:

```
TIMESTAMP '2025-12-21 23:59:59.999Z'
TIMESTAMP '2025-12-21 23:59:59+23:59'
'2025-12-21 23:59:59'
'2025-12-21T23:59:59.123+11:11'
```

###### Note

The double precision data is not exact. Some values are not converted exactly, and
will not represent all real numbers due to limited precision. Floating-point data in the
query may not be the same value represented internally. The value is rounded if the
precision of an input number is too high.
