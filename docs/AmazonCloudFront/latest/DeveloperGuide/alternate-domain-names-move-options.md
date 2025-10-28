# Move the alternate domain

name

Depending on your situation, choose from the following ways to move the alternate
domain name:

**The source and target distributions (standard or tenant) are in the same
AWS account**

Use the **update-domain-association** command in the
AWS Command Line Interface (AWS CLI) to move the alternate domain name.

This command works for all same-account moves, including when the
alternate domain name is an apex domain (also called a _root domain_, like example.com).

**The source and target distributions (standard or tenant) are in different
AWS accounts**

If you have access to the source standard distribution or distribution tenant, the alternate domain name
is _not_ an apex domain, and you are not
already using a wildcard that overlaps with that alternate domain name, use
a wildcard to move the alternate domain name. For more information, see
[Use a wildcard to move an
alternate domain name](#alternate-domain-names-move-use-wildcard "#alternate-domain-names-move-use-wildcard").

If you don’t have access to the AWS account that has the source
standard distribution or distribution tenant, you can try using the
**update-domain-association** command to move the
alternate domain name. The source standard distribution or distribution tenant must be disabled before you
can move the alternate domain name. For additional help, see [Contact AWS Support to
move an alternate domain name](#alternate-domain-names-move-contact-support "#alternate-domain-names-move-contact-support").

###### Note

You can use the **associate-alias** command, but this command only
supports standard distributions. See [AssociateAlias](../../../cloudfront/latest/APIReference/API_AssociateAlias.md "../../../cloudfront/latest/APIReference/API_AssociateAlias.md") in the _Amazon CloudFront API
Reference_.

update-domain-association (standard distributions and distribution tenants)

###### To use `update-domain-association` to move an alternate

domain name

1.  Use the `update-domain-association` command, as shown
    in the following example.

        1. Replace `example.com` with the
         alternate domain name, and specify the ID of the target
         standard distribution or distribution tenant.
        2. Run this command using credentials that are in the same
         AWS account as the target standard distribution or distribution tenant.###### Note the following restrictions



        * In addition to the
         `cloudfront:UpdateDomainAssociation`
         permission, you must have the
         `cloudfront:UpdateDistribution`
         permission to update a standard distribution. To update a distribution tenant,
         you must have the
         `cloudfront:UpdateDistributionTenant`
         permission.
        * If the source and target distributions (standard or
         tenant) are in different AWS accounts, the source must
         be disabled before you can move the domain.
        * The target distribution must be set up as described in
         [Set up the target
         standard distribution or distribution tenant](alternate-domain-names-move-create-target.md "alternate-domain-names-move-create-target.md").

    **Request**

```
aws cloudfront update-domain-association \
  --domain "`www.example.com`" \
  --target-resource DistributionTenantId=dt_9Fd3xTZq7Hl2KABC \
  --if-match E3UN6WX5ABC123
```

**Response**

```
{
    "ETag": "E7Xp1Y3N9DABC",
    "Domain": "www.example.com",
    "ResourceId": "dt_9Fd3xTZq7Hl2KABC"
}
```

This command removes the alternate domain name from the source
standard distribution or distribution tenant and adds it to the target standard distribution or distribution tenant. 2. After the target distribution is fully deployed, update your DNS
configuration to point your domain name to the CloudFront routing
endpoint. For example, your DNS record would point your alternate
domain name (`www.example.com`) to the CloudFront provided
domain name d111111abcdef8.cloudfront.net. If the target is a distribution tenant,
specify the connection group endpoint. For more information, see
[Point domains to CloudFront](managed-cloudfront-certificates.md#point-domains-to-cloudfront "managed-cloudfront-certificates.md#point-domains-to-cloudfront").

associate-alias (standard distributions only)

###### To use `associate-alias` to move an alternate domain

name

1.  Use the `associate-alias` command, as shown in the
    following example.
    1. Replace `www.example.com` with
       the alternate domain name, and
       `EDFDVBD6EXAMPLE` with the
       target standard distribution ID.
    2. Run this command using credentials that are in the same
       AWS account as the target standard distribution.

    ###### Note the following restrictions

        * You must have
         `cloudfront:AssociateAlias` and
         `cloudfront:UpdateDistribution`
         permissions on the target standard distribution.
        * If the source and target standard distribution are in the
         same AWS account, you must have
         `cloudfront:UpdateDistribution`
         permission on the source standard distribution.
        * If the source standard distribution and target standard distribution
         are in different AWS accounts, you must disable
         the source standard distribution first.
        * The target standard distribution must be set up as
         described in [Set up the target
         standard distribution or distribution tenant](alternate-domain-names-move-create-target.md "alternate-domain-names-move-create-target.md").

    **Request**

    ```
    aws cloudfront associate-alias \
    --alias `www.example.com` \
    --target-distribution-id `EDFDVBD6EXAMPLE`
    ```

    This command removes the alternate domain name from the
    source standard distribution and moves it to the target
    standard distribution.

2.  After the target standard distribution is fully deployed, update your DNS
    configuration to point the alternate domain name’s DNS record to the
    distribution domain name of the target standard distribution. For example, your
    DNS record would point your alternate domain name
    (`www.example.com`) to the CloudFront provided domain name
    d111111abcdef8.cloudfront.net.

For more information, see the [associate-alias](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudfront/associate-alias.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudfront/associate-alias.html") command in the
_AWS CLI Command Reference_.

## Use a wildcard to move an

alternate domain name

If the source distribution is in a different AWS account than the target
distribution, and the source distribution is enabled, you can use a wildcard to move
the alternate domain name.

###### Note

You can’t use a wildcard to move an apex domain (like example.com). To move an
apex domain when the source and target distributions are in different
AWS accounts, contact Support. For more information, see [Contact AWS Support to
move an alternate domain name](#alternate-domain-names-move-contact-support "#alternate-domain-names-move-contact-support").

###### To use a wildcard to move an alternate domain name

###### Note

This process involves multiple updates to your distributions. Wait for
each distribution to fully deploy the latest change before proceeding to the
next step.

1. Update the target distribution to add a wildcard alternate domain name
   that covers the alternate domain name that you are moving. For example, if
   the alternate domain name that you’re moving is www.example.com, add the
   alternate domain name \*.example.com to the target distribution. To do this,
   the SSL/TLS certificate on the target distribution must include the wildcard
   domain name. For more information, see [Update a distribution](HowToUpdateDistribution.md "HowToUpdateDistribution.md").
2. Update the DNS settings for the alternate domain name to point to the
   domain name of the target distribution. For example, if the alternate domain
   name that you’re moving is www.example.com, update the DNS record for
   www.example.com to route traffic to the domain name of the target
   distribution (for example d111111abcdef8.cloudfront.net).

###### Note

Even after you update the DNS settings, the alternate domain name is
still served by the source distribution because that’s where the
alternate domain name is currently configured. 3. Update the source distribution to remove the alternate domain name. For
more information, see [Update a distribution](HowToUpdateDistribution.md "HowToUpdateDistribution.md"). 4. Update the target distribution to add the alternate domain name. For more
information, see [Update a distribution](HowToUpdateDistribution.md "HowToUpdateDistribution.md"). 5. Use **dig** (or a similar DNS query tool) to validate that
the DNS record for the alternate domain name resolves to the domain name of
the target distribution. 6. (Optional) Update the target distribution to remove the wildcard alternate
domain name.

## Contact AWS Support to

move an alternate domain name

If the source and target distributions are in different AWS accounts, and you
don’t have access to the source distribution’s AWS account or can’t disable the
source distribution, you can contact Support to move the alternate domain name.

###### To contact Support to move an alternate domain name

1. Set up a target distribution, including the DNS TXT record that points to
   the target distribution. For more information, see [Set up the target
   standard distribution or distribution tenant](alternate-domain-names-move-create-target.md "alternate-domain-names-move-create-target.md").
2. [Contact Support](https://console.aws.amazon.com/support/home "https://console.aws.amazon.com/support/home") to request
   that they verify that you own the domain, and move the domain to the new
   CloudFront distribution for you.
3. After the target distribution is fully deployed, update your DNS
   configuration to point the alternate domain name’s DNS record to the
   distribution domain name of the target distribution.
