# Use `GetOperationDetail` with an AWS SDK or CLI

The following code examples show how to use `GetOperationDetail`.

Action examples are code excerpts from larger programs and must be run in context. You can see this action in
context in the following code example:

- [Learn the basics](route-53-domains_example_route-53-domains_Scenario_GetStartedRoute53Domains_section.md "route-53-domains_example_route-53-domains_Scenario_GetStartedRoute53Domains_section.md")

.NET

**SDK for .NET**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/dotnetv3/Route53#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/dotnetv3/Route53#code-examples").

```

    /// <summary>
    /// Get details for a domain action operation.
    /// </summary>
    /// <param name="operationId">The operational Id.</param>
    /// <returns>A string describing the operational details.</returns>
    public async Task<string> GetOperationDetail(string? operationId)
    {
        if (operationId == null)
            return "Unable to get operational details because ID is null.";
        try
        {
            var operationDetails =
                await _amazonRoute53Domains.GetOperationDetailAsync(
                    new GetOperationDetailRequest
                    {
                        OperationId = operationId
                    }
                );

            var details = $"\tOperation {operationId}:\n" +
                          $"\tFor domain {operationDetails.DomainName} on {operationDetails.SubmittedDate.ToShortDateString()}.\n" +
                          $"\tMessage is {operationDetails.Message}.\n" +
                          $"\tStatus is {operationDetails.Status}.\n";

            return details;
        }
        catch (AmazonRoute53DomainsException ex)
        {
            return $"Unable to get operation details. Here's why: {ex.Message}.";
        }
    }


```

- For API details, see
  [GetOperationDetail](../../../goto/DotNetSDKV3/route53domains-2014-05-15/GetOperationDetail.md "../../../goto/DotNetSDKV3/route53domains-2014-05-15/GetOperationDetail.md")
  in _AWS SDK for .NET API Reference_.

CLI

**AWS CLI**

**To get the current status of an operation**

Some domain registration operations operate asynchronously and return a response before they finish. These operations return an operation ID that you can use to get the current status. The following `get-operation-detail` command returns the status of the specified operation.

This command runs only in the `us-east-1` Region. If your default region is set to `us-east-1`, you can omit the `region` parameter.

```
`aws route53domains get-operation-detail \
 --region `us-east-1` \
 --operation-id `edbd8d63-7fe7-4343-9bc5-54033example``

```

Output:

```
{
    "OperationId": "edbd8d63-7fe7-4343-9bc5-54033example",
    "Status": "SUCCESSFUL",
    "DomainName": "example.com",
    "Type": "DOMAIN_LOCK",
    "SubmittedDate": 1573749367.864
}
```

- For API details, see
  [GetOperationDetail](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53domains/get-operation-detail.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53domains/get-operation-detail.html")
  in _AWS CLI Command Reference_.

Java

**SDK for Java 2.x**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/route53#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/route53#code-examples").

```
    public static void getOperationalDetail(Route53DomainsClient route53DomainsClient, String operationId) {
        try {
            GetOperationDetailRequest detailRequest = GetOperationDetailRequest.builder()
                    .operationId(operationId)
                    .build();

            GetOperationDetailResponse response = route53DomainsClient.getOperationDetail(detailRequest);
            System.out.println("Operation detail message is " + response.message());

        } catch (Route53Exception e) {
            System.err.println(e.getMessage());
            System.exit(1);
        }
    }


```

- For API details, see
  [GetOperationDetail](../../../goto/SdkForJavaV2/route53domains-2014-05-15/GetOperationDetail.md "../../../goto/SdkForJavaV2/route53domains-2014-05-15/GetOperationDetail.md")
  in _AWS SDK for Java 2.x API Reference_.

Kotlin

**SDK for Kotlin**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/kotlin/services/route53#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/kotlin/services/route53#code-examples").

```
suspend fun getOperationalDetail(opId: String?) {
    val detailRequest =
        GetOperationDetailRequest {
            operationId = opId
        }
    Route53DomainsClient.fromEnvironment { region = "us-east-1" }.use { route53DomainsClient ->
        val response = route53DomainsClient.getOperationDetail(detailRequest)
        println("Operation detail message is ${response.message}")
    }
}


```

- For API details, see
  [GetOperationDetail](https://sdk.amazonaws.com/kotlin/api/latest/index.html "https://sdk.amazonaws.com/kotlin/api/latest/index.html")
  in _AWS SDK for Kotlin API reference_.

For a complete list of AWS SDK developer guides and code examples, see
[Using Route 53 with an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.
