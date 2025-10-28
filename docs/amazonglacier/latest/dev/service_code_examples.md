**This page is only for existing customers of the Amazon Glacier service using Vaults and the original REST API from 2012.**

If you're looking for archival storage solutions, we recommend using the Amazon Glacier storage classes in Amazon S3, S3 Glacier Instant Retrieval, S3 Glacier Flexible Retrieval, and S3 Glacier Deep Archive. To learn more about these storage options, see [Amazon Glacier storage classes](https://aws.amazon.com/s3/storage-classes/glacier/ "https://aws.amazon.com/s3/storage-classes/glacier/").

Amazon Glacier (original standalone vault-based service) will no longer accept new customers starting December 15, 2025, with no impact to existing customers. Amazon Glacier is a standalone service with its own APIs that stores data in vaults and is distinct from Amazon S3 and the Amazon S3 Glacier storage classes. Your existing data will remain secure and accessible in Amazon Glacier indefinitely. No migration is required. For low-cost, long-term archival storage, AWS recommends the [Amazon S3 Glacier storage classes](https://aws.amazon.com/s3/storage-classes/glacier/ "https://aws.amazon.com/s3/storage-classes/glacier/"), which deliver a superior customer experience with S3 bucket-based APIs, full AWS Region availability, lower costs, and AWS service integration. If you want enhanced capabilities, consider migrating to Amazon S3 Glacier storage classes by using our [AWS Solutions Guidance for transferring data from Amazon Glacier vaults to Amazon S3 Glacier storage classes](https://aws.amazon.com/solutions/guidance/data-transfer-from-amazon-s3-glacier-vaults-to-amazon-s3/ "https://aws.amazon.com/solutions/guidance/data-transfer-from-amazon-s3-glacier-vaults-to-amazon-s3/").

# Code examples for Amazon Glacier using AWS SDKs

The following code examples show how to use Amazon Glacier with an AWS software development kit (SDK).

_Actions_ are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

_Scenarios_ are code examples that show you how to accomplish specific tasks by calling multiple functions within a service or combined with other AWS services.

For a complete list of AWS SDK developer guides and code examples, see
[Using Amazon Glacier with an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.

**Get started**

The following code example shows how to get started using Amazon Glacier.

.NET

**SDK for .NET**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/dotnetv3/EventBridge#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/dotnetv3/EventBridge#code-examples").

```

using Amazon.Glacier;
using Amazon.Glacier.Model;

namespace GlacierActions;

public static class HelloGlacier
{
    static async Task Main()
    {
        var glacierService = new AmazonGlacierClient();

        Console.WriteLine("Hello Amazon Glacier!");
        Console.WriteLine("Let's list your Glacier vaults:");

        // You can use await and any of the async methods to get a response.
        // Let's get the vaults using a paginator.
        var glacierVaultPaginator = glacierService.Paginators.ListVaults(
            new ListVaultsRequest { AccountId = "-" });

        await foreach (var vault in glacierVaultPaginator.VaultList)
        {
            Console.WriteLine($"{vault.CreationDate}:{vault.VaultName}, ARN:{vault.VaultARN}");
        }
    }
}


```

- For API details, see
  [ListVaults](../../../goto/DotNetSDKV3/glacier-2012-06-01/ListVaults.md "../../../goto/DotNetSDKV3/glacier-2012-06-01/ListVaults.md")
  in _AWS SDK for .NET API Reference_.

###### Code examples

- [Basics](service_code_examples_basics.md "service_code_examples_basics.md")
  - [Hello Amazon Glacier](example_glacier_Hello_section.md "example_glacier_Hello_section.md")
  - [Actions](service_code_examples_actions.md "service_code_examples_actions.md")
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

- [Scenarios](service_code_examples_scenarios.md "service_code_examples_scenarios.md")
  - [Archive a file, get notifications, and initiate a job](example_glacier_Usage_UploadNotifyInitiate_section.md "example_glacier_Usage_UploadNotifyInitiate_section.md")
  - [Get archive content and delete the archive](example_glacier_Usage_RetrieveDelete_section.md "example_glacier_Usage_RetrieveDelete_section.md")
