# Use the AWS Glue Schema registry with KCL

You can integrate Kinesis Data Streams with the AWS Glue Schema registry. The AWS Glue Schema registry
lets you centrally discover, control, and evolve schemas, while ensuring data produced
is continuously validated by a registered schema. A schema defines the structure and
format of a data record. A schema is a versioned specification for reliable data
publication, consumption, or storage. The AWS Glue Schema registry lets you improve
end-to-end data quality and data governance within your streaming applications. For more
information, see [AWS Glue Schema
Registry](../../../glue/latest/dg/schema-registry.md "../../../glue/latest/dg/schema-registry.md"). One of the ways to set up this integration is through KCL for
Java.

###### Important

- AWS Glue Schema registry integration for Kinesis Data Streams is only supported in KCL 2.3
  or later.
- AWS Glue Schema registry integration for Kinesis Data Streams is _not_
  supported for KCL consumers written in non-Java languages that run with
  `multilangdaemon`.
- AWS Glue Schema registry integration for Kinesis Data Streams is _not_
  supported in any versions of KCL 1.x.
  For detailed instructions on how to set up integration of Kinesis Data Streamswith AWS Glue Schema
  registry using KCL, see the "Interacting with Data Using the KPL/KCL Libraries" section
  in [Use Case: Integrating Amazon Kinesis Data Streams with the AWS Glue Schema
  Registry.](../../../glue/latest/dg/schema-registry-integrations.md#schema-registry-integrations-kds "../../../glue/latest/dg/schema-registry-integrations.md#schema-registry-integrations-kds")
