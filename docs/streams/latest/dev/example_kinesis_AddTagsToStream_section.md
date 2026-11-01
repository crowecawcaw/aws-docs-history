

# Use `AddTagsToStream` with an AWS SDK or CLI
<a name="example_kinesis_AddTagsToStream_section"></a>

The following code examples show how to use `AddTagsToStream`.

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
    /// This example shows how to apply key/value pairs to an Amazon Kinesis
    /// stream.
    /// </summary>
    public class TagStream
    {
        public static async Task Main()
        {
            IAmazonKinesis client = new AmazonKinesisClient();

            string streamName = "AmazonKinesisStream";
            var tags = new Dictionary<string, string>
            {
                { "Project", "Sample Kinesis Project" },
                { "Application", "Sample Kinesis App" },
            };

            var success = await ApplyTagsToStreamAsync(client, streamName, tags);

            if (success)
            {
                Console.WriteLine($"Taggs successfully added to {streamName}.");
            }
            else
            {
                Console.WriteLine("Tags were not added to the stream.");
            }
        }

        /// <summary>
        /// Applies the set of tags to the named Kinesis stream.
        /// </summary>
        /// <param name="client">The initialized Kinesis client.</param>
        /// <param name="streamName">The name of the Kinesis stream to which
        /// the tags will be attached.</param>
        /// <param name="tags">A sictionary containing key/value pairs which
        /// will be used to create the Kinesis tags.</param>
        /// <returns>A Boolean value which represents the success or failure
        /// of AddTagsToStreamAsync.</returns>
        public static async Task<bool> ApplyTagsToStreamAsync(
            IAmazonKinesis client,
            string streamName,
            Dictionary<string, string> tags)
        {
            var request = new AddTagsToStreamRequest
            {
                StreamName = streamName,
                Tags = tags,
            };

            var response = await client.AddTagsToStreamAsync(request);

            return response.HttpStatusCode == System.Net.HttpStatusCode.OK;
        }
    }
```
+  For API details, see [AddTagsToStream](https://docs.aws.amazon.com/goto/DotNetSDKV3/kinesis-2013-12-02/AddTagsToStream) in *AWS SDK for .NET API Reference*. 

------
#### [ CLI ]

**AWS CLI**  
**To add tags to a data stream**  
The following `add-tags-to-stream` example assigns a tag with the key `samplekey` and value `example` to the specified stream.  

```
aws kinesis add-tags-to-stream \
    --stream-name {{samplestream}} \
    --tags {{samplekey=example}}
```
This command produces no output.  
For more information, see [Tagging Your Streams](https://docs.aws.amazon.com/streams/latest/dev/tagging.html) in the *Amazon Kinesis Data Streams Developer Guide*.  
+  For API details, see [AddTagsToStream](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kinesis/add-tags-to-stream.html) in *AWS CLI Command Reference*. 

------
#### [ Python ]

**SDK for Python (Boto3)**  
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/kinesis#code-examples). 

```
    def add_tags_to_stream(self, stream_name, tags):
        """
        Adds or updates tags for a Kinesis data stream.

        :param stream_name: The name of the stream to tag.
        :param tags: A dictionary of tag key-value pairs.
        """
        try:
            self.kinesis_client.add_tags_to_stream(StreamName=stream_name, Tags=tags)
            logger.info("Added %s tag(s) to stream '%s'.", len(tags), stream_name)
        except ClientError as err:
            if err.response["Error"]["Code"] == "ResourceNotFoundException":
                logger.error("Stream '%s' not found. Cannot add tags.", stream_name)
            raise
```
+  For API details, see [AddTagsToStream](https://docs.aws.amazon.com/goto/boto3/kinesis-2013-12-02/AddTagsToStream) in *AWS SDK for Python (Boto3) API Reference*. 

------

For a complete list of AWS SDK developer guides and code examples, see [Using this service with an AWS SDK](sdk-general-information-section.md). This topic also includes information about getting started and details about previous SDK versions.