

# Use `RemoveTagsFromStream` with an AWS SDK or CLI
<a name="example_kinesis_RemoveTagsFromStream_section"></a>

The following code examples show how to use `RemoveTagsFromStream`.

Action examples are code excerpts from larger programs and must be run in context. You can see this action in context in the following code example: 
+  [Learn the basics](example_kinesis_Scenario_GettingStarted_section.md) 

------
#### [ CLI ]

**AWS CLI**  
**To remove tags from a data stream**  
The following `remove-tags-from-stream` example removes the tag with the specified key from the specified data stream.  

```
aws kinesis remove-tags-from-stream \
    --stream-name {{samplestream}} \
    --tag-keys {{samplekey}}
```
This command produces no output.  
For more information, see [Tagging Your Streams](https://docs.aws.amazon.com/streams/latest/dev/tagging.html) in the *Amazon Kinesis Data Streams Developer Guide*.  
+  For API details, see [RemoveTagsFromStream](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kinesis/remove-tags-from-stream.html) in *AWS CLI Command Reference*. 

------
#### [ Python ]

**SDK for Python (Boto3)**  
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/kinesis#code-examples). 

```
    def remove_tags_from_stream(self, stream_name, tag_keys):
        """
        Removes tags from a Kinesis data stream.

        :param stream_name: The name of the stream to remove tags from.
        :param tag_keys: A list of tag keys to remove.
        """
        try:
            self.kinesis_client.remove_tags_from_stream(
                StreamName=stream_name, TagKeys=tag_keys
            )
            logger.info("Removed tag(s) %s from stream '%s'.", tag_keys, stream_name)
        except ClientError as err:
            if err.response["Error"]["Code"] == "ResourceNotFoundException":
                logger.error("Stream '%s' not found for tag removal.", stream_name)
            raise
```
+  For API details, see [RemoveTagsFromStream](https://docs.aws.amazon.com/goto/boto3/kinesis-2013-12-02/RemoveTagsFromStream) in *AWS SDK for Python (Boto3) API Reference*. 

------

For a complete list of AWS SDK developer guides and code examples, see [Using this service with an AWS SDK](sdk-general-information-section.md). This topic also includes information about getting started and details about previous SDK versions.