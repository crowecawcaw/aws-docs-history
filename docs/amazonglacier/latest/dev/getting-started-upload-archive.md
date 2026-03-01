**This page is only for existing customers of the Amazon Glacier service using Vaults and the original REST API from 2012.**

If you're looking for archival storage solutions, we recommend using the Amazon Glacier storage classes in Amazon S3, S3 Glacier Instant Retrieval, S3 Glacier Flexible Retrieval, and S3 Glacier Deep Archive. To learn more about these storage options, see [Amazon Glacier storage classes](https://aws.amazon.com/s3/storage-classes/glacier/ "https://aws.amazon.com/s3/storage-classes/glacier/").

Amazon Glacier (original standalone vault-based service) is no longer accepting new customers. Amazon Glacier is a standalone service with its own APIs that stores data in vaults and is distinct from Amazon S3 and the Amazon S3 Glacier storage classes. Your existing data will remain secure and accessible in Amazon Glacier indefinitely. No migration is required. For low-cost, long-term archival storage, AWS recommends the [Amazon S3 Glacier storage classes](https://aws.amazon.com/s3/storage-classes/glacier/ "https://aws.amazon.com/s3/storage-classes/glacier/"), which deliver a superior customer experience with S3 bucket-based APIs, full AWS Region availability, lower costs, and AWS service integration. If you want enhanced capabilities, consider migrating to Amazon S3 Glacier storage classes by using our [AWS Solutions Guidance for transferring data from Amazon Glacier vaults to Amazon S3 Glacier storage classes](https://aws.amazon.com/solutions/guidance/data-transfer-from-amazon-s3-glacier-vaults-to-amazon-s3/ "https://aws.amazon.com/solutions/guidance/data-transfer-from-amazon-s3-glacier-vaults-to-amazon-s3/").

# Step 3: Upload an Archive to a Vault in Amazon Glacier

In this step, you'll upload a sample archive to the vault that you created in the preceding
step (see [Step 2: Create a Vault in Amazon Glacier](getting-started-create-vault.md "getting-started-create-vault.md")). Depending on the development
platform that you're using, choose one of the links at the end of this section.

###### Important

Any archive operation, such as upload, download, or deletion, requires you to use the
AWS Command Line Interface (CLI) or write code. There is no console support for archive operations.
For example, to upload data, such as photos, videos, and other documents, you must
either use the AWS CLI or write code to make requests, by using either the REST API
directly or by using the AWS SDKs.

To install the AWS CLI, see [AWS Command Line Interface](http://aws.amazon.com/cli/ "http://aws.amazon.com/cli/").
For more information about using Amazon Glacier with the AWS CLI, see [AWS CLI
Reference for Amazon Glacier](../../../cli/latest/reference/glacier/index.md "../../../cli/latest/reference/glacier/index.md"). For examples of using the AWS CLI to upload
archives to Amazon Glacier, see [Using
Amazon Glacier with the AWS Command Line Interface](../../../cli/latest/userguide/cli-using-glacier.md "../../../cli/latest/userguide/cli-using-glacier.md").

An archive is any object, such as a photo, video, or document, that you store in a vault. An
archive is the base unit of storage in Amazon Glacier. You can upload an archive in a single
request. For large archives, Amazon Glacier provides a multipart upload API operation that
enables you to upload an archive in parts.

In this getting started section, you upload a sample archive in a single request. For
this exercise, you specify a file that is smaller in size. For larger files, multipart
upload is suitable. For more information, see [Uploading Large Archives in Parts (Multipart Upload)](uploading-archive-mpu.md "uploading-archive-mpu.md").

###### Topics

- [Upload an Archive to a Vault in Amazon Glacier by Using the AWS SDK for Java](getting-started-upload-archive-java.md "getting-started-upload-archive-java.md")
- [Upload an Archive to a Vault in Amazon Glacier by Using the AWS SDK for .NET](getting-started-upload-archive-dotnet.md "getting-started-upload-archive-dotnet.md")
