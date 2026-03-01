# Differences for directory buckets

When using Amazon S3, you can choose the bucket type that best fits your application and
performance requirements. A directory bucket is a type of bucket that is best used for
low latency or data residency use cases. To
learn more about directory buckets, see [Working with directory buckets](directory-buckets-overview.md "directory-buckets-overview.md").

For more information about how directory buckets are different, see
the following topics.

###### Topics

- [Differences for directory buckets](#s3-express-specifications "#s3-express-specifications")
- [API operations supported for directory buckets](#s3-express-differences-api-operations "#s3-express-differences-api-operations")
- [Amazon S3 features not supported by directory buckets](#s3-express-differences-unsupported-features "#s3-express-differences-unsupported-features")

## Differences for directory buckets

- **Directory bucket names**
  - A directory bucket name consists of a base name that you
    provide and a suffix that contains the ID of the AWS Zone
    (an Availability Zone or Local Zone) that your bucket is located in, followed by `--x-s`. For a list of rules and examples of
    directory bucket names, see [Directory bucket naming rules](directory-bucket-naming-rules.md "directory-bucket-naming-rules.md").

- **`ListObjectsV2` behavior**
  - For directory buckets, `ListObjectsV2` does not
    return objects in lexicographical (alphabetical) order.
    Additionally, prefixes must end in a delimiter and only "/" can
    be specified as the delimiter.
  - For directory buckets, `ListObjectsV2` response
    includes the prefixes that are related only to in-progress
    multipart uploads.

- **Deletion behavior** – When you
  delete an object in a directory bucket, Amazon S3 recursively deletes any
  empty directories in the object path. For example, if you delete the
  object key `dir1/dir2/file1.txt`, Amazon S3 deletes
  `file1.txt`. If the `dir1/`
  and `dir2/` directories are empty and contain no
  other objects, Amazon S3 also deletes those directories.
- **ETags and checksums** – Entity tags
  (ETags) for directory buckets are random alphanumeric strings unique to the object and not MD5 checksums.
  For more information about using additional checksums with directory buckets, see
  [S3 additional checksum best practices](s3-express-optimizing-performance.md#s3-express-optimizing-performance-checksums "s3-express-optimizing-performance.md#s3-express-optimizing-performance-checksums").
- **Object keys in `DeleteObjects`
  requests**
  - Object keys in `DeleteObjects` requests must
    contain at least one non-white space character. Strings of all
    white space characters aren't supported in
    `DeleteObjects` requests.
  - Object keys in `DeleteObjects` requests cannot
    contain Unicode control characters, except for the newline
    (`\n`), tab (`\t`), and carriage
    return (`\r`) characters.

- **Regional and Zonal endpoints** –
  Bucket-management API operations for directory buckets are available
  through a Regional endpoint and are referred to as Regional endpoint API
  operations. Examples of Regional endpoint API operations are
  CreateBucket and DeleteBucket. After you create a directory bucket, you
  can use Zonal endpoint API operations to upload and manage the objects
  in your directory bucket. Zonal endpoint API operations are available
  through a Zonal endpoint. Examples of Zonal endpoint API operations are
  `PutObject` and `CopyObject`. When using
  directory buckets, you must specify the Region in all requests. For
  Regional endpoints, you specify the Region, for example,
  `s3express-control.us-west-2.amazonaws.com`. For Zonal
  endpoints, you specify both the Region and the Availability Zone, for
  example, `s3express-usw2-az1.us-west-2.amazonaws.com`. For
  more information, see [Regional and Zonal endpoints for directory buckets](s3-express-Regions-and-Zones.md "s3-express-Regions-and-Zones.md").
- **Multipart uploads** – You can
  upload and copy large objects that are stored in directory buckets by
  using the multipart upload process. However, the following are some
  differences when using the multipart upload process with objects stored
  in directory buckets. For more information, see [Using multipart uploads with directory buckets](s3-express-using-multipart-upload.md "s3-express-using-multipart-upload.md").
  - The object creation date is the completion date of the
    multipart upload.
  - Multipart part numbers must use consecutive part numbers. If
    you try to complete a multipart upload request with
    nonconsecutive part numbers, Amazon S3 generates an HTTP `400
(Bad Request)` error.
  - The initiator of a multipart upload can abort the multipart
    upload request only if they have been granted explicit allow
    access to `AbortMultipartUpload` through the
    `s3express:CreateSession` permission. For more
    information, see [Authorizing Regional endpoint API operations with IAM](s3-express-security-iam.md "s3-express-security-iam.md").

- **Emptying a directory bucket** –
  The `s3 rm` command through the AWS Command Line Interface (CLI), the
  `delete` operation through Mountpoint, and the
  **Empty** bucket option button through the
  AWS Management Console are unable to delete in-progress multipart uploads in a
  directory bucket. To delete these in-progress multipart uploads, use
  the `ListMultipartUploads` operation to list the in-progress
  multipart uploads in the bucket and use the
  `AbortMultipartUpload` operation to abort all the
  in-progress multipart uploads.
- **AWS Local Zones** – Local Zones are only supported for directory buckets not general purpose buckets.
  - Appending data to existing objects isn’t supported for
    directory buckets that reside in Local Zones. You can only append data to
    existing objects in directory buckets that reside in Availability
    Zones.

## API operations supported for directory buckets

The directory buckets support both Regional (bucket level, or control plane) and
Zonal (object level, or data plane) endpoint API operations. For more information, see
[Networking for directory buckets](s3-express-networking.md "s3-express-networking.md") and
[Endpoints and gateway VPC endpoints](directory-bucket-high-performance.md#s3-express-overview-endpoints "directory-bucket-high-performance.md#s3-express-overview-endpoints"). For a list of supported API operations see [Directory bucket API operations](s3-express-APIs.md "s3-express-APIs.md").

## Amazon S3 features not supported by directory buckets

The following Amazon S3 features are not supported by directory buckets:

- AWS managed policies
- AWS PrivateLink for S3
- MD5 checksums
- Multi-factor authentication (MFA) delete
- S3 Object Lock
- Requester Pays
- S3 Access Grants
- Amazon CloudWatch request metrics
- S3 Event Notifications
- S3 Lifecycle transition actions
- S3 Multi-Region Access Points
- S3 Object Lambda Access Points
- S3 Versioning
- S3 Inventory
- S3 Replication
- Object tags
- S3 Select
- Server access logs
- Static website hosting
- S3 Storage Lens
- S3 Storage Lens groups
- S3 Transfer Acceleration
- Dual-layer server-side encryption with AWS Key Management Service (AWS KMS) keys
  (DSSE-KMS)
- Server-side encryption with customer-provided keys (SSE-C)
- The option to copy an existing bucket's settings when creating a new bucket in
  the Amazon S3 console
- Enhanced access denied (HTTP `403 Forbidden`) error messages
