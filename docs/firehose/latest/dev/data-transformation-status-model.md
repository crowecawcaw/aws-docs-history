# Required parameters for data

transformation

All transformed records from Lambda must contain the following parameters, or Amazon Data Firehose
rejects them and treats that as a data transformation failure.

For Kinesis Data Streams and Direct PUTThe following parameters are required for all transformed records from Lambda.

- `recordId` – The record ID is passed from Amazon Data Firehose to Lambda during the
  invocation. The transformed record must contain the same record ID.
  Any mismatch between the ID of the original record and the ID of the
  transformed record is treated as a data transformation
  failure.
- `result` – The status of the data transformation of the record. The possible
  values are: `Ok` (the record was transformed
  successfully), `Dropped` (the record was dropped
  intentionally by your processing logic), and
  `ProcessingFailed` (the record could not be
  transformed). If a record has a status of `Ok` or
  `Dropped`, Amazon Data Firehose considers it successfully
  processed. Otherwise, Amazon Data Firehose considers it unsuccessfully
  processed.
- `data` – The transformed data payload, after base64-encoding.

Following is a sample Lambda result output:

```
 {
    "recordId": `"<recordId from the Lambda input>"`,
    "result": "Ok",
    "data": `"<Base64 encoded Transformed data>"`
}
```

For Amazon MSK
The following parameters are required for all transformed records from
Lambda.

- `recordId` – The record ID is passed from Firehose to Lambda during the
  invocation. The transformed record must contain the same record ID.
  Any mismatch between the ID of the original record and the ID of the
  transformed record is treated as a data transformation
  failure.
- `result` – The status of the data transformation of the record. The possible
  values are: `Ok` (the record was transformed
  successfully), `Dropped` (the record was dropped
  intentionally by your processing logic), and
  `ProcessingFailed` (the record could not be
  transformed). If a record has a status of `Ok` or
  `Dropped`, Firehose considers it successfully processed.
  Otherwise, Firehose considers it unsuccessfully processed.
- `KafkaRecordValue` – The transformed data payload, after
  base64-encoding.

Following is a sample Lambda result output:

```
 {
    "recordId": `"<recordId from the Lambda input>"`,
    "result": "Ok",
    "kafkaRecordValue": `"<Base64 encoded Transformed data>"`
}
```
