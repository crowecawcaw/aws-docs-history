

# Getting started with CDC streams
<a name="cdc-setup"></a>

This guide walks you through every step required to start streaming committed row-level changes from an Aurora DSQL cluster to an Amazon Kinesis data stream. By the end of this guide, you've created a working CDC pipeline and a Python script that reads and prints change records.

## Prerequisites
<a name="cdc-prerequisites"></a>

Before you begin, confirm the following:
+ You've created an Aurora DSQL cluster in `ACTIVE` status. If your cluster is idle, connect to it with any PostgreSQL-compatible client to wake it up before you create a CDC stream. `CreateStream` returns a validation error if the cluster isn't in `ACTIVE` status.
+ Aurora DSQL requires all CDC resources—the cluster, Amazon Kinesis data stream, IAM service role, and calling principal—to be in the same AWS account.
+ Your Amazon Kinesis data stream is in the same AWS Region as your Aurora DSQL cluster.
+ You've installed and configured the AWS CLI with credentials that have permission to create IAM roles and Amazon Kinesis data streams.

## Step 1: Create an Amazon Kinesis data stream
<a name="cdc-step1-kinesis"></a>

Create a Kinesis data stream in the same AWS account and Region as your Aurora DSQL cluster. CDC records are larger than the corresponding Aurora DSQL row because the JSON format includes column names, metadata, and encoding overhead.

### Sizing the Kinesis data stream
<a name="cdc-sizing"></a>

Aurora DSQL CDC delivers the full row on every change. An update that touches a single column produces a record that contains every column in the row. Delete records are the exception—they include only the primary key columns.

**Estimate average record size**  
Measure the average on-disk row size to understand the volume that CDC will produce and to anticipate oversized records. The following query returns the average tuple size in bytes for a table:

```
SELECT avg(pg_column_size(t.*)) FROM {{your_table}} t;
```

