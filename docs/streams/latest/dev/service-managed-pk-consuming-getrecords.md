

# GetRecords API behavior
<a name="service-managed-pk-consuming-getrecords"></a>

When reading records from a service-managed stream using the [GetRecords](https://docs.aws.amazon.com/kinesis/latest/APIReference/API_GetRecords.html) API, the response includes the following behavior for each record:
+ **PartitionKey** – Returns `null` if the producer did not provide a partition key when writing the record. If the producer provided a partition key (which was ignored for shard placement), the original value is returned as-is.
+ **SequenceNumber** – Returned normally. Sequence numbers continue to be assigned to each record regardless of distribution strategy.
+ **ApproximateArrivalTimestamp** – Returned normally.
+ **Data** – Returned normally. Record data is unaffected by the distribution strategy.

**Example GetRecords response for a service-managed stream**  

```
{
    "Records": [
        {
            "SequenceNumber": "49654108311168735921334927185702664421081712646",
            "ApproximateArrivalTimestamp": 1719849600.123,
            "Data": "eyJtZXRyaWMiOiAiY3B1X3V0aWxpemF0aW9uIiwgInZhbHVlIjogNzIuNX0=",
            "PartitionKey": null,
            "EncryptionType": "KMS"
        },
        {
            "SequenceNumber": "49654108311168735921334927186891775532192823757",
            "ApproximateArrivalTimestamp": 1719849600.456,
            "Data": "eyJldmVudCI6ICJwYWdlX3ZpZXciLCAicGFnZSI6ICIvaG9tZSJ9",
            "PartitionKey": "device-12345",
            "EncryptionType": "KMS"
        }
    ],
    "NextShardIterator": "EXAMPLEShardIterator1234567890EXAMPLE",
    "MillisBehindLatest": 0
}
```

**Note**  
In the example above, the first record was written without a partition key (the producer omitted it), so `PartitionKey` is `null`. The second record was written with a partition key (which was ignored for distribution purposes), so the original value is returned.