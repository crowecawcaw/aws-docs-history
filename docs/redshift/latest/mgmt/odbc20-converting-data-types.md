

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# Data types conversions
<a name="odbc20-converting-data-types"></a>

The Amazon Redshift ODBC driver version 2.x supports many common data formats, converting between Amazon Redshift and SQL data types.

The following table lists the supported data type mappings.


| Amazon Redshift type | SQL type | 
| --- | --- | 
| BIGINT | SQL\_BIGINT | 
| BOOLEAN | SQL\_BIT | 
| CHAR | SQL\_CHAR | 
| DATE | SQL\_TYPE\_DATE | 
| DECIMAL | SQL\_NUMERIC | 
| DOUBLE PRECISION | SQL\_DOUBLE | 
| GEOGRAPHY | SQL\_ LONGVARBINARY | 
| GEOMETRY | SQL\_ LONGVARBINARY | 
| INTEGER | SQL\_INTEGER | 
| REAL | SQL\_REAL | 
| SMALLINT | SQL\_SMALLINT | 
| SUPER | SQL\_LONGVARCHAR | 
| TEXT | SQL\_LONGVARCHAR | 
| TIME | SQL\_TYPE\_TIME | 
| TIMETZ | SQL\_TYPE\_TIME | 
| TIMESTAMP | SQL\_TYPE\_ TIMESTAMP | 
| TIMESTAMPTZ | SQL\_TYPE\_ TIMESTAMP | 
| VARBYTE | SQL\_LONGVARBINARY | 
| VARCHAR | SQL\_VARCHAR | 