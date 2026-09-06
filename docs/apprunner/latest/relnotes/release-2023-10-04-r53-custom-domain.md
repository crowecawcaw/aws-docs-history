

AWS App Runner will no longer be open to new customers starting April 30, 2026. If you would like to use App Runner, sign up prior to that date. Existing customers can continue to use the service as normal. For more information, see [AWS App Runner availability change](https://docs.aws.amazon.com/apprunner/latest/dg/apprunner-availability-change.html).

# Release: App Runner automates Route 53 domain configuration for your services on October 4, 2023
<a name="release-2023-10-04-r53-custom-domain"></a>

AWS App Runner automates Route 53 domain configuration for your App Runner service web applications.

**Release date:** October 4, 2023

## Changes
<a name="release-2023-10-04-r53-custom-domain.changes"></a>

AWS App Runner now supports automatic configuration for your Amazon Route 53 domains to point to your App Runner service web applications.

You no longer have to copy and paste any information from the App Runner console to your Route 53 domain. With just a few clicks from the **Custom domains** tab on your service dashboard page, you can select from your account's available Amazon Route 53 domain names. Then App Runner automatically configures the Route 53 domain with the required certificate validation and DNS records to link to your App Runner web application.

For more information, see [Managing custom domain names for an App Runner service](https://docs.aws.amazon.com/apprunner/latest/dg/manage-custom-domains.html) in the *AWS App Runner Developer Guide*.