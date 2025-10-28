# Using FSx for Windows File Server with Amazon Kendra

Amazon Kendra is a highly accurate and intelligent search service. FSx for Windows File Server file
systems can be used as data sources for Amazon Kendra, allowing you to index and intelligently
search for information contained in documents stored on your file system.

- For more information about Amazon Kendra,
  see
  [What is Amazon Kendra](../../../kendra/latest/dg/what-is-kendra.md "../../../kendra/latest/dg/what-is-kendra.md") in the
  _Amazon Kendra Developer's Guide_.
- For more information about how to add your file system as an Amazon Kendra data source,
  see
  [Getting started with an Amazon FSx data source (console)](../../../kendra/latest/dg/getting-started-fsx.md "../../../kendra/latest/dg/getting-started-fsx.md") in the
  _Amazon Kendra Developer's Guide_.
- For overview information about Amazon Kendra,
  see the [Amazon Kendra website](https://aws.amazon.com/kendra/ "https://aws.amazon.com/kendra/").
- For a walkthrough of how to search your file system using Amazon Kendra, see [Securely search unstructured data on Windows file systems with the Amazon Kendra connector for Amazon FSx for Windows File Server](https://aws.amazon.com/blogs/machine-learning/securely-search-unstructured-data-on-windows-file-systems-with-amazon-kendra-connector-for-amazon-fsx-for-windows-file-server/ "https://aws.amazon.com/blogs/machine-learning/securely-search-unstructured-data-on-windows-file-systems-with-amazon-kendra-connector-for-amazon-fsx-for-windows-file-server/")
  on the _AWS Machine Learning Blog_.

## File system performance

When you add an FSx for Windows File Server file system as a data source, Amazon Kendra crawls the
files and folders on the file system on a regular sync frequency to create and
maintain its search index. (You can select the sync frequency when you establish
the integration.) This file access activity from Amazon Kendra will consume file system
resources, similar to activity from your own workloads accessing the file system.

Ensure your file system is configured with sufficient resources such that your
workload performance is not impacted. Specifically, if you are planning to index
a large number of files, we recommend using a file system with SSD storage type,
which provides higher maximum throughput and IOPS levels for requests that need
to access the storage volumes. For more information about the Amazon FSx performance model, see [FSx for Windows File Server performance](performance.md "performance.md").
