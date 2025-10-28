# Use `DeleteRolePolicy` with an AWS SDK or CLI

The following code examples show how to use `DeleteRolePolicy`.

.NET

**SDK for .NET**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/dotnetv3/IAM#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/dotnetv3/IAM#code-examples").

```
    /// <summary>
    /// Delete an IAM role policy.
    /// </summary>
    /// <param name="roleName">The name of the IAM role.</param>
    /// <param name="policyName">The name of the IAM role policy to delete.</param>
    /// <returns>A Boolean value indicating the success of the action.</returns>
    public async Task<bool> DeleteRolePolicyAsync(string roleName, string policyName)
    {
        var response = await _IAMService.DeleteRolePolicyAsync(new DeleteRolePolicyRequest
        {
            PolicyName = policyName,
            RoleName = roleName,
        });

        return response.HttpStatusCode == System.Net.HttpStatusCode.OK;
    }



```

- For API details, see
  [DeleteRolePolicy](../../../goto/DotNetSDKV3/iam-2010-05-08/DeleteRolePolicy.md "../../../goto/DotNetSDKV3/iam-2010-05-08/DeleteRolePolicy.md")
  in _AWS SDK for .NET API Reference_.

CLI

**AWS CLI**

**To remove a policy from an IAM role**

The following `delete-role-policy` command removes the policy named `ExamplePolicy` from the role named `Test-Role`.

```
`aws iam delete-role-policy \
 --role-name `Test-Role` \
 --policy-name `ExamplePolicy``

```

This command produces no output.

For more information, see [Modifying a role](id_roles_manage_modify.md "id_roles_manage_modify.md") in the _AWS IAM User Guide_.

- For API details, see
  [DeleteRolePolicy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/delete-role-policy.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/delete-role-policy.html")
  in _AWS CLI Command Reference_.

JavaScript

**SDK for JavaScript (v3)**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javascriptv3/example_code/iam#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javascriptv3/example_code/iam#code-examples").

```
import { DeleteRolePolicyCommand, IAMClient } from "@aws-sdk/client-iam";

const client = new IAMClient({});

/**
 *
 * @param {string} roleName
 * @param {string} policyName
 */
export const deleteRolePolicy = (roleName, policyName) => {
  const command = new DeleteRolePolicyCommand({
    RoleName: roleName,
    PolicyName: policyName,
  });
  return client.send(command);
};


```

- For API details, see
  [DeleteRolePolicy](../../../AWSJavaScriptSDK/v3/latest/client/iam/command/DeleteRolePolicyCommand.md "../../../AWSJavaScriptSDK/v3/latest/client/iam/command/DeleteRolePolicyCommand.md")
  in _AWS SDK for JavaScript API Reference_.

PowerShell

**Tools for PowerShell V4**

**Example 1: This example deletes the inline policy `S3AccessPolicy` that is embedded in the IAM role `S3BackupRole`.**

```
Remove-IAMRolePolicy -PolicyName S3AccessPolicy -RoleName S3BackupRole

```

- For API details, see
  [DeleteRolePolicy](../../../powershell/v4/reference.md "../../../powershell/v4/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V4)_.

**Tools for PowerShell V5**

**Example 1: This example deletes the inline policy `S3AccessPolicy` that is embedded in the IAM role `S3BackupRole`.**

```
Remove-IAMRolePolicy -PolicyName S3AccessPolicy -RoleName S3BackupRole

```

- For API details, see
  [DeleteRolePolicy](../../../powershell/v5/reference.md "../../../powershell/v5/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V5)_.

For a complete list of AWS SDK developer guides and code examples, see
[Using this service with an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.
