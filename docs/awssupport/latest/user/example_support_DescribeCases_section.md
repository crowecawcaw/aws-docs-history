

# Use `DescribeCases` with an AWS SDK or CLI
<a name="example_support_DescribeCases_section"></a>

The following code examples show how to use `DescribeCases`.

Action examples are code excerpts from larger programs and must be run in context. You can see this action in context in the following code examples: 
+  [Learn the basics](example_support_Scenario_GetStartedSupportCases_section.md) 
+  [Getting started with technical support](example_support_GettingStarted_062_section.md) 

------
#### [ .NET ]

**SDK for .NET**  
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/dotnetv3/Support#code-examples). 

```
    /// <summary>
    /// Get case details for a list of case ids, optionally with date filters.
    /// </summary>
    /// <param name="caseIds">The list of case IDs.</param>
    /// <param name="displayId">Optional display ID.</param>
    /// <param name="includeCommunication">True to include communication. Defaults to true.</param>
    /// <param name="includeResolvedCases">True to include resolved cases. Defaults to false.</param>
    /// <param name="afterTime">The optional start date for a filtered search.</param>
    /// <param name="beforeTime">The optional end date for a filtered search.</param>
    /// <param name="language">Optional language support for your case.
    /// Currently Chinese (“zh”), English ("en"), Japanese ("ja") and Korean (“ko”) are supported.</param>
    /// <returns>A list of CaseDetails.</returns>
    public async Task<List<CaseDetails>> DescribeCases(List<string> caseIds, string? displayId = null, bool includeCommunication = true,
        bool includeResolvedCases = false, DateTime? afterTime = null, DateTime? beforeTime = null,
        string language = "en")
    {
        var results = new List<CaseDetails>();
        var paginateCases = _amazonSupport.Paginators.DescribeCases(
            new DescribeCasesRequest()
            {
                CaseIdList = caseIds,
                DisplayId = displayId,
                IncludeCommunications = includeCommunication,
                IncludeResolvedCases = includeResolvedCases,
                AfterTime = afterTime?.ToString("s"),
                BeforeTime = beforeTime?.ToString("s"),
                Language = language
            });
        // Get the entire list using the paginator.
        await foreach (var cases in paginateCases.Cases)
        {
            results.Add(cases);
        }
        return results;
    }
```
+  For API details, see [DescribeCases](https://docs.aws.amazon.com/goto/DotNetSDKV3/support-2013-04-15/DescribeCases) in *AWS SDK for .NET API Reference*. 

------
#### [ CLI ]

**AWS CLI**  
**To describe a case**  
The following `describe-cases` example returns information about the specified support case in your AWS account.  

```
aws support describe-cases \
    --display-id {{"1234567890"}} \
    --after-time {{"2020-03-23T21:31:47.774Z"}} \
    --include-resolved-cases \
    --language {{"en"}} \
    --no-include-communications \
    --max-item {{1}}
```
Output:  

```
{
    "cases": [
        {
            "status": "resolved",
            "ccEmailAddresses": [],
            "timeCreated": "2020-03-23T21:31:47.774Z",
            "caseId": "case-12345678910-2013-c4c1d2bf33c5cf47",
            "severityCode": "low",
            "language": "en",
            "categoryCode": "using-aws",
            "serviceCode": "general-info",
            "submittedBy": "myemail@example.com",
            "displayId": "1234567890",
            "subject": "Question about my account"
        }
    ]
}
```
For more information, see [Case management](https://docs.aws.amazon.com/awssupport/latest/user/case-management.html) in the *AWS Support User Guide*.  
+  For API details, see [DescribeCases](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/support/describe-cases.html) in *AWS CLI Command Reference*. 

------
#### [ Java ]

**SDK for Java 2.x**  
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/support#code-examples). 

```
    public static void getOpenCase(SupportClient supportClient) {
        try {
            // Specify the start and end time.
            Instant now = Instant.now();
            java.time.LocalDate.now();
            Instant yesterday = now.minus(1, ChronoUnit.DAYS);

            DescribeCasesRequest describeCasesRequest = DescribeCasesRequest.builder()
                    .maxResults(20)
                    .afterTime(yesterday.toString())
                    .beforeTime(now.toString())
                    .build();

            DescribeCasesResponse response = supportClient.describeCases(describeCasesRequest);
            List<CaseDetails> cases = response.cases();
            for (CaseDetails sinCase : cases) {
                System.out.println("The case status is " + sinCase.status());
                System.out.println("The case Id is " + sinCase.caseId());
                System.out.println("The case subject is " + sinCase.subject());
            }

        } catch (SupportException e) {
            System.out.println(e.getLocalizedMessage());
            System.exit(1);
        }
    }
```
+  For API details, see [DescribeCases](https://docs.aws.amazon.com/goto/SdkForJavaV2/support-2013-04-15/DescribeCases) in *AWS SDK for Java 2.x API Reference*. 

------
#### [ JavaScript ]

**SDK for JavaScript (v3)**  
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javascriptv3/example_code/support#code-examples). 

```
import { DescribeCasesCommand } from "@aws-sdk/client-support";

import { client } from "../libs/client.js";

export const main = async () => {
  try {
    // Get all of the unresolved cases in your account.
    // Filter or expand results by providing parameters to the DescribeCasesCommand. Refer
    // to the TypeScript definition and the API doc for more information on possible parameters.
    // https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/clients/client-support/interfaces/describecasescommandinput.html
    const response = await client.send(new DescribeCasesCommand({}));
    const caseIds = response.cases.map((supportCase) => supportCase.caseId);
    console.log(caseIds);
    return response;
  } catch (err) {
    console.error(err);
  }
};
```
+  For API details, see [DescribeCases](https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/client/support/command/DescribeCasesCommand) in *AWS SDK for JavaScript API Reference*. 

------
#### [ Kotlin ]

**SDK for Kotlin**  
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/kotlin/services/support#code-examples). 

```
suspend fun getOpenCase() {
    // Specify the start and end time.
    val now = Instant.now()
    LocalDate.now()
    val yesterday = now.minus(1, ChronoUnit.DAYS)
    val describeCasesRequest =
        DescribeCasesRequest {
            maxResults = 20
            afterTime = yesterday.toString()
            beforeTime = now.toString()
        }

    SupportClient.fromEnvironment { region = "us-west-2" }.use { supportClient ->
        val response = supportClient.describeCases(describeCasesRequest)
        response.cases?.forEach { sinCase ->
            println("The case status is ${sinCase.status}")
            println("The case Id is ${sinCase.caseId}")
            println("The case subject is ${sinCase.subject}")
        }
    }
}
```
+  For API details, see [DescribeCases](https://sdk.amazonaws.com/kotlin/api/latest/index.html) in *AWS SDK for Kotlin API reference*. 

------
#### [ PowerShell ]

**Tools for PowerShell V4**  
**Example 1: Returns the details of all support cases.**  

```
Get-ASACase
```
**Example 2: Returns the details of all support cases since the specified date and time.**  

```
Get-ASACase -AfterTime "2013-09-10T03:06Z"
```
**Example 3: Returns the details of the first 10 support cases, including those that have been resolved.**  

```
Get-ASACase -MaxResult 10 -IncludeResolvedCases $true
```
**Example 4: Returns the details of the single specified support case.**  

```
Get-ASACase -CaseIdList "case-12345678910-2013-c4c1d2bf33c5cf47"
```
**Example 5: Returns the details of specified support cases.**  

```
Get-ASACase -CaseIdList @("case-12345678910-2013-c4c1d2bf33c5cf47", "case-18929034710-2011-c4fdeabf33c5cf47")
```
+  For API details, see [DescribeCases](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*. 

**Tools for PowerShell V5**  
**Example 1: Returns the details of all support cases.**  

```
Get-ASACase
```
**Example 2: Returns the details of all support cases since the specified date and time.**  

```
Get-ASACase -AfterTime "2013-09-10T03:06Z"
```
**Example 3: Returns the details of the first 10 support cases, including those that have been resolved.**  

```
Get-ASACase -MaxResult 10 -IncludeResolvedCases $true
```
**Example 4: Returns the details of the single specified support case.**  

```
Get-ASACase -CaseIdList "case-12345678910-2013-c4c1d2bf33c5cf47"
```
**Example 5: Returns the details of specified support cases.**  

```
Get-ASACase -CaseIdList @("case-12345678910-2013-c4c1d2bf33c5cf47", "case-18929034710-2011-c4fdeabf33c5cf47")
```
+  For API details, see [DescribeCases](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*. 

------
#### [ Python ]

**SDK for Python (Boto3)**  
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/support#code-examples). 

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


    def describe_cases(self, after_time, before_time, resolved):
        """
        Describe support cases over a period of time, optionally filtering
        by status.

        :param after_time: The start time to include for cases.
        :param before_time: The end time to include for cases.
        :param resolved: True to include resolved cases in the results,
            otherwise results are open cases.
        :return: The final status of the case.
        """
        try:
            cases = []
            paginator = self.support_client.get_paginator("describe_cases")
            for page in paginator.paginate(
                afterTime=after_time,
                beforeTime=before_time,
                includeResolvedCases=resolved,
                language="en",
            ):
                cases += page["cases"]
        except ClientError as err:
            if err.response["Error"]["Code"] == "SubscriptionRequiredException":
                logger.info(
                    "You must have a Business, Enterprise On-Ramp, or Enterprise Support "
                    "plan to use the AWS Support API. \n\tPlease upgrade your subscription to run these "
                    "examples."
                )
            else:
                logger.error(
                    "Couldn't describe cases. Here's why: %s: %s",
                    err.response["Error"]["Code"],
                    err.response["Error"]["Message"],
                )
                raise
        else:
            if resolved:
                cases = filter(lambda case: case["status"] == "resolved", cases)
            return cases
```
+  For API details, see [DescribeCases](https://docs.aws.amazon.com/goto/boto3/support-2013-04-15/DescribeCases) in *AWS SDK for Python (Boto3) API Reference*. 

------

For a complete list of AWS SDK developer guides and code examples, see [Using AWS Support with an AWS SDK](sdk-general-information-section.md). This topic also includes information about getting started and details about previous SDK versions.