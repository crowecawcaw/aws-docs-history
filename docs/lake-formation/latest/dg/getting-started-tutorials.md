# AWS Lake Formation tutorials

The following tutorials are organized into three tracks and provide step-by-step instructions on how to build a data lake, ingest data, share, and secure data lakes using
AWS Lake Formation:

1. **Build a data lake and ingest data:** Learn to build a data lake and use blueprints to move, store, catalog, clean, and organize your data. You will
   also learn to set up governed tables. A governed table is a new Amazon S3 table type that supports atomic, consistent, isolated, and durable (ACID) transactions.

Before you begin, make sure that you have completed the steps in [Getting started with Lake Formation](getting-started-setup.md "getting-started-setup.md").

    * [Creating a data lake from an AWS CloudTrail source](getting-started-cloudtrail-tutorial.md "getting-started-cloudtrail-tutorial.md")


    Create and load your first data lake by using your own CloudTrail logs as the data source.
    * [Creating a data lake from a JDBC source in Lake Formation](getting-started-tutorial-jdbc.md "getting-started-tutorial-jdbc.md")


    Create a data lake by using one of your JDBC-accessible data stores, such as a relational database, as the data source.

2. **Securing data lakes:** Learn to use tag-based and row-level access controls to effectively secure and manage access to your data lakes.
   - [Setting up permissions for open table storage formats in Lake Formation](otf-tutorial.md "otf-tutorial.md")

   This tutorial demonstrates how to set up permissions for open source transactional table formats (Apache Iceberg, Apache Hudi, and Linux Foundation Delta Lake tables) in Lake Formation.
   - [Managing a data lake using Lake Formation tag-based
     access control](managing-dl-tutorial.md "managing-dl-tutorial.md")

   Learn to manage access to the data within a data lake using tag-based access control in Lake Formation.
   - [Securing data lakes with row-level access control](cbac-tutorial.md "cbac-tutorial.md")

   Learn to set up row-level permissions that allow you to restrict access to specific rows based on data compliance and governance policies in Lake Formation.

3. **Sharing data:** Learn to securely share your data across
   AWS accounts using tag-based access control (TBAC) and manage granular permissions on datasets shared between AWS accounts.
   - [Sharing a data lake using Lake Formation tag-based
     access control and named resources](share-dl-tbac-tutorial.md "share-dl-tbac-tutorial.md")

   In this tutorial, you learn how to securely share your data across AWS accounts
   using Lake Formation.
   - [Sharing a data lake using Lake Formation fine-grained access control](share-dl-fgac-tutorial.md "share-dl-fgac-tutorial.md")

   In this tutorial, you learn how to quickly and easily share datasets using Lake Formation when managing multiple AWS accounts with AWS Organizations.

###### Topics

- [Creating a data lake from an AWS CloudTrail source](getting-started-cloudtrail-tutorial.md "getting-started-cloudtrail-tutorial.md")
- [Creating a data lake from a JDBC source in Lake Formation](getting-started-tutorial-jdbc.md "getting-started-tutorial-jdbc.md")
- [Setting up permissions for open table storage formats in Lake Formation](otf-tutorial.md "otf-tutorial.md")
- [Managing a data lake using Lake Formation tag-based
  access control](managing-dl-tutorial.md "managing-dl-tutorial.md")
- [Securing data lakes with row-level access control](cbac-tutorial.md "cbac-tutorial.md")
- [Sharing a data lake using Lake Formation tag-based
  access control and named resources](share-dl-tbac-tutorial.md "share-dl-tbac-tutorial.md")
- [Sharing a data lake using Lake Formation fine-grained access control](share-dl-fgac-tutorial.md "share-dl-fgac-tutorial.md")
