Amazon Managed Service for Apache Flink (Amazon MSF) was previously known as Amazon Kinesis Data Analytics for Apache Flink.

# Transform data using operators in Managed Service for Apache Flink with the

DataStream API

To transform incoming data in a Managed Service for Apache Flink, you use an Apache Flink
_operator_. An Apache Flink operator transforms one or more data
streams into a new data stream. The new data stream contains modified data from the original
data stream. Apache Flink provides more than 25 pre-built stream processing operators. For
more information, see [Operators](https://nightlies.apache.org/flink/flink-docs-release-1.19/docs/dev/datastream/operators/overview/ "https://nightlies.apache.org/flink/flink-docs-release-1.19/docs/dev/datastream/operators/overview/") in the Apache Flink
Documentation.

###### This topic contains the following sections:

- [Use transform operators](#how-operators-transform "#how-operators-transform")
- [Use aggregation operators](#how-operators-agg "#how-operators-agg")

## Use transform operators

The following is an example of a simple text transformation on one of the fields of a
JSON data stream.

This code creates a transformed data stream. The new data stream has the same data as
the original stream, with the string " `Company`" appended to the contents of
the `TICKER` field.

```
DataStream<ObjectNode> output = input.map(
    new MapFunction<ObjectNode, ObjectNode>() {
        @Override
        public ObjectNode map(ObjectNode value) throws Exception {
            return value.put("TICKER", value.get("TICKER").asText() + " Company");
        }
    }
);
```

## Use aggregation operators

The following is an example of an aggregation operator. The code creates an aggregated
data stream. The operator creates a 5-second tumbling window and returns the sum of the
`PRICE` values for the records in the window with the same
`TICKER` value.

```
DataStream<ObjectNode> output = input.keyBy(node -> node.get("TICKER").asText())
    .window(TumblingProcessingTimeWindows.of(Time.seconds(5)))
    .reduce((node1, node2) -> {
        double priceTotal = node1.get("PRICE").asDouble() + node2.get("PRICE").asDouble();
        node1.replace("PRICE", JsonNodeFactory.instance.numberNode(priceTotal));
    return node1;
});
```

For more code examples, see [Examples for creating and working with
Managed Service for Apache Flink applications](examples-collapsibles.md "examples-collapsibles.md").
