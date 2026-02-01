# Globals section of the AWS SAM

template

Sometimes resources that you declare in an AWS SAM template have common configurations. For
example, you might have an application with multiple `AWS::Serverless::Function`
resources that have identical `Runtime`, `Memory`,
`VPCConfig`, `Environment`, and `Cors` configurations.
Instead of duplicating this information in every resource, you can declare them once in the
`Globals` section and let your resources inherit them.

The `Globals` section supports the following AWS SAM resource types:

- `AWS::Serverless::Api`
- `AWS::Serverless::CapacityProvider`
- `AWS::Serverless::Function`
- `AWS::Serverless::HttpApi`
- `AWS::Serverless::SimpleTable`
- `AWS::Serverless::StateMachine`
  Example:

```
Globals:
  Function:
    Runtime: nodejs12.x
    Timeout: 180
    Handler: index.handler
    Environment:
      Variables:
        TABLE_NAME: data-table

Resources:
  HelloWorldFunction:
    Type: AWS::Serverless::Function
    Properties:
      Environment:
        Variables:
          MESSAGE: "Hello From SAM"

  ThumbnailFunction:
    Type: AWS::Serverless::Function
    Properties:
      Events:
        Thumbnail:
          Type: Api
          Properties:
            Path: /thumbnail
            Method: POST
```

In this example, both `HelloWorldFunction` and `ThumbnailFunction`
use "nodejs12.x" for `Runtime`, "180" seconds for `Timeout`, and
"index.handler" for `Handler`. `HelloWorldFunction` adds the MESSAGE
environment variable, in addition to the inherited TABLE_NAME.
`ThumbnailFunction` inherits all the `Globals` properties and adds
an API event source.

## Supported resources and properties

AWS SAM supports the following resources and properties.

```
Globals:
  Api:
    AccessLogSetting:
    Auth:
    BinaryMediaTypes:
    CacheClusterEnabled:
    CacheClusterSize:
    CanarySetting:
    Cors:
    DefinitionUri:
    Domain:
    EndpointConfiguration:
    GatewayResponses:
    MethodSettings:
    MinimumCompressionSize:
    Name:
    OpenApiVersion:
    PropagateTags:
    TracingEnabled:
    Variables:

  CapacityProvider:
    InstanceRequirements:
    KmsKeyArn:
    OperatorRole:
    PropagateTags:
    ScalingConfig:
    Tags:
    VpcConfig:

  Function:
    Architectures:
    AssumeRolePolicyDocument:
    AutoPublishAlias:
    AutoPublishAliasAllProperties:
    CapacityProviderConfig:
    CodeSigningConfigArn:
    CodeUri:
    DeadLetterQueue:
    DeploymentPreference:
    Description:
    DurableConfig:
    Environment:
    EphemeralStorage:
    EventInvokeConfig:
    FileSystemConfigs:
    FunctionScalingConfig:
    FunctionUrlConfig:
    Handler:
    KmsKeyArn:
    Layers:
    LoggingConfig:
    MemorySize:
    PermissionsBoundary:
    PropagateTags:
    ProvisionedConcurrencyConfig:
    PublishToLatestPublished:
    RecursiveLoop:
    ReservedConcurrentExecutions:
    RolePath:
    Runtime:
    RuntimeManagementConfig:
    SnapStart:
    SourceKMSKeyArn:
    Tags:
    TenancyConfig:
    Timeout:
    Tracing:
    VersionDeletionPolicy:
    VpcConfig:

  HttpApi:
    AccessLogSettings:
    Auth:
    PropagateTags:
    StageVariables:
    Tags:

  SimpleTable:
    SSESpecification:

  StateMachine:
    PropagateTags:
```

###### Note

Any resources and properties that are not included in the previous list are not
supported. Some reasons for not supporting them include: 1) They open potential
security issues, or 2) They make the template hard to understand.

## Implicit

APIs

AWS SAM creates _implicit APIs_ when you declare an API in the
`Events` section. You can use `Globals` to override all
properties of implicit APIs.

## Overridable

properties

Resources can override the properties that you declare in the `Globals`
section. For example, you can add new variables to an environment variable map, or you
can override globally declared variables. But the resource cannot remove a property
that's specified in the `Globals` section.

More generally, the `Globals` section declares properties that all your
resources share. Some resources can provide new values for globally declared properties,
but they can't remove them. If some resources use a property but others don't, then you
must not declare them in the `Globals` section.

The following sections describe how overriding works for different data types.

### Primitive data types are replaced

Primitive data types include strings, numbers, Booleans, and so on.

The value specified in the `Resources` section replaces the value in
the `Globals` section.

Example:

```
Globals:
  Function:
    Runtime: nodejs12.x

Resources:
  MyFunction:
    Type: AWS::Serverless::Function
    Properties:
      Runtime: python3.9
```

The `Runtime` for `MyFunction` is set to
`python3.9`.

### Maps

are merged

Maps are also known as dictionaries or collections of key-value pairs.

Map entries in the `Resources` section are merged with global map
entries. If there are duplicates, the `Resource` section entry overrides
the `Globals` section entry.

Example:

```
Globals:
  Function:
    Environment:
      Variables:
        STAGE: Production
        TABLE_NAME: global-table

Resources:
  MyFunction:
    Type: AWS::Serverless::Function
    Properties:
      Environment:
        Variables:
          TABLE_NAME: resource-table
          NEW_VAR: hello
```

The environment variables of `MyFunction` are set to the
following:

```
{
  "STAGE": "Production",
  "TABLE_NAME": "resource-table",
  "NEW_VAR": "hello"
}
```

### Lists are additive

Lists are also known as arrays.

List entries in the `Globals` section are prepended to the list in the
`Resources` section.

Example:

```
Globals:
  Function:
    VpcConfig:
      SecurityGroupIds:
        - sg-123
        - sg-456

Resources:
  MyFunction:
    Type: AWS::Serverless::Function
    Properties:
      VpcConfig:
        SecurityGroupIds:
          - sg-first
```

The `SecurityGroupIds` for `MyFunction`'s
`VpcConfig` are set to the following:

```
[ "sg-123", "sg-456", "sg-first" ]
```
