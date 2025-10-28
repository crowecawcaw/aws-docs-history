# Understand partitioning keys

With dynamic partitioning, you create targeted data sets from the streaming S3 data by
partitioning the data based on partitioning keys. Partitioning keys enable you to filter
your streaming data based on specific values. For example, if you need to filter your
data based on customer ID and country, you can specify the data field of
`customer_id` as one partitioning key and the data field of
`country` as another partitioning key. Then, you specify the expressions
(using the supported formats) to define the S3 bucket prefixes to which the dynamically
partitioned data records are to be delivered.

You can create partitioning keys with the following methods.

- **Inline parsing** – this method uses
  Firehose built-in support mechanism, a [jq parser](https://stedolan.github.io/jq/ "https://stedolan.github.io/jq/"), for extracting the keys for partitioning from data
  records that are in JSON format. Currently, we only support `jq 1.6`
  version.
- **AWS Lambda function** – this method
  uses a specified AWS Lambda function to extract and return the data fields needed
  for partitioning.

###### Important

When you enable dynamic partitioning, you must configure at least one of these
methods to partition your data. You can configure either of these methods to specify
your partitioning keys or both of them at the same time.

## Create partitioning keys with inline

parsing

To configure inline parsing as the dynamic partitioning method for your streaming
data, you must choose data record parameters to be used as partitioning keys and
provide a value for each specified partitioning key.

The following sample data record shows how you can define partitioning keys for it
with inline parsing. Note that the data should be encoded in Base64 format. You can
also refer to the [CLI example](../../../cli/latest/reference/firehose/put-record.md#examples "../../../cli/latest/reference/firehose/put-record.md#examples").

```
{
   "type": {
    "device": "mobile",
    "event": "user_clicked_submit_button"
  },
  "customer_id": "1234567890",
  "event_timestamp": 1565382027,   #epoch timestamp
  "region": "sample_region"
}

```

For example, you can choose to partition your data based on the
`customer_id` parameter or the `event_timestamp`
parameter. This means that you want the value of the `customer_id`
parameter or the `event_timestamp` parameter in each record to be used in
determining the S3 prefix to which the record is to be delivered. You can also
choose a nested parameter, like `device` with an expression
`.type.device`. Your dynamic partitioning logic can depend on
multiple parameters.

After selecting data parameters for your partitioning keys, you then map each
parameter to a valid jq expression. The following table shows such a mapping of
parameters to jq expressions:

| Parameter     | jq expression    |
| ------------- | ---------------- | -------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `customer_id` | .customer_id     |
| `device`      | .type.device     |
| `year`        | .event_timestamp | strftime("%Y") |
| `month`       | .event_timestamp | strftime("%m") |
| `day`         | .event_timestamp | strftime("%d") |
| `hour`        | .event_timestamp | strftime("%H") | At runtime, Firehose uses the right column above to evaluate the parameters based on the data in each record. ## Create partitioning keys with an AWS Lambda function For compressed or encrypted data records, or data that is in any file format other than JSON, you can use the integrated AWS Lambda function with your own custom code to decompress, decrypt, or transform the records in order to extract and return the data fields needed for partitioning. This is an expansion of the existing transform Lambda function that is available today with Firehose. You can transform, parse and return the data fields that you can then use for dynamic partitioning using the same Lambda function. The following is an example Firehose stream processing Lambda function in Python that replays every read record from input to output and extracts partitioning keys from the records. `from __future__ import print_function import base64 import json import datetime # Signature for all Lambda functions that user must implement def lambda_handler(firehose_records_input, context): print("Received records for processing from DeliveryStream: " + firehose_records_input['deliveryStreamArn'] + ", Region: " + firehose_records_input['region'] + ", and InvocationId: " + firehose_records_input['invocationId']) # Create return value. firehose_records_output = {'records': []} # Create result object. # Go through records and process them for firehose_record_input in firehose_records_input['records']: # Get user payload payload = base64.b64decode(firehose_record_input['data']) json_value = json.loads(payload) print("Record that was received") print(json_value) print("\n") # Create output Firehose record and add modified payload and record ID to it. firehose_record_output = {} event_timestamp = datetime.datetime.fromtimestamp(json_value['eventTimestamp']) partition_keys = {"customerId": json_value['customerId'], "year": event_timestamp.strftime('%Y'), "month": event_timestamp.strftime('%m'), "day": event_timestamp.strftime('%d'), "hour": event_timestamp.strftime('%H'), "minute": event_timestamp.strftime('%M') } # Create output Firehose record and add modified payload and record ID to it. firehose_record_output = {'recordId': firehose_record_input['recordId'], 'data': firehose_record_input['data'], 'result': 'Ok', 'metadata': { 'partitionKeys': partition_keys }} # Must set proper record ID # Add the record to the list of output records. firehose_records_output['records'].append(firehose_record_output) # At the end return processed records return firehose_records_output` The following is an example Firehose stream processing Lambda function in Go that replays every read record from input to output and extracts partitioning keys from the records. ``package main import ( "fmt" "encoding/json" "time" "strconv" "github.com/aws/aws-lambda-go/events" "github.com/aws/aws-lambda-go/lambda" ) type DataFirehoseEventRecordData struct { CustomerId string `json:"customerId"` } func handleRequest(evnt events.DataFirehoseEvent) (events.DataFirehoseResponse, error) { fmt.Printf("InvocationID: %s\n", evnt.InvocationID) fmt.Printf("DeliveryStreamArn: %s\n", evnt.DeliveryStreamArn) fmt.Printf("Region: %s\n", evnt.Region) var response events.DataFirehoseResponse for _, record := range evnt.Records { fmt.Printf("RecordID: %s\n", record.RecordID) fmt.Printf("ApproximateArrivalTimestamp: %s\n", record.ApproximateArrivalTimestamp) var transformedRecord events.DataFirehoseResponseRecord transformedRecord.RecordID = record.RecordID transformedRecord.Result = events.DataFirehoseTransformedStateOk transformedRecord.Data = record.Data var metaData events.DataFirehoseResponseRecordMetadata var recordData DataFirehoseEventRecordData partitionKeys := make(map[string]string) currentTime := time.Now() json.Unmarshal(record.Data, &recordData) partitionKeys["customerId"] = recordData.CustomerId partitionKeys["year"] = strconv.Itoa(currentTime.Year()) partitionKeys["month"] = strconv.Itoa(int(currentTime.Month())) partitionKeys["date"] = strconv.Itoa(currentTime.Day()) partitionKeys["hour"] = strconv.Itoa(currentTime.Hour()) partitionKeys["minute"] = strconv.Itoa(currentTime.Minute()) metaData.PartitionKeys = partitionKeys transformedRecord.Metadata = metaData response.Records = append(response.Records, transformedRecord) } return response, nil } func main() { lambda.Start(handleRequest) }`` |
