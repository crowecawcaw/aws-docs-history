# Using Data Catalog tables for the data

source

For all data sources except Amazon S3 and connectors, a table must exist in the
AWS Glue Data Catalog for the source type that you choose. AWS Glue does not create the Data Catalog
table.

###### To configure a data source node based on a Data Catalog table

1. Go to the visual editor for a new or saved job.
2. Choose a data source node in the job diagram.
3. Choose the **Data source properties** tab, and then enter the following
   information:
   - **S3 source type**: (For Amazon S3 data sources only)
     Choose the option **Select a Catalog table** to use an existing
     AWS Glue Data Catalog table.
   - **Database**: Choose the database in the Data Catalog that contains
     the source table you want to use for this job. You can use the search field to
     search for a database by its name.
   - **Table**: Choose the table associated with the source data
     from the list. This table must already exist in theAWS Glue Data Catalog. You can use the
     search field to search for a table by its name.
   - **Partition predicate**: (For Amazon S3 data sources
     only) Enter a Boolean expression based on Spark SQL that includes only the
     partitioning columns. For example: `"(year=='2020' and
month=='04')"`
   - **Temporary directory**: (For Amazon Redshift data sources only) Enter a
     path for the location of a working directory in Amazon S3 where your ETL job
     can write temporary intermediate results.
   - **Role associated with the cluster**: (For Amazon Redshift data sources
     only) Enter a role for your ETL job to use that contains permissions for
     Amazon Redshift clusters. For more information, see [Data source and data target
     permissions](getting-started-min-privs-job.md#getting-started-min-privs-data "getting-started-min-privs-job.md#getting-started-min-privs-data").
