# Sharing objects with presigned URLs

By default, all Amazon S3 objects are private, only the object owner has permission to access
them. However, the object owner may share objects with others by creating a presigned URL. A
presigned URL uses security credentials to grant time-limited permission to download objects. The
URL can be entered in a browser or used by a program to download the object. The credentials
used by the presigned URL are those of the AWS user who generated the URL.

For general information about presigned URLs, see [Download and upload objects with presigned
URLs](using-presigned-url.md "using-presigned-url.md").

You can create a presigned URL for sharing an object without writing any code by using the Amazon S3
console, AWS Explorer for Visual Studio (Windows), or AWS Toolkit for Visual Studio Code. You can also generate a presigned URL programmatically
by using the AWS Command Line Interface (AWS CLI) or the AWS SDKs.

You can use the Amazon S3 console to generate a presigned URL for sharing an object up to 5 TB
by following these steps. When using the console the maximum expiration time for a presigned URL
is 12 hours from the time of creation.

###### To generate a presigned URL by using the Amazon S3 console

1. Sign in to the AWS Management Console and open the Amazon S3 console at
   [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. In the left navigation pane, choose **General purpose
   buckets**.
3. In the **General purpose buckets** list, choose the name of the
   general purpose bucket that contains the object that you want a presigned URL for.
4. In the **Objects** list, select the object that you want to create
   a presigned URL for.
5. On the **Object actions** menu, choose **Share with a
   presigned URL**.
6. Specify how long you want the presigned URL to be valid.
7. Choose **Create presigned URL**.
8. When a confirmation appears, the URL is automatically copied to your clipboard. You
   will see a button to copy the presigned URL if you need to copy it again.
   The following example AWS CLI command generates a presigned URL for sharing an object from an
   Amazon S3 bucket. When you use the AWS CLI, the maximum expiration time for a presigned URL is 7 days
   from the time of creation. To use this example, replace the `user input
 placeholders` with your own information.

```
aws s3 presign s3://`amzn-s3-demo-bucket`/`mydoc.txt` --expires-in `604800`
```

The `--expires-in` parameter specifies the expiration time in seconds.

###### Note

For all AWS Regions launched after March 20, 2019 you need to specify the
`endpoint-url` and `AWS Region` with the request. For a list of
all the Amazon S3 Regions and endpoints, see [Regions
and Endpoints](../../../general/latest/gr/rande.md#s3_region "../../../general/latest/gr/rande.md#s3_region") in the _AWS General Reference_.

```
aws s3 presign s3://`amzn-s3-demo-bucket`/`mydoc.txt` --expires-in `604800` --region `af-south-1` --endpoint-url `https://s3.af-south-1.amazonaws.com`
```

For more information, see [presign](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3/presign.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3/presign.html") in the _AWS CLI Command
Reference_.

You can generate a presigned URL programmatically by using the AWS SDKs.

Python
The following Python script generates a `GET` presigned URL for
sharing an object.

1. Copy the contents of the script and save it as
   “`get-only-url.py`” file. To use the following
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
    args = parser.parse_args()

    # By default, this will use credentials from ~/.aws/credentials
    s3_client = boto3.client("s3")

    # The presigned URL is specified to expire in 1000 seconds
    url = generate_presigned_url(
        s3_client,
        "get_object",
        {"Bucket": args.bucket, "Key": args.key},
        1000
    )
    print(f"Generated GET presigned URL: {url}")

if __name__ == "__main__":
    main()
```

2. To generate a `GET` presigned URL for sharing a file, run the
   following script with your bucket name and desired object path.

The following command uses example values. Replace the `user input
 placeholders` with your own information.

```
python `get-only-url.py` ``amzn-s3-demo-bucket`` `<object-path>`
```

The script will output a `GET` presigned URL:

```
Generated GET presigned URL: https://`amzn-s3-demo-bucket`.s3.amazonaws.com/`object.txt`?AWSAccessKeyId=`AKIAIOSFODNN7EXAMPLE`&Signature=`vjbyNxybdZaMmLa%2ByT372YEAiv4%3D`&Expires=`1741978496`
```

3. You can download the file using the generated presigned URL with curl:

```
curl -X GET `"generated-presigned-url"` -o `"path/to/save/file"`
```

For more examples of using the AWS SDKs to generate a presigned URL for sharing an
object, see [Create a presigned URL for Amazon S3 by using an AWS
SDK](../API/s3_example_s3_Scenario_PresignedUrl_section.md "../API/s3_example_s3_Scenario_PresignedUrl_section.md").

###### Note

For all AWS Regions launched after March 20, 2019 you need to specify the
`endpoint-url` and `AWS Region` with the request. For a list of
all the Amazon S3 Regions and endpoints, see [Regions
and Endpoints](../../../general/latest/gr/rande.md#s3_region "../../../general/latest/gr/rande.md#s3_region") in the _AWS General Reference_.

###### Note

When using the AWS SDKs, the Tagging attribute must be a header and not a query
parameter. All other attributes can be passed as a parameter for the presigned URL.

###### Note

At this time, the AWS Toolkit for Visual Studio does not support Visual Studio for Mac.

1. Install the AWS Toolkit for Visual Studio using the following instructions, [Installing and setting up the Toolkit for Visual Studio](../../../toolkit-for-visual-studio/latest/user-guide/setup.md "../../../toolkit-for-visual-studio/latest/user-guide/setup.md") in the _AWS Toolkit for Visual Studio User Guide_.
2. Connect to AWS using the following steps, [Connecting to AWS](../../../AWSToolkitVS/latest/UserGuide/connect.md "../../../AWSToolkitVS/latest/UserGuide/connect.md") in the
   _AWS Toolkit for Visual Studio User Guide_.
3. In the left side panel labeled **AWS Explorer**, double-click the bucket containing your object.
4. Right-click the object you wish to have a presigned URL generated for and select **Create Pre-Signed URL...**.
5. In the pop-up window, set the expiration date and time for your presigned URL.
6. The **Object Key**, should pre-populate based on the object you selected.
7. Choose **GET** to specify that this presigned URL will be used for
   downloading an object.
8. Choose the **Generate** button.
9. To copy the URL to the clipboard, choose **Copy**.
10. To use the generated presigned URL, paste the URL into any browser.
    If you're using Visual Studio Code, you can generate a presigned URL to share an object
    without writing any code by using AWS Toolkit for Visual Studio Code. For general information, see [AWS Toolkit for Visual Studio Code](../../../toolkit-for-vscode/latest/userguide/welcome.md "../../../toolkit-for-vscode/latest/userguide/welcome.md") in the _AWS Toolkit for Visual Studio Code User Guide_.

For instructions on how to install the AWS Toolkit for Visual Studio Code, see [Installing the AWS Toolkit for Visual Studio Code](../../../toolkit-for-vscode/latest/userguide/setup-toolkit.md "../../../toolkit-for-vscode/latest/userguide/setup-toolkit.md") in
the _AWS Toolkit for Visual Studio Code User Guide_.

1. Connect to AWS using the following steps, [Connecting to AWS Toolkit for Visual Studio Code](../../../toolkit-for-vscode/latest/userguide/connect.md "../../../toolkit-for-vscode/latest/userguide/connect.md") in the
   _AWS Toolkit for Visual Studio Code User Guide_.
2. Select the AWS logo on the left panel in Visual Studio Code.
3. Under **EXPLORER**, select **S3**.
4. Choose a bucket and file and open the context menu (right-click).
5. Choose **Generate presigned URL**, and then set the expiration time (in
   minutes).
6. Press Enter, and the presigned URL will be copied to your clipboard.
