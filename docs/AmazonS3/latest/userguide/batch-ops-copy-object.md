# Copy objects

You can use Amazon S3 Batch Operations to perform large-scale batch operations on Amazon S3 objects.
 The Batch Operations **Copy** operation copies each object that is specified in the
 manifest. You can copy objects to a bucket in the same AWS Region or to a bucket in a
 different Region. S3 Batch Operations supports most options available through Amazon S3 for copying
 objects. These options include setting object metadata, setting permissions, and changing an
 object's storage class. 

You can also use the **Copy** operation to copy existing unencrypted
 objects and write them back to the same bucket as encrypted objects. For more information, see
 [Encrypting objects
 with Amazon S3 Batch Operations](https://aws.amazon.com/blogs/storage/encrypting-objects-with-amazon-s3-batch-operations/ "https://aws.amazon.com/blogs/storage/encrypting-objects-with-amazon-s3-batch-operations/").

When you copy objects, you can change the checksum algorithm used to calculate the checksum
 of the object. If objects don't have an additional checksum calculated, you can also add one by
 specifying the checksum algorithm for Amazon S3 to use. For more information, see 
 [Checking object integrity in Amazon S3](checking-object-integrity.md "checking-object-integrity.md").

For more information about copying objects in Amazon S3 and the required and optional parameters,
 see [Copying, moving, and renaming objects](copy-object.md "copy-object.md") in this guide and [CopyObject](../API/API_CopyObject.md "../API/API_CopyObject.md") in the *Amazon Simple Storage Service API Reference*.


## Restrictions and limitations


When you're using the Batch Operations **Copy** operation, the following
 restrictions and limitations apply:



* All source objects must be in one bucket.
* All destination objects must be in one bucket.
* You must have read permissions for the source bucket and write permissions for the
 destination bucket.
* Objects to be copied can be up to 5 GB in size.
* If you try to copy objects from the S3 Glacier Flexible Retrieval or S3 Glacier Deep Archive
 classes to the S3 Standard storage class, you must first restore these objects. For more
 information, see [Restoring an archived object](restoring-objects.md "restoring-objects.md").
* You must create your Batch Operations **Copy** jobs in the destination
 Region, which is the Region that you intend to copy the objects to.
* All `CopyObject` options are supported except for conditional checks on
 entity tags (ETags) and server-side encryption with customer-provided encryption keys (SSE-C).
* If the destination bucket is unversioned, you will overwrite any objects that have the
 same key names.
* Objects aren't necessarily copied in the same order as they appear in the manifest.
 For versioned buckets, if preserving the current or noncurrent version order is important,
 copy all noncurrent versions first. Then, after the first job is complete, copy the
 current versions in a subsequent job.
* Copying objects to the Reduced Redundancy Storage (RRS) class isn't supported.
* A single Batch Operations Copy job can support a manifest with up to 20 billion objects.
