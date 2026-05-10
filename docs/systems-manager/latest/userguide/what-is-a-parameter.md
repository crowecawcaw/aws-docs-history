# Understanding parameter types

A _parameter_ is any piece of data stored in Parameter Store, such as a block
of text, a list of names, an AMI ID, a license key, and so on. You can
centrally and securely reference this data in your scripts, commands, and SSM
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

The value of a `SecureString` parameter is any sensitive data that
needs to be stored and referenced in a secure manner. If you have data that you
don't want users to alter or reference in plaintext, such as lightweight secrets or license
keys, create those parameters using the `SecureString` data
type.

We recommend using `SecureString` parameters for the following
scenarios:

- You want to use data/parameters across AWS services without exposing the
  values as plaintext in commands, functions, agent logs, or CloudTrail logs.
- You want to control who has access to sensitive data.
- You want to be able to audit when sensitive data is accessed
  (CloudTrail).
- You want to encrypt your sensitive data, and you want to bring your own
  encryption keys to manage access.

You can use the `SecureString` parameter type for textual data that you
want to encrypt, such as lightweight secrets that don't require rotation, confidential configuration
data, or any other types of data that you want to protect. `SecureString`
data is encrypted and decrypted using an AWS KMS key. You can use either a default KMS
key provided by AWS or create and use your own AWS KMS key. (Use your own
AWS KMS key if you want to restrict user access to `SecureString`
parameters. For more information, see [IAM permissions for using AWS default keys and customer managed keys](sysman-paramstore-access.md#ps-kms-permissions "sysman-paramstore-access.md#ps-kms-permissions").)

###### Important

Note the following important information.

- If you manage credentials that require automatic rotation, cross-account access, or fine-grained audit logging, we recommend using [AWS Secrets Manager](../../../secretsmanager/latest/userguide/intro.md "../../../secretsmanager/latest/userguide/intro.md"). Secrets Manager is purpose-built for managing secrets such as database credentials, API keys, and supported third-party software-vended secrets. For more information, see [What is AWS Secrets Manager?](../../../secretsmanager/latest/userguide/intro.md "../../../secretsmanager/latest/userguide/intro.md") in the _AWS Secrets Manager User Guide_.
- Don't store sensitive data in a `String` or `StringList`
  parameter. For all sensitive data that must remain encrypted, use only the
  `SecureString` parameter type.
- Only the _value_ of a `SecureString` parameter is
  encrypted. Parameter names, descriptions, and other properties aren't
  encrypted.

You can also use `SecureString` parameters with other AWS services.
In the following example, the Lambda function retrieves a `SecureString`
parameter by using the [GetParameters](../APIReference/API_GetParameters.md "../APIReference/API_GetParameters.md") API.

```
import json
import boto3
ssm = boto3.client('ssm', 'us-east-2')
def get_parameters():
    response = ssm.get_parameters(
        Names=['LambdaSecureString'],WithDecryption=True
    )
    for parameter in response['Parameters']:
        return parameter['Value']

def lambda_handler(event, context):
    value = get_parameters()
    print("value1 = " + value)
    return value  # Echo back the first key value

```

###### AWS KMS encryption and pricing

If you choose the `SecureString` parameter type when
you create your parameter, Systems Manager uses AWS KMS to encrypt the parameter
value.

###### Important

Parameter Store only supports [symmetric encryption KMS keys](../../../kms/latest/developerguide/symm-asymm-choose-key-spec.md#symmetric-cmks "../../../kms/latest/developerguide/symm-asymm-choose-key-spec.md#symmetric-cmks"). You can't use an [asymmetric encryption KMS key](../../../kms/latest/developerguide/symmetric-asymmetric.md "../../../kms/latest/developerguide/symmetric-asymmetric.md") to encrypt your parameters. For help
determining whether a KMS key is symmetric or asymmetric, see [Identifying symmetric and asymmetric KMS keys](../../../kms/latest/developerguide/find-symm-asymm.md "../../../kms/latest/developerguide/find-symm-asymm.md") in the
_AWS Key Management Service Developer Guide_

There is no charge from Parameter Store to create a `SecureString` parameter, but charges for use of AWS KMS encryption do
apply. For information, see [AWS Key Management Service
pricing](https://aws.amazon.com/kms/pricing "https://aws.amazon.com/kms/pricing").

For more information about AWS managed keys and customer managed keys, see [AWS Key Management Service
Concepts](../../../kms/latest/developerguide/concepts.md "../../../kms/latest/developerguide/concepts.md") in the _AWS Key Management Service Developer Guide_. For more
information about Parameter Store and AWS KMS encryption, see [How
AWS Systems Manager Parameter Store Uses AWS KMS](../../../kms/latest/developerguide/services-parameter-store.md "../../../kms/latest/developerguide/services-parameter-store.md").

###### Note

To view an AWS managed key, use the AWS KMS `DescribeKey`
operation. This AWS Command Line Interface (AWS CLI) example uses `DescribeKey` to view
an AWS managed key.

```
aws kms describe-key --key-id alias/aws/ssm
```
