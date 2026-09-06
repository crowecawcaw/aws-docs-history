

# Deleting a public hosted zone
<a name="DeleteHostedZone"></a>

This section explains how to delete a public hosted zone using the Amazon Route 53 console.

You can delete a hosted zone only if it has no records other than the default SOA and NS records. If your hosted zone has other records, delete them first. This prevents you from removing a hosted zone that still has records in use.

**Topics**
+ [Preventing traffic from being routed to your domain](#delete-public-hosted-zone-stop-routing)
+ [Deleting public hosted zones that were created by another service](#delete-public-hosted-zone-created-by-another-service)
+ [Using the Route 53 console to delete a public hosted zone](#delete-public-hosted-zone-procedure)

## Preventing traffic from being routed to your domain
<a name="delete-public-hosted-zone-stop-routing"></a>

If you want to keep your domain registration but stop routing internet traffic to your website or web application, we suggest that you delete *records* in the hosted zone instead of deleting the hosted zone.

**Important**  
If you delete a hosted zone, you can't undo it. You must create a new hosted zone and update the name servers for your domain, which can take up to 48 hours to take effect. Also, if you delete a hosted zone, someone could hijack the domain and route traffic to their own resources using your domain name.  
If you gave a subdomain its own hosted zone and you want to delete that child hosted zone, you must also update the parent hosted zone by deleting the NS record with the same name as the child hosted zone. For example, if you want to delete the hosted zone acme.example.com, you must also delete the NS record acme.example.com in the example.com hosted zone. We suggest that you delete the NS record first, and wait for the TTL on that NS record to expire before you delete the child hosted zone. This ensures that no one can hijack the child hosted zone while DNS resolvers still have the child hosted zone's name servers cached.

If you want to avoid the monthly charge for the hosted zone, you can move DNS service for the domain to a free DNS service. When you move DNS service, you must update the name servers for the domain. If the domain is registered with Route 53, see [Adding or changing name servers and glue records for a domain](domain-name-servers-glue-records.md) for information about how to replace Route 53 name servers with name servers for the new DNS service. If the domain is registered with another registrar, use the method provided by that registrar to update name servers for the domain. For more information, search the internet for "free DNS service."

## Deleting public hosted zones that were created by another service
<a name="delete-public-hosted-zone-created-by-another-service"></a>

If another service created a hosted zone, you can't delete it using the Route 53 console. Instead, use the right process for that service:
+ **AWS Cloud Map** – To delete a hosted zone that AWS Cloud Map created when you created a public DNS namespace, delete the namespace. AWS Cloud Map deletes the hosted zone automatically. For more information, see [Deleting namespaces](https://docs.aws.amazon.com/cloud-map/latest/dg/deleting-namespaces.html) in the *AWS Cloud Map Developer Guide*.
+ **Amazon Elastic Container Service (Amazon ECS) Service Discovery** – To delete a public hosted zone that Amazon ECS created when you created a service using service discovery, delete the Amazon ECS services that are using the namespace, and delete the namespace. For more information, see [Deleting a service](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/delete-service.html) in the *Amazon Elastic Container Service Developer Guide*.

## Using the Route 53 console to delete a public hosted zone
<a name="delete-public-hosted-zone-procedure"></a>

To use the Route 53 console to delete a public hosted zone, perform the following procedure.

**To delete a public hosted zone using the Route 53 console**

1. Sign in to the AWS Management Console and open the Route 53 console at [https://console.aws.amazon.com/route53/](https://console.aws.amazon.com/route53/).

1. In the navigation pane, choose **Hosted zones**, and choose the highlighted link for the hosted zone you want to delete.

1. Confirm that the hosted zone that you want to delete contains only an NS and an SOA record. If it contains additional records, delete them. You will also need to disable DNSSEC signing:
**Note**  
If you attempt to delete the hosted zone without completing these requirements, Route 53 will return an error:  
If DNSSEC signing is enabled: The specified hosted zone contains DNSSEC Key Signing Keys and so cannot be deleted
If other resource record sets exist (other than the default SOA and NS records): The specified hosted zone contains non-required resource record sets and so cannot be deleted

   1. On the hosted zone detail page, in the **Records** list, if the list of records includes any records for which the value of the **Type** column is something other than NS or SOA, choose the row, and choose **Delete**.

     To select multiple, consecutive records, choose the first row, press and hold the **Shift** key, and choose the last row. To select multiple, non-consecutive records, choose the first row, press and hold the **Ctrl** key, and choose the remaining rows. 
**Note**  
If you created any NS records for subdomains in the hosted zone, delete those records, too.

1. Go back to the the **Hosted zones** page, and choose the row for the hosted zone that you want to delete.

1. Choose **Delete**.

1. Type the confirmation key and choose **Delete**.

1. If you want to make the domain unavailable on the internet, we recommend that you transfer DNS service to a free DNS service and then delete the Route 53 hosted zone. This prevents future DNS queries from possibly being misrouted. 

   If the domain is registered with Route 53, see [Adding or changing name servers and glue records for a domain](domain-name-servers-glue-records.md) for information about how to replace Route 53 name servers with name servers for the new DNS service. If the domain is registered with another registrar, use the method provided by the registrar to change name servers for the domain.
**Note**  
If you're deleting a hosted zone for a subdomain (acme.example.com), you don't need to change name servers for the domain (example.com).