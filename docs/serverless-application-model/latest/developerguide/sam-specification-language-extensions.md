

# CloudFormation language extensions support
<a name="sam-specification-language-extensions"></a>

The AWS SAM CLI supports templates that use the `AWS::LanguageExtensions` transform, including `Fn::ForEach`, `Fn::Length`, `Fn::ToJsonString`, and `Fn::FindInMap` with `DefaultValue`. For complete reference information about these constructs, see [AWS::LanguageExtensions transform](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/transform-aws-languageextensions.html) in the *AWS CloudFormation User Guide*.

To use language extensions in a AWS SAM template, list `AWS::LanguageExtensions` in the `Transform` section *before* `AWS::Serverless-2016-10-31`:

```
Transform:
  - AWS::LanguageExtensions
  - AWS::Serverless-2016-10-31
```

When the AWS SAM CLI detects `AWS::LanguageExtensions` in a template's `Transform` section *and* you have opted in to local processing, it expands language extension constructs locally before running AWS SAM transforms. This enables `sam build`, `sam package`, `sam deploy`, `sam sync`, `sam validate`, `sam local invoke`, `sam local start-api`, and `sam local start-lambda` to work with templates that use these constructs.

Local processing is off by default. When off, the AWS SAM CLI passes the template through unchanged and CloudFormation processes the `AWS::LanguageExtensions` transform server-side at deploy time. For activation methods, see [Enabling language extensions](#sam-specification-language-extensions-enabling).

The expansion happens in two phases when enabled:

1. **Phase 1 (Language Extensions)** — `Fn::ForEach` loops are expanded, intrinsic functions are resolved where possible, and the template is converted to standard CloudFormation.

1. **Phase 2 (AWS SAM Transform)** — The expanded template is processed by the AWS SAM Translator as usual.

The original template (with `Fn::ForEach` intact) is preserved for CloudFormation deployment, since CloudFormation processes the `AWS::LanguageExtensions` transform server-side.

## Enabling language extensions
<a name="sam-specification-language-extensions-enabling"></a>

Local processing of `AWS::LanguageExtensions` is opt-in per command. There are three equivalent activation methods, listed in priority order:

1. **CLI flag** — pass `--language-extensions` on a single invocation:

   ```
   sam build --language-extensions
   sam package --language-extensions ...
   sam deploy --language-extensions ...
   ```

   `--no-language-extensions` explicitly disables, overriding both `samconfig.toml` and the environment variable described below.

1. **`samconfig.toml`** — persist the choice per project:

   ```
   [default.build.parameters]
   language_extensions = true
   
   [default.package.parameters]
   language_extensions = true
   
   [default.deploy.parameters]
   language_extensions = true
   
   [default.sync.parameters]
   language_extensions = true
   
   [default.local_invoke.parameters]
   language_extensions = true
   
   [default.local_start_api.parameters]
   language_extensions = true
   
   [default.local_start_lambda.parameters]
   language_extensions = true
   
   [default.validate.parameters]
   language_extensions = true
   ```

   A `samconfig.toml` entry is loaded as a default for the command, so it takes effect as if the flag were passed — and therefore wins over the environment variable.

1. **Environment variable** — set `SAM_CLI_ENABLE_LANGUAGE_EXTENSIONS=1` to enable for the current shell:

   ```
   export SAM_CLI_ENABLE_LANGUAGE_EXTENSIONS=1
   sam build
   sam local invoke MyFunction
   ```

   Truthy values (case-insensitive) are `1`, `true`, and `yes`. Anything else, including the empty string, is treated as off. The environment variable is consulted only when neither the CLI flag nor `samconfig.toml` sets a value.

**Important**  
Each command needs its own activation. Passing `--language-extensions` to `sam build` does not propagate to a later `sam local invoke` — local processing is decided per command invocation. Use the environment variable or a `samconfig.toml` entry to enable across commands without repeating the flag.

## Fn::ForEach
<a name="sam-specification-language-extensions-foreach"></a>

`Fn::ForEach` generates multiple resources, conditions, or outputs from a single template definition:

```
Transform:
  - AWS::LanguageExtensions
  - AWS::Serverless-2016-10-31

Parameters:
  ServiceNames:
    Type: CommaDelimitedList
    Default: "Users,Orders,Products"

Resources:
  Fn::ForEach::Services:
    - Name
    - !Ref ServiceNames
    - ${Name}Function:
        Type: AWS::Serverless::Function
        Properties:
          Handler: index.handler
          Runtime: python3.12
          CodeUri: ./services/${Name}
```

Running `sam build` expands this into `UsersFunction`, `OrdersFunction`, and `ProductsFunction`, each built from its respective source directory.

### Dynamic artifact properties
<a name="sam-specification-language-extensions-dynamic-artifacts"></a>

When a packageable property uses a loop variable (for example, `./services/${Name}`), the AWS SAM CLI generates a CloudFormation `Mappings` section that maps each collection value to its Amazon S3 URI. The `Fn::ForEach` body is rewritten to use `Fn::FindInMap` so CloudFormation can resolve the correct artifact at deploy time.

The recognized artifact properties are the same ones `sam package` rewrites today. That includes:


**Dynamic artifact properties recognized by the AWS SAM CLI**  

| Resource type | Property | 
| --- | --- | 
| `AWS::Serverless::Function` | `CodeUri`, `ImageUri` | 
| `AWS::Serverless::LayerVersion` | `ContentUri` | 
| `AWS::Serverless::Api` | `DefinitionUri` | 
| `AWS::Serverless::HttpApi` | `DefinitionUri` | 
| `AWS::Serverless::StateMachine` | `DefinitionUri` | 
| `AWS::Serverless::GraphQLApi` | `SchemaUri`, `CodeUri` | 
| `AWS::Serverless::Application` | `Location` | 
| `AWS::Lambda::Function` | `Code`, `Code.ImageUri` | 
| `AWS::Lambda::LayerVersion` | `Content` | 
| `AWS::ApiGateway::RestApi` | `BodyS3Location` | 
| `AWS::ApiGatewayV2::Api` | `BodyS3Location` | 
| `AWS::AppSync::GraphQLSchema` | `DefinitionS3Location` | 
| `AWS::AppSync::Resolver` | `RequestMappingTemplateS3Location`, `ResponseMappingTemplateS3Location`, `CodeS3Location` | 
| `AWS::AppSync::FunctionConfiguration` | `RequestMappingTemplateS3Location`, `ResponseMappingTemplateS3Location`, `CodeS3Location` | 
| `AWS::StepFunctions::StateMachine` | `DefinitionS3Location` | 
| `AWS::ElasticBeanstalk::ApplicationVersion` | `SourceBundle` | 
| `AWS::Glue::Job` | `Command.ScriptLocation` | 
| `AWS::CloudFormation::Stack` | `TemplateURL` | 
| `AWS::CloudFormation::StackSet` | `TemplateURL` | 
| `AWS::CloudFormation::ModuleVersion` | `ModulePackage` | 
| `AWS::CloudFormation::ResourceVersion` | `SchemaHandlerPackage` | 

For dotted properties (for example, `Command.ScriptLocation` on `AWS::Glue::Job` or `Code.ImageUri` on `AWS::Lambda::Function`), the value is read and written at the nested location on the resource. The generated Mapping name uses only the leaf segment of the property path.

When the property is loop-templated, the Mapping name is `SAM<LeafProperty><LoopName>` (for example, `SAMCodeUriServices` or `SAMScriptLocationJobs`).

**Important**  
Customer-authored mappings should not start with these `SAM*` prefixes — they are reserved for the AWS SAM CLI. See [Limitations](#sam-specification-language-extensions-limitations).

For example, after `sam package`:

```
Mappings:
  SAMCodeUriServices:
    Users:
      CodeUri: s3://my-bucket/abc123
    Orders:
      CodeUri: s3://my-bucket/def456
    Products:
      CodeUri: s3://my-bucket/ghi789

Resources:
  Fn::ForEach::Services:
    - Name
    - !Ref ServiceNames
    - ${Name}Function:
        Type: AWS::Serverless::Function
        Properties:
          Handler: index.handler
          Runtime: python3.12
          CodeUri: !FindInMap [SAMCodeUriServices, !Ref Name, CodeUri]
```

### Multiple resources per ForEach body
<a name="sam-specification-language-extensions-multiple-resources"></a>

A single `Fn::ForEach` body can emit more than one resource per iteration. Each resource is generated for every collection value:

```
Resources:
  Fn::ForEach::Tables:
    - TableName
    - [Users, Orders, Products]
    - ${TableName}Table:
        Type: AWS::DynamoDB::Table
        Properties:
          TableName: !Sub "${AWS::StackName}-${TableName}"
          # ...

      ${TableName}StreamProcessor:
        Type: AWS::Serverless::Function
        Properties:
          CodeUri: stream-processors/${TableName}/
          Events:
            DDBStream:
              Type: DynamoDB
              Properties:
                Stream: !GetAtt
                  - !Sub "${TableName}Table"
                  - StreamArn
```

### Mapping name collision resolution
<a name="sam-specification-language-extensions-mapping-collisions"></a>

When two resources in the same `Fn::ForEach` body declare the same dynamic artifact property (for example, both an `Api` and a `StateMachine` use `DefinitionUri`), the AWS SAM CLI appends a suffix taken from the static portion of the resource logical-ID template to keep Mapping names unique:


**Example of mapping names with collision suffixes**  

| Resource template | Property | Mapping name | 
| --- | --- | --- | 
| `${Svc}Api` | `DefinitionUri` | `SAMDefinitionUriServicesApi` | 
| `${Svc}StateMachine` | `DefinitionUri` | `SAMDefinitionUriServicesStateMachine` | 

When there is no collision the base name (for example, `SAMDefinitionUriServices`) is used.

### Parameter-based collections
<a name="sam-specification-language-extensions-parameter-collections"></a>

When the `Fn::ForEach` collection is a parameter reference (for example, `!Ref ServiceNames`) and the loop body uses a dynamic artifact property (for example, `CodeUri: ./services/${Name}`), the AWS SAM CLI needs the collection values to generate the `SAM*` Mappings described in [Dynamic artifact properties](#sam-specification-language-extensions-dynamic-artifacts). It resolves them when it processes the template, from:

1. `--parameter-overrides` passed to the AWS SAM CLI command.

1. The parameter's `Default` value in the template.

**Important**  
Because the `SAM*` Mappings are baked in at package time, you must re-package whenever you change the parameter value (for example, when adding a new service) so the Mappings include entries for the new values. This applies only when the parameter drives a dynamic artifact loop; other parameter overrides can be changed at deploy time as usual.

```
# Package with the values you intend to deploy with
sam package --language-extensions --parameter-overrides ServiceNames="Users,Orders,Products"

# Deploy with the same values
sam deploy --language-extensions --parameter-overrides ServiceNames="Users,Orders,Products"
```

### Nested stacks
<a name="sam-specification-language-extensions-nested-stacks"></a>

`Fn::ForEach` in nested stack templates (`AWS::CloudFormation::Stack`) is supported. The AWS SAM CLI passes the parent stack's `Parameters` property to the child template expansion, so child `Fn::ForEach` collections that reference parent-supplied parameters resolve correctly.

```
# parent.yaml
Resources:
  ChildStack:
    Type: AWS::CloudFormation::Stack
    Properties:
      TemplateURL: ./child.yaml
      Parameters:
        ServiceNames: "Users,Orders,Products"
```

### Nested Fn::ForEach
<a name="sam-specification-language-extensions-nested-foreach"></a>

Up to 5 levels of nesting are supported, matching the CloudFormation limit:

```
Resources:
  Fn::ForEach::Envs:
    - Env
    - [Dev, Staging, Prod]
    - Fn::ForEach::Services:
        - Svc
        - [Users, Orders]
        - ${Env}${Svc}Function:
            Type: AWS::Serverless::Function
            Properties:
              CodeUri: ./services/${Svc}
              Environment:
                Variables:
                  STAGE: ${Env}
```

### ForEach in Outputs
<a name="sam-specification-language-extensions-foreach-outputs"></a>

`Fn::ForEach` blocks are also expanded inside the `Outputs` section, so you can emit one output per collection value:

```
Outputs:
  Fn::ForEach::FunctionArns:
    - Name
    - [alpha, beta]
    - ${Name}FunctionArn:
        Value: !GetAtt
          - !Sub "${Name}Function"
          - Arn
```

### Conditions and DependsOn
<a name="sam-specification-language-extensions-conditions-dependson"></a>

Resources emitted by `Fn::ForEach` can carry `Condition` and `DependsOn` like any other resource. The condition or dependency is replicated onto each generated resource:

```
Conditions:
  IsProd: !Equals [!Ref Environment, prod]

Resources:
  SharedTable:
    Type: AWS::DynamoDB::Table
    # ...

  Fn::ForEach::Functions:
    - Name
    - [api, worker]
    - ${Name}Function:
        Type: AWS::Serverless::Function
        Condition: IsProd
        DependsOn: SharedTable
        Properties:
          Handler: main.handler
          CodeUri: functions/${Name}/
```

### &{identifier} syntax
<a name="sam-specification-language-extensions-identifier-syntax"></a>

The `&{identifier}` syntax strips non-alphanumeric characters from the substituted value, which is useful for generating valid logical IDs from values such as IP addresses:

```
Fn::ForEach::Hosts:
  - IP
  - ["10.0.0.1", "10.0.0.2"]
  - Host&{IP}:
      Type: AWS::EC2::Instance
      # Expands to Host10001, Host10002
```

## Supported intrinsic functions
<a name="sam-specification-language-extensions-supported-functions"></a>

The following intrinsic functions are resolved locally during expansion:


**Intrinsic functions resolved locally during language extensions expansion**  

| Function | Description | 
| --- | --- | 
| `Fn::ForEach` | Loop expansion. | 
| `Fn::Length` | Returns the count of list elements. | 
| `Fn::ToJsonString` | Converts a value to a JSON string. | 
| `Fn::FindInMap` | Map lookup, including the optional `DefaultValue`. | 
| `Fn::If` | Conditional value selection. | 
| `Fn::Sub` | String substitution. | 
| `Fn::Join` | String concatenation. | 
| `Fn::Split` | String splitting. | 
| `Fn::Select` | List element selection. | 
| `Fn::Base64` | Base64 encoding. | 
| `Fn::Equals`, `Fn::And`, `Fn::Or`, `Fn::Not` | Condition evaluation. | 
| `Ref` | Parameter and pseudo-parameter references. | 

Functions that require deployed resources (`Fn::GetAtt`, `Fn::ImportValue`, `Fn::GetAZs`) are preserved for CloudFormation to resolve at deploy time.

## Validation errors
<a name="sam-specification-language-extensions-validation-errors"></a>

The following template issues are caught locally before the AWS SAM transform runs:


**Validation errors raised during language extensions expansion**  

| Cause | Error message | 
| --- | --- | 
| The `Fn::ForEach` value is malformed — not a list, doesn't have exactly 3 elements, or has a non-string loop identifier. | `Fn::ForEach::<key> layout is incorrect` (raised as `InvalidTemplateException`). | 
| More than 5 levels of `Fn::ForEach` are nested. | `Fn::ForEach nesting depth of <N> exceeds the maximum allowed depth of 5. CloudFormation supports up to 5 nested Fn::ForEach loops.` | 
| The collection resolves to an empty list (for example, a `CommaDelimitedList` parameter with `Default: ""`). | No error — the loop is silently skipped and no resources are emitted. | 
| The `!Ref` in the collection points at a parameter that is not declared in the template. | No error — the unresolved reference is preserved in the template. At deploy time, CloudFormation will resolve it server-side. | 

## Limitations
<a name="sam-specification-language-extensions-limitations"></a>
+ **Collections must be resolvable at build/package time.** `Fn::ForEach` collections that use `Fn::GetAtt`, `Fn::ImportValue`, or SSM/Secrets Manager dynamic references cannot be expanded locally. Use a parameter with `--parameter-overrides` instead.
+ **Dynamic artifact mappings are fixed at package time.** When a `Fn::ForEach` collection is a parameter reference and the loop body uses a dynamic artifact property (for example, `CodeUri: ./services/${Name}`), the generated `SAM*` Mappings only contain entries for the parameter values that were resolved at package time. If you change `--parameter-overrides` for that parameter at deploy time without re-packaging, the new values won't have Mapping entries and deployment will fail. This does not apply to parameters that aren't used to drive a dynamic artifact `Fn::ForEach`.
+ **`DeletionPolicy` and `UpdateReplacePolicy`** are validated and resolved during expansion. They support `Ref` to parameters but not other intrinsic functions.
+ **Nesting limit.** Up to 5 levels of `Fn::ForEach` may be nested, matching the CloudFormation server-side limit.
+ **Reserved Mapping names.** Mapping names starting with any of the following are reserved for the AWS SAM CLI — do not author your own mappings with these prefixes:
  + `SAMCodeUri`, `SAMImageUri`, `SAMContentUri`, `SAMDefinitionUri`, `SAMSchemaUri`, `SAMBodyS3Location`, `SAMDefinitionS3Location`, `SAMTemplateURL`, `SAMCode`, `SAMContent` — emitted by `sam package` for dynamic artifact properties. See the [Dynamic artifact properties](#sam-specification-language-extensions-dynamic-artifacts) table.
  + `SAMLayers` — emitted by `sam build` when an `Fn::ForEach`-generated function picks up auto-generated dependency-layer references (Lambda layers the AWS SAM CLI builds into a nested stack). This prefix has no corresponding user-authored property; it is added automatically.

## Telemetry
<a name="sam-specification-language-extensions-telemetry"></a>

The AWS SAM CLI emits a `CFNLanguageExtensions` telemetry event when a command is invoked with `--language-extensions` (or its environment-variable equivalent) *and* the template declares the `AWS::LanguageExtensions` transform. The event fires once per invocation and no template content is transmitted. When local processing is off (the default), no event fires.