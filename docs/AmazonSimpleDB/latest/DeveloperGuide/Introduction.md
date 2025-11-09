# Introduction to Amazon SimpleDB

###### Topics

- [Features](#Features "#Features")
- [How Amazon Charges for Amazon SimpleDB](#HowAmazonChargesForSDB "#HowAmazonChargesForSDB")
- [Viewing Your Bill](#ViewingYourBill "#ViewingYourBill")
  This introduction to Amazon SimpleDB is intended to give you a detailed summary of this web service.
  After reading this section, you should have a good idea of what it offers and how it can fit
  in with your business.

Traditionally, the type of functionality provided by Amazon SimpleDB has been accomplished with a
clustered relational database that requires a sizable upfront investment, brings more
complexity than is typically needed, and often requires a DBA to maintain and administer. In
contrast, Amazon SimpleDB is easy to use and provides the core functionality of a database - real-time
lookup and simple querying of structured data - without the operational complexity. Amazon SimpleDB
requires no schema, automatically indexes your data and provides a simple API for storage
and access. This eliminates the administrative burden of data modeling, index maintenance,
and performance tuning. Developers gain access to this functionality within Amazon's proven
computing environment, are able to scale instantly, and pay only for what they use.

## Features

Following are some of the major Amazon SimpleDB attributes:

###### Features

- Simple to use—Amazon SimpleDB provides streamlined
  access to the lookup and query functions that traditionally are achieved using a
  relational database cluster while leaving out other complex, often-unused
  database operations.

The service allows you to quickly add data and easily retrieve or edit that
data through a simple set of API calls. Accessing these capabilities through a
web service also eliminates the complexity of maintaining and scaling these
operations

- Flexible—With Amazon SimpleDB, it is not necessary
  to pre-define all of the data formats you will need to store; simply add new
  attributes to your Amazon SimpleDB data set when needed, and the system will automatically
  index your data accordingly.

The ability to store structured data without first defining a schema provides
developers with greater flexibility when building applications.

- Scalable—Amazon SimpleDB allows you to easily scale
  your application. You can quickly create new domains as your data grows or your
  request throughput increases.

Currently, you can store up to 10 GB per domain and you can create up to 250
domains.

- Fast—Amazon SimpleDB provides quick, efficient
  storage and retrieval of your data to support high performance web
  applications.
- Reliable—The service runs within Amazon's
  high-availability data centers to provide strong and consistent performance.

To prevent data from being lost or becoming unavailable, your fully indexed
data is stored redundantly across multiple servers and data centers.

- Designed for use with other Amazon Web
  Services—Amazon SimpleDB is designed to integrate easily with other
  web-scale services such as Amazon EC2 and Amazon S3.

For example, developers can run their applications in Amazon EC2 and store
their data objects in Amazon S3. Amazon SimpleDB can then be used to query the object
metadata from within the application in Amazon EC2 and return pointers to the
objects stored in Amazon S3.

- Inexpensive—Amazon SimpleDB passes on to you the
  financial benefits of Amazon's scale. You pay only for resources you actually
  consume.

Compare this with the significant up-front expenditures traditionally required
to obtain software licenses and purchase and maintain hardware, either in-house
or hosted. This frees you from many of the complexities of capacity planning,
transforms large capital expenditures into much smaller operating costs, and
eliminates the need to over-buy "safety net" capacity to handle periodic traffic
spikes.

## How Amazon Charges for Amazon SimpleDB

Amazon SimpleDB pricing is based on your actual usage. Your usage is measured and rounded up to
the nearest cent.

Amazon SimpleDB charges you for the following types of usage:

- Structured Data Storage—Measures the size
  of your billable data by adding the raw byte size of the data you upload + 45
  bytes of overhead for each item, attribute name and attribute-value pair.
- Data Transfer—Measures the amount of data
  transferred for every operation.

Data transferred between Amazon SimpleDB and other Amazon Web Services (e.g., Amazon S3,
Amazon EC2, Amazon SQS, and others) is free of charge.

- Machine Utilization—Measures the
  _machine utilization_ of each request and charges based
  on the amount of machine capacity used to complete the particular request
  (SELECT, GET, PUT, etc.).

###### Note

Amazon Web Services provides a free tier of Amazon SimpleDB usage. The free tier is a
monthly offer. Free usage does not accumulate.

Any data stored as part of the free tier program must be actively used. If a
domain is not accessed for a period of 6 months, it will be subject to removal at
the discretion of Amazon Web Services.

### Storage

You are charged for the amount of storage your data uses each month which can be
considered an average of the month. For example, if you use one gigabyte for the
month, you are charged for one gigabyte of storage. If you use zero gigabytes for
the first half of the month and two gigabytes for the second half, you are also
charged for one gigabyte of storage.

Several times each day, Amazon SimpleDB measures the amount of storage used by all of the
objects in your account. Amazon SimpleDB stores this information in byte-hours and averages it
with all other recorded measurements at the end of the billing cycle.

### Data Transfer

Amazon charges you for the amount of data transferred into and out of Amazon SimpleDB. For
every operation, Amazon SimpleDB monitors the amount of data sent and received and records the
data. Once per hour, the usage total is recorded to your account. This information
is stored and totaled at the end of the billing cycle.

### Machine Utilization

For each successful request, Amazon SimpleDB charges you for the amount of machine capacity used to
complete that request.

You are also charged for any request that fails with an HTTP 4xx error. For example, if
Amazon SimpleDB cannot authorize a request, you will receive an HTTP 403 error (Forbidden) and
incur a machine utilization charge for the failed request.

## Viewing Your Bill

You can view the charges for your current billing period at any time by going to the
[AWS Portal](http://aws.amazon.com "http://aws.amazon.com").

###### To view your activity

1. Log in to your AWS account.
2. Move the pointer over **Your Web Services Account**.
3. Click **Account Activity**.

A list of services to which you subscribe appears. 4. Locate the Amazon SimpleDB service.

| Billing Component        | Description                                                                                                |
| ------------------------ | ---------------------------------------------------------------------------------------------------------- |
| View/Edit Service Button | Enables you to view or change settings associated with the Amazon SimpleDB<br>service.                     |
| Machine Hour Usage       | Shows the machine hour usage cost, current number of hours consumed,<br>and billing for the current cycle. |
| Data Transferred         | Shows the data transfer cost, current amount of data transferred, and<br>billing for the current cycle.    |
| Storage                  | Shows the storage usage cost, average amount of storage consumed, and<br>billing for the current cycle.    |
| Usage Report             | Shows detailed data used to calculate your bill.                                                           |
