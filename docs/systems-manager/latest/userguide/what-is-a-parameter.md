# Parameter Store reference

A _parameter_ is any piece of data stored in Parameter Store, such as a block
of text, a list of names, an AMI ID, a merchant ID, or another configuration
value. You can centrally reference this data in your scripts, commands, and SSM
documents.

When you reference a parameter, you specify the parameter name using the following
convention.

{{`ssm:`parameter-name``}}

###### Note

Parameters can't be referenced or nested in the values of other parameters. You
can't include `{{}}` or
`{{ssm:`parameter-name`}}` in a parameter
value.

Parameter Store provides support for three types of parameters: `String`,
`StringList`, and `SecureString`.

With one exception, when you create or update a parameter, you enter the parameter
value as plaintext, and Parameter Store performs no validation on the text you enter. For
`String` parameters, however, you can specify the data type as
`aws:ec2:image`, and Parameter Store validates that the value you enter is the
proper format for an Amazon EC2 AMI; for example:
`ami-12345abcdeEXAMPLE`.

## Parameter type: String

By default, the value of a `String` parameter consists of any block of
text you enter. For example:

- `abc123`
- `Example Corp`
- `<img src="images/bannerImage1.png"/>`

## Parameter type: StringList

The values of `StringList` parameters contain a comma-separated list of
values, as shown in the following examples.

`Monday,Wednesday,Friday`

`CSV,TSV,CLF,ELF,JSON`

## Parameter type: SecureString

Use `SecureString` for configuration values that require encryption, such as service endpoints and account identifiers. For secrets such as database credentials, API keys, or tokens, we recommend AWS Secrets Manager, which provides purpose built security controls including automatic rotation and cross-region replication.

Only the parameter value is encrypted. The parameter name, description, and other
metadata aren't encrypted.

