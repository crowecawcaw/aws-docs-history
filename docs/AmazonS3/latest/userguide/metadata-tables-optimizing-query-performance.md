# Optimizing metadata table query
 performance

Because S3 Metadata is based on the Apache Iceberg table format, you can optimize the
 performance and cost of your journal
 table queries by using specific time ranges.

For example, the following SQL query provides the sensitivity level of new objects in an S3 general
 purpose bucket:


```
SELECT key, object_tags['SensitivityLevel'] 
FROM "b_`general-purpose-bucket-name`"."journal"
WHERE record_type = 'CREATE'
GROUP BY object_tags['SensitivityLevel']
```
This query scans the entire journal table, which might take a long time to run. To improve
 performance, you can include the `record_timestamp` column to focus on a specific time range.
 We also recommend using the fully qualified table name, which you can find in the Amazon S3 console on the
 metadata configuration details page on the general purpose bucket's **Metadata** tab.
 Here's an updated version of the previous query that looks at new objects from the past month:


```
SELECT key, object_tags['SensitivityLevel'] 
FROM b_`general-purpose-bucket-name`"."aws-s3.b_`general-purpose-bucket-name`.journal"
WHERE record_type = 'CREATE'
AND record_timestamp > (CURRENT_TIMESTAMP – interval '1' month)
GROUP BY object_tags['SensitivityLevel']
```
To improve the performance of queries on inventory tables, make sure that you query only on the
 minimum columns that you need.
