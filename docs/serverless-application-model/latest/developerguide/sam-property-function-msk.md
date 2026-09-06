

# MSK
<a name="sam-property-function-msk"></a>

The object describing an `MSK` event source type. For more information, see [Using AWS Lambda with Amazon MSK](https://docs.aws.amazon.com/lambda/latest/dg/with-msk.html) in the *AWS Lambda Developer Guide*.

AWS Serverless Application Model (AWS SAM) generates an [AWS::Lambda::EventSourceMapping](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-eventsourcemapping.html) resource when this event type is set.

To use Schema Registry, you need to define specific IAM role permissions for your function. See [Complete setup with IAM roles](#sam-property-function-msk-example-complete) for an example of the required configuration.

## Syntax
<a name="sam-property-function-msk-syntax"></a>

To declare this entity in your AWS SAM template, use the following syntax.

### YAML
<a name="sam-property-function-msk-syntax.yaml"></a>

```
  [BatchSize](#sam-function-msk-batchsize): {{Integer}}
  [BisectBatchOnFunctionError](#sam-function-msk-bisectbatchonfunctionerror): {{Boolean}}
  [ConsumerGroupId](#sam-function-msk-consumergroupid): {{String}}
  DestinationConfig: {{[DestinationConfig](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-eventsourcemapping-destinationconfig.html)}}
  [Enabled](#sam-function-msk-enabled): {{Boolean}}
  [FilterCriteria](#sam-function-msk-filtercriteria): {{[FilterCriteria](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-eventsourcemapping-filtercriteria.html)}}
  [FunctionResponseTypes](#sam-function-msk-functionresponsetypes): {{List}}
  KmsKeyArn: {{String}}
  [MaximumBatchingWindowInSeconds](#sam-function-msk-maximumbatchingwindowinseconds): {{Integer}}
  [MaximumRecordAgeInSeconds](#sam-function-msk-maximumrecordageinseconds): {{Integer}}
  [MaximumRetryAttempts](#sam-function-msk-maximumretryattempts): {{Integer}}
  [LoggingConfig](#sam-function-msk-loggingconfig): {{[LoggingConfig](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-eventsourcemapping-loggingconfig.html)}}
  [MetricsConfig](#sam-function-msk-metricsconfig): {{[MetricsConfig](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-eventsourcemapping-metricsconfig.html)}}
  [ProvisionedPollerConfig](#sam-function-msk-provisionedpollerconfig): {{[ProvisionedPollerConfig](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-eventsourcemapping-provisionedpollerconfig)}}
  [SchemaRegistryConfig](#sam-function-msk-schemaregistryconfig): {{[SchemaRegistryConfig](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-eventsourcemapping-schemaregistryconfig.html)}}
  SourceAccessConfigurations: {{[SourceAccessConfigurations](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-eventsourcemapping.html#cfn-lambda-eventsourcemapping-sourceaccessconfigurations)}}
  [StartingPosition](#sam-function-msk-startingposition): {{String}}
  StartingPositionTimestamp: {{Double}}
  [Stream](#sam-function-msk-stream): {{String}}
  [Topics](#sam-function-msk-topics): {{List}}
```

## Properties
<a name="sam-property-function-msk-properties"></a>

 `BatchSize`   <a name="sam-function-msk-batchsize"></a>
The maximum number of records in each batch that Lambda pulls from your stream or queue and sends to your function. Lambda passes all of the records in the batch to the function in a single call, up to the payload limit for synchronous invocation (6 MB).  
*Default*: 100  
*Valid Range*: Minimum value of 1. Maximum value of 10,000.  
*Type*: Integer  
*Required*: No  
*CloudFormation compatibility*: This property is passed directly to the `[BatchSize](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-eventsourcemapping.html#cfn-lambda-eventsourcemapping-batchsize)` property of an `AWS::Lambda::EventSourceMapping` resource.

 `BisectBatchOnFunctionError`   <a name="sam-function-msk-bisectbatchonfunctionerror"></a>
If the function returns an error, split the batch in two and retry.  
*Type*: Boolean  
*Required*: No  
*CloudFormation compatibility*: This property is passed directly to the `[BisectBatchOnFunctionError](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-eventsourcemapping.html#cfn-lambda-eventsourcemapping-bisectbatchonfunctionerror)` property of an `AWS::Lambda::EventSourceMapping` resource.

 `ConsumerGroupId`   <a name="sam-function-msk-consumergroupid"></a>
A string that configures how events will be read from Kafka topics.  
*Type*: String  
*Required*: No  
*CloudFormation compatibility*: This property is passed directly to the `[AmazonManagedKafkaConfiguration](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-eventsourcemapping.html)` property of an `AWS::Lambda::EventSourceMapping` resource.

 `DestinationConfig`   <a name="sam-function-msk-destinationconfig"></a>
A configuration object that specifies the destination of an event after Lambda processes it.  
Use this property to specify the destination of failed invocations from the Amazon MSK event source.  
*Type*: [DestinationConfig](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-eventsourcemapping.html#cfn-lambda-eventsourcemapping-destinationconfig)  
*Required*: No  
*CloudFormation compatibility*: This property is passed directly to the `[ DestinationConfig](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-eventsourcemapping-destinationconfig.html)` property of an `AWS::Lambda::EventSourceMapping` resource.

 `Enabled`   <a name="sam-function-msk-enabled"></a>
Disables the event source mapping to pause polling and invocation.  
*Type*: Boolean  
*Required*: No  
*CloudFormation compatibility*: This property is passed directly to the `[Enabled](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-eventsourcemapping.html#cfn-lambda-eventsourcemapping-enabled)` property of an `AWS::Lambda::EventSourceMapping` resource.

 `FilterCriteria`   <a name="sam-function-msk-filtercriteria"></a>
A object that defines the criteria that determines whether Lambda should process an event. For more information, see [AWS Lambda event filtering](https://docs.aws.amazon.com/lambda/latest/dg/invocation-eventfiltering.html) in the *AWS Lambda Developer Guide*.  
*Type*: [FilterCriteria](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-eventsourcemapping-filtercriteria.html)  
*Required*: No  
*CloudFormation compatibility*: This property is passed directly to the `[FilterCriteria](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-eventsourcemapping-filtercriteria.html)` property of an `AWS::Lambda::EventSourceMapping` resource.

 `FunctionResponseTypes`   <a name="sam-function-msk-functionresponsetypes"></a>
A list of the response types currently applied to the event source mapping. For more information, see [Reporting batch item failures](https://docs.aws.amazon.com/lambda/latest/dg/kafka-retry-configurations.html) in the *AWS Lambda Developer Guide*.  
*Valid values*: `ReportBatchItemFailures`  
*Type*: List  
*Required*: No  
*CloudFormation compatibility*: This property is passed directly to the `[FunctionResponseTypes](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-eventsourcemapping.html#cfn-lambda-eventsourcemapping-functionresponsetypes)` property of an `AWS::Lambda::EventSourceMapping` resource.

 `KmsKeyArn`   <a name="sam-function-msk-kmskeyarn"></a>
The Amazon Resource Name (ARN) of the key to encrypt information related to this event.  
*Type*: String  
*Required*: No  
*CloudFormation compatibility*: This property is passed directly to the `[KmsKeyArn](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-eventsourcemapping.html#cfn-lambda-eventsourcemapping-kmskeyarn)` property of an `AWS::Lambda::EventSourceMapping` resource.

 `MaximumBatchingWindowInSeconds`   <a name="sam-function-msk-maximumbatchingwindowinseconds"></a>
The maximum amount of time to gather records before invoking the function, in seconds.  
*Type*: Integer  
*Required*: No  
*CloudFormation compatibility*: This property is passed directly to the `[MaximumBatchingWindowInSeconds](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-eventsourcemapping.html#cfn-lambda-eventsourcemapping-maximumbatchingwindowinseconds)` property of an `AWS::Lambda::EventSourceMapping` resource.

 `MaximumRecordAgeInSeconds`   <a name="sam-function-msk-maximumrecordageinseconds"></a>
The maximum age of a record that Lambda sends to a function for processing.  
*Type*: Integer  
*Required*: No  
*CloudFormation compatibility*: This property is passed directly to the `[MaximumRecordAgeInSeconds](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-eventsourcemapping.html#cfn-lambda-eventsourcemapping-maximumrecordageinseconds)` property of an `AWS::Lambda::EventSourceMapping` resource.

 `MaximumRetryAttempts`   <a name="sam-function-msk-maximumretryattempts"></a>
The maximum number of times to retry when the function returns an error.  
*Type*: Integer  
*Required*: No  
*CloudFormation compatibility*: This property is passed directly to the `[MaximumRetryAttempts](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-eventsourcemapping.html#cfn-lambda-eventsourcemapping-maximumretryattempts)` property of an `AWS::Lambda::EventSourceMapping` resource.

 `LoggingConfig`   <a name="sam-function-msk-loggingconfig"></a>
A configuration object that specifies the logging configuration for the event source mapping.  
*Type*: [LoggingConfig](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-eventsourcemapping-loggingconfig.html)  
*Required*: No  
*CloudFormation compatibility*: This property is passed directly to the `[LoggingConfig](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-eventsourcemapping-loggingconfig.html)` property of an `AWS::Lambda::EventSourceMapping` resource.

 `MetricsConfig`   <a name="sam-function-msk-metricsconfig"></a>
A configuration object that specifies the metrics configuration for the event source mapping.  
*Type*: [MetricsConfig](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-eventsourcemapping-metricsconfig.html)  
*Required*: No  
*CloudFormation compatibility*: This property is passed directly to the `[MetricsConfig](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-eventsourcemapping-metricsconfig.html)` property of an `AWS::Lambda::EventSourceMapping` resource.

 `ProvisionedPollerConfig`   <a name="sam-function-msk-provisionedpollerconfig"></a>
Configuration to increase the amount of pollers used to compute event source mappings. This configuration allows for a minimum of 1 poller and a maximum of 2000 pollers. For an example, refer to [ProvisionedPollerConfig example](#sam-property-function-msk-example-provisionedpollerconfig).  
*Type*: [ProvisionedPollerConfig](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-eventsourcemapping-provisionedpollerconfig)  
*Required*: No  
*CloudFormation compatibility*: This property is passed directly to the `[ProvisionedPollerConfig](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-eventsourcemapping-provisionedpollerconfig)` property of an `AWS::Lambda::EventSourceMapping` resource.

`SchemaRegistryConfig`  <a name="sam-function-msk-schemaregistryconfig"></a>
Configuration for using a schema registry with the Kafka event source.  
This feature requires `ProvisionedPollerConfig` to be configured.
*Type*: SchemaRegistryConfig  
*Required*: No  
*CloudFormation compatibility:* This property is passed directly to the `[AmazonManagedKafkaEventSourceConfig](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-eventsourcemapping-amazonmanagedkafkaeventsourceconfig)` property of an `AWS::Lambda::EventSourceMapping` resource.

 `SourceAccessConfigurations`   <a name="sam-function-msk-sourceaccessconfigurations"></a>
An array of the authentication protocol, VPC components, or virtual host to secure and define your event source.  
*Valid values*: `CLIENT_CERTIFICATE_TLS_AUTH`  
*Type*: List of [SourceAccessConfiguration](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-eventsourcemapping-sourceaccessconfiguration.html)  
*Required*: No  
*CloudFormation compatibility:* This propertyrty is part of the [AmazonManagedKafkaEventSourceConfig](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-lambda-eventsourcemapping-amazonmanagedkafkaeventsourceconfig) property of an `AWS::Lambda::EventSourceMapping` resource.

 `StartingPosition`   <a name="sam-function-msk-startingposition"></a>
The position in a stream from which to start reading.  
+ `AT_TIMESTAMP` – Specify a time from which to start reading records.
+ `LATEST` – Read only new records.
+ `TRIM_HORIZON` – Process all available records.
*Valid values*: `AT_TIMESTAMP` \| `LATEST` \| `TRIM_HORIZON`  
*Type*: String  
*Required*: No  
*CloudFormation compatibility*: This property is passed directly to the `[StartingPosition](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-eventsourcemapping.html#cfn-lambda-eventsourcemapping-startingposition)` property of an `AWS::Lambda::EventSourceMapping` resource.

 `StartingPositionTimestamp`   <a name="sam-function-msk-startingpositiontimestamp"></a>
The time from which to start reading, in Unix time seconds. Define `StartingPositionTimestamp` when `StartingPosition` is specified as `AT_TIMESTAMP`.  
*Type*: Double  
*Required*: No  
*CloudFormation compatibility*: This property is passed directly to the `[StartingPositionTimestamp](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-eventsourcemapping.html#cfn-lambda-eventsourcemapping-startingpositiontimestamp)` property of an `AWS::Lambda::EventSourceMapping` resource.

 `Stream`   <a name="sam-function-msk-stream"></a>
The Amazon Resource Name (ARN) of the data stream or a stream consumer.  
*Type*: String  
*Required*: Yes  
*CloudFormation compatibility*: This property is passed directly to the `[EventSourceArn](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-eventsourcemapping.html#cfn-lambda-eventsourcemapping-eventsourcearn)` property of an `AWS::Lambda::EventSourceMapping` resource.

 `Topics`   <a name="sam-function-msk-topics"></a>
The name of the Kafka topic.  
*Type*: List  
*Required*: Yes  
*CloudFormation compatibility*: This property is passed directly to the `[Topics](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-eventsourcemapping.html#cfn-lambda-eventsourcemapping-topics)` property of an `AWS::Lambda::EventSourceMapping` resource.

## Examples
<a name="sam-property-function-msk--examples"></a>

### Complete setup with IAM roles
<a name="sam-property-function-msk-example-complete"></a>

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
<a name="sam-property-function-msk-example-provisionedpollerconfig"></a>

```
ProvisionedPollerConfig:
  MinimumPollers: 1
  MaximumPollers: 200
```

### Amazon MSK Example for Existing Cluster
<a name="sam-property-function-msk--examples--amazon-msk-example-for-existing-cluster"></a>

The following is an example of an `MSK` event source type for an Amazon MSK cluster that already exists in an AWS account.

#### YAML
<a name="sam-property-function-msk--examples--amazon-msk-example-for-existing-cluster--yaml"></a>

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
<a name="sam-property-function-msk--examples--amazon-msk-example-for-cluster-declared-in-same-template"></a>

The following is an example of an `MSK` event source type for an Amazon MSK cluster that is declared in the same template file.

#### YAML
<a name="sam-property-function-msk--examples--amazon-msk-example-for-cluster-declared-in-same-template--yaml"></a>

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
<a name="sam-property-function-msk-example-schemaregistry"></a>

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
<a name="sam-property-function-msk-example-schemaregistry-confluent"></a>

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