# Migrate to a multi-tenant distribution

If you have a CloudFront standard distribution and you want to migrate to a multi-tenant distribution, follow these steps.

###### To migrate from a standard distribution to a multi-tenant distribution

1. Review the [Unsupported features](distribution-config-options.md#unsupported-saas "distribution-config-options.md#unsupported-saas").
2. Create a multi-tenant distribution with the same configuration as your standard distribution, minus the
 unsupported features. For more information, see [Create a CloudFront distribution in the console](distribution-web-creating-console.md#create-console-distribution "distribution-web-creating-console.md#create-console-distribution").
3. Create a distribution tenant and add an alternative domain name that you own.


###### Warning

Do *not* use the current domain name that's associated with
 your standard distribution. Add a placeholder domain instead. You will move your domain over
 later. For more information about creating a distribution tenant, see [Create a CloudFront distribution in the console](distribution-web-creating-console.md#create-console-distribution "distribution-web-creating-console.md#create-console-distribution").
4. Provide an existing certificate for the distribution tenant domain. This is the certificate
 that will cover the placeholder domain and the domain that you want to move.
5. Copy the CloudFront routing endpoint from the distribution tenant detail page in the console.
 Alternatively, find it by using the [ListConnectionGroups](../../../cloudfront/latest/APIReference/API_ListConnectionGroups.md "../../../cloudfront/latest/APIReference/API_ListConnectionGroups.md") API action in the *Amazon CloudFront API
 Reference*.
6. To verify domain ownership, create a DCV TXT record with an underscore ( \_ )
 prefix that points to the CloudFront routing endpoint for your distribution tenant. For more
 information, see [Point domains to CloudFront](managed-cloudfront-certificates.md#point-domains-to-cloudfront "managed-cloudfront-certificates.md#point-domains-to-cloudfront").
7. When your changes have propagated, update your distribution tenant to use the domain that you
 previously used for your standard distribution. 




	* **Console** – For detailed
	 instructions, see [Add a domain and certificate
	 (distribution tenant)](managed-cloudfront-certificates.md#vanity-domain-tls-tenant "managed-cloudfront-certificates.md#vanity-domain-tls-tenant").
	* **API** – Use the [UpdateDomainAssociation](../../../cloudfront/latest/APIReference/API_UpdateDomainAssociation.md "../../../cloudfront/latest/APIReference/API_UpdateDomainAssociation.md") API action in the *Amazon CloudFront
	 API Reference*.
###### Important

This resets the cache key for your content. After this, CloudFront starts caching
 your content using the new cache key. For more information, see [Understand the cache key](understanding-the-cache-key.md "understanding-the-cache-key.md").
8. Update your DNS record to point your domain to the CloudFront routing endpoint for your
 distribution tenant. Once you complete this step, your domain will be ready to serve traffic
 to your distribution tenant. For more information, see [Point domains to CloudFront](managed-cloudfront-certificates.md#point-domains-to-cloudfront "managed-cloudfront-certificates.md#point-domains-to-cloudfront").
9. (Optional) After you successfully migrate your domain to a distribution tenant, you can use a
 different CloudFront managed certificate that covers the domain name for your distribution tenant. To
 request a managed certificate, create a separate TXT record to issue the certificate
 and follow the steps here in [Complete domain setup](managed-cloudfront-certificates.md#complete-domain-ownership "managed-cloudfront-certificates.md#complete-domain-ownership").
