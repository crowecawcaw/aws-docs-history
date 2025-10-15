# Use `ListObjects` with a CLI

The following code examples show how to use `ListObjects`.

Action examples are code excerpts from larger programs and must be run in context. You can see this action in
 context in the following code example:
 


* [Create a web page that lists Amazon S3 objects](s3_example_s3_Scenario_ListObjectsWeb_section.md "s3_example_s3_Scenario_ListObjectsWeb_section.md")

CLI


**AWS CLI**

The following example uses the `list-objects` command to display the names of all the objects in the specified bucket:



```
`aws s3api list-objects --bucket `text-content` --query '`Contents[].{Key: Key, Size: Size}`'`

```

The example uses the `--query` argument to filter the output of
`list-objects` down to the key value and size for each object


For more information about objects, see Working with Amazon S3 Objects in the *Amazon S3 Developer Guide*.



* For API details, see
 [ListObjects](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/list-objects.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/list-objects.html")
 in *AWS CLI Command Reference*.




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


* For API details, see
 [ListObjects](https://docs.aws.amazon.com/powershell/v4/reference "https://docs.aws.amazon.com/powershell/v4/reference")
 in *AWS Tools for PowerShell Cmdlet Reference (V4)*.


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


* For API details, see
 [ListObjects](https://docs.aws.amazon.com/powershell/v5/reference "https://docs.aws.amazon.com/powershell/v5/reference")
 in *AWS Tools for PowerShell Cmdlet Reference (V5)*.




For a complete list of AWS SDK developer guides and code examples, see
 [Developing with Amazon S3 using the AWS SDKs](sdk-general-information-section.md "sdk-general-information-section.md").
 This topic also includes information about getting started and details about previous SDK versions.
