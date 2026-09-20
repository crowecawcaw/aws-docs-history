

# Use variables in your custom component document
<a name="toe-user-defined-variables"></a>

Variables provide a way to label data with meaningful names that can be used throughout an application. You can define custom variables with simple and readable formats for complex workflows, and reference them in the YAML application component document for an AWSTOE component.

This section provides information to help you define variables for your AWSTOE component in the YAML application component document, including syntax, name constraints, and examples.

## Constants
<a name="user-defined-vars-constants"></a>

Constants are immutable variables that cannot be modified or overridden once defined. Constants can be defined using values in the `constants` section of an AWSTOE document.

**Rules for constant names**
+ The name must be between 3 and 128 characters in length.
+ The name can only contain alphanumeric characters (a-z, A-Z, 0-9), dashes (-), or underscores (\_).
+ The name must be unique within the document.
+ The name must be specified as a YAML string.

**Syntax**

```
constants:
  - <name>:
      type: <constant type>
      value: <constant value>
```


| Key name | Required | Description | 
| --- | --- | --- | 
| `name` | Yes | Name of the constant. Must be unique for the document (it must not be the same as any other parameter names or constants). | 
| `value` | Yes | Value of the constant. | 
| `type` | Yes | Type of the constant. Supported type is string. | 

**Reference constant values in a document**  
You can reference constants in step or loop inputs inside of your YAML document, as follows:
+ Constant references are case-sensitive, and the name must match exactly.
+ The name must be enclosed within double curly braces `{{` {{MyConstant}} `}}`.
+ Spaces are allowed within the curly braces, and are automatically trimmed. For example, all of the following references are valid:

  `{{ {{MyConstant}} }}`, `{{ {{MyConstant}}}}`, `{{{{MyConstant}} }}`, `{{{{MyConstant}}}}`
+ The reference in the YAML document must be specified as a string (enclosed in single or double quotes).

  For example: `- {{ {{MyConstant}} }}` is not valid, as it is not identified as a string.

  However, the following references are both valid: `- '{{ {{MyConstant}} }}'` and `- "{{ {{MyConstant}} }}"`.

**Examples**  
Constant referenced in step inputs

```
name: Download AWS CLI version 2
schemaVersion: 1.0
constants:
  - Source:
      type: string
      value: https://awscli.amazonaws.com/AWSCLIV2.msi
phases:
  - name: build
    steps:
      - name: Download
        action: WebDownload
        inputs:
          - source: '{{ Source }}'
            destination: 'C:\Windows\Temp\AWSCLIV2.msi'
```

Constant referenced in loop inputs

```
name: PingHosts
schemaVersion: 1.0
constants:
  - Hosts:
      type: string
      value: 127.0.0.1,amazon.com
phases:
  - name: build
    steps:
      - name: Ping
        action: ExecuteBash
        loop:
          forEach:
            list: '{{ Hosts }}'
            delimiter: ','
        inputs:
          commands:
            - ping -c 4 {{ loop.value }}
```

## Parameters
<a name="user-defined-vars-parameters"></a>

Parameters are mutable variables, with settings that the calling application can provide at runtime. You can define parameters in the `Parameters` section of the YAML document.

**Rules for parameter names**
+ The name must be between 3 and 128 characters in length.
+ The name can only contain alphanumeric characters (a-z, A-Z, 0-9), dashes (-), or underscores (\_).
+ The name must be unique within the document.
+ The name must be specified as a YAML string.

### Syntax
<a name="vars-parameters-syntax"></a>

```
parameters:
  - <name>:
      type: <parameter type>
      default: <parameter value>
      description: <parameter description>
```


| Key name | Required | Description | 
| --- | --- | --- | 
| `name` | Yes | The name of the parameter. Must be unique for the document (it must not be the same as any other parameter names or constants). | 
| `type` | Yes | The data type of the parameter. Supported types include: `string`. | 
| `default` | No | The default value for the parameter. | 
| `description` | No | Describes the parameter. | 

### Reference parameter values in a document
<a name="vars-parameters-referencing"></a>

You can reference parameters in step or loop inputs inside of your YAML document, as follows:
+ Parameter references are case-sensitive, and the name must match exactly.
+ The name must be enclosed within double curly braces `{{` {{MyParameter}} `}}`.
+ Spaces are allowed within the curly braces, and are automatically trimmed. For example, all of the following references are valid:

  `{{ {{MyParameter}} }}`, `{{ {{MyParameter}}}}`, `{{{{MyParameter}} }}`, `{{{{MyParameter}}}}`
