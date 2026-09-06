

# 10 – Choose the best-performing file format and partitioning
<a name="design-principle-10"></a>

 **How do you select the best-performing file formats and partitioning?** Selecting the best-performing file format and data partitioning for data-at-rest can have a large impact on the overall analytics workload efficiency. 


|  **ID**  |  **Priority**  |  **Best practice**  | 
| --- | --- | --- | 
| ☐ BP 10.1  |  Recommended  |  Select format based on data write frequency and patterns for append-only compared to in-place update.  | 
| ☐ BP 10.2  |  Recommended  |  Choose data formatting based on your data access pattern  | 
| ☐ BP 10.3  |  Recommended  |  Utilize compression techniques to both decrease storage requirements and enhance I/O efficiency.  | 
| ☐ BP 10.4  |  Recommended  |  Partition your data to enable efficient data pruning and reduce unnecessary file reads.  | 

 For more details, refer to the following information: 
+  Amazon Redshift Database Developer Guide: [Creating data files for queries in Amazon Redshift](https://docs.aws.amazon.com/redshift/latest/dg/c-spectrum-data-files.html) [Spectrum](https://docs.aws.amazon.com/redshift/latest/dg/c-spectrum-data-files.html) 
+  Amazon EMR Release Guide: [Hudi](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-hudi.html) 
+  AWS Big Data Blog: [Apply record level changes from relational databases to Amazon S3 data lake](https://aws.amazon.com/blogs/big-data/apply-record-level-changes-from-relational-databases-to-amazon-s3-data-lake-using-apache-hudi-on-amazon-emr-and-aws-database-migration-service/) [using Apache Hudi on Amazon EMR and AWS Database Migration service](https://aws.amazon.com/blogs/big-data/apply-record-level-changes-from-relational-databases-to-amazon-s3-data-lake-using-apache-hudi-on-amazon-emr-and-aws-database-migration-service/) 