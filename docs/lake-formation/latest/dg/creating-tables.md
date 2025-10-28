# Creating tables

AWS Lake Formation metadata tables contain information about data in the data lake, including schema
information, partition information, and data location. These tables are stored in the AWS Glue
Data Catalog. You use them to access underlying data in the data lake and manage that data with Lake Formation
permissions. Tables are stored within databases in the Data Catalog.

There are several ways to create Data Catalog tables:

- Run a crawler in AWS Glue. See [Defining crawlers](../../../glue/latest/dg/add-crawler.md "../../../glue/latest/dg/add-crawler.md") in the
  _AWS Glue Developer Guide_.
- Create and run a workflow. See [Importing data using workflows in Lake Formation](workflows.md "workflows.md").
- Create a table manually using the Lake Formation console, AWS Glue API, or AWS Command Line Interface
  (AWS CLI).
- Create a table using Amazon Athena.
- Create a resource link to a table in an external account. See [Creating resource links](creating-resource-links.md "creating-resource-links.md").
