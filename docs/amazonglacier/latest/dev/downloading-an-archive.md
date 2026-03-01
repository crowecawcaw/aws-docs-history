**This page is only for existing customers of the Amazon Glacier service using Vaults and the original REST API from 2012.**

If you're looking for archival storage solutions, we recommend using the Amazon Glacier storage classes in Amazon S3, S3 Glacier Instant Retrieval, S3 Glacier Flexible Retrieval, and S3 Glacier Deep Archive. To learn more about these storage options, see [Amazon Glacier storage classes](https://aws.amazon.com/s3/storage-classes/glacier/ "https://aws.amazon.com/s3/storage-classes/glacier/").

Amazon Glacier (original standalone vault-based service) is no longer accepting new customers. Amazon Glacier is a standalone service with its own APIs that stores data in vaults and is distinct from Amazon S3 and the Amazon S3 Glacier storage classes. Your existing data will remain secure and accessible in Amazon Glacier indefinitely. No migration is required. For low-cost, long-term archival storage, AWS recommends the [Amazon S3 Glacier storage classes](https://aws.amazon.com/s3/storage-classes/glacier/ "https://aws.amazon.com/s3/storage-classes/glacier/"), which deliver a superior customer experience with S3 bucket-based APIs, full AWS Region availability, lower costs, and AWS service integration. If you want enhanced capabilities, consider migrating to Amazon S3 Glacier storage classes by using our [AWS Solutions Guidance for transferring data from Amazon Glacier vaults to Amazon S3 Glacier storage classes](https://aws.amazon.com/solutions/guidance/data-transfer-from-amazon-s3-glacier-vaults-to-amazon-s3/ "https://aws.amazon.com/solutions/guidance/data-transfer-from-amazon-s3-glacier-vaults-to-amazon-s3/").

# Downloading an Archive in Amazon Glacier

Amazon Glacier provides a management console, which you can use to create and delete vaults.
However, you cannot download archives from Amazon Glacier by using the management console. To
download data, such as photos, videos, and other documents, you must either use the
AWS Command Line Interface (AWS CLI) or write code to make requests, by using either the REST API directly or
by using the AWS SDKs.

For information about using Amazon Glacier with the AWS CLI, see the [AWS CLI Reference for
Amazon Glacier](../../../cli/latest/reference/glacier/index.md "../../../cli/latest/reference/glacier/index.md"). To install the AWS CLI, see [AWS Command Line Interface](http://aws.amazon.com/cli/ "http://aws.amazon.com/cli/"). The following topics describe how to download archives to Amazon Glacier
by using the AWS SDK for Java, the AWS SDK for .NET, and the Amazon Glacier REST API.

###### Topics

- [Retrieving Amazon Glacier Archives](downloading-an-archive-two-steps.md "downloading-an-archive-two-steps.md")
- [Downloading an Archive in Amazon Glacier Using the AWS SDK for Java](downloading-an-archive-using-java.md "downloading-an-archive-using-java.md")
- [Downloading an Archive in Amazon Glacier Using the AWS SDK for .NET](downloading-an-archive-using-dotnet.md "downloading-an-archive-using-dotnet.md")
- [Downloading a Large Archive Using Parallel Processing with Python](downloading-large-archive-parallel-python.md "downloading-large-archive-parallel-python.md")
- [Downloading an Archive by Using the REST API](downloading-an-archive-using-rest.md "downloading-an-archive-using-rest.md")
- [Downloading an Archive in Amazon Glacier Using the AWS CLI](downloading-an-archive-using-cli.md "downloading-an-archive-using-cli.md")
