

# Creating a subdomain that uses Amazon Route 53 as the DNS service without migrating the parent domain
<a name="CreatingNewSubdomain"></a>

You can create a subdomain that uses Amazon Route 53 as the DNS service without migrating the parent domain from another DNS service.

The process has these basic steps:

1. [Determine whether this procedure applies to your use case](#decide-procedure-create-subdomain).

1. [Create a Route 53 hosted zone for the subdomain](#CreateZoneNewSubdomain).

1. [Add records](#AddNewSubdomainRecords) for the new subdomain to your Route 53 hosted zone.

1. *API only:* [Confirm that your changes have propagated](#CheckStatusNewSubdomain) to all Route 53 DNS servers.
**Note**  
Currently, the only way to verify that changes have propagated is to use the [GetChange](https://docs.aws.amazon.com/Route53/latest/APIReference/API_GetChange.html) API action. Changes generally propagate to all Route 53 name servers within 60 seconds.

1. [Update the DNS service for the parent domain by adding name server records for the subdomain](#UpdateDNSParentDomain).

## Deciding which procedures to use for creating a subdomain
<a name="decide-procedure-create-subdomain"></a>

These steps explain an uncommon task. If you already use Route 53 as the DNS service for your domain and you want to route traffic for a subdomain, see [Routing traffic for subdomains](dns-routing-traffic-for-subdomains.md).

Use this procedure *only* if you're using another DNS service for a domain, such as example.com, and you want to start using Route 53 as the DNS service for an new subdomain of that domain, such as www.example.com.

## Creating a hosted zone for the new subdomain
<a name="CreateZoneNewSubdomain"></a>

To use Amazon Route 53 as the DNS service for a new subdomain without migrating the parent domain, first create a hosted zone for the subdomain. Route 53 stores your subdomain data in this zone.

For information about how to create a hosted zone using the Route 53 console, see [Creating a public hosted zone](CreatingHostedZone.md).

## Creating records
<a name="AddNewSubdomainRecords"></a>

You can create records using the Amazon Route 53 console or the Route 53 API. The records that you create become the records that DNS uses after you delegate the subdomain to Route 53, as explained in [Updating your DNS service with name server records for the subdomain](#UpdateDNSParentDomain).

**Important**  
Do not create extra name server (NS) or start of authority (SOA) records in the Route 53 hosted zone. Do not delete the existing NS and SOA records. 

To create records using the Route 53 console, see [Working with records](rrsets-working-with.md). To create records using the Route 53 API, use `ChangeResourceRecordSets`. For more information, see [ChangeResourceRecordSets](https://docs.aws.amazon.com/Route53/latest/APIReference/API_ChangeResourceRecordSets.html) in the *[Amazon Route 53 API Reference](https://docs.aws.amazon.com/Route53/latest/APIReference/)*.

## Checking the status of your changes (API only)
<a name="CheckStatusNewSubdomain"></a>

Creating a new hosted zone and changing records take time to propagate to the Route 53 DNS servers. If you used [ChangeResourceRecordSets](https://docs.aws.amazon.com/Route53/latest/APIReference/API_ChangeResourceRecordSets.html) to create your records, you can use the `GetChange` action to determine whether your changes have propagated. (`ChangeResourceRecordSets` returns a value for `ChangeId`, which you can include in a subsequent `GetChange` request. `ChangeId` is not available if you created the records by using the console.) For more information, see [GET GetChange](https://docs.aws.amazon.com/Route53/latest/APIReference/API_GetChange.html) in the *Amazon Route 53 API Reference*.

**Note**  
Changes generally propagate to all Route 53 name servers within 60 seconds.

## Updating your DNS service with name server records for the subdomain
<a name="UpdateDNSParentDomain"></a>

After your changes to Amazon Route 53 records have spread (see [Checking the status of your changes (API only)](#CheckStatusNewSubdomain)), update the DNS service for the parent domain by adding NS records for the subdomain. This delegates the subdomain to Route 53. For example, if example.com uses another DNS service and you created test.example.com in Route 53, update the DNS for example.com with NS records for test.example.com.

**To update your DNS service with name server records for the subdomain**

1. Using the method provided by your DNS service, back up the zone file for the parent domain.

1. In the Route 53 console, get the name servers for your Route 53 hosted zone:

   1. Sign in to the AWS Management Console and open the Route 53 console at [https://console.aws.amazon.com/route53/](https://console.aws.amazon.com/route53/).

   1. In the navigation pane, click **Hosted zones**.

   1. On the **Hosted zones** page, choose the radio button (not the name) for the hosted zone, then choose **View details**.

   1. On the details page for the hosted zone, choose **Hosted zone details**.

   1. Make note of the four servers listed for **Name servers**.

   Alternatively, you can use the `GetHostedZone` action. For more information, see [GetHostedZone](https://docs.aws.amazon.com/Route53/latest/APIReference/API_GetHostedZone.html) in the *Amazon Route 53 API Reference*.

1. Add NS records for the subdomain to the zone file of the parent domain, using the method from the DNS service. In these NS records, specify the four Route 53 name servers linked to the hosted zone that you created in Step 1.

**Important**  
Do not add a start of authority (SOA) record to the zone file for the parent domain. The subdomain uses Route 53, so the parent's DNS service does not control the subdomain.   
If your DNS service added an SOA record for the subdomain, delete it. Do not delete the SOA record for the parent domain.