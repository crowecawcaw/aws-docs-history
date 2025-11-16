# Connecting to data with AWS Glue DataBrew

In AWS Glue DataBrew, a _dataset_ represents data that's either uploaded from a
file or stored elsewhere. For example, data can be stored in Amazon S3, in a supported JDBC data
source, or an AWS Glue Data Catalog. If you're not uploading a file directly to DataBrew, the
dataset also contains details on how DataBrew can connect to the data.

When you create your dataset (for example, `inventory-dataset`), you enter the
connection details only once. From that point, DataBrew can access the underlying
data for you. With this approach, you can create projects and develop transformations
for your data, without having to worry about connection details or file formats.

###### Topics

- [Supported file types for data sources](supported-data-file-sources.md "supported-data-file-sources.md")
- [Supported connections for data sources and outputs](supported-data-connection-sources.md "supported-data-connection-sources.md")
- [Using datasets in AWS Glue DataBrew](datasets.md "datasets.md")
- [Connecting to your data](datasets.md "datasets.md")
- [Connecting to data in a text file with DataBrew](datasets.md "datasets.md")
- [Connecting data in multiple files in Amazon S3](datasets.md "datasets.md")
- [Data types](datatypes.md "datatypes.md")
- [Advanced data types](projects.md "projects.md")
