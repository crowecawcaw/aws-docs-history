

# AWS::Serverless::WebFunction
<a name="sam-resource-webfunction"></a>

 Creates an AWS Lambda Web Function, which serves HTTP requests through a managed endpoint. Unlike a Lambda Event Function, which runs in response to invocations and events, a Web Function runs your web server and receives HTTP requests directly. From a single `AWS::Serverless::WebFunction`, AWS SAM generates the Web Function, an immutable revision that contains your code and configuration, and an endpoint that routes traffic to one or more revisions. 

**Note**  
When you deploy to AWS CloudFormation, AWS SAM transforms your AWS SAM resources into CloudFormation resources. For more information, see [Generated CloudFormation resources for AWS SAM](sam-specification-generated-resources.md). 

**Important**  
Your function code must run an HTTP server that listens on the host and port in the `AWS_LAMBDA_HTTP_ENDPOINT` environment variable. The runtime does not set `PORT`. By default, the runtime runs `index.js` at the root of the deployment package. Use [EntryPoint](#sam-webfunction-entrypoint) to run a different file.

**Important**  
The Amazon S3 bucket that holds your deployment package must meet the following requirements:  
Versioning is enabled.
A bucket policy grants `lambda.amazonaws.com` the `s3:GetObject` and `s3:GetObjectVersion` permissions. We recommend that you scope the policy with an `ArnLike` condition on `aws:SourceArn` that matches the function's revisions, for example `arn:aws:lambda:{{us-east-1}}:{{111122223333}}:web-function/{{my-function}}/revision/*`.
If the object is encrypted with SSE-KMS, it uses a customer managed key whose key policy allows `lambda.amazonaws.com` to call `kms:Decrypt`. The AWS managed key for Amazon S3 (`aws/s3`) isn't supported, because you can't change its key policy.
For an example bucket policy, see [Bucket policy for Lambda](https://docs.aws.amazon.com/lambda/latest/dg/web-functions-code-s3.html#web-functions-code-s3-bucket-policy) in the *AWS Lambda Developer Guide*.  
`CodeUri` must reference an object in Amazon S3. The `sam build` and `sam package` commands don't support local paths for this resource.

## Syntax
<a name="sam-resource-webfunction-syntax"></a>

To declare this entity in your AWS Serverless Application Model (AWS SAM) template, use the following syntax.

### YAML
<a name="sam-resource-webfunction-syntax.yaml"></a>

```
Type: AWS::Serverless::WebFunction
Properties:
  [AuthType](#sam-webfunction-authtype): {{String}}
  [AutoDeploymentMode](#sam-webfunction-autodeploymentmode): {{String}}
  [CodeUri](#sam-webfunction-codeuri): {{String | CodeUri}}
  [EgressNetworkConnectorArn](#sam-webfunction-egressnetworkconnectorarn): {{String}}
  [EndpointDescription](#sam-webfunction-endpointdescription): {{String}}
  [EndpointName](#sam-webfunction-endpointname): {{String}}
  [EndpointType](#sam-webfunction-endpointtype): {{String}}
  [EntryPoint](#sam-webfunction-entrypoint): {{String}}
  [EnvironmentVariables](#sam-webfunction-environmentvariables): {{Map}}
  [ExecutionRoleArn](#sam-webfunction-executionrolearn): {{String}}
  [FunctionName](#sam-webfunction-functionname): {{String}}
  [InlineCode](#sam-webfunction-inlinecode): {{String}}
  [KmsKeyArn](#sam-webfunction-kmskeyarn): {{String}}
  [LoggingConfig](#sam-webfunction-loggingconfig): {{Map}}
  [MaxConcurrencyPerEnvironment](#sam-webfunction-maxconcurrencyperenvironment): {{Integer}}
  [ReplicaRegions](#sam-webfunction-replicaregions): {{List | ReplicaRegions}}
  [RevisionDescription](#sam-webfunction-revisiondescription): {{String}}
  [RevisionWeights](#sam-webfunction-revisionweights): {{RevisionWeights}}
  [Runtime](#sam-webfunction-runtime): {{String}}
  [ScalingConfig](#sam-webfunction-scalingconfig): {{Map}}
  [Tags](#sam-webfunction-tags): {{Map}}
  [ThrottleConfig](#sam-webfunction-throttleconfig): {{Map}}
  [Timeout](#sam-webfunction-timeout): {{Integer}}
```

## Properties
<a name="sam-resource-webfunction-properties"></a>

 `AuthType`   <a name="sam-webfunction-authtype"></a>
How the endpoint authorizes requests.  
+ `IamAuth`: Lambda authorizes requests with Signature Version 4 and IAM. Callers need the `lambda:InvokeWebFunctionEndpoint` permission, granted through a resource-based policy on the function.
+ `ApplicationManaged`: the endpoint is public. Your function must authorize every request itself.
*Valid values*: `IamAuth`, `ApplicationManaged`  
*Type*: String  
*Required*: Yes  
*CloudFormation compatibility*: This property is passed directly to the `[AuthType](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-lambda-webfunctionendpoint.html#cfn-lambda-webfunctionendpoint-authtype)` property of an `AWS::Lambda::WebFunctionEndpoint` resource. 

 `AutoDeploymentMode`   <a name="sam-webfunction-autodeploymentmode"></a>
How the endpoint routes traffic across revisions.  
+ `LatestRevision`: sends 100% of traffic to the revision that this deployment creates.
+ `Disabled`: routes traffic according to [RevisionWeights](#sam-webfunction-revisionweights).
Which values you can use, and whether `RevisionWeights` is required, depends on [EndpointType](#sam-webfunction-endpointtype):  
+ `HomeRegion`: use either value. With `Disabled`, `RevisionWeights` is required.
+ `MultiRegion` or `PerRegion`: use `Disabled`. If you omit `RevisionWeights`, the endpoint routes 100% of traffic to the revision created in the same stack, so you can create the endpoint in a single deployment. Traffic doesn't move to revisions that later deployments create.
The value must resolve when AWS SAM transforms the template. A `Ref` to a parameter is supported. Other intrinsic functions are not supported.  
*Valid values*: `LatestRevision`, `Disabled`  
*Type*: String  
*Required*: No  
*Default*: `LatestRevision`  
*CloudFormation compatibility*: This property is unique to AWS SAM and doesn't have an CloudFormation equivalent.

 `CodeUri`   <a name="sam-webfunction-codeuri"></a>
The Amazon S3 location of the deployment package. Specify an `s3://{{bucket}}/{{key}}` URI or an object with `Bucket`, `Key`, and optional `Version` keys. For bucket requirements, see the note at the top of this page.  
*Type*: String \| [CodeUri](sam-property-webfunction-codeuri.md)  
*Required*: Yes  
*CloudFormation compatibility*: This property is similar to the `[BuildConfig.CodeConfig.S3Object](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-lambda-webfunctionrevision-s3object.html)` property of an `AWS::Lambda::WebFunctionRevision` resource. AWS SAM converts an `s3://` URI into `Bucket`, `Key`, and `VersionId`. 

 `EgressNetworkConnectorArn`   <a name="sam-webfunction-egressnetworkconnectorarn"></a>
The version-qualified ARN of a network connector that routes the function's outbound traffic through your VPC. The ARN must end in a version number, for example `arn:aws:lambda:us-east-1:123456789012:network-connector:my-connector:1`. To use the latest version of a connector in the same template, specify `!GetAtt {{MyConnector}}.LatestVersionArn`. The connector's [ComputeTypes](sam-resource-networkconnector.md#sam-networkconnector-computetypes) must be `WebFunction`.  
If you specify a literal string, AWS SAM checks that it's a version-qualified network connector ARN. Intrinsic functions are passed through and validated by the service. Changing this value creates a new revision.  
*Type*: String  
*Required*: No  
*CloudFormation compatibility*: This property is passed directly to the `[ServiceConfig.EgressNetworkConnectorArn](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-lambda-webfunctionrevision-serviceconfig.html)` property of an `AWS::Lambda::WebFunctionRevision` resource. 

 `EndpointDescription`   <a name="sam-webfunction-endpointdescription"></a>
A description of the endpoint.  
*Type*: String  
*Required*: No  
*CloudFormation compatibility*: This property is passed directly to the `[Description](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-lambda-webfunctionendpoint.html#cfn-lambda-webfunctionendpoint-description)` property of an `AWS::Lambda::WebFunctionEndpoint` resource. 

 `EndpointName`   <a name="sam-webfunction-endpointname"></a>
The name of the endpoint. Changing the name replaces the endpoint. Changing `EndpointType` also replaces the endpoint, so change `EndpointName` at the same time. CloudFormation can't replace a custom-named resource without a new name.  
*Type*: String  
*Required*: No  
*Default*: `prod`  
*CloudFormation compatibility*: This property is passed directly to the `[EndpointName](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-lambda-webfunctionendpoint.html#cfn-lambda-webfunctionendpoint-endpointname)` property of an `AWS::Lambda::WebFunctionEndpoint` resource. 

 `EndpointType`   <a name="sam-webfunction-endpointtype"></a>
Where the endpoint serves traffic.  
+ `HomeRegion`: serves from the stack's Region.
+ `MultiRegion`: replicates the function to the Regions in [ReplicaRegions](#sam-webfunction-replicaregions) and routes each request to the nearest Region.
+ `PerRegion`: exposes a separate endpoint in each replica Region.
`MultiRegion` and `PerRegion` require `AutoDeploymentMode: Disabled`.  
*Valid values*: `HomeRegion`, `MultiRegion`, `PerRegion`  
*Type*: String  
*Required*: No  
*Default*: `HomeRegion`  
*CloudFormation compatibility*: This property is passed directly to the `[EndpointType](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-lambda-webfunctionendpoint.html#cfn-lambda-webfunctionendpoint-endpointtype)` property of an `AWS::Lambda::WebFunctionEndpoint` resource. 

 `EntryPoint`   <a name="sam-webfunction-entrypoint"></a>
The file that the runtime runs, relative to the root of the deployment package. AWS SAM passes it to the runtime in the reserved `AWS_LAMBDA_NODEJS_ENTRYPOINT` environment variable.  
You can't use this property when `EnvironmentVariables` is an intrinsic function.  
*Type*: String  
*Required*: No  
*Default*: `index.js`  
*CloudFormation compatibility*: This property is unique to AWS SAM and doesn't have an CloudFormation equivalent.

 `EnvironmentVariables`   <a name="sam-webfunction-environmentvariables"></a>
Key-value pairs to set as environment variables for the revision.  
+ Keys must start with a letter and contain only letters, numbers, and underscores.
+ Values must be non-empty and at most 4,096 characters.
+ AWS SAM converts number and Boolean values to strings.
*Type*: Map  
*Required*: No  
*CloudFormation compatibility*: This property is passed directly to the `[ServiceConfig.EnvironmentVariables](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-lambda-webfunctionrevision-serviceconfig.html#cfn-lambda-webfunctionrevision-serviceconfig-environmentvariables)` property of an `AWS::Lambda::WebFunctionRevision` resource. 

 `ExecutionRoleArn`   <a name="sam-webfunction-executionrolearn"></a>
The ARN of the IAM role that the function assumes when it runs. If you don't specify a role, AWS SAM creates one with the `AWSLambdaBasicExecutionRole` managed policy and a logical ID of `{{<resource-logical-id>}}Role`.  
*Type*: String  
*Required*: No  
*CloudFormation compatibility*: This property is passed directly to the `[ServiceConfig.ExecutionRoleArn](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-lambda-webfunctionrevision-serviceconfig.html#cfn-lambda-webfunctionrevision-serviceconfig-executionrolearn)` property of an `AWS::Lambda::WebFunctionRevision` resource. 

 `FunctionName`   <a name="sam-webfunction-functionname"></a>
The name of the function. Function names must be unique within an account across all Regions. If you don't specify a name, AWS SAM generates one from the logical ID and the stack ID, at most 64 characters. Changing the name replaces the function, its revision, and its endpoint.  
*Type*: String  
*Required*: No  
*CloudFormation compatibility*: This property is passed directly to the `[FunctionName](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-lambda-webfunction.html#cfn-lambda-webfunction-functionname)` property of the `AWS::Lambda::WebFunction`, `AWS::Lambda::WebFunctionRevision`, and `AWS::Lambda::WebFunctionEndpoint` resources. 

 `InlineCode`   <a name="sam-webfunction-inlinecode"></a>
Not supported for `AWS::Serverless::WebFunction`. Use [CodeUri](#sam-webfunction-codeuri).  
*Type*: String  
*Required*: No  
*CloudFormation compatibility*: This property is unique to AWS SAM and doesn't have an CloudFormation equivalent.

 `KmsKeyArn`   <a name="sam-webfunction-kmskeyarn"></a>
The ARN of the AWS KMS key used to encrypt the revision's environment variables.  
*Type*: String  
*Required*: No  
*CloudFormation compatibility*: This property is passed directly to the `[KmsKeyArn](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-lambda-webfunctionrevision.html#cfn-lambda-webfunctionrevision-kmskeyarn)` property of an `AWS::Lambda::WebFunctionRevision` resource. 

 `LoggingConfig`   <a name="sam-webfunction-loggingconfig"></a>
The logging configuration for the revision, such as the log group and log levels.  
*Type*: Map  
*Required*: No  
*CloudFormation compatibility*: This property is passed directly to the `[ServiceConfig.TelemetryConfig.LoggingConfig](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-lambda-webfunctionrevision-telemetryconfig.html#cfn-lambda-webfunctionrevision-telemetryconfig-loggingconfig)` property of an `AWS::Lambda::WebFunctionRevision` resource. 

 `MaxConcurrencyPerEnvironment`   <a name="sam-webfunction-maxconcurrencyperenvironment"></a>
The maximum number of concurrent requests that each execution environment handles.  
*Type*: Integer  
*Required*: No  
*CloudFormation compatibility*: This property is passed directly to the `[ServiceConfig.MaxConcurrencyPerEnvironment](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-lambda-webfunctionrevision-serviceconfig.html#cfn-lambda-webfunctionrevision-serviceconfig-maxconcurrencyperenvironment)` property of an `AWS::Lambda::WebFunctionRevision` resource. 

 `ReplicaRegions`   <a name="sam-webfunction-replicaregions"></a>
The Regions to replicate the function to. Use this property with `MultiRegion` and `PerRegion` endpoints. Specify a list of Region codes and Region groups, or an object with `IncludeRegions` and optional `ExcludeRegions`.  
*Type*: List \| [ReplicaRegions](sam-property-webfunction-replicaregions.md)  
*Required*: No  
*CloudFormation compatibility*: This property is similar to the `[Regions](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-lambda-webfunctionendpoint.html#cfn-lambda-webfunctionendpoint-regions)` property of an `AWS::Lambda::WebFunctionEndpoint` resource. AWS SAM expands Region groups and applies `ExcludeRegions` to produce the Region list. 

 `RevisionDescription`   <a name="sam-webfunction-revisiondescription"></a>
A description of the revision that this deployment creates.  
*Type*: String  
*Required*: No  
*CloudFormation compatibility*: This property is passed directly to the `[Description](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-lambda-webfunctionrevision.html#cfn-lambda-webfunctionrevision-description)` property of an `AWS::Lambda::WebFunctionRevision` resource. 

 `RevisionWeights`   <a name="sam-webfunction-revisionweights"></a>
A map of revision IDs to traffic weights. Use this property when `AutoDeploymentMode` is `Disabled`. Specify up to two revisions. Each weight is an integer from 1 to 100, and the weights must add up to 100.  
*Type*: [RevisionWeights](sam-property-webfunction-revisionweights.md)  
*Required*: Conditional. Required when `AutoDeploymentMode` is `Disabled` and `EndpointType` is `HomeRegion`.  
*CloudFormation compatibility*: This property is similar to the `[RevisionWeights](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-lambda-webfunctionendpoint.html#cfn-lambda-webfunctionendpoint-revisionweights)` property of an `AWS::Lambda::WebFunctionEndpoint` resource. AWS SAM converts the map into a list of `RevisionId` and `Weight` objects. 

 `Runtime`   <a name="sam-webfunction-runtime"></a>
The runtime for the function, for example `nodejs24.x`.  
*Type*: String  
*Required*: Yes  
*CloudFormation compatibility*: This property is passed directly to the `[BuildConfig.RuntimeConfig.Runtime](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-lambda-webfunctionrevision-runtimeconfig.html#cfn-lambda-webfunctionrevision-runtimeconfig-runtime)` property of an `AWS::Lambda::WebFunctionRevision` resource. 

 `ScalingConfig`   <a name="sam-webfunction-scalingconfig"></a>
The scaling configuration for the endpoint, such as the maximum number of execution environments.  
*Type*: Map  
*Required*: No  
*CloudFormation compatibility*: This property is passed directly to the `[ScalingConfig](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-lambda-webfunctionendpoint.html#cfn-lambda-webfunctionendpoint-scalingconfig)` property of an `AWS::Lambda::WebFunctionEndpoint` resource. 

 `Tags`   <a name="sam-webfunction-tags"></a>
A map of key-value pairs that specifies the tags added to the function and to the execution role that AWS SAM generates.  
*Type*: Map  
*Required*: No  
*CloudFormation compatibility*: This property is similar to the `[Tags](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-lambda-webfunction.html#cfn-lambda-webfunction-tags)` property of an `AWS::Lambda::WebFunction` resource. The `Tags` property in AWS SAM consists of key-value pairs (whereas in CloudFormation this property consists of a list of `Tag` objects). Also, AWS SAM automatically adds a `lambda:createdBy:SAM` tag to the function and to the default role that is generated for it. 

 `ThrottleConfig`   <a name="sam-webfunction-throttleconfig"></a>
The throttling configuration for the endpoint, such as the maximum request rate.  
*Type*: Map  
*Required*: No  
*CloudFormation compatibility*: This property is passed directly to the `[ThrottleConfig](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-lambda-webfunctionendpoint.html#cfn-lambda-webfunctionendpoint-throttleconfig)` property of an `AWS::Lambda::WebFunctionEndpoint` resource. 

 `Timeout`   <a name="sam-webfunction-timeout"></a>
The maximum time, in seconds, that the function can run per request. Valid values are from 3 to 900.  
*Type*: Integer  
*Required*: No  
*Default*: `30`  
*CloudFormation compatibility*: This property is passed directly to the `[ServiceConfig.TimeoutSeconds](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-lambda-webfunctionrevision-serviceconfig.html#cfn-lambda-webfunctionrevision-serviceconfig-timeoutseconds)` property of an `AWS::Lambda::WebFunctionRevision` resource. 

## Return Values
<a name="sam-resource-webfunction-return-values"></a>

### Ref
<a name="sam-resource-webfunction-return-values-ref"></a>

When the logical ID of this resource is provided to the `Ref` intrinsic function, it returns the ARN of the Web Function. Where you need the function name, use the value of `FunctionName` instead.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-ref.html) in the *AWS CloudFormation User Guide*.

### Fn::GetAtt
<a name="sam-resource-webfunction-return-values-fn--getatt"></a>

`Fn::GetAtt` returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using `Fn::GetAtt`, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html) in the *AWS CloudFormation User Guide*.

`FunctionArn`  <a name="sam-webfunction-getatt-functionarn"></a>
The Amazon Resource Name (ARN) of the Web Function.

`State`  <a name="sam-webfunction-getatt-state"></a>
The current state of the Web Function.

`StateReason`  <a name="sam-webfunction-getatt-statereason"></a>
The reason for the current state of the Web Function.

`CreatedAt`  <a name="sam-webfunction-getatt-createdat"></a>
The time that the Web Function was created.

`UpdatedAt`  <a name="sam-webfunction-getatt-updatedat"></a>
The time that the Web Function was last updated.

To reference the revision or endpoint that AWS SAM generates, use their logical IDs, `{{<resource-logical-id>}}Revision` and `{{<resource-logical-id>}}Endpoint`. For example, `!GetAtt MyWebFunctionEndpoint.DomainName` returns the domain name of the endpoint for a Web Function with the logical ID `MyWebFunction`. For more information, see [CloudFormation resources generated when AWS::Serverless::WebFunction is specified](sam-specification-generated-resources-webfunction.md).

## Examples
<a name="sam-resource-webfunction-examples"></a>

### Basic Web Function
<a name="sam-resource-webfunction-example-basic"></a>

The following example creates a Web Function with an IAM-authorized endpoint in the stack's Region. AWS SAM generates the execution role, and the endpoint routes all traffic to the revision that this deployment creates.

```
AWSTemplateFormatVersion: '2010-09-09'
Transform: AWS::Serverless-2016-10-31

Resources:
  MyWebFunction:
    Type: AWS::Serverless::WebFunction
    Properties:
      Runtime: nodejs24.x
      AuthType: IamAuth
      CodeUri:
        Bucket: amzn-s3-demo-bucket
        Key: webfn.zip
        Version: {{object-version-id}}
      Timeout: 30

Outputs:
  EndpointUrl:
    Value: !Sub https://${MyWebFunctionEndpoint.DomainName}
```

### Split traffic between two revisions
<a name="sam-resource-webfunction-example-canary"></a>

The following example disables automatic deployment and sends 90% of traffic to one existing revision and 10% to another. Both revisions must already exist.

```
AWSTemplateFormatVersion: '2010-09-09'
Transform: AWS::Serverless-2016-10-31

Resources:
  MyWebFunction:
    Type: AWS::Serverless::WebFunction
    Properties:
      Runtime: nodejs24.x
      AuthType: IamAuth
      CodeUri: s3://amzn-s3-demo-bucket/webfn-v2.zip
      AutoDeploymentMode: Disabled
      RevisionWeights:
        rev-abc123: 90
        rev-def456: 10
```

### Multi-Region Web Function
<a name="sam-resource-webfunction-example-multiregion"></a>

The following example replicates the function to the US Regions except `us-west-1` and routes each request to the nearest Region. Because `RevisionWeights` is omitted, the endpoint routes all traffic to the revision created in this stack.

```
AWSTemplateFormatVersion: '2010-09-09'
Transform: AWS::Serverless-2016-10-31

Resources:
  MyWebFunction:
    Type: AWS::Serverless::WebFunction
    Properties:
      Runtime: nodejs24.x
      AuthType: IamAuth
      CodeUri:
        Bucket: amzn-s3-demo-bucket
        Key: webfn.zip
        Version: {{object-version-id}}
      EndpointName: prodmr
      EndpointType: MultiRegion
      AutoDeploymentMode: Disabled
      ReplicaRegions:
        IncludeRegions:
          - US
        ExcludeRegions:
          - us-west-1
```

### Web Function with VPC egress
<a name="sam-resource-webfunction-example-vpc-egress"></a>

The following example creates a network connector for Web Functions and routes the function's outbound traffic through the connector's subnets and security groups.

```
AWSTemplateFormatVersion: '2010-09-09'
Transform: AWS::Serverless-2016-10-31

Resources:
  MyConnector:
    Type: AWS::Serverless::NetworkConnector
    Properties:
      ComputeTypes:
        - WebFunction
      VpcConfig:
        SubnetIds:
          - subnet-0abc123def4567890
          - subnet-0def456abc7890123
        SecurityGroupIds:
          - sg-0abc1234abcde0001
        NetworkProtocol: IPv4

  MyWebFunction:
    Type: AWS::Serverless::WebFunction
    Properties:
      Runtime: nodejs24.x
      AuthType: IamAuth
      CodeUri:
        Bucket: amzn-s3-demo-bucket
        Key: webfn.zip
        Version: {{object-version-id}}
      EgressNetworkConnectorArn: !GetAtt MyConnector.LatestVersionArn
```