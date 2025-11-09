AWS Systems Manager Change Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see
[AWS Systems Manager Change Manager availability change](change-manager-availability-change.md "change-manager-availability-change.md").

# Use `DeleteAssociation` with a CLI

The following code examples show how to use `DeleteAssociation`.

CLI

**AWS CLI**

**Example 1: To delete an association using the association ID**

The following `delete-association` example deletes the association for the specified association ID. There is no output if the command succeeds.

```
`aws ssm delete-association \
 --association-id `"8dfe3659-4309-493a-8755-0123456789ab"``

```

This command produces no output.

For more information, see [Editing and creating a new version of an association](sysman-state-assoc-edit.md "sysman-state-assoc-edit.md") in the _AWS Systems Manager User Guide_.

**Example 2: To delete an association**

The following `delete-association` example deletes the association between an instance and a document. There is no output if the command succeeds.

```
`aws ssm delete-association \
 --instance-id `"i-1234567890abcdef0"` \
 --name `"AWS-UpdateSSMAgent"``

```

This command produces no output.

For more information, see [Working with associations in Systems Manager](systems-manager-associations.md "systems-manager-associations.md") in the _AWS Systems Manager User Guide_.

- For API details, see
  [DeleteAssociation](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/delete-association.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/delete-association.html")
  in _AWS CLI Command Reference_.

PowerShell

**Tools for PowerShell V4**

**Example 1: This example deletes the association between an instance and a document. There is no output if the command succeeds.**

```
Remove-SSMAssociation -InstanceId "i-0cb2b964d3e14fd9f" -Name "AWS-UpdateSSMAgent"

```

- For API details, see
  [DeleteAssociation](../../../powershell/v4/reference.md "../../../powershell/v4/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V4)_.

**Tools for PowerShell V5**

**Example 1: This example deletes the association between an instance and a document. There is no output if the command succeeds.**

```
Remove-SSMAssociation -InstanceId "i-0cb2b964d3e14fd9f" -Name "AWS-UpdateSSMAgent"

```

- For API details, see
  [DeleteAssociation](../../../powershell/v5/reference.md "../../../powershell/v5/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V5)_.

For a complete list of AWS SDK developer guides and code examples, see
[Using this service with an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.
