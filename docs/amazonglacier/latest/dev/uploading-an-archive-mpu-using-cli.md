

 **This page is only for existing customers of the Amazon Glacier service using Vaults and the original REST API from 2012.**

If you're looking for archival storage solutions, we recommend using the Amazon Glacier storage classes in Amazon S3, S3 Glacier Instant Retrieval, S3 Glacier Flexible Retrieval, and S3 Glacier Deep Archive. To learn more about these storage options, see [Amazon Glacier storage classes](https://aws.amazon.com/s3/storage-classes/glacier/).

Amazon Glacier (original standalone vault-based service) is no longer accepting new customers. Amazon Glacier is a standalone service with its own APIs that stores data in vaults and is distinct from Amazon S3 and the Amazon S3 Glacier storage classes. Your existing data will remain secure and accessible in Amazon Glacier indefinitely. No migration is required. For low-cost, long-term archival storage, AWS recommends the [Amazon S3 Glacier storage classes](https://aws.amazon.com/s3/storage-classes/glacier/), which deliver a superior customer experience with S3 bucket-based APIs, full AWS Region availability, lower costs, and AWS service integration. If you want enhanced capabilities, consider migrating to Amazon S3 Glacier storage classes by using our [AWS Solutions Guidance for transferring data from Amazon Glacier vaults to Amazon S3 Glacier storage classes](https://aws.amazon.com/solutions/guidance/data-transfer-from-amazon-s3-glacier-vaults-to-amazon-s3/).

# Uploading Large Archives by Using the AWS CLI
<a name="uploading-an-archive-mpu-using-cli"></a>

You can upload an archive in Amazon Glacier (Amazon Glacier) by using the AWS Command Line Interface (AWS CLI). To improve the upload experience for larger archives, Amazon Glacier provides several API operations to support multipart uploads. By using these API operations, you can upload archives in parts. These parts can be uploaded independently, in any order, and in parallel. If a part upload fails, you need to upload only that part again, not the entire archive. You can use multipart uploads for archives from 1 byte to about 40,000 gibibytes (GiB) in size. 

For more information about Amazon Glacier multipart uploads, see [Uploading Large Archives in Parts (Multipart Upload)](uploading-archive-mpu.md).

**Topics**
+ [(Prerequisite) Setting Up the AWS CLI](#Creating-Vaults-CLI-Setup)
+ [(Prerequisite) Install Python](#Uploading-Archives-mpu-CLI-Install-Python)
+ [(Prerequisite) Create an Amazon Glacier Vault](#Uploading-Archives-mpu-CLI-Create-Vault)
+ [Example: Uploading Large Archives in Parts by Using the AWS CLI](#Uploading-Archives-mpu-CLI-Implementation)

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

## (Prerequisite) Install Python
<a name="Uploading-Archives-mpu-CLI-Install-Python"></a>

To complete a multipart upload, you must calculate the SHA256 tree hash of the archive that you're uploading. Doing so is different than calculating the SHA256 tree hash of the file that you want to upload. To calculate the SHA256 tree hash of the archive that you're uploading, you can use Java, C\# (with .NET), or Python. In this example, you will use Python. For instructions on using Java or C\#, see [Computing Checksums](checksum-calculations.md). 

For more information about installing Python, see [Install or update Python](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/quickstart.html#installation) in the *Boto3 Developer Guide*.

## (Prerequisite) Create an Amazon Glacier Vault
<a name="Uploading-Archives-mpu-CLI-Create-Vault"></a>

To use the following example, you must have at least one Amazon Glacier vault created. For more information about creating vaults, see [Creating a Vault in Amazon Glacier](creating-vaults.md).

## Example: Uploading Large Archives in Parts by Using the AWS CLI
<a name="Uploading-Archives-mpu-CLI-Implementation"></a>

In this example, you will create a file and use multipart upload API operations to upload this file, in parts, to Amazon Glacier.
**Important**  
Before starting this procedure, make sure that you've performed all of the prerequisite steps. To upload an archive, you must have a vault created, the AWS CLI configured, and be prepared to use Java, C\#, or Python to calculate a SHA256 tree hash.

The following procedure uses the `initiate-multipart-upload`, `upload-multipart-part`, and `complete-multipart-upload` AWS CLI commands. 

For more detailed information about each of these commands, see [initiate-multipart-upload](https://docs.aws.amazon.com/cli/latest/reference/glacier/initiate-multipart-upload.html), [upload-multipart-part](https://docs.aws.amazon.com/cli/latest/reference/glacier/upload-multipart-part.html), and [complete-multipart-upload](https://docs.aws.amazon.com/cli/latest/reference/glacier/complete-multipart-upload.html) in the *AWS CLI Command Reference*.

1. Use the [initiate-multipart-upload](https://docs.aws.amazon.com/cli/latest/reference/glacier/initiate-multipart-upload.html) command to create a multipart upload resource. In your request, specify the part size in number of bytes. Each part that you upload, except the last part, will be this size. You don't need to know the overall archive size when initiating an upload. However, you will need the total size, in bytes, of each part when completing the upload on the final step.

   In the following command, replace the values for the `--vault-name` and `--account-ID` parameters with your own information. This command specifies that you will upload an archive with a part size of 1 mebibyte (MiB) (1024 x 1024 bytes) per file. Replace this `--part-size` parameter value if needed. 

   ```
   aws glacier initiate-multipart-upload --vault-name {{awsexamplevault}} --part-size {{1048576}} --account-id {{123456789012}}
   ```

   Expected output:

   ```
   {
   "location": "/{{123456789012}}/vaults/{{awsexamplevault}}/multipart-uploads/{{uploadId}}",
   "uploadId": "{{uploadId}}"
   }
   ```

   When finished, the command will output the multipart upload resource's upload ID and location in Amazon Glacier. You will use this upload ID in subsequent steps.

1. For this example, you can use the following commands to create a 4.4 MiB file, split it into 1 MiB chunks, and upload each chunk. To upload your own files, you can follow a similar procedure of splitting your data into chunks and uploading each part. 

   

**Linux or macOS**  
The following command creates a 4.4 MiB file, named `file_to_upload`, on Linux or macOS.

   ```
   mkfile -n 9000b {{file_to_upload}}
   ```

**Windows**  
The following command creates a 4.4 MiB file, named `file_to_upload`, on Windows.

   ```
   fsutil file createnew {{file_to_upload}} 4608000
   ```

1. Next, you will split this file into 1 MiB chunks. 

   ```
   split -b 1048576 {{file_to_upload}} chunk
   ```

   You now have the following five chunks. The first four are 1 MiB, and the last is approximately 400 kibibytes (KiB). 

   ```
   chunkaa
   chunkab
   chunkac
   chunkad
   chunkae
   ```

1. Use the [upload-multipart-part](https://docs.aws.amazon.com/cli/latest/reference/glacier/upload-multipart-part.html) command to upload a part of an archive. You can upload archive parts in any order. You can also upload them in parallel. You can upload up to 10,000 parts for a multipart upload.

   In the following command, replace the values for the `--vault-name`, `--account-ID`, and `--upload-id` parameters. The upload ID must match the ID given as output of the `initiate-multipart-upload` command. The `--range` parameter specifies that you will upload a part with a size of 1 MiB (1024 x 1024 bytes). This size must match what you specified in the `initiate-multipart-upload` command. Adjust this size value if needed. The `--body` parameter specifies the name of the part that you're uploading.

   ```
   aws glacier upload-multipart-part --body {{chunkaa}} --range={{'bytes 0-1048575/*'}} --vault-name {{awsexamplevault}} --account-id {{123456789012}} --upload-id {{upload_ID}}
   ```

   If successful, the command will produce output that contains the checksum for the uploaded part.

1. Run the `upload-multipart-part` command again to upload the remaining parts of your multipart upload. Update the `--range` and `–-body` parameter values for each command to match the part that you're uploading. 

   ```
   aws glacier upload-multipart-part --body {{chunkab}} --range={{'bytes 1048576-2097151/*'}} --vault-name {{awsexamplevault}} --account-id {{123456789012}} --upload-id {{upload_ID}}
   ```

   ```
   aws glacier upload-multipart-part --body {{chunkac}} --range={{'bytes 2097152-3145727/*'}} --vault-name {{awsexamplevault}} --account-id {{123456789012}} --upload-id {{upload_ID}}
   ```

   ```
   aws glacier upload-multipart-part --body {{chunkad}} --range={{'bytes 3145728-4194303/*'}} --vault-name {{awsexamplevault}} --account-id {{123456789012}} --upload-id {{upload_ID}}
   ```

   ```
   aws glacier upload-multipart-part --body {{chunkae}} --range={{'bytes 4194304-4607999/*'}} --vault-name {{awsexamplevault}} --account-id {{123456789012}} --upload-id {{upload_ID}}
   ```
**Note**  
The final command's `--range` parameter value is smaller because the final part of our upload is less than 1 MiB. If successful, each command will produce output that contains the checksum for each uploaded part.

1. Next, you will assemble the archive and finish the upload. You must include the total size and SHA256 tree hash of the archive.

   To calculate the SHA256 tree hash of the archive, you can use Java, C\#, or Python. In this example, you will use Python. For instructions on using Java or C\#, see [Computing Checksums](checksum-calculations.md).

   Create the Python file `checksum.py` and insert the following code. If needed, replace the name of the original file.

   ```
   from botocore.utils import calculate_tree_hash
   					
   checksum = calculate_tree_hash(open('{{file_to_upload}}', 'rb'))
   print(checksum)
   ```

1. Run `checksum.py` to calculate the SHA256 tree hash. The following hash may not match your output.

   ```
   $ python3 checksum.py
   $ 3d760edb291bfc9d90d35809243de092aea4c47b308290ad12d084f69988ae0c
   ```

1. Use the [complete-multipart-upload](https://docs.aws.amazon.com/cli/latest/reference/glacier/complete-multipart-upload.html) command to finish the archive upload. Replace the values for the `--vault-name`, `--account-ID`, `--upload-ID`, and `--checksum` parameters. The `--archive` parameter value specifies the total size, in bytes, of the archive. This value must be the sum of all the sizes of the individual parts that you uploaded. Replace this value if needed. 

   ```
   aws glacier complete-multipart-upload --archive-size {{4608000}} --vault-name {{awsexamplevault}} --account-id {{123456789012}} --upload-id {{upload_ID}} --checksum {{checksum}}
   ```

   When finished, the command will output the archive's ID, checksum, and location in Amazon Glacier. 