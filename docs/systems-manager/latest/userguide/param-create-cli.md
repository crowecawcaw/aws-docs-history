# Creating a Parameter Store parameter using the

AWS CLI

You can use the AWS Command Line Interface (AWS CLI) to create `String`,
`StringList`, and `SecureString`
parameter types. After deleting a parameter, wait for at least 30 seconds to
create a parameter with the same name.

Parameters can't be referenced or nested in the values of other parameters. You
can't include `{{}}` or
`{{ssm:`parameter-name`}}` in a parameter
value.

###### Note

Parameters are only available in the AWS Region where they were
created.

###### Topics

- [Creating a String parameter using the AWS CLI](#param-create-cli-string "#param-create-cli-string")
- [Creating a StringList
  parameter using the AWS CLI](#param-create-cli-stringlist "#param-create-cli-stringlist")
- [Creating a SecureString
  parameter using the AWS CLI](#param-create-cli-securestring "#param-create-cli-securestring")
- [Creating a multi-line parameter
  using the AWS CLI](#param-create-cli-multiline "#param-create-cli-multiline")

## Creating a `String` parameter using the AWS CLI

1. Install and configure the AWS Command Line Interface (AWS CLI), if you haven't already.

For information, see [Installing or updating the
latest version of the AWS CLI](../../../cli/latest/userguide/getting-started-install.md "../../../cli/latest/userguide/getting-started-install.md"). 2. Run the following command to create a `String`-type
parameter. Replace each `example resource
 placeholder` with your own information.

Linux & macOS

```
aws ssm put-parameter \
    --name "`parameter-name`" \
    --value "`parameter-value`" \
    --type String \
    --tags "Key=`tag-key`,Value=`tag-value`"
```

Windows

```
aws ssm put-parameter ^
    --name "`parameter-name`" ^
    --value "`parameter-value`" ^
    --type String ^
    --tags "Key=`tag-key`,Value=`tag-value`"
```

-or-

Run the following command to create a parameter that contains an
Amazon Machine Image (AMI) ID as the parameter value.

Linux & macOS

```
aws ssm put-parameter \
    --name "`parameter-name`" \
    --value "`an-AMI-id`" \
    --type String \
    --data-type "aws:ec2:image" \
    --tags "Key=`tag-key`,Value=`tag-value`"
```

Windows

```
aws ssm put-parameter ^
    --name "`parameter-name`" ^
    --value "`an-AMI-id`" ^
    --type String ^
    --data-type "aws:ec2:image" ^
    --tags "Key=`tag-key`,Value=`tag-value`"
```

The `--name` option supports hierarchies. For
information about hierarchies, see [Working with parameter hierarchies
in Parameter Store](sysman-paramstore-hierarchies.md "sysman-paramstore-hierarchies.md").

The `--data-type` option must be specified only if you
are creating a parameter that contains an AMI ID. It validates
that the parameter value you enter is a properly formatted Amazon Elastic Compute Cloud
(Amazon EC2) AMI ID. For all other parameters, the default data type is
`text` and it's optional to specify a value. For more
information, see [Using native parameter support in
Parameter Store for Amazon Machine Image IDs](parameter-store-ec2-aliases.md "parameter-store-ec2-aliases.md").

###### Important

If successful, the command returns the version number of the
parameter. **Exception**: If you
have specified `aws:ec2:image` as the data type, a
new version number in the response doesn't mean that the
parameter value has been validated yet. For more information,
see [Using native parameter support in
Parameter Store for Amazon Machine Image IDs](parameter-store-ec2-aliases.md "parameter-store-ec2-aliases.md").

The following example adds two key-value pair tags to a parameter.

Linux & macOS

```
aws ssm put-parameter \
    --name `parameter-name` \
    --value "`parameter-value`" \
    --type "String" \
    --tags '[{"Key":"Region","Value":"East"},{"Key":"Environment", "Value":"Production"}]'
```

Windows

```
aws ssm put-parameter ^
    --name `parameter-name` ^
    --value "`parameter-value`" ^
    --type "String" ^
    --tags [{\"Key\":\"Region1\",\"Value\":\"East1\"},{\"Key\":\"Environment1\",\"Value\":\"Production1\"}]
```

The following example uses a parameter hierarchy in the name to
create a plaintext `String` parameter. It returns the
version number of the parameter. For more information about
parameter hierarchies, see [Working with parameter hierarchies
in Parameter Store](sysman-paramstore-hierarchies.md "sysman-paramstore-hierarchies.md").

Linux & macOS
**Parameter not in a
hierarchy**

```
aws ssm put-parameter \
    --name "golden-ami" \
    --type "String" \
    --value "ami-12345abcdeEXAMPLE"
```

**Parameter in a
hierarchy**

```
aws ssm put-parameter \
    --name "/amis/linux/golden-ami" \
    --type "String" \
    --value "ami-12345abcdeEXAMPLE"
```

Windows
**Parameter not in a
hierarchy**

```
aws ssm put-parameter ^
    --name "golden-ami" ^
    --type "String" ^
    --value "ami-12345abcdeEXAMPLE"
```

**Parameter in a
hierarchy**

```
aws ssm put-parameter ^
    --name "/amis/windows/golden-ami" ^
    --type "String" ^
    --value "ami-12345abcdeEXAMPLE"
```

3. Run the following command to view the latest parameter value and
   verify the details of your new parameter.

```
aws ssm get-parameters --names "/Test/IAD/helloWorld"
```

The system returns information like the following.

```
{
    "InvalidParameters": [],
    "Parameters": [
        {
            "Name": "/Test/IAD/helloWorld",
            "Type": "String",
            "Value": "My updated parameter value",
            "Version": 2,
            "LastModifiedDate": "2020-02-25T15:55:33.677000-08:00",
            "ARN": "arn:aws:ssm:us-east-2:123456789012:parameter/Test/IAD/helloWorld"
        }
    ]
}
```

Run the following command to change the parameter value. It returns the
version number of the parameter.

```
aws ssm put-parameter --name "/Test/IAD/helloWorld" --value "My updated 1st parameter" --type String --overwrite
```

Run the following command to view the parameter value history.

```
aws ssm get-parameter-history --name "/Test/IAD/helloWorld"
```

Run the following command to use this parameter in a command.

```
aws ssm send-command --document-name "AWS-RunShellScript" --parameters '{"commands":["echo {{ssm:/Test/IAD/helloWorld}}"]}' --targets "Key=instanceids,Values=`instance-ids`"
```

Run the following command if you only want to retrieve the parameter
Value.

```
aws ssm get-parameter --name testDataTypeParameter --query "Parameter.Value"
```

Run the following command if you only want to retrieve the parameter Value
using `get-parameters`.

```
aws ssm get-parameters --names "testDataTypeParameter" --query "Parameters[*].Value"
```

Run the following command to view the parameter metadata.

```
aws ssm describe-parameters --filters "Key=Name,Values=/Test/IAD/helloWorld"
```

###### Note

_Name_ must be capitalized.

The system returns information like the following.

```
{
    "Parameters": [
        {
            "Name": "helloworld",
            "Type": "String",
            "LastModifiedUser": "arn:aws:iam::123456789012:user/JohnDoe",
            "LastModifiedDate": 1494529763.156,
            "Version": 1,
            "Tier": "Standard",
            "Policies": []
        }
    ]
}
```

## Creating a StringList

parameter using the AWS CLI

1. Install and configure the AWS Command Line Interface (AWS CLI), if you haven't already.

For information, see [Installing or updating the
latest version of the AWS CLI](../../../cli/latest/userguide/getting-started-install.md "../../../cli/latest/userguide/getting-started-install.md"). 2. Run the following command to create a parameter. Replace each
`example resource placeholder` with
your own information.

Linux & macOS

```
aws ssm put-parameter \
    --name "`parameter-name`" \
    --value "`a-comma-separated-list-of-values`" \
    --type StringList \
    --tags "Key=`tag-key`,Value=`tag-value`"
```

Windows

```
aws ssm put-parameter ^
    --name "`parameter-name`" ^
    --value "`a-comma-separated-list-of-values`" ^
    --type StringList ^
    --tags "Key=`tag-key`,Value=`tag-value`"
```

###### Note

If successful, the command returns the version number of the
parameter.

This example adds two key-value pair tags to a parameter.
(Depending on the operating system type on your local machine, run
one of the following commands. The version to run from a local
Windows machine includes the escape characters ("\") that you need
to run the command from your command line tool.)

Here is a `StringList` example that uses a parameter
hierarchy.

Linux & macOS

```
aws ssm put-parameter \
    --name /IAD/ERP/Oracle/addUsers \
    --value "Milana,Mariana,Mark,Miguel" \
    --type StringList
```

Windows

```
aws ssm put-parameter ^
    --name /IAD/ERP/Oracle/addUsers ^
    --value "Milana,Mariana,Mark,Miguel" ^
    --type StringList
```

###### Note

Items in a `StringList` must be
separated by a comma (,). You can't use other punctuation or
special characters to escape items in the list. If you have a
parameter value that requires a comma, then use the `String` type. 3. Run the `get-parameters` command to verify the details
of the parameter. For example:

```
aws ssm get-parameters --name "/IAD/ERP/Oracle/addUsers"
```

## Creating a SecureString

parameter using the AWS CLI

Use the following procedure to create a `SecureString`
parameter. Replace each `example resource
 placeholder` with your own information.

###### Important

Only the _value_ of a `SecureString` parameter is
encrypted. Parameter names, descriptions, and other properties aren't
encrypted.

###### Important

Parameter Store only supports [symmetric encryption KMS keys](../../../kms/latest/developerguide/symm-asymm-choose-key-spec.md#symmetric-cmks "../../../kms/latest/developerguide/symm-asymm-choose-key-spec.md#symmetric-cmks"). You can't use an [asymmetric encryption KMS key](../../../kms/latest/developerguide/symmetric-asymmetric.md "../../../kms/latest/developerguide/symmetric-asymmetric.md") to encrypt your parameters. For help
determining whether a KMS key is symmetric or asymmetric, see [Identifying symmetric and asymmetric KMS keys](../../../kms/latest/developerguide/find-symm-asymm.md "../../../kms/latest/developerguide/find-symm-asymm.md") in the
_AWS Key Management Service Developer Guide_

1. Install and configure the AWS Command Line Interface (AWS CLI), if you haven't already.

For information, see [Installing or updating the
latest version of the AWS CLI](../../../cli/latest/userguide/getting-started-install.md "../../../cli/latest/userguide/getting-started-install.md"). 2. Run **one** of the following commands
to create a parameter that uses the `SecureString` data
type.

Linux & macOS
**Create a
`SecureString` parameter using the
default AWS managed key**

```
aws ssm put-parameter \
    --name "`parameter-name`" \
    --value "`parameter-value`" \
    --type "SecureString"
```

**Create a
`SecureString` parameter that uses a
customer managed key**

```
aws ssm put-parameter \
    --name "`parameter-name`" \
    --value "`a-parameter-value, for example P@ssW%rd#1`" \
    --type "SecureString"
    --tags "Key=`tag-key`,Value=`tag-value`"
```

**Create a
`SecureString` parameter that uses a
custom AWS KMS key**

```
aws ssm put-parameter \
    --name "`parameter-name`" \
    --value "`a-parameter-value, for example P@ssW%rd#1`" \
    --type "SecureString" \
    --key-id "`your-account-ID/the-custom-AWS KMS-key`" \
    --tags "Key=`tag-key`,Value=`tag-value`"
```

Windows
**Create a
`SecureString` parameter using the
default AWS managed key**

```
aws ssm put-parameter ^
    --name "`parameter-name`" ^
    --value "`parameter-value`" ^
    --type "SecureString"
```

**Create a
`SecureString` parameter that uses a
customer managed key**

```
aws ssm put-parameter ^
    --name "`parameter-name`" ^
    --value "`a-parameter-value, for example P@ssW%rd#1`" ^
    --type "SecureString" ^
    --tags "Key=`tag-key`,Value=`tag-value`"
```

**Create a
`SecureString` parameter that uses a
custom AWS KMS key**

```
aws ssm put-parameter ^
    --name "`parameter-name`" ^
    --value "`a-parameter-value, for example P@ssW%rd#1`" ^
    --type "SecureString" ^
    --key-id " ^
    --tags "Key=`tag-key`,Value=`tag-value`"`account-ID/the-custom-AWS KMS-key`"
```

If you create a `SecureString` parameter by using the
AWS managed key key in your account and Region, then you
_don't_ have to provide a value for the
`--key-id` parameter.

###### Note

To use the AWS KMS key assigned to your AWS account and
AWS Region, remove the `key-id`
parameter from the command. For more information about
AWS KMS keys, see [AWS Key Management Service
Concepts](../../../kms/latest/developerguide/concepts.md#aws-managed-cmk "../../../kms/latest/developerguide/concepts.md#aws-managed-cmk") in the
_AWS Key Management Service Developer Guide_.

To use a customer managed key instead of the AWS managed key assigned to
your account, specify the key by using the `--key-id`
parameter. The parameter supports the following KMS parameter
formats.

    * Key Amazon Resource Name (ARN) example:



    `arn:aws:kms:us-east-2:123456789012:key/`key-id``
    * Alias ARN example:


    `arn:aws:kms:us-east-2:123456789012:alias/`alias-name``
    * Key ID example:


    `12345678-1234-1234-1234-123456789012`
    * Alias Name example:


    `alias/MyAliasName`

You can create a customer managed key by using the AWS Management Console or the AWS KMS
API. The following AWS CLI commands create a customer managed key in
the current AWS Region of your AWS account.

```
aws kms create-key
```

Use a command in the following format to create a
`SecureString` parameter using the key you just
created.

The following example uses an obfuscated name
(`3l3vat3131`) for a password parameter and an
AWS KMS key.

Linux & macOS

```
aws ssm put-parameter \
    --name /Finance/Payroll/3l3vat3131 \
    --value "P@sSwW)rd" \
    --type SecureString \
    --key-id arn:aws:kms:us-east-2:123456789012:key/1a2b3c4d-1a2b-1a2b-1a2b-1a2b3c4d5e
```

Windows

```
aws ssm put-parameter ^
    --name /Finance/Payroll/3l3vat3131 ^
    --value "P@sSwW)rd" ^
    --type SecureString ^
    --key-id arn:aws:kms:us-east-2:123456789012:key/1a2b3c4d-1a2b-1a2b-1a2b-1a2b3c4d5e
```

3. Run the following command to verify the details of the
   parameter.

If you don't specify the `with-decryption` parameter, or if you specify the `no-with-decryption` parameter, the command
returns an encrypted GUID.

Linux & macOS

```
aws ssm get-parameters \
    --name "`the-parameter-name-you-specified`" \
    --with-decryption
```

Windows

```
aws ssm get-parameters ^
    --name "`the-parameter-name-you-specified`" ^
    --with-decryption
```

4. Run the following command to view the parameter metadata.

Linux & macOS

```
aws ssm describe-parameters \
    --filters "Key=Name,Values=`the-name-that-you-specified`"
```

Windows

```
aws ssm describe-parameters ^
    --filters "Key=Name,Values=`the-name-that-you-specified`"
```

5. Run the following command to change the parameter value if you're
   **not** using a customer managed
   AWS KMS key.

Linux & macOS

```
aws ssm put-parameter \
    --name "`the-name-that-you-specified`" \
    --value "`a-new-parameter-value`" \
    --type "SecureString" \
    --overwrite
```

Windows

```
aws ssm put-parameter ^
    --name "`the-name-that-you-specified`" ^
    --value "`a-new-parameter-value`" ^
    --type "SecureString" ^
    --overwrite
```

-or-

Run one of the following commands to change the parameter value if
you **are** using a customer managed
AWS KMS key.

Linux & macOS

```
aws ssm put-parameter \
    --name "`the-name-that-you-specified`" \
    --value "`a-new-parameter-value`" \
    --type "SecureString" \
    --key-id "`the-KMSkey-ID`" \
    --overwrite
```

```
aws ssm put-parameter \
    --name "`the-name-that-you-specified`" \
    --value "`a-new-parameter-value`" \
    --type "SecureString" \
    --key-id "`account-alias/the-KMSkey-ID`" \
    --overwrite
```

Windows

```
aws ssm put-parameter ^
    --name "`the-name-that-you-specified`" ^
    --value "`a-new-parameter-value`" ^
    --type "SecureString" ^
    --key-id "`the-KMSkey-ID`" ^
    --overwrite
```

```
aws ssm put-parameter ^
    --name "`the-name-that-you-specified`" ^
    --value "`a-new-parameter-value`" ^
    --type "SecureString" ^
    --key-id "`account-alias/the-KMSkey-ID`" ^
    --overwrite
```

6. Run the following command to view the latest parameter
   value.

Linux & macOS

```
aws ssm get-parameters \
    --name "`the-name-that-you-specified`" \
    --with-decryption
```

Windows

```
aws ssm get-parameters ^
    --name "`the-name-that-you-specified`" ^
    --with-decryption
```

7. Run the following command to view the parameter value
   history.

Linux & macOS

```
aws ssm get-parameter-history \
    --name "`the-name-that-you-specified`"
```

Windows

```
aws ssm get-parameter-history ^
    --name "`the-name-that-you-specified`"
```

###### Note

You can manually create a parameter with an encrypted value. In this
case, because the value is already encrypted, you don’t have to choose
the `SecureString` parameter type. If you do
choose `SecureString`, your parameter is doubly
encrypted.

By default, all `SecureString` values are displayed as
cipher-text. To decrypt a `SecureString` value, a user must have
permission to call the AWS KMS [Decrypt](../../../kms/latest/APIReference/API_Decrypt.md "../../../kms/latest/APIReference/API_Decrypt.md") API operation. For information about configuring AWS KMS
access control, see [Authentication and Access Control for AWS KMS](../../../kms/latest/developerguide/control-access.md "../../../kms/latest/developerguide/control-access.md") in the
_AWS Key Management Service Developer Guide_.

###### Important

If you change the KMS key alias for the KMS key used to encrypt a
parameter, then you must also update the key alias the parameter uses to
reference AWS KMS. This only applies to the KMS key alias; the key ID
that an alias attaches to stays the same unless you delete the whole
key.

## Creating a multi-line parameter

using the AWS CLI

You can use the AWS CLI to create a parameter with line breaks. Use line
breaks to break up the text in longer parameter values for better legibility
or, for example, update multi-paragraph parameter content for a web page.
You can include the content in a JSON file and use the
`--cli-input-json` option, using line break characters like
`\n`, as shown in the following example.

1. Install and configure the AWS Command Line Interface (AWS CLI), if you haven't already.

For information, see [Installing or updating the
latest version of the AWS CLI](../../../cli/latest/userguide/getting-started-install.md "../../../cli/latest/userguide/getting-started-install.md"). 2. Run the following command to create a multi-line parameter.

Linux & macOS

```
aws ssm put-parameter \
    --name "MultiLineParameter" \
    --type String \
    --cli-input-json file://MultiLineParameter.json
```

Windows

```
aws ssm put-parameter ^
    --name "MultiLineParameter" ^
    --type String ^
    --cli-input-json file://MultiLineParameter.json
```

The following example shows the contents of the file
`MultiLineParameter.json`.

```
{
    "Value": "<para>Paragraph One</para>\n<para>Paragraph Two</para>\n<para>Paragraph Three</para>"
}
```

The saved parameter value is stored as follows.

```
<para>Paragraph One</para>
<para>Paragraph Two</para>
<para>Paragraph Three</para>
```
