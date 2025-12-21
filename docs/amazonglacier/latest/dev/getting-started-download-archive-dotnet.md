**This page is only for existing customers of the Amazon Glacier service using Vaults and the original REST API from 2012.**

If you're looking for archival storage solutions, we recommend using the Amazon Glacier storage classes in Amazon S3, S3 Glacier Instant Retrieval, S3 Glacier Flexible Retrieval, and S3 Glacier Deep Archive. To learn more about these storage options, see [Amazon Glacier storage classes](https://aws.amazon.com/s3/storage-classes/glacier/ "https://aws.amazon.com/s3/storage-classes/glacier/").

Amazon Glacier (original standalone vault-based service) is no longer accepting new customers. Amazon Glacier is a standalone service with its own APIs that stores data in vaults and is distinct from Amazon S3 and the Amazon S3 Glacier storage classes. Your existing data will remain secure and accessible in Amazon Glacier indefinitely. No migration is required. For low-cost, long-term archival storage, AWS recommends the [Amazon S3 Glacier storage classes](https://aws.amazon.com/s3/storage-classes/glacier/ "https://aws.amazon.com/s3/storage-classes/glacier/"), which deliver a superior customer experience with S3 bucket-based APIs, full AWS Region availability, lower costs, and AWS service integration. If you want enhanced capabilities, consider migrating to Amazon S3 Glacier storage classes by using our [AWS Solutions Guidance for transferring data from Amazon Glacier vaults to Amazon S3 Glacier storage classes](https://aws.amazon.com/solutions/guidance/data-transfer-from-amazon-s3-glacier-vaults-to-amazon-s3/ "https://aws.amazon.com/solutions/guidance/data-transfer-from-amazon-s3-glacier-vaults-to-amazon-s3/").

# Download an Archive from a Vault in

Amazon Glacier by Using the AWS SDK for .NET

The following C# code example uses the high-level API of the AWS SDK for .NET to download the
archive that you uploaded previously in [Upload an Archive to a Vault in Amazon Glacier by
Using the AWS SDK for .NET](getting-started-upload-archive-dotnet.md "getting-started-upload-archive-dotnet.md"). In the code
example, note the following:

- The example creates an instance of the
  `ArchiveTransferManager` class for the specified
  Amazon Glacier Region endpoint.
- The code example uses the US West (Oregon) Region
  (`us-west-2`) to match the location where you
  created the vault previously in [Step 2: Create a Vault in Amazon Glacier](getting-started-create-vault.md "getting-started-create-vault.md").
- The example uses the `Download` API operation of the
  `ArchiveTransferManager` class to download your
  archive. The example creates an Amazon Simple Notification Service (Amazon SNS) topic, and an
  Amazon Simple Queue Service (Amazon SQS) queue that is subscribed to that topic. If you
  created an AWS Identity and Access Management (IAM) admin user as instructed in [Step 1: Before You Begin with Amazon Glacier](getting-started-before-you-begin.md "getting-started-before-you-begin.md"), your
  user has the necessary IAM permissions for the creation and use of
  the Amazon SNS topic and Amazon SQS queue.
- The example then initiates the archive retrieval job and polls the
  queue for the archive to be available. When the archive is
  available, the download begins. For information about retrieval
  times, see [Archive
  Retrieval Options](downloading-an-archive-two-steps.md#api-downloading-an-archive-two-steps-retrieval-options "downloading-an-archive-two-steps.md#api-downloading-an-archive-two-steps-retrieval-options").
  For step-by-step instructions on how to run this example, see [Running Code Examples](using-aws-sdk-for-dot-net.md#setting-up-and-testing-sdk-dotnet "using-aws-sdk-for-dot-net.md#setting-up-and-testing-sdk-dotnet"). You must update the code as shown with the
  archive ID of the file that you uploaded in [Step 3: Upload an Archive to a Vault in
  Amazon Glacier](getting-started-upload-archive.md "getting-started-upload-archive.md").

###### Example — Download an Archive by

Using the High-Level API of the AWS SDK for .NET

```
using System;
using Amazon.Glacier;
using Amazon.Glacier.Transfer;
using Amazon.Runtime;

namespace glacier.amazon.com.docsamples
{
    class ArchiveDownloadHighLevel_GettingStarted
    {
        static string vaultName = "examplevault";
        static string archiveId = "*** Provide archive ID ***";
        static string downloadFilePath = "*** Provide the file name and path to where to store the download ***";

        public static void Main(string[] args)
        {
            try
            {
                var manager = new ArchiveTransferManager(Amazon.RegionEndpoint.USWest2);

                var options = new DownloadOptions();
                options.StreamTransferProgress += ArchiveDownloadHighLevel_GettingStarted.progress;
                // Download an archive.
                Console.WriteLine("Intiating the archive retrieval job and then polling SQS queue for the archive to be available.");
                Console.WriteLine("Once the archive is available, downloading will begin.");
                manager.Download(vaultName, archiveId, downloadFilePath, options);
                Console.WriteLine("To continue, press Enter");
                Console.ReadKey();
            }
            catch (AmazonGlacierException e) { Console.WriteLine(e.Message); }
            catch (AmazonServiceException e) { Console.WriteLine(e.Message); }
            catch (Exception e) { Console.WriteLine(e.Message); }
            Console.WriteLine("To continue, press Enter");
            Console.ReadKey();
        }

        static int currentPercentage = -1;
        static void progress(object sender, StreamTransferProgressArgs args)
        {
            if (args.PercentDone != currentPercentage)
            {
                currentPercentage = args.PercentDone;
                Console.WriteLine("Downloaded {0}%", args.PercentDone);
            }
        }
    }
}
```
