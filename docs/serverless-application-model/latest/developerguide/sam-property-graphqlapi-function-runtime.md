# Runtime

The runtime of your pipeline resolver or function. Specifies the name and version to
use.

## Syntax

To declare this entity in your AWS Serverless Application Model (AWS SAM) template, use the following
syntax.

### YAML

```
Name: `String`
Version: `String`
```

## Properties

`Name`

The name of the runtime to use. Currently, the only allowed value is
`APPSYNC_JS`.

_Type_: String

_Required_: Yes

_CloudFormation compatibility_: This property is passed directly to the
`Name` property of an `AWS::AppSync::FunctionConfiguration
 AppSyncRuntime` object.

`Version`

The version of the runtime to use. Currently, the only allowed version is
`1.0.0`.

_Type_: String

_Required_: Yes

_CloudFormation compatibility_: This property is passed directly to the
`RuntimeVersion` property of an
`AWS::AppSync::FunctionConfiguration AppSyncRuntime` object.
