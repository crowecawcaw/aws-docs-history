# Migration from a third-party schema registry to AWS Glue Schema Registry

The migration from a third-party schema registry to the AWS Glue Schema Registry has a dependency on the existing, current third-party schema registry.
If there are records in an Apache Kafka topic which were sent using a third-party schema registry, consumers need the third-party schema registry to deserialize those records.
The `AWSKafkaAvroDeserializer` provides the ability to specify a secondary deserializer class which points to the third-party deserializer and is used to deserialize those records.

There are two criteria for retirement of a third-party schema. First, retirement can occur only after records in Apache Kafka topics using the 3rd party schema registry are either no longer required by and for any consumers. Second, retirement can occur by aging out of the Apache Kafka topics, depending on the retention period specified for those topics. Note that if you have topics which have infinite retention, you can still migrate to the AWS Glue Schema Registry but you will not be able to retire the third-party schema registry. As a workaround, you can use an application or Mirror Maker 2 to read from the current topic and produce to a new topic with the AWS Glue Schema Registry.

To migrate from a third-party schema registry to the AWS Glue Schema Registry:

1. Create a registry in the AWS Glue Schema Registry, or use the default registry.
2. Stop the consumer. Modify it to include AWS Glue Schema Registry as the primary deserializer, and the third-party schema registry as the secondary.
   - Set the consumer properties. In this example, the secondary_deserializer is set to a different
     deserializer. The behavior is as follows: the consumer retrieves
     records from Amazon MSK and first tries to use the
     `AWSKafkaAvroDeserializer`. If it is unable to read
     the magic byte that contains the Avro Schema ID for the AWS Glue Schema
     Registry schema, the `AWSKafkaAvroDeserializer` then
     tries to use the deserializer class provided in the
     secondary_deserializer. The properties specific to the secondary
     deserializer also need to be provided in the consumer properties,
     such as the schema_registry_url_config and
     specific_avro_reader_config, as shown below.

   ```
   consumerProps.setProperty(ConsumerConfig.**KEY\_DESERIALIZER\_CLASS\_CONFIG**, StringDeserializer.class.getName());
   consumerProps.setProperty(ConsumerConfig.**VALUE\_DESERIALIZER\_CLASS\_CONFIG**, AWSKafkaAvroDeserializer.class.getName());
   consumerProps.setProperty(AWSSchemaRegistryConstants.**AWS\_REGION**, KafkaClickstreamConsumer.gsrRegion);
   consumerProps.setProperty(AWSSchemaRegistryConstants.**SECONDARY\_DESERIALIZER**, KafkaAvroDeserializer.class.getName());
   consumerProps.setProperty(KafkaAvroDeserializerConfig.**SCHEMA\_REGISTRY\_URL\_CONFIG**, "`URL for third-party schema registry`");
   consumerProps.setProperty(KafkaAvroDeserializerConfig.**SPECIFIC\_AVRO\_READER\_CONFIG**, "true");

   ```

3. Restart the consumer.
4. Stop the producer and point the producer to the AWS Glue Schema Registry.
   1. Set the producer properties. In this example, the producer will use the default-registry and auto register schema versions.

   ```
   producerProps.setProperty(ProducerConfig.**KEY\_SERIALIZER\_CLASS\_CONFIG**, StringSerializer.class.getName());
   producerProps.setProperty(ProducerConfig.**VALUE\_SERIALIZER\_CLASS\_CONFIG**, AWSKafkaAvroSerializer.class.getName());
   producerProps.setProperty(AWSSchemaRegistryConstants.**AWS\_REGION**, "us-east-2");
   producerProps.setProperty(AWSSchemaRegistryConstants.**AVRO\_RECORD\_TYPE**, AvroRecordType.**SPECIFIC\_RECORD**.getName());
   producerProps.setProperty(AWSSchemaRegistryConstants.**SCHEMA\_AUTO\_REGISTRATION\_SETTING**, "true");
   ```

5. (Optional) Manually move existing schemas and schema versions from the current third-party schema registry to the AWS Glue Schema Registry, either to the default-registry in AWS Glue Schema Registry or to a specific non-default registry in AWS Glue Schema Registry. This can be done by exporting schemas from the third-party schema registries in JSON format and creating new schemas in AWS Glue Schema Registry using the AWS Management Console or the AWS CLI.

This step may be important if you need to enable compatibility checks with previous schema versions for newly created schema versions using the AWS CLI and the AWS Management Console, or when producers send messages with a new schema with auto-registration of schema versions turned on. 6. Start the producer.
