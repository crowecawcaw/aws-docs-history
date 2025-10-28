# Process serialized data using AWS Lambda with

the Amazon Kinesis Producer Library

The [Amazon Kinesis Producer Library](../../../kinesis/latest/dev/developing-producers-with-kpl.md "../../../kinesis/latest/dev/developing-producers-with-kpl.md") (KPL) aggregates small user-formatted records into
larger records up to 1 MB to make better use of Amazon Kinesis Data Streams throughput. While the KCL for Java
supports deaggregating these records, you need to use a special module to deaggregate records
when using AWS Lambda as the consumer of your streams. You can obtain the necessary project
code and instructions from GitHub at [Amazon Kinesis Producer Library
Deaggregation Modules for AWS Lambda](https://github.com/awslabs/kinesis-deaggregation "https://github.com/awslabs/kinesis-deaggregation"). The components in this project give you the
ability to process KPL serialized data within AWS Lambda, in Java, Node.js
and Python. These components can also be used as part of a [multi-lang KCL application](https://github.com/awslabs/amazon-kinesis-client/blob/master/amazon-kinesis-client-multilang/src/main/java/software/amazon/kinesis/multilang/package-info.java "https://github.com/awslabs/amazon-kinesis-client/blob/master/amazon-kinesis-client-multilang/src/main/java/software/amazon/kinesis/multilang/package-info.java").
