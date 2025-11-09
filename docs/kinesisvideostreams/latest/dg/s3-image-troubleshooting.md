# Troubleshooting

## Images not delivered to the Amazon S3 bucket

To troubleshoot this issue, there are a few things to look out for:

1. Missing permissions
2. The image generation configuration is incorrect
3. The tag was not added to the fragment

### Missing permissions

If you're using a customer managed KMS key, ensure that the role performing the `PutMedia` calls (uploader) has the
appropriate encrypt and decrypt permissions, and has access to the Amazon S3 bucket, as follows:

- `kms:Encrypt`
- `kms:GenerateDataKey`
- `kms:Decrypt`
- `s3:PutObject`

For more information, see [How do I get started with server-side encryption?](how-kms.md#getting-started-with-sse-akvs "how-kms.md#getting-started-with-sse-akvs").

### Verify the destination

Use the AWS CLI to call the DescribeImageGenerationConfiguration API for your stream.

```
aws kinesisvideo describe-image-generation-configuration \
  --stream-name "`demo-stream`"
```

Review the `DestinationConfig` in the response and confirm it looks correct.

### Verify that the image generation tag was added to the fragment

1. Check that the `putKinesisVideoEventMetadata` call succeeded.

The `putKinesisVideoEventMetadata` method returns a status code 0 upon success. We recommend checking the return values of the functions for 0.
If a non-zero status code is returned, convert it to hex and check the [Error code reference](producer-sdk-errors.md "producer-sdk-errors.md") for more information.

Make sure you have error logs turned on and review the logs for any other errors in the application. Review and compare your application's
frame submission call pattern against the recommended implementation: [Adding image generation tags to fragments](s3-real-time-image-create.md#s3-adding-image-tags "s3-real-time-image-create.md#s3-adding-image-tags"). 2. Verify the locally-generated MKV file

Confirm that the Producer SDK or Sample Application appended the tags correctly.

    1. Set the `KVS_DEBUG_DUMP_DATA_FILE_DIR` environment variable. If this value is set, the Producer SDK writes the media files
     that it would have sent to Kinesis Video Streams to the specified location.



    ```
    export KVS_DEBUG_DUMP_DATA_FILE_DIR=/path/to/output/directory
    ```

    ###### Note

    The SDK will not create a new directory if the path doesn't exist. Create the folder if necessary.
    2. Run the application again. You should see `.mkv` files getting written to the specified output directory.
    3. Verify the contents to ensure the tag is present using MKVToolNix, or other software.


    	1. Install MKVToolNix: `brew install mkvtoolnix`
    	2. Run MKVToolNix with one of the `.mkv` files in the output directory.



    	```
    	mkvinfo -v ./path/to/video/file
    	```
    	3. Review the MKVToolNix output. If the `KinesisVideoStream::PutFragmentMetadata` producer SDK method was invoked correctly,
    	 you should see the following MKV tag.



    	```
    	|+ Tags
    	| + Tag
    	|  + Simple
    	|   + Name: AWS_KINESISVIDEO_IMAGE_GENERATION
    	```

    	###### Note

    	The tags belong to the Cluster before it.
    4. If the MKV tag is not present, ensure that the `KinesisVideoStream::PutEventMetadata` producer SDK method has been called with the `STREAM_EVENT_TYPE_IMAGE_GENERATION` argument, and that it returned a success (0) code.
