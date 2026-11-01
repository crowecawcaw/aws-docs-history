

# Differences between PySpark 1.0 and PySpark 2.0 analysis templates
<a name="pyspark-template-versions"></a>

PySpark analysis templates that use the `PYSPARK_2_0` format (PySpark 2.0) let you choose CSV or Parquet results and run multiple jobs at the same time in a collaboration. They also differ from PySpark 1.0 analysis templates in supported column types and CSV output. Existing PySpark 1.0 analysis templates aren't affected.

**Topics**
+ [Moving to PySpark 2.0](#pyspark-template-versions-migration)
+ [Result format](#pyspark-template-versions-result-format)
+ [Multiple job concurrency in a collaboration](#pyspark-template-versions-concurrency)
+ [Supported column types](#pyspark-template-versions-types)
+ [CSV output differences](#pyspark-template-versions-csv)

## Moving to PySpark 2.0
<a name="pyspark-template-versions-migration"></a>

Existing PySpark 1.0 analysis templates continue to produce the same output as before. You can move to PySpark 2.0 on your own timeline. To move, create an analysis template that uses the `PYSPARK_2_0` format and have collaboration members review it. Before you switch, do the following:
+ Check that your DataFrames use only column types that your result format supports.
+ Test any downstream systems that read your CSV results.
+ If you read Parquet results with tools other than Spark, test your timestamp and interval columns.
+ Confirm that the service role that writes job results still allows `s3:GetBucketLocation` and `s3:ListBucket`. For more information about this role, see [Create a service role to write results of a PySpark job](setting-up-roles.md#create-role-pyspark-job).

If you move back to PySpark 1.0, set the result format for job results back to **CSV**, because PySpark 1.0 doesn't support Parquet.

## Result format
<a name="pyspark-template-versions-result-format"></a>

If your membership can receive results, you choose whether job results are written as CSV or Parquet. If you set the result format to Parquet, jobs that use a PySpark 1.0 analysis template fail validation. For more information about setting the result format, see [Receiving job results](receive-job-results.md).

## Multiple job concurrency in a collaboration
<a name="pyspark-template-versions-concurrency"></a>

PySpark 2.0 jobs can run at the same time in a membership, up to the **Concurrent ongoing job per membership** quota. By default, this quota is 5. The **Concurrent PySpark jobs per account** quota also applies. PySpark 1.0 jobs run one at a time. You can't start a PySpark 1.0 job while another job is in progress in the membership, or start another job while a PySpark 1.0 job is in progress. If you start a job that exceeds these limits, `StartProtectedJob` returns a `ServiceQuotaExceededException`. For default values and how to request a quota increase, see [AWS Clean Rooms quotas](clean-rooms-quotas.md).

## Supported column types
<a name="pyspark-template-versions-types"></a>

If a DataFrame contains a column type that the result format doesn't support, the job fails.


| Column type | PySpark 1.0 CSV | PySpark 2.0 CSV | PySpark 2.0 Parquet | 
| --- | --- | --- | --- | 
| Numeric, string, Boolean, DATE, TIMESTAMP\_NTZ, and day-time INTERVAL | Yes | Yes | Yes | 
| Year-month INTERVAL | No | Yes | Yes | 
| STRUCT | Yes | No | Yes | 
| ARRAY, MAP, and BINARY | No | No | Yes | 
| Column of NULL values with no type | Yes | No | No | 

PySpark 2.0 also supports `TIMESTAMP` columns in both formats. For complex types, choose Parquet results. For a column that contains only `NULL` values, cast it to a type, for example `CAST(NULL AS STRING)`.

## CSV output differences
<a name="pyspark-template-versions-csv"></a>

The following table shows values that PySpark 2.0 writes differently. Decimals, dates, nulls, and other values not listed are written the same way in both versions.


| Value | PySpark 1.0 output | PySpark 2.0 output | 
| --- | --- | --- | 
| Boolean true | True | true | 
| Double 1e308 | 1e\+308 | 1.0E308 | 
| Double NaN | Empty field | NaN | 
| Double positive infinity | inf | Infinity | 
| Integer 1, in a column that contains a null | 1.0 | 1 | 
| TIMESTAMP\_NTZ 2026-01-02 03:04:05.123456 | 2026-01-02T03:04:05 | 2026-01-02T03:04:05.123 | 
| Day-time interval | 1 days 02:03:04.123456 | INTERVAL '1 02:03:04.123456' DAY TO SECOND | 
| String say "hi" | "say ""hi""" | "say \\"hi\\"" | 
| String with leading or trailing spaces | Spaces kept | Spaces removed | 
| Empty string | Empty field | "" | 

PySpark 2.0 writes `TIMESTAMP` values with milliseconds and a time zone offset, for example `2026-01-02T03:04:05.123Z`.

Because PySpark 2.0 escapes quotation marks with a backslash, configure your CSV reader to use a backslash as the escape character (for example, `escapechar='\\'` in pandas).