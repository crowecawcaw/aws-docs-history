# Transform source data in Amazon Data Firehose

Amazon Data Firehose can invoke your Lambda function to transform incoming source data and deliver the
transformed data to destinations. You can enable Amazon Data Firehose data transformation when you create
your Firehose stream.

## Understand data transformation flow

When you enable Firehose data transformation, Firehose buffers incoming data. The buffering
size hint ranges between 0.2 MB and 3MB. The default Lambda buffering size hint is 1 MB
for all destinations, except Splunk and Snowflake. For Splunk and Snowflake, the default
buffering hint is 256 KB. The Lambda buffering interval hint ranges between 0 and 900
seconds. The default Lambda buffering interval hint is sixty seconds for all
destinations except Snowflake. For Snowflake, the default buffering hint interval is 30
seconds. To adjust the buffering size, set the [ProcessingConfiguration](../APIReference/API_ProcessingConfiguration.md "../APIReference/API_ProcessingConfiguration.md") parameter of the [CreateDeliveryStream](../APIReference/API_CreateDeliveryStream.md "../APIReference/API_CreateDeliveryStream.md") or [UpdateDestination](../APIReference/API_UpdateDestination.md "../APIReference/API_UpdateDestination.md") API with the [ProcessorParameter](../APIReference/API_ProcessorParameter.md "../APIReference/API_ProcessorParameter.md") called `BufferSizeInMBs` and
`IntervalInSeconds`. Firehose then invokes the specified Lambda function
synchronously with each buffered batch using the AWS Lambda synchronous invocation mode.
The transformed data is sent from Lambda to Firehose. Firehose then sends it to the
destination when the specified destination buffering size or buffering interval is
reached, whichever happens first.

###### Important

The Lambda synchronous invocation mode has a payload size limit of 6 MB for both
the request and the response. Make sure that your buffering size for sending the
request to the function is less than or equal to 6 MB. Also ensure that the response
that your function returns doesn't exceed 6 MB.

## Lambda invocation

duration

Amazon Data Firehose supports a Lambda invocation time of up to 5 minutes. If your Lambda function
takes more than 5 minutes to complete, you get the following error: **`Firehose
 encountered timeout errors when calling AWS Lambda. The maximum supported function
 timeout is 5 minutes.`**

For information about what Amazon Data Firehose does if such an error occurs, see [Handle failure in data
transformation](data-transformation-failure-handling.md "data-transformation-failure-handling.md") .
