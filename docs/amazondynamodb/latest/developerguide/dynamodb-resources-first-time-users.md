# Amazon DynamoDB resources for first-time users

We recommend that first time users begin by reading the following sections, and refer to them as needed.

- **Service highlights and pricing** – The [product detail page](https://aws.amazon.com/dynamodb/ "https://aws.amazon.com/dynamodb/") provides a general product
  overview of DynamoDB, common use cases, service highlights, and pricing.
- **DynamoDB resources** – The [DynamoDB resources](https://aws.amazon.com/dynamodb/resources/ "https://aws.amazon.com/dynamodb/resources/") section has videos,
  tutorials, and prescriptive guidance that introduces you to the service, concepts of data
  modeling, and core features and capabilities.
- **Getting started** – The [Getting started with DynamoDB](GettingStartedDynamoDB.md "GettingStartedDynamoDB.md") section includes information on setting up DynamoDB, creating
  sample tables, and uploading data. It also provides information about performing basic database
  operations using the AWS Management Console, AWS CLI, NoSQL Workbench, and DynamoDB APIs.
- **DynamoDB basics course** – A [free digital course](https://explore.skillbuilder.aws/learn/course/external/view/elearning/16104/amazon-dynamodb-basics "https://explore.skillbuilder.aws/learn/course/external/view/elearning/16104/amazon-dynamodb-basics") that teaches the fundamentals of DynamoDB, including table design,
  data types, and basic operations. This course is ideal for developers new to DynamoDB and NoSQL
  databases.
- **DynamoDB Nuggets** –A collection of short, focused [video
  tutorials](https://www.youtube.com/playlist?list=PLhr1KZpdzukemNOO71Hca0GpjG0QmXwEd "https://www.youtube.com/playlist?list=PLhr1KZpdzukemNOO71Hca0GpjG0QmXwEd") that explain key DynamoDB concepts and features. These bite-sized videos cover
  topics like data modeling, partitioning strategies, access patterns, and best practices in an
  easy-to-understand format.
- [**DynamoDB code samples repository**](https://github.com/aws-samples/aws-dynamodb-examples "https://github.com/aws-samples/aws-dynamodb-examples") – Provides practical DynamoDB code
  examples in various programming languages.
- **Free DynamoDB training** – AWS provides [free
  digital training courses](https://explore.skillbuilder.aws/learn/courses/1525/developing-with-amazon-dynamodb "https://explore.skillbuilder.aws/learn/courses/1525/developing-with-amazon-dynamodb") that cover DynamoDB concepts, features, and best practices. The
  DynamoDB deep-dive course series helps you learn how to design efficient data models, implement
  effective partition keys, and use secondary indexes effectively.
- **NoSQL Workbench for DynamoDB** – [NoSQL Workbench](https://youtu.be/p5va6ZX9_o0 "https://youtu.be/p5va6ZX9_o0") is a unified visual tool that
  provides data modeling, data visualization, and query development features. It helps you design,
  create, query, and manage DynamoDB tables, making it especially valuable for learning DynamoDB's data
  modeling concepts and testing access patterns.
- **DynamoDB Design Patterns** – A [Best practices for designing and architecting with
  DynamoDB](best-practices.md "best-practices.md") and data modeling examples that demonstrate best practices for different use cases. Includes
  practical examples and code samples for implementing effective solutions.
- **Hands-on Tutorials** – Step-by-step tutorials in the
  AWS Management Console that guide you through common DynamoDB tasks, from [creating tables](https://aws.amazon.com/tutorials/create-nosql-table/ "https://aws.amazon.com/tutorials/create-nosql-table/") to
  implementing complex queries.
- **Migrating to DynamoDB** – This [Migrating to DynamoDB from a relational database](migration-guide.md "migration-guide.md") provides an overview of the process, tools, and strategies for
  migrating a database into DynamoDB.
- **AWS Well-Architected Lens for DynamoDB** – The [Using the DynamoDB Well-Architected Lens to optimize your DynamoDB
  workload](bp-wal.md "bp-wal.md") provides architectural best practices for designing and operating reliable,
  secure, efficient, and cost-effective applications using DynamoDB. It includes design principles,
  architectural patterns, and operational guidance aligned with the six pillars of the
  Well-Architected Framework.

## Amazon DynamoDB additional best practices for first-time

users

After you complete the preceding sections, read these sections:

- **[DynamoDB throughput capacity](capacity-mode.md "capacity-mode.md")**

Provides an overview of the two throughput modes available for DynamoDB and considerations in
selecting the appropriate capacity mode for your application. On-demand mode is the default and
recommended throughput option for most DynamoDB workloads.

- **[Best practices for designing and architecting with
  DynamoDB](best-practices.md "best-practices.md")**

Identify and address issues to maximize performance and minimize costs when working with
DynamoDB.

## AWS CLI resources

If you want to use the AWS Command Line Interface (AWS CLI), you can use these documents to help you get started:

- **[AWS CLI
  documentation](../../../cli.md "../../../cli.md")**

This section provides information on downloading the AWS CLI, getting the AWS CLI working on your system, and providing your AWS credentials.

- **[AWS CLI documentation for DynamoDB](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dynamodb/index.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dynamodb/index.html")**

This separate document covers all of the AWS CLI for DynamoDB commands, including syntax and examples.

## Programming resources

You can write application programs to use the DynamoDB API with a variety of popular programming languages. Here are some resources:

- **[Tools for
  Amazon Web Services](https://aws.amazon.com/developer/tools/ "https://aws.amazon.com/developer/tools/")**

AWS provides a number of software development kits (SDKs) with support for DynamoDB. You can code for DynamoDB using Java, .NET, PHP, Ruby, and other languages. These SDKs can greatly simplify your application development by formatting your requests to DynamoDB, parsing responses, and providing retry logic and error handling.

- **[DynamoDB
  API Reference](../APIReference/Welcome.md "../APIReference/Welcome.md")**

If you don't want to use the AWS SDKs, you can interact with DynamoDB directly using the DynamoDB API. This document covers all of the DynamoDB API operations, including syntax and examples. You can find troubleshooting tips and information on creating and authenticating requests and handling responses in this section.
