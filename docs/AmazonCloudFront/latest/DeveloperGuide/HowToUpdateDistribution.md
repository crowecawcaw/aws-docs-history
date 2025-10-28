# Update a distribution

In the CloudFront console, you can see the CloudFront distributions that are associated with your
AWS account, view the settings for a distribution, and update most settings. Be aware that
settings changes that you make won't take effect until the distribution has propagated to the
AWS edge locations.

## Update a distribution in the console

The following procedures show you how to update a CloudFront distribution in the console.

Multi-tenant

###### To update a multi-tenant distribution

1. Sign in to the AWS Management Console and open the CloudFront console at
   [https://console.aws.amazon.com/cloudfront/v4/home](https://console.aws.amazon.com/cloudfront/v4/home "https://console.aws.amazon.com/cloudfront/v4/home").
2. Search for and choose the ID of the multi-tenant distribution.
3. Choose the tab for the settings you want to update.
4. Make the updates, and then, to save your changes, choose **Save changes**. For more information
   about the settings you can update, see [Preconfigured distribution settings reference](template-preconfigured-origin-settings.md "template-preconfigured-origin-settings.md").

You can also update a distribution by using the CloudFront API:

- To update a distribution, see [UpdateDistribution](../../../cloudfront/latest/APIReference/API_UpdateDistribution.md "../../../cloudfront/latest/APIReference/API_UpdateDistribution.md")
  in the _Amazon CloudFront API Reference_.

###### Important

When you update your distribution, be aware that a number of additional fields are required that are
not required when you first create a distribution. To help make sure
that all of the required fields are included when you use the CloudFront API to update a distribution, follow the steps described
in [UpdateDistribution](../../../cloudfront/latest/APIReference/API_UpdateDistribution.md "../../../cloudfront/latest/APIReference/API_UpdateDistribution.md")
in the _Amazon CloudFront API Reference_.

To change the multi-tenant distribution for a distribution tenant, you update the distribution tenant. You also update the distribution tenant to update its domain, certificate, customizations, or parameter values. For more details about updating the distribution tenant certificate, see [Add a domain and certificate
(distribution tenant)](managed-cloudfront-certificates.md#vanity-domain-tls-tenant "managed-cloudfront-certificates.md#vanity-domain-tls-tenant").

###### To update a distribution tenant

1. Sign in to the AWS Management Console and open the CloudFront console at
   [https://console.aws.amazon.com/cloudfront/v4/home](https://console.aws.amazon.com/cloudfront/v4/home "https://console.aws.amazon.com/cloudfront/v4/home").
2. Under **SaaS**, choose **Distribution tenants**.
3. Search for the distribution tenant. Use the dropdown menu in the search bar to filter by domain, name, distribution ID, certificate ID, connection group ID, or web ACL ID.
4. Choose the distribution tenant's name.
5. To update general **Details**, choose **Edit**, make the updates, and choose **Update distribution tenant**.
6. Choose the appropriate tab for any other settings to update, make your updates, and save them. For more information about the distribution tenant settings you can customize, see [Distribution tenant customizations](tenant-customization.md "tenant-customization.md").

Standard

###### To update a standard distribution

1. Sign in to the AWS Management Console and open the CloudFront console at
   [https://console.aws.amazon.com/cloudfront/v4/home](https://console.aws.amazon.com/cloudfront/v4/home "https://console.aws.amazon.com/cloudfront/v4/home").
2. Select the ID of a distribution. The list includes all of the distributions associated with the AWS
   account that you used to sign in to the CloudFront console.
3. To update general settings, choose **Edit**. Otherwise, choose the tab
   for the settings that you want to update.
4. Make the updates, and then choose **Save changes**. For information
   about the fields, see the following topics:
   - **General settings:**
     [Distribution settings](DownloadDistValuesGeneral.md "DownloadDistValuesGeneral.md")
   - **Origin settings:**
     [Origin settings](DownloadDistValuesOrigin.md "DownloadDistValuesOrigin.md")
   - **Cache behavior settings:**
     [Cache behavior
     settings](DownloadDistValuesCacheBehavior.md "DownloadDistValuesCacheBehavior.md")

5. If you want to delete an origin in your distribution, do the following:
   1. Choose **Behaviors**, and then make sure you have moved any default cache behaviors associated
      with the origin to another origin.
   2. Choose **Origins**, and then select an origin.
   3. Choose **Delete**.

You can also update a distribution by using the CloudFront API:

- To update a distribution, see [UpdateDistribution](../../../cloudfront/latest/APIReference/API_UpdateDistribution.md "../../../cloudfront/latest/APIReference/API_UpdateDistribution.md")
  in the _Amazon CloudFront API Reference_.

###### Important

When you update your distribution, be aware that a number of additional fields are required that are
not required to create a distribution. To help make sure
that all of the required fields are included when you use the CloudFront API to update a distribution, follow the steps described
in [UpdateDistribution](../../../cloudfront/latest/APIReference/API_UpdateDistribution.md "../../../cloudfront/latest/APIReference/API_UpdateDistribution.md")
in the _Amazon CloudFront API Reference_.

When you save changes to your distribution configuration, CloudFront starts to propagate the
changes to all edge locations. Successive configuration changes propagate in their
respective order. Until your configuration is updated in an edge location, CloudFront
continues to serve your content from that location based on the previous
configuration. After your configuration is updated in an edge location, CloudFront
immediately starts to serve your content from that location based on the new
configuration.

Your changes don't propagate to every edge location at the same time. While CloudFront is propagating your changes, we can't determine
whether a given edge location is serving your content based on the previous
configuration or the new configuration.

###### Note

In rare cases when a host or network link is disrupted, some distribution tenant traffic might be served using older configurations for a brief period until your changes make their way through the network.

To see when your changes are propagated, view your distribution **Details** in the console. The **Last modified** field changes from **Deploying** to a date and time when deployment is complete.
