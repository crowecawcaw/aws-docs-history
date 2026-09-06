

 **This page is only for existing customers of the Amazon Glacier service using Vaults and the original REST API from 2012.**

If you're looking for archival storage solutions, we recommend using the Amazon Glacier storage classes in Amazon S3, S3 Glacier Instant Retrieval, S3 Glacier Flexible Retrieval, and S3 Glacier Deep Archive. To learn more about these storage options, see [Amazon Glacier storage classes](https://aws.amazon.com/s3/storage-classes/glacier/).

Amazon Glacier (original standalone vault-based service) is no longer accepting new customers. Amazon Glacier is a standalone service with its own APIs that stores data in vaults and is distinct from Amazon S3 and the Amazon S3 Glacier storage classes. Your existing data will remain secure and accessible in Amazon Glacier indefinitely. No migration is required. For low-cost, long-term archival storage, AWS recommends the [Amazon S3 Glacier storage classes](https://aws.amazon.com/s3/storage-classes/glacier/), which deliver a superior customer experience with S3 bucket-based APIs, full AWS Region availability, lower costs, and AWS service integration. If you want enhanced capabilities, consider migrating to Amazon S3 Glacier storage classes by using our [AWS Solutions Guidance for transferring data from Amazon Glacier vaults to Amazon S3 Glacier storage classes](https://aws.amazon.com/solutions/guidance/data-transfer-from-amazon-s3-glacier-vaults-to-amazon-s3/).

# Creating a Vault in Amazon Glacier
<a name="creating-vaults"></a>

Creating a vault adds a vault to the set of vaults in your account. An AWS account can create up to 1,000 vaults per AWS Region. For a list of the AWS Regions supported by Amazon Glacier (Amazon Glacier), see [Regions and Endpoints](https://docs.aws.amazon.com/general/latest/gr/rande.html#glacier_region) in the *AWS General Reference*.

When you create a vault, you must provide a vault name. The following are the vault naming requirements: 

 
+  Names can be between 1 and 255 characters long. 
+ Allowed characters are a–z, A–Z, 0–9, '\_' (underscore), '-' (hyphen), and '.' (period).

Vault names must be unique within an account and the AWS Region in which the vault is being created. That is, an account can create vaults with the same name in different AWS Regions but not in the same AWS Region. 

**Topics**
+ [Creating a Vault in Amazon Glacier Using the AWS SDK for Java](creating-vaults-sdk-java.md)
+ [Creating a Vault in Amazon Glacier Using the AWS SDK for .NET](creating-vaults-dotnet-sdk.md)
+ [Creating a Vault in Amazon Glacier Using the REST API](creating-vaults-rest-api.md)
+ [Creating a Vault Using the Amazon Glacier Console](creating-vaults-console.md)
+ [Creating a Vault in Amazon Glacier Using the AWS Command Line Interface](creating-vaults-cli.md)