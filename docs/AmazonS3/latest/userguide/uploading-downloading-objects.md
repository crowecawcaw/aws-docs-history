# Working with objects in Amazon S3

To store your data in Amazon S3, you work with resources known as buckets and objects. A
_bucket_ is a container for objects. An _object_ is a file and any metadata that describes that
file.

To store an object in Amazon S3, you create a bucket and then upload the object to a bucket.
When the object is in the bucket, you can open it, download it, and copy it. When you no
longer need an object or a bucket, you can clean up these resources.

###### Note

For more information about using the Amazon S3 Express One Zone storage class with directory buckets, see [S3 Express One Zone](directory-bucket-high-performance.md#s3-express-one-zone "directory-bucket-high-performance.md#s3-express-one-zone") and [Working with directory buckets](directory-buckets-overview.md "directory-buckets-overview.md").

###### Important

In the Amazon S3 console, when you choose **Open** or **Download As** for an object, these operations create presigned URLs. For the duration of five minutes, your object will be accessible to anyone who has access to these presigned URLs. For more information about presigned URLs, see [Using presigned URLS](using-presigned-url.md "using-presigned-url.md").

With Amazon S3, you pay only for what you use. For more information about Amazon S3 features and
pricing, see [Amazon S3](https://aws.amazon.com/s3 "https://aws.amazon.com/s3"). If you are a new Amazon S3 customer,
you can get started with Amazon S3 for free. For more information, see [AWS Free Tier](https://aws.amazon.com/free "https://aws.amazon.com/free").

###### Topics

- [Amazon S3 objects overview](UsingObjects.md "UsingObjects.md")
- [Naming Amazon S3 objects](object-keys.md "object-keys.md")
- [Working with object metadata](UsingMetadata.md "UsingMetadata.md")
- [Uploading objects](upload-objects.md "upload-objects.md")
- [Add preconditions to S3 operations with conditional requests](conditional-requests.md "conditional-requests.md")
- [Copying, moving, and renaming objects](copy-object.md "copy-object.md")
- [Downloading objects](download-objects.md "download-objects.md")
- [Checking object integrity in Amazon S3](checking-object-integrity.md "checking-object-integrity.md")
- [Deleting Amazon S3 objects](DeletingObjects.md "DeletingObjects.md")
- [Organizing, listing, and working with your objects](organizing-objects.md "organizing-objects.md")
- [Download and upload objects with presigned URLs](using-presigned-url.md "using-presigned-url.md")
- [Transforming objects with S3 Object Lambda](transforming-objects.md "transforming-objects.md")
- [Performing object operations in bulk with Batch Operations](batch-ops.md "batch-ops.md")
- [Querying data in place with Amazon S3 Select](selecting-content-from-objects.md "selecting-content-from-objects.md")
