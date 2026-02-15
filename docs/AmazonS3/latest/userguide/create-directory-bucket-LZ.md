# Creating a directory bucket in a Local Zone

In Dedicated Local Zones, you can create directory buckets to store and retrieve objects in a specific
data perimeter to help meet your data residency and data isolation use cases. S3
directory buckets are the only supported bucket type in Local Zones, and contain a bucket
location type called `LocalZone`. A directory bucket name consists of a base
name that you provide and a suffix that contains the Zone ID of your bucket location and
`--x-s3`. You can obtain a list of Local Zone IDs by using the [DescribeAvailabilityZones](../../../AWSEC2/latest/APIReference/API_DescribeAvailabilityZones.md "../../../AWSEC2/latest/APIReference/API_DescribeAvailabilityZones.md") API operation.
For more information, see [Directory bucket naming rules](directory-bucket-naming-rules.md "directory-bucket-naming-rules.md").

###### Note

- For all the services in AWS Dedicated Local Zones (Dedicated Local Zones), including S3, your administrator
  must enable your AWS account before you can create or access any resource in
  the Dedicated Local Zone. For more information, see [Enable accounts for Local Zones](opt-in-directory-bucket-lz.md "opt-in-directory-bucket-lz.md").
- For the data residency requirements, we recommend enabling access to your
  buckets only from gateway VPC endpoints. For more information, see [Private connectivity from your
  VPC](connectivity-lz-directory-buckets.md "connectivity-lz-directory-buckets.md").
- To restrict access to only within the Local Zone network border groups, you can use
  the condition key `s3express:AllAccessRestrictedToLocalZoneGroup` in
  your IAM policies. For more information, see [Authenticating and authorizing for
  directory buckets in Local Zones](iam-directory-bucket-LZ.md "iam-directory-bucket-LZ.md").
  The following describes ways to create a directory bucket in a single Local Zone with the
  AWS Management Console, AWS CLI, and AWS SDKs.

