# Listing object keys programmatically

In Amazon S3, keys can be listed by prefix. You can choose a common prefix for the names of
related keys and mark these keys with a special character that delimits hierarchy. You can
then use the list operation to select and browse keys hierarchically. This is similar to how
files are stored in directories within a file system.

Amazon S3 exposes a list operation that lets you enumerate the keys contained in a bucket. Keys
are selected for listing by bucket and prefix. For example, consider a bucket named
"`dictionary`" that contains a key for every English word. You might make a
call to list all the keys in that bucket that start with the letter "q". List results are
always returned in UTF-8 binary order.

Both the SOAP and REST list operations return an XML document that contains the names of
matching keys and information about the object identified by each key.

###### Note

SOAP APIs for Amazon S3 are not available for new customers, and are approaching End of Life (EOL) on August 31, 2025. We recommend that you use either the REST API or the AWS SDKs.

Groups of keys that share a prefix terminated by a special delimiter can be rolled up by
that common prefix for the purposes of listing. This enables applications to organize and
browse their keys hierarchically, much like how you would organize your files into
directories in a file system.

For example, to extend the dictionary bucket to contain more than just English words, you
might form keys by prefixing each word with its language and a delimiter, such as
"`French/logical`". Using this naming scheme and the hierarchical listing
feature, you could retrieve a list of only French words. You could also browse the top-level
list of available languages without having to iterate through all the lexicographically
intervening keys. For more information about this aspect of listing, see [Organizing objects using prefixes](using-prefixes.md "using-prefixes.md").

###### REST API

If your application requires it, you can send REST requests directly. You can send a
GET request to return some or all of the objects in a bucket or you can use selection
criteria to return a subset of the objects in a bucket. For more information, see [GET Bucket (List Objects) Version 2](../API/v2-RESTBucketGET.md "../API/v2-RESTBucketGET.md")
in the _Amazon Simple Storage Service API Reference_.

###### List implementation efficiency

List performance is not substantially affected by the total number of keys in your
bucket. It's also not affected by the presence or absence of the `prefix`,
`marker`, `maxkeys`, or `delimiter` arguments.

###### Iterating through multipage results

As buckets can contain a virtually unlimited number of keys, the complete results of a
list query can be extremely large. To manage large result sets, the Amazon S3 API supports
pagination to split them into multiple responses. Each list keys response returns a page
of up to 1,000 keys with an indicator indicating if the response is truncated. You send
a series of list keys requests until you have received all the keys. AWS SDK wrapper
libraries provide the same pagination.

## Examples

When you list all of the objects in your bucket, note that you must have the
`s3:ListBucket` permission.

CLI

**list-objects**

The following example uses the `list-objects`
command to display the names of all the objects in the
specified bucket:

```
`aws s3api list-objects --bucket `text-content` --query '`Contents[].{Key: Key, Size: Size}`'`

```

The example uses the `--query` argument to
filter the output of `list-objects` down to the
key value and size for each object

For more information about objects, see [Working with objects in
Amazon S3](uploading-downloading-objects.md "uploading-downloading-objects.md").

- For API details, see [ListObjects](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/list-objects.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/list-objects.html") in
  _AWS CLI Command Reference_.

**ls**

The following example lists all objects and prefixes in a
bucket by using the `ls` command.

To use this example command, replace
`amzn-s3-demo-bucket` with the
name of your bucket.

```
$ aws s3 ls s3://``amzn-s3-demo-bucket``
```

- For more information about the high-level command
  `ls`, see [List buckets and objects](../../../cli/latest/userguide/cli-services-s3-commands.md#using-s3-commands-listing-buckets "../../../cli/latest/userguide/cli-services-s3-commands.md#using-s3-commands-listing-buckets") in
  _AWS Command Line Interface User Guide_.

PowerShell

**Tools for PowerShell V4**

**Example 1: This command retrieves the information about all of the items in the bucket "test-files".**

```
Get-S3Object -BucketName amzn-s3-demo-bucket

```

**Example 2: This command retrieves the information about the item "sample.txt" from bucket "test-files".**

```
Get-S3Object -BucketName amzn-s3-demo-bucket -Key sample.txt

```

**Example 3: This command retrieves the information about all items with the prefix "sample" from bucket "test-files".**

```
Get-S3Object -BucketName amzn-s3-demo-bucket -KeyPrefix sample

```

- For API details, see
  [ListObjects](../../../powershell/v4/reference.md "../../../powershell/v4/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V4)_.

**Tools for PowerShell V5**

**Example 1: This command retrieves the information about all of the items in the bucket "test-files".**

```
Get-S3Object -BucketName amzn-s3-demo-bucket

```

**Example 2: This command retrieves the information about the item "sample.txt" from bucket "test-files".**

```
Get-S3Object -BucketName amzn-s3-demo-bucket -Key sample.txt

```

**Example 3: This command retrieves the information about all items with the prefix "sample" from bucket "test-files".**

```
Get-S3Object -BucketName amzn-s3-demo-bucket -KeyPrefix sample

```

- For API details, see
  [ListObjects](../../../powershell/v5/reference.md "../../../powershell/v5/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V5)_.
