# Use `AddCommunicationToCase` with an AWS SDK or CLI

The following code examples show how to use `AddCommunicationToCase`.

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
    /// Add communication to a case, including optional attachment set ID and CC email addresses.
    /// </summary>
    /// <param name="caseId">Id for the support case.</param>
    /// <param name="body">Body text of the communication.</param>
    /// <param name="attachmentSetId">Optional Id for an attachment set.</param>
    /// <param name="ccEmailAddresses">Optional list of CC email addresses.</param>
    /// <returns>True if successful.</returns>
    public async Task<bool> AddCommunicationToCase(string caseId, string body,
        string? attachmentSetId = null, List<string>? ccEmailAddresses = null)
    {
        var response = await _amazonSupport.AddCommunicationToCaseAsync(
            new AddCommunicationToCaseRequest()
            {
                CaseId = caseId,
                CommunicationBody = body,
                AttachmentSetId = attachmentSetId,
                CcEmailAddresses = ccEmailAddresses
            });
        return response.Result;
    }



```

- For API details, see
  [AddCommunicationToCase](../../../goto/DotNetSDKV3/support-2013-04-15/AddCommunicationToCase.md "../../../goto/DotNetSDKV3/support-2013-04-15/AddCommunicationToCase.md")
  in _AWS SDK for .NET API Reference_.

CLI

**AWS CLI**

**To add communication to a case**

The following `add-communication-to-case` example adds communications to a support case in your AWS account.

```
`aws support add-communication-to-case \
 --case-id `"case-12345678910-2013-c4c1d2bf33c5cf47"` \
 --communication-body `"I'm attaching a set of images to this case."` \
 --cc-email-addresses `"myemail@example.com"` \
 --attachment-set-id `"as-2f5a6faa2a4a1e600-mu-nk5xQlBr70-G1cUos5LZkd38KOAHZa9BMDVzNEXAMPLE"``

```

Output:

```
{
    "result": true
}
```

For more information, see [Case management](case-management.md "case-management.md") in the _AWS Support User Guide_.

- For API details, see
  [AddCommunicationToCase](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/support/add-communication-to-case.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/support/add-communication-to-case.html")
  in _AWS CLI Command Reference_.

Java

**SDK for Java 2.x**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/support#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/support#code-examples").

```
    public static void addAttachSupportCase(SupportClient supportClient, String caseId, String attachmentSetId) {
        try {
            AddCommunicationToCaseRequest caseRequest = AddCommunicationToCaseRequest.builder()
                    .caseId(caseId)
                    .attachmentSetId(attachmentSetId)
                    .communicationBody("Please refer to attachment for details.")
                    .build();

            AddCommunicationToCaseResponse response = supportClient.addCommunicationToCase(caseRequest);
            if (response.result())
                System.out.println("You have successfully added a communication to an AWS Support case");
            else
                System.out.println("There was an error adding the communication to an AWS Support case");

        } catch (SupportException e) {
            System.out.println(e.getLocalizedMessage());
            System.exit(1);
        }
    }


```

- For API details, see
  [AddCommunicationToCase](../../../goto/SdkForJavaV2/support-2013-04-15/AddCommunicationToCase.md "../../../goto/SdkForJavaV2/support-2013-04-15/AddCommunicationToCase.md")
  in _AWS SDK for Java 2.x API Reference_.

JavaScript

**SDK for JavaScript (v3)**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javascriptv3/example_code/support#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javascriptv3/example_code/support#code-examples").

```
import { AddCommunicationToCaseCommand } from "@aws-sdk/client-support";

import { client } from "../libs/client.js";

export const main = async () => {
  let attachmentSetId;

  try {
    // Add a communication to a case.
    const response = await client.send(
      new AddCommunicationToCaseCommand({
        communicationBody: "Adding an attachment.",
        // Set value to an existing support case id.
        caseId: "CASE_ID",
        // Optional. Set value to an existing attachment set id to add attachments to the case.
        attachmentSetId,
      }),
    );
    console.log(response);
    return response;
  } catch (err) {
    console.error(err);
  }
};


