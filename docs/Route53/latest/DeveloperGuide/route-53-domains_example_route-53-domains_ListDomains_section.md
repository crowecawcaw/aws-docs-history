# Use `ListDomains` with an AWS SDK or CLI

The following code examples show how to use `ListDomains`.

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
    /// List the domains for the account.
    /// </summary>
    /// <returns>A collection of domain summary records.</returns>
    public async Task<List<DomainSummary>> ListDomains()
    {
        var results = new List<DomainSummary>();
        var paginateDomains = _amazonRoute53Domains.Paginators.ListDomains(
            new ListDomainsRequest());

        // Get the entire list using the paginator.
        await foreach (var domain in paginateDomains.Domains)
        {
            results.Add(domain);
        }
        return results;
    }


```

- For API details, see
  [ListDomains](../../../goto/DotNetSDKV3/route53domains-2014-05-15/ListDomains.md "../../../goto/DotNetSDKV3/route53domains-2014-05-15/ListDomains.md")
  in _AWS SDK for .NET API Reference_.

CLI

**AWS CLI**

**To list the domains that are registered with the current AWS account**

The following `list-domains` command lists summary information about the domains that are registered with the current AWS account.

This command runs only in the `us-east-1` Region. If your default region is set to `us-east-1`, you can omit the `region` parameter.

```
`aws route53domains list-domains
 --region `us-east-1``

```

Output:

```
{
    "Domains": [
        {
            "DomainName": "example.com",
            "AutoRenew": true,
            "TransferLock": true,
            "Expiry": 1602712345.0
        },
        {
            "DomainName": "example.net",
            "AutoRenew": true,
            "TransferLock": true,
            "Expiry": 1602723456.0
        },
        {
            "DomainName": "example.org",
            "AutoRenew": true,
            "TransferLock": true,
            "Expiry": 1602734567.0
        }
    ]
}
```

- For API details, see
  [ListDomains](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53domains/list-domains.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53domains/list-domains.html")
  in _AWS CLI Command Reference_.

Java

**SDK for Java 2.x**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/route53#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/route53#code-examples").

```
    public static void listDomains(Route53DomainsClient route53DomainsClient) {
        try {
            ListDomainsIterable listRes = route53DomainsClient.listDomainsPaginator();
            listRes.stream()
                    .flatMap(r -> r.domains().stream())
                    .forEach(content -> System.out.println("The domain name is " + content.domainName()));

        } catch (Route53Exception e) {
            System.err.println(e.getMessage());
            System.exit(1);
        }
    }


```

- For API details, see
  [ListDomains](../../../goto/SdkForJavaV2/route53domains-2014-05-15/ListDomains.md "../../../goto/SdkForJavaV2/route53domains-2014-05-15/ListDomains.md")
  in _AWS SDK for Java 2.x API Reference_.

Kotlin

**SDK for Kotlin**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/kotlin/services/route53#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/kotlin/services/route53#code-examples").

```
suspend fun listDomains() {
    Route53DomainsClient.fromEnvironment { region = "us-east-1" }.use { route53DomainsClient ->
        route53DomainsClient
            .listDomainsPaginated(ListDomainsRequest {})
            .transform { it.domains?.forEach { obj -> emit(obj) } }
            .collect { content ->
                println("The domain name is ${content.domainName}")
            }
    }
}


```

- For API details, see
  [ListDomains](https://sdk.amazonaws.com/kotlin/api/latest/index.html "https://sdk.amazonaws.com/kotlin/api/latest/index.html")
  in _AWS SDK for Kotlin API reference_.

For a complete list of AWS SDK developer guides and code examples, see
[Using Route 53 with an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.
