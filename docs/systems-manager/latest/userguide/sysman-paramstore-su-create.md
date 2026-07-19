# Creating Parameter Store parameters in Systems Manager

A _parameter_ is any piece of data stored in Parameter Store, such as a block
of text, a list of names, an AMI ID, a license key, and so on. You can
centrally and securely reference this data in your scripts, commands, and SSM
documents.

Parameter Store provides support for the following parameter types:

- `String`
- `StringList`
- `SecureString`
  For more information about the preceding types, see [Understanding parameter types](systems-manager/latest/userguide/what-is-a-parameter.md "systems-manager/latest/userguide/what-is-a-parameter.md").

In the following sections, you learn how to create Parameter Store parameters
using the AWS Management Console, the AWS Command Line Interface (AWS CLI), or AWS Tools for Windows PowerShell (Tools for Windows PowerShell).

###### Topics

- [Creating a Parameter Store parameter using the console](parameter-create-console.md "parameter-create-console.md")
- [Creating a Parameter Store parameter using the AWS CLI](param-create-cli.md "param-create-cli.md")
- [Creating a Parameter Store parameter using Tools for Windows PowerShell](param-create-ps.md "param-create-ps.md")
