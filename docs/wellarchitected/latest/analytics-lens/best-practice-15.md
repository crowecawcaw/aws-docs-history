# Best practice 15.3 – Encourage a culture of data minimization

Analytics relies heavily on large volumes of data being stored and processed. Minimizing the amount of data stored and processed can have a positive impact on the environmental impact of your organization’s analytics platform. Encourage architects, data engineers, and other roles that work on the platform to think about ways to minimize the amount of data stored and processed at every point in the system. A just enough data mindset can reduce the overall amount of data processed and therefore reduce the amount of compute power and storage used, and lower the environmental impact.

Look for opportunities to break linear relationships so that datasets don’t need to grow at the same pace as your business. As your user base increases, find ways to avoid datasets growing at the same pace. In many cases it may be unavoidable, but for example, if you store partially aggregated data you can break the linear relationship.

Encouraging a culture of always thinking about ways to minimize data can help ensure your organization does not unintentionally increase its environmental impact again after reductions have been made.
More information on building and implementing an Improvement
process can be found in the
[Sustainability
Pillar whitepaper](../sustainability-pillar/improvement-process.md "../sustainability-pillar/improvement-process.md").

**How do you minimize the amount of
data that is processed?**

## Suggestion 15.3.1– Minimize the amount of data extracted from your source systems that gets stored in your data warehouse

Data warehousing plays an important role in providing meaningful insights to your reporting layers and analytics. Data warehousing is the ingestion and merging of multiple data sources to create a single data model optimized for the business’ needs. Typically it employs techniques such as denormalization and materialized views of aggregates to provide faster query response times. It is encouraged that your organization applies these principles of building a data warehouse.

It is common that all source data is ingested into a data warehouse. Since data warehouses are good at storing massive amounts of data, and because it’s hard to know in advance what is going to be needed, many organizations store everything. This leads to higher environmental impact because of the added compute and storage requirements.

Work backwards from the business needs, reports, and dashboards when designing ingestion processes and data models for data warehouses. This avoids the overhead of extracting, processing, and storing source data that is not strictly needed.

For more details, refer to the following information:

