# Use `GetServiceLinkedRoleDeletionStatus` with an AWS SDK or CLI

The following code examples show how to use `GetServiceLinkedRoleDeletionStatus`.

CLI

**AWS CLI**

**To check the status of a request to delete a service-linked role**

The following `get-service-linked-role-deletion-status` example displays the status of a previously request to delete a service-linked role. The delete operation occurs asynchronously. When you make the request, you get a `DeletionTaskId` value that you provide as a parameter for this command.

```
`aws iam get-service-linked-role-deletion-status \
 --deletion-task-id `task/aws-service-role/lex.amazonaws.com/AWSServiceRoleForLexBots/1a2b3c4d-1234-abcd-7890-abcdeEXAMPLE``

```

Output:

```
{
"Status": "SUCCEEDED"
}
```

For more information, see [Using service-linked roles](using-service-linked-roles.md "using-service-linked-roles.md") in the _AWS IAM User Guide_.

- For API details, see
  [GetServiceLinkedRoleDeletionStatus](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/get-service-linked-role-deletion-status.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/get-service-linked-role-deletion-status.html")
  in _AWS CLI Command Reference_.

JavaScript

**SDK for JavaScript (v3)**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javascriptv3/example_code/iam#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javascriptv3/example_code/iam#code-examples").

```
import {
  GetServiceLinkedRoleDeletionStatusCommand,
  IAMClient,
} from "@aws-sdk/client-iam";

const client = new IAMClient({});

/**
 *
 * @param {string} deletionTaskId
 */
export const getServiceLinkedRoleDeletionStatus = (deletionTaskId) => {
  const command = new GetServiceLinkedRoleDeletionStatusCommand({
    DeletionTaskId: deletionTaskId,
  });

  return client.send(command);
};


```

- For API details, see
  [GetServiceLinkedRoleDeletionStatus](../../../AWSJavaScriptSDK/v3/latest/client/iam/command/GetServiceLinkedRoleDeletionStatusCommand.md "../../../AWSJavaScriptSDK/v3/latest/client/iam/command/GetServiceLinkedRoleDeletionStatusCommand.md")
  in _AWS SDK for JavaScript API Reference_.

For a complete list of AWS SDK developer guides and code examples, see
[Using this service with an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.
