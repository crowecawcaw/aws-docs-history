# Deleting a single object

You can use the Amazon S3 console or the DELETE API to delete a single existing object from an
S3 bucket. For more information about deleting objects in Amazon S3, see [Deleting Amazon S3 objects](DeletingObjects.md "DeletingObjects.md").

Because all objects in your S3 bucket incur storage costs, you should delete objects that
you no longer need. For example, if you are collecting log files, it's a good idea to delete
them when they're no longer needed. You can set up a lifecycle rule to automatically delete
objects such as log files. For more information, see [Setting an S3 Lifecycle configuration on a bucket](how-to-set-lifecycle-configuration-intro.md "how-to-set-lifecycle-configuration-intro.md").

For information about Amazon S3 features and pricing, see [Amazon S3 pricing](https://aws.amazon.com/s3/pricing "https://aws.amazon.com/s3/pricing").

Follow these steps to use the Amazon S3 console to delete a single object from a bucket.

###### Warning

When you permanently delete an object or specified object version in the Amazon S3 console,
the deletion can't be undone.

###### To delete an object that has versioning enabled or suspended

###### Note

If the version ID for an object in a versioning-suspended bucket is
marked as `NULL`, S3 permanently deletes the object since no
previous versions exist. However, if a valid version ID is listed for the object
in a versioning-suspended bucket, then S3 creates a delete marker for the
deleted object, while retaining the previous versions of the object.

1. Sign in to the AWS Management Console and open the Amazon S3 console at
   [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. In the left navigation pane, choose **General purpose buckets** or **Directory buckets**.
3. In the bucket list, choose the name of the bucket that
   you want to delete an object from.
4. Select the object and then choose **Delete**.
5. To confirm deletion of the objects list under **Specified
   objects** in the **Delete objects?** text box,
   enter `delete`.

###### To permanently delete a specific object version in a versioning-enabled bucket

###### Warning

When you permanently delete a specific object version in Amazon S3, the deletion
can't be undone.

1. Sign in to the AWS Management Console and open the Amazon S3 console at
   [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. In the **Bucket name** list, choose the name of the bucket that
   you want to delete an object from.
3. Select the object that you want to delete.
4. Choose the **Show versions** toggle.
5. Select the object version and then choose
   **Delete**.
6. To confirm permanent deletion of the specific object versions listed under
   **Specified objects**, in the **Delete
   objects?** text box, enter **Permanently
   delete**. Amazon S3 permanently deletes the specific object
   version.

###### To permanently delete an object in an Amazon S3 bucket that _doesn't_ have versioning enabled

###### Warning

When you permanently delete an object in Amazon S3, the deletion can't be undone.
Also, for any buckets without versioning enabled, deletions are
permanent.

1. Sign in to the AWS Management Console and open the Amazon S3 console at
   [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. In the left navigation pane, choose **General purpose buckets**.
3. In the bucket list, choose the name of the bucket that
   you want to delete an object from.
4. Select the object and then choose **Delete**.
5. To confirm permanent deletion of the object listed under
   **Specified objects**, in the **Delete
   objects?** text box, enter **permanently
   delete**.

###### Note

If you're experiencing any issues with deleting your object, see [I want to permanently delete versioned objects](troubleshooting-versioning.md#delete-objects-permanent "troubleshooting-versioning.md#delete-objects-permanent").

To delete one object per request, use the `DELETE` API. For more
information, see [DELETE
Object](../API/RESTObjectDELETE.md "../API/RESTObjectDELETE.md"). For more information about using the CLI to delete an object,
see [delete-object](https://awscli.amazonaws.com/v2/documentation/api/2.0.34/reference/s3api/delete-object.html "https://awscli.amazonaws.com/v2/documentation/api/2.0.34/reference/s3api/delete-object.html").

You can use the AWS SDKs to delete an object. However, if your application
requires it, you can send REST requests directly. For more information, see [DELETE Object](../API/RESTObjectDELETE.md "../API/RESTObjectDELETE.md") in the
_Amazon Simple Storage Service API Reference_.

The following examples show how you can use the AWS SDKs to delete an object from a
bucket. For more information, see [DELETE
Object](../API/RESTObjectDELETE.md "../API/RESTObjectDELETE.md") in the _Amazon Simple Storage Service API Reference_

If you have S3 Versioning enabled on the bucket, you have the following options:

- Delete a specific object version by specifying a version ID.
- Delete an object without specifying a version ID, in which case Amazon S3 adds a delete
  marker to the object.
  For more information about S3 Versioning, see [Retaining multiple versions of objects with S3 Versioning](Versioning.md "Versioning.md").

For more examples, and examples in other languages, see [Use `DeleteObject` with an AWS SDK or CLI](../API/s3_example_s3_DeleteObject_section.md "../API/s3_example_s3_DeleteObject_section.md") in the _Amazon S3 API reference_.

Java
To delete objects using the AWS SDK for Java, you can delete objects from both versioned and non-versioned buckets:

- _Non-versioned bucket:_ In the delete request, you specify only the object key and not a version ID.
- _Versioned bucket:_ You can delete a specific object version by specifying both the object key name and version ID. If there are no other versions of that object, Amazon S3 deletes the object entirely. Otherwise, Amazon S3 only deletes the specified version.

###### Note

You can get the version IDs of an object by sending a `ListVersions` request.

For examples of how to delete a single object with the AWS SDK for Java, see [Delete an object](../API/s3_example_s3_DeleteObject_section.md "../API/s3_example_s3_DeleteObject_section.md") in the _Amazon S3 API Reference_.

.NET
The following examples show how to delete an object from both versioned and
non-versioned buckets. For more information about S3 Versioning, see [Retaining multiple versions of objects with S3 Versioning](Versioning.md "Versioning.md").

###### Example Deleting an object from a non-versioned bucket

The following C# example deletes an object from a non-versioned bucket.
The example assumes that the objects don't have version IDs, so you don't
specify version IDs. You specify only the object key.

For
information about setting up and running the code examples, see [Getting Started
with the AWS SDK for .NET](../../../sdk-for-net/latest/developer-guide/net-dg-setup.md "../../../sdk-for-net/latest/developer-guide/net-dg-setup.md") in the _AWS SDK for .NET Developer
Guide_.

```
using Amazon;
using Amazon.S3;
using Amazon.S3.Model;
using System;
using System.Threading.Tasks;

namespace Amazon.DocSamples.S3
{
    class DeleteObjectNonVersionedBucketTest
    {
        private const string bucketName = "*** bucket name ***";
        private const string keyName = "*** object key ***";
        // Specify your bucket region (an example region is shown).
        private static readonly RegionEndpoint bucketRegion = RegionEndpoint.USWest2;
        private static IAmazonS3 client;

        public static void Main()
        {
            client = new AmazonS3Client(bucketRegion);
            DeleteObjectNonVersionedBucketAsync().Wait();
        }
        private static async Task DeleteObjectNonVersionedBucketAsync()
        {
            try
            {
                var deleteObjectRequest = new DeleteObjectRequest
                {
                    BucketName = bucketName,
                    Key = keyName
                };

                Console.WriteLine("Deleting an object");
                await client.DeleteObjectAsync(deleteObjectRequest);
            }
            catch (AmazonS3Exception e)
            {
                Console.WriteLine("Error encountered on server. Message:'{0}' when deleting an object", e.Message);
            }
            catch (Exception e)
            {
                Console.WriteLine("Unknown encountered on server. Message:'{0}' when deleting an object", e.Message);
            }
        }
    }
}

```

###### Example Deleting an object from a versioned bucket

The following C# example deletes an object from a versioned bucket. It
deletes a specific version of the object by specifying the object key name
and version ID.

The code performs the following tasks:

1. Enables S3 Versioning on a bucket that you specify (if S3
   Versioning is already enabled, this has no effect).
2. Adds a sample object to the bucket. In response, Amazon S3 returns the
   version ID of the newly added object. The example uses this version
   ID in the delete request.
3. Deletes the sample object by specifying both the object key name
   and a version ID.

###### Note

You can also get the version ID of an object by sending a
`ListVersions` request.

```
var listResponse = client.ListVersions(new ListVersionsRequest { BucketName = bucketName, Prefix = keyName });
```

For
information about setting up and running the code examples, see [Getting Started
with the AWS SDK for .NET](../../../sdk-for-net/latest/developer-guide/net-dg-setup.md "../../../sdk-for-net/latest/developer-guide/net-dg-setup.md") in the _AWS SDK for .NET Developer
Guide_.

```
using Amazon;
using Amazon.S3;
using Amazon.S3.Model;
using System;
using System.Threading.Tasks;

namespace Amazon.DocSamples.S3
{
    class DeleteObjectVersion
    {
        private const string bucketName = "*** versioning-enabled bucket name ***";
        private const string keyName = "*** Object Key Name ***";
        // Specify your bucket region (an example region is shown).
        private static readonly RegionEndpoint bucketRegion = RegionEndpoint.USWest2;
        private static IAmazonS3 client;

        public static void Main()
        {
            client = new AmazonS3Client(bucketRegion);
            CreateAndDeleteObjectVersionAsync().Wait();
        }

        private static async Task CreateAndDeleteObjectVersionAsync()
        {
            try
            {
                // Add a sample object.
                string versionID = await PutAnObject(keyName);

                // Delete the object by specifying an object key and a version ID.
                DeleteObjectRequest request = new DeleteObjectRequest
                {
                    BucketName = bucketName,
                    Key = keyName,
                    VersionId = versionID
                };
                Console.WriteLine("Deleting an object");
                await client.DeleteObjectAsync(request);
            }
            catch (AmazonS3Exception e)
            {
                Console.WriteLine("Error encountered on server. Message:'{0}' when deleting an object", e.Message);
            }
            catch (Exception e)
            {
                Console.WriteLine("Unknown encountered on server. Message:'{0}' when deleting an object", e.Message);
            }
        }

        static async Task<string> PutAnObject(string objectKey)
        {
            PutObjectRequest request = new PutObjectRequest
            {
                BucketName = bucketName,
                Key = objectKey,
                ContentBody = "This is the content body!"
            };
            PutObjectResponse response = await client.PutObjectAsync(request);
            return response.VersionId;
        }
    }
}

```

PHP
This example shows how to use classes from version 3 of the AWS SDK for PHP to
delete an object from a non-versioned bucket. For information about deleting an
object from a versioned bucket, see [Using the REST API](DeletingAnObjectsUsingREST.md "DeletingAnObjectsUsingREST.md").

For more information about the AWS SDK for Ruby API, go to [AWS SDK for Ruby - Version
2](../../../sdkforruby/api/index.md "../../../sdkforruby/api/index.md").

The following PHP example deletes an object from a bucket. Because this
example shows how to delete objects from non-versioned buckets, it provides only
the bucket name and object key (not a version ID) in the delete request.

```
<?php

require 'vendor/autoload.php';

use Aws\S3\S3Client;
use Aws\S3\Exception\S3Exception;

$bucket = '*** Your Bucket Name ***';
$keyname = '*** Your Object Key ***';

$s3 = new S3Client([
    'version' => 'latest',
    'region'  => 'us-east-1'
]);

// 1. Delete the object from the bucket.
try
{
    echo 'Attempting to delete ' . $keyname . '...' . PHP_EOL;

    $result = $s3->deleteObject([
        'Bucket' => $bucket,
        'Key'    => $keyname
    ]);

    if ($result['DeleteMarker'])
    {
        echo $keyname . ' was deleted or does not exist.' . PHP_EOL;
    } else {
        exit('Error: ' . $keyname . ' was not deleted.' . PHP_EOL);
    }
}
catch (S3Exception $e) {
    exit('Error: ' . $e->getAwsErrorMessage() . PHP_EOL);
}

// 2. Check to see if the object was deleted.
try
{
    echo 'Checking to see if ' . $keyname . ' still exists...' . PHP_EOL;

    $result = $s3->getObject([
        'Bucket' => $bucket,
        'Key'    => $keyname
    ]);

    echo 'Error: ' . $keyname . ' still exists.';
}
catch (S3Exception $e) {
    exit($e->getAwsErrorMessage());
}

```

Javascript

```
import { DeleteObjectCommand } from "@aws-sdk/client-s3";
import { s3Client } from "./libs/s3Client.js" // Helper function that creates Amazon S3 service client module.

export const bucketParams = { Bucket: "BUCKET_NAME", Key: "KEY" };

export const run = async () => {
  try {
    const data = await s3Client.send(new DeleteObjectCommand(bucketParams));
    console.log("Success. Object deleted.", data);
    return data; // For unit tests.
  } catch (err) {
    console.log("Error", err);
  }
};
run();

```