- [Amazon Redshift development guide: Database Developer Guide](https://docs.amazonaws.cn/en_us/redshift/latest/dg/redshift-dg.pdf "https://docs.amazonaws.cn/en_us/redshift/latest/dg/redshift-dg.pdf")
- [Optimize your modern data architecture for sustainability: Part 1 – data ingestion and data lake](https://aws.amazon.com/blogs/architecture/optimize-your-modern-data-architecture-for-sustainability-part-1-data-ingestion-and-data-lake/ "https://aws.amazon.com/blogs/architecture/optimize-your-modern-data-architecture-for-sustainability-part-1-data-ingestion-and-data-lake/")

When designing your source data extraction processes, it is recommended that your organization should only extract data required for the workloads, such as reports and dashboards, that the data warehouse supports. This results in less data being transferred over the network, less data processed, less data being loaded into the data warehouse, less data being stored over time, and less data to remove when applying data retention policies.

When extracting data from your source datastore, your organization should use a date range to extract only data that has been added or updated in the source datastore since the last data extract. This is called delta updates. This approach reduces the environmental impact of reprocessing the same data multiple times.

Designing and building an efficient data model requires
upfront consideration. Your development team should ensure
that the optimal row-level granularity (for example
customer level, address level, or product level) and data
attributes reduces unnecessary deduplication and
filtering further downstream.

Most reporting applications support data editing and data
filtering capabilities. Therefore, your development teams
can develop a subset of data within the business tool
minimizing the amount of data required for a report
refresh.

For more details, refer to the following information:

- [Quick Suite: Creating
  datasets](../../../quicksight/latest/user/creating-data-sets.md "../../../quicksight/latest/user/creating-data-sets.md")

## Suggestion 15.3.2 – Use appropriate data types when developing database tables

Databases and data warehouses can store many different types of data, and have optimized storage mechanisms for each type. Choosing the appropriate type for columns can optimize both the storage size of a dataset and the compute resources needed to process it. For example, storing numbers as integers, floats, and so on, instead of strings can save a lot of storage space, and greatly reduce the processing required when performing calculations. Similarly, dates and timestamps should be stored using matching data types. Consider each column and assign the most specific data type possible.

For more details, refer to the following information:

- [Amazon Redshift best practices for designing tables](../../../redshift/latest/dg/c_designing-tables-best-practices.md "../../../redshift/latest/dg/c_designing-tables-best-practices.md")
- [Data
  types in Amazon Athena](../../../athena/latest/ug/data-types.md "../../../athena/latest/ug/data-types.md")
- [Amazon Redshift data types](../../../redshift/latest/dg/c_Supported_data_types.md "../../../redshift/latest/dg/c_Supported_data_types.md")
- [Quick Suite: Supported
  data types and values](../../../quicksight/latest/user/supported-data-types-and-values.md "../../../quicksight/latest/user/supported-data-types-and-values.md")

## Suggestion 15.3.3 – Review your APIs to understand whether all data must be shared with your streaming applications

APIs play an important role in connecting and sharing data between
applications, databases and other systems. Application developers should consider the size
of an event payload submitted to these systems.

Organizations require the ability to run analytics on
real-time data. To do so, organizations send data to
streaming services. Streaming services, such as Amazon Managed Streaming for Apache Kafka (Amazon MSK) and Amazon Kinesis, allow organizations to run analytics on real-time
streams of information. It is important that the data
being shared with such streaming services is reviewed
through the improvement process, because the more data
provided in the payload will require more resources to
store and process the data. Reducing the network, storage,
and compute resources required to process unnecessary data
can help towards reducing your organization’s analytics
environmental impact.

Review data that is captured by the application and pushed
to the streaming platform to identify data attributes that
can be removed. Also identify opportunities to store
commonly used transforms to create values that can be
computed once. Review your Kafka topic and identify if
it’s duplicated data of whether a single topic is enough
to deliver to multiple dependencies. Through the
Improvement process you should consider data volumes and
the value of your assets, and measure these against your
organization’s proxy metrics.

If it is not possible to reduce data at the point of data
capture, as a developer, you can use AWS Lambda to trim
event payloads of data attributes that are not required
for downstream processing. However, as an organization,
you should balance the trade-off of compute cost of
removing the data versus retaining the original data
values. This is not a binary option but should be measured
over time to determine if it would be worthwhile removing
data.

For more details, refer to the following information:

- AWS Lambda:
  [Using
  AWS Lambda with Amazon Kinesis](../../../lambda/latest/dg/with-kinesis-example.md "../../../lambda/latest/dg/with-kinesis-example.md")

Implement a monitor and alert strategy to get a clear
picture of data growth over time. Take action on any
significant data growth by understanding what additional
attributes have been added to the event payload. Alerts
should be implemented on thresholds, such as 3x data
growth, or create an internal metric that your
organization should expect to increase the overall data
footprint aligned with new customers.

For more details, refer to the following information:

- Amazon Kinesis:
  [Monitoring
  the Amazon Kinesis Data Streams Service with Amazon CloudWatch](../../../streams/latest/dev/monitoring-with-cloudwatch.md "../../../streams/latest/dev/monitoring-with-cloudwatch.md")

## Suggestion 15.3.4 – Reduce the amount of data migrated from one environment to another

Migrating data from one environment to another is a common exercise. Your
organization should consider data minimization when migrating from one environment to
another as migration requires additional network, storage, and compute resources for
migrating unwanted information. Your organization should regularly review all
information that is in scope of the migration and determine whether it is necessary
for future workloads, rather than defaulting to a _migrate all_
approach.

If your organization maintains a data catalog, a review of the data assets by a
data owner prior to migrating the data should be performed to understand
whether the data is required by the business.

For more details, refer to the following information:

- AWS Data Migration: [Top 10 Data Migration](https://pages.awscloud.com/rs/112-TZM-766/images/2020_0124-STG_Slide-Deck.pdf "https://pages.awscloud.com/rs/112-TZM-766/images/2020_0124-STG_Slide-Deck.pdf")
- AWS Data Migration (video):
  [Top 10 Data
  Migration Best Practices](https://www.youtube.com/watch?v=i0-pSHQJ7pA "https://www.youtube.com/watch?v=i0-pSHQJ7pA")

## Suggestion 15.3.5 – Apply the optimal data model for your data access patterns

Understanding your data access patterns helps you determine which data modeling technique is most suitable. Work backwards from the way you access the data to determine the most suitable data model. There are two broad approaches to data modelling that you can start to consider: normalization and denormalization.

*Normalization* is the method of arranging the data in a data model
to reduce redundant data and improve query efficiency. This method involves designing the tables and setting up relationships between those tables according to certain rules. Each piece of data is only stored once, and is referenced using its ID. Joins are used to reassemble the full data model. Typically, normalized data models are used in online transaction processing (OLTP) and are supported by relational databases that store the database data in rows. Normalized models minimize the amount of data stored, and compute power needed to make updates.

_Denormalization_ is almost the opposite of normalization. Instead of referencing data using IDs, data is copied as many times as needed. Denormalized data models are typically used in online analytical processing (OLAP) where the data is stored in column-oriented massively parallel processing (MPP) databases such as Amazon Redshift. OLAP is designed for multidimensional analysis of data in a data warehouse, which contains both transactional and historical data. In MPP architectures data locality is important, and keeping redundant copies of data and avoiding joins can reduce the compute power needed, as well as network overhead. On the flip side, they may take up more storage, and updates require more compute power.

Whether you should choose normalization or denormalization for your data model depends on your data access patterns. Consider the way you query and update the data set first. In analytics, denormalized data models often perform better. The extra storage requirements from data duplication is often balanced by compression. When storing data in columns instead of rows, data encoding and compression becomes more efficient.

To normalize or denormalize is not an either-or proposition, but a scale. You can denormalize some parts of your data model heavily, while keeping other parts more normalized. For example, if you store personal data and have to be able to update and delete it easily, normalization of that part of the model may lead to the least environmental impact overall. Each query may become slightly less efficient, but you ensure you don’t have to rewrite the whole data set to remove multiple copies of a data point.

For more details, refer to the following information:

- Modern data architecture:
  [Build a modern data architecture on AWS with Amazon AppFlow, AWS Lake Formation, and Amazon Redshift](https://aws.amazon.com/blogs/big-data/build-a-modern-data-architecture-on-aws-with-amazon-appflow-aws-lake-formation-and-amazon-redshift/ "https://aws.amazon.com/blogs/big-data/build-a-modern-data-architecture-on-aws-with-amazon-appflow-aws-lake-formation-and-amazon-redshift/")
