# Use `DescribeCommunications` with an AWS SDK or CLI

The following code examples show how to use `DescribeCommunications`.

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
    /// Describe the communications for a case, optionally with a date filter.
    /// </summary>
    /// <param name="caseId">The ID of the support case.</param>
    /// <param name="afterTime">The optional start date for a filtered search.</param>
    /// <param name="beforeTime">The optional end date for a filtered search.</param>
    /// <returns>The list of communications for the case.</returns>
    public async Task<List<Communication>> DescribeCommunications(string caseId, DateTime? afterTime = null, DateTime? beforeTime = null)
    {
        var results = new List<Communication>();
        var paginateCommunications = _amazonSupport.Paginators.DescribeCommunications(
            new DescribeCommunicationsRequest()
            {
                CaseId = caseId,
                AfterTime = afterTime?.ToString("s"),
                BeforeTime = beforeTime?.ToString("s")
            });
        // Get the entire list using the paginator.
        await foreach (var communications in paginateCommunications.Communications)
        {
            results.Add(communications);
        }
        return results;
    }



```

- For API details, see
  [DescribeCommunications](../../../goto/DotNetSDKV3/support-2013-04-15/DescribeCommunications.md "../../../goto/DotNetSDKV3/support-2013-04-15/DescribeCommunications.md")
  in _AWS SDK for .NET API Reference_.

CLI

**AWS CLI**

**To describe the latest communication for a case**

The following `describe-communications` example returns the latest communication for the specified support case in your AWS account.

```
`aws support describe-communications \
 --case-id `"case-12345678910-2013-c4c1d2bf33c5cf47"` \
 --after-time `"2020-03-23T21:31:47.774Z"` \
 --max-item `1``

```

Output:

```
{
    "communications": [
        {
            "body": "I want to learn more about an AWS service.",
            "attachmentSet": [],
            "caseId": "case-12345678910-2013-c4c1d2bf33c5cf47",
            "timeCreated": "2020-05-12T23:12:35.000Z",
            "submittedBy": "Amazon Web Services"
        }
    ],
    "NextToken": "eyJuZXh0VG9rZW4iOiBudWxsLCAiYm90b190cnVuY2F0ZV9hbW91bnQEXAMPLE=="
}
```

For more information, see [Case management](case-management.md "case-management.md") in the _AWS Support User Guide_.

- For API details, see
  [DescribeCommunications](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/support/describe-communications.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/support/describe-communications.html")
  in _AWS CLI Command Reference_.

Java

**SDK for Java 2.x**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/support#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/support#code-examples").

```
    public static String listCommunications(SupportClient supportClient, String caseId) {
        try {
            String attachId = null;
            DescribeCommunicationsRequest communicationsRequest = DescribeCommunicationsRequest.builder()
                    .caseId(caseId)
                    .maxResults(10)
                    .build();

            DescribeCommunicationsResponse response = supportClient.describeCommunications(communicationsRequest);
            List<Communication> communications = response.communications();
            for (Communication comm : communications) {
                System.out.println("the body is: " + comm.body());

                // Get the attachment id value.
                List<AttachmentDetails> attachments = comm.attachmentSet();
                for (AttachmentDetails detail : attachments) {
                    attachId = detail.attachmentId();
                }
            }
            return attachId;

        } catch (SupportException e) {
            System.out.println(e.getLocalizedMessage());
            System.exit(1);
        }
        return "";
    }


```

- For API details, see
  [DescribeCommunications](../../../goto/SdkForJavaV2/support-2013-04-15/DescribeCommunications.md "../../../goto/SdkForJavaV2/support-2013-04-15/DescribeCommunications.md")
  in _AWS SDK for Java 2.x API Reference_.

JavaScript

**SDK for JavaScript (v3)**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javascriptv3/example_code/support#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javascriptv3/example_code/support#code-examples").

```
import { DescribeCommunicationsCommand } from "@aws-sdk/client-support";

import { client } from "../libs/client.js";

