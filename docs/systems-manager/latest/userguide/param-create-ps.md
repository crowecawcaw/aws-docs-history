• AWS Systems Manager Change Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see
[AWS Systems Manager Change Manager availability change](change-manager-availability-change.md "change-manager-availability-change.md").

 

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see
[Amazon CloudWatch Dashboard documentation](../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md "../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md").

# Creating a Parameter Store parameter using

Tools for Windows PowerShell

You can use AWS Tools for Windows PowerShell to create `String`, `StringList`, and `SecureString`
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

- [Creating a String parameter
  (Tools for Windows PowerShell)](#param-create-ps-string "#param-create-ps-string")
- [Creating a StringList parameter
  (Tools for Windows PowerShell)](#param-create-ps-stringlist "#param-create-ps-stringlist")
- [Creating a SecureString
  parameter (Tools for Windows PowerShell)](#param-create-ps-securestring "#param-create-ps-securestring")

## Creating a String parameter

(Tools for Windows PowerShell)

1. Install and configure the AWS Tools for PowerShell (Tools for Windows PowerShell), if you haven't already.

For information, see [Installing the
AWS Tools for PowerShell](../../../powershell/latest/userguide/pstools-getting-set-up.md "../../../powershell/latest/userguide/pstools-getting-set-up.md"). 2. Run the following command to create a parameter that contains a
plain text value. Replace each `example resource
 placeholder` with your own information.

```
Write-SSMParameter `
    -Name "`parameter-name`" `
    -Value "`parameter-value`" `
    -Type "String"
```

-or-

Run the following command to create a parameter that contains an
Amazon Machine Image (AMI) ID as the parameter value.

###### Note

To create a parameter with a tag, create the service.model.tag
before hand as a variable. Here is an example.

```
$tag = New-Object Amazon.SimpleSystemsManagement.Model.Tag
$tag.Key = "tag-key"
$tag.Value = "tag-value"
```

```
Write-SSMParameter `
    -Name "`parameter-name`" `
    -Value "`an-AMI-id`" `
    -Type "String" `
    -DataType "aws:ec2:image" `
    -Tags $tag
```

The `-DataType` option must be specified only if you
are creating a parameter that contains an AMI ID. For all other
parameters, the default data type is `text`. For more
information, see [Using native parameter support in
Parameter Store for Amazon Machine Image IDs](parameter-store-ec2-aliases.md "parameter-store-ec2-aliases.md").

Here is an example that uses a parameter hierarchy.

```
Write-SSMParameter `
    -Name "/IAD/Web/SQL/IPaddress" `
    -Value "99.99.99.999" `
    -Type "String" `
    -Tags $tag
```

3. Run the following command to verify the details of the
   parameter.

```
(Get-SSMParameterValue -Name "`the-parameter-name-you-specified`").Parameters
```

## Creating a StringList parameter

(Tools for Windows PowerShell)

1. Install and configure the AWS Tools for PowerShell (Tools for Windows PowerShell), if you haven't already.

For information, see [Installing the
AWS Tools for PowerShell](../../../powershell/latest/userguide/pstools-getting-set-up.md "../../../powershell/latest/userguide/pstools-getting-set-up.md"). 2. Run the following command to create a StringList parameter.
Replace each `example resource placeholder`
with your own information.

###### Note

To create a parameter with a tag, create the service.model.tag
before hand as a variable. Here is an example.

```
$tag = New-Object Amazon.SimpleSystemsManagement.Model.Tag
$tag.Key = "tag-key"
$tag.Value = "tag-value"
```

```
Write-SSMParameter `
    -Name "`parameter-name`" `
    -Value "`a-comma-separated-list-of-values`" `
    -Type "StringList" `
    -Tags $tag
```

If successful, the command returns the version number of the
parameter.

Here is an example.

```
Write-SSMParameter `
    -Name "stringlist-parameter" `
    -Value "Milana,Mariana,Mark,Miguel" `
    -Type "StringList" `
    -Tags $tag
```

###### Note

Items in a `StringList` must be
separated by a comma (,). You can't use other punctuation or
special characters to escape items in the list. If you have a
parameter value that requires a comma, then use the `String` type. 3. Run the following command to verify the details of the
parameter.

```
(Get-SSMParameterValue -Name "`the-parameter-name-you-specified`").Parameters
```

## Creating a SecureString

parameter (Tools for Windows PowerShell)

Before you create a `SecureString` parameter, read about the
requirements for this type of parameter. For more information, see [Creating a SecureString
parameter using the AWS CLI](param-create-cli.md#param-create-cli-securestring "param-create-cli.md#param-create-cli-securestring").

###### Important

Only the _value_ of a `SecureString` parameter is
encrypted. Parameter names, descriptions, and other properties aren't
encrypted.

###### Important

Parameter Store only supports [symmetric encryption KMS keys](../../../kms/latest/developerguide/symm-asymm-choose-key-spec.md#symmetric-cmks "../../../kms/latest/developerguide/symm-asymm-choose-key-spec.md#symmetric-cmks"). You can't use an [asymmetric encryption KMS key](../../../kms/latest/developerguide/symmetric-asymmetric.md "../../../kms/latest/developerguide/symmetric-asymmetric.md") to encrypt your parameters. For help
determining whether a KMS key is symmetric or asymmetric, see [Identifying symmetric and asymmetric KMS keys](../../../kms/latest/developerguide/find-symm-asymm.md "../../../kms/latest/developerguide/find-symm-asymm.md") in the
_AWS Key Management Service Developer Guide_

1. Install and configure the AWS Tools for PowerShell (Tools for Windows PowerShell), if you haven't already.

For information, see [Installing the
AWS Tools for PowerShell](../../../powershell/latest/userguide/pstools-getting-set-up.md "../../../powershell/latest/userguide/pstools-getting-set-up.md"). 2. Run the following command to create a parameter. Replace each
`example resource placeholder` with
your own information.

###### Note

To create a parameter with a tag, first create the
service.model.tag as a variable. Here is an example.

```
$tag = New-Object Amazon.SimpleSystemsManagement.Model.Tag
$tag.Key = "tag-key"
$tag.Value = "tag-value"
```

```
Write-SSMParameter `
    -Name "`parameter-name`" `
    -Value "`parameter-value`" `
    -Type "SecureString"  `
    -KeyId "`an AWS KMS key ID, an AWS KMS key ARN, an alias name, or an alias ARN`" `
    -Tags $tag
```

If successful, the command returns the version number of the
parameter.

###### Note

To use the AWS managed key assigned to your account, remove
the `-KeyId` parameter from the
command.

Here is an example that uses an obfuscated name (3l3vat3131) for a
password parameter and an AWS managed key.

```
Write-SSMParameter `
    -Name "/Finance/Payroll/3l3vat3131" `
    -Value "P@sSwW)rd" `
    -Type "SecureString"`
    -Tags $tag
```

3. Run the following command to verify the details of the
   parameter.

```
(Get-SSMParameterValue -Name "`the-parameter-name-you-specified`" –WithDecryption $true).Parameters
```

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
