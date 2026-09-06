

# SelfManagedKafka
<a name="sam-property-function-selfmanagedkafka"></a>

The object describing a `SelfManagedKafka` event source type. For more information, see [Using AWS Lambda with self-managed Apache Kafka](https://docs.aws.amazon.com/lambda/latest/dg/with-kafka.html) in the *AWS Lambda Developer Guide*.

AWS Serverless Application Model (AWS SAM) generates an [AWS::Lambda::EventSourceMapping](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-eventsourcemapping.html) resource when this event type is set.

To use Schema Registry, you need to define specific IAM role permissions for your function. See [Complete setup with IAM roles](sam-property-function-msk.md#sam-property-function-msk-example-complete) for an example of the required configuration.

## Syntax
<a name="sam-property-function-selfmanagedkafka-syntax"></a>

To declare this entity in your AWS SAM template, use the following syntax.

### YAML
<a name="sam-property-function-selfmanagedkafka-syntax.yaml"></a>

```
  [BatchSize](#sam-function-selfmanagedkafka-batchsize): {{Integer}}
  [BisectBatchOnFunctionError](#sam-function-selfmanagedkafka-bisectbatchonfunctionerror): {{Boolean}}
  [ConsumerGroupId](#sam-function-selfmanagedkafka-consumergroupid): {{String}}
  DestinationConfig: {{[DestinationConfig](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-eventsourcemapping-destinationconfig.html)}}
  [Enabled](#sam-function-selfmanagedkafka-enabled): {{Boolean}}
  [FilterCriteria](#sam-function-selfmanagedkafka-filtercriteria): {{[FilterCriteria](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-eventsourcemapping-filtercriteria.html)}}
  [KafkaBootstrapServers](#sam-function-selfmanagedkafka-kafkabootstrapservers): {{List}}
  [FunctionResponseTypes](#sam-function-selfmanagedkafka-functionresponsetypes): {{List}}
  KmsKeyArn: {{String}}
  [LoggingConfig](#sam-function-selfmanagedkafka-loggingconfig): {{LoggingConfig}}
  [MaximumRecordAgeInSeconds](#sam-function-selfmanagedkafka-maximumrecordageinseconds): {{Integer}}
  [MaximumRetryAttempts](#sam-function-selfmanagedkafka-maximumretryattempts): {{Integer}}
  [MetricsConfig](#sam-function-selfmanagedkafka-metricsconfig): {{MetricsConfig}}
  [ProvisionedPollerConfig](#sam-function-selfmanagedkafka-provisionedpollerconfig): {{[ProvisionedPollerConfig](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-eventsourcemapping-provisionedpollerconfig)}}
  [SchemaRegistryConfig](#sam-function-selfmanagedkafka-schemaregistryconfig): {{[SchemaRegistryConfig](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-eventsourcemapping-schemaregistryconfig.html)}}
  [SourceAccessConfigurations](#sam-function-selfmanagedkafka-sourceaccessconfigurations): {{[SourceAccessConfigurations](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-eventsourcemapping.html#cfn-lambda-eventsourcemapping-sourceaccessconfigurations)}}
  StartingPosition: {{String}}
  StartingPositionTimestamp: {{Double}}
  [Topics](#sam-function-selfmanagedkafka-topics): {{List}}
```

## Properties
<a name="sam-property-function-selfmanagedkafka-properties"></a>

 `BatchSize`   <a name="sam-function-selfmanagedkafka-batchsize"></a>
The maximum number of records in each batch that Lambda pulls from your stream and sends to your function.  
*Type*: Integer  
*Required*: No  
*Default*: 100  
*CloudFormation compatibility*: This property is passed directly to the `[BatchSize](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-eventsourcemapping.html#cfn-lambda-eventsourcemapping-batchsize)` property of an `AWS::Lambda::EventSourceMapping` resource.  
*Minimum*: `1`  
*Maximum*: `10000`

 `BisectBatchOnFunctionError`   <a name="sam-function-selfmanagedkafka-bisectbatchonfunctionerror"></a>
If the function returns an error, split the batch in two and retry.  
*Type*: Boolean  
*Required*: No  
*CloudFormation compatibility*: This property is passed directly to the `[BisectBatchOnFunctionError](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-eventsourcemapping.html#cfn-lambda-eventsourcemapping-bisectbatchonfunctionerror)` property of an `AWS::Lambda::EventSourceMapping` resource.

 `ConsumerGroupId`   <a name="sam-function-selfmanagedkafka-consumergroupid"></a>
A string that configures how events will be read from Kafka topics.  
*Type*: String  
*Required*: No  
*CloudFormation compatibility*: This property is passed directly to the `[SelfManagedKafkaEventSourceConfig](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-eventsourcemapping-selfmanagedkafkaeventsourceconfig)` property of an `AWS::Lambda::EventSourceMapping` resource.

 `DestinationConfig`   <a name="sam-function-selfmanagedkafka-destinationconfig"></a>
A configuration object that specifies the destination of an event after Lambda processes it.  
Use this property to specify the destination of failed invocations from the self-managed Kafka event source.  
*Type*: [DestinationConfig](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-eventsourcemapping-destinationconfig.html)  
*Required*: No  
*CloudFormation compatibility*: This property is passed directly to the `[ DestinationConfig](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-eventsourcemapping.html#cfn-lambda-eventsourcemapping-destinationconfig)` property of an `AWS::Lambda::EventSourceMapping` resource.

 `Enabled`   <a name="sam-function-selfmanagedkafka-enabled"></a>
Disables the event source mapping to pause polling and invocation.  
*Type*: Boolean  
*Required*: No  
*CloudFormation compatibility*: This property is passed directly to the `[Enabled](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-eventsourcemapping.html#cfn-lambda-eventsourcemapping-enabled)` property of an `AWS::Lambda::EventSourceMapping` resource.

 `FilterCriteria`   <a name="sam-function-selfmanagedkafka-filtercriteria"></a>
A object that defines the criteria to determine whether Lambda should process an event. For more information, see [AWS Lambda event filtering](https://docs.aws.amazon.com/lambda/latest/dg/invocation-eventfiltering.html) in the *AWS Lambda Developer Guide*.  
*Type*: [FilterCriteria](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-eventsourcemapping-filtercriteria.html)  
*Required*: No  
*CloudFormation compatibility*: This property is passed directly to the `[FilterCriteria](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-eventsourcemapping.html#cfn-lambda-eventsourcemapping-filtercriteria)` property of an `AWS::Lambda::EventSourceMapping` resource.

 `KafkaBootstrapServers`   <a name="sam-function-selfmanagedkafka-kafkabootstrapservers"></a>
The list of bootstrap servers for your Kafka brokers. Include the port, for example `broker.example.com:{{xxxx}}`  
*Type*: List  
*Required*: No  
*CloudFormation compatibility*: This property is unique to AWS SAM and doesn't have an CloudFormation equivalent.

 `FunctionResponseTypes`   <a name="sam-function-selfmanagedkafka-functionresponsetypes"></a>
A list of the response types currently applied to the event source mapping. For more information, see [Reporting batch item failures](https://docs.aws.amazon.com/lambda/latest/dg/kafka-retry-configurations.html) in the *AWS Lambda Developer Guide*.  
*Valid values*: `ReportBatchItemFailures`  
*Type*: List  
*Required*: No  
*CloudFormation compatibility*: This property is passed directly to the `[FunctionResponseTypes](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-eventsourcemapping.html#cfn-lambda-eventsourcemapping-functionresponsetypes)` property of an `AWS::Lambda::EventSourceMapping` resource.

 `KmsKeyArn`   <a name="sam-function-selfmanagedkafka-kmskeyarn"></a>
The Amazon Resource Name (ARN) of the key to encrypt information related to this event.  
*Type*: String  
*Required*: No  
*CloudFormation compatibility*: This property is passed directly to the `[KmsKeyArn](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-eventsourcemapping.html#cfn-lambda-eventsourcemapping-kmskeyarn)` property of an `AWS::Lambda::EventSourceMapping` resource.

 `LoggingConfig`   <a name="sam-function-selfmanagedkafka-loggingconfig"></a>
The logging configuration for your event source.  
*Type*: [LoggingConfig](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-eventsourcemapping-loggingconfig)  
*Required*: No  
*CloudFormation compatibility*: This property is passed directly to the `[LoggingConfig](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-eventsourcemapping.html#cfn-lambda-eventsourcemapping-loggingconfig)` property of an `AWS::Lambda::EventSourceMapping` resource.

 `MaximumRecordAgeInSeconds`   <a name="sam-function-selfmanagedkafka-maximumrecordageinseconds"></a>
The maximum age of a record that Lambda sends to a function for processing.  
*Type*: Integer  
*Required*: No  
*CloudFormation compatibility*: This property is passed directly to the `[MaximumRecordAgeInSeconds](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-eventsourcemapping.html#cfn-lambda-eventsourcemapping-maximumrecordageinseconds)` property of an `AWS::Lambda::EventSourceMapping` resource.

 `MetricsConfig`   <a name="sam-function-selfmanagedkafka-metricsconfig"></a>
The metrics configuration for your event source.  
*Type*: [MetricsConfig](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-eventsourcemapping-metricsconfig)  
*Required*: No  
*CloudFormation compatibility*: This property is passed directly to the `[MetricsConfig](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-eventsourcemapping.html#cfn-lambda-eventsourcemapping-metricsconfig)` property of an `AWS::Lambda::EventSourceMapping` resource.

 `MaximumRetryAttempts`   <a name="sam-function-selfmanagedkafka-maximumretryattempts"></a>
The maximum number of times to retry when the function returns an error.  
*Type*: Integer  
*Required*: No  
*CloudFormation compatibility*: This property is passed directly to the `[MaximumRetryAttempts](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-eventsourcemapping.html#cfn-lambda-eventsourcemapping-maximumretryattempts)` property of an `AWS::Lambda::EventSourceMapping` resource.

 `ProvisionedPollerConfig`   <a name="sam-function-selfmanagedkafka-provisionedpollerconfig"></a>
Configuration to increase the amount of pollers used to compute event source mappings. This configuration allows for a minumum of 1 poller and a maximum of 2000 pollers. For an example, refer to [ProvisionedPollerConfig example](#sam-property-function-selfmanagedkafka-example-provisionedpollerconfig)  
*Type*: [ProvisionedPollerConfig](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-eventsourcemapping-provisionedpollerconfig)  
*Required*: No  
*CloudFormation compatibility*: This property is passed directly to the `[ProvisionedPollerConfig](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-eventsourcemapping.html#cfn-lambda-eventsourcemapping-provisionedpollerconfig)` property of an `AWS::Lambda::EventSourceMapping` resource.

`SchemaRegistryConfig`  <a name="sam-function-selfmanagedkafka-schemaregistryconfig"></a>
Configuration for using a schema registry with the self-managed Kafka event source.  
This feature requires `ProvisionedPollerConfig` to be configured.
*Type*: [SchemaRegistryConfig](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-eventsourcemapping-schemaregistryconfig)  
*Required*: No  
*CloudFormation compatibility:* This property is passed directly to the `[SelfManagedKafkaEventSourceConfig](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-eventsourcemapping-selfmanagedkafkaeventsourceconfig)` property of an `AWS::Lambda::EventSourceMapping` resource.

 `SourceAccessConfigurations`   <a name="sam-function-selfmanagedkafka-sourceaccessconfigurations"></a>
An array of the authentication protocol, VPC components, or virtual host to secure and define your event source.  
*Valid values*: `BASIC_AUTH | CLIENT_CERTIFICATE_TLS_AUTH | SASL_SCRAM_256_AUTH | SASL_SCRAM_512_AUTH | SERVER_ROOT_CA_CERTIFICATE`  
*Type*: List of [SourceAccessConfiguration](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-eventsourcemapping-sourceaccessconfiguration)  
*Required*: Yes  
*CloudFormation compatibility:* This property is part of the `[SelfManagedKafkaEventSourceConfig](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-eventsourcemapping-selfmanagedkafkaeventsourceconfig)` property of an `AWS::Lambda::EventSourceMapping` resource.

 `StartingPosition`   <a name="sam-function-selfmanagedkafka-startingposition"></a>
The position in a stream from which to start reading.  
+ `AT_TIMESTAMP` – Specify a time from which to start reading records.
+ `LATEST` – Read only new records.
+ `TRIM_HORIZON` – Process all available records.
*Valid values*: `AT_TIMESTAMP` \| `LATEST` \| `TRIM_HORIZON`  
*Type*: String  
*Required*: No  
*CloudFormation compatibility*: This property is passed directly to the `[StartingPosition](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-eventsourcemapping.html#cfn-lambda-eventsourcemapping-startingposition)` property of an `AWS::Lambda::EventSourceMapping` resource.

 `StartingPositionTimestamp`   <a name="sam-function-selfmanagedkafka-startingpositiontimestamp"></a>
The time from which to start reading, in Unix time seconds. Define `StartingPositionTimestamp` when `StartingPosition` is specified as `AT_TIMESTAMP`.  
*Type*: Double  
*Required*: No  
*CloudFormation compatibility*: This property is passed directly to the `[StartingPositionTimestamp](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-eventsourcemapping.html#cfn-lambda-eventsourcemapping-startingpositiontimestamp)` property of an `AWS::Lambda::EventSourceMapping` resource.

 `Topics`   <a name="sam-function-selfmanagedkafka-topics"></a>
The name of the Kafka topic.  
*Type*: List  
*Required*: Yes  
*CloudFormation compatibility*: This property is passed directly to the `[Topics](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-eventsourcemapping.html#cfn-lambda-eventsourcemapping-topics)` property of an `AWS::Lambda::EventSourceMapping` resource.

## Examples
<a name="sam-property-function-selfmanagedkafka--examples"></a>

### Complete setup with IAM roles
<a name="sam-property-function-selfmanagedkafka-example-complete"></a>

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
<a name="sam-property-function-selfmanagedkafka-example-provisionedpollerconfig"></a>

```
ProvisionedPollerConfig:
  MinimumPollers: 1
  MaximumPollers: 200
```

### Self-managed Kafka event source
<a name="sam-property-function-selfmanagedkafka--examples--self-managed-kafka-event-source"></a>

The following is an example of a `SelfManagedKafka` event source type.

#### YAML
<a name="sam-property-function-selfmanagedkafka--examples--self-managed-kafka-event-source--yaml"></a>

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
<a name="sam-property-function-selfmanagedkafka-example-schemaregistry"></a>

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
<a name="sam-property-function-selfmanagedkafka-example-schemaregistry-confluent"></a>

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