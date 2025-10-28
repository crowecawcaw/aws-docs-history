AWS HealthOmics variant stores and annotation stores will no longer be open to new customers starting
November 7th, 2025. If you would like to use variant stores or annotation stores,
sign up prior to that date. Existing customers can continue to use the service as normal. For more information, see
[AWS HealthOmics variant store and annotation store availability change](variant-store-availability-change.md "variant-store-availability-change.md").

# Accessing HealthOmics read sets with Amazon S3 URIs

You can use Amazon S3 URI paths to access your active sequence store read sets.

With the Amazon S3 URI path, you can use Amazon S3 operations to list, share, and download your read sets. Access through
the S3 APIs accelerates collaboration and tool integration given many industry tools are built already to read from
S3. In addition, you can share access to the S3 APIs with other accounts and provide cross-region read access to
data.

HealthOmics doesn't support Amazon S3 URI access to archived read sets. When you activate a read set, it's restored to the
same URI path each time.

With data loaded into HealthOmics stores, because the Amazon S3 URI is based on Amazon S3 access points, you can
directly integrate with industry standard tools that read Amazon S3 URIs, such as the following:

- Visual analysis applications such as Integrative Genomics Viewer (IGV) or
  UCSC Genome Browser.
- Common workflows with Amazon S3 extensions such as CWL, WDL, and
  Nextflow.
- Any tool that can authenticate and read from access point Amazon S3 URIs or read presigned Amazon S3
  URIs.
