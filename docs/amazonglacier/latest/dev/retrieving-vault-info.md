**This page is only for existing customers of the Amazon Glacier service using Vaults and the original REST API from 2012.**

If you're looking for archival storage solutions, we recommend using the Amazon Glacier storage classes in Amazon S3, S3 Glacier Instant Retrieval, S3 Glacier Flexible Retrieval, and S3 Glacier Deep Archive. To learn more about these storage options, see [Amazon Glacier storage classes](https://aws.amazon.com/s3/storage-classes/glacier/ "https://aws.amazon.com/s3/storage-classes/glacier/").

Amazon Glacier (original standalone vault-based service) is no longer accepting new customers. Amazon Glacier is a standalone service with its own APIs that stores data in vaults and is distinct from Amazon S3 and the Amazon S3 Glacier storage classes. Your existing data will remain secure and accessible in Amazon Glacier indefinitely. No migration is required. For low-cost, long-term archival storage, AWS recommends the [Amazon S3 Glacier storage classes](https://aws.amazon.com/s3/storage-classes/glacier/ "https://aws.amazon.com/s3/storage-classes/glacier/"), which deliver a superior customer experience with S3 bucket-based APIs, full AWS Region availability, lower costs, and AWS service integration. If you want enhanced capabilities, consider migrating to Amazon S3 Glacier storage classes by using our [AWS Solutions Guidance for transferring data from Amazon Glacier vaults to Amazon S3 Glacier storage classes](https://aws.amazon.com/solutions/guidance/data-transfer-from-amazon-s3-glacier-vaults-to-amazon-s3/ "https://aws.amazon.com/solutions/guidance/data-transfer-from-amazon-s3-glacier-vaults-to-amazon-s3/").

# Retrieving Vault Metadata in Amazon Glacier

You can retrieve vault information such as the vault creation date, number of archives in the
vault, and the total size of all the archives in the vault. Amazon Glacier (Amazon Glacier) provides API
calls for you to retrieve this information for a specific vault or all the vaults in a
specific AWS Region in your account.

If you retrieve a vault list, Amazon Glacier returns the list sorted by the ASCII values of
the vault names. The list contains up to 1,000 vaults. You should always check the response
for a marker at which to continue the list; if there are no more items the marker field is
`null`. You can optionally limit the number of vaults returned in the
response. If there are more vaults than are returned in the response, the result is
paginated. You need to send additional requests to fetch the next set of vaults.

###### Topics

- [Retrieving Vault Metadata in Amazon Glacier Using the AWS SDK for Java](retrieving-vault-info-sdk-java.md "retrieving-vault-info-sdk-java.md")
- [Retrieving Vault Metadata in Amazon Glacier Using the AWS SDK for .NET](retrieving-vault-info-sdk-dotnet.md "retrieving-vault-info-sdk-dotnet.md")
- [Retrieving Vault Metadata Using the REST API](listing-vaults-rest-api.md "listing-vaults-rest-api.md")
- [Retrieving Vault Metadata in Amazon Glacier Using the AWS Command Line Interface](retrieving-vault-info-cli.md "retrieving-vault-info-cli.md")
