# Amazon DynamoDB resources for first-time users

We recommend that first time users begin by reading the following sections, and refer to them as needed.

|                                                                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                                                                                                                                               |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **[Service highlights and pricing](https://aws.amazon.com/dynamodb/ "https://aws.amazon.com/dynamodb/")**Provides a general product overview of DynamoDB, common use cases, service highlights, and pricing.                                                                                | **[DynamoDB resources](https://aws.amazon.com/dynamodb/resources/ "https://aws.amazon.com/dynamodb/resources/")**Videos, tutorials, and prescriptive guidance that introduces you to the service, concepts of data modeling, and core features and capabilities.                                                                                              |
| **[Getting started](GettingStartedDynamoDB.md "GettingStartedDynamoDB.md")**Information on setting up DynamoDB, creating sample tables, and uploading data.                                                                                                                                 | **[DynamoDB basics course](https://explore.skillbuilder.aws/learn/course/external/view/elearning/16104/amazon-dynamodb-basics "https://explore.skillbuilder.aws/learn/course/external/view/elearning/16104/amazon-dynamodb-basics")**Free digital course that teaches the fundamentals of DynamoDB, including table design, data types, and basic operations. |
| **[DynamoDB Nuggets](https://www.youtube.com/playlist?list=PLhr1KZpdzukemNOO71Hca0GpjG0QmXwEd "https://www.youtube.com/playlist?list=PLhr1KZpdzukemNOO71Hca0GpjG0QmXwEd")**Short, focused video tutorials that explain key DynamoDB concepts and features.                                  | **[DynamoDB code samples repository](https://github.com/aws-samples/aws-dynamodb-examples "https://github.com/aws-samples/aws-dynamodb-examples")**Practical DynamoDB code examples in various programming languages.                                                                                                                                         |
| **[Free DynamoDB training](https://skillbuilder.aws/learn/WC3K4Y4S5N/amazon-dynamodb-getting-started/ "https://skillbuilder.aws/learn/WC3K4Y4S5N/amazon-dynamodb-getting-started/")**AWS provides free digital training courses that cover DynamoDB concepts, features, and best practices. | **[NoSQL Workbench for DynamoDB](https://youtu.be/p5va6ZX9_o0 "https://youtu.be/p5va6ZX9_o0")**Unified visual tool that provides data modeling, data visualization, and query development features.                                                                                                                                                           |
| **[DynamoDB Design Patterns](best-practices.md "best-practices.md")**Best practices and data modeling examples for different use cases with practical code samples.                                                                                                                         | **[Hands-on Tutorials](https://aws.amazon.com/tutorials/create-nosql-table/ "https://aws.amazon.com/tutorials/create-nosql-table/")**Step-by-step tutorials in the AWS Management Console that guide you through common DynamoDB tasks.                                                                                                                       |
| **[Migrating to DynamoDB](migration-guide.md "migration-guide.md")**Overview of the process, tools, and strategies for migrating a database into DynamoDB.                                                                                                                                  | **[AWS Well-Architected Lens for DynamoDB](bp-wal.md "bp-wal.md")**Architectural best practices for designing and operating reliable, secure, efficient, and cost-effective applications using DynamoDB.                                                                                                                                                      |

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
