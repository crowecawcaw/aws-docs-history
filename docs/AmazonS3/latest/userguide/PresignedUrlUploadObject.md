# Uploading objects with presigned URLs

You may use presigned URLs to allow someone to upload an object to your Amazon S3 bucket. Using a
presigned URL will allow an upload without requiring another party to have AWS security
credentials or permissions. A presigned URL is limited by the permissions of the user who creates
it. That is, if you receive a presigned URL to upload an object, you can upload an object only if
the creator of the URL has the necessary permissions to upload that object.

When someone uses the URL to upload an object, Amazon S3 creates the object in the specified
bucket. If an object with the same key that is specified in the presigned URL already exists in the
bucket, Amazon S3 replaces the existing object with the uploaded object. After upload, the bucket
owner will own the object.

For general information about presigned URLs, see [Download and upload objects with presigned
URLs](using-presigned-url.md "using-presigned-url.md").

You can create a presigned URL for uploading an object without writing any code by using AWS
Explorer for Visual Studio. You can also generate a presigned URL programmatically by using the
AWS SDKs.

###### Note

At this time, the AWS Toolkit for Visual Studio doesn't support Visual Studio for Mac.

1. Install the AWS Toolkit for Visual Studio using the following instructions, [Installing and setting up the Toolkit for Visual Studio](../../../toolkit-for-visual-studio/latest/user-guide/setup.md "../../../toolkit-for-visual-studio/latest/user-guide/setup.md") in the _AWS Toolkit for Visual Studio User Guide_.
2. Connect to AWS using the following steps, [Connecting to AWS](../../../AWSToolkitVS/latest/UserGuide/connect.md "../../../AWSToolkitVS/latest/UserGuide/connect.md") in the
   _AWS Toolkit for Visual Studio User Guide_.
3. In the left side panel labeled **AWS Explorer**, right-click the bucket you wish to have an object uploaded to.
4. Choose **Create Pre-Signed URL...**.
5. In the pop-up window, set the expiration date and time for your presigned URL.
6. For **Object Key**, set the name of the file to be uploaded. The file you're uploading must match this name exactly. If an object with the same object key already exists in the
   bucket, Amazon S3 will replace the existing object with the newly uploaded object.
7. Choose **PUT** to specify that this presigned URL will be used for
   uploading an object.
8. Choose the **Generate** button.
9. To copy the URL to the clipboard, choose **Copy**.
10. To use this URL you can send a PUT request with the `curl` command. Include the full path to your file and the presigned URL itself.

```
curl -X PUT -T "`/path/to/file`" "`presigned URL`"
```

You can generate a presigned URL that can perform an S3 action for a limited time.

###### Note

If you use the AWS CLI or AWS SDKs, the expiration time for presigned URLs can be set as
high as 7 days. For more information, see
[Expiration time for presigned URLs](using-presigned-url.md#PresignedUrl-Expiration "using-presigned-url.md#PresignedUrl-Expiration").

Python
The following Python script generates a `PUT` presigned URL for uploading an object
to an S3 general purpose bucket.

1. Copy the contents of the script and save it as
   “`put-only-url.py`” file. To use the following
   examples, replace the `user input placeholders` with your
   own information (such as your file name).

```
import argparse
import boto3
from botocore.exceptions import ClientError

def generate_presigned_url(s3_client, client_method, method_parameters, expires_in):
    """
    Generate a presigned Amazon S3 URL that can be used to perform an action.

    :param s3_client: A Boto3 Amazon S3 client.
    :param client_method: The name of the client method that the URL performs.
    :param method_parameters: The parameters of the specified client method.
    :param expires_in: The number of seconds the presigned URL is valid for.
    :return: The presigned URL.
    """
    try:
        url = s3_client.generate_presigned_url(
            ClientMethod=client_method,
            Params=method_parameters,
            ExpiresIn=expires_in
        )
    except ClientError:
        print(f"Couldn't get a presigned URL for client method '{client_method}'.")
        raise
    return url

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("bucket", help="The name of the bucket.")
    parser.add_argument(
        "key", help="The key (path and filename) in the S3 bucket.",
    )
    parser.add_argument(
        "--region", help="The AWS region where the bucket is located.", default="us-east-1"
    )
    parser.add_argument(
        "--content-type", help="The content type of the file to upload.", default="application/octet-stream"
    )
    args = parser.parse_args()

    # Create S3 client with explicit region configuration
    s3_client = boto3.client("s3", region_name=args.region)

    # Optionally set signature version if needed for older S3 regions
    # s3_client.meta.config.signature_version = 's3v4'

    # The presigned URL is specified to expire in 1000 seconds
    url = generate_presigned_url(
        s3_client,
        "put_object",
        {
            "Bucket": args.bucket,
            "Key": args.key,
            "ContentType": args.content_type  # Specify content type
        },
        1000
    )
    print(f"Generated PUT presigned URL: {url}")

if __name__ == "__main__":
    main()
```

2. To generate a `PUT` presigned URL for uploading a file, run the
   following script with your bucket name and desired object path.

The following command uses example values. Replace the `user input
 placeholders` with your own information.

```
python `put-only-url.py` ``amzn-s3-demo-bucket`` `<object-path>` --region `us-east-1` --content-type `application/octet-stream`
```

The script will output a `PUT` presigned URL:

```
Generated PUT presigned URL: https://`amzn-s3-demo-bucket`.s3.amazonaws.com/`object.txt`?AWSAccessKeyId=`AKIAIOSFODNN7EXAMPLE`&Signature=`vjbyNxybdZaMmLa%2ByT372YEAiv4%3D`&Expires=`1741978496`
```

3. You can now upload the file using the generated presigned URL with curl. Make sure to include the same content type that was used when generating the URL:

```
curl -X PUT -T `"path/to/your/local/file"` -H "Content-Type: application/octet-stream" `"generated-presigned-url"`
```

If you specified a different content type when generating the URL, make sure to use that same content type in the curl command.

For more examples of using the AWS SDKs to generate a presigned URL for uploading an object, see
[Create a presigned URL for Amazon S3 by using an AWS SDK](../API/s3_example_s3_Scenario_PresignedUrl_section.md "../API/s3_example_s3_Scenario_PresignedUrl_section.md").

###### Troubleshooting SignatureDoesNotMatch errors

If you encounter a `SignatureDoesNotMatch` error when using presigned URLs, check the following:

- Verify your system time is synchronized with a reliable time server
- Ensure you're using the URL exactly as generated, without any modifications
- Check if the URL has expired and generate a new one if needed
- Make sure the content type in your upload request matches the content type specified when generating the URL
- Confirm you're using the correct region for the bucket
- When using curl, enclose the URL in quotes to properly handle special characters