- Amazon S3 utilities such as Mountpoint or CloudFront.
  Amazon S3 Mountpoint makes it possible for you to use an Amazon S3 bucket as a local file system. To learn more
  about Mountpoint and to install it for use, see [Mountpoint
  for Amazon S3](https://github.com/awslabs/mountpoint-s3 "https://github.com/awslabs/mountpoint-s3").

Amazon CloudFront is a content delivery network (CDN) service built for high performance, security,
and developer convenience. To learn more about using Amazon CloudFront, see[the Amazon CloudFront documentation](../../../cloudfront.md "../../../cloudfront.md"). To set up
CloudFront with a sequence store, contact the AWS HealthOmics team.

The data owner root account is enabled for the actions S3:GetObject, S3:GetObjectTagging, and S3:List
Bucket on the sequence store prefix. For a user in the account to access the data, you create an IAM policy and
attach it to the user or role. For an example policy, see [Permissions for data access using Amazon S3 URIs](s3-sharing.md "s3-sharing.md").

You can use the following Amazon S3 API operations on the active read sets to list and retrieve your data.
You can access archived read sets through Amazon S3 URIs after they have been activated.

- [GetObject](../../../AmazonS3/latest/API/API_GetObject.md "../../../AmazonS3/latest/API/API_GetObject.md")— Retrieves an object from Amazon S3.
- [HeadObject](../../../AmazonS3/latest/API/API_HeadObject.md "../../../AmazonS3/latest/API/API_HeadObject.md")— The HEAD operation retrieves metadata from an object without returning the
  object itself. This operation is useful if you only want an object's metadata.
- [ListObjects and ListObject v2](../../../AmazonS3/latest/API/API_ListObjects.md "../../../AmazonS3/latest/API/API_ListObjects.md")— Returns some or all (up
  to 1,000) of the objects in a bucket.
- [CopyObject](../../../AmazonS3/latest/API/API_CopyObject.md "../../../AmazonS3/latest/API/API_CopyObject.md")— Creates a copy of an object that's already stored in Amazon S3. HealthOmics
  supports copying to an Amazon S3 access point, but not writing to an access point.
  HealthOmics sequence stores maintain the semantic identity of files through ETags. Throughout a lifecycle of
  a file, the Amazon S3 ETag, which is based on bitwise identity, may change, however, the HealthOmics ETag remains the same. To
  learn more, see [HealthOmics ETags and data provenance](etags-and-provenance.md "etags-and-provenance.md").

###### Topics

- [Amazon S3 URI structure in HealthOmics
  storage](#s3-uri-structure "#s3-uri-structure")
- [Using Hosted or Local IGV to access read
  sets](#s3-access-igv "#s3-access-igv")
- [Using Samtools or HTSlib in HealthOmics](#s3-access-Samtools "#s3-access-Samtools")
- [Using Mountpoint HealthOmics](#s3-access-Mountpoint "#s3-access-Mountpoint")
- [Using CloudFront with HealthOmics](#s3-access-CloudFront "#s3-access-CloudFront")

## Amazon S3 URI structure in HealthOmics

storage

All files with Amazon S3 URIs have `omics:subjectId` and `omics:sampleId`
resource tags. You can use these tags to share access by using IAM policies through a pattern such as
`"s3:ExistingObjectTag/omics:subjectId": "pattern desired"`.

The file structure is as follows:

`.../`account_id`/sequenceStore/`seq_store_id`/readSet/`read_set_id`/`files`.`

For files imported into sequence stores from Amazon S3, the sequence store attempts to maintain the
original source name. When the names conflict, the system appends read set information to ensure that the file
names are unique. For instance, for fastq read sets, if both file names are the same, to make the names
unique, `sourceX` is inserted before .fastq.gz or .fq.gz. For a direct upload, the file names
follow the following patterns:

- For FASTQ—
  `read_set_name`\_`sourcex`.fastq.gz
- For uBAM/BAM/CRAM—
  `read_set_name`.`file
extension` with extensions of `.bam` or
  `.cram`. An example is `NA193948.bam`.

For read sets that are BAM or CRAM, index files are automatically generated during the ingestion
process. For the index files generated, the proper index extension at the end of the file name is applied. It
has the pattern `<name of the Source the index is on>.<file index extension>.`
The index extensions are `.bai` or `.crai`.

## Using Hosted or Local IGV to access read

sets

IGV is a genome browser used to analyze BAM and CRAM files. It requires both the file and the
index because it only displays a portion of the genome at a time. IGV can be downloaded and used locally, and
there are guides to creating an AWS hosted IGV. The public web version isn't supported because it requires
CORS.

Local IGV relies on the local AWS configuration to access files. Ensure that the role used in
that configuration has a policy attached that enables kms:Decrypt and s3:GetObject permissions to the s3 URI
of the read sets being accessed. After that, in IGV, you can use “File > load from URL” and paste in the URI
for the source and index. Alternatively, presigned URLs can be generated and used in the same manner, which
will bypass the AWS configuration. Note that CORS isn't supported with Amazon S3 URI access, so requests relying on
CORS aren't supported.

The example AWS Hosted IGV relies on AWS Cognito to create the correct configurations and
permissions inside the environment. Ensure that a policy is created that enableskms:Decrypt and s3:GetObject
permissions to the Amazon S3 URI of the read sets being accessed, and add this policy to the role that's assigned to
the Cognito user pool. After that, in IGV, you can use “File > load from URL” and enter in the URI for the
source and index. Alternatively, presigned URLs can be generated and used in the same manner, which bypasses the
AWS configuration.

Note that the sequence store will not appear under the “Amazon” tab because that only displays
buckets owned by you in the Region in which the AWS profile is configured.

## Using Samtools or HTSlib in HealthOmics

HTSlib is the core library that's shared by several tools such as Samtools, rSamtools, PySam, and
others. Use HTSlib version 1.20 or later to get seamless support for Amazon S3 Access Points. For older versions of
the HTSlib library, you can use the following workarounds:

- Set the environment variable for the HTS Amazon S3 host with:
  `export HTS_S3_HOST="s3.`region`.amazonaws.com"`.
- Generate a presigned URL for the files that you want to use. If a BAM or CRAM is being
  used, ensure that a presigned URL is generated for both the file and the index. After that, both files can
  be used with the libraries.
- Use Mountpoint to mount the sequence store or read set prefix in the same environment
  where you’re using HTSlib libraries. From here, the files can be accessed by using local file paths.

## Using Mountpoint HealthOmics

Mountpoint for Amazon S3 is a simple, high-throughput file client for [mounting an Amazon S3 bucket as a local file system](https://aws.amazon.com/blogs/storage/the-inside-story-on-mountpoint-for-amazon-s3-a-high-performance-open-source-file-client/ "https://aws.amazon.com/blogs/storage/the-inside-story-on-mountpoint-for-amazon-s3-a-high-performance-open-source-file-client/"). With Mountpoint for Amazon S3, your applications can
access objects stored in Amazon S3 through file operations such as open and read. Mountpoint for Amazon S3 automatically
translates these operations into Amazon S3 object API calls, giving your applications access to the elastic storage
and throughput of Amazon S3 through a file interface.

Mountpoint can be installed by using [the Mountpoint installation
instructions](https://github.com/awslabs/mountpoint-s3/blob/main/doc/INSTALL.md "https://github.com/awslabs/mountpoint-s3/blob/main/doc/INSTALL.md"). Mountpoint uses the AWS Profile that's local to the installation and works at an Amazon S3
prefix level. Ensure that the profile being used has a policy that enables s3:GetObject, s3:ListBucket, and
kms:Decrypt permissions to the Amazon S3 URI prefix of the read set(s) or sequence store being accessed. After
that, the bucket can be mounted by using the following path:

```
mount-s3 ``access point arn`` ``local path to mount`` --prefix ``prefix to sequence store or read set`` --region ``region``
```

## Using CloudFront with HealthOmics

Amazon CloudFront is a content delivery network (CDN) service that's built for high performance,
security, and developer convenience. Customers that want to use CloudFront must work with the Service team to
turn on the CloudFront distribution. Work with your account team to engage the HealthOmics service team.
