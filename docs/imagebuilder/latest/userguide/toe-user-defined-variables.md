# Use variables in your custom component document

Variables provide a way to label data with meaningful names that can be used
throughout an application. You can define custom variables with simple and readable formats
for complex workflows, and reference them in the YAML application component document
for an AWSTOE component.

This section provides information to help you define variables for your AWSTOE component
in the YAML application component document, including syntax, name constraints, and examples.

## Constants

Constants are immutable variables that cannot be modified or overridden once defined. Constants can be defined using values in the
`constants` section of an AWSTOE document.

###### Rules for constant names

- The name must be between 3 and 128 characters in length.
- The name can only contain alphanumeric characters (a-z, A-Z, 0-9), dashes (-), or underscores (\_).
- The name must be unique within the document.
- The name must be specified as a YAML string.

**Syntax**

```
constants:
  - <name>:
      type: <constant type>
      value: <constant value>
```

| Key name | Required | Description                                                                                                                   |
| -------- | -------- | ----------------------------------------------------------------------------------------------------------------------------- |
| `name`   | Yes      | Name of the constant. Must be unique for the document<br>(it must not be the same as any other parameter names or constants). |
| `value`  | Yes      | Value of the constant.                                                                                                        |
| `type`   | Yes      | Type of the constant. Supported type is `string`.                                                                             |

###### Reference constant values in a document

You can reference constants in step or loop inputs inside of your YAML document, as follows:

- Constant references are case-sensitive, and the name must match exactly.
- The name must be enclosed within double curly braces `{{`
  `MyConstant` `}}`.
- Spaces are allowed within the curly braces, and are automatically trimmed.
  For example, all of the following references are valid:

`{{ `MyConstant` }}`,
`{{ `MyConstant`}}`,
`{{`MyConstant` }}`,
`{{`MyConstant`}}`

- The reference in the YAML document must be specified as a string
  (enclosed in single or double quotes).

For example: `- {{ `MyConstant` }}`
is not valid, as it is not identified as a string.

However, the following references are both valid:
`- '{{ `MyConstant` }}'`
and `- "{{ `MyConstant` }}"`.

###### Examples

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

Parameters are mutable variables, with settings that the calling application
can provide at runtime. You can define parameters in the `Parameters`
section of the YAML document.

###### Rules for parameter names

- The name must be between 3 and 128 characters in length.
- The name can only contain alphanumeric characters (a-z, A-Z, 0-9), dashes (-), or underscores (\_).
- The name must be unique within the document.
- The name must be specified as a YAML string.

### Syntax

```
parameters:
  - <name>:
      type: <parameter type>
      default: <parameter value>
      description: <parameter description>
```

| Key name      | Required | Description                                                                                                                        |
| ------------- | -------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| `name`        | Yes      | The name of the parameter. Must be unique for the document<br>(it must not be the same as any other parameter names or constants). |
| `type`        | Yes      | The data type of the parameter. Supported types include: `string`.                                                                 |
| `default`     | No       | The default value for the parameter.                                                                                               |
| `description` | No       | Describes the parameter.                                                                                                           |

### Reference parameter values in a document

You can reference parameters in step or loop inputs inside of your YAML document, as follows:

- Parameter references are case-sensitive, and the name must match exactly.
- The name must be enclosed within double curly braces `{{`
  `MyParameter` `}}`.
- Spaces are allowed within the curly braces, and are automatically trimmed.
  For example, all of the following references are valid:

`{{ `MyParameter` }}`,
`{{ `MyParameter`}}`,
`{{`MyParameter` }}`,
`{{`MyParameter`}}`

- The reference in the YAML document must be specified as a string
  (enclosed in single or double quotes).

For example: `- {{ `MyParameter` }}`
is not valid, as it is not identified as a string.

However, the following references are both valid:
`- '{{ `MyParameter` }}'`
and `- "{{ `MyParameter` }}"`.

###### Examples

The following examples show how to use parameters in your YAML document:

- Refer to a parameter in step inputs:

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

- Refer to a parameter in loop inputs:

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

You can use the `--parameters` option from the AWS CLI with a key-value pair to
set a parameter value at runtime.

- Specify the parameter key-value pair as the name and value, separated by an equals sign
  (<name>=<value>).
- Multiple parameters must be separated by a comma.
- Parameter names that are not found in the YAML component document are ignored.
- The parameter name and value are both required.

###### Important

