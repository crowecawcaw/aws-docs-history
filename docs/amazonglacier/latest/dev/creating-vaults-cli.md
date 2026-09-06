

 **This page is only for existing customers of the Amazon Glacier service using Vaults and the original REST API from 2012.**

If you're looking for archival storage solutions, we recommend using the Amazon Glacier storage classes in Amazon S3, S3 Glacier Instant Retrieval, S3 Glacier Flexible Retrieval, and S3 Glacier Deep Archive. To learn more about these storage options, see [Amazon Glacier storage classes](https://aws.amazon.com/s3/storage-classes/glacier/).

Amazon Glacier (original standalone vault-based service) is no longer accepting new customers. Amazon Glacier is a standalone service with its own APIs that stores data in vaults and is distinct from Amazon S3 and the Amazon S3 Glacier storage classes. Your existing data will remain secure and accessible in Amazon Glacier indefinitely. No migration is required. For low-cost, long-term archival storage, AWS recommends the [Amazon S3 Glacier storage classes](https://aws.amazon.com/s3/storage-classes/glacier/), which deliver a superior customer experience with S3 bucket-based APIs, full AWS Region availability, lower costs, and AWS service integration. If you want enhanced capabilities, consider migrating to Amazon S3 Glacier storage classes by using our [AWS Solutions Guidance for transferring data from Amazon Glacier vaults to Amazon S3 Glacier storage classes](https://aws.amazon.com/solutions/guidance/data-transfer-from-amazon-s3-glacier-vaults-to-amazon-s3/).

# Creating a Vault in Amazon Glacier Using the AWS Command Line Interface
<a name="creating-vaults-cli"></a>

Follow these steps to create a vault in Amazon Glacier (Amazon Glacier) using the AWS Command Line Interface (AWS CLI).

**Topics**
+ [(Prerequisite) Setting Up the AWS CLI](#Creating-Vaults-CLI-Setup)
+ [Example: Creating a Vault Using the AWS CLI](#Creating-Vaults-CLI-Implementation)

## (Prerequisite) Setting Up the AWS CLI
<a name="Creating-Vaults-CLI-Setup"></a>

1. Download and configure the AWS CLI. For instructions, see the following topics in the *AWS Command Line Interface User Guide*: 

    [Installing the AWS Command Line Interface](https://docs.aws.amazon.com/cli/latest/userguide/installing.html) 

   [Configuring the AWS Command Line Interface](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html)

1. Verify your AWS CLI setup by entering the following commands at the command prompt. These commands don't provide credentials explicitly, so the credentials of the default profile are used.
   + Try using the help command.

     ```
     aws help
     ```
   + To get a list of Amazon Glacier vaults on the configured account, use the `list-vaults` command. Replace {{123456789012}} with your AWS account ID.

     ```
     aws glacier list-vaults --account-id {{123456789012}}
     ```
   + To see the current configuration data for the AWS CLI, use the `aws configure list` command.

     ```
     aws configure list
     ```

## Example: Creating a Vault Using the AWS CLI
<a name="Creating-Vaults-CLI-Implementation"></a>

1. Use the `create-vault` command to create a vault named {{awsexamplevault}} under account {{111122223333}}.

   ```
   aws glacier create-vault --vault-name {{awsexamplevault}} --account-id {{111122223333}}
   ```

   Expected output:

   ```
   {
       "location": "/{{111122223333}}/vaults/{{awsexamplevault}}"
   }
   ```

1. Verify creation using the `describe-vault` command.

   ```
   aws glacier describe-vault --vault-name {{awsexamplevault}} --account-id {{111122223333}}
   ```