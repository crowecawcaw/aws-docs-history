**This page is only for existing customers of the Amazon Glacier service using Vaults and the original REST API from 2012.**

If you're looking for archival storage solutions, we recommend using the Amazon Glacier storage classes in Amazon S3, S3 Glacier Instant Retrieval, S3 Glacier Flexible Retrieval, and S3 Glacier Deep Archive. To learn more about these storage options, see [Amazon Glacier storage classes](https://aws.amazon.com/s3/storage-classes/glacier/ "https://aws.amazon.com/s3/storage-classes/glacier/").

Amazon Glacier (original standalone vault-based service) will no longer accept new customers starting December 15, 2025, with no impact to existing customers. Amazon Glacier is a standalone service with its own APIs that stores data in vaults and is distinct from Amazon S3 and the Amazon S3 Glacier storage classes. Your existing data will remain secure and accessible in Amazon Glacier indefinitely. No migration is required. For low-cost, long-term archival storage, AWS recommends the [Amazon S3 Glacier storage classes](https://aws.amazon.com/s3/storage-classes/glacier/ "https://aws.amazon.com/s3/storage-classes/glacier/"), which deliver a superior customer experience with S3 bucket-based APIs, full AWS Region availability, lower costs, and AWS service integration. If you want enhanced capabilities, consider migrating to Amazon S3 Glacier storage classes by using our [AWS Solutions Guidance for transferring data from Amazon Glacier vaults to Amazon S3 Glacier storage classes](https://aws.amazon.com/solutions/guidance/data-transfer-from-amazon-s3-glacier-vaults-to-amazon-s3/ "https://aws.amazon.com/solutions/guidance/data-transfer-from-amazon-s3-glacier-vaults-to-amazon-s3/").

# Getting Started with Amazon Glacier

You can get started with Amazon Glacier (Amazon Glacier) by working with vaults and archives. A _vault_ is a container for storing archives, and an _archive_ is any object, such as a photo, video, or document, that you store in a vault. An archive is the base unit of storage in Amazon Glacier. This getting started exercise provides instructions for you to explore basic Amazon Glacier operations on vaults and archives. For more information about these resources, see the [Amazon Glacier Data Model](amazon-glacier-data-model.md "amazon-glacier-data-model.md") section.

In the getting started exercise, you will create a vault, upload and download an archive, and then delete the archive and the vault. You can do all these operations programmatically. However, the getting started exercise uses the Amazon Glacier management console to create and delete a vault. For uploading and downloading an archive, this getting started section uses the high-level API for the AWS SDK for Java and the AWS SDK for .NET. The high-level API provides a simplified programming experience when working with Amazon Glacier. For more information about using the high-level API with the AWS SDKs, see [Using the AWS SDKs with Amazon Glacier](using-aws-sdk.md "using-aws-sdk.md").

###### Important

Amazon Glacier does provide a console. However, any archive operation, such as upload, download, or deletion, requires you to use the AWS Command Line Interface (CLI) or write code. There is no console support for archive operations. For example, to upload data, such as photos, videos, and other documents, you must either use the AWS CLI or write code to make requests, by using either the REST API directly or by using the AWS SDKs.

To install the AWS CLI, see [AWS Command Line Interface](http://aws.amazon.com/cli/ "http://aws.amazon.com/cli/"). For more information about using Amazon Glacier with the AWS CLI, see the [AWS CLI Reference for Amazon Glacier](../../../cli/latest/reference/glacier/index.md "../../../cli/latest/reference/glacier/index.md"). For examples of using the AWS CLI to upload archives to Amazon Glacier, see [Using Amazon Glacier with the AWS Command Line Interface](../../../cli/latest/userguide/cli-using-glacier.md "../../../cli/latest/userguide/cli-using-glacier.md").

This getting started exercise provides code examples in Java and C# for you to upload and download an archive. The last section of the getting started exercise provides steps where you can learn more about the developer experience with Amazon Glacier.

###### Topics

- [Step 1: Before You Begin with Amazon Glacier](getting-started-before-you-begin.md "getting-started-before-you-begin.md")
- [Step 2: Create a Vault in Amazon Glacier](getting-started-create-vault.md "getting-started-create-vault.md")
- [Step 3: Upload an Archive to a Vault in
  Amazon Glacier](getting-started-upload-archive.md "getting-started-upload-archive.md")
- [Step 4: Download an Archive from a Vault in
  Amazon Glacier](getting-started-download-archive.md "getting-started-download-archive.md")
- [Step 5: Delete an Archive from a Vault in
  Amazon Glacier](getting-started-delete-archive.md "getting-started-delete-archive.md")
- [Step 6: Delete a Vault in Amazon Glacier](getting-started-delete-vault.md "getting-started-delete-vault.md")
- [Where Do I Go From Here?](getting-started-where-do-i-go-next.md "getting-started-where-do-i-go-next.md")
