# Using custom connectors and connections with AWS Glue Studio

AWS Glue provides built-in support for the most commonly used data stores (such as
Amazon Redshift, Amazon Aurora, Microsoft SQL Server, MySQL, MongoDB, and PostgreSQL) using
JDBC connections. AWS Glue also allows you to use custom JDBC drivers in your extract, transform,
and load (ETL) jobs. For data stores that are not natively supported, such as SaaS applications,
you can use connectors.

A _connector_ is an optional code package that assists with accessing
data stores in AWS Glue Studio. You can subscribe to several connectors offered in AWS Marketplace.

When creating ETL jobs, you can use a natively supported data store, a connector from AWS Marketplace,
or your own custom connectors. If you use a connector, you must first create a connection for
the connector. A _connection_ contains the properties that are required to
connect to a particular data store. You use the connection with your data sources and data
targets in the ETL job. Connectors and connections work together to facilitate access to the
data stores.

The following connections are available when creating connections for connectors:

- **Amazon Aurora** – a scalable, high-performance relational database engine with
  built-in security, backup and restore, and in-memory acceleration.
- **Amazon DocumentDB** – a scalable, highly available, and fully managed document
  database service that supports MongoDB and SQL APIs.
- **Amazon Redshift** – a scalable, highly available, and fully managed document
  database service that supports MongoDB and SQL APIs.
- **Azure SQL** – a cloud-based relational database service from Microsoft Azure that
  provides scalable, reliable, and secure data storage and management capabilities.
- **Cosmos DB** – a globally distributed cloud database service from Microsoft Azure that
  provides scalable, high-performance data storage and querying capabilities.
- **Google BigQuery** – a serverless cloud data warehouse for running fast SQL queries
  on large datasets.
- **JDBC** – a relational database management system (RDBMS) that uses a Java API for
  connecting and interacting with data connections.
- **Kafka** – an open-source stream processing platform used for real-time data
  streaming and messaging.
- **MariaDB** – a community-developed fork of MySQL that offers enhanced performance,
  scalability, and features.
- **MongoDB** – a cross-platform document-oriented database that provides high scalability,
  flexibility, and performance.
- **MongoDB Atlas** – a cloud-based database as a service (DBaaS) offering from MongoDB that
  simplifies the management and scaling of MongoDB deployments.
- **Microsoft SQL Server** – a relational database management system (RDBMS) from Microsoft
  that provides robust data storage, analysis, and reporting capabilities.
- **Mixpanel** – an analytics platform that helps businesses analyze how users interact with their websites,
  mobile applications, and other digital products.
- **MySQL** – an open-source relational database management system (RDBMS) that is widely
  used in web applications and is known for its reliability and scalability.
- **Network** – a network data source represents a network-accessible resource or service
  that can be accessed by a data integration platform.
- **OpenSearch** – an OpenSearch data source is an application that OpenSearch can
  connect to and ingest data from.
- **Oracle** – a relational database management system (RDBMS) from Oracle Corporation
  that provides robust data storage, analysis, and reporting capabilities.
- **PostgreSQL** – an open-source relational database management system (RDBMS) that provides
  robust data storage, analysis, and reporting capabilities.
- **Salesforce** – Salesforce provides customer relationship management (CRM) software that help you with sales, customer service, e-commerce, and more. If you're a Salesforce user, you can connect AWS Glue to your Salesforce account. Then, you can use Salesforce as a data source or destination in your ETL jobs. Run these jobs to transfer data between Salesforce and AWS services or other supported applications.
- **SAP HANA** – an in-memory database and analytics platform that provides fast data
  processing, advanced analytics, and real-time data integration.
- **Snowflake** – a cloud-based data warehouse that provides scalable, high-performance data
  storage and analytics services.
- **Teradata** – a relational database management system (RDBMS) that provides high-performance
  data storage, analysis, and reporting capabilities.
- **Vertica** – a columnar-oriented analytical data warehouse designed for big data analytics
  that offers fast query performance, advanced analytics, and scalability.
