# Use `ListPrices` with an AWS SDK

The following code examples show how to use `ListPrices`.

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
    /// List prices for domain type operations.
    /// </summary>
    /// <param name="domainTypes">Domain types to include in the results.</param>
    /// <returns>The list of domain prices.</returns>
    public async Task<List<DomainPrice>> ListPrices(List<string> domainTypes)
    {
        var results = new List<DomainPrice>();
        var paginatePrices = _amazonRoute53Domains.Paginators.ListPrices(new ListPricesRequest());
        // Get the entire list using the paginator.
        await foreach (var prices in paginatePrices.Prices)
        {
            results.Add(prices);
        }
        return results.Where(p => domainTypes.Contains(p.Name)).ToList();
    }


```

- For API details, see
  [ListPrices](../../../goto/DotNetSDKV3/route53domains-2014-05-15/ListPrices.md "../../../goto/DotNetSDKV3/route53domains-2014-05-15/ListPrices.md")
  in _AWS SDK for .NET API Reference_.

Java

**SDK for Java 2.x**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/route53#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/route53#code-examples").

```
    public static void listPrices(Route53DomainsClient route53DomainsClient, String domainType) {
        try {
            ListPricesRequest pricesRequest = ListPricesRequest.builder()
                    .tld(domainType)
                    .build();

            ListPricesIterable listRes = route53DomainsClient.listPricesPaginator(pricesRequest);
            listRes.stream()
                    .flatMap(r -> r.prices().stream())
                    .forEach(content -> System.out.println(" Name: " + content.name() +
                            " Registration: " + content.registrationPrice().price() + " "
                            + content.registrationPrice().currency() +
                            " Renewal: " + content.renewalPrice().price() + " " + content.renewalPrice().currency()));

        } catch (Route53Exception e) {
            System.err.println(e.getMessage());
            System.exit(1);
        }
    }


```

- For API details, see
  [ListPrices](../../../goto/SdkForJavaV2/route53domains-2014-05-15/ListPrices.md "../../../goto/SdkForJavaV2/route53domains-2014-05-15/ListPrices.md")
  in _AWS SDK for Java 2.x API Reference_.

Kotlin

**SDK for Kotlin**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/kotlin/services/route53#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/kotlin/services/route53#code-examples").

```
suspend fun listAllPrices(domainType: String?) {
    val pricesRequest =
        ListPricesRequest {
            tld = domainType
        }

    Route53DomainsClient.fromEnvironment { region = "us-east-1" }.use { route53DomainsClient ->
        route53DomainsClient
            .listPricesPaginated(pricesRequest)
            .transform { it.prices?.forEach { obj -> emit(obj) } }
            .collect { pr ->
                println("Registration: ${pr.registrationPrice} ${pr.registrationPrice?.currency}")
                println("Renewal: ${pr.renewalPrice?.price} ${pr.renewalPrice?.currency}")
                println("Transfer: ${pr.transferPrice?.price} ${pr.transferPrice?.currency}")
                println("Restoration: ${pr.restorationPrice?.price} ${pr.restorationPrice?.currency}")
            }
    }
}


```

- For API details, see
  [ListPrices](https://sdk.amazonaws.com/kotlin/api/latest/index.html "https://sdk.amazonaws.com/kotlin/api/latest/index.html")
  in _AWS SDK for Kotlin API reference_.

For a complete list of AWS SDK developer guides and code examples, see
[Using Route 53 with an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.
