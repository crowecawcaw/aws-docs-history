# Use `CreateGroup` with an AWS SDK or CLI

The following code examples show how to use `CreateGroup`.

CLI

**AWS CLI**

**To create an IAM group**

The following `create-group` command creates an IAM group named `Admins`.

```
`aws iam create-group \
 --group-name `Admins``

```

Output:

```
{
    "Group": {
        "Path": "/",
        "CreateDate": "2015-03-09T20:30:24.940Z",
        "GroupId": "AIDGPMS9RO4H3FEXAMPLE",
        "Arn": "arn:aws:iam::123456789012:group/Admins",
        "GroupName": "Admins"
    }
}
```

For more information, see [Creating IAM user groups](id_groups_create.md "id_groups_create.md") in the _AWS IAM User Guide_.

- For API details, see
  [CreateGroup](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/create-group.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/create-group.html")
  in _AWS CLI Command Reference_.

JavaScript

**SDK for JavaScript (v3)**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javascriptv3/example_code/iam#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javascriptv3/example_code/iam#code-examples").

```
import { CreateGroupCommand, IAMClient } from "@aws-sdk/client-iam";

const client = new IAMClient({});

/**
 *
 * @param {string} groupName
 */
export const createGroup = async (groupName) => {
  const command = new CreateGroupCommand({ GroupName: groupName });

  const response = await client.send(command);
  console.log(response);
  return response;
};


```

- For API details, see
  [CreateGroup](../../../AWSJavaScriptSDK/v3/latest/client/iam/command/CreateGroupCommand.md "../../../AWSJavaScriptSDK/v3/latest/client/iam/command/CreateGroupCommand.md")
  in _AWS SDK for JavaScript API Reference_.

PowerShell

**Tools for PowerShell V4**

**Example 1: This example creates a new IAM group named `Developers`.**

```
New-IAMGroup -GroupName Developers

```

**Output:**

```
Arn        : arn:aws:iam::123456789012:group/Developers
CreateDate : 4/14/2015 11:21:31 AM
GroupId    : QNEJ5PM4NFSQCEXAMPLE1
GroupName  : Developers
Path       : /
```

- For API details, see
  [CreateGroup](../../../powershell/v4/reference.md "../../../powershell/v4/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V4)_.

**Tools for PowerShell V5**

**Example 1: This example creates a new IAM group named `Developers`.**

```
New-IAMGroup -GroupName Developers

```

**Output:**

```
Arn        : arn:aws:iam::123456789012:group/Developers
CreateDate : 4/14/2015 11:21:31 AM
GroupId    : QNEJ5PM4NFSQCEXAMPLE1
GroupName  : Developers
Path       : /
```

- For API details, see
  [CreateGroup](../../../powershell/v5/reference.md "../../../powershell/v5/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V5)_.

For a complete list of AWS SDK developer guides and code examples, see
[Using this service with an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.
