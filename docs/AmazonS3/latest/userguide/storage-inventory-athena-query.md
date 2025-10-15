# Querying Amazon S3 Inventory with Amazon Athena

You can query Amazon S3 Inventory files with standard SQL queries by using Amazon Athena in all
 Regions where Athena is available. To check for AWS Region availability, see the [AWS Region Table](https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/ "https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/"). 

Athena can query Amazon S3 Inventory files in [Apache optimized row columnar (ORC)](https://orc.apache.org/ "https://orc.apache.org/"), [Apache Parquet](https://parquet.apache.org/ "https://parquet.apache.org/"), or
 comma-separated values (CSV) format. When you use Athena to query inventory files, we
 recommend that you use ORC-formatted or Parquet-formatted inventory files.
 The ORC and Parquet formats provide faster query performance and lower query
 costs. ORC and Parquet are self-describing, type-aware columnar file formats
 designed for [Apache Hadoop](http://hadoop.apache.org/ "http://hadoop.apache.org/").
 The columnar format lets the reader read, decompress, and process only the columns that are
 required for the current query. The ORC and Parquet formats for Amazon S3
 Inventory are available in all AWS Regions.

###### To use Athena to query Amazon S3 Inventory files

1. Create an Athena table. For information about creating a table, see [Creating Tables in Amazon Athena](https://docs.aws.amazon.com/athena/latest/ug/creating-tables.html "https://docs.aws.amazon.com/athena/latest/ug/creating-tables.html") in
 the *Amazon Athena User Guide*.
2. Create your query by using one of the following sample query templates, depending
 on whether you're querying an ORC-formatted, a Parquet-formatted, or a CSV-formatted
 inventory report. 




	* When you're using Athena to query an ORC-formatted inventory report, use
	 the following sample query as a template.
	
	
	The following sample query includes all the optional fields in an
	 ORC-formatted inventory report. 
	
	
	To use this sample query, do the following: 
	
	
	
	
		+ Replace ``your_table_name``
		 with the name of the Athena table that you created.
		+ Remove any optional fields that you did not choose for your
		 inventory so that the query corresponds to the fields chosen for
		 your inventory.
		+ Replace the following bucket name and inventory location
		 (the configuration ID) as appropriate for your configuration.
		
		
		`s3://`amzn-s3-demo-bucket`/`config-ID`/hive/`
		+ Replace the
		 ``2022-01-01-00-00`` date
		 under `projection.dt.range` with the first day of the time range within which you
		 partition the data in Athena. For more information, see [Partitioning data in Athena](https://docs.aws.amazon.com/athena/latest/ug/partitions.html "https://docs.aws.amazon.com/athena/latest/ug/partitions.html").
	
	```
	CREATE EXTERNAL TABLE `your_table_name`(
	         bucket string,
	         key string,
	         version_id string,
	         is_latest boolean,
	         is_delete_marker boolean,
	         size bigint,
	         last_modified_date timestamp,
	         e_tag string,
	         storage_class string,
	         is_multipart_uploaded boolean,
	         replication_status string,
	         encryption_status string,
	         object_lock_retain_until_date bigint,
	         object_lock_mode string,
	         object_lock_legal_hold_status string,
	         intelligent_tiering_access_tier string,
	         bucket_key_status string,
	         checksum_algorithm string,
	         object_access_control_list string,
	         object_owner string
	) PARTITIONED BY (
	        dt string
	)
	ROW FORMAT SERDE 'org.apache.hadoop.hive.ql.io.orc.OrcSerde'
	  STORED AS INPUTFORMAT 'org.apache.hadoop.hive.ql.io.SymlinkTextInputFormat'
	  OUTPUTFORMAT 'org.apache.hadoop.hive.ql.io.IgnoreKeyTextOutputFormat'
	  LOCATION 's3://`source-bucket/config-ID`/hive/'
	  TBLPROPERTIES (
	    "projection.enabled" = "true",
	    "projection.dt.type" = "date",
	    "projection.dt.format" = "yyyy-MM-dd-HH-mm",
	    "projection.dt.range" = "`2022-01-01-00-00`,NOW",
	    "projection.dt.interval" = "1",
	    "projection.dt.interval.unit" = "HOURS"
	  );
	```
	* When you're using Athena to query a Parquet-formatted
	 inventory report, use the sample query for an ORC-formatted report. However,
	 use the following Parquet SerDe in place of the ORC SerDe in
	 the `ROW FORMAT SERDE` statement.
	
	
	
	```
	ROW FORMAT SERDE 'org.apache.hadoop.hive.ql.io.parquet.serde.ParquetHiveSerDe'
	```
	* When you're using Athena to query a CSV-formatted inventory report, use the
	 following sample query as a template.
	
	
	The following sample query includes all the optional fields in an
	 CSV-formatted inventory report. 
	
	
	To use this sample query, do the following: 
	
	
	
	
		+ Replace ``your_table_name``
		 with the name of the Athena table that you created.
		+ Remove any optional fields that you did not choose for your
		 inventory so that the query corresponds to the fields chosen for
		 your inventory.
		+ Replace the following bucket name and inventory location
		 (the configuration ID) as appropriate for your configuration. 
		
		
		`s3://`amzn-s3-demo-bucket`/`config-ID`/hive/`
		+ Replace the
		 ``2022-01-01-00-00`` date
		 under `projection.dt.range` with the first day of the time range within which you
		 partition the data in Athena. For more information, see [Partitioning data in Athena](https://docs.aws.amazon.com/athena/latest/ug/partitions.html "https://docs.aws.amazon.com/athena/latest/ug/partitions.html").
	
	```
	CREATE EXTERNAL TABLE `your_table_name`(
	         bucket string,
	         key string,
	         version_id string,
	         is_latest boolean,
	         is_delete_marker boolean,
	         size string,
	         last_modified_date string,
	         e_tag string,
	         storage_class string,
	         is_multipart_uploaded boolean,
	         replication_status string,
	         encryption_status string,
	         object_lock_retain_until_date string,
	         object_lock_mode string,
	         object_lock_legal_hold_status string,
	         intelligent_tiering_access_tier string,
	         bucket_key_status string,
	         checksum_algorithm string,
	         object_access_control_list string,
	         object_owner string
	) PARTITIONED BY (
	        dt string
	)
	ROW FORMAT SERDE 'org.apache.hadoop.hive.serde2.OpenCSVSerde'
	  STORED AS INPUTFORMAT 'org.apache.hadoop.hive.ql.io.SymlinkTextInputFormat'
	  OUTPUTFORMAT 'org.apache.hadoop.hive.ql.io.IgnoreKeyTextOutputFormat'
	  LOCATION 's3://`source-bucket/config-ID`/hive/'
	  TBLPROPERTIES (
	    "projection.enabled" = "true",
	    "projection.dt.type" = "date",
	    "projection.dt.format" = "yyyy-MM-dd-HH-mm",
	    "projection.dt.range" = "`2022-01-01-00-00`,NOW",
	    "projection.dt.interval" = "1",
	    "projection.dt.interval.unit" = "HOURS"
	  );
	```
3. You can now run various queries on your inventory, as shown in the following
 examples. Replace each ``user input
 placeholder`` with your own information.



```
# Get a list of the latest inventory report dates available.
SELECT DISTINCT dt FROM `your_table_name` ORDER BY 1 DESC limit 10;
          
# Get the encryption status for a provided report date.
SELECT encryption_status, count(*) FROM `your_table_name` WHERE dt = '`YYYY-MM-DD-HH-MM`' GROUP BY encryption_status;
          
# Get the encryption status for inventory report dates in the provided range.
SELECT dt, encryption_status, count(*) FROM `your_table_name` 
WHERE dt > '`YYYY-MM-DD-HH-MM`' AND dt < '`YYYY-MM-DD-HH-MM`' GROUP BY dt, encryption_status;
```

When you configure S3 Inventory to add the Object Access Control List (Object ACL)
 field to an inventory report, the report displays the value for the Object ACL field
 as a base64-encoded string. To get the decoded value in JSON for the Object ACL
 field, you can query this field by using Athena. See the following query examples.
 For more information about the Object ACL field, see [Working with the Object ACL field](objectacl.md "objectacl.md").



```
# Get the S3 keys that have Object ACL grants with public access.
WITH grants AS (
    SELECT key,
        CAST(
            json_extract(from_utf8(from_base64(object_access_control_list)), '$.grants') AS ARRAY(MAP(VARCHAR, VARCHAR))
        ) AS grants_array
    FROM `your_table_name`
)
SELECT key,
       grants_array,
       grant
FROM grants, UNNEST(grants_array) AS t(grant)
WHERE element_at(grant, 'uri') = 'http://acs.amazonaws.com/groups/global/AllUsers'
            
```


```
# Get the S3 keys that have Object ACL grantees in addition to the object owner.
WITH grants AS 
    (SELECT key,
    from_utf8(from_base64(object_access_control_list)) AS object_access_control_list,
         object_owner,
         CAST(json_extract(from_utf8(from_base64(object_access_control_list)),
         '$.grants') AS ARRAY(MAP(VARCHAR, VARCHAR))) AS grants_array
    FROM `your_table_name`)
SELECT key,
       grant,
       objectowner
FROM grants, UNNEST(grants_array) AS t(grant)
WHERE cardinality(grants_array) > 1 AND element_at(grant, 'canonicalId') != object_owner;
            
```


```
# Get the S3 keys with READ permission that is granted in the Object ACL. 
WITH grants AS (
    SELECT key,
        CAST(
            json_extract(from_utf8(from_base64(object_access_control_list)), '$.grants') AS ARRAY(MAP(VARCHAR, VARCHAR))
        ) AS grants_array
    FROM `your_table_name`
)
SELECT key,
       grants_array,
       grant
FROM grants, UNNEST(grants_array) AS t(grant)
WHERE element_at(grant, 'permission') = 'READ';
            
```


```
# Get the S3 keys that have Object ACL grants to a specific canonical user ID.
WITH grants AS (
    SELECT key,
        CAST(
            json_extract(from_utf8(from_base64(object_access_control_list)), '$.grants') AS ARRAY(MAP(VARCHAR, VARCHAR))
        ) AS grants_array
    FROM `your_table_name`
)
SELECT key,
       grants_array,
       grant
FROM grants, UNNEST(grants_array) AS t(grant)
WHERE element_at(grant, 'canonicalId') = 'user-canonical-id';
            
```


```
# Get the number of grantees on the Object ACL.
SELECT key,
       object_access_control_list,
       json_array_length(json_extract(object_access_control_list,'$.grants')) AS grants_count
FROM `your_table_name`;
            
```
For more information about using Athena, see the [Amazon Athena User Guide](https://docs.aws.amazon.com/athena/latest/ug/ "https://docs.aws.amazon.com/athena/latest/ug/").
