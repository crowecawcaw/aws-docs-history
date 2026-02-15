# Listing directory buckets

The following examples show how to list directory buckets by using the AWS Management Console, AWS SDKs, and AWS CLI.

1. Sign in to the AWS Management Console and open the Amazon S3 console at
   [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. In the navigation bar on the top of the page, choose the name of the currently
   displayed AWS Region. Next, choose the Region in which you want to view a list of your directory buckets.
3. In the left navigation pane, choose **Directory buckets**. A list of directory buckets appears. To view the objects in the bucket,
   bucket properties, bucket permissions, metrics, access points associated with the bucket, or to manage the bucket, choose the bucket name.

SDK for Java 2.x

###### Example

The following example lists directory buckets by using the AWS SDK for Java 2.x.

```

 public static void listBuckets(S3Client s3Client) {
        try {
            ListDirectoryBucketsRequest listDirectoryBucketsRequest = ListDirectoryBucketsRequest.builder().build();
            ListDirectoryBucketsResponse response = s3Client.listDirectoryBuckets(listDirectoryBucketsRequest);
            if (response.hasBuckets()) {
                for (Bucket bucket: response.buckets()) {
                    System.out.println(bucket.name());
                    System.out.println(bucket.creationDate());
                }
            }
        }

        catch (S3Exception e) {
            System.err.println(e.awsErrorDetails().errorMessage());
            System.exit(1);
        }
    }

```

SDK for Python

###### Example

The following example lists directory buckets by using the AWS SDK for Python (Boto3).

```

import logging
import boto3
from botocore.exceptions import ClientError

def list_directory_buckets(s3_client):
'''
Prints a list of all directory buckets in a Region

:param s3_client: boto3 S3 client
:return: True if there are buckets in the Region, else False
'''
try:
    response = s3_client.list_directory_buckets()
    for bucket in response['Buckets']:
        print (bucket['Name'])
except ClientError as e:
    logging.error(e)
    return False
return True


if __name__ == '__main__':
    region = '`us-east-1`'
    s3_client = boto3.client('s3', region_name = region)
    list_directory_buckets(s3_client)
```

SDK for .NET

###### Example

The following example lists directory buckets by using the AWS SDK for .NET.

```

var listDirectoryBuckets = await amazonS3Client.ListDirectoryBucketsAsync(new ListDirectoryBucketsRequest
{
  MaxDirectoryBuckets = 10
  }).ConfigureAwait(false);

```

SDK for PHP

###### Example

The following example lists directory buckets by using the AWS SDK for PHP.

```

require 'vendor/autoload.php';

$s3Client = new S3Client([
    'region'      => '`us-east-1`',
]);
$result = $s3Client->listDirectoryBuckets();

```

SDK for Ruby

###### Example

The following example lists directory buckets by using the AWS SDK for Ruby.

```

s3 = Aws::S3::Client.new(region:'`us-west-1`')
s3.list_directory_buckets

```

The following `list-directory-buckets` example command shows how you can use
the AWS CLI to list your directory buckets in the `us-east-1`
region. To run this command, replace the `user input placeholders`
with your own information.

```
aws s3api list-directory-buckets --region `us-east-1`
```

For more information, see [list-directory-buckets](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/list-directory-buckets.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/list-directory-buckets.html") in the
_AWS CLI Command Reference_.
