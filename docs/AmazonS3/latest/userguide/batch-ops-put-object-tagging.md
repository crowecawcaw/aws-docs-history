

# Replace all object tags
<a name="batch-ops-put-object-tagging"></a>

You can use Amazon S3 Batch Operations to perform large-scale batch operations on Amazon S3 objects. The **Replace all object tags** operation replaces the object tags on every object listed in the manifest. An object tag is a key-value pair of strings that you can use to store metadata about an object.

To create a **Replace all object tags** job, you provide a set of tags that you want to apply. S3 Batch Operations applies the same set of tags to every object. The tag set that you provide replaces whatever tag sets are already associated with the objects in the manifest. S3 Batch Operations doesn't support adding tags to objects while leaving the existing tags in place.

If the objects in your manifest are in a versioned bucket, you can apply the tag set to specific versions of every object. To do so, specify a version ID for every object in the manifest. If you don't include a version ID for any objects, S3 Batch Operations applies the tag set to the latest version of every object. For more information about Batch Operations manifests, see [Specifying a manifest](batch-ops-create-job.md#specify-batchjob-manifest). 

For more information about object tagging, see [Tagging your objects](object-tagging.md) in this guide, and see [PutObjectTagging](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutObjectTagging.html), [GetObjectTagging](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetObjectTagging.html), and [DeleteObjectTagging](https://docs.aws.amazon.com/AmazonS3/latest/API/API_DeleteObjectTagging.html) in the *Amazon Simple Storage Service API Reference*.

To use the console to create a **Replace all object tags** job, see [Creating an S3 Batch Operations job](batch-ops-create-job.md).

## Restrictions and limitations
<a name="batch-ops-set-tagging-restrictions"></a>

When you're using Batch Operations to replace object tags, the following restrictions and limitations apply:
+ The AWS Identity and Access Management (IAM) role that you specify to run the Batch Operations job must have permissions to perform the underlying `PutObjectTagging` operation. For more information about the permissions required, see [PutObjectTagging](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutObjectTagging.html) in the *Amazon Simple Storage Service API Reference*.
+ S3 Batch Operations uses the Amazon S3 [PutObjectTagging](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutObjectTagging.html) operation to apply tags to each object in the manifest. All restrictions and limitations that apply to the underlying operation also apply to S3 Batch Operations jobs.
+ A single replace all object tags job can support a manifest with up to 20 billion objects.