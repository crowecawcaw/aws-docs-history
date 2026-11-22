

# Serve domains on specific IP addresses with address-based selection

With address-based selection, CloudFront selects the distribution tenant for a viewer request based on both the domain name and the IP address that the request arrives on. You can use address-based selection to do the following:
+ Serve the same wildcard domain, such as `*.example.com`, from more than one distribution tenant, each on its own Anycast static IP list. Your DNS records decide which IP addresses a hostname resolves to, and so which distribution tenant serves it.
+ Serve a wildcard domain only on your own Anycast static IP addresses, so that CloudFront doesn't serve it on other IP addresses.

You can use address-based selection only with distribution tenants, in connection groups that use an Anycast static IP list. For more information, see [Create custom connection group (optional)](custom-connection-group.md) and [Request Anycast static IPs to use for allowlisting](request-static-ips.md).

**Topics**
+ [How address-based selection works](#address-based-selection-how-it-works)
+ [Use cases](#address-based-selection-use-cases)
+ [Address-based selection requirements and restrictions](#address-based-selection-requirements)
+ [Required permissions](#address-based-selection-permissions)
+ [Set up address-based selection](#address-based-selection-set-up)
+ [Example: Serve three service tiers under one wildcard domain](#address-based-selection-example)
+ [Troubleshoot address-based selection](#address-based-selection-troubleshooting)

## How address-based selection works
<a name="address-based-selection-how-it-works"></a>

A distribution tenant gets its IP addresses from its connection group. For each domain on a distribution tenant, the `ServeOn` setting controls which IP addresses the distribution tenant serves that domain on:
+ `any` (default) – The distribution tenant serves the domain on any CloudFront IP address. This includes the shared CloudFront IP addresses and your Anycast static IP lists. This is how CloudFront serves domains when you don't use address-based selection.
+ `anycast-ip-list-only` – The distribution tenant serves the domain only on the IP addresses of the Anycast static IP list that's associated with its connection group.

CloudFront selects the resource that serves a request based on the IP address that the request arrives on. When a request arrives on the IP addresses of an Anycast static IP list, CloudFront selects the resource in the following order:

1. A standard distribution or distribution tenant whose alternate domain name exactly matches the requested domain.

1. The distribution tenant that serves a matching wildcard domain with `anycast-ip-list-only` on that Anycast static IP list. If more than one wildcard domain matches, CloudFront selects the most specific one.

1. A standard distribution or distribution tenant whose wildcard alternate domain name matches the requested domain.

For requests that arrive on any other IP address, CloudFront ignores domains that are set to `anycast-ip-list-only`. If no resource serves the requested domain on the IP address that the request arrived on, CloudFront rejects the request.

**Important**  
When you set a domain that already receives traffic to `anycast-ip-list-only`, the distribution tenant stops serving it on every other IP address. Before you update the distribution tenant, point the DNS record for every hostname under the domain to the connection group's routing endpoint or Anycast static IP addresses.

## Use cases
<a name="address-based-selection-use-cases"></a>

Address-based selection supports the following use cases:

**Service tiers**  
Serve paid tiers from dedicated IP addresses, each with its own configuration, and serve a free tier on the shared CloudFront IP addresses, all under the same wildcard domain.

**Sharding**  
Split a large customer base across several distribution tenants, each with its own IP addresses, origins, and configuration. To move a customer to a different shard, you change only that customer's DNS record.

## Address-based selection requirements and restrictions
<a name="address-based-selection-requirements"></a>

To serve a domain with `anycast-ip-list-only`, the following must be true:
+ The distribution tenant's connection group uses an Anycast static IP list, and no other connection group uses that list.
+ The domain is a wildcard domain with one or two labels before the top-level domain, such as `*.example.com` or `*.app.example.com`. You can't use an exact domain name, such as `www.example.com` or `example.com`, or a wildcard of a public suffix, such as `*.co.uk`.
+ A certificate that you provide covers the domain, or a DNS record for the domain points to the connection group. The certificate can be the distribution tenant's own certificate or its multi-tenant distribution's certificate. Without a certificate, CloudFront verifies the DNS record instead and serves the domain over HTTP only. For more information, see [Serve distribution tenant domains without a certificate](tenant-domains-without-certificate.md). `ServeOn` doesn't change the domain control and certificate requirements for a domain. For more information, see [Domain considerations (distribution tenant)](managed-cloudfront-certificates.md#tenant-domain-considerations).
**Note**  
CloudFront managed certificates don't support domains that are set to `anycast-ip-list-only`. CloudFront doesn't include these domains in a managed certificate request, so a managed certificate on the distribution tenant doesn't cover them.

Note the following restrictions:
+ A distribution tenant can serve up to 10 domains with `anycast-ip-list-only`.
+ On a given Anycast static IP list, only one distribution tenant can serve a domain with `anycast-ip-list-only`. You can serve the same domain from other distribution tenants that use other Anycast static IP lists.
+ A distribution tenant can't serve the same domain with both `any` and `anycast-ip-list-only`.
+ The rule that an alternate domain name can be associated with only one CloudFront resource doesn't apply to domains that are set to `anycast-ip-list-only`. Another standard distribution or distribution tenant can use the same domain as an alternate domain name.
+ `anycast-ip-list-only` applies to every IP address in the Anycast static IP list. You can't serve a domain on only some of the IP addresses in a list.
+ When a distribution tenant in the connection group serves a domain with `anycast-ip-list-only`, you can't change the connection group's Anycast static IP list or IPv6 setting, change the Anycast static IP list itself, such as its IP address type, or associate the Anycast static IP list with another connection group. To make these changes, first remove the `anycast-ip-list-only` domains from the distribution tenants in the connection group, and remove the connection group's viewer fallback if it has one. For more information, see [Viewer fallback requirements and restrictions](connection-group-viewer-fallback.md#connection-group-viewer-fallback-requirements).
+ To move a distribution tenant that serves domains with `anycast-ip-list-only` to another connection group, the new connection group must also use its own Anycast static IP list, and no other distribution tenant can already serve the domains on that list. After the move, the distribution tenant serves the domains on the new list. You can't move the distribution tenant to a connection group that doesn't use an Anycast static IP list, such as the default connection group.
+ To move a domain that's set to `anycast-ip-list-only` from one distribution tenant to another distribution tenant on the same Anycast static IP list, first update the source distribution tenant to remove the domain, and then update the target distribution tenant to add it. Between the two updates, no distribution tenant serves the domain on that list.

## Required permissions
<a name="address-based-selection-permissions"></a>

To set up address-based selection, you need permission to create connection groups and to create and update distribution tenants. The following policy grants the permissions for the procedure in this topic.

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "cloudfront:CreateConnectionGroup",
            "Resource": "arn:aws:cloudfront::{{123456789012}}:connection-group/*"
        },
        {
            "Effect": "Allow",
            "Action": [
                "cloudfront:CreateDistributionTenant",
                "cloudfront:UpdateDistributionTenant",
                "cloudfront:GetDistributionTenant"
            ],
            "Resource": "arn:aws:cloudfront::{{123456789012}}:distribution-tenant/*"
        }
    ]
}
```

## Set up address-based selection
<a name="address-based-selection-set-up"></a>

The following procedure uses the AWS CLI to serve `*.example.com` from a distribution tenant only on the IP addresses of an Anycast static IP list. Before you begin, you need a multi-tenant distribution, an Anycast static IP list, and an ACM certificate in the US East (N. Virginia) (`us-east-1`) Region that covers the domain.

**To set up address-based selection**

1. Create a connection group that uses your Anycast static IP list. Replace the Anycast static IP list ID with your own.

   ```bash
   aws cloudfront create-connection-group \
       --name example-dedicated-group \
       --anycast-ip-list-id {{aip_EXAMPLE11111}}
   ```

   In the response, note the connection group `Id` and `RoutingEndpoint`. The connection group's `Status` is `InProgress` until CloudFront deploys it, which can take a few minutes.

   ```json
   {
       "ETag": "E2QWRUHEXAMPLE",
       "ConnectionGroup": {
           "Id": "cg_EXAMPLE11111",
           "Name": "example-dedicated-group",
           "Arn": "arn:aws:cloudfront::123456789012:connection-group/cg_EXAMPLE11111",
           "RoutingEndpoint": "d111111abcdef8.cloudfront.net",
           "AnycastIpListId": "aip_EXAMPLE11111",
           "Ipv6Enabled": false,
           "Status": "InProgress",
           "Enabled": true,
           "IsDefault": false
       }
   }
   ```

1. Create a distribution tenant in the connection group, and set `ServeOn` to `anycast-ip-list-only` for the domain. Replace the multi-tenant distribution ID, the connection group ID, and the certificate ARN with your own.

   ```bash
   aws cloudfront create-distribution-tenant \
       --distribution-id {{EDFDVBD6EXAMPLE}} \
       --name example-dedicated \
       --connection-group-id {{cg_EXAMPLE11111}} \
       --domains '[{"Domain": "*.example.com", "ServeOn": "anycast-ip-list-only"}]' \
       --customizations '{"Certificate": {"Arn": "arn:aws:acm:us-east-1:{{123456789012}}:certificate/{{a1b2c3d4-5678-90ab-cdef-EXAMPLE11111}}"}}'
   ```

   The `Domains` list in the response shows the `ServeOn` value for each domain.

   ```json
   {
       "ETag": "E3QWRUHEXAMPLE",
       "DistributionTenant": {
           "Id": "dt_EXAMPLE22222",
           "DistributionId": "EDFDVBD6EXAMPLE",
           "Name": "example-dedicated",
           "Domains": [
               {
                   "Domain": "*.example.com",
                   "ServeOn": "anycast-ip-list-only",
                   "Status": "active"
               }
           ],
           "ConnectionGroupId": "cg_EXAMPLE11111",
           "Enabled": true,
           "Status": "InProgress"
       }
   }
   ```

   To change an existing distribution tenant instead, use the **update-distribution-tenant** command with the distribution tenant's `--id`, its current ETag in `--if-match`, and the same `--domains` and `--connection-group-id` values. Include every domain on the distribution tenant in `--domains`.

1. In your DNS configuration, create a CNAME record for each hostname that points to the connection group's routing endpoint. The routing endpoint resolves to the IP addresses of the connection group's Anycast static IP list.

   ```
   app1.example.com.  300  IN  CNAME  d111111abcdef8.cloudfront.net.
   ```

1. After the distribution tenant's status changes to `Deployed`, confirm that the hostname resolves to an IP address on your Anycast static IP list, and that CloudFront serves the request.

   ```bash
   dig +short app1.example.com
   curl -sI https://app1.example.com
   ```

## Example: Serve three service tiers under one wildcard domain
<a name="address-based-selection-example"></a>

A software-as-a-service (SaaS) provider hosts customer apps under `*.example.com` and offers premium, pro, and free tiers. Premium and pro customers get dedicated IP addresses and their own configuration, and free customers share CloudFront's IP addresses. The provider creates three distribution tenants that all serve `*.example.com`. The following table shows each distribution tenant's connection group and `ServeOn` setting, and the IP addresses that it serves requests on.


| Distribution tenant | Connection group | `ServeOn` | Serves requests that arrive on | 
| --- | --- | --- | --- | 
| premium | Uses the premium Anycast static IP list | anycast-ip-list-only | The premium list | 
| pro | Uses the pro Anycast static IP list | anycast-ip-list-only | The pro list | 
| free | Default connection group | any | Every other CloudFront IP address | 

Each customer's hostname is a CNAME record to the routing endpoint of the connection group for that customer's tier. A request for `customer1.example.com` that resolves to the premium list goes to the premium distribution tenant. A request for `customer2.example.com` that resolves to a shared CloudFront IP address goes to the free distribution tenant. To move a customer to another tier, the provider changes only that customer's DNS record.

**Note**  
Because the free distribution tenant serves `*.example.com` on any IP address, it also receives requests for premium or pro hostnames whose DNS records point to the shared CloudFront IP addresses, for example because of an incorrect record. Those requests get the free tier's configuration instead of being rejected. If you want such requests to fail, serve every tier on its own Anycast static IP list.

## Troubleshoot address-based selection
<a name="address-based-selection-troubleshooting"></a>

The following are common issues with address-based selection and how to resolve them.

**CloudFront rejects requests for the domain**  
The hostname resolves to an IP address that no distribution tenant serves the domain on. Use **dig** to see which IP addresses the hostname resolves to, and check that its DNS record points to the routing endpoint of the connection group whose distribution tenant serves the domain.

**The wrong distribution tenant serves requests**  
CloudFront selects the distribution tenant from the IP address that the request arrives on, so check the hostname's DNS record first. If the record points to the shared CloudFront IP addresses, a resource that serves the domain with `any` receives the request. If another standard distribution or distribution tenant has the exact hostname as an alternate domain name, that resource receives the request.  
The **get-distribution-tenant-by-domain** command doesn't find distribution tenants by domains that are set to `anycast-ip-list-only`. It returns only a distribution tenant that has the domain as a regular alternate domain name. To see which distribution tenant serves a domain on an Anycast static IP list, list the distribution tenants in the connection group and check their `Domains`:  

```bash
aws cloudfront list-distribution-tenants \
    --association-filter ConnectionGroupId={{cg_EXAMPLE11111}}
```

**Creating or updating a distribution tenant fails**  
Check the following:  
+ Another distribution tenant already serves the domain with `anycast-ip-list-only` on the same Anycast static IP list.
+ The connection group doesn't use an Anycast static IP list, or another connection group also uses the list.
+ The domain isn't a supported wildcard domain. Or no certificate on the distribution tenant or its multi-tenant distribution covers the domain, and CloudFront couldn't verify the domain's DNS records instead. A CloudFront managed certificate doesn't cover domains that are set to `anycast-ip-list-only`.