export const main = async () => {
  try {
    // Get all communications for the support case.
    // Filter results by providing parameters to the DescribeCommunicationsCommand. Refer
    // to the TypeScript definition and the API doc for more information on possible parameters.
    // https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/clients/client-support/interfaces/describecommunicationscommandinput.html
    const response = await client.send(
      new DescribeCommunicationsCommand({
        // Set value to an existing case id.
        caseId: "CASE_ID",
      }),
    );
    const text = response.communications.map((item) => item.body).join("\n");
    console.log(text);
    return response;
  } catch (err) {
    console.error(err);
  }
};


```

- For API details, see
  [DescribeCommunications](../../../AWSJavaScriptSDK/v3/latest/client/support/command/DescribeCommunicationsCommand.md "../../../AWSJavaScriptSDK/v3/latest/client/support/command/DescribeCommunicationsCommand.md")
  in _AWS SDK for JavaScript API Reference_.

Kotlin

**SDK for Kotlin**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/kotlin/services/support#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/kotlin/services/support#code-examples").

```
suspend fun listCommunications(caseIdVal: String?): String? {
    val communicationsRequest =
        DescribeCommunicationsRequest {
            caseId = caseIdVal
            maxResults = 10
        }

    SupportClient.fromEnvironment { region = "us-west-2" }.use { supportClient ->
        val response = supportClient.describeCommunications(communicationsRequest)
        response.communications?.forEach { comm ->
            println("the body is: " + comm.body)
            comm.attachmentSet?.forEach { detail ->
                return detail.attachmentId
            }
        }
    }
    return ""
}


```

- For API details, see
  [DescribeCommunications](https://sdk.amazonaws.com/kotlin/api/latest/index.html "https://sdk.amazonaws.com/kotlin/api/latest/index.html")
  in _AWS SDK for Kotlin API reference_.

PowerShell

**Tools for PowerShell V4**

**Example 1: Returns all communications for the specified case.**

```
Get-ASACommunication -CaseId "case-12345678910-2013-c4c1d2bf33c5cf47"

```

**Example 2: Returns all communications since midnight UTC on January 1st 2012 for the specified case.**

```
Get-ASACommunication -CaseId "case-12345678910-2013-c4c1d2bf33c5cf47" -AfterTime "2012-01-10T00:00Z"

```

- For API details, see
  [DescribeCommunications](../../../powershell/v4/reference.md "../../../powershell/v4/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V4)_.

**Tools for PowerShell V5**

**Example 1: Returns all communications for the specified case.**

```
Get-ASACommunication -CaseId "case-12345678910-2013-c4c1d2bf33c5cf47"

```

**Example 2: Returns all communications since midnight UTC on January 1st 2012 for the specified case.**

```
Get-ASACommunication -CaseId "case-12345678910-2013-c4c1d2bf33c5cf47" -AfterTime "2012-01-10T00:00Z"

```

- For API details, see
  [DescribeCommunications](../../../powershell/v5/reference.md "../../../powershell/v5/reference.md")
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


    def describe_all_case_communications(self, case_id):
        """
        Describe all the communications for a case using a paginator.

        :param case_id: The ID of the case.
        :return: The communications for the case.
        """
        try:
            communications = []
            paginator = self.support_client.get_paginator("describe_communications")
            for page in paginator.paginate(caseId=case_id):
                communications += page["communications"]
        except ClientError as err:
            if err.response["Error"]["Code"] == "SubscriptionRequiredException":
                logger.info(
                    "You must have a Business, Enterprise On-Ramp, or Enterprise Support "
                    "plan to use the AWS Support API. \n\tPlease upgrade your subscription to run these "
                    "examples."
                )
            else:
                logger.error(
                    "Couldn't describe communications. Here's why: %s: %s",
                    err.response["Error"]["Code"],
                    err.response["Error"]["Message"],
                )
                raise
        else:
            return communications



```

- For API details, see
  [DescribeCommunications](../../../goto/boto3/support-2013-04-15/DescribeCommunications.md "../../../goto/boto3/support-2013-04-15/DescribeCommunications.md")
  in _AWS SDK for Python (Boto3) API Reference_.

For a complete list of AWS SDK developer guides and code examples, see
[Using AWS Support with an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.
