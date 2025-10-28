# AWS Data Exchange Heartbeat

AWS Data Exchange Heartbeat (Test product) is a free product that subscribers can use to understand how to
interact with an AWS Data Exchange product subscription. You can use it for testing purposes and to get
familiar with the AWS Data Exchange API and concepts.

AWS Data Exchange Heartbeat contains a single data set named **Heartbeat**. Approximately
every 15 minutes, a new revision is published to this data set.

## Example content of a revision

Each new revision contains two assets:

- Epoch asset
- Manifest asset

## Epoch asset

Each AWS Data Exchange Heartbeat revision contains a JSON file Amazon Simple Storage Service (Amazon S3) object that
contains a single array. The array's name is
`TimestampsSinceLastRevision`, and its value is a list of each UNIX
Epoch second that has elapsed since the last revision.

The name of the asset is in the form `Epoch{start}-{end}.json`
where `{start}` and `{end}` represent the Epoch seconds
corresponding to the period of time covered by the revision.

## Manifest asset

Each AWS Data Exchange Heartbeat revision contains a JSON file S3 object that contains metadata
about the revision and the schema of the Epoch asset JSON file. The name of the
asset is in the form `Manifest{start}-{end}.json` where
`{start}` and `{end}` represent the Epoch seconds
corresponding to the period of time covered by the revision. The following example
shows the content of a manifest file.

```
{
        "manifestSchemaVersion":"1.0",
        "schema":"{
                \"type\":\"object\",
                \"properties\":{
                    \"TimestampsSinceLastRevision\":{
                        \"type\":\"array\",
                        \"description\":\"List of epoch timestamps in seconds.\",
                        \"items\":{
                            \"type\":\"number\",
                            \"description\":\"Epoch timestamp in seconds.\"
                         }
                     }
                 }
        }",
        "startTimestamp":1554898111,
        "endTimestamp":1554905311,
        "numberOfTimestamps":7201
}
```

The following topic describes how to subscribe to AWS Data Exchange Heartbeat on AWS Data Exchange.

###### Topics

- [Subscribing to AWS Data Exchange Heartbeat on AWS Data Exchange](how-to-subscribe.md "how-to-subscribe.md")