```

- For API details, see
  [AddCommunicationToCase](../../../AWSJavaScriptSDK/v3/latest/client/support/command/AddCommunicationToCaseCommand.md "../../../AWSJavaScriptSDK/v3/latest/client/support/command/AddCommunicationToCaseCommand.md")
  in _AWS SDK for JavaScript API Reference_.

Kotlin

**SDK for Kotlin**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/kotlin/services/support#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/kotlin/services/support#code-examples").

```
suspend fun addAttachSupportCase(
    caseIdVal: String?,
    attachmentSetIdVal: String?,
) {
    val caseRequest =
        AddCommunicationToCaseRequest {
            caseId = caseIdVal
            attachmentSetId = attachmentSetIdVal
            communicationBody = "Please refer to attachment for details."
        }

    SupportClient.fromEnvironment { region = "us-west-2" }.use { supportClient ->
        val response = supportClient.addCommunicationToCase(caseRequest)
        if (response.result) {
            println("You have successfully added a communication to an AWS Support case")
        } else {
            println("There was an error adding the communication to an AWS Support case")
        }
    }
}


```

- For API details, see
  [AddCommunicationToCase](https://sdk.amazonaws.com/kotlin/api/latest/index.html "https://sdk.amazonaws.com/kotlin/api/latest/index.html")
  in _AWS SDK for Kotlin API reference_.

PowerShell

**Tools for PowerShell V4**

**Example 1: Adds the body of an email communication to the specified case.**

```
Add-ASACommunicationToCase -CaseId "case-12345678910-2013-c4c1d2bf33c5cf47" -CommunicationBody "Some text about the case"

```

**Example 2: Adds the body of an email communication to the specified case plus one or more email addresses contained in the CC line of the email.**

```
Add-ASACommunicationToCase -CaseId "case-12345678910-2013-c4c1d2bf33c5cf47" -CcEmailAddress @("email1@address.com", "email2@address.com") -CommunicationBody "Some text about the case"

```

- For API details, see
  [AddCommunicationToCase](../../../powershell/v4/reference.md "../../../powershell/v4/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V4)_.

**Tools for PowerShell V5**

**Example 1: Adds the body of an email communication to the specified case.**

```
Add-ASACommunicationToCase -CaseId "case-12345678910-2013-c4c1d2bf33c5cf47" -CommunicationBody "Some text about the case"

```

**Example 2: Adds the body of an email communication to the specified case plus one or more email addresses contained in the CC line of the email.**

```
Add-ASACommunicationToCase -CaseId "case-12345678910-2013-c4c1d2bf33c5cf47" -CcEmailAddress @("email1@address.com", "email2@address.com") -CommunicationBody "Some text about the case"

```

- For API details, see
  [AddCommunicationToCase](../../../powershell/v5/reference.md "../../../powershell/v5/reference.md")
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


    def add_communication_to_case(self, attachment_set_id, case_id):
        """
        Add a communication and an attachment set to a case.

        :param attachment_set_id: The ID of an existing attachment set.
        :param case_id: The ID of the case.
        """
        try:
            self.support_client.add_communication_to_case(
                caseId=case_id,
                communicationBody="This is an example communication added to a support case.",
                attachmentSetId=attachment_set_id,
            )
        except ClientError as err:
            if err.response["Error"]["Code"] == "SubscriptionRequiredException":
                logger.info(
                    "You must have a Business, Enterprise On-Ramp, or Enterprise Support "
                    "plan to use the AWS Support API. \n\tPlease upgrade your subscription to run these "
                    "examples."
                )
            else:
                logger.error(
                    "Couldn't add communication. Here's why: %s: %s",
                    err.response["Error"]["Code"],
                    err.response["Error"]["Message"],
                )
                raise



```

- For API details, see
  [AddCommunicationToCase](../../../goto/boto3/support-2013-04-15/AddCommunicationToCase.md "../../../goto/boto3/support-2013-04-15/AddCommunicationToCase.md")
  in _AWS SDK for Python (Boto3) API Reference_.

For a complete list of AWS SDK developer guides and code examples, see
[Using AWS Support with an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.
