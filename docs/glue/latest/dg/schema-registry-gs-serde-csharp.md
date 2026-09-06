

# C\# Implementation
<a name="schema-registry-gs-serde-csharp"></a>

**Note**  
Prerequisites: Before completing the following steps, you will need to have a Amazon Managed Streaming for Apache Kafka (Amazon MSK) or Apache Kafka cluster running. Your producers and consumers need to be running on .NET 8.0 or above.

## Installation
<a name="schema-registry-gs-serde-csharp-install"></a>

For C\# applications, install the AWS Glue Schema Registry SerDe NuGet package using one of the following methods:

**.NET CLI:**  
Use the following command to install the package:

```
dotnet add package Aws.Glue.SchemaRegistry --version 1.0.0-<rid>
```

where `<rid>` could be `1.0.0-linux-x64`, `1.0.0-linux-musl-x64` or `1.0.0-linux-arm64`

**PackageReference (in your .csproj file):**  
Add the following to your project file:

```
<PackageReference Include="Aws.Glue.SchemaRegistry" Version="1.0.0-<rid>" />
```

where `<rid>` could be `1.0.0-linux-x64`, `1.0.0-linux-musl-x64` or `1.0.0-linux-arm64`

## Configuration File Setup
<a name="schema-registry-gs-serde-csharp-config"></a>

Create a configuration properties file (e.g., `gsr-config.properties`) with the required settings:

**Minimal Configuration:**  
The following shows a minimal configuration example:

```
region=us-east-1
registry.name=default-registry
dataFormat=AVRO
schemaAutoRegistrationEnabled=true
```

## Using C\# Glue Schema client library for Kafka SerDes
<a name="schema-registry-gs-serde-csharp-kafka"></a>

**Sample serializer usage:**  
The following example shows how to use the serializer:

```
private static readonly string PROTOBUF_CONFIG_PATH = "<PATH_TO_CONFIG_FILE>";
var protobufSerializer = new GlueSchemaRegistryKafkaSerializer(PROTOBUF_CONFIG_PATH);
var serialized = protobufSerializer.Serialize(message, message.Descriptor.FullName);
// send serialized bytes to Kafka using producer.Produce(serialized)
```

**Sample deserializer usage:**  
The following example shows how to use the deserializer:

```
private static readonly string PROTOBUF_CONFIG_PATH = "<PATH_TO_CONFIG_FILE>";
var dataConfig = new GlueSchemaRegistryDataFormatConfiguration(
    new Dictionary<string, dynamic>
    {
        {
            GlueSchemaRegistryConstants.ProtobufMessageDescriptor, message.Descriptor
        }
    }
);
var protobufDeserializer = new GlueSchemaRegistryKafkaDeserializer(PROTOBUF_CONFIG_PATH, dataConfig);

// read message from Kafka using serialized = consumer.Consume()
var deserializedObject = protobufDeserializer.Deserialize(message.Descriptor.FullName, serialized);
```

## Using C\# Glue Schema client library with KafkaFlow for SerDes
<a name="schema-registry-gs-serde-csharp-kafkaflow"></a>

**Sample serializer usage:**  
The following example shows how to configure KafkaFlow with the serializer:

```
services.AddKafka(kafka => kafka
    .UseConsoleLog()
    .AddCluster(cluster => cluster
        .WithBrokers(new[] { "localhost:9092" })
        .AddProducer<CustomerProducer>(producer => producer
            .DefaultTopic("customer-events")
            .AddMiddlewares(m => m
                .AddSerializer<GlueSchemaRegistryKafkaFlowProtobufSerializer<Customer>>(
                    () => new GlueSchemaRegistryKafkaFlowProtobufSerializer<Customer>("config/gsr-config.properties")
                )
            )
        )
    )
);
```

**Sample deserializer usage:**  
The following example shows how to configure KafkaFlow with the deserializer:

```
.AddConsumer(consumer => consumer
    .Topic("customer-events")
    .WithGroupId("customer-group")
    .WithBufferSize(100)
    .WithWorkersCount(10)
    .AddMiddlewares(middlewares => middlewares
        .AddDeserializer<GlueSchemaRegistryKafkaFlowProtobufDeserializer<Customer>>(
            () => new GlueSchemaRegistryKafkaFlowProtobufDeserializer<Customer>("config/gsr-config.properties")
        )
        .AddTypedHandlers(h => h.AddHandler<CustomerHandler>())
    )
)
```

## Optional Producer Properties
<a name="schema-registry-gs-serde-csharp-optional"></a>

You can extend your configuration file with additional optional properties:

```
# Auto-registration (if not passed, uses "false")
schemaAutoRegistrationEnabled=true

# Schema name (if not passed, uses topic name)
schema.name=my-schema

# Registry name (if not passed, uses "default-registry")
registry.name=my-registry

# Cache settings
cacheTimeToLiveMillis=86400000
cacheSize=200

# Compatibility mode (if not passed, uses BACKWARD)
compatibility=FULL

# Registry description
description=This registry is used for several purposes.

# Compression (if not passed, records are sent uncompressed)
compressionType=ZLIB
```

## Supported Data Formats
<a name="schema-registry-gs-serde-supported-formats"></a>

Both Java and C\# implementations support the same data formats:
+ *AVRO*: Apache Avro binary format
+ *JSON*: JSON Schema format
+ *PROTOBUF*: Protocol Buffers format

## Notes
<a name="schema-registry-gs-serde-csharp-notes"></a>
+ To get started with the library, please visit [https://www.nuget.org/packages/AWS.Glue.SchemaRegistry](https://www.nuget.org/packages/AWS.Glue.SchemaRegistry)
+ Source code is available at: [https://github.com/awslabs/aws-glue-schema-registry](https://github.com/awslabs/aws-glue-schema-registry)