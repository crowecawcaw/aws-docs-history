# Installing SerDe Libraries

###### Note

Prerequisites: Before completing the following steps, you will need to have a
Amazon Managed Streaming for Apache Kafka (Amazon MSK) or Apache Kafka cluster running. Your producers and
consumers need to be running on Java 8 or above.

The SerDe libraries provide a framework for serializing and deserializing data.

You will install the open source serializer for your applications producing data
(collectively the "serializers"). The serializer handles serialization, compression,
and the interaction with the Schema Registry. The serializer automatically extracts
the schema from a record being written to a Schema Registry compatible destination,
such as Amazon MSK. Likewise, you will install the open source deserializer on your
applications consuming data.

To install the libraries on producers and consumers:

1. Inside both the producers’ and consumers’ pom.xml files, add this dependency via the code below:

```
<dependency>
    <groupId>software.amazon.glue</groupId>
    <artifactId>schema-registry-serde</artifactId>
    <version>1.1.5</version>
</dependency>
```

Alternatively, you can clone the [AWS Glue Schema Registry Github repository](https://github.com/awslabs/aws-glue-schema-registry "https://github.com/awslabs/aws-glue-schema-registry"). 2. Setup your producers with these required properties:

```
props.put(ProducerConfig.KEY_SERIALIZER_CLASS_CONFIG, StringSerializer.class.getName()); // Can replace StringSerializer.class.getName()) with any other key serializer that you may use
props.put(ProducerConfig.VALUE_SERIALIZER_CLASS_CONFIG, GlueSchemaRegistryKafkaSerializer.class.getName());
props.put(AWSSchemaRegistryConstants.AWS_REGION, "us-east-2");
properties.put(AWSSchemaRegistryConstants.DATA_FORMAT, "JSON"); // OR "AVRO"
```

If there are no existing schemas, then auto-registration needs to be turned on (next step). If you do have a schema that you would like to apply, then replace "my-schema" with your schema name. Also the "registry-name" has to be provided if schema auto-registration is off. If the schema is created under the "default-registry" then registry name can be omitted. 3. (Optional) Set any of these optional producer properties. For detailed property descriptions, see [the ReadMe file](https://github.com/awslabs/aws-glue-schema-registry/blob/master/README.md "https://github.com/awslabs/aws-glue-schema-registry/blob/master/README.md").

```
props.put(AWSSchemaRegistryConstants.SCHEMA_AUTO_REGISTRATION_SETTING, "true"); // If not passed, uses "false"
props.put(AWSSchemaRegistryConstants.SCHEMA_NAME, "my-schema"); // If not passed, uses transport name (topic name in case of Kafka, or stream name in case of Kinesis Data Streams)
props.put(AWSSchemaRegistryConstants.REGISTRY_NAME, "my-registry"); // If not passed, uses "default-registry"
props.put(AWSSchemaRegistryConstants.CACHE_TIME_TO_LIVE_MILLIS, "86400000"); // If not passed, uses 86400000 (24 Hours)
props.put(AWSSchemaRegistryConstants.CACHE_SIZE, "10"); // default value is 200
props.put(AWSSchemaRegistryConstants.COMPATIBILITY_SETTING, Compatibility.FULL); // Pass a compatibility mode. If not passed, uses Compatibility.BACKWARD
props.put(AWSSchemaRegistryConstants.DESCRIPTION, "This registry is used for several purposes."); // If not passed, constructs a description
props.put(AWSSchemaRegistryConstants.COMPRESSION_TYPE, AWSSchemaRegistryConstants.COMPRESSION.ZLIB); // If not passed, records are sent uncompressed
```

Auto-registration registers the schema version under the default registry ("default-registry"). If a `SCHEMA_NAME` is not specified in the previous step, then the topic name is inferred as `SCHEMA_NAME`.

See [Schema versioning and compatibility](schema-registry.md#schema-registry-compatibility "schema-registry.md#schema-registry-compatibility") for more information on compatibility modes. 4. Setup your consumers with these required properties:

```
props.put(ConsumerConfig.KEY_DESERIALIZER_CLASS_CONFIG, StringDeserializer.class.getName());
props.put(ConsumerConfig.VALUE_DESERIALIZER_CLASS_CONFIG, GlueSchemaRegistryKafkaDeserializer.class.getName());
props.put(AWSSchemaRegistryConstants.AWS_REGION, "us-east-2"); // Pass an AWS Region
props.put(AWSSchemaRegistryConstants.AVRO_RECORD_TYPE, AvroRecordType.GENERIC_RECORD.getName()); // Only required for AVRO data format
```

5. (Optional) Set these optional consumer properties. For detailed property descriptions, see [the ReadMe file](https://github.com/awslabs/aws-glue-schema-registry/blob/master/README.md "https://github.com/awslabs/aws-glue-schema-registry/blob/master/README.md").

```
properties.put(AWSSchemaRegistryConstants.CACHE_TIME_TO_LIVE_MILLIS, "86400000"); // If not passed, uses 86400000
props.put(AWSSchemaRegistryConstants.CACHE_SIZE, "10"); // default value is 200
props.put(AWSSchemaRegistryConstants.SECONDARY_DESERIALIZER, "com.amazonaws.services.schemaregistry.deserializers.external.ThirdPartyDeserializer"); // For migration fall back scenario
```
