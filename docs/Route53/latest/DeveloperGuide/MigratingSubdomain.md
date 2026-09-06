

# Migrating DNS service for a subdomain to Amazon Route 53 without migrating the parent domain
<a name="MigratingSubdomain"></a>

You can migrate a subdomain to use Amazon Route 53 as the DNS service without migrating the parent domain from another DNS service.

The process has these basic steps:

1. [Determine whether this procedure applies to your use case](#decide-procedure-migrate-subdomain).

1. [Create a Route 53 hosted zone for the subdomain](#CreateZoneMigratedSubdomain).

1. [Get the current DNS configuration from the current DNS service provider for the parent domain](#GetParentDomainResourceRecords).

1. [Add records](#AddMigratedSubdomainRecords) for the subdomain to your Route 53 hosted zone.

1. *API only:* [Confirm that your changes have propagated](#MigratingSubdomainCheckStatus) to all Route 53 DNS servers.
**Note**  
Currently, the only way to verify that changes have propagated is to use the [GetChange](https://docs.aws.amazon.com/Route53/latest/APIReference/API_GetChange.html) API action. Changes generally propagate to all Route 53 name servers within 60 seconds.

1. [Update the DNS configuration with the DNS service provider for the parent domain by adding name server records for the subdomain](#UpdateOldDNS).

## Deciding which procedures to use for creating a subdomain
<a name="decide-procedure-migrate-subdomain"></a>

The procedures in this topic explain how to perform an uncommon task. If you already use Route 53 as the DNS service for your domain and you want to route traffic for a subdomain, such as www.example.com, to your resources, see [Routing traffic for subdomains](dns-routing-traffic-for-subdomains.md).

Use this procedure *only* if you're using another DNS service for a domain, such as example.com, and you want to start using Route 53 as the DNS service for an existing subdomain of that domain, such as www.example.com.

## Creating a hosted zone for the subdomain
<a name="CreateZoneMigratedSubdomain"></a>

To migrate a subdomain from another DNS service to Amazon Route 53 without migrating the parent domain, start by creating a hosted zone for the subdomain. Route 53 stores your subdomain information in this hosted zone. 

For information about how to create a hosted zone using the Route 53 console, see [Creating a public hosted zone](CreatingHostedZone.md).

## Getting your current DNS configuration from your DNS service provider
<a name="GetParentDomainResourceRecords"></a>

Contact your current DNS service provider and request the current DNS configuration. Ask your current DNS service provider how to get a *zone file* or a *records list*. You can use this as a basis for configuring Route 53 as the DNS service for the subdomain. 

What you ask for and the format depends on your current DNS service provider. Ideally, they give you a zone file, which has all the records in your current configuration. These records tell DNS how to route traffic for your domains and subdomains. For example, a record can route traffic for your domain name to a web server in your data center, an Amazon EC2 instance, or a CloudFront distribution. If you can get a zone file, you can edit it to remove records you don't want to migrate to Amazon Route 53. Then import the remaining records into your Route 53 hosted zone. This greatly simplifies the process. 

## Creating records
<a name="AddMigratedSubdomainRecords"></a>

Using the records from your current DNS service provider as a starting point, create matching records in the Amazon Route 53 hosted zone that you created for the subdomain. These records will become the records that DNS uses after you delegate the subdomain to Route 53, as explained in [Updating your DNS service with name server records for the subdomain](#UpdateOldDNS).

**Important**  
Do not create additional name server (NS) or start of authority (SOA) records in the Route 53 hosted zone, and do not delete the existing NS and SOA records. 

To create records using the Route 53 console, see [Working with records](rrsets-working-with.md). To create records using the Route 53 API, use `ChangeResourceRecordSets`. For more information, see [ChangeResourceRecordSets](https://docs.aws.amazon.com/Route53/latest/APIReference/API_ChangeResourceRecordSets.html) in the *[Amazon Route 53 API Reference](https://docs.aws.amazon.com/Route53/latest/APIReference/)*.

## Checking the status of your changes (API only)
<a name="MigratingSubdomainCheckStatus"></a>

Creating a new hosted zone and changing records take time to propagate to the Route 53 DNS servers. If you used [ChangeResourceRecordSets](https://docs.aws.amazon.com/Route53/latest/APIReference/API_ChangeResourceRecordSets.html) to create your records, you can use the `GetChange` action to determine whether your changes have propagated. (`ChangeResourceRecordSets` returns a value for `ChangeId`, which you can include in a subsequent `GetChange` request. `ChangeId` is not available if you created the records by using the console.) For more information, see [GET GetChange](https://docs.aws.amazon.com/Route53/latest/APIReference/API_GetChange.html) in the *Amazon Route 53 API Reference*.

**Note**  
Changes generally propagate to all Route 53 name servers within 60 seconds.

## Updating your DNS service with name server records for the subdomain
<a name="UpdateOldDNS"></a>

After your changes to Amazon Route 53 records have propagated (see [Checking the status of your changes (API only)](#MigratingSubdomainCheckStatus)), update the DNS service for the parent domain by adding NS records for the subdomain. This delegates the subdomain to Route 53. For example, suppose example.com is hosted with another DNS service and you're migrating test.example.com to Route 53. You must update the DNS service for example.com with the NS records that Route 53 assigned to the new hosted zone. 

**To update your DNS service with name server records for the subdomain**

1. Using the method provided by your DNS service, back up the zone file for the parent domain.

1. If your previous DNS provider lets you change TTL settings for their name servers, change the settings to 900 seconds. This limits the time during which client requests try to resolve domain names using obsolete name servers. If the current TTL is 172800 seconds (two days), you still need to wait two days for resolvers and clients to stop caching DNS records. After the TTL settings expire, you can safely delete the records stored at the previous provider and make changes only to Route 53.

1. In the Route 53 console, get the name servers for your Route 53 hosted zone:

   1. Sign in to the AWS Management Console and open the Route 53 console at [https://console.aws.amazon.com/route53/](https://console.aws.amazon.com/route53/).

   1. In the navigation pane, click **Hosted zones**.

   1. On the **Hosted zones** page, choose the radio button (not the name) for the hosted zone, then choose **View details**.

   1. On the details page for the hosted zone, choose **Hosted zone details**.

   1. Make note of the four servers listed for **Name servers**.

   Alternatively, you can use the `GetHostedZone` action. For more information, see [GetHostedZone](https://docs.aws.amazon.com/Route53/latest/APIReference/API_GetHostedZone.html) in the *Amazon Route 53 API Reference*.

1. Using the method provided by the DNS service of the parent domain, add NS records for the subdomain to the zone file. Name the NS records with the subdomain name. For the values, specify the four Route 53 name servers linked to the hosted zone you created in Step 2. Different DNS services use different terms. You might need to contact support to learn how to do this. 
**Important**  
Do not add a start of authority (SOA) record to the zone file for the parent domain. Because the subdomain will use Route 53, the DNS service for the parent domain is not the authority for the subdomain.   
If your DNS service automatically added an SOA record for the subdomain, delete the record for the subdomain. However, do not delete the SOA record for the parent domain.

   Changes to DNS resolvers can take 48 hours or more to propagate. During this period, DNS resolvers might still answer with the name servers for the DNS service of the parent domain. Also, client computers might still have the previous name servers for the subdomain in their cache.

1. After the registrar's TTL settings for the domain expire (see Step 2), delete these records from the zone file for the parent domain:
   + The records that you added to Route 53 as described in [Creating records](#AddMigratedSubdomainRecords).
   + Your DNS service's NS records. When you finish deleting NS records, the only NS records in the zone file will be the ones you created in Step 4.