

# Optimizing query performance using column statistics
<a name="column-statistics"></a>

You can compute column-level statistics for AWS Glue Data Catalog tables in data formats such as Parquet, ORC, JSON, ION, CSV, and XML without setting up additional data pipelines. Column statistics help you to understand data profiles by getting insights about values within a column. 

Data Catalog supports generating statistics for column values such as minimum value, maximum value, total null values, total distinct values, average length of values, and total occurrences of true values. AWS analytical services such as Amazon Redshift and Amazon Athena can use these column statistics to generate query execution plans, and choose the optimal plan that improves query performance.

There are three scenarios for generating column statistics: 

 **Auto**   
AWS Glue supports automatic column statistics generation at the catalog-level so that it can automatically generate statistics for new tables in the AWS Glue Data Catalog. 

**Scheduled**  
AWS Glue supports scheduling column statistics generation so that it can be run automatically on a recurring schedule.   
With scheduled statistics computation, the column statistics task updates the overall table-level statistics, such as min, max, and avg with the new statistics, providing query engines with accurate and up-to-date statistics to optimize query execution. 

**On-demand**  
Use this option to generate column statistics on-demand whenever needed. This is useful for ad-hoc analysis or when statistics need to be computed immediately. 

You can configure to run column statistics generation task using AWS Glue console, AWS CLI, and AWS Glue API operations. When you initiate the process, AWS Glue starts a Spark job in the background and updates the AWS Glue table metadata in the Data Catalog. You can view column statistics using AWS Glue console or AWS CLI or by calling the [GetColumnStatisticsForTable](https://docs.aws.amazon.com/glue/latest/webapi/API_GetColumnStatisticsForTable.html) API operation.

**Note**  
If you're using Lake Formation permissions to control access to the table, the role assumed by the column statistics task requires full table access to generate statistics.

**Note**  
Column statistics do not support Iceberg v3 data types, including VARIANT, UNKNOWN, Geography, and Geometry. Columns with these data types are skipped during statistics generation.

 The following video demonstrates how to enhance query performance using column statistics. 

[![AWS Videos](http://img.youtube.com/vi/zUHEXJdHUxs?si=HjyhpoALR6RXJz2i/0.jpg)](http://www.youtube.com/watch?v=zUHEXJdHUxs?si=HjyhpoALR6RXJz2i)


**Topics**
+ [Prerequisites for generating column statistics](column-stats-prereqs.md)
+ [Automatic column statistics generation](auto-column-stats-generation.md)
+ [Generating column statistics on a schedule](generate-column-stats.md)
+ [Generating column statistics on demand](column-stats-on-demand.md)
+ [Viewing column statistics](view-column-stats.md)
+ [Viewing column statistics task runs](view-stats-run.md)
+ [Stopping column statistics task run](stop-stats-run.md)
+ [Deleting column statistics](delete-column-stats.md)
+ [Considerations and limitations](column-stats-notes.md)