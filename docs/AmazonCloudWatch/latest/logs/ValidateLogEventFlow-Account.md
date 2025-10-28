# Validate the flow of log

events

After you create the account-level subscription filter policy, CloudWatch Logs
forwards all the incoming log events that match the filter pattern and
selection criteria to the stream that is encapsulated within the destination
stream called "**RecipientStream**". The destination owner
can verify that this is happening by using the **aws kinesis
get-shard-iterator** command to grab a Kinesis Data Streams shard, and using
the **aws kinesis get-records** command to fetch some Kinesis Data Streams
records:

```
`aws kinesis get-shard-iterator \
 --stream-name RecipientStream \
 --shard-id shardId-000000000000 \
 --shard-iterator-type TRIM_HORIZON`

{
    "ShardIterator":
    "AAAAAAAAAAFGU/kLvNggvndHq2UIFOw5PZc6F01s3e3afsSscRM70JSbjIefg2ub07nk1y6CDxYR1UoGHJNP4m4NFUetzfL+wev+e2P4djJg4L9wmXKvQYoE+rMUiFq+p4Cn3IgvqOb5dRA0yybNdRcdzvnC35KQANoHzzahKdRGb9v4scv+3vaq+f+OIK8zM5My8ID+g6rMo7UKWeI4+IWiKEXAMPLE"
}

`aws kinesis get-records \
 --limit 10 \
 --shard-iterator
 "AAAAAAAAAAFGU/kLvNggvndHq2UIFOw5PZc6F01s3e3afsSscRM70JSbjIefg2ub07nk1y6CDxYR1UoGHJNP4m4NFUetzfL+wev+e2P4djJg4L9wmXKvQYoE+rMUiFq+p4Cn3IgvqOb5dRA0yybNdRcdzvnC35KQANoHzzahKdRGb9v4scv+3vaq+f+OIK8zM5My8ID+g6rMo7UKWeI4+IWiKEXAMPLE"`
```

###### Note

You might need to rerun the `get-records` command a few
times before Kinesis Data Streams starts to return data.

You should see a response with an array of Kinesis Data Streams records. The data
attribute in the Kinesis Data Streams record is compressed in gzip format and then base64
encoded. You can examine the raw data from the command line using the
following Unix command:

```
echo -n "<`Content of Data`>" | base64 -d | zcat
```

The base64 decoded and decompressed data is formatted as JSON with the
following structure:

```
{
    "owner": "111111111111",
    "logGroup": "CloudTrail/logs",
    "logStream": "111111111111_CloudTrail/logs_us-east-1",
    "subscriptionFilters": [
        "RecipientStream"
    ],
    "messageType": "DATA_MESSAGE",
    "logEvents": [
        {
            "id": "3195310660696698337880902507980421114328961542429EXAMPLE",
            "timestamp": 1432826855000,
            "message": "{\"eventVersion\":\"1.03\",\"userIdentity\":{\"type\":\"Root\"}"
        },
        {
            "id": "3195310660696698337880902507980421114328961542429EXAMPLE",
            "timestamp": 1432826855000,
            "message": "{\"eventVersion\":\"1.03\",\"userIdentity\":{\"type\":\"Root\"}"
        },
        {
            "id": "3195310660696698337880902507980421114328961542429EXAMPLE",
            "timestamp": 1432826855000,
            "message": "{\"eventVersion\":\"1.03\",\"userIdentity\":{\"type\":\"Root\"}"
        }
    ]
}
```

The key elements in the data structure are the following:

**messageType**

Data messages will use the "DATA_MESSAGE" type. Sometimes
CloudWatch Logs might emit Kinesis Data Streams records with a "CONTROL_MESSAGE" type,
mainly for checking if the destination is reachable.

**owner**

The AWS Account ID of the originating log data.

**logGroup**

The log group name of the originating log data.

**logStream**

The log stream name of the originating log data.

**subscriptionFilters**

The list of subscription filter names that matched with the
originating log data.

**logEvents**

The actual log data, represented as an array of log event
records. The "id" property is a unique identifier for every log
event.

**policyLevel**

The level at which the policy was enforced.
"ACCOUNT_LEVEL_POLICY" is the `policyLevel` for an
account-level subscription filter policy.