+ The reference in the YAML document must be specified as a string (enclosed in single or double quotes).

  For example: `- {{ {{MyParameter}} }}` is not valid, as it is not identified as a string.

  However, the following references are both valid: `- '{{ {{MyParameter}} }}'` and `- "{{ {{MyParameter}} }}"`.

**Examples**  
The following examples show how to use parameters in your YAML document:
+ Refer to a parameter in step inputs:

  ```
  name: Download AWS CLI version 2
  schemaVersion: 1.0
  parameters:
    - Source:
        type: string
        default: 'https://awscli.amazonaws.com/AWSCLIV2.msi'
        description: The AWS CLI installer source URL.
  phases:
    - name: build
      steps:
        - name: Download
          action: WebDownload
          inputs:
            - source: '{{ Source }}'
              destination: 'C:\Windows\Temp\AWSCLIV2.msi'
  ```
+ Refer to a parameter in loop inputs:

  ```
  name: PingHosts
  schemaVersion: 1.0
  parameters:
    - Hosts:
        type: string
        default: 127.0.0.1,amazon.com
        description: A comma separated list of hosts to ping.
  phases:
    - name: build
      steps:
        - name: Ping
          action: ExecuteBash
          loop:
            forEach:
              list: '{{ Hosts }}'
              delimiter: ','
          inputs:
            commands:
              - ping -c 4 {{ loop.value }}
  ```

### Override parameters at runtime
<a name="vars-parameters-set-at-runtime"></a>

You can use the `--parameters` option from the AWS CLI with a key-value pair to set a parameter value at runtime.
+ Specify the parameter key-value pair as the name and value, separated by an equals sign (<name>=<value>).
+ Multiple parameters must be separated by a comma.
+ Parameter names that are not found in the YAML component document are ignored.
+ The parameter name and value are both required.

