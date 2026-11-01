

# Hello
<a name="example_kinesis_Hello_section"></a>

The following code example shows how to get started using .

------
#### [ Python ]

**SDK for Python (Boto3)**  
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/kinesis#code-examples). 

```
import logging

import boto3
from botocore.exceptions import ClientError

logger = logging.getLogger(__name__)


def hello_kinesis():
    """
    Lists Kinesis data streams with a limit of 10 and displays the results.
    Use this example to verify that your environment is configured correctly.
    """
    kinesis_client = boto3.client("kinesis")
    print("Hello, Amazon Kinesis! Let's list some of your streams:\n")
    try:
        response = kinesis_client.list_streams(Limit=10)
        stream_summaries = response.get("StreamSummaries", list())
        if stream_summaries:
            for summary in stream_summaries:
                print(f"  Stream: {summary['StreamName']}")
            print(f"\nFound {len(stream_summaries)} stream(s).")
        else:
            print("No streams found in your account.")
    except ClientError as err:
        if err.response["Error"]["Code"] == "LimitExceededException":
            logger.error("Request rate too high. Retry after a brief delay.")
        else:
            logger.error(
                "Error listing streams: %s: %s",
                err.response["Error"]["Code"],
                err.response["Error"]["Message"],
            )
        raise


if __name__ == "__main__":
    hello_kinesis()
```
+  For API details, see [ListStreams](https://docs.aws.amazon.com/goto/boto3/kinesis-2013-12-02/ListStreams) in *AWS SDK for Python (Boto3) API Reference*. 

------

For a complete list of AWS SDK developer guides and code examples, see [Using this service with an AWS SDK](sdk-general-information-section.md). This topic also includes information about getting started and details about previous SDK versions.