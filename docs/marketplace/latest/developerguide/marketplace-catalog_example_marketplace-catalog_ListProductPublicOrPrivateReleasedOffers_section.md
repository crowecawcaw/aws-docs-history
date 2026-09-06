

The AWS Marketplace API Reference was restructured. For more information about the supported API operations, see the [AWS Marketplace API Reference](https://docs.aws.amazon.com/marketplace/latest/APIReference/Welcome.html).

# List released public and private offers for a specific product ID using an AWS SDK
<a name="marketplace-catalog_example_marketplace-catalog_ListProductPublicOrPrivateReleasedOffers_section"></a>

The following code example shows how to list released public and private offers for a specific product ID.

------
#### [ Java ]

**SDK for Java 2.x**  
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Marketplace API Reference Code Library](https://github.com/aws-samples/aws-marketplace-reference-code/tree/main/java#catalog-api-reference-code) repository. 

```
package com.example.awsmarketplace.catalogapi;

import java.util.ArrayList;
import java.util.List;

import static com.example.awsmarketplace.utils.ReferenceCodesConstants.*;
import com.example.awsmarketplace.utils.ReferenceCodesUtils;

import software.amazon.awssdk.auth.credentials.ProfileCredentialsProvider;
import software.amazon.awssdk.http.apache.ApacheHttpClient;
import software.amazon.awssdk.services.marketplacecatalog.MarketplaceCatalogClient;
import software.amazon.awssdk.services.marketplacecatalog.model.EntitySummary;
import software.amazon.awssdk.services.marketplacecatalog.model.EntityTypeFilters;
import software.amazon.awssdk.services.marketplacecatalog.model.ListEntitiesRequest;
import software.amazon.awssdk.services.marketplacecatalog.model.ListEntitiesResponse;
import software.amazon.awssdk.services.marketplacecatalog.model.OfferFilters;
import software.amazon.awssdk.services.marketplacecatalog.model.OfferProductIdFilter;
import software.amazon.awssdk.services.marketplacecatalog.model.OfferStateFilter;
import software.amazon.awssdk.services.marketplacecatalog.model.OfferTargetingFilter;

public class ListProductPublicOrPrivateReleasedOffers {

	/*
	 * List released Public/Private offers for a specific product id.
	 * Example below is to list released public offers.
	 * To change to released private offers, change OFFER_TARGETING_NONE (None) to OFFER_TARGETING_BUYERACCOUNTS(BuyerAccounts)
	 */
	public static void main(String[] args) {

		List<EntitySummary> entitySummaryList = getEntitySummaryLIst();
		ReferenceCodesUtils.formatOutput(entitySummaryList);
	}

	public static List<EntitySummary> getEntitySummaryLIst() {
		MarketplaceCatalogClient marketplaceCatalogClient = 
				MarketplaceCatalogClient.builder()
				.httpClient(ApacheHttpClient.builder().build())
				.credentialsProvider(ProfileCredentialsProvider.create())
				.build();
		
		// define list entities filters
		
		EntityTypeFilters entityTypeFilters = 
				EntityTypeFilters.builder()
				.offerFilters(OfferFilters.builder()
						.targeting(OfferTargetingFilter.builder()
								.valueListWithStrings(OFFER_TARGETING_NONE)
								.build())
						.state(OfferStateFilter.builder()
								.valueListWithStrings(OFFER_STATE_RELEASED)
								.build())
						.productId(OfferProductIdFilter.builder()
								.valueList(PRODUCT_ID)
								.build())
						.build())
				.build();
		
		ListEntitiesRequest listEntitiesRequest = 
				ListEntitiesRequest.builder()
				.catalog(AWS_MP_CATALOG)
				.entityType(ENTITY_TYPE_OFFER)
				.maxResults(10)
				.entityTypeFilters(entityTypeFilters)
				.nextToken(null)
				.build();
		
		ListEntitiesResponse listEntitiesResponse = marketplaceCatalogClient.listEntities(listEntitiesRequest);
		
		// save all entitySummary of the results into entitySummaryList
		
		List<EntitySummary> entitySummaryList = new ArrayList<EntitySummary>();
		
		entitySummaryList.addAll(listEntitiesResponse.entitySummaryList());
		
		while ( listEntitiesResponse.nextToken() != null && listEntitiesResponse.nextToken().length() > 0) {
			listEntitiesRequest = 
					ListEntitiesRequest.builder()
					.catalog(AWS_MP_CATALOG)
					.entityType(ENTITY_TYPE_OFFER)
					.maxResults(10)
					.entityTypeFilters(entityTypeFilters)
					.nextToken(listEntitiesResponse.nextToken())
					.build();
			listEntitiesResponse = marketplaceCatalogClient.listEntities(listEntitiesRequest);
			entitySummaryList.addAll(listEntitiesResponse.entitySummaryList());
		}
		return entitySummaryList;
	}

}
```
+  For API details, see [StartChangeSet](https://docs.aws.amazon.com/goto/SdkForJavaV2/marketplace-catalog-2018-09-17/StartChangeSet) in *AWS SDK for Java 2.x API Reference*. 

------

For a complete list of AWS SDK developer guides and code examples, see [Using this service with an AWS SDK](sdk-general-information-section.md). This topic also includes information about getting started and details about previous SDK versions.