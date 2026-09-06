

# Best practice 15.4 – Implement data retention processes to remove unnecessary data from your analytics environment
<a name="best-practice-15.4-implement-data-retention-processes-to-remove-redundant-data-from-your-analytics-environment."></a>

 The retention of data should be informed, relevant, and limited to what is necessary for the purposes for which the data is processed. Storing data indefinitely and without purpose can cause significant storage and processing overhead that can impact your organization’s analytics environmental impact. Ensure that the period for which the data should be stored is limited and reviewed on a regular basis. 

 **How can you remove unnecessary data from an object store?** 

## Suggestion 15.4.1 – Deﬁne and implement a data lifecycle process for data at rest
<a name="suggestion-15.4.1-define-and-implement-a-data-lifecycle-process-for-data-at-rest-data-lake."></a>

 Implement a lifecycle management process that will either remove data that is no longer required, or archive data into less resource-intensive storage. 

 When removing data from an object store, your organization should consider the following design points:
+  The data retention removal process should run on a regular basis 
+  The data retention removal process should remove data from all buckets, sub-directories and prefixes. 
+  The data retention removal process should take an audit of what data has been removed, when it was removed, and who performed the removal process. This audit data should be tracked in an immutable audit log for auditing purposes. 
+  Production, user acceptance test (UAT), and development (DEV) environments must be included and adhere to the agreed retention policy across all environments. 
+  Consider other locations where data might be stored, such as SFTP locations. 
+  Classify your organization’s data by data temperature, such as *hot* for frequently accessed, and *cold* for infrequently accessed. After data has been classified by temperature, your organization should implement a strategy to move data into the respective S3 bucket storage classes. For example, cold data could be moved to Amazon Glacier storage class. For an illustration of data temperatures, see [Optimizing your AWS Infrastructure for Sustainability, Part II: Storage](https://aws.amazon.com/blogs/architecture/optimizing-your-aws-infrastructure-for-sustainability-part-ii-storage/). 

 For more details, refer to the following information: 
+  Amazon S3 Lifecycle Management: [Managing your storage lifecycle](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lifecycle-mgmt.html) 

 

 **How can you remove unnecessary data from databases?** 

## Suggestion 15.4.2 – Remove unnecessary data from databases
<a name="suggestion-15.4.2-remove-unnecessary-data-from-a-database."></a>

 To effectively remove information from a database, your organization should track when the data was loaded into the database and when the last customer interaction occurred, such as a purchase or other activity. This tracking helps you accurately identify when data should be removed. 
+  The data retention removal process should run frequently, but should not be run excessively, as excessive deletion can increase compute resources that could mitigate the benefit of removing the data from your database. 
+  The data retention removal process should remove data from all databases and tables. 
+  The data retention removal process should retain an audit of what data has been removed, when it was removed, and who performed the removal process. This audit data should be tracked in an immutable audit log for auditing purposes. 
+  If your database enforces referral integrity, you should redact only the data and retain the primary and foreign keys. 

 For more details, refer to the following information: 
+  Amazon Redshift: [Amazon Redshift Stored Procedures](https://docs.amazonaws.cn/en_us/redshift/latest/dg/stored-procedure-create.html) 
+  Amazon Redshift: [DELETE Statement](https://docs.aws.amazon.com/redshift/latest/dg/r_DELETE.html) 
+  Amazon Redshift: [Scheduling a query on the Amazon Redshift console](https://docs.aws.amazon.com/redshift/latest/mgmt/query-editor-schedule-query.html) 

## Suggestion 15.4.3 – Use the shortest possible retention period in streaming applications
<a name="suggestion-15.4.3-develop-a-process-to-remove-data-from-your-streaming-application-when-no-longer-required."></a>

 The primary use-case of a streaming application is to transfer information from source to target, but they can also retain data for a configured time. This allows replaying the stream to, for example, recover from corruption in a downstream system. At the same time, data stored in a streaming application becomes redundant as soon as it has been stored downstream. Determine the shortest possible retention period that you need to meet your Recovery Point Objective (RPO). 

 For more details, refer to the following information: 
+  Amazon Kinesis: [Changing the Data Retention Period](https://docs.aws.amazon.com/streams/latest/dev/kinesis-extended-retention.html) 
+  Amazon Managed Streaming for Apache Kafka: [Adjust data retention parameters](https://docs.aws.amazon.com/msk/latest/developerguide/bestpractices.html) 

 

## Suggestion 15.4.4 – Design your application to make it possible to efficiently remove or archive outdated data
<a name="suggestion-15.4.4"></a>

 Designing a data model that supports efficient deletion of data can be surprisingly hard. In the worst case, the deletion of a single piece of data may require rewriting a large portion of the data set in a data lake. This is inefficient and has an unnecessary environmental impact. When designing an application, also design how you remove or archive data from it once that data is outdated, no longer relevant, or upon request. 

 Consider, and design for things like: 
+  How to delete all data belonging to a specific user 
+  How to delete data older than a specific time 
+  How to delete personal data 

 In data lakes and analytics applications it is often hard to delete individual pieces of data. Consider how to organize data to reduce the amount of data that has to be rewritten to delete a single piece of data – but always balance it against the impact to query performance. 

 It is often good practice to partition a data set in a data lake by time to make it possible to efficiently delete historical data when it is no longer needed. Similarly, in a data warehouse, keeping data sorted by time yields similar efficiencies. 

 For more details see: 
+ [ Optimize your modern data architecture for sustainability: Part 1 – data ingestion and data lake ](https://aws.amazon.com/blogs/architecture/optimize-your-modern-data-architecture-for-sustainability-part-1-data-ingestion-and-data-lake/)
+ [AWS Well-Architected Framework: SUS04-BP05 Remove unneeded or redundant data ](https://docs.aws.amazon.com/wellarchitected/latest/sustainability-pillar/sus_sus_data_a6.html)