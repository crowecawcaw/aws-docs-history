**This page is only for existing customers of the Amazon Glacier service using Vaults and the original REST API from 2012.**

If you're looking for archival storage solutions, we recommend using the Amazon Glacier storage classes in Amazon S3, S3 Glacier Instant Retrieval, S3 Glacier Flexible Retrieval, and S3 Glacier Deep Archive. To learn more about these storage options, see [Amazon Glacier storage classes](https://aws.amazon.com/s3/storage-classes/glacier/ "https://aws.amazon.com/s3/storage-classes/glacier/").

Amazon Glacier (original standalone vault-based service) is no longer accepting new customers. Amazon Glacier is a standalone service with its own APIs that stores data in vaults and is distinct from Amazon S3 and the Amazon S3 Glacier storage classes. Your existing data will remain secure and accessible in Amazon Glacier indefinitely. No migration is required. For low-cost, long-term archival storage, AWS recommends the [Amazon S3 Glacier storage classes](https://aws.amazon.com/s3/storage-classes/glacier/ "https://aws.amazon.com/s3/storage-classes/glacier/"), which deliver a superior customer experience with S3 bucket-based APIs, full AWS Region availability, lower costs, and AWS service integration. If you want enhanced capabilities, consider migrating to Amazon S3 Glacier storage classes by using our [AWS Solutions Guidance for transferring data from Amazon Glacier vaults to Amazon S3 Glacier storage classes](https://aws.amazon.com/solutions/guidance/data-transfer-from-amazon-s3-glacier-vaults-to-amazon-s3/ "https://aws.amazon.com/solutions/guidance/data-transfer-from-amazon-s3-glacier-vaults-to-amazon-s3/").

# Retrieving Vault Metadata in Amazon Glacier Using the AWS SDK for .NET

###### Topics

- [Retrieve Vault Metadata for a Vault](#retrieve-vault-info-sdk-dotnet-lowlevel-one-vault "#retrieve-vault-info-sdk-dotnet-lowlevel-one-vault")
- [Retrieve Vault Metadata for
  All Vaults in a Region](#retrieve-vault-info-sdk-dotnet-lowlevel-all-vaults "#retrieve-vault-info-sdk-dotnet-lowlevel-all-vaults")
- [Example: Retrieving Vault Metadata Using the
  Low-Level API of the AWS SDK for .NET](#creating-vaults-sdk-dotnet-example "#creating-vaults-sdk-dotnet-example")

## Retrieve Vault Metadata for a Vault

You can retrieve metadata for a specific vault or all the vaults in a specific AWS Region. The
following are the steps to retrieve vault metadata for a specific vault using the
low-level API of the AWS SDK for .NET.

1. Create an instance of the `AmazonGlacierClient` class (the client).

You need to specify an AWS Region where the vault resides. All operations you perform
using this client apply to that AWS Region. 2. Provide request information by creating an instance of the
`DescribeVaultRequest` class.

Amazon Glacier (Amazon Glacier) requires you to provide a vault name and your account ID. If you don't
provide an account ID, then the account ID associated with the credentials you
provide to sign the request is assumed. For more information, see [Using the AWS SDK for .NET with Amazon Glacier](using-aws-sdk-for-dot-net.md "using-aws-sdk-for-dot-net.md"). 3. Run the `DescribeVault` method by providing the request object as a
parameter.

The vault metadata information that Amazon Glacier returns is available in the
`DescribeVaultResult` object.

The following C# code snippet illustrates the preceding steps. The snippet retrieves metadata
information of an existing vault in the US West (Oregon) Region.

```
AmazonGlacierClient client;
client = new AmazonGlacierClient(Amazon.RegionEndpoint.USWest2);

DescribeVaultRequest describeVaultRequest = new DescribeVaultRequest()
{
  VaultName = "*** Provide vault name ***"
};
DescribeVaultResponse describeVaultResponse = client.DescribeVault(describeVaultRequest);
Console.WriteLine("\nVault description...");
Console.WriteLine(
   "\nVaultName: " + describeVaultResponse.VaultName +
   "\nVaultARN: " + describeVaultResponse.VaultARN +
   "\nVaultCreationDate: " + describeVaultResponse.CreationDate +
   "\nNumberOfArchives: " + describeVaultResponse.NumberOfArchives +
   "\nSizeInBytes: " + describeVaultResponse.SizeInBytes +
   "\nLastInventoryDate: " + describeVaultResponse.LastInventoryDate
   );
```

###### Note

For information about the underlying REST API, see [Describe Vault (GET vault)](api-vault-get.md "api-vault-get.md").

## Retrieve Vault Metadata for

All Vaults in a Region

You can also use the `ListVaults` method to retrieve metadata for all the vaults
in a specific AWS Region.

The following C# code snippet retrieves list of vaults in the US West (Oregon) Region. The request limits the number of vaults returned in the response to 5. The code
snippet then makes a series of `ListVaults` calls to retrieve the entire
vault list from the AWS Region.

```
AmazonGlacierClient client;
client = new AmazonGlacierClient(Amazon.RegionEndpoint.USWest2);
string lastMarker = null;
Console.WriteLine("\n List of vaults in your account in the specific AWS Region ...");
do
{
  ListVaultsRequest request = new ListVaultsRequest()
  {
    Limit = 5,
    Marker = lastMarker
  };
  ListVaultsResponse response = client.ListVaults(request);

  foreach (DescribeVaultOutput output in response.VaultList)
  {
    Console.WriteLine("Vault Name: {0} \tCreation Date: {1} \t #of archives: {2}",
                      output.VaultName, output.CreationDate, output.NumberOfArchives);
  }
  lastMarker = response.Marker;
} while (lastMarker != null);
```

In the preceding code segment, if you don't specify the `Limit` value in the
request, Amazon Glacier returns up to 10 vaults, as set by the Amazon Glacier API.

Note that the information returned for each vault in the list is the same as the
information you get by calling the `DescribeVault` method for a specific
vault.

###### Note

The `ListVaults` method calls the underlying REST API (see [List Vaults (GET vaults)](api-vaults-get.md "api-vaults-get.md")).

## Example: Retrieving Vault Metadata Using the

Low-Level API of the AWS SDK for .NET

For a working code example, see [Example: Vault Operations Using the Low-Level API of the AWS SDK for .NET](creating-vaults-dotnet-sdk.md#vault-operations-example-dotnet-lowlevel "creating-vaults-dotnet-sdk.md#vault-operations-example-dotnet-lowlevel"). The C# code example creates a vault and
retrieves the vault metadata.
