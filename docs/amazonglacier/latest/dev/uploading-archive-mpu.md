**This page is only for existing customers of the Amazon Glacier service using Vaults and the original REST API from 2012.**

If you're looking for archival storage solutions, we recommend using the Amazon Glacier storage classes in Amazon S3, S3 Glacier Instant Retrieval, S3 Glacier Flexible Retrieval, and S3 Glacier Deep Archive. To learn more about these storage options, see [Amazon Glacier storage classes](https://aws.amazon.com/s3/storage-classes/glacier/ "https://aws.amazon.com/s3/storage-classes/glacier/").

Amazon Glacier (original standalone vault-based service) is no longer accepting new customers. Amazon Glacier is a standalone service with its own APIs that stores data in vaults and is distinct from Amazon S3 and the Amazon S3 Glacier storage classes. Your existing data will remain secure and accessible in Amazon Glacier indefinitely. No migration is required. For low-cost, long-term archival storage, AWS recommends the [Amazon S3 Glacier storage classes](https://aws.amazon.com/s3/storage-classes/glacier/ "https://aws.amazon.com/s3/storage-classes/glacier/"), which deliver a superior customer experience with S3 bucket-based APIs, full AWS Region availability, lower costs, and AWS service integration. If you want enhanced capabilities, consider migrating to Amazon S3 Glacier storage classes by using our [AWS Solutions Guidance for transferring data from Amazon Glacier vaults to Amazon S3 Glacier storage classes](https://aws.amazon.com/solutions/guidance/data-transfer-from-amazon-s3-glacier-vaults-to-amazon-s3/ "https://aws.amazon.com/solutions/guidance/data-transfer-from-amazon-s3-glacier-vaults-to-amazon-s3/").

# Uploading Large Archives in Parts (Multipart Upload)

###### Topics

- [Multipart Upload Process](#MPUprocess "#MPUprocess")
- [Quick Facts](#qfacts "#qfacts")
- [Uploading Large Archives by Using the
  AWS CLI](uploading-an-archive-mpu-using-cli.md "uploading-an-archive-mpu-using-cli.md")
- [Uploading Large Archives in Parts Using the Amazon SDK for Java](uploading-an-archive-mpu-using-java.md "uploading-an-archive-mpu-using-java.md")
- [Uploading Large Archives Using the AWS SDK for .NET](uploading-an-archive-mpu-using-dotnet.md "uploading-an-archive-mpu-using-dotnet.md")
- [Uploading Large Archives in Parts Using the REST
  API](uploading-an-archive-mpu-using-rest.md "uploading-an-archive-mpu-using-rest.md")

## Multipart Upload Process

As described in [Uploading an Archive in Amazon Glacier](uploading-an-archive.md "uploading-an-archive.md"), we
encourage Amazon Glacier (Amazon Glacier) customers to use Multipart Upload to upload archives greater
than 100 mebibytes (MiB).

1. Initiate Multipart Upload

When you send a request to initiate a multipart upload, Amazon Glacier returns a
multipart upload ID, which is a unique identifier for your multipart upload. Any
subsequent multipart upload operations require this ID. This ID doesn't expire
for at least 24 hours after Amazon Glacier completes the job.

In your request to start a multipart upload, specify the part size
in number of bytes. Each part you upload, except the last part, must be this
size.

###### Note

You don't need to know the overall archive size when using multipart uploads. This means
that you can use multipart uploads in cases where you don't know the
archive size when you start uploading the archive. You only need to decide
the part size at the time you start the multipart upload.

In the initiate multipart upload request, you can also provide an optional
archive description. 2. Upload Parts

For each part upload request, you must include the multipart upload ID you obtained in
step 1. In the request, you must also specify the content range, in bytes,
identifying the position of the part in the final archive. Amazon Glacier later
uses the content range information to assemble the archive in proper sequence.
Because you provide the content range for each part that you upload, it
determines the part's position in the final assembly of the archive, and
therefore you can upload parts in any order. You can also upload parts in
parallel. If you upload a new part using the same content range as a previously
uploaded part, the previously uploaded part is overwritten. 3. Complete (or stop) Multipart Upload

After uploading all the archive parts, you use the complete operation. Again,
you must specify the upload ID in your request. Amazon Glacier creates an archive by
concatenating parts in ascending order based on the content range you provided.
Amazon Glacier response to a Complete Multipart Upload request includes an archive ID
for the newly created archive. If you provided an optional archive description
in the Initiate Multipart Upload request, Amazon Glacier associates it with the
assembled archive. After you successfully complete a multipart upload, you
cannot refer to the multipart upload ID. That means you cannot access parts
associated with the multipart upload ID.

If you stop a multipart upload, you cannot upload any more parts using that
multipart upload ID. All storage consumed by any parts associated with the
stopped multipart upload is freed. If any part uploads were in-progress, they
can still succeed or fail even after stopped.

### Additional Multipart Upload

Operations

Amazon Glacier (Amazon Glacier) provides the following additional multipart upload API calls.

- List Parts—Using this operation, you can list the
  parts of a specific multipart upload. It returns information about the
  parts that you have uploaded for a multipart upload. For each list parts
  request, Amazon Glacier returns information for up to 1,000 parts. If
  there are more parts to list for the multipart upload, the result is
  paginated and a marker is returned in the response at which to continue
  the list. You need to send additional requests to retrieve subsequent
  parts. Note that the returned list of parts doesn't include parts that
  haven't completed uploading.
- List Multipart Uploads—Using this
  operation, you can obtain a list of multipart uploads in progress. An
  in-progress multipart upload is an upload that you have initiated, but have
  not yet completed or stopped. For each list multipart uploads request,
  Amazon Glacier returns up to 1,000 multipart uploads. If there are more multipart
  uploads to list, then the result is paginated and a marker is returned in
  the response at which to continue the list. You need to send additional
  requests to retrieve the remaining multipart uploads.

## Quick Facts

The following table provides multipart upload core specifications.

| Item                                                                                | Specification                                                                                                                                                                                                                                                        |
| ----------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Maximum archive size                                                                | 10,000 x 4 gibibytes (GiB)                                                                                                                                                                                                                                           |
| Maximum number of parts per upload                                                  | 10,000                                                                                                                                                                                                                                                               |
| Part size                                                                           | 1 MiB to 4 GiB, last part can be < 1 MiB. You specify the size value in bytes.<br>The part size must be a mebibyte (1024 kibibytes [KiB]) multiplied by a power of 2. For example,<br>`1048576` (1 MiB), `2097152` (2 MiB),<br>`4194304` (4 MiB), `8388608` (8 MiB). |
| Maximum number of parts returned for a list parts request                           | 1,000                                                                                                                                                                                                                                                                |
| Maximum number of multipart uploads returned in a list multipart<br>uploads request | 1,000                                                                                                                                                                                                                                                                |
