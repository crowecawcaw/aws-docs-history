# MSK

The object describing an `MSK` event source type. For more information, see
[Using AWS Lambda with Amazon MSK](../../../lambda/latest/dg/with-msk.md "../../../lambda/latest/dg/with-msk.md") in the _AWS Lambda Developer Guide_.

AWS Serverless Application Model (AWS SAM) generates an [AWS::Lambda::EventSourceMapping](../../../AWSCloudFormation/latest/UserGuide/aws-resource-lambda-eventsourcemapping.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-lambda-eventsourcemapping.md") resource when this event type is
set.

To use Schema Registry, you need to define specific IAM role permissions for your function. See [Complete setup with IAM roles](#sam-property-function-msk-example-complete "#sam-property-function-msk-example-complete") for an example of the required configuration.

## Syntax

To declare this entity in your AWS SAM template, use the following syntax.

### YAML

```
  BatchSize: `Integer`
  ConsumerGroupId: `String`
  DestinationConfig: `DestinationConfig`
  Enabled: `Boolean`
  FilterCriteria: `FilterCriteria`
  KmsKeyArn: `String`
  MaximumBatchingWindowInSeconds: `Integer`
  ProvisionedPollerConfig: `ProvisionedPollerConfig`
  SchemaRegistryConfig: `SchemaRegistryConfig`
  SourceAccessConfigurations: `SourceAccessConfigurations`
  StartingPosition: `String`
  StartingPositionTimestamp: `Double`
  Stream: `String`
  Topics: `List`

```

## Properties

`BatchSize`

The maximum number of records in each batch that Lambda pulls from your stream or queue and sends to your function. Lambda passes all of the records in the batch to the function in a single call, up to the payload limit for synchronous invocation (6 MB).

_Default_: 100

_Valid Range_: Minimum value of 1. Maximum value of 10,000.

_Type_: Integer

_Required_: No

_AWS CloudFormation compatibility_: This property is passed directly to the
`BatchSize` property of an
`AWS::Lambda::EventSourceMapping` resource.

`ConsumerGroupId`

A string that configures how events will be read from Kafka topics.

_Type_: String

_Required_: No

_AWS CloudFormation compatibility_: This property is passed directly to the
`AmazonManagedKafkaConfiguration` property of an
`AWS::Lambda::EventSourceMapping` resource.

`DestinationConfig`

A configuration object that specifies the destination of an event after Lambda processes it.

Use this property to specify the destination of failed invocations from the Amazon MSK event source.

_Type_: [DestinationConfig](../../../AWSCloudFormation/latest/UserGuide/aws-resource-lambda-eventsourcemapping.md#cfn-lambda-eventsourcemapping-destinationconfig "../../../AWSCloudFormation/latest/UserGuide/aws-resource-lambda-eventsourcemapping.md#cfn-lambda-eventsourcemapping-destinationconfig")

_Required_: No

_AWS CloudFormation compatibility_: This property is passed directly to the
`DestinationConfig` property of an `AWS::Lambda::EventSourceMapping` resource.

`Enabled`

Disables the event source mapping to pause polling and invocation.

_Type_: Boolean

_Required_: No

_AWS CloudFormation compatibility_: This property is passed directly to the
`Enabled` property of an
`AWS::Lambda::EventSourceMapping` resource.

`FilterCriteria`

A object that defines the criteria that determines whether Lambda should process an
event. For more information, see [AWS Lambda event filtering](../../../lambda/latest/dg/invocation-eventfiltering.md "../../../lambda/latest/dg/invocation-eventfiltering.md") in
the _AWS Lambda Developer Guide_.

_Type_: [FilterCriteria](../../../AWSCloudFormation/latest/UserGuide/aws-properties-lambda-eventsourcemapping-filtercriteria.md "../../../AWSCloudFormation/latest/UserGuide/aws-properties-lambda-eventsourcemapping-filtercriteria.md")

_Required_: No

_AWS CloudFormation compatibility_: This property is passed directly to the
`FilterCriteria` property of an
`AWS::Lambda::EventSourceMapping` resource.

`KmsKeyArn`

The Amazon Resource Name (ARN) of the key to encrypt information related to this event.

_Type_: String

_Required_: No

_AWS CloudFormation compatibility_: This property is passed directly to the
`KmsKeyArn`
property of an `AWS::Lambda::EventSourceMapping` resource.

`MaximumBatchingWindowInSeconds`

The maximum amount of time to gather records before invoking the function, in
seconds.

_Type_: Integer

_Required_: No

_AWS CloudFormation compatibility_: This property is passed directly to the
`MaximumBatchingWindowInSeconds` property of an
`AWS::Lambda::EventSourceMapping` resource.

`ProvisionedPollerConfig`

Configuration to increase the amount of pollers used to compute event source mappings.
This configuration allows for a minimum of 1 poller and a maximum of 20 pollers. For an example,
refer to [ProvisionedPollerConfig example](#sam-property-function-msk-example-provisionedpollerconfig "#sam-property-function-msk-example-provisionedpollerconfig").

_Type_: [ProvisionedPollerConfig](../../../AWSCloudFormation/latest/UserGuide/aws-resource-lambda-eventsourcemapping.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-lambda-eventsourcemapping.md")

_Required_: No

_AWS CloudFormation compatibility_: This property is passed directly to the
`ProvisionedPollerConfig` property of an
`AWS::Lambda::EventSourceMapping` resource.

`SchemaRegistryConfig`

Configuration for using a schema registry with the Kafka event source.

###### Note

This feature requires `ProvisionedPollerConfig` to be configured.

_Type_: SchemaRegistryConfig

_Required_: No

_AWS CloudFormation compatibility:_ This property is passed directly to the
`AmazonManagedKafkaEventSourceConfig`
property of an `AWS::Lambda::EventSourceMapping` resource.

`SourceAccessConfigurations`

An array of the authentication protocol, VPC components, or virtual host to secure
and define your event source.

_Valid values_:
`CLIENT_CERTIFICATE_TLS_AUTH`

_Type_: List of [SourceAccessConfiguration](../../../AWSCloudFormation/latest/UserGuide/aws-properties-lambda-eventsourcemapping-sourceaccessconfiguration.md "../../../AWSCloudFormation/latest/UserGuide/aws-properties-lambda-eventsourcemapping-sourceaccessconfiguration.md")

_Required_: No

_AWS CloudFormation compatibility:_ This propertyrty is part of the
[AmazonManagedKafkaEventSourceConfig](../../../AWSCloudFormation/latest/TemplateReference/aws-properties-lambda-eventsourcemapping-amazonmanagedkafkaeventsourceconfig.md "../../../AWSCloudFormation/latest/TemplateReference/aws-properties-lambda-eventsourcemapping-amazonmanagedkafkaeventsourceconfig.md")
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

_AWS CloudFormation compatibility_: This property is passed directly to the
`StartingPosition` property of an
`AWS::Lambda::EventSourceMapping` resource.

`StartingPositionTimestamp`

The time from which to start reading, in Unix time seconds. Define
`StartingPositionTimestamp` when `StartingPosition` is specified
as `AT_TIMESTAMP`.

_Type_: Double

_Required_: No

_AWS CloudFormation compatibility_: This property is passed directly to the
`StartingPositionTimestamp` property of an
`AWS::Lambda::EventSourceMapping` resource.

`Stream`

The Amazon Resource Name (ARN) of the data stream or a stream consumer.

_Type_: String

_Required_: Yes

_AWS CloudFormation compatibility_: This property is passed directly to the
`EventSourceArn` property of an
`AWS::Lambda::EventSourceMapping` resource.

`Topics`

The name of the Kafka topic.

_Type_: List

_Required_: Yes

_AWS CloudFormation compatibility_: This property is passed directly to the
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
  MskClusterName4:
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
      - PolicyName: KafkaClusterPermissions
        PolicyDocument:
          Statement:
          - Action: [kafka:DescribeClusterV2, kafka:GetBootstrapBrokers]
            Effect: Allow
            Resource: 'arn:aws:kafka:us-east-1:123456789012:cluster/*'
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

  MyMskCluster:
    Type: AWS::MSK::Cluster
    Properties:
      BrokerNodeGroupInfo:
        ClientSubnets:
        - Ref: PreCreatedSubnetOne
        - Ref: PreCreatedSubnetTwo
        InstanceType: kafka.t3.small
        StorageInfo:
          EBSStorageInfo:
            VolumeSize: 1
      ClusterName:
        Ref: MskClusterName4
      KafkaVersion: 3.8.x
      NumberOfBrokerNodes: 2

  MyMskStreamProcessor:
    Type: AWS::Serverless::Function
    Properties:
      Runtime: nodejs18.x
      Handler: index.handler
      CodeUri: ${codeuri}
      Role:
        Fn::GetAtt: [MyLambdaExecutionRole, Arn]
      Events:
        MyMskEvent:
          Type: MSK
          Properties:
            StartingPosition: LATEST
            Stream:
              Ref: MyMskCluster
            SourceAccessConfigurations:
            - Type: SASL_SCRAM_512_AUTH
              URI: !Sub arn:${AWS::Partition}:secretsmanager:us-west-2:123456789012:secret:my-path/my-secret-name-1a2b3c
            Topics:
            - SchemaRegistryTestTopic
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
  MaximumPollers: 20
```

### Amazon MSK Example for Existing Cluster

The following is an example of an `MSK` event source type for an Amazon MSK
cluster that already exists in an AWS account.

#### YAML

```
Events:
  MSKEvent:
    Type: MSK
    Properties:
      StartingPosition: LATEST
      Stream: arn:aws:kafka:us-east-1:012345678012:cluster/exampleClusterName/abcdefab-1234-abcd-5678-cdef0123ab01-2
      Topics:
        - MyTopic

```

### Amazon MSK Example for Cluster Declared in Same Template

The following is an example of an `MSK` event source type for an Amazon MSK
cluster that is declared in the same template file.

#### YAML

```
Events:
  MSKEvent:
    Type: MSK
    Properties:
      StartingPosition: LATEST
      Stream:
        Ref: MyMskCluster   # This must be the name of an MSK cluster declared in the same template file
      Topics:
        - MyTopic

```

#### MSK Event Source with Schema Registry

The following is an example of an `MSK` event source type configured with a schema registry.

```
Events:
  MSKEvent:
    Type: MSK
    Properties:
      StartingPosition: LATEST
      Stream:
        Ref: MyMskCluster
      Topics:
        - SchemaRegistryTestTopic
      ProvisionedPollerConfig:
        MinimumPollers: 1
      SchemaRegistryConfig:
        SchemaRegistryURI: !Sub arn:${AWS::Partition}:glue:us-west-2:123456789012:registry/myregistry
        EventRecordFormat: JSON
        SchemaValidationConfigs:
          - Attribute: KEY
          - Attribute: VALUE
```

#### MSK Event Source with Confluent Schema Registry

The following is an example of an `MSK` event source type configured with a Confluent Schema Registry.

```
Events:
  MSKEvent:
    Type: MSK
    Properties:
      StartingPosition: LATEST
      Stream:
        Ref: MyMskCluster
      Topics:
        - SchemaRegistryTestTopic
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
```