1. Sign in to the AWS Management Console and open the Amazon S3 console at
   [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. In the navigation bar on the top of the page, choose the name of the
   currently displayed AWS Region. Next, choose the parent Region of a Local Zone
   in which you want to create a directory bucket.

###### Note

For more information about the parent Regions, see [Concepts for directory buckets in
Local Zones](s3-lzs-for-directory-buckets.md "s3-lzs-for-directory-buckets.md"). 3. In the left navigation pane, choose **Buckets**. 4. Choose **Create bucket**.

The **Create bucket** page opens. 5. Under **General configuration**, view the AWS Region
where your bucket will be created. 6. Under **Bucket type**, choose
**Directory**.

###### Note

    * If you've chosen a Region that doesn't support directory
     buckets, the bucket type defaults to a general purpose bucket. To
     create a directory bucket, you must choose a supported Region.
     For a list of Regions that support directory buckets, see [Regional and Zonal endpoints for directory buckets](s3-express-Regions-and-Zones.md "s3-express-Regions-and-Zones.md").
    * After you create the bucket, you can't change the bucket
     type.

7. Under **Bucket location**, choose a Local Zone that you want to
   use.

###### Note

The Local Zone can't be changed after the bucket is created. 8. Under **Bucket location**, select the checkbox to
acknowledge that in the event of a Local Zone outage, your data might be
unavailable or lost.

###### Important

Although directory buckets are stored across multiple devices within
a single Local Zone, directory buckets don't store data redundantly across
Local Zones. 9. For **Bucket name**, enter a name for your
directory bucket.

For more information about the naming rules for directory buckets, see
[General purpose bucket naming rules](bucketnamingrules.md "bucketnamingrules.md"). A
suffix is automatically added to the base name that you provide when you
create a directory bucket using the console. This suffix includes the Zone
ID of the Local Zone that you chose.

After you create the bucket, you can't change its name.

###### Important

Don't include sensitive information, such as account numbers, in the
bucket name. The bucket name is visible in the URLs that point to the
objects in the bucket. 10. Under **Object Ownership**, the **Bucket owner
enforced** setting is automatically enabled, and all access
control lists (ACLs) are disabled. For directory buckets, ACLs are disabled
and can't be enabled.

With the **Bucket owner enforced** setting enabled, the
bucket owner automatically owns and has full control over every object in
the bucket. ACLs no longer affect access permissions to data in the S3
bucket. The bucket uses policies exclusively to define access control. A
majority of modern use cases in Amazon S3 no longer require the use of ACLs. For
more information, see [Controlling ownership of objects and disabling ACLs
for your bucket](about-object-ownership.md "about-object-ownership.md"). 11. Under **Block Public Access settings for this bucket**,
all Block Public Access settings for your directory bucket are automatically
enabled. These settings can't be modified for directory buckets. For more
information about blocking public access, see [Blocking public access to your Amazon S3
storage](access-control-block-public-access.md "access-control-block-public-access.md"). 12. Under **Default encryption**, directory buckets use
**Server-side encryption with Amazon S3 managed keys
(SSE-S3)** to encrypt data by default. You also have the option
to encrypt data in directory buckets with **Server-side encryption
with AWS Key Management Service keys (SSE-KMS)**. 13. Choose **Create bucket**.

After creating the bucket, you can add files and folders to the bucket.
For more information, see [Working with objects in a directory
bucket](directory-buckets-objects.md "directory-buckets-objects.md").
This example shows how to create a directory bucket in a Local Zone by using the
AWS CLI. To use the command, replace the `user input
 placeholders` with your own information.

When you create a directory bucket, you must provide configuration details and
use the following naming convention: ``bucket-base-name`--`zone-id`--x-s3`.

```
aws s3api create-bucket
--bucket `bucket-base-name`--`zone-id`--x-s3
--create-bucket-configuration 'Location={Type=LocalZone,Name=`local-zone-id`},Bucket={DataRedundancy=SingleLocalZone,Type=Directory}'
--region `parent-region-code`
```

For more information about Local Zone ID and Parent Region Code, see [Concepts for directory buckets in
Local Zones](s3-lzs-for-directory-buckets.md "s3-lzs-for-directory-buckets.md"). For more information about the
AWS CLI command, see [create-bucket](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/create-bucket.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/create-bucket.html") in the _AWS CLI Command Reference_.

SDK for Go
This example shows how to create a directory bucket in a Local Zone by
using the AWS SDK for Go.

###### Example

```
var bucket = "`bucket-base-name`--`zone-id`--x-s3" // The full directory bucket name

func runCreateBucket(c *s3.Client) {
    resp, err := c.CreateBucket(context.Background(), &s3.CreateBucketInput{
        Bucket: &bucket,
        CreateBucketConfiguration: &types.CreateBucketConfiguration{
            Location: &types.LocationInfo{
                Name: aws.String("`local-zone-id`"),
                Type: types.LocationTypeLocalZone,
            },
            Bucket: &types.BucketInfo{
                DataRedundancy: types.DataRedundancySingleLocalZone,
                Type:           types.BucketTypeDirectory,
            },
        },
    })
    var terr *types.BucketAlreadyOwnedByYou
    if errors.As(err, &terr) {
        fmt.Printf("BucketAlreadyOwnedByYou: %s\n", aws.ToString(terr.Message))
        fmt.Printf("noop...\n") // No operation performed, just printing a message
        return
    }
    if err != nil {
        log.Fatal(err)
    }

    fmt.Printf("bucket created at %s\n", aws.ToString(resp.Location))
}
```

SDK for Java 2.x
This example shows how to create a directory bucket in a Local Zone by
using the AWS SDK for Java 2.x.

###### Example

```
public static void createBucket(S3Client s3Client, String bucketName) {

    //Bucket name format is {base-bucket-name}--{local-zone-id}--x-s3
    //example: `doc-example-bucket`--`local-zone-id`--x-s3 is a valid name for a directory bucket created in a Local Zone.

    CreateBucketConfiguration bucketConfiguration = CreateBucketConfiguration.builder()
             .location(LocationInfo.builder()
                     .type(LocationType.LOCAL_ZONE)
                     .name("`local-zone-id`").build()) //this must match the Local Zone ID in your bucket name
             .bucket(BucketInfo.builder()
                    .type(BucketType.DIRECTORY)
                    .dataRedundancy(DataRedundancy.SINGLE_LOCAL_ZONE)
                    .build()).build();
    try {

             CreateBucketRequest bucketRequest = CreateBucketRequest.builder().bucket(bucketName).createBucketConfiguration(bucketConfiguration).build();
             CreateBucketResponse response = s3Client.createBucket(bucketRequest);
             System.out.println(response);
    }

    catch (S3Exception e) {
            System.err.println(e.awsErrorDetails().errorMessage());
            System.exit(1);
         }
    }


```

AWS SDK for JavaScript
This example shows how to create a directory bucket in a Local Zone by
using the AWS SDK for JavaScript.

###### Example

```
// file.mjs, run with Node.js v16 or higher
// To use with the preview build, place this in a folder
// inside the preview build directory, such as /aws-sdk-js-v3/workspace/

import { S3 } from "@aws-sdk/client-s3";

const region = "`parent-region-code`";
const zone = "`local-zone-id`";
const suffix = `${zone}--x-s3`;

const s3 = new S3({ region });

const bucketName = ``bucket-base-name`--${suffix}`; // Full directory bucket name

const createResponse = await s3.createBucket(
    { Bucket: bucketName,
      CreateBucketConfiguration: {Location: {Type: "LocalZone", Name: "`local-zone-id`"},
      Bucket: { Type: "Directory", DataRedundancy: "SingleLocalZone" }}
    }
   );
```

SDK for .NET
This example shows how to create a directory bucket in a Local Zone by
using the SDK for .NET.

###### Example

```
using (var amazonS3Client = new AmazonS3Client())
{
    var putBucketResponse = await amazonS3Client.PutBucketAsync(new PutBucketRequest
    {

       BucketName = "`bucket-base-name`--`local-zone-id`--x-s3",
       PutBucketConfiguration = new PutBucketConfiguration
       {
         BucketInfo = new BucketInfo { DataRedundancy = DataRedundancy.SingleLocalZone, Type = BucketType.Directory },
         Location = new LocationInfo { Name = "`local-zone-id`", Type = LocationType.LocalZone }
       }
     }).ConfigureAwait(false);
}
```

SDK for PHP
This example shows how to create a directory bucket in a Local Zone by
using the AWS SDK for PHP.

###### Example

```
require 'vendor/autoload.php';

$s3Client = new S3Client([

    'region'      => '`parent-region-code`',
]);


$result = $s3Client->createBucket([
    'Bucket' => '`bucket-base-name`--`local-zone-id`--x-s3',
    'CreateBucketConfiguration' => [
        'Location' => ['Name'=> '`local-zone-id`', 'Type'=> 'LocalZone'],
        'Bucket' => ["DataRedundancy" => "SingleLocalZone" ,"Type" => "Directory"]   ],
]);
```

SDK for Python
This example shows how to create a directory bucket in a Local Zone by
using the AWS SDK for Python (Boto3).

###### Example

```
import logging
import boto3
from botocore.exceptions import ClientError

def create_bucket(s3_client, bucket_name, local_zone):
    '''
    Create a directory bucket in a specified Local Zone

    :param s3_client: boto3 S3 client
    :param bucket_name: Bucket to create; for example, '`bucket-base-name`--`local-zone-id`--x-s3'
    :param local_zone: String; Local Zone ID to create the bucket in
    :return: True if bucket is created, else False
    '''

    try:
        bucket_config = {
                'Location': {
                    'Type': 'LocalZone',
                    'Name': local_zone
                },
                'Bucket': {
                    'Type': 'Directory',
                    'DataRedundancy': 'SingleLocalZone'
                }
            }
        s3_client.create_bucket(
            Bucket = bucket_name,
            CreateBucketConfiguration = bucket_config
        )
    except ClientError as e:
        logging.error(e)
        return False
    return True


if __name__ == '__main__':
    bucket_name = '`BUCKET_NAME`'
    region = '`parent-region-code`'
    local_zone = '`local-zone-id`'
    s3_client = boto3.client('s3', region_name = region)
    create_bucket(s3_client, bucket_name, local_zone)
```

SDK for Ruby
This example shows how to create an directory bucket in a Local Zone by
using the AWS SDK for Ruby.

###### Example

```
s3 = Aws::S3::Client.new(region:'`parent-region-code`')
s3.create_bucket(
  bucket: "`bucket-base-name`--`local-zone-id`--x-s3",
  create_bucket_configuration: {
    location: { name: '`local-zone-id`', type: 'LocalZone' },
    bucket: { data_redundancy: 'SingleLocalZone', type: 'Directory' }
  }
)
```
