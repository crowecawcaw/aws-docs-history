AWS Systems Manager Change Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see
[AWS Systems Manager Change Manager availability change](change-manager-availability-change.md "change-manager-availability-change.md").

# AWS Systems Manager Parameter Store

Parameter Store, a tool in AWS Systems Manager, provides secure, hierarchical storage for configuration
data management and secrets management. You can store data such as passwords, database
strings, Amazon Machine Image (AMI) IDs, and license codes as parameter values. You can store values
as plain text or encrypted data. You can reference Systems Manager parameters in your scripts,
commands, SSM documents, and configuration and automation workflows by using the unique
name that you specified when you created the parameter. To get started with Parameter Store, open
the [Systems Manager console](https://console.aws.amazon.com//systems-manager/parameters "https://console.aws.amazon.com//systems-manager/parameters"). In the
navigation pane, choose **Parameter Store**.

Parameter Store is also integrated with Secrets Manager. You can retrieve Secrets Manager secrets when using other
AWS services that already support references to Parameter Store parameters. For more information,
see [Referencing AWS Secrets Manager secrets from
Parameter Store parameters](integration-ps-secretsmanager.md "integration-ps-secretsmanager.md").

###### Note

To implement password rotation lifecycles, use AWS Secrets Manager. You can rotate, manage, and
retrieve database credentials, API keys, and other secrets throughout their lifecycle
using Secrets Manager. For more information, see [What is AWS Secrets Manager?](../../../secretsmanager/latest/userguide/intro.md "../../../secretsmanager/latest/userguide/intro.md") in the
_AWS Secrets Manager User Guide_.

## How can Parameter Store benefit my

organization?

Parameter Store offers these benefits:

- Use a secure, scalable, hosted secrets management service with no servers to
  manage.
- Improve your security posture by separating your data from your code.
- Store configuration data and encrypted strings in hierarchies and track
  versions.
- Control and audit access at granular levels.
- Store parameters reliably because Parameter Store is hosted in multiple Availability
  Zones in an AWS Region.

## Who should use Parameter Store?

- Any AWS customer who wants to have a centralized way to manage configuration
  data.
- Software developers who want to store different logins and reference
  streams.
- Administrators who want to receive notifications when their secrets and
  passwords are or aren't changed.

## What are the features of Parameter Store?

- **Change notification**

You can configure change notifications and invoke automated actions for both
parameters and parameter policies. For more information, see [Setting up notifications or triggering
actions based on Parameter Store events](sysman-paramstore-cwe.md "sysman-paramstore-cwe.md").

- **Organize
  parameters**

You can tag your parameters individually to help you identify one or more
parameters based on the tags you've assigned to them. For example, you can tag
parameters for specific environments or departments.

- **Label versions**

You can associate an alias for versions of your parameter by creating labels.
Labels can help you remember the purpose of a parameter version when there are
multiple versions.

- **Data validation**

You can create parameters that point to an Amazon Elastic Compute Cloud (Amazon EC2) instance and
Parameter Store validates these parameters to make sure that it references expected
resource type, that the resource exists, and that the customer has permission to
use the resource. For example, you can create a parameter with Amazon Machine Image (AMI)
ID as a value with `aws:ec2:image` data type, and Parameter Store performs
an asynchronous validation operation to make sure that the parameter value meets
the formatting requirements for an AMI ID, and that the specified AMI is
available in your AWS account.

- **Reference secrets**

Parameter Store is integrated with AWS Secrets Manager so that you can retrieve Secrets Manager secrets
when using other AWS services that already support references to Parameter Store
parameters.

- **Share parameters with other accounts**

You can optionally centralize configuration data in a single AWS account and
share parameters with other accounts that need to access them.

- **Accessible from other AWS services**

You can use Parameter Store parameters with other Systems Manager tools and AWS services to
retrieve secrets and configuration data from a central store. Parameters work
with Systems Manager tools such as Run Command, Automation, and State Manager, tools in AWS Systems Manager.
You can also reference parameters in a number of other AWS services, including
the following:

    + Amazon Elastic Compute Cloud (Amazon EC2)
    + Amazon Elastic Container Service (Amazon ECS)
    + AWS Secrets Manager
    + AWS Lambda
    + AWS CloudFormation
    + AWS CodeBuild
    + AWS CodePipeline
    + AWS CodeDeploy

- **Integrate with other AWS services**

Configure integration with the following AWS services for encryption,
notification, monitoring, and auditing:

    + AWS Key Management Service (AWS KMS)
    + Amazon Simple Notification Service (Amazon SNS)
    + Amazon CloudWatch: For more information, see [Configuring EventBridge rules for parameters
     and parameter policies](sysman-paramstore-cwe.md#cwe-parameter-changes "sysman-paramstore-cwe.md#cwe-parameter-changes").
    + Amazon EventBridge: For more information, see [Monitoring Systems Manager status changes using
     Amazon SNS notifications](monitoring-sns-notifications.md "monitoring-sns-notifications.md") and [Reference: Amazon EventBridge event patterns and types
     for Systems Manager](reference-eventbridge-events.md "reference-eventbridge-events.md").
    + AWS CloudTrail: For more information, see [Logging AWS Systems Manager API calls with AWS CloudTrail](monitoring-cloudtrail-logs.md "monitoring-cloudtrail-logs.md").

## What is a parameter?

A Parameter Store parameter is any piece of data that is saved in Parameter Store, such as a block
of text, a list of names, a password, an AMI ID, a license key, and so on. You can
centrally and securely reference this data in your scripts, commands, and SSM
documents.

When you reference a parameter, you specify the parameter name by using the following
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

### Parameter type: String

By default, the value of a `String` parameter consists of any block of
text you enter. For example:

- `abc123`
- `Example Corp`
- `<img src="images/bannerImage1.png"/>`

### Parameter type: StringList

The values of `StringList` parameters contain a comma-separated list of
values, as shown in the following examples.

`Monday,Wednesday,Friday`

`CSV,TSV,CLF,ELF,JSON`

### Parameter type: SecureString

The value of a `SecureString` parameter is any sensitive data that
needs to be stored and referenced in a secure manner. If you have data that you
don't want users to alter or reference in plaintext, such as passwords or license
keys, create those parameters using the `SecureString` data
type.

###### Important

Don't store sensitive data in a `String` or `StringList`
parameter. For all sensitive data that must remain encrypted, use only the
`SecureString` parameter type.

For more information, see [Creating a SecureString
parameter using the AWS CLI](param-create-cli.md#param-create-cli-securestring "param-create-cli.md#param-create-cli-securestring").

We recommend using `SecureString` parameters for the following
scenarios:

- You want to use data/parameters across AWS services without exposing the
  values as plaintext in commands, functions, agent logs, or CloudTrail logs.
- You want to control who has access to sensitive data.
- You want to be able to audit when sensitive data is accessed
  (CloudTrail).
- You want to encrypt your sensitive data, and you want to bring your own
  encryption keys to manage access.

###### Important

Only the _value_ of a `SecureString` parameter is
encrypted. Parameter names, descriptions, and other properties aren't
encrypted.

You can use the `SecureString` parameter type for textual data that you
want to encrypt, such as passwords, application secrets, confidential configuration
data, or any other types of data that you want to protect. `SecureString`
data is encrypted and decrypted using an AWS KMS key. You can use either a default KMS
key provided by AWS or create and use your own AWS KMS key. (Use your own
AWS KMS key if you want to restrict user access to `SecureString`
parameters. For more information, see [IAM permissions for using AWS default
keys and customer managed keys](sysman-paramstore-access.md#ps-kms-permissions "sysman-paramstore-access.md#ps-kms-permissions").)

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

**More info**

- [Creating a SecureString
  parameter in Parameter Store and joining a node to a Domain (PowerShell)](sysman-param-securestring-walkthrough.md "sysman-param-securestring-walkthrough.md")
- [Use Parameter Store to Securely Access Secrets and Config Data in
  CodeDeploy](https://aws.amazon.com/blogs/mt/use-parameter-store-to-securely-access-secrets-and-config-data-in-aws-codedeploy/ "https://aws.amazon.com/blogs/mt/use-parameter-store-to-securely-access-secrets-and-config-data-in-aws-codedeploy/")
- [Interesting Articles on Amazon EC2 Systems Manager Parameter Store](https://aws.amazon.com/blogs/mt/interesting-articles-on-ec2-systems-manager-parameter-store/ "https://aws.amazon.com/blogs/mt/interesting-articles-on-ec2-systems-manager-parameter-store/")

## Parameter size limits

Parameter Store has different size limits for parameter values depending on the parameter
tier you use:

- **Standard parameters**: Maximum value size of 4
  KB
- **Advanced parameters**: Maximum value size of 8
  KB

If you need to store parameter values larger than 4 KB, you must use the advanced
parameter tier. Advanced parameters provide additional capabilities but incur charges on
your AWS account. For more information about parameter tiers and their features, see
[Managing parameter
tiers](parameter-store-advanced-parameters.md "parameter-store-advanced-parameters.md").

For a complete list of Parameter Store quotas and limits, see [AWS Systems Manager endpoints and
quotas](../../../general/latest/gr/ssm.md#parameter-store "../../../general/latest/gr/ssm.md#parameter-store") in the _AWS General Reference_.
