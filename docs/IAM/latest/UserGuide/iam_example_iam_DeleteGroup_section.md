# Use `DeleteGroup` with an AWS SDK or CLI

The following code examples show how to use `DeleteGroup`.

CLI

**AWS CLI**

**To delete an IAM group**

The following `delete-group` command deletes an IAM group named `MyTestGroup`.

```
`aws iam delete-group \
 --group-name `MyTestGroup``

```

This command produces no output.

For more information, see [Deleting an IAM user group](id_groups_manage_delete.md "id_groups_manage_delete.md") in the _AWS IAM User Guide_.

- For API details, see
  [DeleteGroup](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/delete-group.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/delete-group.html")
  in _AWS CLI Command Reference_.

JavaScript

**SDK for JavaScript (v3)**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javascriptv3/example_code/iam#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javascriptv3/example_code/iam#code-examples").

```
import { DeleteGroupCommand, IAMClient } from "@aws-sdk/client-iam";

const client = new IAMClient({});

/**
 *
 * @param {string} groupName
 */
export const deleteGroup = async (groupName) => {
  const command = new DeleteGroupCommand({
    GroupName: groupName,
  });

  const response = await client.send(command);
  console.log(response);
  return response;
};


```

- For API details, see
  [DeleteGroup](../../../AWSJavaScriptSDK/v3/latest/client/iam/command/DeleteGroupCommand.md "../../../AWSJavaScriptSDK/v3/latest/client/iam/command/DeleteGroupCommand.md")
  in _AWS SDK for JavaScript API Reference_.

PowerShell

**Tools for PowerShell V4**

**Example 1: This example deletes the IAM group named `MyTestGroup`. The first command removes any IAM users that are members of the group, and the second command deletes the IAM group. Both commands work without any prompts for confirmation.**

```
(Get-IAMGroup -GroupName MyTestGroup).Users | Remove-IAMUserFromGroup -GroupName MyTestGroup -Force
Remove-IAMGroup -GroupName MyTestGroup -Force

```

- For API details, see
  [DeleteGroup](../../../powershell/v4/reference.md "../../../powershell/v4/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V4)_.

**Tools for PowerShell V5**

**Example 1: This example deletes the IAM group named `MyTestGroup`. The first command removes any IAM users that are members of the group, and the second command deletes the IAM group. Both commands work without any prompts for confirmation.**

```
(Get-IAMGroup -GroupName MyTestGroup).Users | Remove-IAMUserFromGroup -GroupName MyTestGroup -Force
Remove-IAMGroup -GroupName MyTestGroup -Force

```

- For API details, see
  [DeleteGroup](../../../powershell/v5/reference.md "../../../powershell/v5/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V5)_.

For a complete list of AWS SDK developer guides and code examples, see
[Using this service with an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.
