# Managing object tags

This section explains how you can manage object tags using the AWS SDKs for
Java and .NET or the Amazon S3 console.

Object tagging gives you a way to categorize storage in general purpose buckets. Each tag is a key-value pair
that adheres to the following rules:

- You can associate up to 10 tags with an object. Tags that are associated with an object must have unique tag keys.
- A tag key can be up to 128 Unicode characters in length, and tag values can be up to 256 Unicode characters in length. Amazon S3 object tags are internally represented in UTF-16. Note that in UTF-16, characters consume either 1 or 2 character positions.
- The key and values are case sensitive.
  For more information about object tags, see [Categorizing your objects using tags](object-tagging.md "object-tagging.md"). For more information about tag restrictions, see
  [User-Defined
  Tag Restrictions](../../../awsaccountbilling/latest/aboutv2/allocation-tag-restrictions.md "../../../awsaccountbilling/latest/aboutv2/allocation-tag-restrictions.md") in the _AWS Billing and Cost Management User Guide_.

###### To add tags to an object

1. Sign in to the AWS Management Console and open the Amazon S3 console at
   [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. In the left navigation pane, choose **General purpose buckets**.
3. In the bucket list, choose the name of the bucket that
   contains the object.
4. Select the check box to the left of the names of the objects you want to
   change.
5. In the **Actions** menu, choose **Edit
   tags**.
6. Review the objects listed, and choose **Add tags**.
7. Each object tag is a key-value pair. Enter a **Key** and a
   **Value**. To add another tag, choose **Add Tag**.

You can enter up to 10 tags for an object. 8. Choose **Save changes**.

Amazon S3 adds the tags to the specified objects.
For more information, see also
[Viewing object properties in the Amazon S3 console](view-object-properties.md "view-object-properties.md") and
[Uploading objects](upload-objects.md "upload-objects.md")
in this guide.

Java
To manage object tags using the AWS SDK for Java, you can set tags for a new object and retrieve or replace tags for an existing object. For more information about object tagging, see [Categorizing your objects using tags](object-tagging.md "object-tagging.md").

Upload an object to a bucket and set tags using an S3Client. For examples, see [Upload an object to a bucket](../API/s3_example_s3_PutObject_section.md "../API/s3_example_s3_PutObject_section.md") in the _Amazon S3 API Reference_.

.NET
The following example shows how to use the AWS SDK for .NET to set the tags for a new
object and retrieve or replace the tags for an existing object. For more information
about object tagging, see [Categorizing your objects using tags](object-tagging.md "object-tagging.md").

For
information about setting up and running the code examples, see [Getting Started
with the AWS SDK for .NET](../../../sdk-for-net/latest/developer-guide/net-dg-setup.md "../../../sdk-for-net/latest/developer-guide/net-dg-setup.md") in the _AWS SDK for .NET Developer
Guide_.

```
using Amazon;
using Amazon.S3;
using Amazon.S3.Model;
using System;
using System.Collections.Generic;
using System.Threading.Tasks;

namespace Amazon.DocSamples.S3
{
    public class ObjectTagsTest
    {
        private const string bucketName = "*** bucket name ***";
        private const string keyName = "*** key name for the new object ***";
        private const string filePath = @"*** file path ***";
        // Specify your bucket region (an example region is shown).
        private static readonly RegionEndpoint bucketRegion = RegionEndpoint.USWest2;
        private static IAmazonS3 client;

        public static void Main()
        {
            client = new AmazonS3Client(bucketRegion);
            PutObjectWithTagsTestAsync().Wait();
        }

        static async Task PutObjectWithTagsTestAsync()
        {
            try
            {
                // 1. Put an object with tags.
                var putRequest = new PutObjectRequest
                {
                    BucketName = bucketName,
                    Key = keyName,
                    FilePath = filePath,
                    TagSet = new List<Tag>{
                        new Tag { Key = "Keyx1", Value = "Value1"},
                        new Tag { Key = "Keyx2", Value = "Value2" }
                    }
                };

                PutObjectResponse response = await client.PutObjectAsync(putRequest);
                // 2. Retrieve the object's tags.
                GetObjectTaggingRequest getTagsRequest = new GetObjectTaggingRequest
                {
                    BucketName = bucketName,
                    Key = keyName
                };

                GetObjectTaggingResponse objectTags = await client.GetObjectTaggingAsync(getTagsRequest);
                for (int i = 0; i < objectTags.Tagging.Count; i++)
                    Console.WriteLine("Key: {0}, Value: {1}", objectTags.Tagging[i].Key, objectTags.Tagging[i].Value);


                // 3. Replace the tagset.

                Tagging newTagSet = new Tagging();
                newTagSet.TagSet = new List<Tag>{
                    new Tag { Key = "Key3", Value = "Value3"},
                    new Tag { Key = "Key4", Value = "Value4" }
                };


                PutObjectTaggingRequest putObjTagsRequest = new PutObjectTaggingRequest()
                {
                    BucketName = bucketName,
                    Key = keyName,
                    Tagging = newTagSet
                };
                PutObjectTaggingResponse response2 = await client.PutObjectTaggingAsync(putObjTagsRequest);

                // 4. Retrieve the object's tags.
                GetObjectTaggingRequest getTagsRequest2 = new GetObjectTaggingRequest();
                getTagsRequest2.BucketName = bucketName;
                getTagsRequest2.Key = keyName;
                GetObjectTaggingResponse objectTags2 = await client.GetObjectTaggingAsync(getTagsRequest2);
                for (int i = 0; i < objectTags2.Tagging.Count; i++)
                    Console.WriteLine("Key: {0}, Value: {1}", objectTags2.Tagging[i].Key, objectTags2.Tagging[i].Value);

            }
            catch (AmazonS3Exception e)
            {
                Console.WriteLine(
                        "Error encountered ***. Message:'{0}' when writing an object"
                        , e.Message);
            }
            catch (Exception e)
            {
                Console.WriteLine(
                    "Encountered an error. Message:'{0}' when writing an object"
                    , e.Message);
            }
        }
    }
}

```
