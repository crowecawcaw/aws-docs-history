**This page is only for existing customers of the Amazon Glacier service using Vaults and the original REST API from 2012.**

If you're looking for archival storage solutions, we recommend using the Amazon Glacier storage classes in Amazon S3, S3 Glacier Instant Retrieval, S3 Glacier Flexible Retrieval, and S3 Glacier Deep Archive. To learn more about these storage options, see [Amazon Glacier storage classes](https://aws.amazon.com/s3/storage-classes/glacier/ "https://aws.amazon.com/s3/storage-classes/glacier/").

Amazon Glacier (original standalone vault-based service) is no longer accepting new customers. Amazon Glacier is a standalone service with its own APIs that stores data in vaults and is distinct from Amazon S3 and the Amazon S3 Glacier storage classes. Your existing data will remain secure and accessible in Amazon Glacier indefinitely. No migration is required. For low-cost, long-term archival storage, AWS recommends the [Amazon S3 Glacier storage classes](https://aws.amazon.com/s3/storage-classes/glacier/ "https://aws.amazon.com/s3/storage-classes/glacier/"), which deliver a superior customer experience with S3 bucket-based APIs, full AWS Region availability, lower costs, and AWS service integration. If you want enhanced capabilities, consider migrating to Amazon S3 Glacier storage classes by using our [AWS Solutions Guidance for transferring data from Amazon Glacier vaults to Amazon S3 Glacier storage classes](https://aws.amazon.com/solutions/guidance/data-transfer-from-amazon-s3-glacier-vaults-to-amazon-s3/ "https://aws.amazon.com/solutions/guidance/data-transfer-from-amazon-s3-glacier-vaults-to-amazon-s3/").

# Actions for Amazon Glacier using AWS SDKs

The following code examples demonstrate how to perform individual Amazon Glacier
actions with AWS SDKs. Each example includes
a link to GitHub, where you can find instructions for setting up and running the code.

These excerpts call the Amazon Glacier API and
are code excerpts from larger programs that must be run in context.
You can see actions in context in
[Scenarios for
Amazon Glacier using AWS SDKs](service_code_examples_scenarios.md "service_code_examples_scenarios.md") .

The following examples include only the most commonly used actions.
For a complete list, see the
[Amazon Glacier API Reference](amazon-glacier-api.md "amazon-glacier-api.md").

###### Examples

- [AddTagsToVault](example_glacier_AddTagsToVault_section.md "example_glacier_AddTagsToVault_section.md")
- [CreateVault](example_glacier_CreateVault_section.md "example_glacier_CreateVault_section.md")
- [DeleteArchive](example_glacier_DeleteArchive_section.md "example_glacier_DeleteArchive_section.md")
- [DeleteVault](example_glacier_DeleteVault_section.md "example_glacier_DeleteVault_section.md")
- [DeleteVaultNotifications](example_glacier_DeleteVaultNotifications_section.md "example_glacier_DeleteVaultNotifications_section.md")
- [DescribeJob](example_glacier_DescribeJob_section.md "example_glacier_DescribeJob_section.md")
- [DescribeVault](example_glacier_DescribeVault_section.md "example_glacier_DescribeVault_section.md")
- [GetJobOutput](example_glacier_GetJobOutput_section.md "example_glacier_GetJobOutput_section.md")
- [GetVaultNotifications](example_glacier_GetVaultNotifications_section.md "example_glacier_GetVaultNotifications_section.md")
- [InitiateJob](example_glacier_InitiateJob_section.md "example_glacier_InitiateJob_section.md")
- [ListJobs](example_glacier_ListJobs_section.md "example_glacier_ListJobs_section.md")
- [ListTagsForVault](example_glacier_ListTagsForVault_section.md "example_glacier_ListTagsForVault_section.md")
- [ListVaults](example_glacier_ListVaults_section.md "example_glacier_ListVaults_section.md")
- [SetVaultNotifications](example_glacier_SetVaultNotifications_section.md "example_glacier_SetVaultNotifications_section.md")
- [UploadArchive](example_glacier_UploadArchive_section.md "example_glacier_UploadArchive_section.md")
- [UploadMultipartPart](example_glacier_UploadMultipartPart_section.md "example_glacier_UploadMultipartPart_section.md")
