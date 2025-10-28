# Find deduplication key and ID in your output data

You can see the deduplication key and ID in your output data. The
deduplication key is identified by
`dataset-objectid-attribute-name`. When you use your own
custom deduplication key, your output contains something similar to the
following:

```
"dataset-objectid-attribute-name": "`byo-key`",
"`byo-key`": "`UniqueId`",
```

When you do not specify a key, you can find the deduplication ID that Ground Truth
assigned to your data object as follows. The
`$`label-attribute-name`-object-id`
parameter identifies your deduplication ID.

```
{
    "source-ref":"`s3://bucket/prefix/object1`",
    "dataset-objectid-attribute-name":"$`label-attribute-name`-object-id"
    "`label-attribute-name`" :0,
    "`label-attribute-name`-metadata": {`...`},
    "$`label-attribute-name`-object-id":"`<service-generated-key>`"
}
```

For
`<service-generated-key>`, if
the data object came through an Amazon S3 configuration, Ground Truth adds a unique
value used by the service and emits a new field keyed by
`$`sequencer`` which shows
the Amazon S3 sequencer used. If object was fed to SNS directly, Ground Truth use the
SNS message ID.
