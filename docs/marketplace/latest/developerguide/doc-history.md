

The AWS Marketplace API Reference was restructured. For more information about the supported API operations, see the [AWS Marketplace API Reference](https://docs.aws.amazon.com/marketplace/latest/APIReference/Welcome.html).

# Document history
<a name="doc-history"></a>

The following table describes the documentation updates for this guide.

| Change | Description | Date | 
| --- |--- |--- |
| [Auto-renewal support in the AWS Marketplace Agreement API](#doc-history) | Documented how buyers turn auto-renewal on and off with the AWS Marketplace Agreement API, including when the preference can still be changed and why turning auto-renewal on does not by itself guarantee that an agreement renews. | August 31, 2026 | 
| [AWS Marketplace Discovery API public launch](#doc-history) | The AWS Marketplace Discovery API is now available. Added 9 API operations: GetListing, GetProduct, GetOffer, GetOfferTerms, GetOfferSet, ListPurchaseOptions, ListFulfillmentOptions, SearchFacets, and SearchListings. Standard AWS SDK support and IAM-based access. | April 8, 2026 | 
| [Updates to ML products](#doc-history) |  Updated seller product machine learning information.  | March 26, 2025 | 
| [CustomerIdentifier](#doc-history) | Added notice of deprecation of CustomerIdentifier in March 2026. | March 25, 2025 | 
| [AWS Marketplace Catalog API topic updates](#doc-history) | Updated CPPO prerequisites. | May 9, 2024 | 
| [AWS Marketplace Catalog API topic updates](#doc-history) | Updated instances of the `Details` attribute to `DetailsDocument`. | April 30, 2024 | 
| [AWS Marketplace Catalog API topic updates](#doc-history) | Added notes to [Working with offers](https://docs.aws.amazon.com/marketplace-catalog/latest/api-reference/offers.html) to clarify constraints. | April 17, 2024 | 
| [AWS Marketplace Catalog API supports service-linked for resale authorization](#doc-history) | Updated resale authorization prerequisites for service-linked role. | March 20, 2024 | 
| [AWS Marketplace Catalog API supports organization units](#doc-history) | Added content to enable private marketplace support at Organization Unit (OU) level. | February 16, 2024 | 
| [AWS Marketplace Catalog API supports setting intent on requests](#doc-history) | Sellers now can request changes for entities with specific intent using the AWS Marketplace Catalog API. | February 9, 2024 | 
| [AWS Marketplace Catalog API supports wildcard filter validation](#doc-history) | Added wildcard filter validation in ListEntities API. | February 5, 2024 | 
| [AWS Marketplace Catalog API supports Amazon EKS add-ons](#doc-history) | Added content and error messages related to publishing to Amazon EKS add-ons from AWS Marketplace container-based product. | January 29, 2024 | 
| [AWS Marketplace Catalog API supports listing details about entities](#doc-history) | Sellers can now list details about entities using the AWS Marketplace Catalog API. | December 19, 2023 | 
| [The AWS Marketplace Deployment Service API reference is now generally available](#doc-history) | This service provides an API interface that supports a secure method for passing deployment parameters (for example, API keys and external IDs) during the Quick Launch experience. | November 29, 2023 | 
| [The AWS Marketplace Agreement Service API reference is now generally available](#doc-history) | This service provides an API interface that helps AWS Marketplace sellers manage their product-related agreements, including listing, searching, and filtering agreements. | November 29, 2023 | 
| [AWS Marketplace Catalog API supports the ability to create products, offers, Resale Authorizations, and CPPOs](#doc-history) | Sellers can now use the AWS Marketplace Catalog API to create and update [products](https://docs.aws.amazon.com/marketplace-catalog/latest/api-reference/seller-products.html), [offers](https://docs.aws.amazon.com/marketplace-catalog/latest/api-reference/offers.html), [Resale Authorizations](https://docs.aws.amazon.com/marketplace-catalog/latest/api-reference/resale-authorizations.html), and [channel partner private offers (CPPOs)](https://docs.aws.amazon.com/marketplace-catalog/latest/api-reference/cppos.html).  | November 29, 2023 | 
| [AWS Marketplace Catalog API supports enhanced filtering and sorting capabilities](#doc-history) | Sellers can now sort and filter products using the AWS Marketplace Catalog API. | November 29, 2023 | 
| [AWS Marketplace Catalog API supports resource sharing](#doc-history) | The AWS Marketplace Catalog API integrates with AWS Resource Access Manager (AWS RAM) to enable resource sharing. See [ Working with AWS RAM to share resources](https://docs.aws.amazon.com/marketplace-catalog/latest/api-reference/resource-sharing-ram.html). | April 12, 2023 | 
| [AWS Marketplace Discovery API topic update](#doc-history) | The AWS Marketplace Discovery API now supports CloudTrail. See [ Logging AWS Marketplace Discovery API calls using AWS CloudTrail](https://docs.aws.amazon.com/marketplace-catalog/latest/api-reference/logging-using-cloudtrail.html). | December 15, 2022 | 
| [AWS Marketplace supports archiving private marketplace experiences](#doc-history) | Buyers can now archive and reactivate private marketplace experiences in AWS Marketplace. See [Working with a private marketplace](https://docs.aws.amazon.com/marketplace-catalog/latest/api-reference/private-marketplace.html). | December 12, 2022 | 
| [AWS Marketplace Private marketplace granular permissions](#doc-history) | Buyers now have more granular permissions to manage private marketplace experiences. See [Working with a private marketplace](https://docs.aws.amazon.com/marketplace-catalog/latest/api-reference/private-marketplace.html). | September 8, 2022 | 
| [AWS Marketplace Discovery API release notes](#doc-history) | Added [Release notes](https://docs.aws.amazon.com/marketplace-catalog/latest/api-reference/discovery-api-release-notes.html) for the AWS Marketplace Discovery API. | May 20, 2022 | 
| [AWS Marketplace Discovery API topic update](#doc-history) | Documentation-only update to the [AWS Marketplace Discovery API topic](https://docs.aws.amazon.com/marketplace-catalog/latest/api-reference/discovery-api.html). | January 14, 2022 | 
| [Support for Helm chart delivery options and QuickLaunch for container-based products](#doc-history) | Added documentation for adding or updating Helm chart delivery options in container-based product versions, including enabling QuickLaunch for buyers. See [Working with container-based products](https://docs.aws.amazon.com/marketplace-catalog/latest/api-reference/container-products.html). | November 29, 2021 | 
| [Support for managing seller products](#doc-history) | Added the ability to manage AMI and container products programmatically. See [Working with seller products](https://docs.aws.amazon.com/marketplace-catalog/latest/api-reference/seller-products.html). | March 26, 2021 | 
| [Support for managing private marketplaces](#doc-history) | Added the ability to create and maintain private marketplaces for AWS Organizations programmatically. See [Working with a private marketplace](https://docs.aws.amazon.com/marketplace-catalog/latest/api-reference/private-marketplace.html). | December 3, 2020 | 
| [The AWS Marketplace Discovery API is now available](#doc-history) | The Discovery API provides programmatic access to find products in the AWS Marketplace. For details, see [Discovery API](https://docs.aws.amazon.com/marketplace-catalog/latest/api-reference/discovery-api.html). | September 30, 2020 | 
| [The AWS Marketplace Catalog API is now generally available](#doc-history) | This service provides an API interface for approved providers to programmatically access the self-service publishing capabilities on the AWS Marketplace Management Portal. | November 12, 2019 | 

## Release notes for AWS Marketplace Discovery API
<a name="discovery-release-notes"></a>

Release notes for AWS Marketplace Discovery API. Details about new features, improvements, fixes, and announcements.



### Discovery API release notes for 2026
<a name="release-notes-2026"></a>

#### April 8, 2026
<a name="april-8-2026"></a>

The AWS Marketplace Discovery API is now publicly available through the standard AWS SDK. The API provides programmatic access to the AWS Marketplace catalog, including searching and browsing listings, retrieving product details and fulfillment options, and accessing public and private offer pricing and terms.

##### Launch announcements
<a name="4-8-launch"></a>
+ 9 API operations available: GetListing, GetProduct, GetOffer, GetOfferTerms, GetOfferSet, ListPurchaseOptions, ListFulfillmentOptions, SearchFacets, and SearchListings.
+ Standard AWS SDK support in all languages (Java, Python, JavaScript, .NET, Go, and others). No private SDK required.
+ IAM-based access control with resource-level permissions. No manual onboarding required.
+ Available in US East (N. Virginia), US West (Oregon), and Europe (Ireland).

### Discovery API release notes for 2024
<a name="release-notes-2024"></a>

#### August 15, 2024
<a name="august-15-2024"></a>

Discovery API customers can access the updated Discovery API documentation and SDK on the Amazon Simple Storage Service bucket provided by the Discovery API team. Customers can refer to the Change Log in the private documentation for more details.

##### Launch announcements
<a name="8-15-launch"></a>

The Discovery API Private SDK is now available in JavaScript V3.
+ For information about using the AWS SDK for JavaScript V3, see the [AWS SDK for JavaScript V3 Developer Guide](https://docs.aws.amazon.com/sdk-for-javascript/v3/developer-guide/welcome.html).
+ For information about migrating from V2 to V3, see [ Migrate from version 2.x to 3.x of the AWS SDK for JavaScript](https://docs.aws.amazon.com/sdk-for-javascript/v3/developer-guide/migrating.html), in the *AWS SDK for JavaScript V3 Developer Guide*.

##### Improvements
<a name="8-15-improvements"></a>
+ AWS SDK paginators are now available for the `SearchListings` and `ListListingViewQueries` API operations in all supported languages that have native SDK support for paginators.

  You can still use `NextToken` to manually paginate. You can use `NextToken` with the `SearchListings`, `ListListingViewQueries`, and `GetSearchFacets` API operations across all the SDKs that we vend.
+ SDK updated for all supported languages with the latest AWS SDK artifacts.
+ Private documentation updated to include an SDK usage section for JavaScript V3.

### Discovery API release notes for 2022
<a name="release-notes-2022"></a>

#### May 20, 2022
<a name="may-20-2022"></a>

Published on May 20, 2022

Discovery API customers can access the updated Discovery API documentation and SDK on the Amazon Simple Storage Service (Amazon S3) bucket that the Discovery API team shared with them previously. Refer to the Change Log in the private documentation for more details.

Discovery API announces the following launch, and improvements:

##### Launch announcements
<a name="may-20-launch-annoucements"></a>
+ Discovery API launched in two additional AWS Regions: 
  + US West (Oregon) – `us-west-2`
  + Europe (Ireland) – `eu-west-1`
+ Discovery API Private SDK is now available in Java 2.x:
  + For more information about how to use the AWS SDK for Java 2.x, see the [AWS SDK for Java 2.x Developer Guide](https://docs.aws.amazon.com/sdk-for-java/v2/developer-guide/welcome.html). 
  + For more information about migration, see [migrating from version 1.x to 2.x of the AWS SDK for Java](https://docs.aws.amazon.com/sdk-for-java/v2/migration-guide/what-is-java-migration.html) in the *AWS SDK for Java 2.x Developer Guide*.
  + For more information about changes between versions 1.11.x and 2.x of the AWS SDK for Java 2.x, see [ 1.11 to 2.x Changelog](https://github.com/aws/aws-sdk-java-v2/blob/master/docs/LaunchChangelog.md) on the GitHub website.

##### Improvements
<a name="may-20-improvements"></a>
+ Enhanced sorting functionality for the `SearchListings` API operation by introducing new options for: 
  + `SortBy` – `AVERAGE_CUSTOMER_RATING`, `CREATION_TIME`, `LAST_MODIFIED_TIME`
  + `SortOrder` – `ASCENDING`
+ SDK updated for all the existing languages with the latest AWS SDK artifacts.
+ Documentation updated to include SDK usage section for all languages.