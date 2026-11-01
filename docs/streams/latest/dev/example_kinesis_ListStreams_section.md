

# Use `ListStreams` with an AWS SDK or CLI
<a name="example_kinesis_ListStreams_section"></a>

The following code examples show how to use `ListStreams`.

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
    /// Retrieves and displays a list of existing Amazon Kinesis streams.
    /// </summary>
    public class ListStreams
    {
        public static async Task Main(string[] args)
        {
            IAmazonKinesis client = new AmazonKinesisClient();
            var response = await client.ListStreamsAsync(new ListStreamsRequest());

            List<string> streamNames = response.StreamNames;

            if (streamNames.Count > 0)
            {
                streamNames
                    .ForEach(s => Console.WriteLine($"Stream name: {s}"));
            }
            else
            {
                Console.WriteLine("No streams were found.");
            }
        }
    }
```
+  For API details, see [ListStreams](https://docs.aws.amazon.com/goto/DotNetSDKV3/kinesis-2013-12-02/ListStreams) in *AWS SDK for .NET API Reference*. 

------
#### [ CLI ]

**AWS CLI**  
**To list data streams**  
The following `list-streams` example lists all active data streams in the current account and region.  

```
aws kinesis list-streams
```
Output:  

```
{
    "StreamNames": [
        "samplestream",
        "samplestream1"
    ]
}
```
For more information, see [Listing Streams](https://docs.aws.amazon.com/streams/latest/dev/kinesis-using-sdk-java-list-streams.html) in the *Amazon Kinesis Data Streams Developer Guide*.  
+  For API details, see [ListStreams](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kinesis/list-streams.html) in *AWS CLI Command Reference*. 

------
#### [ Python ]

**SDK for Python (Boto3)**  
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/kinesis#code-examples). 

```
    def list_streams(self, limit=100):
        """
        Lists Kinesis data streams in the account.

        :param limit: The maximum number of streams to list.
        :return: A list of stream summary dictionaries.
        """
        try:
            streams = list()
            response = self.kinesis_client.list_streams(Limit=limit)
            streams.extend(response.get("StreamSummaries", list()))
            while response.get("HasMoreStreams", False):
                summaries = response.get("StreamSummaries", list())
                if not summaries:
                    break
                next_name = summaries[-1]["StreamName"]
                response = self.kinesis_client.list_streams(
                    Limit=limit, ExclusiveStartStreamName=next_name
                )
                streams.extend(response.get("StreamSummaries", list()))
            logger.info("Listed %s stream(s).", len(streams))
            return streams
        except ClientError as err:
            if err.response["Error"]["Code"] == "LimitExceededException":
                logger.error(
                    "Request rate too high for ListStreams. Retry after a brief delay."
                )
            raise
```
+  For API details, see [ListStreams](https://docs.aws.amazon.com/goto/boto3/kinesis-2013-12-02/ListStreams) in *AWS SDK for Python (Boto3) API Reference*. 

------
#### [ Rust ]

**SDK for Rust**  
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/rustv1/examples/kinesis#code-examples). 

```
async fn show_streams(client: &Client) -> Result<(), Error> {
    let resp = client.list_streams().send().await?;

    println!("Stream names:");

    let streams = resp.stream_names;
    for stream in &streams {
        println!("  {}", stream);
    }

    println!("Found {} stream(s)", streams.len());

    Ok(())
}
```
+  For API details, see [ListStreams](https://docs.rs/aws-sdk-kinesis/latest/aws_sdk_kinesis/client/struct.Client.html#method.list_streams) in *AWS SDK for Rust API reference*. 

------
#### [ SAP ABAP ]

**SDK for SAP ABAP**  
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/sap-abap/services/kns#code-examples). 

```
    TRY.
        oo_result = lo_kns->liststreams(        " oo_result is returned for testing purposes. "
            "Set Limit to specify that a maximum of streams should be returned."
            iv_limit = iv_limit ).
        DATA(lt_streams) = oo_result->get_streamnames( ).
        MESSAGE 'Streams listed.' TYPE 'I'.
      CATCH /aws1/cx_knslimitexceededex.
        MESSAGE 'The request processing has failed because of a limit exceed exception.' TYPE 'E'.
    ENDTRY.
```
+  For API details, see [ListStreams](https://docs.aws.amazon.com/sdk-for-sap-abap/v1/api/latest/index.html) in *AWS SDK for SAP ABAP API reference*. 

------

For a complete list of AWS SDK developer guides and code examples, see [Using this service with an AWS SDK](sdk-general-information-section.md). This topic also includes information about getting started and details about previous SDK versions.