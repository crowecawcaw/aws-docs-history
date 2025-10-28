# Tutorial: Upload an object through multipart upload and

verify its data integrity

Multipart upload allows you to upload a single object as a set of parts. Each part is a
contiguous portion of the object's data. You can upload these object parts independently and
in any order. If transmission of any part fails, you can retransmit that part without
affecting other parts. After all parts of your object are uploaded, Amazon S3 assembles these
parts and creates the object. In general, when your object size reaches 100 MB, you should
consider using multipart uploads instead of uploading the object in a single operation. For
more information about multipart uploads, see [Uploading and copying objects using multipart upload in Amazon S3](mpuoverview.md "mpuoverview.md"). For limits related to multipart
uploads, see [Amazon S3 multipart upload limits](qfacts.md "qfacts.md").

You can use checksums to verify that assets are not altered when they are copied.
Performing a checksum consists of using an algorithm to iterate sequentially over every byte
in a file. Amazon S3 offers multiple checksum options for checking the integrity of data. We
recommend that you perform these integrity checks as a durability best practice and to
confirm that every byte is transferred without alteration. Amazon S3 also supports the following
algorithms: SHA-1, SHA-256, CRC32, and CRC32C. Amazon S3 uses one or more of these algorithms to
compute an additional checksum value and store it as part of the object metadata. For more
information about checksums, see [Checking object integrity in Amazon S3](checking-object-integrity.md "checking-object-integrity.md").

###### Objective

In this tutorial, you will learn how to upload an object to Amazon S3 by using a multipart
upload and an additional SHA-256 checksum through the AWS Command Line Interface (AWS
CLI). You’ll also learn how to check the object’s data integrity by calculating the MD5
hash and SHA-256 checksum of the uploaded object.

###### Topics

