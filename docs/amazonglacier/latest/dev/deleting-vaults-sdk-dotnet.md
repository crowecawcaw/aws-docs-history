**This page is only for existing customers of the Amazon Glacier service using Vaults and the original REST API from 2012.**

If you're looking for archival storage solutions, we recommend using the Amazon Glacier storage classes in Amazon S3, S3 Glacier Instant Retrieval, S3 Glacier Flexible Retrieval, and S3 Glacier Deep Archive. To learn more about these storage options, see [Amazon Glacier storage classes](https://aws.amazon.com/s3/storage-classes/glacier/ "https://aws.amazon.com/s3/storage-classes/glacier/").

Amazon Glacier (original standalone vault-based service) is no longer accepting new customers. Amazon Glacier is a standalone service with its own APIs that stores data in vaults and is distinct from Amazon S3 and the Amazon S3 Glacier storage classes. Your existing data will remain secure and accessible in Amazon Glacier indefinitely. No migration is required. For low-cost, long-term archival storage, AWS recommends the [Amazon S3 Glacier storage classes](https://aws.amazon.com/s3/storage-classes/glacier/ "https://aws.amazon.com/s3/storage-classes/glacier/"), which deliver a superior customer experience with S3 bucket-based APIs, full AWS Region availability, lower costs, and AWS service integration. If you want enhanced capabilities, consider migrating to Amazon S3 Glacier storage classes by using our [AWS Solutions Guidance for transferring data from Amazon Glacier vaults to Amazon S3 Glacier storage classes](https://aws.amazon.com/solutions/guidance/data-transfer-from-amazon-s3-glacier-vaults-to-amazon-s3/ "https://aws.amazon.com/solutions/guidance/data-transfer-from-amazon-s3-glacier-vaults-to-amazon-s3/").

# Deleting a Vault in Amazon Glacier Using the AWS SDK for .NET

Both the [high-level and low-level APIs](using-aws-sdk.md "using-aws-sdk.md") provided by the Amazon SDK for .NET provide a method to delete a vault.

###### Topics

- [Deleting a Vault Using the High-Level API of the AWS SDK for .NET](#deleting-vault-sdk-dotnet-high-level "#deleting-vault-sdk-dotnet-high-level")
- [Deleting a Vault Using the Low-Level API of the AWS SDK for .NET](#deleting-vault-sdk-dotnet-low-level "#deleting-vault-sdk-dotnet-low-level")

## Deleting a Vault Using the High-Level API of the AWS SDK for .NET

The `ArchiveTransferManager` class of the high-level API provides the
`DeleteVault` method you can use to delete a vault.

### Example: Deleting a Vault Using the High-Level API of the AWS SDK for .NET

For a working code example, see [Example: Vault Operations Using the High-Level API of the AWS SDK for .NET](creating-vaults-dotnet-sdk.md#vault-operations-example-dotnet-highlevel "creating-vaults-dotnet-sdk.md#vault-operations-example-dotnet-highlevel"). The C# code example shows basic vault
operations including create and delete vault.

## Deleting a Vault Using the Low-Level API of the AWS SDK for .NET

The following are the steps to delete a vault using the AWS SDK for .NET.

1. Create an instance of the `AmazonGlacierClient` class (the client).

You need to specify an AWS Region from where you want to delete a vault. All
operations you perform using this client apply to that AWS Region. 2. Provide request information by creating an instance of the `DeleteVaultRequest`
class.

You need to provide the vault name and account ID. If you don't provide an account ID,
then account ID associated with the credentials you provide to sign the
request is assumed. For more information, see [Using the AWS SDK for .NET with Amazon Glacier](using-aws-sdk-for-dot-net.md "using-aws-sdk-for-dot-net.md"). 3. Run the `DeleteVault` method by providing the request object as a
parameter.

Amazon Glacier (Amazon Glacier) deletes the vault only if it is empty. For more information, see [Delete Vault (DELETE vault)](api-vault-delete.md "api-vault-delete.md").

The following C# code snippet illustrates the preceding steps. The snippet retrieves metadata
information of a vault that exists in the default AWS Region.

```
AmazonGlacier client;
client = new AmazonGlacierClient(Amazon.RegionEndpoint.USEast1);

DeleteVaultRequest request = new DeleteVaultRequest()
{
  VaultName = "*** provide vault name ***"
};

DeleteVaultResponse response = client.DeleteVault(request);
```

###### Note

For information about the underlying REST API, see [Delete Vault (DELETE vault)](api-vault-delete.md "api-vault-delete.md").

### Example: Deleting a Vault Using the Low-Level API of the AWS SDK for .NET

For a working code example, see [Example: Vault Operations Using the Low-Level API of the AWS SDK for .NET](creating-vaults-dotnet-sdk.md#vault-operations-example-dotnet-lowlevel "creating-vaults-dotnet-sdk.md#vault-operations-example-dotnet-lowlevel"). The C# code example shows basic vault
operations including create and delete vault.