Parameter Store encrypts and decrypts `SecureString` parameter values
using an AWS KMS key. You can use the default AWS managed key for
Parameter Store or a customer managed key. Use a customer managed key when you need to restrict
which principals can decrypt particular parameters. For more information, see
[Encrypting and decrypting parameters using AWS KMS keys](parameter-store-setting-up.md#ps-kms-permissions "parameter-store-setting-up.md#ps-kms-permissions").

###### Important

Note the following important information.

- If you manage credentials that require automatic rotation, cross-account access, or fine-grained audit logging, we recommend using [AWS Secrets Manager](../../../secretsmanager/latest/userguide/intro.md "../../../secretsmanager/latest/userguide/intro.md"). Secrets Manager is purpose-built for managing secrets such as database credentials, API keys, and supported third-party software-vended secrets. For more information, see [What is AWS Secrets Manager?](../../../secretsmanager/latest/userguide/intro.md "../../../secretsmanager/latest/userguide/intro.md") in the _AWS Secrets Manager User Guide_.
- Don't store sensitive data in a `String` or `StringList`
  parameter. For all sensitive data that must remain encrypted, use only the
  `SecureString` parameter type.
- Only the _value_ of a `SecureString` parameter is
  encrypted. Parameter names, descriptions, and other properties aren't
  encrypted.

You can use `SecureString` parameters with other
AWS services. The following Lambda function retrieves an encrypted merchant ID
from the `/myapp/dev/vendor/merchant-id` parameter. The function
uses the value without writing it to the function logs or returning it in the
response.

```
import json
import boto3

ssm = boto3.client("ssm", region_name="us-east-1")

def lambda_handler(event, context):
    response = ssm.get_parameter(
        Name="/myapp/dev/vendor/merchant-id",
        WithDecryption=True
    )

    merchant_id = response["Parameter"]["Value"]

    # Use merchant_id when communicating with the vendor system.
    # Don't write the value to logs or include it in the response.

    return {
        "statusCode": 200,
        "body": json.dumps("Vendor configuration retrieved.")
    }
```

###### AWS KMS encryption and pricing

When you create a `SecureString` parameter, Systems Manager uses
AWS KMS to encrypt the parameter value.

###### Important

Parameter Store only supports [symmetric encryption KMS keys](../../../kms/latest/developerguide/symm-asymm-choose-key-spec.md#symmetric-cmks "../../../kms/latest/developerguide/symm-asymm-choose-key-spec.md#symmetric-cmks"). You can't use an [asymmetric encryption KMS key](../../../kms/latest/developerguide/symmetric-asymmetric.md "../../../kms/latest/developerguide/symmetric-asymmetric.md") to encrypt your parameters. For help
determining whether a KMS key is symmetric or asymmetric, see [Identifying symmetric and asymmetric KMS keys](../../../kms/latest/developerguide/find-symm-asymm.md "../../../kms/latest/developerguide/find-symm-asymm.md") in the
_AWS Key Management Service Developer Guide_

There is no charge from Parameter Store to create a
`SecureString` parameter, but charges for using AWS KMS can apply.
For more information, see
[AWS Key Management Service pricing](https://aws.amazon.com/kms/pricing "https://aws.amazon.com/kms/pricing").

For more information about AWS managed keys and customer managed keys, see
[AWS Key Management Service
Concepts](../../../kms/latest/developerguide/concepts.md "../../../kms/latest/developerguide/concepts.md") in the _AWS Key Management Service Developer Guide_. For more
information about how Parameter Store uses AWS KMS, see
[How
AWS Systems Manager Parameter Store uses AWS KMS](../../../kms/latest/developerguide/services-parameter-store.md "../../../kms/latest/developerguide/services-parameter-store.md").

###### Note

To view the default AWS managed key for Parameter Store, run the
following command.

```
aws kms describe-key \
    --region us-east-1 \
    --key-id alias/aws/ssm
```

## Parameter name constraints

Use the information in this topic to help you specify valid values for
parameter names when you create a parameter.

This information supplements the details in the topic [PutParameter](../APIReference/API_PutParameter.md "../APIReference/API_PutParameter.md") in the
_AWS Systems Manager API Reference_, which also provides information about
the values **AllowedPattern**, **Description**, **KeyId**,
**Overwrite**, **Type**, and **Value**.

The requirements and constraints for parameter names include the
following:

- **Case sensitivity**: Parameter names are
  case sensitive.
- **Spaces**: Parameter names can't include
  spaces.
- **Valid characters**: Parameter names can
  consist of the following symbols and letters only:
  `a-zA-Z0-9_.-`

In addition, the slash character ( / ) is used to delineate
hierarchies in parameter names. For example:
`/Dev/Production/East/Project-ABC/MyParameter`

- **Valid AMI format**: When you choose
  `aws:ec2:image` as the data type for a
  `String` parameter, the ID you enter must validate for
  the AMI ID format `ami-12345abcdeEXAMPLE`.
- **Fully qualified**: When you create or
  reference a parameter in a hierarchy, include a leading forward slash
  character (/) . When you reference a parameter that is part of a
  hierarchy, specify the entire hierarchy path including the initial slash
  (/).

  - Fully qualified parameter names:
    `MyParameter1`,
    `/MyParameter2`,
    `/Dev/Production/East/Project-ABC/MyParameter`
  - Not fully qualified parameter name:
    `MyParameter3/L1`

- **Length**: The maximum length for a
  parameter name that you specify is 1011 characters. This count of 1011
  characters includes the characters in the ARN that precede the name you
  specify, such as the 45 characters in
  `arn:aws:ssm:us-east-2:111122223333:parameter/`.
- **Prefixes**: A parameter name can't be
  prefixed with "`aws`" or "`ssm`"
  (case-insensitive). For example, attempts to create parameters with the
  following names fail with an exception:

  - `awsTestParameter`
  - `SSM-testparameter`
  - `/aws/testparam1`

###### Note

When you specify a parameter in an SSM document, command, or
script, include `ssm` as part of the syntax. For example,
{{ssm:`parameter-name`}} and {{
 ssm:`parameter-name` }}, such as
`{{ssm:MyParameter}}`, and `{{ ssm:MyParameter
 }}.`

- **Uniqueness**: A parameter name must be
  unique within an AWS Region. For example, Systems Manager treats the following
  as separate parameters, if they exist in the same Region:

  - `/Test/TestParam1`
  - `/TestParam1`
    The following examples are also unique:

  - `/Test/TestParam1/Logpath1`
  - `/Test/TestParam1`
    The following examples, however, if in the same Region, aren't
    unique:

  - `/TestParam1`
  - `TestParam1`

- **Hierarchy depth**: If you specify a
  parameter hierarchy, the hierarchy can have a maximum depth of fifteen
  levels. You can define a parameter at any level of the hierarchy. Both
  of the following examples are structurally valid:

  - `/Level-1/L2/L3/L4/L5/L6/L7/L8/L9/L10/L11/L12/L13/L14/parameter-name`
  - `parameter-name`
    Attempting to create the following parameter would fail with a
    `HierarchyLevelLimitExceededException` exception:

  - `/Level-1/L2/L3/L4/L5/L6/L7/L8/L9/L10/L11/L12/L13/L14/L15/L16/parameter-name`

###### Important

If a user has access to a path, then the user can access all levels of
that path. For example, if a user has permission to access path
`/a`, then the user can also access
`/a/b`. Even if a user has explicitly been denied
access in AWS Identity and Access Management (IAM) for parameter `/a/b`, they
can still call the [GetParametersByPath](../APIReference/API_GetParametersByPath.md "../APIReference/API_GetParametersByPath.md") API operation recursively for
`/a` and view `/a/b`.
