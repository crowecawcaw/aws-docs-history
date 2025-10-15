# Replace all object tags

You can use Amazon S3 Batch Operations to perform large-scale batch operations on Amazon S3 objects.
 The **Replace all object tags** operation replaces the object tags on every
 object listed in the manifest. An object tag is a key-value pair of strings that you can use to
 store metadata about an object.

To create a **Replace all object tags** job, you provide a set of tags that
 you want to apply. S3 Batch Operations applies the same set of tags to every object. The tag set that
 you provide replaces whatever tag sets are already associated with the objects in the manifest.
 S3 Batch Operations doesn't support adding tags to objects while leaving the existing tags in
 place.

If the objects in your manifest are in a versioned bucket, you can apply the tag set to
 specific versions of every object. To do so, specify a version ID for every object in the
 manifest. If you don't include a version ID for any objects, S3 Batch Operations applies the tag set
 to the latest version of every object. For more information about Batch Operations manifests, see
 [Specifying a manifest](batch-ops-create-job.md#specify-batchjob-manifest "batch-ops-create-job.md#specify-batchjob-manifest"). 

For more information about object tagging, see [Categorizing your objects using tags](object-tagging.md "object-tagging.md") in this guide, and see [PutObjectTagging](../API/API_PutObjectTagging.md "../API/API_PutObjectTagging.md"),
 [GetObjectTagging](../API/API_GetObjectTagging.md "../API/API_GetObjectTagging.md"), and [DeleteObjectTagging](../API/API_DeleteObjectTagging.md "../API/API_DeleteObjectTagging.md") in the *Amazon Simple Storage Service API Reference*.

To use the console to create a **Replace all object tags** job, see [Creating an S3 Batch Operations job](batch-ops-create-job.md "batch-ops-create-job.md").


## Restrictions and limitations


When you're using Batch Operations to replace object tags, the following restrictions and
 limitations apply:



* The AWS Identity and Access Management (IAM) role that you specify to run the Batch Operations job must have
 permissions to perform the underlying `PutObjectTagging` operation. For more
 information about the permissions required, see [PutObjectTagging](../API/API_PutObjectTagging.md "../API/API_PutObjectTagging.md") in the
 *Amazon Simple Storage Service API Reference*.
* S3 Batch Operations uses the Amazon S3 [PutObjectTagging](../API/API_PutObjectTagging.md "../API/API_PutObjectTagging.md") operation to apply tags to each object in the
 manifest. All restrictions and limitations that apply to the underlying operation also
 apply to S3 Batch Operations jobs.
* A single replace all object tags job can support a manifest with up to 20 billion objects.