Component parameters are plain text values, and are logged
in AWS CloudTrail. We recommend that you use AWS Secrets Manager or the AWS Systems Manager Parameter Store to store
your secrets. For more information about Secrets Manager, see [What
is Secrets Manager?](../../../secretsmanager/latest/userguide/intro.md "../../../secretsmanager/latest/userguide/intro.md") in the _AWS Secrets Manager User Guide_. For more information about
AWS Systems Manager Parameter Store, see [AWS Systems Manager
Parameter Store](../../../systems-manager/latest/userguide/systems-manager-parameter-store.md "../../../systems-manager/latest/userguide/systems-manager-parameter-store.md") in the _AWS Systems Manager User Guide_.

#### Syntax

```
--parameters `name1`=`value1`,`name2`=`value2`...
```

| CLI option                      | Required | Description                                                                    |
| ------------------------------- | -------- | ------------------------------------------------------------------------------ |
| --parameters `name`=`value`,... | No       | This option takes list of key-value pairs, with the parameter name as the key. |

###### Examples

The following examples show how to use parameters in your YAML document:

- The parameter key-value pair specified in this `--parameter` option is not
  valid:

```
--parameters ntp-server=
```

- Set one parameter key-value pair with the `--parameter` option in the
  AWS CLI:

```
--parameters ntp-server=ntp-server-windows-qe.us-east1.amazon.com
```

- Set multiple parameter key-value pairs with the `--parameter` option in the
  AWS CLI:

```
--parameters ntp-server=ntp-server.amazon.com,http-url=https://internal-us-east1.amazon.com
```

## Use Systems Manager Parameter Store parameters

You can reference AWS Systems Manager Parameter Store parameters (SSM parameters) in your component
documents by prefixing variables with `aws:ssm`. For example,

`{{ aws:ssm:/my/param }}` resolves to the value of the SSM parameter
`/my/param`.

This feature supports the following SSM parameter types:

- String – Maps to the AWSTOE string type.
- StringList – Maps to the AWSTOE `stringList` type.
- SecureString – Maps to the AWSTOE string type.

For more information about the Parameter Store see [AWS Systems Manager
Parameter Store](../../../systems-manager/latest/userguide/systems-manager-parameter-store.md "../../../systems-manager/latest/userguide/systems-manager-parameter-store.md") in the _AWS Systems Manager User Guide_.

You can also reference AWS Secrets Manager secrets using an SSM parameter `SecureString`.
For example: `{{ aws:ssm:/aws/reference/secretsmanager/test/test-secret }}`. For more information,
see [Referencing AWS Secrets Manager
secrets from Parameter Store parameters](../../../systems-manager/latest/userguide/integration-ps-secretsmanager.md "../../../systems-manager/latest/userguide/integration-ps-secretsmanager.md").

###### Important

Image Builder excludes `SecureString` parameter resolution from its logs. However, you are
also responsible for ensuring that sensitive information is not logged through commands issued
in the component document. For example, if you use the `echo` command with a secure
string, the command writes a plaintext value to the log.

### Required IAM permissions

To use Systems Manager parameters in your components, your instance role must have the
`ssm:GetParameter` permission for the parameter resource ARN. For example:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": "ssm:GetParameter",
 "Resource": "arn:aws:ssm:*:`111122223333`:parameter/ImageBuilder-*"
 }
 ]
}`

```

To access encrypted values, you'll also need the following permissions:

- Add `kms:Decrypt` for `SecureString` parameters or AWS Secrets Manager
  values that are encrypted with a customer managed AWS KMS key.
- Add `secretsmanager:GetSecretValue` if you reference a Secrets Manager secret.

### Reference an SSM parameter in a component document

The following example shows how to reference an Systems Manager Parameter Store parameter of Systems Manager parameters
in a component:

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
            - echo "Log SSM parameter name: `/my/test/param`, value {{ aws:ssm:`/my/test/param` }}."
```

### Dynamic runtime variable resolution for SSM parameters

AWSTOE provides the following built-in function that you can use within variable references to
manipulate or transform values at runtime.

#### resolve function

The `resolve` function resolves a variable reference inside of another variable reference,
allowing for dynamic variable name referencing. This is useful when working with SSM parameters where
part of the parameter path may be variable and passed in as a document parameter.

The `resolve` function only supports dynamic resolution of the name portion of
an SSM parameter.

##### Syntax

The `dynamic_variable` in the following example represents the name of an SSM
parameter, and must be one of the following:

- An SSM parameter reference (for example,
  `aws:ssm:`/my/param``)
- A component document parameter reference (for example,
  `parameter-name`)

```
{{ aws:ssm:resolve(`dynamic_variable`) }}
```

##### Example: Resolve an SSM parameter at runtime

The following example shows how to use the `resolve` function
in a YAML component document:

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
