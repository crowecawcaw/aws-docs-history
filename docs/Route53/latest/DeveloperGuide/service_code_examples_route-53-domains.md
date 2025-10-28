# Code examples for Route 53 domain registration using AWS SDKs

The following code examples show how to use Route 53 domain registration with an AWS software development kit (SDK).

_Basics_ are code examples that show you how to perform the essential operations within a service.

_Actions_ are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

For a complete list of AWS SDK developer guides and code examples, see
[Using Route 53 with an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.

**Get started**

The following code examples show how to get started using Route 53 domain registration.

.NET

**SDK for .NET**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/dotnetv3/Route53#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/dotnetv3/Route53#code-examples").

```

public static class HelloRoute53Domains
{
    static async Task Main(string[] args)
    {
        // Use the AWS .NET Core Setup package to set up dependency injection for the Amazon Route 53 domain registration service.
        // Use your AWS profile name, or leave it blank to use the default profile.
        using var host = Host.CreateDefaultBuilder(args)
            .ConfigureServices((_, services) =>
                services.AddAWSService<IAmazonRoute53Domains>()
            ).Build();

        // Now the client is available for injection.
        var route53Client = host.Services.GetRequiredService<IAmazonRoute53Domains>();

        // You can use await and any of the async methods to get a response.
        var response = await route53Client.ListPricesAsync(new ListPricesRequest { Tld = "com" });
        Console.WriteLine($"Hello Amazon Route 53 Domains! Following are prices for .com domain operations:");
        var comPrices = response.Prices.FirstOrDefault();
        if (comPrices != null)
        {
            Console.WriteLine($"\tRegistration: {comPrices.RegistrationPrice?.Price} {comPrices.RegistrationPrice?.Currency}");
            Console.WriteLine($"\tRenewal: {comPrices.RenewalPrice?.Price} {comPrices.RenewalPrice?.Currency}");
        }
    }
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
import software.amazon.awssdk.regions.Region;
import software.amazon.awssdk.services.route53domains.Route53DomainsClient;
import software.amazon.awssdk.services.route53.model.Route53Exception;
import software.amazon.awssdk.services.route53domains.model.DomainPrice;
import software.amazon.awssdk.services.route53domains.model.ListPricesRequest;
import software.amazon.awssdk.services.route53domains.model.ListPricesResponse;
import java.util.List;

/**
 * Before running this Java V2 code example, set up your development
 * environment, including your credentials.
 *
 * For more information, see the following documentation topic:
 *
 * https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/get-started.html
 *
 * This Java code examples performs the following operation:
 *
 * 1. Invokes ListPrices for at least one domain type, such as the “com” type
 * and displays the prices for Registration and Renewal.
 *
 */
public class HelloRoute53 {
    public static final String DASHES = new String(new char[80]).replace("\0", "-");

    public static void main(String[] args) {
        final String usage = "\n" +
                "Usage:\n" +
                "    <hostedZoneId> \n\n" +
                "Where:\n" +
                "    hostedZoneId - The id value of an existing hosted zone. \n";

        if (args.length != 1) {
            System.out.println(usage);
            System.exit(1);
        }

        String domainType = args[0];
        Region region = Region.US_EAST_1;
        Route53DomainsClient route53DomainsClient = Route53DomainsClient.builder()
                .region(region)
                .build();

        System.out.println(DASHES);
        System.out.println("Invokes ListPrices for at least one domain type.");
        listPrices(route53DomainsClient, domainType);
        System.out.println(DASHES);
    }

    public static void listPrices(Route53DomainsClient route53DomainsClient, String domainType) {
        try {
            ListPricesRequest pricesRequest = ListPricesRequest.builder()
                    .maxItems(10)
                    .tld(domainType)
                    .build();

            ListPricesResponse response = route53DomainsClient.listPrices(pricesRequest);
            List<DomainPrice> prices = response.prices();
            for (DomainPrice pr : prices) {
                System.out.println("Name: " + pr.name());
                System.out.println(
                        "Registration: " + pr.registrationPrice().price() + " " + pr.registrationPrice().currency());
                System.out.println("Renewal: " + pr.renewalPrice().price() + " " + pr.renewalPrice().currency());
                System.out.println("Transfer: " + pr.transferPrice().price() + " " + pr.transferPrice().currency());
                System.out.println("Transfer: " + pr.transferPrice().price() + " " + pr.transferPrice().currency());
                System.out.println("Change Ownership: " + pr.changeOwnershipPrice().price() + " "
                        + pr.changeOwnershipPrice().currency());
                System.out.println(
                        "Restoration: " + pr.restorationPrice().price() + " " + pr.restorationPrice().currency());
                System.out.println(" ");
            }

        } catch (Route53Exception e) {
            System.err.println(e.getMessage());
            System.exit(1);
        }
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

/**
 Before running this Kotlin code example, set up your development environment,
 including your credentials.

 For more information, see the following documentation topic:
 https://docs.aws.amazon.com/sdk-for-kotlin/latest/developer-guide/setup.html
 */
suspend fun main(args: Array<String>) {
    val usage = """
        Usage:
           <domainType>

       Where:
           domainType - The domain type (for example, com).
    """

    if (args.size != 1) {
        println(usage)
        exitProcess(0)
    }

    val domainType = args[0]
    println("Invokes ListPrices using a Paginated method.")
    listPricesPaginated(domainType)
}

suspend fun listPricesPaginated(domainType: String) {
    val pricesRequest =
        ListPricesRequest {
            maxItems = 10
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

###### Code examples

- [Basics](service_code_examples_route-53-domains_basics.md "service_code_examples_route-53-domains_basics.md")
  - [Hello Route 53 domain registration](route-53-domains_example_route-53-domains_Hello_section.md "route-53-domains_example_route-53-domains_Hello_section.md")
  - [Learn the basics](route-53-domains_example_route-53-domains_Scenario_GetStartedRoute53Domains_section.md "route-53-domains_example_route-53-domains_Scenario_GetStartedRoute53Domains_section.md")
  - [Actions](service_code_examples_route-53-domains_actions.md "service_code_examples_route-53-domains_actions.md")
    - [CheckDomainAvailability](route-53-domains_example_route-53-domains_CheckDomainAvailability_section.md "route-53-domains_example_route-53-domains_CheckDomainAvailability_section.md")
    - [CheckDomainTransferability](route-53-domains_example_route-53-domains_CheckDomainTransferability_section.md "route-53-domains_example_route-53-domains_CheckDomainTransferability_section.md")
    - [GetDomainDetail](route-53-domains_example_route-53-domains_GetDomainDetail_section.md "route-53-domains_example_route-53-domains_GetDomainDetail_section.md")
    - [GetDomainSuggestions](route-53-domains_example_route-53-domains_GetDomainSuggestions_section.md "route-53-domains_example_route-53-domains_GetDomainSuggestions_section.md")
    - [GetOperationDetail](route-53-domains_example_route-53-domains_GetOperationDetail_section.md "route-53-domains_example_route-53-domains_GetOperationDetail_section.md")
    - [ListDomains](route-53-domains_example_route-53-domains_ListDomains_section.md "route-53-domains_example_route-53-domains_ListDomains_section.md")
    - [ListOperations](route-53-domains_example_route-53-domains_ListOperations_section.md "route-53-domains_example_route-53-domains_ListOperations_section.md")
    - [ListPrices](route-53-domains_example_route-53-domains_ListPrices_section.md "route-53-domains_example_route-53-domains_ListPrices_section.md")
    - [RegisterDomain](route-53-domains_example_route-53-domains_RegisterDomain_section.md "route-53-domains_example_route-53-domains_RegisterDomain_section.md")
    - [ViewBilling](route-53-domains_example_route-53-domains_ViewBilling_section.md "route-53-domains_example_route-53-domains_ViewBilling_section.md")
