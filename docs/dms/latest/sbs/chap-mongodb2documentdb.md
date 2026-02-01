# Migrating from MongoDB to Amazon DocumentDB

Use the following tutorial to guide you through the process of migrating from MongoDB to Amazon DocumentDB (with MongoDB compatibility). In this tutorial, you do the following:

- Install MongoDB on an Amazon EC2 instance.
- Populate MongoDB with sample data.
- Create an AWS DMS replication instance, a source endpoint (for MongoDB), and a target endpoint (for Amazon DocumentDB).
- Run an AWS DMS task to migrate the data from the source endpoint to the target endpoint.

###### Important

Before you begin, make sure to launch an Amazon DocumentDB cluster in your default virtual private cloud (VPC). For more information, see [Getting started](../../../documentdb/latest/developerguide/getting-started.md "../../../documentdb/latest/developerguide/getting-started.md") in the _Amazon DocumentDB Developer Guide._

To estimate what it will cost to run this walkthrough on AWS, you can use the AWS Pricing Calculator. For more information, see [https://calculator.aws/](https://calculator.aws/ "https://calculator.aws/").

###### Topics

- [Launch an Amazon EC2 instance for MongoDB migration](chap-mongodb2documentdb.md "chap-mongodb2documentdb.md")
- [Install and configure MongoDB community edition](chap-mongodb2documentdb.md "chap-mongodb2documentdb.md")
- [Create an AWS DMS replication instance for MongoDB migration](chap-mongodb2documentdb.md "chap-mongodb2documentdb.md")
- [Create source and target endpoints for MongoDB migration](chap-mongodb2documentdb.md "chap-mongodb2documentdb.md")
- [Create and run a MongoDB migration task](chap-mongodb2documentdb.md "chap-mongodb2documentdb.md")
