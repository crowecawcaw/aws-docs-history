

# Use `ListTagsForStream` with an AWS SDK or CLI
<a name="example_kinesis_ListTagsForStream_section"></a>

The following code examples show how to use `ListTagsForStream`.

Action examples are code excerpts from larger programs and must be run in context. You can see this action in context in the following code example: 
+  [Learn the basics](example_kinesis_Scenario_GettingStarted_section.md) 

------
#### [ .NET ]

**SDK for .NET**  
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/dotnetv3/Kinesis#code-examples). 

```
    using System;
    using System.Collections.Generic;
    using System.Threading.Tasks;
    using Amazon.Kinesis;
    using Amazon.Kinesis.Model;

    /// <summary>
    /// Shows how to list the tags that have been attached to an Amazon Kinesis
    /// stream.
    /// </summary>
    public class ListTags
    {
        public static async Task Main()
        {
            IAmazonKinesis client = new AmazonKinesisClient();
            string streamName = "AmazonKinesisStream";

            await ListTagsAsync(client, streamName);
        }

        /// <summary>
        /// List the tags attached to a Kinesis stream.
        /// </summary>
        /// <param name="client">An initialized Kinesis client object.</param>
        /// <param name="streamName">The name of the Kinesis stream for which you
        /// wish to display tags.</param>
        public static async Task ListTagsAsync(IAmazonKinesis client, string streamName)
        {
            var request = new ListTagsForStreamRequest
            {
                StreamName = streamName,
                Limit = 10,
            };

            var response = await client.ListTagsForStreamAsync(request);
            DisplayTags(response.Tags);

            while (response.HasMoreTags)
            {
                request.ExclusiveStartTagKey = response.Tags[response.Tags.Count - 1].Key;
                response = await client.ListTagsForStreamAsync(request);
            }
        }

        /// <summary>
        /// Displays the items in a list of Kinesis tags.
        /// </summary>
        /// <param name="tags">A list of the Tag objects to be displayed.</param>
        public static void DisplayTags(List<Tag> tags)
        {
            tags
                .ForEach(t => Console.WriteLine($"Key: {t.Key} Value: {t.Value}"));
        }
    }
```
+  For API details, see [ListTagsForStream](https://docs.aws.amazon.com/goto/DotNetSDKV3/kinesis-2013-12-02/ListTagsForStream) in *AWS SDK for .NET API Reference*. 

------
#### [ CLI ]

**AWS CLI**  
**To list tags for a data stream**  
The following `list-tags-for-stream` example lists the tags attached to the specified data stream.  

```
aws kinesis list-tags-for-stream \
    --stream-name {{samplestream}}
```
Output:  

```
{
    "Tags": [
        {
            "Key": "samplekey",
            "Value": "example"
        }
    ],
    "HasMoreTags": false
}
```
For more information, see [Tagging Your Streams](https://docs.aws.amazon.com/streams/latest/dev/tagging.html) in the *Amazon Kinesis Data Streams Developer Guide*.  
+  For API details, see [ListTagsForStream](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kinesis/list-tags-for-stream.html) in *AWS CLI Command Reference*. 

------
#### [ Python ]

**SDK for Python (Boto3)**  
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/kinesis#code-examples). 

```
    def list_tags_for_stream(self, stream_name):
        """
        Lists the tags for a Kinesis data stream.

        :param stream_name: The name of the stream whose tags to list.
        :return: A tuple of (list of tag dictionaries with 'Key' and 'Value',
                 bool indicating whether more tags are available).
        """
        try:
            response = self.kinesis_client.list_tags_for_stream(StreamName=stream_name)
            tags = response.get("Tags", list())
            has_more = response.get("HasMoreTags", False)
            logger.info(
                "Listed %s tag(s) for stream '%s'. HasMoreTags: %s.",
                len(tags),
                stream_name,
                has_more,
            )
            return tags, has_more
        except ClientError as err:
            if err.response["Error"]["Code"] == "ResourceNotFoundException":
                logger.error("Stream '%s' not found when listing tags.", stream_name)
            raise
```
+  For API details, see [ListTagsForStream](https://docs.aws.amazon.com/goto/boto3/kinesis-2013-12-02/ListTagsForStream) in *AWS SDK for Python (Boto3) API Reference*. 

------

For a complete list of AWS SDK developer guides and code examples, see [Using this service with an AWS SDK](sdk-general-information-section.md). This topic also includes information about getting started and details about previous SDK versions.