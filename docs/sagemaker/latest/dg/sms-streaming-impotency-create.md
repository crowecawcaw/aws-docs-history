# Specify a deduplication key and ID in an Amazon SNS

message

When you send a data object to your streaming labeling job using an Amazon SNS
message, you have the option to specify your deduplication key and deduplication
ID in one of the following ways. In all of these scenarios, identify your
deduplication key with `dataset-objectid-attribute-name`.

**Bring Your Own Deduplication Key and
ID**

Create your own deduplication key and deduplication ID by
configuring your Amazon SNS message as follows. Replace
`byo-key` with your key
and `UniqueId` with the
deduplication ID for that data object.

```
{
    "source-ref":"s3://`amzn-s3-demo-bucket`/`prefix/object1`",
    "dataset-objectid-attribute-name":"`byo-key`",
    "`byo-key`":"`UniqueId`"
}
```

Your deduplication key can be up to 140 characters. Supported patterns
include: `"^[$a-zA-Z0-9](-*[a-zA-Z0-9])*"`.

Your deduplication ID can be up to 1,024 characters. Supported
patterns include: `^(https|s3)://([^/]+)/?(.*)$`.

**Use an Existing Key for your Deduplication
Key**

You can use an existing key in your message as the deduplication
key. When you do this, the value associated with that key is used for
the deduplication ID.

For example, you can specify use the `source-ref` key as your
deduplication key by formatting your message as follows:

```
{
    "source-ref":"s3://`amzn-s3-demo-bucket`/`prefix/object1`",
    "dataset-objectid-attribute-name":"source-ref"
}
```

In this example, Ground Truth uses `"s3://`amzn-s3-demo-bucket`/`prefix/object1`"` for the
deduplication id.