**Important**  
Component parameters are plain text values, and are logged in AWS CloudTrail. We recommend that you use AWS Secrets Manager or the AWS Systems Manager Parameter Store to store your secrets. For more information about Secrets Manager, see [What is Secrets Manager?](https://docs.aws.amazon.com/secretsmanager/latest/userguide/intro.html) in the *AWS Secrets Manager User Guide*. For more information about AWS Systems Manager Parameter Store, see [AWS Systems Manager Parameter Store](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-parameter-store.html) in the *AWS Systems Manager User Guide*.

#### Syntax
<a name="vars-runtime-parameters-syntax"></a>

```
--parameters {{name1}}={{value1}},{{name2}}={{value2}}...
```


| CLI option | Required | Description | 
| --- | --- | --- | 
| --parameters {{name}}={{value}},... | No | This option takes list of key-value pairs, with the parameter name as the key. | 

**Examples**  
The following examples show how to use parameters in your YAML document:
+ The parameter key-value pair specified in this `--parameter` option is not valid:

  ```
  --parameters ntp-server=
  ```
+ Set one parameter key-value pair with the `--parameter` option in the AWS CLI:

  ```
  --parameters ntp-server=ntp-server-windows-qe.us-east1.amazon.com
  ```
+ Set multiple parameter key-value pairs with the `--parameter` option in the AWS CLI:

  ```
  --parameters ntp-server=ntp-server.amazon.com,http-url=https://internal-us-east1.amazon.com
  ```

## Use Systems Manager Parameter Store parameters
<a name="toe-ssm-parameters"></a>

You can reference AWS Systems Manager Parameter Store parameters (SSM parameters) in your component documents by prefixing variables with `aws:ssm`. For example, 

`{{ aws:ssm:/my/param }}` resolves to the value of the SSM parameter `/my/param`.

This feature supports the following SSM parameter types:
+ String – Maps to the AWSTOE string type.
+ StringList – Maps to the AWSTOE `stringList` type.
+ SecureString – Maps to the AWSTOE string type.

For more information about the Parameter Store see [AWS Systems Manager Parameter Store](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-parameter-store.html) in the *AWS Systems Manager User Guide*.

You can also reference AWS Secrets Manager secrets using an SSM parameter `SecureString`. For example: `{{ aws:ssm:/aws/reference/secretsmanager/test/test-secret }}`. For more information, see [Referencing AWS Secrets Manager secrets from Parameter Store parameters](https://docs.aws.amazon.com/systems-manager/latest/userguide/integration-ps-secretsmanager.html).

**Important**  
Image Builder excludes `SecureString` parameter resolution from its logs. However, you are also responsible for ensuring that sensitive information is not logged through commands issued in the component document. For example, if you use the `echo` command with a secure string, the command writes a plaintext value to the log.

### Required IAM permissions
<a name="toe-ssm-parameters-permissions"></a>

To use Systems Manager parameters in your components, your instance role must have the `ssm:GetParameter` permission for the parameter resource ARN. For example:

------
#### [ JSON ]

****  

```
{
	"Version":"2012-10-17",		 	 	 
	"Statement": [
		{
			"Effect": "Allow",
			"Action": "ssm:GetParameter",
			"Resource": "arn:aws:ssm:*:{{111122223333}}:parameter/ImageBuilder-*"
		}
	]
}
```

------

To access encrypted values, you'll also need the following permissions:
+ Add `kms:Decrypt` for `SecureString` parameters or AWS Secrets Manager values that are encrypted with a customer managed AWS KMS key.
+ Add `secretsmanager:GetSecretValue` if you reference a Secrets Manager secret.

### Reference an SSM parameter in a component document
<a name="toe-ssm-parameters-example"></a>

The following example shows how to reference an Systems Manager Parameter Store parameter of Systems Manager parameters in a component:

```
name: UseSSMParameterVariable
description: This is a sample component document that prints out the value of an SSM Parameter. Never do this for a SecureString parameter.
schemaVersion: 1.0

phases:
  - name: verify
    steps:
      - name: EchoParameterValue
        action: ExecuteBash
        inputs:
          commands:
            - echo "Log SSM parameter name: {{/my/test/param}}, value {{ aws:ssm:{{/my/test/param}} }}."
```

### Dynamic runtime variable resolution for SSM parameters
<a name="toe-dynamic-vars"></a>

AWSTOE provides the following built-in function that you can use within variable references to manipulate or transform values at runtime.

#### resolve function
<a name="toe-function-resolve"></a>

The `resolve` function resolves a variable reference inside of another variable reference, allowing for dynamic variable name referencing. This is useful when working with SSM parameters where part of the parameter path may be variable and passed in as a document parameter.

The `resolve` function only supports dynamic resolution of the name portion of an SSM parameter.

##### Syntax
<a name="toe-function-resolve-syntax"></a>

The `dynamic_variable` in the following example represents the name of an SSM parameter, and must be one of the following:
+ An SSM parameter reference (for example, `aws:ssm:{{/my/param}}`)
+ A component document parameter reference (for example, `{{parameter-name}}`)

```
{{ aws:ssm:resolve({{dynamic_variable}}) }}
```

##### Example: Resolve an SSM parameter at runtime
<a name="toe-function-resolve-examples"></a>

The following example shows how to use the `resolve` function in a YAML component document:

```
name: SsmParameterTest
description: This component verifies an SSM parameter variable reference with the echo command.
schemaVersion: 1.0

parameters:
  - parameter-name:
      type: string
      description: "test"

phases:
  - name: validate
    steps:
      - name: PrintDynamicVariable
        action: ExecuteBash
        inputs:
          commands:
            - echo "{{ aws:ssm:resolve(parameter-name) }}"
```

## Use environment variables
<a name="toe-env-variables"></a>

AWSTOE can resolve operating system environment variables that are set on the build or test instance. To reference an environment variable, prefix the variable name with `env:`. For example, `{{ env:{{MY_VAR}} }}` resolves to the value of the `MY_VAR` environment variable on the instance.

AWSTOE matches environment variable names exactly. A name can contain any characters that are valid for the operating system, including dots, spaces, and parentheses. For example, `{{ env:ProgramFiles(x86) }}` is a valid reference on Windows.

The following example shows how to reference an environment variable in a component:

```
name: UseEnvironmentVariable
description: This sample component prints out the value of an environment variable.
schemaVersion: 1.0

phases:
  - name: build
    steps:
      - name: EchoEnvironmentVariable
        action: ExecuteBash
        inputs:
          commands:
            - echo "The value of SOME_VAR is {{ env:{{SOME_VAR}} }}."
```

### Environment variables that Image Builder provides
<a name="toe-ib-env-variables"></a>

When Image Builder runs a component on a build or test instance, it sets environment variables that describe the current image build. Your components read these values with the AWSTOE `env:` variable prefix described earlier in this topic.

Image Builder provides the following environment variables.


| Name | Description | 
| --- | --- | 
| `IMAGE_WORKFLOW_EXECUTION_ID` | The ID of the workflow execution for the current image build. | 
| `IMAGE_STEP_EXECUTION_ID` | The ID of the workflow step execution that is running the component. | 
| `IMAGE_BUILD_VERSION_ARN` | The Amazon Resource Name (ARN) of the image build version that Image Builder creates. | 
| `IMAGE_PIPELINE_ARN` | The ARN of the image pipeline. This value is an empty string when the build does not run from a pipeline. | 
| `IMAGE_PHASE` | The current image build stage: `BUILDING` during the build stage, or `TESTING` during the test stage.<br />This stage is distinct from the AWSTOE component document phases (`build`, `validate`, and `test`). The `IMAGE_PHASE` value never takes a component document phase name. | 
| `IMAGE_VERSION` | The semantic version of the image (for example, `2.1.1`). | 
| `IMAGE_BUILD_VERSION` | The build version number of the image (for example, `1`). | 

The following example shows how to read Image Builder environment variables in a component:

```
name: UseImageBuilderEnvironmentVariables
description: This sample component prints out Image Builder environment variable values.
schemaVersion: 1.0

phases:
  - name: build
    steps:
      - name: EchoImageBuildValues
        action: ExecuteBash
        inputs:
          commands:
            - echo "Image phase: {{ env:IMAGE_PHASE }}."
            - echo "Image build version ARN: {{ env:IMAGE_BUILD_VERSION_ARN }}."
```

## Use instance metadata (IMDS) variables
<a name="toe-imds-variables"></a>

AWSTOE can resolve values from the Amazon EC2 Instance Metadata Service (IMDS) on the build or test instance. To reference a metadata value, prefix the metadata path with `aws:imds:`. The path is relative to the instance metadata `meta-data/` category. For example, `{{ aws:imds:instance-id }}` resolves to the instance ID. The reference `{{ aws:imds:placement/region }}` resolves to the AWS Region.

**Unsupported metadata paths**  
AWSTOE does not support the `iam/` and `identity-credentials/` metadata paths. These paths return sensitive credential data. AWSTOE rejects references to them when it validates the component document.

For more information about instance metadata, see [Use instance metadata to manage your EC2 instance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-metadata.html) in the *Amazon EC2 User Guide*.

The following example shows how to reference an IMDS value in a component:

```
name: UseInstanceMetadataVariable
description: This sample component prints out the instance ID from IMDS.
schemaVersion: 1.0

phases:
  - name: build
    steps:
      - name: EchoInstanceId
        action: ExecuteBash
        inputs:
          commands:
            - echo "The instance ID is {{ aws:imds:instance-id }}."
```

## Use context variables
<a name="toe-context-variables"></a>

AWSTOE provides context variables that describe the current execution and instance. To reference a context variable, prefix the key with `context:`. For example, `{{ context:accountId }}` resolves to the AWS account ID.

AWSTOE provides the following context variables.


| Key | Description | 
| --- | --- | 
| `executionId` | The ID of the current AWSTOE execution. | 
| `accountId` | The ID of the AWS account that the instance runs in. | 
| `region` | The AWS Region that the instance runs in. | 
| `osPlatform` | The operating system platform of the instance (for example, `linux` or `windows`). | 
| `osName` | The operating system name (for example, `Amazon Linux` or `Ubuntu`). On Linux, AWSTOE reads this value from `/etc/os-release`. | 
| `osVersion` | The operating system version (for example, `2023`). On Linux, AWSTOE reads this value from `/etc/os-release`. On Windows and macOS, this value is an empty string. | 
| `date` | The current date in UTC, in `YYYY-MM-DD` format (for example, `2026-06-15`). | 
| `dateTime` | The current date and time in UTC, in RFC 3339 format (for example, `2026-06-15T10:30:00Z`). | 
| `uuid` | A randomly generated version 4 UUID. | 
| `hostname` | The hostname of the instance. | 
| `phase` | The name of the currently running phase. | 
| `step` | The name of the currently running step. | 

**Note**  
To get the instance ID, use the IMDS variable `{{ aws:imds:instance-id }}` rather than a context variable.

The following example shows how to reference context variables in a component:

```
name: UseContextVariables
description: This sample component prints out context variable values.
schemaVersion: 1.0

phases:
  - name: build
    steps:
      - name: EchoContextValues
        action: ExecuteBash
        inputs:
          commands:
            - echo "Account: {{ context:accountId }}, OS: {{ context:osName }}."
```