- [Prerequisites](#mpu-prerequisites "#mpu-prerequisites")
- [Step 1: Create a large file](#create-large-file-step1 "#create-large-file-step1")
- [Step 2: Split the file into multiple
  files](#split-large-file-step2 "#split-large-file-step2")
- [Step 3: Create the multipart upload with
  an additional checksum](#create-multipart-upload-step3 "#create-multipart-upload-step3")
- [Step 4: Upload the parts of your multipart
  upload](#upload-parts-step4 "#upload-parts-step4")
- [Step 5: List all the parts of your multipart
  upload](#list-parts-step5 "#list-parts-step5")
- [Step 6: Complete the multipart
  upload](#complete-multipart-upload-step6 "#complete-multipart-upload-step6")
- [Step 7: Confirm that the object is uploaded to
  your bucket](#confirm-upload-step7 "#confirm-upload-step7")
- [Step 8: Verify object integrity with an MD5
  checksum](#verify-object-integrity-step8 "#verify-object-integrity-step8")
- [Step 9: Verify object integrity
  with an additional checksum](#verify-object-integrity-sha256-step9 "#verify-object-integrity-sha256-step9")
- [Step 10: Clean up your resources](#clean-up-step10 "#clean-up-step10")

## Prerequisites

- Before you start this tutorial, make sure that you have access to an Amazon S3
  bucket that you can upload to. For more information, see [Creating a general purpose bucket](create-bucket-overview.md "create-bucket-overview.md").
- You must have the AWS CLI installed and configured. If you don’t have the
  AWS CLI installed, see [Install or update
  to the latest version of the AWS CLI](../../../cli/latest/userguide/getting-started-install.md "../../../cli/latest/userguide/getting-started-install.md") in the
  _AWS Command Line Interface User Guide_.
- Alternatively, you can run AWS CLI commands from the console by using
  AWS CloudShell. AWS CloudShell is a browser-based, pre-authenticated shell that you can
  launch directly from the AWS Management Console. For more information, see [What is CloudShell?](../../../cloudshell/latest/userguide/welcome.md "../../../cloudshell/latest/userguide/welcome.md") and [Getting started with AWS CloudShell](../../../cloudshell/latest/userguide/getting-started.md "../../../cloudshell/latest/userguide/getting-started.md") in the _AWS CloudShell User Guide_.

## Step 1: Create a large file

If you already have a file ready for upload, you can use the file for this tutorial.
Otherwise, create a 15 MB file using the following steps. For limits related to
multipart uploads, see [Amazon S3 multipart upload limits](qfacts.md "qfacts.md").

**To create a large file**

Use one of the following commands to create your file, depending on which operating
system you're using.

###### Linux or macOS

To create a 15 MB file, open your local terminal and run the following command:

```
dd if=/dev/urandom of=census-data.bin bs=1M count=15
```

This command creates a file named `census-data.bin` filled with
random bytes, with a size of 15 MB.

###### Windows

To create a 15 MB file, open your local terminal and run the following
command:

```
fsutil file createnew census-data.bin 15728640
```

This command creates a file named `census-data.bin` with a size of
15 MB of arbitrary data (15728640 bytes).

## Step 2: Split the file into multiple

files

To perform the multipart upload, you have to split your large file into smaller parts. You can then upload the smaller
parts by using the multipart upload process. This step demonstrates how to split the
large file created in [Step 1](#create-large-file-step1 "#create-large-file-step1") into smaller
parts. The following example uses a 15 MB file named
`census-data.bin`.

**To split a large file into parts**

###### Linux or macOS

To divide the large file into 5 MB parts, use the `split` command. Open your
terminal and run the following:

```
split -b 5M -d census-data.bin census-part
```

This command splits `census-data.bin` into 5 MB parts named
`census-part**`, where `**` is a numeric suffix starting from
`00`.

###### Windows

To split the large file, use PowerShell. Open [Powershell](https://learn.microsoft.com/en-us/powershell/ "https://learn.microsoft.com/en-us/powershell/"), and run the
following script:

```

$inputFile = "census-data.bin"
$outputFilePrefix = "census-part"
$chunkSize = 5MB

$fs = [System.IO.File]::OpenRead($inputFile)
$buffer = New-Object byte[] $chunkSize
$fileNumber = 0

while ($fs.Position -lt $fs.Length) {
$bytesRead = $fs.Read($buffer, 0, $chunkSize)
$outputFile = "{0}{1:D2}" -f $outputFilePrefix, $fileNumber
$fileStream = [System.IO.File]::Create($outputFile)
$fileStream.Write($buffer, 0, $bytesRead)
$fileStream.Close()
$fileNumber++
}

$fs.Close()

```

This PowerShell script reads the large file in chunks of 5 MB and writes each chunk to
a new file with a numeric suffix.

After running the appropriate command, you should see the parts in the directory where
you executed the command. Each part will have a suffix corresponding to its part number,
for example:

```
census-part00 census-part01 census-part02
```

## Step 3: Create the multipart upload with

an additional checksum

To begin the multipart upload process, you need to create the multipart upload
request. This step involves initiating the multipart upload and specifying an additional
checksum for data integrity. The following example uses the SHA-256 checksum. If you want to
provide any metadata describing the object being uploaded, you must provide it in the
request to initiate the multipart upload.

###### Note

In this step and subsequent steps, this tutorial uses the SHA-256 additional
algorithm. You might optionally use another additional checksum for these steps,
such as CRC32, CRC32C, or SHA-1. If you use a different algorithm, you must use it
throughout the tutorial steps.

**To start the multipart upload**

In your terminal, use the following `create-multipart-upload` command to
start a multipart upload for your bucket. Replace
`amzn-s3-demo-bucket1` with your actual
bucket name. Also, replace the `census_data_file` with your chosen
file name. This file name becomes the object key when the upload completes.

```
aws s3api create-multipart-upload --bucket `amzn-s3-demo-bucket1` --key '`census_data_file`' --checksum-algorithm sha256
```

If your request succeeds, you'll see JSON output like the following:

```

{
    "ServerSideEncryption": "AES256",
    "ChecksumAlgorithm": "SHA256",
    "Bucket": "`amzn-s3-demo-bucket1`",
    "Key": "census_data_file",
    "UploadId": "cNV6KCSNANFZapz1LUGPC5XwUVi1n6yUoIeSP138sNOKPeMhpKQRrbT9k0ePmgoOTCj9K83T4e2Gb5hQvNoNpCKqyb8m3.oyYgQNZD6FNJLBZluOIUyRE.qM5yhDTdhz"
}

```

###### Note

When you send a request to initiate a multipart upload, Amazon S3 returns a
response with an upload ID, which is a unique identifier for your multipart upload.
You must include this upload ID whenever you upload parts, list the parts, complete
an upload, or stop an upload. You'll need to use the
`UploadId`, `Key`, and
`Bucket` values for later steps, so make sure to save
these.

Also, if you’re using multipart upload with additional checksums, the part numbers
must be consecutive. If you use nonconsecutive part numbers, the
`complete-multipart-upload` request can result in an HTTP `500
 Internal Server Error`.

## Step 4: Upload the parts of your multipart

upload

In this step, you will upload the parts of your multipart upload to your S3 bucket. Use
the `upload-part` command to upload each part individually. This
process requires specifying the upload ID, the part number, and the file to be uploaded
for each part.

###### To upload the parts

1. When uploading a part, in addition to the upload ID, you must specify a part
   number by using the `--part-number` argument. You can choose any part
   number between 1 and 10,000. A part number uniquely identifies a part and its
   position in the object you are uploading. The part number that you choose must
   be in a consecutive sequence (for example, it can be 1, 2, or 3). If you upload
   a new part using the same part number as a previously uploaded part, the
   previously uploaded part is overwritten.
2. Use the `upload-part` command to upload each part of your multipart
   upload. The `--upload-id` is the same as it was in the output created
   by the `create-multipart-upload` command in [Step 3](#create-multipart-upload-step3 "#create-multipart-upload-step3"). To upload the first
   part of your data, use the following command:

```
aws s3api upload-part --bucket `amzn-s3-demo-bucket1` --key '`census_data_file`' --part-number `1` --body `census-part00` --upload-id "`cNV6KCSNANFZapz1LUGPC5XwUVi1n6yUoIeSP138sNOKPeMhpKQRrbT9k0ePmgoOTCj9K83T4e2Gb5hQvNoNpCKqyb8m3.oyYgQNZD6FNJLBZluOIUyRE.qM5yhDTdhz`" --checksum-algorithm `SHA256`
```

Upon completion of each `upload-part` command, you should see
output like the following example:

```

{
    "ServerSideEncryption": "AES256",
    "ETag": "\"e611693805e812ef37f96c9937605e69\"",
    "ChecksumSHA256": "QLl8R4i4+SaJlrl8ZIcutc5TbZtwt2NwB8lTXkd3GH0="
}

```

3. For subsequent parts, increment the part number accordingly:

```
aws s3api upload-part --bucket `amzn-s3-demo-bucket1` --key '`census_data_file`' --part-number `<part-number>` --body <file-path> --upload-id "<your-upload-id>" --checksum-algorithm SHA256
```

For example, use the following command to upload the second part:

```
aws s3api upload-part --bucket `amzn-s3-demo-bucket1` --key 'census_data_file' --part-number 2 --body census-part01 --upload-id "cNV6KCSNANFZapz1LUGPC5XwUVi1n6yUoIeSP138sNOKPeMhpKQRrbT9k0ePmgoOTCj9K83T4e2Gb5hQvNoNpCKqyb8m3.oyYgQNZD6FNJLBZluOIUyRE.qM5yhDTdhz" --checksum-algorithm SHA256
```

Amazon S3 returns an entity tag (ETag) and additional checksums for each
uploaded part as a header in the response. 4. Continue using the `upload-part` command until you have
uploaded all the parts of your object.

## Step 5: List all the parts of your multipart

upload

To complete the multipart upload, you will need a list of all the parts that have been
uploaded for that specific multipart upload. The output from the `list-parts`
command provides information such as bucket name, key, upload ID, part number, ETag,
additional checksums, and more. It’s helpful to save this output in a file so that you
can use it for the next step when completing the multipart upload process. You can
create a JSON output file called `parts.json` by using the following
method.

###### To create a file that lists all of the parts

1. To generate a JSON file with the details of all the uploaded parts, use the
   following `list-parts` command. Replace
   `amzn-s3-demo-bucket1` with your actual bucket
   name and `<your-upload-id>` with the upload ID that you
   received in [Step 3](#create-multipart-upload-step3 "#create-multipart-upload-step3"). For
   more information on the `list-parts` command, see [list-parts](../../../cli/latest/reference/s3api/list-parts.md "../../../cli/latest/reference/s3api/list-parts.md") in the _AWS Command Line Interface User Guide_.

```
aws s3api list-parts --bucket `amzn-s3-demo-bucket1` --key '`census_data_file`' --upload-id `<your-upload-id>` --query '{Parts: Parts[*].{PartNumber: PartNumber, ETag: ETag, ChecksumSHA256: ChecksumSHA256}}' --output json > parts.json
```

A new file called `parts.json` is generated. The file contains the
JSON formatted information for all of your uploaded parts. The
`parts.json` file includes essential information for each
part of your multipart upload, such as the part numbers and their corresponding
ETag values, which are necessary for completing the multipart upload
process. 2. Open `parts.json` by using any text editor or through the terminal.
Here’s the example output:

```

{
    "Parts": [
        {
            "PartNumber": 1,
            "ETag": "\"3c3097f89e2a2fece47ac54b243c9d97\"",
            "ChecksumSHA256": "fTPVHfyNHdv5VkR4S3EewdyioXECv7JBxN+d4FXYYTw="
        },
        {
            "PartNumber": 2,
            "ETag": "\"03c71cc160261b20ab74f6d2c476b450\"",
            "ChecksumSHA256": "VDWTa8enjOvULBAO3W2a6C+5/7ZnNjrnLApa1QVc3FE="
        },
        {
            "PartNumber": 3,
            "ETag": "\"81ae0937404429a97967dffa7eb4affb\"",
            "ChecksumSHA256": "cVVkXehUlzcwrBrXgPIM+EKQXPUvWist8mlUTCs4bg8="
        }
    ]
}

```

## Step 6: Complete the multipart

upload

After uploading all parts of your multipart upload and listing them, the final step is
to complete the multipart upload. This step merges all the uploaded parts into a single
object in your S3 bucket.

###### Note

You can calculate the object checksum before calling
`complete-multipart-upload` by including
`--checksum-sha256` in your request. If the checksums don't match,
Amazon S3 fails the request. For more information, see [complete-multipart-upload](../../../cli/latest/reference/s3api/complete-multipart-upload.md "../../../cli/latest/reference/s3api/complete-multipart-upload.md") in the
_AWS Command Line Interface User Guide_.

**To complete the multipart upload**

To finalize the multipart upload, use the `complete-multipart-upload`
command. This command requires the `parts.json` file created in [Step 5](#list-parts-step5 "#list-parts-step5"), your bucket name, and the upload ID.
Replace `<`amzn-s3-demo-bucket1`>` with your bucket name and
`<your-upload-id>` with the upload ID of
`parts.json`.

```
aws s3api complete-multipart-upload --multipart-upload file://parts.json --bucket `amzn-s3-demo-bucket1` --key 'census_data_file' --upload-id <your-upload-id>
```

Here’s the example output:

```

{
    "ServerSideEncryption": "AES256",
    "Location": "https://`amzn-s3-demo-bucket1`.s3.us-east-2.amazonaws.com/census_data_file",
    "Bucket": "`amzn-s3-demo-bucket1`",
    "Key": "census_data_file",
    "ETag": "\"f453c6dccca969c457efdf9b1361e291-3\"",
    "ChecksumSHA256": "aI8EoktCdotjU8Bq46DrPCxQCGuGcPIhJ51noWs6hvk=-3"
}

```

###### Note

Don't delete the individual part files yet. You will need the individual
parts so that you can perform checksums on them to verify the integrity of the
merged-together object.

## Step 7: Confirm that the object is uploaded to

your bucket

After completing the multipart upload, you can verify that the object has been
successfully uploaded to your S3 bucket. To list the objects in your bucket and confirm the presence of your newly
uploaded file, use the `list-objects-v2`
command

**To list the uploaded object**

To list the objects in your, use the `list-objects-v2` command
bucket. Replace `amzn-s3-demo-bucket1` with your
actual bucket name:

```
aws s3api list-objects-v2 --bucket `amzn-s3-demo-bucket1`
```

This command returns a list of objects in your bucket. Look for your uploaded
file (for example, `census_data_file`) in the list of objects.

For more information, see the [Examples](../../../cli/latest/reference/s3api/list-objects-v2.md "../../../cli/latest/reference/s3api/list-objects-v2.md") section for the `list-objects-v2` command in the _AWS Command Line Interface User Guide_.

## Step 8: Verify object integrity with an MD5

checksum

When you upload an object, you can specify a checksum algorithm for
Amazon S3 to use. By default, Amazon S3 stores the MD5 digest of bytes as the object’s ETag.
For multipart uploads, the ETag is not the checksum for the entire object, but rather a composite of
checksums for each individual part.

###### To verify object integrity by using an MD5 checksum

1. To retrieve the ETag of the uploaded object, perform a
   `head-object` request:

```
aws s3api head-object --bucket `amzn-s3-demo-bucket1` --key `census_data_file`
```

Here’s the example output:

```

{
    "AcceptRanges": "bytes",
    "LastModified": "2024-07-26T19:04:13+00:00",
    "ContentLength": 16106127360,
    "ETag": "\"f453c6dccca969c457efdf9b1361e291-3\"",
    "ContentType": "binary/octet-stream",
    "ServerSideEncryption": "AES256",
    "Metadata": {}
}

```

This ETag has "-3" appended to the end. This indicates that the object was
uploaded in three parts using multipart upload. 2. Next, calculate the MD5 checksum of each part using the
`md5sum` command. Make sure that you provide the correct
path to your part files:

```
md5sum census-part*
```

Here’s the example output:

```

e611693805e812ef37f96c9937605e69 census-part00
63d2d5da159178785bfd6b6a5c635854 census-part01
95b87c7db852451bb38b3b44a4e6d310 census-part02

```

3. For this step, manually combine the MD5 hashes into one string. Then, run the
   following command to convert the string to binary and calculate the MD5 checksum of the
   binary value:

```
echo "`e611693805e812ef37f96c9937605e6963d2d5da159178785bfd6b6a5c63585495b87c7db852451bb38b3b44a4e6d310`" | xxd -r -p | md5sum
```

Here’s the example output:

```
f453c6dccca969c457efdf9b1361e291 -
```

This hash value should match the hash value of the original ETag value in [Step 1](#create-large-file-step1 "#create-large-file-step1"), which validates the integrity of the
`census_data_file` object.

When you instruct Amazon S3 to use additional checksums, Amazon S3 calculates the
checksum value for each part and stores the values. If you want to retrieve the checksum
values for individual parts of multipart uploads that are still in progress, you can use
`list-parts`.

For more information about how checksums work with multipart upload objects, see
[Checking object integrity in Amazon S3](checking-object-integrity.md "checking-object-integrity.md").

## Step 9: Verify object integrity

with an additional checksum

In this step, this tutorial uses SHA-256 as an additional checksum to validate object integrity.
If you’ve used a different additional checksum, use that checksum value instead.

###### To verify object integrity with SHA256

1. Run the following command in your terminal, including the
   `--checksum-mode enabled` argument, to display the
   `ChecksumSHA256` value of your object:

```
aws s3api head-object --bucket `amzn-s3-demo-bucket1` --key census_data_file --checksum-mode enabled
```

Here’s the example output:

```

{
    "AcceptRanges": "bytes",
    "LastModified": "2024-07-26T19:04:13+00:00",
    "ContentLength": 16106127360,
    "ChecksumSHA256": "aI8EoktCdotjU8Bq46DrPCxQCGuGcPIhJ51noWs6hvk=-3",
    "ETag": "\"f453c6dccca969c457efdf9b1361e291-3\"",
    "ContentType": "binary/octet-stream",
    "ServerSideEncryption": "AES256",
    "Metadata": {}
}

```

2. Use the following commands to decode the `ChecksumSHA256` values
   for the individual parts into base64 and save them into a binary file called
   `outfile`. These values can be found in your `parts.json`
   file. Replace the example base64 strings with your actual
   `ChecksumSHA256` values.

```

echo "`QLl8R4i4+SaJlrl8ZIcutc5TbZtwt2NwB8lTXkd3GH0=`" | base64 --decode >> outfile
echo "`xCdgs1K5Bm4jWETYw/CmGYr+m6O2DcGfpckx5NVokvE=`" | base64 --decode >> outfile
echo "`f5wsfsa5bB+yXuwzqG1Bst91uYneqGD3CCidpb54mAo=`" | base64 --decode >> outfile

```

3. Run the following command to calculate the SHA256 checksum of the
   `outfile`:

```
sha256sum outfile
```

Here’s the example output:

```
688f04a24b42768b6353c06ae3a0eb3c2c50086b8670f221279d67a16b3a86f9 outfile
```

In the next step, take the hash value and convert it into a binary value. This binary value should match the `ChecksumSHA256` value from
[Step 1](#create-large-file-step1 "#create-large-file-step1"). 4. Convert the SHA256 checksum from [Step 3](#create-multipart-upload-step3 "#create-multipart-upload-step3") into binary, and then encode it to
base64 to verify that it matches the `ChecksumSHA256` value from [Step 1](#create-large-file-step1 "#create-large-file-step1"):

```
echo "688f04a24b42768b6353c06ae3a0eb3c2c50086b8670f221279d67a16b3a86f9" | xxd -r -p | base64
```

Here’s the example output:

```
aI8EoktCdotjU8Bq46DrPCxQCGuGcPIhJ51noWs6hvk=
```

This output should confirm that the base64 output matches the
`ChecksumSHA256` value from the `head-object`
command output. If the output matches the checksum value, then the object is valid.

###### Important

- When you instruct Amazon S3 to use additional checksums, Amazon S3
  calculates the checksum values for each part and stores these values.
- If you want to retrieve the checksum values for individual parts of
  multipart uploads that are still in progress, you can use the
  `list-parts` command.

## Step 10: Clean up your resources

If you want to clean up the files created in this tutorial, use the following method.
For instructions on deleting the files uploaded to your S3 bucket, see [Deleting Amazon S3 objects](DeletingObjects.md "DeletingObjects.md").

**Delete local files created in [Step 1](#create-large-file-step1 "#create-large-file-step1"):**

To remove the files that you created for your multipart upload, run the following command from your working directory:

```
rm `census-data.bin` census-part* outfile parts.json
```
