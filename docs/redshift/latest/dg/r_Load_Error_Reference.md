Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Load error reference

If any errors occur while loading data from a file, query the [STL_LOAD_ERRORS](r_STL_LOAD_ERRORS.md "r_STL_LOAD_ERRORS.md") table to identify
the error and determine the possible explanation. The following table lists all error
codes that might occur during data loads:

## Load error codes

| Error code | Description                                                                                                                                                                      |
| ---------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1200       | Unknown parse error. Contact support.                                                                                                                                            |
| 1201       | Field delimiter was not found in the input file.                                                                                                                                 |
| 1202       | Input data had more columns than were defined in<br>the DDL.                                                                                                                     |
| 1203       | Input data had fewer columns than were defined in<br>the DDL.                                                                                                                    |
| 1204       | Input data exceeded the acceptable range for the<br>data type.                                                                                                                   |
| 1205       | Date format is not valid. See [DATEFORMAT and TIMEFORMAT<br>strings](r_DATEFORMAT_and_TIMEFORMAT_strings.md "r_DATEFORMAT_and_TIMEFORMAT_strings.md") for valid<br>formats.      |
| 1206       | Timestamp format is not valid. See [DATEFORMAT and TIMEFORMAT<br>strings](r_DATEFORMAT_and_TIMEFORMAT_strings.md "r_DATEFORMAT_and_TIMEFORMAT_strings.md") for valid<br>formats. |
| 1207       | Data contained a value outside of the expected<br>range of 0-9.                                                                                                                  |
| 1208       | FLOAT data type format error.                                                                                                                                                    |
| 1209       | DECIMAL data type format error.                                                                                                                                                  |
| 1210       | BOOLEAN data type format error.                                                                                                                                                  |
| 1211       | Input line contained no data.                                                                                                                                                    |
| 1212       | Load file was not found.                                                                                                                                                         |
| 1213       | A field specified as NOT NULL contained no data.                                                                                                                                 |
| 1214       | Delimiter not found.                                                                                                                                                             |
| 1215       | CHAR field error.                                                                                                                                                                |
| 1216       | Input line is not valid.                                                                                                                                                         |
| 1217       | Identity column value is not valid.                                                                                                                                              |
| 1218       | When using NULL AS '\0', a field containing a null<br>terminator (NUL, or UTF-8 0000) contained more than one byte.                                                              |
| 1219       | UTF-8 hexadecimal contains an invalid<br>digit.                                                                                                                                  |
| 1220       | String contains invalid or unsupported UTF-8 code<br>points.                                                                                                                     |
| 1221       | Encoding of the file is not the same as that<br>specified in the COPY command.                                                                                                   |
| 1222       | Integer value overflow error.                                                                                                                                                    |
| 1223       | Data type not valid.                                                                                                                                                             |
| 1224       | Input data not well formed JSON format for super data type.                                                                                                                      |
| 8001       | COPY with MANIFEST parameter requires full path of an Amazon S3 object.                                                                                                          |
| 9005       | Invalid end key specified.                                                                                                                                                       |
