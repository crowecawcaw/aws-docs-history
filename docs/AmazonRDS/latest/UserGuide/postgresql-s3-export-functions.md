

# Function reference
<a name="postgresql-s3-export-functions"></a>

**Topics**
+ [aws\_s3.query\_export\_to\_s3](#aws_s3.export_query_to_s3)
+ [aws\_commons.create\_s3\_uri](#aws_commons.create_s3_uri)

## aws\_s3.query\_export\_to\_s3
<a name="aws_s3.export_query_to_s3"></a>

Exports a PostgreSQL query result to an Amazon S3 bucket. The `aws_s3` extension provides the `aws_s3.query_export_to_s3` function. 

The two required parameters are `query` and `s3_info`. These define the query to be exported and identify the Amazon S3 bucket to export to. An optional parameter called `options` provides for defining various export parameters. For examples of using the `aws_s3.query_export_to_s3` function, see [Exporting query data using the aws\_s3.query\_export\_to\_s3 function](postgresql-s3-export-examples.md).

**Syntax**

```
aws_s3.query_export_to_s3(
    query text,    
    s3_info aws_commons._s3_uri_1,    
    options text,
    kms_key text
)
```Input parameters

*query*  
A required text string containing an SQL query that the PostgreSQL engine runs. The results of this query are copied to an S3 bucket identified in the `s3_info` parameter.

*s3\_info*  
An `aws_commons._s3_uri_1` composite type containing the following information about the S3 object:  
+ `bucket` – The name of the Amazon S3 bucket to contain the file.
+ `file_path` – The Amazon S3 file name and path.
+ `region` – The AWS Region that the bucket is in. For a listing of AWS Region names and associated values, see [Regions, Availability Zones, and Local Zones](Concepts.RegionsAndAvailabilityZones.md). 

  Currently, this value must be the same AWS Region as that of the exporting DB instance. The default is the AWS Region of the exporting DB instance. 
To create an `aws_commons._s3_uri_1` composite structure, see the [aws\_commons.create\_s3\_uri](#aws_commons.create_s3_uri) function.

*options*  
An optional text string containing arguments for the PostgreSQL `COPY` command. These arguments specify how the data is to be copied when exported. For more details, see the [PostgreSQL COPY documentation](https://www.postgresql.org/docs/current/sql-copy.html).

*kms\_key text*  
An optional text string containing the customer managed KMS key of the S3 bucket to export the data to.

### Alternate input parameters
<a name="aws_s3.export_query_to_s3-alternate-parameters"></a>

To help with testing, you can use an expanded set of parameters instead of the `s3_info` parameter. Following are additional syntax variations for the `aws_s3.query_export_to_s3` function. 

Instead of using the `s3_info` parameter to identify an Amazon S3 file, use the combination of the `bucket`, `file_path`, and `region` parameters.

```
aws_s3.query_export_to_s3(
    query text,    
    bucket text,    
    file_path text,    
    region text,    
    options text,
    kms_key text
)
```

*query*  
A required text string containing an SQL query that the PostgreSQL engine runs. The results of this query are copied to an S3 bucket identified in the `s3_info` parameter.

*bucket*  
A required text string containing the name of the Amazon S3 bucket that contains the file.

*file\_path*  
A required text string containing the Amazon S3 file name including the path of the file.

*region*  
An optional text string containing the AWS Region that the bucket is in. For a listing of AWS Region names and associated values, see [Regions, Availability Zones, and Local Zones](Concepts.RegionsAndAvailabilityZones.md).  
Currently, this value must be the same AWS Region as that of the exporting DB instance. The default is the AWS Region of the exporting DB instance. 

*options*  
An optional text string containing arguments for the PostgreSQL `COPY` command. These arguments specify how the data is to be copied when exported. For more details, see the [PostgreSQL COPY documentation](https://www.postgresql.org/docs/current/sql-copy.html).

*kms\_key text*  
An optional text string containing the customer managed KMS key of the S3 bucket to export the data to.

### Output parameters
<a name="aws_s3.export_query_to_s3-output-parameters"></a>

```
aws_s3.query_export_to_s3(
    OUT rows_uploaded bigint,
    OUT files_uploaded bigint,
    OUT bytes_uploaded bigint
)
```

*rows\_uploaded*  
The number of table rows that were successfully uploaded to Amazon S3 for the given query.

*files\_uploaded*  
The number of files uploaded to Amazon S3. Files are created in sizes of approximately 6 GB. Each additional file created has `_part{{XX}}` appended to the name. The `{{XX}}` represents 2, then 3, and so on as needed.

*bytes\_uploaded*  
The total number of bytes uploaded to Amazon S3.

### Examples
<a name="aws_s3.export_query_to_s3-examples"></a>

```
psql=> SELECT * from aws_s3.query_export_to_s3('select * from sample_table', '{{amzn-s3-demo-bucket}}', 'sample-filepath');
psql=> SELECT * from aws_s3.query_export_to_s3('select * from sample_table', '{{amzn-s3-demo-bucket}}', 'sample-filepath','us-west-2');
psql=> SELECT * from aws_s3.query_export_to_s3('select * from sample_table', '{{amzn-s3-demo-bucket}}', 'sample-filepath','us-west-2','format text');
```

## aws\_commons.create\_s3\_uri
<a name="aws_commons.create_s3_uri"></a>

Creates an `aws_commons._s3_uri_1` structure to hold Amazon S3 file information. You use the results of the `aws_commons.create_s3_uri` function in the `s3_info` parameter of the [aws\_s3.query\_export\_to\_s3](#aws_s3.export_query_to_s3) function. For an example of using the `aws_commons.create_s3_uri` function, see [Specifying the Amazon S3 file path to export to](postgresql-s3-export.md#postgresql-s3-export-file).

**Syntax**

```
aws_commons.create_s3_uri(
   bucket text,
   file_path text,
   region text
)
```Input parameters

*bucket*  
A required text string containing the Amazon S3 bucket name for the file.

*file\_path*  
A required text string containing the Amazon S3 file name including the path of the file.

*region*  
A required text string containing the AWS Region that the file is in. For a listing of AWS Region names and associated values, see [Regions, Availability Zones, and Local Zones](Concepts.RegionsAndAvailabilityZones.md).