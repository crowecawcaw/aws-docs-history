# Use `GetObjectTagging` with a CLI

The following code examples show how to use `GetObjectTagging`.

Action examples are code excerpts from larger programs and must be run in context. You can see this action in
 context in the following code example:
 


* [Get started with tags](s3_example_s3_Scenario_Tagging_section.md "s3_example_s3_Scenario_Tagging_section.md")

CLI


**AWS CLI**

**To retrieve the tags attached to an object**


The following `get-object-tagging` example retrieves the values for the specified key from the specified object.



```
`aws s3api get-object-tagging \
 --bucket `amzn-s3-demo-bucket` \
 --key `doc1.rtf``

```

Output:



```
{
    "TagSet": [
        {
            "Value": "confidential",
            "Key": "designation"
        }
    ]
}
```

The following `get-object-tagging` example tries to retrieve the tag sets of the object `doc2.rtf`, which has no tags.



```
`aws s3api get-object-tagging \
 --bucket `amzn-s3-demo-bucket` \
 --key `doc2.rtf``

```

Output:



```
{
    "TagSet": []
}
```

The following `get-object-tagging` example retrieves the tag sets of the object `doc3.rtf`, which has multiple tags.



```
`aws s3api get-object-tagging \
 --bucket `amzn-s3-demo-bucket` \
 --key `doc3.rtf``

```

Output:



```
{
    "TagSet": [
        {
            "Value": "confidential",
            "Key": "designation"
        },
        {
            "Value": "finance",
            "Key": "department"
        },
        {
            "Value": "payroll",
            "Key": "team"
        }
    ]
}
```


* For API details, see
 [GetObjectTagging](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/get-object-tagging.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/get-object-tagging.html")
 in *AWS CLI Command Reference*.




PowerShell


**Tools for PowerShell V4**

**Example 1: The sample returns the tags associated with the object present on the given S3 bucket.**



```
Get-S3ObjectTagSet -Key 'testfile.txt' -BucketName 'amzn-s3-demo-bucket'

```

**Output:**



```
Key  Value
---  -----
test value
```


* For API details, see
 [GetObjectTagging](https://docs.aws.amazon.com/powershell/v4/reference "https://docs.aws.amazon.com/powershell/v4/reference")
 in *AWS Tools for PowerShell Cmdlet Reference (V4)*.


**Tools for PowerShell V5**

**Example 1: The sample returns the tags associated with the object present on the given S3 bucket.**



```
Get-S3ObjectTagSet -Key 'testfile.txt' -BucketName 'amzn-s3-demo-bucket'

```

**Output:**



```
Key  Value
---  -----
test value
```


* For API details, see
 [GetObjectTagging](https://docs.aws.amazon.com/powershell/v5/reference "https://docs.aws.amazon.com/powershell/v5/reference")
 in *AWS Tools for PowerShell Cmdlet Reference (V5)*.




For a complete list of AWS SDK developer guides and code examples, see
 [Developing with Amazon S3 using the AWS SDKs](sdk-general-information-section.md "sdk-general-information-section.md").
 This topic also includes information about getting started and details about previous SDK versions.
