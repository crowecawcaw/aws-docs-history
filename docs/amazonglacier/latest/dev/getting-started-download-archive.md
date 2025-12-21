**This page is only for existing customers of the Amazon Glacier service using Vaults and the original REST API from 2012.**

If you're looking for archival storage solutions, we recommend using the Amazon Glacier storage classes in Amazon S3, S3 Glacier Instant Retrieval, S3 Glacier Flexible Retrieval, and S3 Glacier Deep Archive. To learn more about these storage options, see [Amazon Glacier storage classes](https://aws.amazon.com/s3/storage-classes/glacier/ "https://aws.amazon.com/s3/storage-classes/glacier/").

Amazon Glacier (original standalone vault-based service) is no longer accepting new customers. Amazon Glacier is a standalone service with its own APIs that stores data in vaults and is distinct from Amazon S3 and the Amazon S3 Glacier storage classes. Your existing data will remain secure and accessible in Amazon Glacier indefinitely. No migration is required. For low-cost, long-term archival storage, AWS recommends the [Amazon S3 Glacier storage classes](https://aws.amazon.com/s3/storage-classes/glacier/ "https://aws.amazon.com/s3/storage-classes/glacier/"), which deliver a superior customer experience with S3 bucket-based APIs, full AWS Region availability, lower costs, and AWS service integration. If you want enhanced capabilities, consider migrating to Amazon S3 Glacier storage classes by using our [AWS Solutions Guidance for transferring data from Amazon Glacier vaults to Amazon S3 Glacier storage classes](https://aws.amazon.com/solutions/guidance/data-transfer-from-amazon-s3-glacier-vaults-to-amazon-s3/ "https://aws.amazon.com/solutions/guidance/data-transfer-from-amazon-s3-glacier-vaults-to-amazon-s3/").

# Step 4: Download an Archive from a Vault in

Amazon Glacier

In this step, you'll download the sample archive that you uploaded previously in [Step 3: Upload an Archive to a Vault in
Amazon Glacier](getting-started-upload-archive.md "getting-started-upload-archive.md").

###### Important

Amazon Glacier does provide a console. However, any archive operation, such as upload, download,
or deletion, requires you to use the AWS Command Line Interface (CLI) or write code. There is no
console support for archive operations. For example, to upload data, such as photos,
videos, and other documents, you must either use the AWS CLI or write code to make
requests, by using either the REST API directly or by using the AWS SDKs.

To install the AWS CLI, see [AWS Command Line Interface](http://aws.amazon.com/cli/ "http://aws.amazon.com/cli/").
For more information about using Amazon Glacier with the AWS CLI, see [AWS CLI
Reference for Amazon Glacier](../../../cli/latest/reference/glacier/index.md "../../../cli/latest/reference/glacier/index.md"). For examples of using the AWS CLI to upload
archives to Amazon Glacier, see [Using
Amazon Glacier with the AWS Command Line Interface](../../../cli/latest/userguide/cli-using-glacier.md "../../../cli/latest/userguide/cli-using-glacier.md").

In general, retrieving your data from Amazon Glacier is a two-step process:

1. Initiate a retrieval job.
2. After the job is completed, download the bytes of data.
   To retrieve an archive from Amazon Glacier, you first initiate a job. After the job is completed,
   you download the data. For more information about archive retrievals, see [Retrieving Amazon Glacier Archives](downloading-an-archive-two-steps.md "downloading-an-archive-two-steps.md").

The access time of your request depends on the retrieval option that you choose: Expedited,
Standard, or Bulk retrievals. For all but the largest archives (250 MB+), archives
accessed by using Expedited retrievals are typically made available within 1–5 minutes.
Archives retrieved by using Standard retrievals typically are available between 3–5
hours. Bulk retrievals typically are available within 5–12 hours. For more information
about the various retrieval options, see the [Amazon Glacier FAQ](http://aws.amazon.com/glacier/faqs/#Data-retrievals "http://aws.amazon.com/glacier/faqs/#Data-retrievals"). For
information about data retrieval charges, see the [Amazon Glacier pricing
page](https://aws.amazon.com/s3/glacier/pricing/ "https://aws.amazon.com/s3/glacier/pricing/").

The code examples shown in the following topics initiate the job, wait for it to be
completed, and then download the archive's data.

###### Topics

- [Download an Archive from a Vault in
  Amazon Glacier by Using the AWS SDK for Java](getting-started-download-archive-java.md "getting-started-download-archive-java.md")
- [Download an Archive from a Vault in
  Amazon Glacier by Using the AWS SDK for .NET](getting-started-download-archive-dotnet.md "getting-started-download-archive-dotnet.md")
