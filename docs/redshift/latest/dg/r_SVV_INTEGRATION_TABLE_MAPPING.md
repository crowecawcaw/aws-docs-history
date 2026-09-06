

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# SVV\_INTEGRATION\_TABLE\_MAPPING
<a name="r_SVV_INTEGRATION_TABLE_MAPPING"></a>

SVV\_INTEGRATION\_TABLE\_MAPPING displays the mapping of source database, schema, table, column, and data type to the target when the identifier value of those fields are different.

**Note**  
This view is only populated for the following types of zero-ETL integrations:  
AWS Glue third-party applications to Amazon SageMaker Lakehouse
Amazon DynamoDB to Amazon SageMaker Lakehouse
For more information, see [Zero-ETL integrations](https://docs.aws.amazon.com/glue/latest/dg/zero-etl-using.html) in the *AWS Glue Developer Guide*.

The transformation of identifier values from source to target follow the following rules:
+ An upper case letter is converted to lower case.
+ A character that is not a lowercase letter, a digit, or underscore (\_) is converted to an underscore (\_).
+ If there is a conflict with a existing identifier value, then an Universally Unique Identifier (UUID) is appended to the new identifier.
+ If the source identifier value is an Amazon Redshift keyword, then the suffix `_redshift` is appended to the new identifier.

After transformation, a character must be a lowercase letter, a digit, or underscore (\_) and match the regex pattern `[a-z0-9_]`. The following examples demonstrate the conversion rules:


| Source | Target | Notes | 
| --- | --- | --- | 
| foo | foo | No transformation | 
| Bar | bar |  | 
| fooBar | foobar |  | 
| foo1 | foo1 | No transformation | 
| foo\_1 | foo\_1 | No transformation | 
| Bar@1 | bar\_1 |  | 
| foo\_bar@ | foo\_bar\_ |  | 
| case | case\_redshift |  | 

SVV\_INTEGRATION\_TABLE\_MAPPING is visible to all users. Superusers can see all rows; regular users can see only their own data. For more information, see [Visibility of data in system tables and views](cm_chap_system-tables.md#c_visibility-of-data).

For information about zero-ETL integrations, see [Zero-ETL integrations](https://docs.aws.amazon.com/redshift/latest/mgmt/zero-etl-using.html) in the *Amazon Redshift Management Guide*.

## Table columns
<a name="r_SVV_INTEGRATION_TABLE_MAPPING-table-columns"></a>


| Column name  | Data type  | Description  | 
| --- | --- | --- | 
| integration\_id | character(128) | The identifier associated with the integration. | 
| source\_database | character(128) | The name of the database in the source. | 
| target\_database | character(128) | The database in Amazon Redshift that receives the integration data. | 
| source\_schema\_name | character(128) | The name of the schema in the source. | 
| target\_schema\_name | character(128) | The schema in Amazon Redshift that receives the integration data. | 
| source\_table\_name | character(128) | The name of the table in the source. | 
| target\_table\_name | character(128) | The table in Amazon Redshift that receives the integration data. | 
| source\_column\_name | character(128) | The name of the column in the source. | 
| target\_column\_name | character(128) | The column in Amazon Redshift that receives the integration data. | 
| source\_data\_type | character(128) | The data type of the column in the source. | 
| target\_data\_type | character(128) | The data type of the column in Amazon Redshift that receives the integration data. | 

## Sample queries
<a name="r_SVV_INTEGRATION_TABLE_MAPPING-sample-queries"></a>

The following SQL command displays mapping of metadata values from source to target.

```
select * from svv_integration_table_mapping;

           integration_id              | source_database | target_database |  source_schema_name | target_schema_name | source_table_name | target_table_name | 
---------------------------------------+-----------------+-----------------+---------------------+--------------------+---------------------------------------+
  99108e72-1cfd-414f-8cc0-0216acefac77 |     mydatabase  |  mydatabase     |  myschema           | myschema           | Mytable           | mytable           | 
  
  
                                       | source_column_name | target_column_name |  source_data_type | target_data_type | 
                                       +--------------------+--------------------+-------------------+------------------+
                                       | Mycolumnname       | mycolumnname       |  Mydatatype       | mydatatype       |
```