# Use `CreateMultipartUpload` with an AWS SDK or CLI

The following code examples show how to use `CreateMultipartUpload`.

Action examples are code excerpts from larger programs and must be run in context. You can see this action in
 context in the following code examples:
 


* [Perform a multipart copy](s3_example_s3_MultipartCopy_section.md "s3_example_s3_MultipartCopy_section.md")
* [Use checksums](s3_example_s3_Scenario_UseChecksums_section.md "s3_example_s3_Scenario_UseChecksums_section.md")
* [Work with Amazon S3 object integrity](s3_example_s3_Scenario_ObjectIntegrity_section.md "s3_example_s3_Scenario_ObjectIntegrity_section.md")

C++


**SDK for C++**

###### Note


 There's more on GitHub. Find the complete example and learn how to set up and run in the
 [AWS Code
 Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/cpp/example_code/s3#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/cpp/example_code/s3#code-examples").
 



```
//! Create a multipart upload.
/*!
    \param bucket: The name of the S3 bucket where the object will be uploaded.
    \param key: The unique identifier (key) for the object within the S3 bucket.
    \param client: The S3 client instance used to perform the upload operation.
    \return Aws::String: Upload ID or empty string if failed.
*/
Aws::String
AwsDoc::S3::createMultipartUpload(const Aws::String &bucket, const Aws::String &key,
                                  Aws::S3::Model::ChecksumAlgorithm checksumAlgorithm,
                                  const Aws::S3::S3Client &client) {
    Aws::S3::Model::CreateMultipartUploadRequest request;
    request.SetBucket(bucket);
    request.SetKey(key);

    if (checksumAlgorithm != Aws::S3::Model::ChecksumAlgorithm::NOT_SET) {
        request.SetChecksumAlgorithm(checksumAlgorithm);
    }

    Aws::S3::Model::CreateMultipartUploadOutcome outcome =
            client.CreateMultipartUpload(request);

    Aws::String uploadID;
    if (outcome.IsSuccess()) {
        uploadID = outcome.GetResult().GetUploadId();
    } else {
        std::cerr << "Error creating multipart upload: " << outcome.GetError().GetMessage() << std::endl;
    }

    return uploadID;
}


```


* For API details, see
 [CreateMultipartUpload](https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/CreateMultipartUpload "https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/CreateMultipartUpload")
 in *AWS SDK for C++ API Reference*.




CLI


**AWS CLI**

The following command creates a multipart upload in the bucket `amzn-s3-demo-bucket` with the key `multipart/01`:



```
`aws s3api create-multipart-upload --bucket `amzn-s3-demo-bucket` --key '`multipart/01`'`

```

Output:



```
{
    "Bucket": "amzn-s3-demo-bucket",
    "UploadId": "dfRtDYU0WWCCcH43C3WFbkRONycyCpTJJvxu2i5GYkZljF.Yxwh6XG7WfS2vC4to6HiV6Yjlx.cph0gtNBtJ8P3URCSbB7rjxI5iEwVDmgaXZOGgkk5nVTW16HOQ5l0R",
    "Key": "multipart/01"
}
```

The completed file will be named `01` in a folder called `multipart` in the bucket `amzn-s3-demo-bucket`. Save the upload ID, key and bucket name for use with the `upload-part` command.



* For API details, see
 [CreateMultipartUpload](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/create-multipart-upload.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/create-multipart-upload.html")
 in *AWS CLI Command Reference*.




Rust


**SDK for Rust**

###### Note


 There's more on GitHub. Find the complete example and learn how to set up and run in the
 [AWS Code
 Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/rustv1/examples/s3#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/rustv1/examples/s3#code-examples").
 



```
    // Create a multipart upload. Use UploadPart and CompleteMultipartUpload to
    // upload the file.
    let multipart_upload_res: CreateMultipartUploadOutput = client
        .create_multipart_upload()
        .bucket(&bucket_name)
        .key(&key)
        .send()
        .await?;

    let upload_id = multipart_upload_res.upload_id().ok_or(S3ExampleError::new(
        "Missing upload_id after CreateMultipartUpload",
    ))?;


```


```
    let mut upload_parts: Vec<aws_sdk_s3::types::CompletedPart> = Vec::new();

    for chunk_index in 0..chunk_count {
        let this_chunk = if chunk_count - 1 == chunk_index {
            size_of_last_chunk
        } else {
            CHUNK_SIZE
        };
        let stream = ByteStream::read_from()
            .path(path)
            .offset(chunk_index * CHUNK_SIZE)
            .length(Length::Exact(this_chunk))
            .build()
            .await
            .unwrap();

        // Chunk index needs to start at 0, but part numbers start at 1.
        let part_number = (chunk_index as i32) + 1;
        let upload_part_res = client
            .upload_part()
            .key(&key)
            .bucket(&bucket_name)
            .upload_id(upload_id)
            .body(stream)
            .part_number(part_number)
            .send()
            .await?;

        upload_parts.push(
            CompletedPart::builder()
                .e_tag(upload_part_res.e_tag.unwrap_or_default())
                .part_number(part_number)
                .build(),
        );
    }


```


```
    // upload_parts: Vec<aws_sdk_s3::types::CompletedPart>
    let completed_multipart_upload: CompletedMultipartUpload = CompletedMultipartUpload::builder()
        .set_parts(Some(upload_parts))
        .build();

    let _complete_multipart_upload_res = client
        .complete_multipart_upload()
        .bucket(&bucket_name)
        .key(&key)
        .multipart_upload(completed_multipart_upload)
        .upload_id(upload_id)
        .send()
        .await?;


```


* For API details, see
 [CreateMultipartUpload](https://docs.rs/aws-sdk-s3/latest/aws_sdk_s3/client/struct.Client.html#method.create_multipart_upload "https://docs.rs/aws-sdk-s3/latest/aws_sdk_s3/client/struct.Client.html#method.create_multipart_upload")
 in *AWS SDK for Rust API reference*.




For a complete list of AWS SDK developer guides and code examples, see
 [Developing with Amazon S3 using the AWS SDKs](sdk-general-information-section.md "sdk-general-information-section.md").
 This topic also includes information about getting started and details about previous SDK versions.
