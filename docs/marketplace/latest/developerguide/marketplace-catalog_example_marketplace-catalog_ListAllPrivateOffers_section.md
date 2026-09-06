

The AWS Marketplace API Reference was restructured. For more information about the supported API operations, see the [AWS Marketplace API Reference](https://docs.aws.amazon.com/marketplace/latest/APIReference/Welcome.html).

# List all private offers using an AWS SDK
<a name="marketplace-catalog_example_marketplace-catalog_ListAllPrivateOffers_section"></a>

The following code examples show how to list all private offers.

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
import software.amazon.awssdk.services.marketplacecatalog.model.DescribeEntityRequest;
import software.amazon.awssdk.services.marketplacecatalog.model.DescribeEntityResponse;
import software.amazon.awssdk.services.marketplacecatalog.model.EntitySummary;
import software.amazon.awssdk.services.marketplacecatalog.model.EntityTypeFilters;
import software.amazon.awssdk.services.marketplacecatalog.model.ListEntitiesRequest;
import software.amazon.awssdk.services.marketplacecatalog.model.ListEntitiesResponse;
import software.amazon.awssdk.services.marketplacecatalog.model.OfferAvailabilityEndDateFilter;
import software.amazon.awssdk.services.marketplacecatalog.model.OfferAvailabilityEndDateFilterDateRange;
import software.amazon.awssdk.services.marketplacecatalog.model.OfferBuyerAccountsFilter;
import software.amazon.awssdk.services.marketplacecatalog.model.OfferFilters;
import software.amazon.awssdk.services.marketplacecatalog.model.OfferReleaseDateFilter;
import software.amazon.awssdk.services.marketplacecatalog.model.OfferReleaseDateFilterDateRange;
import software.amazon.awssdk.services.marketplacecatalog.model.OfferTargetingFilter;

public class ListAllPrivateOffers {

	/*
	 * List all my private offers and sort or filter them by Offer Publish Date, Offer Expiry Date and Buyer IDs
	 * 
	 * OfferTargetingFilter = BuyerAccounts (private offer);
	 * OfferBuyerAccountsFilter: Buyer IDs filter
	 * OfferAvailabilityEndDateFilter : Offer Expiry Date filter
	 * OfferReleaseDateFilter : Offer Publish Date filter
	 */
	
	private static MarketplaceCatalogClient marketplaceCatalogClient = 
			MarketplaceCatalogClient.builder()
			.httpClient(ApacheHttpClient.builder().build())
			.credentialsProvider(ProfileCredentialsProvider.create())
			.build();
	
	public static void main(String[] args) {

		String offerReleaseDateAfterValue = "2023-01-01T23:59:59Z";
		String offerAvailableEndDateAfterValue = "2040-12-24T23:59:59Z";
		
		List<EntitySummary> entitySummaryList = getEntitySummaryList(offerReleaseDateAfterValue, offerAvailableEndDateAfterValue);
		
		// for each offer id, output the offer detail using DescribeEntity API
		
		
		for (EntitySummary entitySummary : entitySummaryList) {
			DescribeEntityRequest describeEntityRequest = 
					DescribeEntityRequest.builder()
					.catalog(AWS_MP_CATALOG)
					.entityId(entitySummary.entityId())
					.build();
			DescribeEntityResponse describeEntityResponse = marketplaceCatalogClient.describeEntity(describeEntityRequest);
			ReferenceCodesUtils.formatOutput(describeEntityResponse);
		}
	}
	
	public static List<EntitySummary> getEntitySummaryList (String offerReleaseDateAfterValue, String offerAvailableEndDateAfterValue) {
		
		EntityTypeFilters entityTypeFilters = 
				EntityTypeFilters.builder()
				.offerFilters(OfferFilters.builder()
						.targeting(OfferTargetingFilter.builder()
								.valueListWithStrings(OFFER_TARGETING_BUYERACCOUNTS)
								.build())
						.buyerAccounts(OfferBuyerAccountsFilter.builder()
								.wildCardValue(BUYER_ACCOUNT_ID)
								.build())
						.availabilityEndDate(OfferAvailabilityEndDateFilter.builder()
								.dateRange(OfferAvailabilityEndDateFilterDateRange.builder()
										.afterValue(offerAvailableEndDateAfterValue).build())
								.build())
						.releaseDate(OfferReleaseDateFilter.builder()
								.dateRange(OfferReleaseDateFilterDateRange.builder()
										.afterValue(offerReleaseDateAfterValue)
										.build())
								.build())
						.build())
				.build();
			
		ListEntitiesRequest listEntitiesRequest = 
				ListEntitiesRequest.builder()
				.catalog(AWS_MP_CATALOG)
				.entityType(ENTITY_TYPE_OFFER).maxResults(10)
				.entityTypeFilters(entityTypeFilters)
				.nextToken(null)
				.build();
		
		ListEntitiesResponse listEntitiesResponse = marketplaceCatalogClient.listEntities(listEntitiesRequest);
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
#### [ Python ]

**SDK for Python (Boto3)**  
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Marketplace API Reference Code Library](https://github.com/aws-samples/aws-marketplace-reference-code/blob/main/python##catalog-api-reference-code) repository. 

```
# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0
"""
Purpose
Shows how to use the AWS SDK for Python (Boto3) for listing offers in the AWS Marketplace Catalog
CAPI-40
"""
import json
import logging

import boto3
from botocore.exceptions import ClientError

logger = logging.getLogger(__name__)

# Constants
MAX_RESULTS = 10
CATALOG = "AWSMarketplace"
ENTITY_TYPE = "Offer"


def pretty_print(response):
    json_object = json.dumps(response, indent=4)
    print(json_object)


def list_private_offers(mp_client, return_all_private_offers):
    """
    This method retrieves list of all Private Offers for this account.
    """
    entity_summary_list = []
    filter_list_param = {
        'OfferFilters': {
            'Targeting': {
                'ValueList': ["BuyerAccounts"]
            }
        }
    }
    try:
        response = mp_client.list_entities(
            Catalog=CATALOG,
            EntityType=ENTITY_TYPE,
            EntityTypeFilters=filter_list_param,
            MaxResults=MAX_RESULTS
        )
    except ClientError as e:
        logger.error("Could not complete list_entities request: %s", e)
        raise

    entity_summary_list.extend(response["EntitySummaryList"])
    logger.info("Number of results in first iteration: %d " % len(entity_summary_list))

    # Get subsequent pages of results if previous response contained a NextToken
    while "NextToken" in response and return_all_private_offers:
        try:
            logger.info("Getting Next Token results: %s " % response["NextToken"])
            response = mp_client.list_entities(
                Catalog=CATALOG,
                EntityType=ENTITY_TYPE,
                EntityTypeFilters=filter_list_param,
                MaxResults=MAX_RESULTS,
                NextToken=response["NextToken"]
            )
        except ClientError as e:
            logger.error("Could not complete list_entities request: %s", e)
            raise

        entity_summary_list.extend(response["EntitySummaryList"])
        logger.info(
            "Number of results in the current iteration: %d "
            % len(response["EntitySummaryList"])
        )

    return entity_summary_list


def get_offer_details(mp_client, offer):
    """
    Describe the details of the Offer.
    """
    try:
        response = mp_client.describe_entity(
            Catalog="AWSMarketplace", EntityId=offer["EntityId"]
        )

        return response
    except ClientError:
        logger.exception("Error: Couldn't get details of the Offer.")
        raise


def usage_demo():
    logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

    print("-" * 88)
    print("Demo  - List Private offers.")
    print("-" * 88)

    mp_client = boto3.client("marketplace-catalog")

    # Get list of all Offers.
    private_offers = list_private_offers(mp_client, False)
    count = len(private_offers)

    logger.info("Number of Offers: %d " % count)
    offer_counter = 0
    # Display details of each Offer.
    for offer in private_offers:
        print("-" * 88)
        offer_counter += 1
        print("Displaying Offer details for Offer# %d" % offer_counter)
        entity = get_offer_details(mp_client, offer)
        pretty_print(entity)

    print("-" * 88)


if __name__ == "__main__":
    usage_demo()
```
+  For API details, see [StartChangeSet](https://docs.aws.amazon.com/goto/boto3/marketplace-catalog-2018-09-17/StartChangeSet) in *AWS SDK for Python (Boto3) API Reference*. 

------

For a complete list of AWS SDK developer guides and code examples, see [Using this service with an AWS SDK](sdk-general-information-section.md). This topic also includes information about getting started and details about previous SDK versions.