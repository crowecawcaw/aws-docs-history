

# Listing objects from a directory bucket
<a name="directory-buckets-objects-listobjectsExamples"></a>

 The following code examples show how to list objects in an Amazon S3 directory bucket by using the `ListObjectsV2` API operation. 

## Using the AWS CLI
<a name="directory-download-object-cli"></a>

The following `list-objects-v2` example command shows how you can use the AWS CLI to list objects from Amazon S3. This command lists objects from the directory bucket `{{bucket-base-name}}--{{zone-id}}--x-s3`. To run this command, replace the `{{user input placeholders}}` with your own information.

```
aws s3api list-objects-v2 --bucket {{bucket-base-name}}--{{zone-id}}--x-s3
```

For more information, see [list-objects-v2](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/list-objects-v2.html) in the *AWS CLI Command Reference*.