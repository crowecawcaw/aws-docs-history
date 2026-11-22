

# Choose how to move the alternate domain name

Depending on your situation, choose from the following ways to move the alternate domain name:

**The target is a distribution tenant**  
When you create or update the target distribution tenant, set `OnDomainTakeover` to `allow`. This works whether the source is in the same AWS account or a different one, and the source doesn't need to be disabled. For more information, see [Move domains when you create or update a distribution tenant](#alternate-domain-names-move-takeover).  
To move a domain that's serving traffic, use **update-domain-association** instead, which checks that a certificate covers the domain. For more information, see [Migrate a live domain without downtime](#alternate-domain-names-move-live).

**The source and target distributions (standard or tenant) are in the same AWS account**  
Use the **update-domain-association** command in the AWS Command Line Interface (AWS CLI) to move the alternate domain name.   
This command works for all same-account moves, including when the alternate domain name is an apex domain (also called a *root domain*, like example.com). For same-account moves, it doesn't require a DNS record that points to the target.

**The source and target distributions (standard or tenant) are in different AWS accounts**  
Use the **update-domain-association** command. The source standard distribution or distribution tenant can be enabled, so viewers keep reaching the domain during the move. A DNS record must prove that you control the alternate domain name, as described in [Set up the target standard distribution or distribution tenant](alternate-domain-names-move-create-target.md). This works for apex domains too.  
You can also use a wildcard to move the alternate domain name. For more information, see [Use a wildcard to move an alternate domain name](#alternate-domain-names-move-use-wildcard). For additional help, see [Contact AWS Support to move an alternate domain name](#alternate-domain-names-move-contact-support).

**Note**  
We recommend that you use **update-domain-association**. You can use the **associate-alias** command, but this command only supports standard distributions. See [AssociateAlias](https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_AssociateAlias.html) in the *Amazon CloudFront API Reference*.

------
#### [ update-domain-association (standard distributions and distribution tenants) ]

**To use `update-domain-association` to move an alternate domain name**

1. Use the `update-domain-association` command, as shown in the following example. 

   1. Replace {{example.com}} with the alternate domain name, and specify the ID of the target standard distribution or distribution tenant. 

   1. Run this command using credentials that are in the same AWS account as the target standard distribution or distribution tenant.
**Note the following restrictions**  
In addition to the `cloudfront:UpdateDomainAssociation` permission, you must have the `cloudfront:UpdateDistribution` permission to update a standard distribution. To update a distribution tenant, you must have the `cloudfront:UpdateDistributionTenant` permission.
If the source and target distributions (standard or tenant) are in different AWS accounts, a DNS record must point the domain to the target, as described in [Set up the target standard distribution or distribution tenant](alternate-domain-names-move-create-target.md). The source can be enabled.
If the source and target are in different AWS accounts, and the source AWS account also serves the domain with `anycast-ip-list-only`, the move fails with `InvalidAssociation`. For more information, see [Serve domains on specific IP addresses with address-based selection](address-based-selection.md).
If the target is a distribution tenant, it doesn't already serve the domain with `anycast-ip-list-only`.
The target distribution must be set up as described in [Set up the target standard distribution or distribution tenant](alternate-domain-names-move-create-target.md).

   **Request**

   ```
   aws cloudfront update-domain-association \
     --domain "{{www.example.com}}" \
     --target-resource DistributionTenantId=dt_9Fd3xTZq7Hl2KABC \
     --if-match E3UN6WX5ABC123
   ```

   **Response**

   ```json
   {
       "ETag": "E7Xp1Y3N9DABC",
       "Domain": "www.example.com",
       "ResourceId": "dt_9Fd3xTZq7Hl2KABC"
   }
   ```

   This command removes the alternate domain name from the source standard distribution or distribution tenant and adds it to the target standard distribution or distribution tenant.

1. After the target distribution is fully deployed, update your DNS configuration to point your domain name to the CloudFront routing endpoint. For example, your DNS record would point your alternate domain name (`www.example.com`) to the CloudFront provided domain name d111111abcdef8.cloudfront.net. If the target is a distribution tenant, specify the connection group endpoint. For more information, see [Point domains to CloudFront](managed-cloudfront-certificates.md#point-domains-to-cloudfront).

------
#### [ associate-alias (standard distributions only) ]

**To use `associate-alias` to move an alternate domain name**

1. Use the `associate-alias` command, as shown in the following example. 

   1. Replace {{www.example.com}} with the alternate domain name, and {{EDFDVBD6EXAMPLE}} with the target standard distribution ID. 

   1. Run this command using credentials that are in the same AWS account as the target standard distribution.
**Note the following restrictions**  
You must have `cloudfront:AssociateAlias` and `cloudfront:UpdateDistribution` permissions on the target standard distribution.
If the source and target standard distribution are in the same AWS account, you must have `cloudfront:UpdateDistribution` permission on the source standard distribution.
If the source standard distribution and target standard distribution are in different AWS accounts, you must disable the source standard distribution first.
The target standard distribution must be set up as described in [Set up the target standard distribution or distribution tenant](alternate-domain-names-move-create-target.md).
You must create the DNS TXT record that associates the alternate domain name with the target standard distribution, even if the source and target standard distributions are in the same AWS account. Otherwise, the command fails with `Invalid or missing alias DNS TXT records`.

      **Request**

      ```
      aws cloudfront associate-alias \
      --alias {{www.example.com}} \
      --target-distribution-id {{EDFDVBD6EXAMPLE}}
      ```

      This command removes the alternate domain name from the source standard distribution and moves it to the target standard distribution.

1. After the target standard distribution is fully deployed, update your DNS configuration to point the alternate domain name’s DNS record to the distribution domain name of the target standard distribution. For example, your DNS record would point your alternate domain name (`www.example.com`) to the CloudFront provided domain name d111111abcdef8.cloudfront.net.

For more information, see the [associate-alias](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudfront/associate-alias.html) command in the *AWS CLI Command Reference*.

------

## Migrate a live domain without downtime
<a name="alternate-domain-names-move-live"></a>

To move a domain that's serving traffic, use **update-domain-association**. It moves the domain only if a certificate on the target covers it, so HTTPS keeps working through the move. Prove that you control the domain before the move, and point the domain to the target only after the move. Viewers keep using the source's DNS name until the domain has moved, and CloudFront keeps serving the domain throughout. Because the domain still points to the source, you can also roll back without changing the DNS record that viewers use.

**Important**  
This procedure applies when viewers reach the domain through the shared CloudFront IP addresses. If the source or the target uses Anycast static IPs, a live migration doesn't work the same way. Requests that still arrive on the source's Anycast static IP addresses after the move might fail until viewers pick up the DNS change, so lower the TTL first and update the domain's DNS record as soon as the move completes.

**To migrate a live domain**

1. Lower the TTL of the domain's DNS record, so that viewers pick up the DNS change in step 6 quickly.

1. Make sure that a certificate on the target covers the domain. For a distribution tenant, this can be the distribution tenant's certificate or its multi-tenant distribution's certificate. If no certificate covers the domain, **update-domain-association** doesn't move it.

1. If the source and the target are in different AWS accounts, create a TXT record that associates the domain with the target. Leave the DNS record that viewers use, such as a CNAME or alias record, pointing to the source. The DNS check passes on a record that points to the resource that you move the domain to, and a record that points to a different CloudFront resource doesn't block the move. So the TXT record lets you move the domain to the target, and a CNAME record that viewers use lets you move it back to the source, without a DNS change in between.

   If the source and the target are in the same AWS account, skip this step. **update-domain-association** doesn't check DNS for moves within one AWS account, in either direction.

   The name of the TXT record depends on the type of domain. The value is the CloudFront domain name of the target standard distribution, or the routing endpoint of the target distribution tenant's connection group, such as d111111abcdef8.cloudfront.net.


<table>
<thead>
  <tr><th>Domain type</th><th>Domain</th><th>TXT record</th></tr>
</thead>
<tbody>
  <tr><td>Subdomain</td><td><code>www.example.com</code></td><td><code>_www.example.com TXT d111111abcdef8.cloudfront.net</code></td></tr>
  <tr><td>Apex (root) domain</td><td><code>example.com</code></td><td><code>_.example.com TXT d111111abcdef8.cloudfront.net</code></td></tr>
  <tr><td>Wildcard domain</td><td><code>*.example.com</code></td><td><code>_*.example.com TXT d111111abcdef8.cloudfront.net</code></td></tr>
</tbody>
</table>


1. Using credentials for the AWS account that owns the target, get the target's current ETag, and then move the domain. Replace the IDs, the ETag, and the domain with your own.

   ```bash
   aws cloudfront get-distribution-tenant --id {{dt_9Fd3xTZq7Hl2KABC}}
   
   aws cloudfront update-domain-association \
     --domain "{{www.example.com}}" \
     --target-resource DistributionTenantId={{dt_9Fd3xTZq7Hl2KABC}} \
     --if-match {{E3UN6WX5ABC123}}
   ```

   If the target is a standard distribution, use **get-distribution** and specify `DistributionId={{EDFDVBD6EXAMPLE}}` for `--target-resource`. When the change reaches the edge locations, CloudFront routes requests for the domain to the target, including requests that still arrive through the source's DNS name.

1. After the target is deployed, check that it serves the domain as expected. If it doesn't, move the domain back by running **update-domain-association** again with the source as the target resource, using credentials for the source's AWS account. You don't need to change DNS first. For a move between AWS accounts, both records from step 3 are already in place, so the move back passes on the CNAME record that viewers use, which points to the source, and the TXT record that points to the target doesn't block it. If you already pointed the domain to the target in step 6, point it back to the source first.

   If viewers reach the domain through an alias record, as is common for an apex domain, the alias record doesn't pass the DNS check, so the TXT record is the only proof that you control the domain. Before you move the domain back to a source in a different AWS account, update the TXT record from step 3 to associate the domain with the source.

1. In your DNS configuration, point the domain to the target. For a distribution tenant, use the routing endpoint of its connection group. For more information, see [Point domains to CloudFront](managed-cloudfront-certificates.md#point-domains-to-cloudfront). If you need to roll back after this step, first point the domain back to the source, and then move the domain back as described in step 5.

1. After the old DNS TTL has passed and you no longer need to roll back, you can delete the TXT record, if you created one, and the source's configuration for the domain.

The target's cache starts empty, so your origin receives more requests right after the move. To limit the impact, move a few domains at a time.

## Move domains when you create or update a distribution tenant
<a name="alternate-domain-names-move-takeover"></a>

When you create or update a distribution tenant, you can move domains that are already associated with another standard distribution or distribution tenant to the distribution tenant in the same request. To do this, set `OnDomainTakeover` in the [CreateDistributionTenant](https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_CreateDistributionTenant.html) or [UpdateDistributionTenant](https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_UpdateDistributionTenant.html) request. Valid values are:
+ `reject` (default) – If a domain in the request is already associated with another standard distribution or distribution tenant, the request fails with `CNAMEAlreadyExists`.
+ `allow` – CloudFront moves each domain in the request that's already associated with another standard distribution or distribution tenant to this distribution tenant.

Unlike **update-domain-association**, which moves one domain at a time to an existing resource, this moves up to 5 domains as part of creating or updating the distribution tenant.

CloudFront removes the domains from their sources and creates or updates the distribution tenant in one operation. If CloudFront can't move one of the domains, the request fails and no domains move.

For each domain that CloudFront moves, the following must be true:
+ A DNS record proves that you control the domain and points the domain to this distribution tenant. Usually, this is the domain's CNAME record. Use one of the following records:
  + A CNAME record that points the domain to the routing endpoint of the distribution tenant's connection group.
  + An A record that resolves the domain to the Anycast static IP addresses of the distribution tenant's connection group.
  + A TXT record that associates the domain with the routing endpoint of the distribution tenant's connection group.

    The name of the TXT record depends on the type of domain. The value is the CloudFront domain name of the target standard distribution, or the routing endpoint of the target distribution tenant's connection group, such as d111111abcdef8.cloudfront.net.


<table>
<thead>
  <tr><th>Domain type</th><th>Domain</th><th>TXT record</th></tr>
</thead>
<tbody>
  <tr><td>Subdomain</td><td><code>www.example.com</code></td><td><code>_www.example.com TXT d111111abcdef8.cloudfront.net</code></td></tr>
  <tr><td>Apex (root) domain</td><td><code>example.com</code></td><td><code>_.example.com TXT d111111abcdef8.cloudfront.net</code></td></tr>
  <tr><td>Wildcard domain</td><td><code>*.example.com</code></td><td><code>_*.example.com TXT d111111abcdef8.cloudfront.net</code></td></tr>
</tbody>
</table>


  An apex domain, such as `example.com`, can't have a CNAME record, and an alias record that resolves the domain to the shared CloudFront IP addresses doesn't prove that you control the domain. For an apex domain, use a TXT record, or an A record that resolves to the Anycast static IP addresses of the connection group.

  CloudFront checks DNS for every domain that it moves, including when the source and the distribution tenant are in the same AWS account.
+ The source isn't owned by an AWS account that CloudFront blocks from moving domains, or by another AWS service.
+ If the source is in a different AWS account, that AWS account doesn't also serve the domain with `anycast-ip-list-only`. Otherwise, the request fails with `InvalidAssociation`. For more information, see [Serve domains on specific IP addresses with address-based selection](address-based-selection.md).

A move can remove the last domain from the source standard distribution or distribution tenant.

A certificate isn't required to move a domain. If a certificate on the distribution tenant or its multi-tenant distribution covers the domain, CloudFront serves the domain over HTTPS as soon as it moves. If no certificate covers the domain, CloudFront still moves it and serves it over HTTP only, so HTTPS requests for the domain fail until you add a certificate. For more information, see [Serve distribution tenant domains without a certificate](tenant-domains-without-certificate.md).

If you request a CloudFront managed certificate for a domain that you're moving, CloudFront moves the domain when you make the request, and HTTPS requests for the domain fail until the certificate is issued. If you request the managed certificate with self-hosted validation and CloudFront can't verify the DNS record for a domain, the request fails and no domains move.

**Important**  
CloudFront doesn't keep a record of where a moved domain came from. If you later remove the domain from the distribution tenant, delete the distribution tenant, or roll back the change, for example in a CloudFormation stack rollback, CloudFront doesn't return the domain to the source. CloudFront stops serving the domain until you add it to a resource again.  
To undo a move, move the domain back to the original resource instead of removing it from the distribution tenant. For more information, see [Move a domain back to its original resource](#alternate-domain-names-move-takeover-undo).

**To move domains when you update a distribution tenant**

1. If the source serves a domain over HTTPS, add a certificate that covers the domain to the distribution tenant or its multi-tenant distribution.
**Warning**  
If no certificate covers the domain, HTTPS requests for the domain start failing when it moves. To have CloudFront check this for you, move the domain with **update-domain-association** instead. For more information, see [Migrate a live domain without downtime](#alternate-domain-names-move-live).

1. Set up the DNS record for each domain that you're moving, as described earlier in this topic. For example, create a CNAME record that points `www.example.com` to the routing endpoint of the target distribution tenant's connection group. For an apex domain, create a TXT record, or an A record that resolves the domain to the Anycast static IP addresses of the connection group.
**Note**  
Until the move completes, the source continues to serve the domain.

1. Update the distribution tenant with the full list of its domains, including the domains that you're moving, and set `--on-domain-takeover` to `allow`.

   ```bash
   aws cloudfront update-distribution-tenant \
     --id {{dt_9Fd3xTZq7Hl2KABC}} \
     --if-match {{E3UN6WX5ABC123}} \
     --domains '[{"Domain": "{{app.example.com}}"}, {"Domain": "{{www.example.com}}"}]' \
     --on-domain-takeover allow
   ```

   If the request succeeds, the response lists the moved domains in `Domains`. CloudFront doesn't return `OnDomainTakeover` in the response, and you must set it again in each request that moves domains.

To move domains while you create a distribution tenant, add `--on-domain-takeover allow` to the **create-distribution-tenant** command.

### Move a domain back to its original resource
<a name="alternate-domain-names-move-takeover-undo"></a>

To undo a move, move the domain from the distribution tenant back to the original standard distribution or distribution tenant instead of removing it from the distribution tenant. Choose one of the following options.

------
#### [ update-domain-association (any original resource) ]

**To move a domain back with `update-domain-association`**

1. If the original resource is in a different AWS account than the distribution tenant, make sure that the original resource is set up as described in [Set up the target standard distribution or distribution tenant](alternate-domain-names-move-create-target.md), including a DNS record that proves that you control the domain. You don't need to disable the distribution tenant that has the domain now.

1. Using credentials for the AWS account that owns the original resource, get the resource's current ETag. Replace the ID with your own.

   ```bash
   aws cloudfront get-distribution --id {{EDFDVBD6EXAMPLE}}
   ```

   If the original resource is a distribution tenant, use **get-distribution-tenant** instead.

1. Move the domain to the original resource. Replace the domain, the resource ID, and the ETag with your own.

   ```bash
   aws cloudfront update-domain-association \
     --domain "{{www.example.com}}" \
     --target-resource DistributionId={{EDFDVBD6EXAMPLE}} \
     --if-match {{E2QWRUHEXAMPLE}}
   ```

   If the original resource is a distribution tenant, specify `DistributionTenantId={{dt_EXAMPLE22222}}` for `--target-resource`.

1. After the original resource is deployed, update the domain's DNS records to point to it. For a standard distribution, use the distribution domain name, such as d111111abcdef8.cloudfront.net. For a distribution tenant, use the routing endpoint of its connection group.

------
#### [ OnDomainTakeover (original resource is a distribution tenant) ]

If the original resource is a distribution tenant, you can also move the domain back the same way that you moved it.

**To move a domain back with `OnDomainTakeover`**

1. Update the domain's DNS records to point to the original distribution tenant, for example with a CNAME record to the routing endpoint of its connection group. For an apex domain, also create a TXT record that associates the domain with the original distribution tenant, unless the domain's A record resolves to the Anycast static IP addresses of its connection group. Until the move completes, the distribution tenant that has the domain now continues to serve it.

1. Using credentials for the AWS account that owns the original distribution tenant, update it with the full list of its domains, including the domain that you're moving back. Replace the ID, the ETag, and the domains with your own.

   ```bash
   aws cloudfront update-distribution-tenant \
     --id {{dt_EXAMPLE22222}} \
     --if-match {{E2QWRUHEXAMPLE}} \
     --domains '[{"Domain": "{{www.example.com}}"}]' \
     --on-domain-takeover allow
   ```

------

If you already removed the domain from the distribution tenant, no resource has the domain. Add it to the original resource again as an alternate domain name, and point the domain's DNS records back to that resource.

## Use a wildcard to move an alternate domain name
<a name="alternate-domain-names-move-use-wildcard"></a>

If the source distribution is in a different AWS account than the target distribution, you can also use a wildcard to move the alternate domain name, instead of **update-domain-association**.

**Note**  
You can't use a wildcard to move an apex domain (like example.com). To move an apex domain, use **update-domain-association**.

**To use a wildcard to move an alternate domain name**
**Note**  
This process involves multiple updates to your distributions. Wait for each distribution to fully deploy the latest change before proceeding to the next step.

1. Update the target distribution to add a wildcard alternate domain name that covers the alternate domain name that you are moving. For example, if the alternate domain name that you’re moving is www.example.com, add the alternate domain name \*.example.com to the target distribution. To do this, the SSL/TLS certificate on the target distribution must include the wildcard domain name. For more information, see [Update a distribution](HowToUpdateDistribution.md).

1. Update the DNS settings for the alternate domain name to point to the domain name of the target distribution. For example, if the alternate domain name that you’re moving is www.example.com, update the DNS record for www.example.com to route traffic to the domain name of the target distribution (for example d111111abcdef8.cloudfront.net).
**Note**  
Even after you update the DNS settings, the alternate domain name is still served by the source distribution because that’s where the alternate domain name is currently configured.

1. Update the source distribution to remove the alternate domain name. For more information, see [Update a distribution](HowToUpdateDistribution.md).

1. Update the target distribution to add the alternate domain name. For more information, see [Update a distribution](HowToUpdateDistribution.md).

1. Use **dig** (or a similar DNS query tool) to validate that the DNS record for the alternate domain name resolves to the domain name of the target distribution.

1. (Optional) Update the target distribution to remove the wildcard alternate domain name.

## Contact AWS Support to move an alternate domain name
<a name="alternate-domain-names-move-contact-support"></a>

If the source and target distributions are in different AWS accounts, and you can't move the alternate domain name yourself, you can contact Support to move it.

**To contact Support to move an alternate domain name**

1. Set up a target distribution, including the DNS TXT record that points to the target distribution. For more information, see [Set up the target standard distribution or distribution tenant](alternate-domain-names-move-create-target.md).

1. [Contact Support](https://console.aws.amazon.com/support/home) to request that they verify that you own the domain, and move the domain to the new CloudFront distribution for you.

1. After the target distribution is fully deployed, update your DNS configuration to point the alternate domain name’s DNS record to the distribution domain name of the target distribution.