

# Enable decompression on an existing Firehose stream
<a name="enabling-decompression-existing-stream-console"></a>

This section provides instructions for enabling decompression on existing Firehose streams. It covers two scenarios – streams with Lambda processing disabled and streams with Lambda processing already enabled. The following sections outline step-by-step procedures for each case, including the creation or modification of Lambda functions, updating Firehose settings, and monitoring CloudWatch metrics to ensure successful implementation of the built-in Firehose decompression feature.

## Enabling decompression when Lambda processing is disabled
<a name="enabling-decomp-exist-stream-lam-disable"></a>

To enable decompression on an existing Firehose stream with Lambda processing disabled, you must first enable Lambda processing. This condition is only valid for existing streams. Following steps show how to enable decompression on existing streams that do not have Lambda processing enabled.

1. Create a Lambda function. You can either create a dummy record pass through or can use this [blueprint](https://github.com/aws-samples/aws-kinesis-firehose-resources/tree/main/blueprints/kinesis-firehose-cloudwatch-logs-processor) to create a new Lambda function. 

1. Update your current Firehose stream to enable Lambda processing and use the Lambda function that you created for processing.

1. Once you update the stream with new Lambda function, go back to Firehose console and enable decompression.

1. Disable the Lambda processing that you enabled in step 1. You can now delete the function that you created in step 1.

## Enabling decompression when Lambda processing is enabled
<a name="enabling-decomp-exist-stream-lam-enable"></a>

If you already have a Firehose stream with a Lambda function, to perform decompression you can replace it with the Firehose decompression feature. Before you proceed, review your Lambda function code to confirm that it only performs decompression or message extraction. The output of your Lambda function should look similar to the examples shown in [Fig 1 or Fig 2](Message_extraction.md). If the output looks similar, you can replace the Lambda function using the following steps.

1. Replace your current Lambda function with this [blueprint](https://github.com/aws-samples/aws-kinesis-firehose-resources/tree/main/blueprints/kinesis-firehose-cloudwatch-logs-processor). The new blueprint Lambda function automatically detects whether the incoming data is compressed or decompressed. It only performs decompression if its input data is compressed.

1. Turn on decompression using the built-in Firehose option for decompression.

1. Enable CloudWatch metrics for your Firehose stream if it's not already enabled. Monitor the metric `CloudWatchProcessorLambda_IncomingCompressedData` and wait until this metric changes to zero. This confirms that all input data sent to your Lambda function is decompressed and the Lambda function is no longer required.

1. Remove the Lambda data transformation because you no longer need it to decompress your stream.