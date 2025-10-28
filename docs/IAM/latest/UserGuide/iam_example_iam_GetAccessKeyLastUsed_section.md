# Use `GetAccessKeyLastUsed` with an AWS SDK or CLI

The following code examples show how to use `GetAccessKeyLastUsed`.

Action examples are code excerpts from larger programs and must be run in context. You can see this action in
context in the following code example:

- [Manage access keys](iam_example_iam_Scenario_ManageAccessKeys_section.md "iam_example_iam_Scenario_ManageAccessKeys_section.md")

C++

**SDK for C++**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/cpp/example_code/iam#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/cpp/example_code/iam#code-examples").

```
bool AwsDoc::IAM::accessKeyLastUsed(const Aws::String &secretKeyID,
                                    const Aws::Client::ClientConfiguration &clientConfig) {
    Aws::IAM::IAMClient iam(clientConfig);
    Aws::IAM::Model::GetAccessKeyLastUsedRequest request;

    request.SetAccessKeyId(secretKeyID);

    Aws::IAM::Model::GetAccessKeyLastUsedOutcome outcome = iam.GetAccessKeyLastUsed(
            request);

    if (!outcome.IsSuccess()) {
        std::cerr << "Error querying last used time for access key " <<
                  secretKeyID << ":" << outcome.GetError().GetMessage() << std::endl;
    }
    else {
        Aws::String lastUsedTimeString =
                outcome.GetResult()
                        .GetAccessKeyLastUsed()
                        .GetLastUsedDate()
                        .ToGmtString(Aws::Utils::DateFormat::ISO_8601);
        std::cout << "Access key " << secretKeyID << " last used at time " <<
                  lastUsedTimeString << std::endl;
    }

    return outcome.IsSuccess();
}


```

- For API details, see
  [GetAccessKeyLastUsed](../../../goto/SdkForCpp/iam-2010-05-08/GetAccessKeyLastUsed.md "../../../goto/SdkForCpp/iam-2010-05-08/GetAccessKeyLastUsed.md")
  in _AWS SDK for C++ API Reference_.

CLI

**AWS CLI**

**To retrieve information about when the specified access key was last used**

The following example retrieves information about when the access key `ABCDEXAMPLE` was last used.

```
`aws iam get-access-key-last-used \
 --access-key-id `ABCDEXAMPLE``

```

Output:

```
{
    "UserName":  "Bob",
    "AccessKeyLastUsed": {
        "Region": "us-east-1",
        "ServiceName": "iam",
        "LastUsedDate": "2015-06-16T22:45:00Z"
    }
}
```

For more information, see [Managing access keys for IAM users](id_credentials_access-keys.md "id_credentials_access-keys.md") in the _AWS IAM User Guide_.

- For API details, see
  [GetAccessKeyLastUsed](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/get-access-key-last-used.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/get-access-key-last-used.html")
  in _AWS CLI Command Reference_.

JavaScript

**SDK for JavaScript (v3)**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javascriptv3/example_code/iam#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javascriptv3/example_code/iam#code-examples").

Get the access key.

```
import { GetAccessKeyLastUsedCommand, IAMClient } from "@aws-sdk/client-iam";

const client = new IAMClient({});

/**
 *
 * @param {string} accessKeyId
 */
export const getAccessKeyLastUsed = async (accessKeyId) => {
  const command = new GetAccessKeyLastUsedCommand({
    AccessKeyId: accessKeyId,
  });

  const response = await client.send(command);

  if (response.AccessKeyLastUsed?.LastUsedDate) {
    console.log(`
    ${accessKeyId} was last used by ${response.UserName} via
    the ${response.AccessKeyLastUsed.ServiceName} service on
    ${response.AccessKeyLastUsed.LastUsedDate.toISOString()}
    `);
  }

  return response;
};


```

- For more information, see [AWS SDK for JavaScript Developer Guide](../../../sdk-for-javascript/v3/developer-guide/iam-examples-managing-access-keys.md#iam-examples-managing-access-keys-last-used "../../../sdk-for-javascript/v3/developer-guide/iam-examples-managing-access-keys.md#iam-examples-managing-access-keys-last-used").
- For API details, see
  [GetAccessKeyLastUsed](../../../AWSJavaScriptSDK/v3/latest/client/iam/command/GetAccessKeyLastUsedCommand.md "../../../AWSJavaScriptSDK/v3/latest/client/iam/command/GetAccessKeyLastUsedCommand.md")
  in _AWS SDK for JavaScript API Reference_.

**SDK for JavaScript (v2)**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javascript/example_code/iam#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javascript/example_code/iam#code-examples").

```
// Load the AWS SDK for Node.js
var AWS = require("aws-sdk");
// Set the region
AWS.config.update({ region: "REGION" });

// Create the IAM service object
var iam = new AWS.IAM({ apiVersion: "2010-05-08" });

iam.getAccessKeyLastUsed(
  { AccessKeyId: "ACCESS_KEY_ID" },
  function (err, data) {
    if (err) {
      console.log("Error", err);
    } else {
      console.log("Success", data.AccessKeyLastUsed);
    }
  }
);


```

- For more information, see [AWS SDK for JavaScript Developer Guide](../../../sdk-for-javascript/v2/developer-guide/iam-examples-managing-access-keys.md#iam-examples-managing-access-keys-last-used "../../../sdk-for-javascript/v2/developer-guide/iam-examples-managing-access-keys.md#iam-examples-managing-access-keys-last-used").
- For API details, see
  [GetAccessKeyLastUsed](../../../goto/AWSJavaScriptSDK/iam-2010-05-08/GetAccessKeyLastUsed.md "../../../goto/AWSJavaScriptSDK/iam-2010-05-08/GetAccessKeyLastUsed.md")
  in _AWS SDK for JavaScript API Reference_.

PowerShell

**Tools for PowerShell V4**

**Example 1: Returns the owning user name and last-usage information for the supplied access key.**

```
Get-IAMAccessKeyLastUsed -AccessKeyId ABCDEXAMPLE

```

- For API details, see
  [GetAccessKeyLastUsed](../../../powershell/v4/reference.md "../../../powershell/v4/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V4)_.

**Tools for PowerShell V5**

**Example 1: Returns the owning user name and last-usage information for the supplied access key.**

```
Get-IAMAccessKeyLastUsed -AccessKeyId ABCDEXAMPLE

```

- For API details, see
  [GetAccessKeyLastUsed](../../../powershell/v5/reference.md "../../../powershell/v5/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V5)_.

Python

**SDK for Python (Boto3)**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/iam#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/iam#code-examples").

```
def get_last_use(key_id):
    """
    Gets information about when and how a key was last used.

    :param key_id: The ID of the key to look up.
    :return: Information about the key's last use.
    """
    try:
        response = iam.meta.client.get_access_key_last_used(AccessKeyId=key_id)
        last_used_date = response["AccessKeyLastUsed"].get("LastUsedDate", None)
        last_service = response["AccessKeyLastUsed"].get("ServiceName", None)
        logger.info(
            "Key %s was last used by %s on %s to access %s.",
            key_id,
            response["UserName"],
            last_used_date,
            last_service,
        )
    except ClientError:
        logger.exception("Couldn't get last use of key %s.", key_id)
        raise
    else:
        return response




```

- For API details, see
  [GetAccessKeyLastUsed](../../../goto/boto3/iam-2010-05-08/GetAccessKeyLastUsed.md "../../../goto/boto3/iam-2010-05-08/GetAccessKeyLastUsed.md")
  in _AWS SDK for Python (Boto3) API Reference_.

For a complete list of AWS SDK developer guides and code examples, see
[Using this service with an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.
