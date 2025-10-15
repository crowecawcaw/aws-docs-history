# Use `GetBucketLocation` with an AWS SDK or CLI

The following code examples show how to use `GetBucketLocation`.


CLI


**AWS CLI**

The following command retrieves the location constraint for a bucket named `amzn-s3-demo-bucket`, if a constraint exists:



```
`aws s3api get-bucket-location --bucket `amzn-s3-demo-bucket``

```

Output:



```
{
    "LocationConstraint": "us-west-2"
}
```


* For API details, see
 [GetBucketLocation](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/get-bucket-location.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/get-bucket-location.html")
 in *AWS CLI Command Reference*.




PowerShell


**Tools for PowerShell V4**

**Example 1: This command returns the location constraint for the bucket 'amzn-s3-demo-bucket', if a constraint exists.**



```
Get-S3BucketLocation -BucketName 'amzn-s3-demo-bucket'

```

**Output:**



```
Value
-----
ap-south-1
```


* For API details, see
 [GetBucketLocation](https://docs.aws.amazon.com/powershell/v4/reference "https://docs.aws.amazon.com/powershell/v4/reference")
 in *AWS Tools for PowerShell Cmdlet Reference (V4)*.


**Tools for PowerShell V5**

**Example 1: This command returns the location constraint for the bucket 'amzn-s3-demo-bucket', if a constraint exists.**



```
Get-S3BucketLocation -BucketName 'amzn-s3-demo-bucket'

```

**Output:**



```
Value
-----
ap-south-1
```


* For API details, see
 [GetBucketLocation](https://docs.aws.amazon.com/powershell/v5/reference "https://docs.aws.amazon.com/powershell/v5/reference")
 in *AWS Tools for PowerShell Cmdlet Reference (V5)*.




Rust


**SDK for Rust**

###### Note


 There's more on GitHub. Find the complete example and learn how to set up and run in the
 [AWS Code
 Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/rustv1/examples/s3#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/rustv1/examples/s3#code-examples").
 



```
async fn show_buckets(
    strict: bool,
    client: &Client,
    region: BucketLocationConstraint,
) -> Result<(), S3ExampleError> {
    let mut buckets = client.list_buckets().into_paginator().send();

    let mut num_buckets = 0;
    let mut in_region = 0;

    while let Some(Ok(output)) = buckets.next().await {
        for bucket in output.buckets() {
            num_buckets += 1;
            if strict {
                let r = client
                    .get_bucket_location()
                    .bucket(bucket.name().unwrap_or_default())
                    .send()
                    .await?;

                if r.location_constraint() == Some(&region) {
                    println!("{}", bucket.name().unwrap_or_default());
                    in_region += 1;
                }
            } else {
                println!("{}", bucket.name().unwrap_or_default());
            }
        }
    }

    println!();
    if strict {
        println!(
            "Found {} buckets in the {} region out of a total of {} buckets.",
            in_region, region, num_buckets
        );
    } else {
        println!("Found {} buckets in all regions.", num_buckets);
    }

    Ok(())
}


```


* For API details, see
 [GetBucketLocation](https://docs.rs/aws-sdk-s3/latest/aws_sdk_s3/client/struct.Client.html#method.get_bucket_location "https://docs.rs/aws-sdk-s3/latest/aws_sdk_s3/client/struct.Client.html#method.get_bucket_location")
 in *AWS SDK for Rust API reference*.




For a complete list of AWS SDK developer guides and code examples, see
 [Developing with Amazon S3 using the AWS SDKs](sdk-general-information-section.md "sdk-general-information-section.md").
 This topic also includes information about getting started and details about previous SDK versions.