The CDC record envelope adds column names, metadata, and encoding overhead on top of the row size. For the exact record format, see [Record payload](cdc-record-format.md#cdc-record-payload). For how Aurora DSQL handles records that exceed the Kinesis record size limit, see [Handling oversized records](cdc-record-format.md#cdc-oversized-records). For the full set of Kinesis service limits, see [Amazon Kinesis Data Streams quotas and limits](https://docs.aws.amazon.com/streams/latest/dev/service-sizes-and-limits.html) in the *Amazon Kinesis Data Streams Developer Guide*.

**Important**  
When you create the Kinesis data stream, set the following:  
`MaxRecordSizeInKiB` to `10240` (10 MiB). The default Kinesis maximum of 1 MiB isn't always large enough for Aurora DSQL CDC records. Any record that exceeds the configured Kinesis record size causes the CDC stream to become impaired with `KINESIS_OVERSIZE_RECORD`. Aurora DSQL splits oversized records into fragments that can approach 10 MiB each, so the Kinesis data stream needs to accept records of that size. For details, see [Handling oversized records](cdc-record-format.md#cdc-oversized-records).
`StreamMode` to `ON_DEMAND`. On-demand mode scales shard capacity automatically and protects you from under-provisioning during unexpected spikes. Kinesis can still return `WriteProvisionedThroughputExceeded` during sharp seconds-scale bursts as capacity scales up. Plan for brief throttling events.

Create CloudWatch alarms on `IncomingBytes` and `WriteProvisionedThroughputExceeded` in the `AWS/Kinesis` namespace. Kinesis throttling slows CDC delivery and increases replication lag. For Aurora DSQL-side metrics and alarm guidance, see [Monitoring best practices](cdc-monitoring.md#cdc-monitoring-best-practices).

The following example uses the AWS CLI. If your AWS CLI version doesn't support the `--max-record-size-in-ki-b` parameter, use an AWS SDK to call the Kinesis [CreateStream](https://docs.aws.amazon.com/kinesis/latest/APIReference/API_CreateStream.html) operation.

```
aws kinesis create-stream \
  --stream-name {{my-cdc-stream}} \
  --stream-mode-details StreamMode=ON_DEMAND \
  --max-record-size-in-ki-b 10240 \
  --region {{region}}
```

Wait for the stream to become active:

```
aws kinesis describe-stream-summary \
  --stream-name {{my-cdc-stream}} \
  --region {{region}} \
  --query 'StreamDescriptionSummary.StreamStatus'
```

The command returns `"ACTIVE"` when the stream is ready.

Record the stream ARN from the output. You need it in the following steps. The ARN has the format `arn:aws:kinesis:{{region}}:{{account-id}}:stream/{{my-cdc-stream}}`.

## Step 2: Create an IAM role for Aurora DSQL
<a name="cdc-step2-iam"></a>

Aurora DSQL assumes an IAM role to write CDC records to your Kinesis data stream. In this step, you create the role with a trust policy and attach a permissions policy. For a full explanation of each policy element, see [Configuring IAM](cdc-iam.md).

**Create the trust policy file**  
Save the following JSON as `trust-policy.json`. Replace {{your-account-id}}, {{region}}, and {{cluster-id}} with your values.

```
{
    "Version": "2012-10-17",		 	 	 
    "Statement": [
        {
            "Sid": "DSQLAccess",
            "Effect": "Allow",
            "Principal": {
                "Service": "dsql.amazonaws.com"
            },
            "Action": "sts:AssumeRole",
            "Condition": {
                "StringEquals": {
                    "aws:SourceAccount": "{{your-account-id}}"
                },
                "ArnLike": {
                    "aws:SourceArn": "arn:aws:dsql:{{region}}:{{your-account-id}}:cluster/{{cluster-id}}/stream/*"
                }
            }
        }
    ]
}
```

**Create the role**  
Run the following command to create the IAM role:

```
aws iam create-role \
  --role-name {{dsql-cdc-role}} \
  --assume-role-policy-document file://trust-policy.json
```

**Create the permissions policy file**  
Save the following JSON as `permissions-policy.json`. Replace the placeholder values with your Kinesis data stream ARN. The `KMSAccess` statement is only required if your Kinesis data stream uses an AWS KMS customer managed key, but you can include it preemptively so that adding a customer managed key later doesn't break your CDC stream. For a full explanation of each condition, see [Service role permissions policy](cdc-iam.md#cdc-iam-permissions-policy).

```
{
    "Version": "2012-10-17",		 	 	 
    "Statement": [
        {
            "Sid": "KinesisAccess",
            "Effect": "Allow",
            "Action": [
                "kinesis:PutRecord",
                "kinesis:PutRecords",
                "kinesis:DescribeStreamSummary",
                "kinesis:ListShards"
            ],
            "Resource": "arn:aws:kinesis:{{region}}:{{your-account-id}}:stream/{{my-cdc-stream}}"
        },
        {
            "Sid": "KMSAccess",
            "Effect": "Allow",
            "Action": [
                "kms:GenerateDataKey"
            ],
            "Resource": "arn:aws:kms:*:*:key/*",
            "Condition": {
                "StringEquals": {
                    "kms:ViaService": "kinesis.{{region}}.amazonaws.com",
                    "kms:EncryptionContext:aws:kinesis:arn": "arn:aws:kinesis:{{region}}:{{your-account-id}}:stream/{{my-cdc-stream}}",
                    "aws:ResourceAccount": "${aws:PrincipalAccount}"
                }
            }
        }
    ]
}
```

**Attach the permissions policy**  
Run the following command:

```
aws iam put-role-policy \
  --role-name {{dsql-cdc-role}} \
  --policy-name dsql-cdc-kinesis-access \
  --policy-document file://permissions-policy.json
```

Record the role ARN from the `create-role` output. The ARN has the format `arn:aws:iam::{{your-account-id}}:role/{{dsql-cdc-role}}`.

## Step 3: Create the CDC stream
<a name="cdc-step3-create-stream"></a>

Use the AWS CLI to create a CDC stream that connects your Aurora DSQL cluster to the Kinesis data stream. Replace the placeholder values with the Kinesis stream ARN from Step 1, the IAM role ARN from Step 2, and your cluster identifier.

```
aws dsql create-stream \
  --cluster-identifier {{cluster-id}} \
  --target-definition '{"kinesis":{"streamArn":"{{kinesis-stream-arn}}","roleArn":"{{role-arn}}"}}' \
  --ordering UNORDERED \
  --format JSON \
  --tags '{"Name":"{{my-cdc-stream}}"}' \
  --region {{region}}
```

The response includes a stream identifier and a status of `CREATING`. Stream creation typically takes one to three minutes.

**Wait for the stream to become active**  
Poll the stream status until it reaches `ACTIVE`:

```
aws dsql get-stream \
  --cluster-identifier {{cluster-id}} \
  --stream-identifier {{stream-id}} \
  --region {{region}} \
  --query 'status'
```

You can also use the `StreamActive` waiter in the AWS SDKs to poll automatically.

After the stream reaches `ACTIVE`, Aurora DSQL begins delivering committed row-level changes to your Kinesis data stream.

**Note**  
Each Aurora DSQL cluster has a maximum number of CDC streams. If you reach this limit, `CreateStream` returns a `ServiceQuotaExceededException`. For the default limit, see [Quotas and limits](https://docs.aws.amazon.com/aurora-dsql/latest/userguide/CHAP_quotas.html).

## Step 4: Verify that records are flowing
<a name="cdc-step4-verify"></a>

Insert a row into a table on your Aurora DSQL cluster. For example:

```
CREATE TABLE IF NOT EXISTS test_cdc (
    id INT PRIMARY KEY,
    message TEXT
);

INSERT INTO test_cdc VALUES (1, 'hello cdc');
```

Read from the Kinesis data stream to verify that the CDC record arrived. Because Aurora DSQL uses randomized partition keys, the record can land on any shard. The following script checks the shards on the stream. CDC records can take a few seconds to arrive because of replication lag—if the output is empty, wait a moment and re-run the script.

```
for SHARD_ID in $(aws kinesis list-shards \
  --stream-name {{my-cdc-stream}} \
  --region {{region}} \
  --query 'Shards[].ShardId' --output text); do

  SHARD_ITERATOR=$(aws kinesis get-shard-iterator \
    --stream-name {{my-cdc-stream}} \
    --shard-id "$SHARD_ID" \
    --shard-iterator-type TRIM_HORIZON \
    --region {{region}} \
    --query 'ShardIterator' --output text)

  aws kinesis get-records \
    --shard-iterator "$SHARD_ITERATOR" \
    --region {{region}} \
    --query 'Records[].Data' --output text
done
```

Each record's `Data` field contains a JSON payload. When you use the AWS CLI, the payload is Base64-encoded in the response. When you use the `boto3` SDK, the SDK decodes it automatically. The decoded JSON looks like the following:

```
{
    "type": "full",
    "op": "c",
    "before": null,
    "after": {"id": 1, "message": "hello cdc"},
    "source": {
        "version": "1.0",
        "ts_ms": 1705318200000,
        "ts_ns": 1705318200000000000,
        "txId": "ffthunp5stx6ffs2vyfqoatmfu",
        "schema": "public",
        "table": "test_cdc",
        "db": "postgres",
        "cluster": "{{cluster-id}}"
    },
    "ts_ms": 1705318200125,
    "ts_ns": 1705318200125483291
}
```

For a complete description of each field, see [Understanding CDC records](cdc-record-format.md).

## Step 5: Consume records with a Python script
<a name="cdc-step5-consume"></a>

The following Python script reads CDC records from a Kinesis data stream and prints each change event. The script uses the `boto3` Amazon Kinesis client to iterate over shards and decode each record. Because Aurora DSQL CDC uses at-least-once delivery, the script might print the same record more than one time.

```
"""
Read CDC records from an Amazon Kinesis data stream.

Usage:
    pip install boto3
    python consume_cdc.py --stream-name my-cdc-stream --region us-east-1
"""
from __future__ import annotations

import argparse
import json

import boto3


def consume_cdc(stream_name: str, region: str) -> None:
    kinesis = boto3.client("kinesis", region_name=region)

    # List all shards (paginate if the stream has many shards)
    shard_ids: list[str] = []
    paginator = kinesis.get_paginator("list_shards")
    for page in paginator.paginate(StreamName=stream_name):
        shard_ids.extend(s["ShardId"] for s in page["Shards"])
    print(f"Reading from {stream_name} ({len(shard_ids)} shard(s))")

    for shard_id in shard_ids:
        iterator_response = kinesis.get_shard_iterator(
            StreamName=stream_name,
            ShardId=shard_id,
            ShardIteratorType="TRIM_HORIZON",
        )
        shard_iterator = iterator_response["ShardIterator"]

        while shard_iterator:
            records_response = kinesis.get_records(
                ShardIterator=shard_iterator, Limit=100
            )
            shard_iterator = records_response.get("NextShardIterator")

            for record in records_response["Records"]:
                # boto3 decodes Base64 automatically; record["Data"] is bytes.
                payload = json.loads(record["Data"])

                # A record's "type" field identifies its structure.
                # "full": inlined record with before/after values.
                # "chunked": main record that references fragments for a split image.
                # "fragment": one piece of a chunked image; reassemble in production code.
                # For details, see cdc-record-format.html#cdc-oversized-records.
                record_type = payload.get("type", "full")
                if record_type == "fragment":
                    print(f"[FRAGMENT] chunk_id={payload['chunk_id']} index={payload['index']}")
                    continue

                source = payload["source"]
                op = payload["op"]
                ts_ns = source["ts_ns"]
                tx_id = source["txId"]
                table = f"{source['schema']}.{source['table']}"

                op_labels = {"c": "INSERT", "u": "UPDATE", "d": "DELETE"}
                print(
                    f"[{op_labels.get(op, op)}] {table} "
                    f"txId={tx_id} ts_ns={ts_ns} type={record_type}"
                )
                if payload.get("after"):
                    print(f"  after:  {json.dumps(payload['after'])}")
                if payload.get("before"):
                    print(f"  before: {json.dumps(payload['before'])}")
                if record_type == "chunked":
                    print(f"  chunked: {json.dumps(payload['chunked'])}")

            if not records_response["Records"]:
                break  # No more records in this shard


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Consume DSQL CDC records from Kinesis"
    )
    parser.add_argument("--stream-name", required=True, help="Kinesis stream name")
    parser.add_argument("--region", required=True, help="AWS Region")
    args = parser.parse_args()
    consume_cdc(args.stream_name, args.region)
```

Run the script:

```
pip install boto3
python consume_cdc.py \
  --stream-name {{my-cdc-stream}} \
  --region {{region}}
```

The script prints each change event as it arrives. You see output similar to the following:

```
Reading from my-cdc-stream (4 shard(s))
[INSERT] public.test_cdc txId=ffthunp5stx6ffs2vyfqoatmfu ts_ns=1705318200000000000 type=full
  after:  {"id": 1, "message": "hello cdc"}
```

**Adding last-writer-wins deduplication**  
Because Aurora DSQL CDC uses at-least-once delivery, production apps should deduplicate and order records. The following code example shows a high-water-mark approach: for each primary key, it tracks the highest `source.ts_ns` seen so far and discards any record with an equal or earlier timestamp. Set `PK_COLUMNS` to the primary key column names of the table you're processing. For strategies that handle multiple tables or deletes, see [Consumer strategies](cdc-streams.md#cdc-consumer-strategies).

```
# Set PK_COLUMNS to the primary key column(s) of your table.
PK_COLUMNS = ["id"]

# Maps each primary key value to the highest ts_ns seen for that key.
high_water: dict[tuple, int] = {}

def process_record(payload: dict) -> bool:
    """Return True if the record is new, False if it's a duplicate or stale.

    Skip fragment records; reassemble them into a full image before calling this.
    """
    if payload.get("type") == "fragment":
        return False  # Fragments are reassembled upstream, not deduplicated here.

    source = payload["source"]
    ts_ns = source["ts_ns"]

    # For inserts/updates the row is in "after"; for deletes it's in "before".
    row = payload.get("after") or payload.get("before") or {}
    pk = tuple(row.get(col) for col in PK_COLUMNS)

    prev_ts = high_water.get(pk, -1)
    if ts_ns <= prev_ts:
        return False  # Duplicate or out-of-order record

    high_water[pk] = ts_ns
    return True
```

## Managing CDC streams
<a name="cdc-manage-streams"></a>

**Listing streams**  
To list all CDC streams for a cluster, use the `ListStreams` operation:

```
aws dsql list-streams \
  --cluster-identifier {{cluster-id}} \
  --region {{region}}
```

**Deleting a stream**  
To delete a CDC stream, run the following command:

```
aws dsql delete-stream \
  --cluster-identifier {{cluster-id}} \
  --stream-identifier {{stream-id}} \
  --region {{region}}
```

You can use the `StreamNotExists` waiter to poll `GetStream` until a `ResourceNotFoundException` is returned, indicating that Aurora DSQL has fully deleted the stream.