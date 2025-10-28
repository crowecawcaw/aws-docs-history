# Interact with

data using the AWS Glue Schema Registry

You can integrate your Kinesis data streams with the AWS Glue Schema Registry. The
AWS Glue Schema Registry allows you to centrally discover, control, and evolve schemas,
while ensuring data produced is continuously validated by a registered schema. A
schema defines the structure and format of a data record. A schema is a versioned
specification for reliable data publication, consumption, or storage. The AWS Glue
Schema Registry enables you to improve end-to-end data quality and data governance
within your streaming applications. For more information, see [AWS Glue
Schema Registry](../../../glue/latest/dg/schema-registry.md "../../../glue/latest/dg/schema-registry.md"). One of the ways to set up this integration is through
the `GetRecords` Kinesis Data Streams API available in the AWS Java
SDK.

For detailed instructions on how to set up integration of Kinesis Data Streams
with Schema Registry using the `GetRecords` Kinesis Data Streams APIs,
see the "Interacting with Data Using the Kinesis Data Streams APIs" section in
[Use Case: Integrating Amazon Kinesis Data Streams with the AWS Glue Schema
Registry](../../../glue/latest/dg/schema-registry-integrations.md#schema-registry-integrations-kds "../../../glue/latest/dg/schema-registry-integrations.md#schema-registry-integrations-kds").
