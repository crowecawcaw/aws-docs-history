# Use `ResolveCase` with an AWS SDK or CLI

The following code examples show how to use `ResolveCase`.

Action examples are code excerpts from larger programs and must be run in context. You can see this action in
context in the following code example:

- [Learn the basics](example_support_Scenario_GetStartedSupportCases_section.md "example_support_Scenario_GetStartedSupportCases_section.md")

.NET

**SDK for .NET**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/dotnetv3/Support#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/dotnetv3/Support#code-examples").

```

    /// <summary>
    /// Resolve a support case by caseId.
    /// </summary>
    /// <param name="caseId">Id for the support case.</param>
    /// <returns>The final status of the case after resolving.</returns>
    public async Task<string> ResolveCase(string caseId)
    {
        var response = await _amazonSupport.ResolveCaseAsync(
            new ResolveCaseRequest()
            {
                CaseId = caseId
            });
        return response.FinalCaseStatus;
    }



```

- For API details, see
  [ResolveCase](../../../goto/DotNetSDKV3/support-2013-04-15/ResolveCase.md "../../../goto/DotNetSDKV3/support-2013-04-15/ResolveCase.md")
  in _AWS SDK for .NET API Reference_.

CLI

**AWS CLI**

**To resolve a support case**

The following `resolve-case` example resolves a support case in your AWS account.

```
`aws support resolve-case \
 --case-id `"case-12345678910-2013-c4c1d2bf33c5cf47"``

```

Output:

```
{
    "finalCaseStatus": "resolved",
    "initialCaseStatus": "work-in-progress"
}
```

For more information, see [Case management](case-management.md "case-management.md") in the _AWS Support User Guide_.

- For API details, see
  [ResolveCase](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/support/resolve-case.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/support/resolve-case.html")
  in _AWS CLI Command Reference_.

Java

**SDK for Java 2.x**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/support#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/support#code-examples").

```
    public static void resolveSupportCase(SupportClient supportClient, String caseId) {
        try {
            ResolveCaseRequest caseRequest = ResolveCaseRequest.builder()
                    .caseId(caseId)
                    .build();

            ResolveCaseResponse response = supportClient.resolveCase(caseRequest);
            System.out.println("The status of case " + caseId + " is " + response.finalCaseStatus());

        } catch (SupportException e) {
            System.out.println(e.getLocalizedMessage());
            System.exit(1);
        }
    }


```

- For API details, see
  [ResolveCase](../../../goto/SdkForJavaV2/support-2013-04-15/ResolveCase.md "../../../goto/SdkForJavaV2/support-2013-04-15/ResolveCase.md")
  in _AWS SDK for Java 2.x API Reference_.

JavaScript

**SDK for JavaScript (v3)**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javascriptv3/example_code/support#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javascriptv3/example_code/support#code-examples").

```
import { ResolveCaseCommand } from "@aws-sdk/client-support";

import { client } from "../libs/client.js";

const main = async () => {
  try {
    const response = await client.send(
      new ResolveCaseCommand({
        caseId: "CASE_ID",
      }),
    );

    console.log(response.finalCaseStatus);
    return response;
  } catch (err) {
    console.error(err);
  }
};


```

- For API details, see
  [ResolveCase](../../../AWSJavaScriptSDK/v3/latest/client/support/command/ResolveCaseCommand.md "../../../AWSJavaScriptSDK/v3/latest/client/support/command/ResolveCaseCommand.md")
  in _AWS SDK for JavaScript API Reference_.

Kotlin

**SDK for Kotlin**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/kotlin/services/support#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/kotlin/services/support#code-examples").

```
suspend fun resolveSupportCase(caseIdVal: String) {
    val caseRequest =
        ResolveCaseRequest {
            caseId = caseIdVal
        }
    SupportClient.fromEnvironment { region = "us-west-2" }.use { supportClient ->
        val response = supportClient.resolveCase(caseRequest)
        println("The status of case $caseIdVal is ${response.finalCaseStatus}")
    }
}


```

- For API details, see
  [ResolveCase](https://sdk.amazonaws.com/kotlin/api/latest/index.html "https://sdk.amazonaws.com/kotlin/api/latest/index.html")
  in _AWS SDK for Kotlin API reference_.

PowerShell

**Tools for PowerShell V4**

**Example 1: Returns the initial state of the specified case and the current state after the call to resolve it is completed.**

```
Resolve-ASACase -CaseId "case-12345678910-2013-c4c1d2bf33c5cf47"

```

- For API details, see
  [ResolveCase](../../../powershell/v4/reference.md "../../../powershell/v4/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V4)_.

**Tools for PowerShell V5**

**Example 1: Returns the initial state of the specified case and the current state after the call to resolve it is completed.**

```
Resolve-ASACase -CaseId "case-12345678910-2013-c4c1d2bf33c5cf47"

```

- For API details, see
  [ResolveCase](../../../powershell/v5/reference.md "../../../powershell/v5/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V5)_.

Python

**SDK for Python (Boto3)**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/support#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/support#code-examples").

```
class SupportWrapper:
    """Encapsulates Support actions."""

    def __init__(self, support_client):
        """
        :param support_client: A Boto3 Support client.
        """
        self.support_client = support_client

    @classmethod
    def from_client(cls):
        """
        Instantiates this class from a Boto3 client.
        """
        support_client = boto3.client("support")
        return cls(support_client)


    def resolve_case(self, case_id):
        """
        Resolve a support case by its caseId.

        :param case_id: The ID of the case to resolve.
        :return: The final status of the case.
        """
        try:
            response = self.support_client.resolve_case(caseId=case_id)
            final_status = response["finalCaseStatus"]
        except ClientError as err:
            if err.response["Error"]["Code"] == "SubscriptionRequiredException":
                logger.info(
                    "You must have a Business, Enterprise On-Ramp, or Enterprise Support "
                    "plan to use the AWS Support API. \n\tPlease upgrade your subscription to run these "
                    "examples."
                )
            else:
                logger.error(
                    "Couldn't resolve case. Here's why: %s: %s",
                    err.response["Error"]["Code"],
                    err.response["Error"]["Message"],
                )
                raise
        else:
            return final_status



```

- For API details, see
  [ResolveCase](../../../goto/boto3/support-2013-04-15/ResolveCase.md "../../../goto/boto3/support-2013-04-15/ResolveCase.md")
  in _AWS SDK for Python (Boto3) API Reference_.

For a complete list of AWS SDK developer guides and code examples, see
[Using AWS Support with an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.
