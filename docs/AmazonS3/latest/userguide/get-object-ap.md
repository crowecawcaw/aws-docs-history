

# Download an object through an access point for a general purpose bucket
<a name="get-object-ap"></a>

This section explains how to download an object through an access point for a general purpose bucket using the AWS Management Console, AWS Command Line Interface, or REST API.

## Using the S3 console
<a name="get-object-ap-console"></a>

**To download an object through an access point in your AWS account**

1. Sign in to the AWS Management Console and open the Amazon S3 console at [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/).

1. In the navigation bar on the top of the page, choose the name of the currently displayed AWS Region. Next, choose the Region that you want to list access points for. 

1. In the navigation pane on the left side of the console, choose **Access Points**.

1. (Optional) Search for access points by name. Only access points in your selected AWS Region will appear here.

1. Choose the name of the access point you want to manage or use.

1. Under the **Objects** tab, select the name of object that you want to download.

1. Choose **Download**.

## Using the AWS CLI
<a name="get-object-ap-cli"></a>

The following `get-object` example command shows how you can use the AWS CLI to download an object through an access point.

The following command downloads the object `puppy.jpg` for AWS account {{111122223333}} using access point {{my-access-point}}. You must include an `outfile`, which is a file name for the downloaded object, such as `{{my_downloaded_image.jpg}}`.

```
aws s3api get-object --bucket arn:aws:s3:{{AWS Region}}:111122223333:accesspoint/{{my-access-point}} --key puppy.jpg {{my_downloaded_image.jpg}}      
```

**Note**  
S3 automatically generate access point aliases for all access points and these aliases can be used anywhere a bucket name is used to perform object-level operations. For more information, see [Access point aliases](access-points-naming.md#access-points-alias).

For more information and examples, see [get-object](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/get-object.html) in the *AWS CLI Command Reference*.

## Using the REST API
<a name="get-object-ap-rest"></a>

You can use the REST API to download an object through an access point. For more information, see [GetObject](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetObject.html) in the *Amazon Simple Storage Service API Reference*.

## Using the AWS SDKs
<a name="download-object-ap-SDKs"></a>

You can use the AWS SDK for Python to download an object through an access point. 

------
#### [ Python ]

In the following example, the file named `{{hello.txt}}` is downloaded for AWS account {{111122223333}} using the access point named {{my-access-point}}.

```
import boto3
s3 = boto3.client('s3')
s3.download_file('arn:aws:s3:{{us-east-1}}:{{111122223333}}:accesspoint/{{my-access-point}}', '{{hello.txt}}', '{{/tmp/hello.txt}}')
```

------