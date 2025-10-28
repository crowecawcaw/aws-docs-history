# Use `AddTagsToStream` with an AWS SDK or CLI

The following code examples show how to use `AddTagsToStream`.

.NET

**SDK for .NET**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/dotnetv3/Kinesis#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/dotnetv3/Kinesis#code-examples").

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

- For API details, see
  [AddTagsToStream](../../../goto/DotNetSDKV3/kinesis-2013-12-02/AddTagsToStream.md "../../../goto/DotNetSDKV3/kinesis-2013-12-02/AddTagsToStream.md")
  in _AWS SDK for .NET API Reference_.

CLI

**AWS CLI**

**To add tags to a data stream**

The following `add-tags-to-stream` example assigns a tag with the key `samplekey` and value `example` to the specified stream.

```
`aws kinesis add-tags-to-stream \
 --stream-name `samplestream` \
 --tags `samplekey=example``

```

This command produces no output.

For more information, see [Tagging Your Streams](tagging.md "tagging.md") in the _Amazon Kinesis Data Streams Developer Guide_.

- For API details, see
  [AddTagsToStream](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kinesis/add-tags-to-stream.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kinesis/add-tags-to-stream.html")
  in _AWS CLI Command Reference_.

For a complete list of AWS SDK developer guides and code examples, see
[Using this service with an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.
