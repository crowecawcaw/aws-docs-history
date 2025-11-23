# SelfManagedKafka

The object describing a `SelfManagedKafka` event source type. For more
information, see [Using AWS Lambda with
self-managed Apache Kafka](../../../lambda/latest/dg/with-kafka.md "../../../lambda/latest/dg/with-kafka.md") in the _AWS Lambda Developer Guide_.

AWS Serverless Application Model (AWS SAM) generates an [AWS::Lambda::EventSourceMapping](../../../AWSCloudFormation/latest/UserGuide/aws-resource-lambda-eventsourcemapping.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-lambda-eventsourcemapping.md") resource when this event type is
set.

To use Schema Registry, you need to define specific IAM role permissions for your function. See [Complete setup with IAM roles](sam-property-function-msk.md#sam-property-function-msk-example-complete "sam-property-function-msk.md#sam-property-function-msk-example-complete") for an example of the required configuration.

## Syntax

To declare this entity in your AWS SAM template, use the following syntax.

### YAML

```
  BatchSize: `Integer`
  BisectBatchOnFunctionError: `Boolean`
  ConsumerGroupId: `String`
  DestinationConfig: `DestinationConfig`
  Enabled: `Boolean`
  FilterCriteria: `FilterCriteria`
  KafkaBootstrapServers: `List`
  FunctionResponseTypes: `List`
  KmsKeyArn: `String`
  MaximumRecordAgeInSeconds: `Integer`
  MaximumRetryAttempts: `Integer`
  ProvisionedPollerConfig: `ProvisionedPollerConfig`
  SchemaRegistryConfig: `SchemaRegistryConfig`
  SourceAccessConfigurations: `SourceAccessConfigurations`
  StartingPosition: `String`
  StartingPositionTimestamp: `Double`
  Topics: `List`

```

## Properties

`BatchSize`

The maximum number of records in each batch that Lambda pulls from your stream and
sends to your function.

_Type_: Integer

_Required_: No

_Default_: 100

_CloudFormation compatibility_: This property is passed directly to the
`BatchSize` property of an
`AWS::Lambda::EventSourceMapping` resource.

_Minimum_: `1`

_Maximum_: `10000`

`BisectBatchOnFunctionError`

If the function returns an error, split the batch in two and retry.

_Type_: Boolean

_Required_: No

_CloudFormation compatibility_: This property is passed directly to the `BisectBatchOnFunctionError` property of an `AWS::Lambda::EventSourceMapping` resource.

`ConsumerGroupId`

A string that configures how events will be read from Kafka topics.

_Type_: String

_Required_: No

_CloudFormation compatibility_: This property is passed directly to the
`SelfManagedKafkaConfiguration` property of an
`AWS::Lambda::EventSourceMapping` resource.

`DestinationConfig`

A configuration object that specifies the destination of an event after Lambda processes it.

Use this property to specify the destination of failed invocations from the self-managed Kafka event
source.

_Type_: [DestinationConfig](../../../AWSCloudFormation/latest/UserGuide/aws-resource-lambda-eventsourcemapping.md#cfn-lambda-eventsourcemapping-destinationconfig "../../../AWSCloudFormation/latest/UserGuide/aws-resource-lambda-eventsourcemapping.md#cfn-lambda-eventsourcemapping-destinationconfig")

_Required_: No

_CloudFormation compatibility_: This property is passed directly to the
`DestinationConfig` property of an `AWS::Lambda::EventSourceMapping` resource.

`Enabled`

Disables the event source mapping to pause polling and invocation.

_Type_: Boolean

_Required_: No

_CloudFormation compatibility_: This property is passed directly to the
`Enabled` property of an `AWS::Lambda::EventSourceMapping`
resource.

`FilterCriteria`

A object that defines the criteria to determine whether Lambda should process an
event. For more information, see [AWS Lambda event filtering](../../../lambda/latest/dg/invocation-eventfiltering.md "../../../lambda/latest/dg/invocation-eventfiltering.md") in
the _AWS Lambda Developer Guide_.

_Type_: [FilterCriteria](../../../AWSCloudFormation/latest/UserGuide/aws-properties-lambda-eventsourcemapping-filtercriteria.md "../../../AWSCloudFormation/latest/UserGuide/aws-properties-lambda-eventsourcemapping-filtercriteria.md")

_Required_: No

_CloudFormation compatibility_: This property is passed directly to the
`FilterCriteria` property of an
`AWS::Lambda::EventSourceMapping` resource.

`KafkaBootstrapServers`

The list of bootstrap servers for your Kafka brokers. Include the port, for example
`broker.example.com:`xxxx``

_Type_: List

_Required_: No

_CloudFormation compatibility_: This property is unique to AWS SAM and
doesn't have an CloudFormation equivalent.

`FunctionResponseTypes`

A list of the response types currently applied to the event source mapping. For more information, see [Reporting batch item failures](../../../lambda/latest/dg/kafka-retry-configurations.md "../../../lambda/latest/dg/kafka-retry-configurations.md") in the _AWS Lambda Developer Guide_.

_Valid values_: `ReportBatchItemFailures`

_Type_: List

_Required_: No

_CloudFormation compatibility_: This property is passed directly to the `FunctionResponseTypes` property of an `AWS::Lambda::EventSourceMapping` resource.

`KmsKeyArn`

The Amazon Resource Name (ARN) of the key to encrypt information related to this event.

_Type_: String

_Required_: No

_CloudFormation compatibility_: This property is passed directly to the
`KmsKeyArn`
property of an `AWS::Lambda::EventSourceMapping` resource.

`MaximumRecordAgeInSeconds`

The maximum age of a record that Lambda sends to a function for processing.

_Type_: Integer

_Required_: No

_CloudFormation compatibility_: This property is passed directly to the `MaximumRecordAgeInSeconds` property of an `AWS::Lambda::EventSourceMapping` resource.

`MaximumRetryAttempts`

The maximum number of times to retry when the function returns an error.

_Type_: Integer

_Required_: No

_CloudFormation compatibility_: This property is passed directly to the `MaximumRetryAttempts` property of an `AWS::Lambda::EventSourceMapping` resource.

`ProvisionedPollerConfig`

Configuration to increase the amount of pollers used to compute event source mappings. This configuration allows for a minumum of 1 poller and a maximum of 2000 pollers.
For an example, refer to [ProvisionedPollerConfig example](#sam-property-function-selfmanagedkafka-example-provisionedpollerconfig "#sam-property-function-selfmanagedkafka-example-provisionedpollerconfig")

_Type_: [ProvisionedPollerConfig](../../../AWSCloudFormation/latest/UserGuide/aws-properties-lambda-eventsourcemapping-provisionedpollerconfig.md "../../../AWSCloudFormation/latest/UserGuide/aws-properties-lambda-eventsourcemapping-provisionedpollerconfig.md")

_Required_: No

_CloudFormation compatibility_: This property is passed directly to the
`ProvisionedPollerConfig` property of an
`AWS::Lambda::EventSourceMapping` resource.

`SchemaRegistryConfig`

Configuration for using a schema registry with the self-managed Kafka event source.

###### Note

This feature requires `ProvisionedPollerConfig` to be configured.

_Type_: SchemaRegistryConfig

_Required_: No

_CloudFormation compatibility:_ This property is passed directly to the
`SelfManagedKafkaEventSourceConfig`
property of an `AWS::Lambda::EventSourceMapping` resource.

`SourceAccessConfigurations`

An array of the authentication protocol, VPC components, or virtual host to secure
and define your event source.

_Valid values_: `BASIC_AUTH | CLIENT_CERTIFICATE_TLS_AUTH |
 SASL_SCRAM_256_AUTH | SASL_SCRAM_512_AUTH | SERVER_ROOT_CA_CERTIFICATE`

_Type_: List of [SourceAccessConfiguration](../../../AWSCloudFormation/latest/UserGuide/aws-properties-lambda-eventsourcemapping-sourceaccessconfiguration.md "../../../AWSCloudFormation/latest/UserGuide/aws-properties-lambda-eventsourcemapping-sourceaccessconfiguration.md")

_Required_: Yes

_CloudFormation compatibility:_ This property is part of the
[SelfManagedKafkaEventSourceConfig](../../../AWSCloudFormation/latest/TemplateReference/aws-properties-lambda-eventsourcemapping-selfmanagedkafkaeventsourceconfig.md "../../../AWSCloudFormation/latest/TemplateReference/aws-properties-lambda-eventsourcemapping-selfmanagedkafkaeventsourceconfig.md")
property of an `AWS::Lambda::EventSourceMapping` resource.

`StartingPosition`

The position in a stream from which to start reading.

- `AT_TIMESTAMP` – Specify a time from which to start reading
  records.
- `LATEST` – Read only new records.
- `TRIM_HORIZON` – Process all available records.

_Valid values_: `AT_TIMESTAMP` |
`LATEST` | `TRIM_HORIZON`

_Type_: String

_Required_: No

_CloudFormation compatibility_: This property is passed directly to the
`StartingPosition` property of an
`AWS::Lambda::EventSourceMapping` resource.

`StartingPositionTimestamp`

The time from which to start reading, in Unix time seconds. Define
`StartingPositionTimestamp` when `StartingPosition` is specified
as `AT_TIMESTAMP`.

_Type_: Double

_Required_: No

_CloudFormation compatibility_: This property is passed directly to the
`StartingPositionTimestamp` property of an
`AWS::Lambda::EventSourceMapping` resource.

`Topics`

The name of the Kafka topic.

_Type_: List

_Required_: Yes

_CloudFormation compatibility_: This property is passed directly to the
`Topics` property of an `AWS::Lambda::EventSourceMapping`
resource.

## Examples

### Complete setup with IAM roles

The following example shows a complete setup including the required IAM role configuration for using Schema Registry:

```
Parameters:
  PreCreatedSubnetOne:
    Type: String
  PreCreatedSubnetTwo:
    Type: String

Resources:
  MyLambdaExecutionRole:
    Type: AWS::IAM::Role
    Properties:
      AssumeRolePolicyDocument:
        Version: '2012-10-17		 	 	 '
        Statement:
        - Action: [sts:AssumeRole]
          Effect: Allow
          Principal:
            Service: [lambda.amazonaws.com]
      Policies:
      - PolicyName: KafkaAuthPolicy
        PolicyDocument:
          Statement:
          - Action: [secretsmanager:GetSecretValue, kms:Decrypt]
            Effect: "Allow"
            Resource: ['arn:aws:secretsmanager:us-west-2:123456789012:secret:kafkaSecret-******',
                        'arn:aws:kms:us-west-2:123456789012:key/keyId']
      - PolicyName: ENIPolicy
        PolicyDocument:
          Statement:
          - Action: [ec2:CreateNetworkInterface,
              ec2:DescribeNetworkInterfaces, ec2:DescribeVpcs, ec2:DeleteNetworkInterface,
              ec2:DescribeSubnets, ec2:DescribeSecurityGroups]
            Effect: Allow
            Resource: '*'
      - PolicyName: SchemaRegistryPolicy
        PolicyDocument:
          Statement:
          - Action: [glue:GetRegistry]
            Effect: Allow
            Resource: 'arn:aws:glue:{region}:{account-id}:registry/{registry-name}'
      - PolicyName: SchemaVersionsPolicy
        PolicyDocument:
          Statement:
          - Action: [glue:GetSchemaVersions]
            Effect: Allow
            Resource: '*'
      ManagedPolicyArns:
      - !Sub arn:${AWS::Partition}:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole
      Tags:
      - {Value: SAM, Key: lambda:createdBy}

  MyKafkaProcessor:
    Type: AWS::Serverless::Function
    Properties:
      Runtime: nodejs18.x
      Handler: index.handler
      CodeUri: ${codeuri}
      Role:
        Fn::GetAtt: [MyLambdaExecutionRole, Arn]
      Events:
        SelfManagedKafkaEvent:
          Type: SelfManagedKafka
          Properties:
            KafkaBootstrapServers:
              - my-kafka-broker-1:9092
              - my-kafka-broker-2:9092
            Topics:
              - SchemaRegistryTestTopic
            StartingPosition: LATEST
            SourceAccessConfigurations:
              - Type: VPC_SUBNET
                URI: subnet:subnet-12345678
              - Type: VPC_SECURITY_GROUP
                URI: security_group:sg-12345678
              - Type: BASIC_AUTH
                URI: !Sub arn:${AWS::Partition}:secretsmanager:us-west-2:123456789012:secret:my-path/my-secret-name-1a2b3c
            ProvisionedPollerConfig:
              MinimumPollers: 1
            SchemaRegistryConfig:
              AccessConfigs:
              - Type: BASIC_AUTH
                URI: !Sub arn:${AWS::Partition}:secretsmanager:us-west-2:123456789012:secret:my-path/my-secret-name-1a2b3c
              SchemaValidationConfigs:
              - Attribute: KEY
              EventRecordFormat: JSON
              SchemaRegistryURI: !Sub arn:${AWS::Partition}:glue:us-west-2:123456789012:registry/myregistry
```

### ProvisionedPollerConfig example

```
ProvisionedPollerConfig:
  MinimumPollers: 1
  MaximumPollers: 200
```

### Self-managed Kafka event source

The following is an example of a `SelfManagedKafka` event source type.

#### YAML

```
Events:
  SelfManagedKafkaEvent:
    Type: SelfManagedKafka
    Properties:
      BatchSize: 1000
      Enabled: true
      KafkaBootstrapServers:
        - abc.xyz.com:xxxx
      SourceAccessConfigurations:
        -  Type: BASIC_AUTH
           URI: arn:aws:secretsmanager:us-west-2:123456789012:secret:my-path/my-secret-name-1a2b3c
      Topics:
        - MyKafkaTopic

```

### Self-managed Kafka Event Source with AWS Glue Schema Registry

The following is an example of a `SelfManagedKafka` event source type configured with AWS Glue Schema Registry.

```
Events:
  SelfManagedKafkaEvent:
    Type: SelfManagedKafka
    Properties:
      KafkaBootstrapServers:
        - abc.xyz.com:9092
      Topics:
        - SchemaRegistryTestTopic
      StartingPosition: LATEST
      ProvisionedPollerConfig:
        MinimumPollers: 1
      SchemaRegistryConfig:
        SchemaRegistryURI: !Sub arn:${AWS::Partition}:glue:us-west-2:123456789012:registry/myregistry
        EventRecordFormat: JSON
        SchemaValidationConfigs:
          - Attribute: KEY
          - Attribute: VALUE
      SourceAccessConfigurations:
        - Type: VPC_SUBNET
          URI: subnet:subnet-12345678
        - Type: VPC_SECURITY_GROUP
          URI: security_group:sg-12345678
```

### Self-managed Kafka Event Source with Confluent Schema Registry

The following is an example of a `SelfManagedKafka` event source type configured with Confluent Schema Registry.

```
Events:
  SelfManagedKafkaEvent:
    Type: SelfManagedKafka
    Properties:
      KafkaBootstrapServers:
        - abc.xyz.com:9092
      Topics:
        - SchemaRegistryTestTopic
      StartingPosition: LATEST
      ProvisionedPollerConfig:
        MinimumPollers: 1
      SchemaRegistryConfig:
        SchemaRegistryURI: https://my-schema-registry.confluent.cloud
        AccessConfigs:
          - Type: BASIC_AUTH
            URI: !Sub arn:${AWS::Partition}:secretsmanager:us-west-2:123456789012:secret:my-secret
        EventRecordFormat: JSON
        SchemaValidationConfigs:
          - Attribute: KEY
          - Attribute: VALUE
      SourceAccessConfigurations:
        - Type: VPC_SUBNET
          URI: subnet:subnet-12345678
        - Type: VPC_SECURITY_GROUP
          URI: security_group:sg-12345678
        - Type: BASIC_AUTH
          URI: !Sub arn:${AWS::Partition}:secretsmanager:us-west-2:123456789012:secret:kafka-secret
```
