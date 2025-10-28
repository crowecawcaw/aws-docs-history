# Handling errors for data format conversion

When Amazon Data Firehose can't parse or deserialize a record (for example, when the data doesn't
match the schema), it writes it to Amazon S3 with an error prefix. If this write fails, Amazon Data Firehose
retries it forever, blocking further delivery. For each failed record, Amazon Data Firehose writes a
JSON document with the following schema:

```
{
  "attemptsMade": long,
  "arrivalTimestamp": long,
  "ErrorCode": string,
  "ErrorMessage": string,
  "attemptEndingTimestamp": long,
  "rawData": string,
  "sequenceNumber": string,
  "subSequenceNumber": long,
  "dataCatalogTable": {
    "catalogId": string,
    "databaseName": string,
    "tableName": string,
    "region": string,
    "versionId": string,
    "catalogArn": string
  }
}
```
